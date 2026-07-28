"""
modelo_biomasa.termodinamica
==============================
Extraído del notebook 01_notebook_v3_CAPEX_corregido.ipynb, Sección 7.

Contiene las funciones de entalpía (IAPWS-IF97) y eficiencia de caldera (ASME)
usadas para la línea base y para las Secciones 6.1+/10/11 (Escenario 1 y 2).

IMPORTANTE (orden de dependencia): este módulo debe importarse y usarse ANTES
de la Sección 6.1 del notebook. En el v3 original, `datos_caldera_LB` se
definía en la Sección 7 pero se usaba en la Sección 6.1 (anterior en el
notebook) — solo funcionaba por ejecución fuera de orden durante el
desarrollo interactivo. Al correr el notebook de forma lineal (kernel
reiniciado), esa dependencia oculta provoca un NameError. Este módulo elimina
ese problema de raíz: se importa una sola vez al inicio y queda disponible
para cualquier sección posterior, sin importar el orden de las celdas.
"""

from iapws import IAPWS97
import pandas as pd

# Datos línea base (hoja Eficiencia, filas 151-169) - las 6 plantas
DATOS_CALDERA_LB = {
    'Planta A': {'m_vapor': 13842,    'P_bar': 24,   'T_vapor': 256,   'T_agua': 95, 'energia_comb': 12691.45},
    'Planta B': {'m_vapor': 19056,    'P_bar': 11,   'T_vapor': 188,   'T_agua': 92, 'energia_comb': 22014.43},
    'Planta C': {'m_vapor': 14127,    'P_bar': 9.6,  'T_vapor': 182.4, 'T_agua': 80, 'energia_comb': 14251.88},
    'Planta D': {'m_vapor': 9878.4,   'P_bar': 9.2,  'T_vapor': 180,   'T_agua': 85, 'energia_comb': 12278.74},
    'Planta E': {'m_vapor': 15480,    'P_bar': 11.3, 'T_vapor': 189.1, 'T_agua': 90, 'energia_comb': 18579.14},
    'Planta F': {'m_vapor': 9720,     'P_bar': 10.3, 'T_vapor': 181.2, 'T_agua': 80, 'energia_comb': 9813.09},
}


def entalpia_vapor(P_bar, T_C):
    """Entalpía del vapor (kJ/kg) vía IAPWS-IF97. P_bar en bar, T_C en °C."""
    return IAPWS97(P=P_bar * 0.1, T=T_C + 273.15).h


def entalpia_agua_alimentacion(T_C, P_bar=1.0):
    """Entalpía del agua de alimentación (kJ/kg) vía IAPWS-IF97."""
    return IAPWS97(P=P_bar * 0.1, T=T_C + 273.15).h


def eficiencia_caldera_ASME(m_vapor_kg_h, P_bar, T_vapor_C, T_agua_C, energia_combustible_kWth):
    """Eficiencia térmica de caldera (ecuación ASME). Retorna (eta, h_f, h_i)."""
    h_f = entalpia_vapor(P_bar, T_vapor_C)
    h_i = entalpia_agua_alimentacion(T_agua_C)
    energia_salida_kWth = m_vapor_kg_h * (h_f - h_i) / 3600  # kJ/h -> kW
    eta = energia_salida_kWth / energia_combustible_kWth
    return eta, h_f, h_i


def validar_iapws97(verbose=True):
    """Valida IAPWS97 contra los valores reportados en el Excel original (Planta A).
    Excel reporta: h_vapor=2897.3 kJ/kg, h_agua=398 kJ/kg."""
    vapor_val = IAPWS97(P=24 * 0.1, T=256 + 273.15)
    agua_val = IAPWS97(P=1 * 0.1, T=95 + 273.15)
    if verbose:
        print(f"h_vapor (IAPWS97): {vapor_val.h:.1f} kJ/kg   | Excel reporta: 2897.3")
        print(f"h_agua (IAPWS97): {agua_val.h:.1f} kJ/kg   | Excel reporta: 398")
    return vapor_val.h, agua_val.h


def calcular_eficiencia_caldera_linea_base(datos_caldera_lb=None, verbose=True):
    """Calcula la eficiencia térmica de caldera (línea base) para las 6 plantas.

    Retorna
    -------
    df_eficiencia_caldera_LB : pd.DataFrame  [Planta, Eficiencia_termica_pct, h_f_kJkg, h_i_kJkg]
    """
    if datos_caldera_lb is None:
        datos_caldera_lb = DATOS_CALDERA_LB

    resultados_eficiencia = []
    for planta, d in datos_caldera_lb.items():
        eta, h_f, h_i = eficiencia_caldera_ASME(d['m_vapor'], d['P_bar'], d['T_vapor'], d['T_agua'], d['energia_comb'])
        resultados_eficiencia.append({'Planta': planta, 'Eficiencia_termica_pct': eta * 100, 'h_f_kJkg': h_f, 'h_i_kJkg': h_i})

    df_eficiencia_caldera_LB = pd.DataFrame(resultados_eficiencia)
    if verbose:
        print(df_eficiencia_caldera_LB)

    return df_eficiencia_caldera_LB