"""
modelo_biomasa.parametros_comunes
===================================
Extraído del notebook 02_notebook_v4_modular.ipynb, Secciones 6.1 y 6.4.

Contiene parámetros y funciones usados por AMBOS escenarios:
  - Sustitución tecnológica de proceso (Tabla 10: esterilización continua,
    clarificación dinámica) — Sección 6.1
  - Digestión anaeróbica de POME y BMP de EFB pretratado (Tabla 13) —
    Sección 6.4

IMPORTANTE: estos valores ya fueron validados y usados para el manuscrito.
No modificar sin re-ejecutar y cruzar contra el resultado central confirmado
(ver docs/Notas_metodologicas_articulo.md).
"""

# ---------------------------------------------------------------------------
# Sección 6.1 — Tabla 10: sustitución tecnológica de proceso
# (aplica a Escenarios 1 y 2, reemplaza procesos convencionales de línea base)
# ---------------------------------------------------------------------------

PARAM_ESTERILIZACION_CONTINUA = {
    'consumo_vapor_kg_tRFF': 315,          # confirmado correcto (caso de estudio, hoja Eficiencia)
    'consumo_electricidad_kWh_tRFF': 1.95, # Tabla 10 tesis
    'presion_bar': 1,
    'temperatura_C': 120,
}

PARAM_CLARIFICACION_DINAMICA = {
    'consumo_vapor_kg_tRFF': 0.6,       # Fernández et al. (2016)
    'consumo_electricidad_kWh_tRFF': 1.5,
    'consumo_agua_L_tRFF': 90,
}

# Capacidad nominal de cada planta (tRFF/h) — Sección 6
CAPACIDADES_PLANTA_T_H = {
    'Planta A': 30, 'Planta B': 40, 'Planta C': 30,
    'Planta D': 24, 'Planta E': 30, 'Planta F': 20,
}


def vapor_esterilizacion_continua(capacidad_planta_tRFF_h):
    """Vapor requerido para esterilización continua (kg/h), escalado por capacidad de planta."""
    return PARAM_ESTERILIZACION_CONTINUA['consumo_vapor_kg_tRFF'] * capacidad_planta_tRFF_h


def kW_termico_tecnologia_nueva(vapor_kg_tRFF, P_bar, T_vapor_C, planta, T_agua_planta,
                                  entalpia_vapor_fn, entalpia_agua_alimentacion_fn,
                                  capacidades=CAPACIDADES_PLANTA_T_H):
    """Demanda térmica (kW) de una tecnología nueva (esterilización continua o
    clarificación dinámica), vía balance de entalpía IAPWS97.

    entalpia_vapor_fn / entalpia_agua_alimentacion_fn: pasar
    modelo_biomasa.termodinamica.entalpia_vapor / entalpia_agua_alimentacion
    (se reciben como parámetro para no crear una dependencia circular de import).
    """
    cap = capacidades[planta]
    m_vapor_kg_h = vapor_kg_tRFF * cap
    h_f = entalpia_vapor_fn(P_bar, T_vapor_C)
    h_i = entalpia_agua_alimentacion_fn(T_agua_planta[planta])
    return m_vapor_kg_h * (h_f - h_i) / 3600  # kW termico


def calcular_ajuste_tecnologico(df_demanda_por_etapa, T_agua_planta,
                                  entalpia_vapor_fn, entalpia_agua_alimentacion_fn,
                                  capacidades=CAPACIDADES_PLANTA_T_H):
    """Ajuste neto de consumo (eléctrico y térmico) por sustitución tecnológica:
    esterilización batch->continua y clarificación convencional->dinámica.

    Retorna un DataFrame con columnas: Planta, delta_electrica_kW, delta_termica_kW
    (y el desglose por componente: delta_esterilizacion_*, delta_clarificacion_*).
    """
    import pandas as pd

    filas = []
    for p, cap in capacidades.items():
        est_elec_nueva = PARAM_ESTERILIZACION_CONTINUA['consumo_electricidad_kWh_tRFF'] * cap
        est_term_nueva = kW_termico_tecnologia_nueva(
            PARAM_ESTERILIZACION_CONTINUA['consumo_vapor_kg_tRFF'],
            PARAM_ESTERILIZACION_CONTINUA['presion_bar'],
            PARAM_ESTERILIZACION_CONTINUA['temperatura_C'], p, T_agua_planta,
            entalpia_vapor_fn, entalpia_agua_alimentacion_fn, capacidades)

        est_elec_vieja = df_demanda_por_etapa.query(
            "Etapa=='Esterilización' and Tipo_energia=='Electrica' and Planta==@p")['Valor_kW'].values[0]
        est_term_vieja = df_demanda_por_etapa.query(
            "Etapa=='Esterilización' and Tipo_energia=='Termica' and Planta==@p")['Valor_kW'].values[0]

        clar_elec_nueva = PARAM_CLARIFICACION_DINAMICA['consumo_electricidad_kWh_tRFF'] * cap
        clar_term_nueva = kW_termico_tecnologia_nueva(
            PARAM_CLARIFICACION_DINAMICA['consumo_vapor_kg_tRFF'], 1, 120, p, T_agua_planta,
            entalpia_vapor_fn, entalpia_agua_alimentacion_fn, capacidades)  # supuesto: saturado 1 bar/120C

        clar_elec_vieja = df_demanda_por_etapa.query(
            "Etapa=='Clarificación' and Tipo_energia=='Electrica' and Planta==@p")['Valor_kW'].values[0]
        clar_term_vieja = df_demanda_por_etapa.query(
            "Etapa=='Clarificación' and Tipo_energia=='Termica' and Planta==@p")['Valor_kW'].values[0]

        filas.append({
            'Planta': p,
            'delta_esterilizacion_elec_kW': est_elec_nueva - est_elec_vieja,
            'delta_esterilizacion_term_kW': est_term_nueva - est_term_vieja,
            'delta_clarificacion_elec_kW': clar_elec_nueva - clar_elec_vieja,
            'delta_clarificacion_term_kW': clar_term_nueva - clar_term_vieja,
            'delta_electrica_kW': (est_elec_nueva - est_elec_vieja) + (clar_elec_nueva - clar_elec_vieja),
            'delta_termica_kW': (est_term_nueva - est_term_vieja) + (clar_term_nueva - clar_term_vieja),
        })

    return pd.DataFrame(filas)


# ---------------------------------------------------------------------------
# Sección 6.4 — Tabla 13: digestión anaeróbica de POME y BMP de EFB pretratado
# ---------------------------------------------------------------------------

PARAM_DIGESTION_ANAEROBICA = {
    'consumo_electricidad_kWh_Nm3_CH4': 0.227,      # Rahayu et al. (2015)
    'disponibilidad_biogas_POME_Nm3_kgDQO': 0.35,   # Rahayu et al. (2015)
    'disponibilidad_lodos_t_tEfluente': 0.03,       # Ocampo Batlle et al. (2020)
}

DQO_ENTRADA_mg_L = {
    'Planta A': 74496, 'Planta B': 97777, 'Planta C': 91573,
    'Planta D': 122973, 'Planta E': 97338, 'Planta F': 94964,
}


def bmp_efb(x_C, x_H, x_L):
    """BMP de material lignocelulósico (L CH4/kg SV). Thomsen et al. (2014).
    x_R = 1 - (x_C + x_H + x_L) es el complemento matemático (no es directamente la ceniza).
    Validado contra la tesis: bmp_efb(0.43, 0.21, 0.15) = 273.51 L CH4/kg SV."""
    x_R = 1 - (x_C + x_H + x_L)
    return 378 * x_C + 354 * x_H - 194 * x_L + 313 * x_R


BMP_EFB_L_CH4_kg_SV = bmp_efb(x_C=0.43, x_H=0.21, x_L=0.15)
