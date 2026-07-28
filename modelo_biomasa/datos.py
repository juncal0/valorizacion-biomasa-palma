"""
modelo_biomasa.datos
=====================
Extraído del notebook 01_notebook_v3_CAPEX_corregido.ipynb, Secciones 1-6.

Contiene la limpieza de las hojas del archivo Escenarios.xlsx:
  - Datos_Base (parámetros de línea base por planta y etapa)
  - Biomass (propiedades fisicoquímicas, HHV/LHV)
  - CAPEX (costos por área, curva de cogeneración, pretratamiento térmico)
  - EmisionesCO2 (factores de emisión)
  - Módulo social (indicadores de cobertura rural)
  - Eficiencia (demanda energética por etapa, línea base)

IMPORTANTE: esta lógica ya fue validada y usada para el manuscrito. No se debe
modificar sin re-ejecutar y cruzar contra el resultado central confirmado
(ver Estado_proyecto_continuidad.md). Cualquier cambio debe documentarse en
las notas metodológicas.
"""

import json

import numpy as np
import pandas as pd

PLANTAS_DEFAULT = ['Planta A', 'Planta B', 'Planta C', 'Planta D', 'Planta E', 'Planta F']

# ---------------------------------------------------------------------------
# Sección 1 — Datos_Base
# ---------------------------------------------------------------------------

def cargar_datos_base(ruta_excel='Escenarios.xlsx', verbose=True):
    """Limpia la hoja 'Datos_Base': tidy format, corrección de \\xa0, tipos numéricos.

    Retorna
    -------
    df_datos_base : pd.DataFrame  columnas [Parametro, Unidad, Etapa, Planta, Valor]
    plantas : list[str]  nombres de planta en el orden del Excel
    """
    raw = pd.read_excel(ruta_excel, sheet_name='Datos_Base', header=None, usecols='A:H')
    plantas = raw.iloc[1, 2:8].tolist()

    df_datos = raw.iloc[2:].copy()
    df_datos.columns = ['Parametro', 'Unidad'] + plantas
    df_datos = df_datos.reset_index(drop=True)

    # Identificar encabezados de etapa (sin unidad y sin ningún valor en las 6 plantas)
    is_header = df_datos['Parametro'].notna() & df_datos['Unidad'].isna() & df_datos[plantas].isna().all(axis=1)
    df_datos['Etapa'] = df_datos['Parametro'].where(is_header).ffill()
    df_datos = df_datos[~is_header].reset_index(drop=True)

    # Rellenar nombre de parámetro para las filas "huérfanas" (valor específico por tRFF)
    df_datos['Parametro'] = df_datos['Parametro'].ffill()
    dup_mask = df_datos.duplicated(subset=['Etapa', 'Parametro'], keep='first')
    df_datos.loc[dup_mask, 'Parametro'] = df_datos.loc[dup_mask, 'Parametro'] + ' (específico por tRFF)'
    df_datos.loc[dup_mask, 'Unidad'] = df_datos.loc[dup_mask, 'Unidad'].fillna('por tRFF procesado')

    # Formato tidy
    df_tidy = df_datos.melt(id_vars=['Parametro', 'Unidad', 'Etapa'], var_name='Planta', value_name='Valor')
    df_tidy['Etapa'] = df_tidy['Etapa'].fillna('General')

    # Limpiar espacios invisibles (\xa0) y forzar tipo numérico
    df_tidy['Valor'] = df_tidy['Valor'].apply(lambda v: str(v).replace('\xa0', '').strip() if isinstance(v, str) else v)
    df_tidy['Valor'] = pd.to_numeric(df_tidy['Valor'], errors='coerce')

    # Separar filas con dato realmente faltante (para no perderlas silenciosamente)
    faltantes = df_tidy[df_tidy['Valor'].isna() & (df_tidy['Etapa'] != 'General')]
    df_tidy = df_tidy.dropna(subset=['Valor']).reset_index(drop=True)

    if verbose:
        print("Filas con dato faltante en el Excel original:")
        print(faltantes[['Parametro', 'Unidad', 'Etapa']].drop_duplicates())

    # Corregir unidad de "Humedad de secado" (error de tecleo en el Excel original: °C -> %)
    df_tidy.loc[df_tidy['Parametro'] == 'Humedad de secado', 'Unidad'] = '%'

    # Agregar de vuelta "Flujo de aire de secado" como dato pendiente explícito (NaN documentado)
    fila_pendiente = pd.DataFrame({
        'Parametro': ['Flujo de aire de secado'] * len(plantas),
        'Unidad': ['kgaire seco∙h-1'] * len(plantas),
        'Etapa': ['Secado de nueces'] * len(plantas),
        'Planta': plantas,
        'Valor': [np.nan] * len(plantas)
    })

    # Separar eficiencias reportadas (no se usan como dato de entrada - se recalculan desde cero)
    es_eficiencia = df_tidy['Parametro'].str.contains('Eficiencia', case=False, na=False)
    df_datos_base = df_tidy[~es_eficiencia].reset_index(drop=True)
    df_datos_base = pd.concat([df_datos_base, fila_pendiente], ignore_index=True)

    if verbose:
        print("\ndf_datos_base listo:", df_datos_base.shape)
        verificacion = df_datos_base[
            (df_datos_base['Parametro'].isin(['Presión de vapor', 'Temperatura de vapor',
                                                'Temperatura agua de alimentación', 'Flujo de vapor'])) &
            (df_datos_base['Planta'] == 'Planta A')
        ]
        print("\nVerificación Planta A:")
        print(verificacion)

    return df_datos_base, plantas


# ---------------------------------------------------------------------------
# Sección 2 — Biomass (propiedades fisicoquímicas, HHV/LHV)
# ---------------------------------------------------------------------------

L_VAPORIZACION_AGUA = 2440  # kJ/kg, calor latente de vaporización del agua (25°C, valor estándar)


def hhv_present_study(C, H, O, N, S):
    """C, H, O, N, S en % base seca (dry basis). Retorna HHV en MJ/kg. (Eq. 7, 'Present study')."""
    return 0.3443 * C + 1.192 * H - 0.113 * O - 0.024 * N + 0.093 * S


def _lhv_corregido_kJkg(df_wide, material):
    """LHV corregido con la fórmula estándar de ingeniería de biomasa.
    Corrige un error de unidades del Excel original (factor de calor latente
    ~1000x menor al valor físico)."""
    fila = df_wide[df_wide['Material'] == material].iloc[0]
    hhv_seco = fila['HHV']
    H_seco = fila['H']
    w = fila['Moisture']
    return hhv_seco * (1 - w) - L_VAPORIZACION_AGUA * (w + 9 * H_seco * (1 - w))


def cargar_biomasa(ruta_excel='Escenarios.xlsx', verbose=True):
    """Limpia la hoja 'Biomass': propiedades, calor específico, HHV/LHV corregido.

    Retorna
    -------
    df_biomasa : pd.DataFrame  (LHV ya corregido)
    df_calor_especifico : pd.DataFrame
    df_wide : pd.DataFrame  (propiedades en formato ancho, usado en Sección 10/11 para
              composición elemental C/H/O/N/S — necesario para balances estequiométricos
              de combustión; NO usar los valores de HHV/LHV de aquí, esos ya están
              corregidos en df_biomasa)
    """
    raw = pd.read_excel(ruta_excel, sheet_name='Biomass', header=None)

    materiales = raw.iloc[4, 2:12:2].tolist()
    propiedades = raw.iloc[7:15, 0].tolist()
    unidades = raw.iloc[7:15, 1].ffill().tolist()

    registros = []
    for i, mat in enumerate(materiales):
        col_avg = 2 + i * 2
        col_std = 3 + i * 2
        for j, fila_excel in enumerate(range(7, 15)):
            registros.append({
                'Material': mat,
                'Propiedad': propiedades[j],
                'Unidad': unidades[j],
                'Promedio': raw.iloc[fila_excel, col_avg],
                'Desviacion_std': raw.iloc[fila_excel, col_std]
            })

    df_biomasa = pd.DataFrame(registros)
    if verbose:
        print("df_biomasa listo:", df_biomasa.shape)

    df_calor_especifico = pd.DataFrame({
        'Material': ['Water', 'Nut shell', 'Kernel', 'Palm oil', 'Fiber', 'EFB', 'Mud, etc.'],
        'Peso_pct': [15, 6.8, 5.2, 23.5, 14.0, 22.0, 12],
        'Cp_kJ_kgK': [4.18, 1.88, 1.59, 1.46, 1.80, 1.67, 2.22]
    })

    # Validación cruzada HHV + corrección LHV
    df_wide = df_biomasa.pivot_table(index='Material', columns='Propiedad', values='Promedio').reset_index()
    df_wide['HHV_calculado_MJkg'] = df_wide.apply(
        lambda row: hhv_present_study(row['C'] * 100, row['H'] * 100, row['O'] * 100, row['N'] * 100, row['S'] * 100),
        axis=1
    )
    df_wide['HHV_reportado_MJkg'] = df_wide['HHV'] / 1000

    if verbose:
        print(df_wide[['Material', 'HHV_calculado_MJkg', 'HHV_reportado_MJkg']])
        print("\nComparación LHV original (Excel) vs. corregido:")

    for material in df_biomasa['Material'].unique():
        original = df_biomasa[(df_biomasa['Material'] == material) & (df_biomasa['Propiedad'] == 'LHV')]['Promedio'].iloc[0]
        corregido = _lhv_corregido_kJkg(df_wide, material)
        if verbose:
            print(f"{material}: original={original:,.1f} kJ/kg | corregido={corregido:,.1f} kJ/kg | "
                  f"diferencia={100 * (original - corregido) / corregido:.1f}%")
        df_biomasa.loc[(df_biomasa['Material'] == material) & (df_biomasa['Propiedad'] == 'LHV'), 'Promedio'] = corregido

    return df_biomasa, df_calor_especifico, df_wide


# ---------------------------------------------------------------------------
# Sección 3 — CAPEX
# ---------------------------------------------------------------------------

CEPCI_2019 = 607.5
CEPCI_2021 = 708.8
CEPCI_2026 = 873.8  # estimado, ver nota metodológica

FACTOR_CEPCI_2019 = CEPCI_2026 / CEPCI_2019
FACTOR_CEPCI_2021 = CEPCI_2026 / CEPCI_2021

COSTO_REF_2021_PRETRATAMIENTO = 1_400_000
COSTO_REF_2026_PRETRATAMIENTO = COSTO_REF_2021_PRETRATAMIENTO * FACTOR_CEPCI_2021
CAPACIDAD_REF_PRETRATAMIENTO = 150_000
N_ESCALA_PRETRATAMIENTO = 0.6


def capex_cogeneracion_usd_kw(capacidad_kw):
    """CAPEX específico (USD/kW) según capacidad instalada. Fuente: Malico et al. (2019).
    Retorna en USD 2026 (ajustado por CEPCI)."""
    valor_2019 = -900.6 * np.log(capacidad_kw) + 10841
    return valor_2019 * FACTOR_CEPCI_2019


def costo_pretratamiento_termico(capacidad_planta_t_ano):
    """Escalamiento de costo de pretratamiento térmico (steam explosion) por regla 6/10."""
    return COSTO_REF_2026_PRETRATAMIENTO * (capacidad_planta_t_ano / CAPACIDAD_REF_PRETRATAMIENTO) ** N_ESCALA_PRETRATAMIENTO


def cargar_capex(df_datos_base, ruta_excel='Escenarios.xlsx', verbose=True):
    """Limpia la hoja 'CAPEX': resumen por área ajustado a USD 2026 (CEPCI).

    Requiere df_datos_base (Sección 1) para el ejemplo de escalamiento de
    pretratamiento térmico por planta.
    """
    raw_capex = pd.read_excel(ruta_excel, sheet_name='CAPEX', header=None)

    registros_capex = []
    for r in range(13, 38):
        area = raw_capex.iloc[r, 6]         # columna G
        total = raw_capex.iloc[r, 9]        # columna J
        especifico = raw_capex.iloc[r, 10]  # columna K
        unidad = raw_capex.iloc[r, 11]      # columna L
        if pd.notna(area):
            registros_capex.append({
                'Area': area,
                'Total_USD_ref': pd.to_numeric(total, errors='coerce'),
                'Valor_especifico': pd.to_numeric(especifico, errors='coerce'),
                'Unidad_especifico': unidad
            })

    df_capex = pd.DataFrame(registros_capex)
    df_capex['Total_USD_2026'] = df_capex['Total_USD_ref'] * FACTOR_CEPCI_2019
    df_capex['Valor_especifico_2026'] = df_capex['Valor_especifico'] * FACTOR_CEPCI_2019

    if verbose:
        print("df_capex:")
        print(df_capex)
        print(df_capex[['Area', 'Total_USD_2026', 'Valor_especifico_2026']])
        print("\nEjemplo curva cogeneración (1500 kW):", capex_cogeneracion_usd_kw(1500))
        print(f"\nCosto de referencia ajustado a 2026: ${COSTO_REF_2026_PRETRATAMIENTO:,.0f} USD")
        fruto_procesado = df_datos_base[df_datos_base['Parametro'] == 'Fruto procesado'].set_index('Planta')['Valor']
        for planta, tRFF_ano in fruto_procesado.items():
            costo = costo_pretratamiento_termico(tRFF_ano)
            print(f"{planta}: {tRFF_ano:,.0f} tRFF/año -> ${costo:,.0f} USD (2026)")

    return df_capex


# ---------------------------------------------------------------------------
# Sección 4 — EmisionesCO2
# ---------------------------------------------------------------------------

FACTOR_CO2_DIESEL = 74100          # kg CO2/TJ (IPCC 2006, validado contra hoja original)
FACTOR_RED_NACIONAL = 0.1634       # kg CO2/kWh (163.4 gCO2/kWh - valor usado en publicación previa)
FACTOR_ABSORCION_PALMA = -135.04   # kg CO2/tRFF (crédito por absorción, cultivo de palma)


def construir_factores_emision():
    """Tabla de factores de emisión (Gómez et al., 2017 - valores IPCC por defecto)."""
    return pd.DataFrame({
        'Gas': ['CH4', 'CH4', 'N2O', 'N2O'],
        'Fuente': ['Biomasa sólida', 'Biogás', 'Biomasa sólida', 'Biogás'],
        'Factor_kg_TJ': [30, 1, 4, 0.1],
        'GWP100_kgCO2eq_kg': [21, 21, 310, 310]
    })


def emisiones_no_co2_biomasa(energia_TJ, fuente='Biomasa sólida', df_factores_emision=None):
    """Emisiones de CH4 y N2O (no-CO2), en kg CO2-eq. El CO2 biogénico no se contabiliza (convención IPCC).

    df_factores_emision es opcional (se reconstruye internamente si no se pasa) para mantener
    compatibilidad con las llamadas existentes en el notebook, que solo pasan (energia_TJ, fuente=...).
    """
    if df_factores_emision is None:
        df_factores_emision = construir_factores_emision()
    fila_ch4 = df_factores_emision[(df_factores_emision['Gas'] == 'CH4') & (df_factores_emision['Fuente'] == fuente)].iloc[0]
    fila_n2o = df_factores_emision[(df_factores_emision['Gas'] == 'N2O') & (df_factores_emision['Fuente'] == fuente)].iloc[0]
    ch4_eq = energia_TJ * fila_ch4['Factor_kg_TJ'] * fila_ch4['GWP100_kgCO2eq_kg']
    n2o_eq = energia_TJ * fila_n2o['Factor_kg_TJ'] * fila_n2o['GWP100_kgCO2eq_kg']
    return ch4_eq + n2o_eq


def emisiones_diesel(energia_TJ):
    return energia_TJ * FACTOR_CO2_DIESEL


def emisiones_red_nacional(electricidad_kWh):
    return electricidad_kWh * FACTOR_RED_NACIONAL


def balance_neto_GEI(emisiones_proceso_kgCO2eq, tRFF_procesado):
    credito_absorcion = FACTOR_ABSORCION_PALMA * tRFF_procesado
    return emisiones_proceso_kgCO2eq + credito_absorcion


def excedente_electrico(electricidad_generada_kWh, electricidad_consumida_kWh):
    return electricidad_generada_kWh - electricidad_consumida_kWh


# ---------------------------------------------------------------------------
# Sección 5 — Módulo social
# ---------------------------------------------------------------------------

DEMANDA_RESIDENCIAL_RURAL_GWh = 30.3
DEMANDA_RESIDENCIAL_URBANA_GWh = 1209
DEMANDA_INDUSTRIAL_COMERCIO_GWh = 1190.7
DEMANDA_TOTAL_DEPARTAMENTAL_GWh = 2430  # validado: suma de las 3 anteriores

USUARIOS_RURALES = 87516
USUARIOS_URBANOS = 231790
USUARIOS_TOTAL_DANE_CNPV2018 = 319306  # validado contra fuente DANE

PERSONAS_POR_HOGAR_MAGDALENA = 3.7  # DANE, CNPV 2018 (promedio departamental)

CONSUMO_PROMEDIO_VIVIENDA_RURAL_kWh = (DEMANDA_RESIDENCIAL_RURAL_GWh * 1_000_000) / USUARIOS_RURALES
CONSUMO_PROMEDIO_VIVIENDA_URBANA_kWh = (DEMANDA_RESIDENCIAL_URBANA_GWh * 1_000_000) / USUARIOS_URBANOS


def viviendas_rurales_beneficiadas(excedente_electrico_kWh_ano):
    return excedente_electrico_kWh_ano / CONSUMO_PROMEDIO_VIVIENDA_RURAL_kWh


def personas_rurales_beneficiadas(excedente_electrico_kWh_ano):
    return viviendas_rurales_beneficiadas(excedente_electrico_kWh_ano) * PERSONAS_POR_HOGAR_MAGDALENA


def porcentaje_cobertura_rural_departamental(excedente_electrico_kWh_ano):
    return (excedente_electrico_kWh_ano / (DEMANDA_RESIDENCIAL_RURAL_GWh * 1_000_000)) * 100


def construir_tabla_impacto_social(excedentes_dict, nombre_escenario):
    """excedentes_dict: {'Planta A': excedente_kWh_ano, ...}
    nombre_escenario: 'Linea_Base', 'Escenario_1_Termico', 'Escenario_2_Biogas'"""
    registros = []
    for planta, excedente in excedentes_dict.items():
        registros.append({
            'Escenario': nombre_escenario,
            'Planta': planta,
            'Excedente_kWh_ano': excedente,
            'Viviendas_rurales_beneficiadas': viviendas_rurales_beneficiadas(excedente),
            'Personas_rurales_beneficiadas': personas_rurales_beneficiadas(excedente),
            'Pct_cobertura_rural_departamental': porcentaje_cobertura_rural_departamental(excedente)
        })
    return pd.DataFrame(registros)


def exportar_datos_sociales(ruta_json='datos_sociales.json'):
    """Guarda las constantes del módulo social a JSON (para reproducir la celda 17 original)."""
    datos_sociales = {
        'demanda_rural_GWh': DEMANDA_RESIDENCIAL_RURAL_GWh,
        'demanda_urbana_GWh': DEMANDA_RESIDENCIAL_URBANA_GWh,
        'usuarios_rurales': USUARIOS_RURALES,
        'usuarios_urbanos': USUARIOS_URBANOS,
        'personas_por_hogar': PERSONAS_POR_HOGAR_MAGDALENA
    }
    with open(ruta_json, 'w') as f:
        json.dump(datos_sociales, f, indent=2)
    return datos_sociales


# ---------------------------------------------------------------------------
# Sección 6 — Eficiencia (demanda energética por etapa, línea base)
# ---------------------------------------------------------------------------

CAPACIDADES_PLANTA_T_H = {'Planta A': 30, 'Planta B': 40, 'Planta C': 30, 'Planta D': 24, 'Planta E': 30, 'Planta F': 20}


def cargar_eficiencia(ruta_excel='Escenarios.xlsx', plantas=None, verbose=True):
    """Limpia la hoja 'Eficiencia': demanda energética (eléctrica/térmica) por etapa y planta.

    Nota de corrección: la columna Eléctrica está en valores específicos (kW por
    t/h de capacidad de planta), no en kW absolutos como sugiere el header
    original del Excel "(kWe)". Verificado por sentido físico (ver docstring
    en el notebook original, Sección 6).
    """
    if plantas is None:
        plantas = PLANTAS_DEFAULT

    raw_efi = pd.read_excel(ruta_excel, sheet_name='Eficiencia', header=None)
    col_inicio = 13  # cada planta ocupa 2 columnas (Eléctrica, Térmica), empieza en columna N

    registros_demanda = []
    for r in range(5, 23):  # filas 6-23 de Excel: 'Recepción' a 'Total'
        etapa = raw_efi.iloc[r, 12]  # columna M
        if pd.isna(etapa):
            continue
        for i, planta in enumerate(plantas):
            col_e = col_inicio + i * 2
            col_t = col_inicio + i * 2 + 1
            valor_e = raw_efi.iloc[r, col_e]
            valor_t = raw_efi.iloc[r, col_t]
            if pd.notna(valor_e):
                registros_demanda.append({'Etapa': etapa, 'Planta': planta, 'Tipo_energia': 'Electrica', 'Valor_kW': valor_e})
            if pd.notna(valor_t):
                registros_demanda.append({'Etapa': etapa, 'Planta': planta, 'Tipo_energia': 'Termica', 'Valor_kW': valor_t})

    df_demanda_por_etapa = pd.DataFrame(registros_demanda)

    df_demanda_por_etapa = df_demanda_por_etapa[
        ~df_demanda_por_etapa['Etapa'].isin(['Total', 'Eficiencia global planta extractora'])
    ].reset_index(drop=True)

    mask_electrica = df_demanda_por_etapa['Tipo_energia'] == 'Electrica'
    df_demanda_por_etapa.loc[mask_electrica, 'Valor_kW'] = df_demanda_por_etapa.loc[mask_electrica].apply(
        lambda row: row['Valor_kW'] * CAPACIDADES_PLANTA_T_H[row['Planta']], axis=1)

    if verbose:
        print("Verificación - consumo eléctrico total por planta (post-corrección):")
        print(df_demanda_por_etapa[df_demanda_por_etapa['Tipo_energia'] == 'Electrica'].groupby('Planta')['Valor_kW'].sum())
        print(df_demanda_por_etapa.shape)

    return df_demanda_por_etapa