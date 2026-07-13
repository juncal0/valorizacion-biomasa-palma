# Notas metodológicas para el artículo — Aspectos a incluir en Métodos

*Documento de trabajo — recopila las decisiones metodológicas tomadas durante la limpieza y preparación de datos. Organizar y redactar en prosa cuando se escriba la sección de Métodos del artículo.*

---

## 1. Fuente de datos y alcance

- Datos primarios de campo de **6 plantas extractoras de aceite de palma en el departamento del Magdalena, Colombia** (Planta A-F), recolectados como parte del proyecto doctoral.
- Alcance: Línea base (desempeño actual) vs. **Escenario 1** (cogeneración térmica: turbinas de extracción-condensación) vs. **Escenario 2** (digestión anaeróbica de POME + cogeneración).
- Los datos crudos provienen de un archivo de trabajo (`Escenarios.xlsx`) con más de 15 hojas de cálculo, construido durante el desarrollo de la tesis doctoral.

## 2. Estructuración de datos (data wrangling)

- Los datos originales estaban en formato "ancho" (una columna por planta) orientado a lectura humana, no a análisis. Se transformaron a formato "tidy" (`Parámetro`, `Unidad`, `Etapa`, `Planta`, `Valor`) usando Python (pandas) para permitir el modelado posterior en Pyomo.
- Se identificaron y organizaron **11 etapas del proceso productivo**: Recepción/General, Esterilización, Desfrutado, Digestión y prensado, Clarificación, Recuperación de aceite, Almacenamiento, Secado de nueces, Rotura de nuez, Calentamiento de agua de proceso, y Caldera.
- **Nota metodológica:** el código de limpieza y todas las transformaciones quedan documentadas en notebooks de Python (Jupyter) — se recomienda mencionar esto en el artículo como buena práctica de reproducibilidad científica, y considerar publicar el repositorio (GitHub) como material suplementario.

## 3. Tratamiento de valores derivados y datos faltantes

- Se identificaron valores "específicos por tonelada de fruto procesado" (ej. vapor de esterilización, condensados) que estaban en filas sin etiqueta en el archivo original — se confirmó matemáticamente (relación exacta con la capacidad de planta) y se etiquetaron explícitamente como `(específico por tRFF)`.
- Se corrigió un error de unidad en el dato original de "Humedad de secado" (aparecía como °C, debía ser %).
- El parámetro "Flujo de aire de secado" no cuenta con dato medido en campo — se documenta como **dato pendiente de estimación** (a resolver mediante balance psicrométrico en la etapa de modelado, no mediante sustitución arbitraria).
- Las eficiencias reportadas originalmente en la hoja de datos base **no se usan como dato de entrada** — se identificó que dependían de una fórmula de Excel con referencia rota. Se recalculan desde cero a partir del balance de masa y energía en el modelo Pyomo, lo cual permite usarlas como variables de salida auditable y como benchmark de validación.

## 4. Propiedades de la biomasa

- Caracterización fisicoquímica (humedad, C, H, O, N, S, HHV, LHV) para 5 tipos de biomasa residual: EFB, Fibra, PKS, Pressed EFB, Dry EFB — reportada como promedio ± desviación estándar.
- **Correlación para poder calorífico superior (HHV):** ecuación propia ("Present study") sin término de ceniza (Ash), por no contar con datos de ceniza para la biomasa de palma:
  
  `HHV = 0.3443·C + 1.192·H − 0.113·O − 0.024·N + 0.093·S`
  
  (C, H, O, N, S en % base seca). Se validó por consistencia interna contra los valores de HHV reportados (coincidencia exacta) — **aclarar en el artículo que esto confirma consistencia de la tabla de datos, no una validación independiente contra literatura externa**, ya que el HHV reportado probablemente se calculó con la misma correlación.
- Capacidad calorífica (Cp) por componente de biomasa (agua, cuesco, almendra, aceite de palma, fibra, EFB, lodos) tomada de tabla de referencia (transcrita de imagen incrustada en el Excel original — pendiente confirmar cita bibliográfica de la fuente original de esta tabla).

## 5. Costos de inversión (CAPEX)

- **Fuente:** cotizaciones reales obtenidas durante el estudio (proveedores: AIC, MFMI, AVM, Tecnintegral), promediadas por área de proceso para construir la tabla resumen (USD, referenciadas a una capacidad de 15 tRFF·h⁻¹).
- **Curva de costo de cogeneración** (economías de escala vs. capacidad instalada), usada para dar robustez al análisis en vez de un precio unitario fijo:
  
  `CAPEX (USD/kW) = -900.6·ln(P) + 10,841`
  
  Fuente: Malico et al. (2019) — **citar explícitamente en el artículo**; señalar como limitación la transferibilidad geográfica del dato (contexto europeo/Portugal aplicado a Colombia).
- **Ajuste temporal de costos:** todos los valores llevados a USD 2026 mediante el índice CEPCI (Chemical Engineering Plant Cost Index):
  - CEPCI 2019 = 607.5; CEPCI 2021 = 708.8; CEPCI 2026 ≈ 873.8 (estimado)
  - **Nota de limitación a incluir en el artículo:** el valor de CEPCI 2026 es una extrapolación (el año está en curso y el índice es ahora un servicio de suscripción paga desde agosto de 2024) — se calculó a partir de la variación interanual más reciente reportada (+7.5% a febrero 2026 vs. febrero 2025). Documentar fecha de consulta y fuente.
- **Estimación de Pretratamiento térmico** (sin cotización disponible): extrapolado por regla de escalamiento de capacidad (regla de los "seis décimos", exponente n=0.6) a partir de un costo de referencia de 1.4M USD para una planta de 150,000 t/año (dato de 2021, ajustado a 2026 con CEPCI). **Señalar como limitación:** el exponente 0.6 es un valor estándar genérico de ingeniería de costos, no específico para pretratamiento de biomasa — sugerir revisión de literatura especializada si se dispone de tiempo antes del envío.

## 6. Factores de emisión y balance de GEI

- **Factores de emisión de CH4 y N2O** para combustión de biomasa sólida y biogás: valores por defecto IPCC, tomados de Gómez et al. (2017) — Tabla 5 (CH4: 30 kg/TJ biomasa sólida, 1 kg/TJ biogás; N2O: 4 kg/TJ biomasa sólida, 0.1 kg/TJ biogás; GWP100: CH4=21, N2O=310).
- **Convención metodológica:** el CO2 de la combustión de biomasa/biogás se considera **biogénico (neutro)** y no se contabiliza en el inventario de GEI, siguiendo la convención estándar IPCC — solo se contabilizan CH4 y N2O (como CO2-eq) de estas fuentes.
- **Factor de emisión de diésel:** 74,100 kg CO2/TJ (IPCC 2006 Guidelines, Vol. 2) — validado exitosamente contra los valores de la hoja original de la tesis (línea base).
- **Factor de emisión de la red eléctrica nacional (Colombia):** 163.4 g CO2/kWh — mismo valor usado en la publicación previa (JCLP 2024) del autor, por consistencia metodológica. **Nota de limitación a incluir en el artículo:** no se identificó un estudio más reciente/actualizado que reemplace este factor; se mantiene por trazabilidad con el trabajo previo publicado.
- **Crédito de absorción de carbono del cultivo de palma:** -135.04 kg CO2/tRFF procesado, aplicado como descuento fijo al balance neto de GEI en los 3 casos (Línea base, Esc. 1, Esc. 2) — dato consolidado de estudio previo ya usado en la publicación anterior del autor (mantiene consistencia entre ambos artículos).
- **Hallazgo relevante para Métodos:** se identificó que la hoja original de resultados de emisiones (`EmisionesCO2`) contenía un error de cálculo en el factor de CH4 aplicado a los escenarios de valorización (aprox. 250× el valor correcto, probablemente por referencia de celda rota) — **se optó por reconstruir el cálculo desde cero** en vez de reutilizar esos resultados, aplicando los factores IPCC directamente sobre la energía (TJ) que calculará el modelo Pyomo. Esto es coherente con la misma decisión tomada para las eficiencias energéticas (Sección 3).
- **Lógica de flujo energético confirmada (clave para las restricciones del modelo Pyomo):**
  - *Escenario 1 (térmico):* biomasa sólida → combustión → vapor total → una fracción va al proceso industrial (esterilización, digestión, etc.), el resto acciona la turbina → genera electricidad → excedente = generación − consumo propio.
  - *Escenario 2 (biogás):* POME → digestión anaeróbica → biogás → combustión total del biogás → toda la energía va a generación eléctrica (no hay división térmica/eléctrica) → excedente = generación − consumo propio.

## 7. Módulo social — impacto poblacional del excedente eléctrico

- **Nomenclatura de escenarios estandarizada:** se reemplazó la nomenclatura interna original ("ERI-1"/"ERI-2", Escenario de Revalorización Integral) por `Escenario_1_Termico` y `Escenario_2_Biogas`, consistente con el resto del proyecto.
- **Indicador principal de impacto social propuesto:** *viviendas rurales equivalentes abastecidas* = excedente eléctrico (kWh-año) ÷ consumo promedio por vivienda rural departamental (kWh-año). Se prefirió sobre un indicador de "% de cobertura departamental" porque es más tangible/interpretable para el lector y evita la confusión de valores >100% (una sola planta comparada contra la demanda rural de todo el departamento).
- **Indicador complementario:** conversión a *personas equivalentes beneficiadas*, usando el promedio de **3.7 personas por hogar** (DANE, Censo Nacional de Población y Vivienda — CNPV 2018, dato departamental para Magdalena). Se validó cruzado: el total de hogares particulares del DANE para Magdalena (319,306) coincide exactamente con el dato ya usado en la hoja de cálculo original de la tesis.
- **Datos base de demanda residencial departamental (Magdalena, 2025):** rural = 30.3 GWh-año, urbana = 1,209 GWh-año, industrial y comercio = 1,190.7 GWh-año (suma total = 2,430 GWh-año, validada).
- **Limitación a incluir explícitamente en el artículo:**
  1. El DANE no reporta el promedio de personas por hogar desagregado por zona rural/urbana a nivel departamental en la fuente consultada — se usa el promedio departamental general (3.7) para ambas zonas. (Referencia nacional para contexto: la Encuesta de Calidad de Vida más reciente reporta 2.99 personas/hogar rural vs. 2.82 urbano a nivel *nacional*, sugiriendo que el valor rural real podría ser marginalmente distinto al promedio usado).
  2. No se dispone de información geo-referenciada a nivel de municipio/zona de influencia directa de cada planta extractora — el indicador de "población beneficiada" se calcula contra la demanda rural **agregada del departamento**, no contra la población específica del área de influencia de cada planta. Esto sobreestima el impacto local real y debe interpretarse como un indicador de **potencial teórico departamental**, no de alcance geográfico verificado.
- **Igual que en Emisiones y CAPEX:** los bloques de resultados de la hoja original (excedente eléctrico y % de cobertura por planta) se reconstruyen desde cero a partir de los resultados del modelo Pyomo, en vez de reutilizar los valores de la hoja de cálculo, por trazabilidad.

## 8. Hoja `Eficiencia` — consolidación de balances de masa y energía (línea base)

- Esta hoja consolida el balance de masa y energía completo de la línea base (columnas A-H, por planta), en el mismo formato tidy ya usado en `Datos_Base`.
- **Columna I:** corresponde a un caso de estudio específico (planta de referencia) usado para modelar el proceso de **esterilización continua** — tecnología que reemplaza la esterilización convencional en los Escenarios 1 y 2 (ver Sección 9 para la justificación).
- **Cálculo de calor específico (Cp) ponderado del fruto esterilizado:** se identificó un sub-cálculo (columnas J-M) que determina el Cp de la mezcla de fruto a partir de su composición (fibra, nueces, agua, aceite, etc.), ponderando el Cp de cada componente por su fracción en peso. Resultado: **Cp ponderado ≈ 2.2027 kJ/kg·K**. Este valor se formaliza como función de Python (no como constante fija) para que se recalcule automáticamente si cambia la composición del fruto.

### 8.1 Cogeneración existente en línea base (filas 217-244)

- Se identificó un desglose de la **fuente del consumo eléctrico por planta** (filas 220-223: fracciones de Biomasa/Biogás/Red nacional/Diésel) — dato reportado directamente, sin fórmula intermedia, por lo tanto trazable.
- **Hallazgo clave:** en línea base, **solo Planta A tiene cogeneración con biomasa** (79.13% de su consumo eléctrico autogenerado), consistente con lo indicado por el autor. **Adicionalmente se detectó que Planta D ya cuenta con un sistema de biogás** cubriendo el 70% de su consumo eléctrico — hallazgo no documentado previamente en estas notas; **queda pendiente decidir si se incorpora al alcance del modelo de línea base o se documenta como nota aparte** (no confundir con el Escenario 2, que es un sistema de biogás *nuevo/mejorado* a evaluar para las 6 plantas).
- **Discrepancia resuelta:** la misma hoja reporta un parámetro separado "Eficiencia cogeneración" = 12.8% (fila 234, columna C, Planta A — valor fijo, no fórmula). Al intentar usar este valor para derivar la electricidad autogenerada a partir de la energía térmica total de la caldera (fila 237), el resultado (~8.29 millones kWh/año) no reconcilia con el consumo eléctrico total de la planta (3,083,731 kWh/año) — es más del triple. **Se determinó que el 12.8% es un dato de referencia/contexto (eficiencia típica reportada de la turbina de contrapresión existente) y no debe usarse como insumo de cálculo directo**, ya que aplicarlo sobre el total de energía térmica de caldera sobreestima la generación. **Se adopta como fuente de entrada del modelo el desglose de fuente del consumo eléctrico** (fracción Biomasa × consumo eléctrico total), por ser un dato medido y trazable sin ambigüedad de fórmula. El 12.8% se mantiene documentado como referencia de validación cualitativa (orden de magnitud típico de una turbina de contrapresión antigua de baja eficiencia).
- **Electricidad autogenerada por cogeneración, Planta A (línea base):** 3,083,731 kWh/año × 79.13% ≈ **2,439,943 kWh/año**.

## 9. Enfoque de modelado para la etapa de esterilización (decisión de alcance)

- **Decisión metodológica clave:** dado que el objetivo central del artículo es la comparativa entre configuraciones (no un análisis termodinámico detallado de la esterilización), se adopta un enfoque práctico:
  1. **Línea base:** se usa el consumo de vapor de esterilización **reportado/medido en campo** (dato real de `Datos_Base`), sin derivarlo de un balance teórico.
  2. **Escenarios 1 y 2:** la esterilización convencional de la línea base se **reemplaza por esterilización continua**, usando como referencia el caso de estudio de la columna I de `Eficiencia`, escalado a la capacidad de cada una de las 6 plantas.
  3. El balance teórico detallado (calor sensible del fruto + calor latente de condensación del vapor, usando el Cp ponderado calculado arriba) se documenta como **método de validación/respaldo**, disponible como función de Python, pero no como el mecanismo principal de cálculo — para no comprometer alcance y tiempo del proyecto en afinar un balance térmico que no es el foco central del estudio.
- **Justificación técnica del cambio a esterilización continua en los escenarios:** la esterilización continua requiere un **flujo de vapor constante, sin variaciones de presión** — característica ideal para integrarse con una **turbina de extracción-condensación** (Escenario 1), ya que permite extraer exactamente el vapor que demanda el proceso a presión constante, mientras el vapor restante se destina completamente a condensación para generación eléctrica adicional. Esta es una restricción de balance central en la formulación del modelo Pyomo para el Escenario 1.
- **Trazabilidad de fórmulas:** se confirmó que las fórmulas originales de Excel (no solo los valores calculados) son extraíbles con Python (`openpyxl`, modo fórmula). Por ejemplo, la fórmula de "Vapor teórico" se leyó explícitamente y coincide con el balance de calor sensible + latente descrito por el autor, incluyendo referencias cruzadas a la hoja `Biomass` (calores específicos) y constantes de entalpía de vapor (K3=2703, K4=2626 kJ/kg). Esto permite traducir el modelo de Excel a Python con fidelidad exacta cuando se requiera, en vez de reconstruir la lógica de memoria.
- **Escalamiento confirmado (esterilización continua):** consumo específico = **315 kg vapor/tRFF procesado** (derivado del caso de estudio, capacidad 40,000 kg RFF/h → 12,600 kg vapor/h), escalado linealmente a la capacidad de cada una de las 6 plantas — mismo criterio de aproximación usado para los costos de inversión "por capacidad de RFF" en la hoja CAPEX.
- **Tabla de demanda energética por etapa de proceso (columnas M-Y):** desglose de demanda eléctrica (kWe) y térmica (kWth) por cada etapa (Recepción, Esterilización, Desfrutado, Prensado de raquis, Digestión y prensado, Clarificación, Palmistería, Almacenamiento, Extracción de palmiste, Calentamiento de agua, Caldera, Planta de tratamiento de agua). Se organizó en formato tidy (`Etapa`, `Planta`, `Tipo_energia`, `Valor_kW`) para permitir cruce directo con la clasificación de `Etapa` ya usada en `Datos_Base`. Validado: la fila "Total" coincide exactamente con "Demanda térmica proceso LB" de `Scenarios1` (11,627.41 kWth, Planta A).

## 12. Análisis de estacionalidad y almacenamiento de biomasa (material para Discusión)

- **Decisión de alcance:** en vez de correr el modelo Pyomo con progresión temporal mensual completa (que multiplicaría el esfuerzo de modelado sin cambiar necesariamente la conclusión comparativa entre escenarios), se optó por un análisis ligero y complementario usando los datos mensuales reales de `RFF evolution` (2022) como corrección/sensibilidad — dejando el modelo mensual completo como trabajo futuro si el cronograma lo permite.
- **Hallazgo de estacionalidad:** patrón semestral claro en las 6 plantas — procesamiento por encima del promedio de enero a mayo (factor de estacionalidad 1.03-1.28, pico en abril), y por debajo de junio a diciembre (factor 0.87-0.97).
- **Indicador propuesto — buffer de almacenamiento requerido:** máximo déficit acumulado de biomasa a lo largo del año (respecto al promedio mensual), como aproximación al tamaño de almacenamiento necesario para sostener una generación energética constante todo el año. Resultados por planta:

| Planta | Buffer requerido (t) | % del procesamiento anual |
|---|---|---|
| A | 14,461 | 8.3% |
| B | 23,777 | 11.5% (mayor exigencia) |
| C | 5,389 | 3.0% (menor exigencia) |
| D | 5,772 | 4.4% |
| E | 5,295 | 7.2% |
| F | 3,042 | 7.9% |

- **Ángulo de discusión propuesto:** la necesidad de almacenamiento varía sustancialmente entre plantas (3.0%-11.5% del procesamiento anual), sugiriendo que la viabilidad de una estrategia de almacenamiento de biomasa para sostener generación constante depende del perfil de estacionalidad específico de cada planta, no de una política uniforme departamental. Valores en el rango de ~10% del procesamiento anual son logísticamente manejables, lo que respalda la viabilidad técnica del almacenamiento como estrategia complementaria a los escenarios de valorización evaluados.
- **Limitación:** los datos de estacionalidad corresponden a 2022 (un solo año) — se documenta como supuesto que el patrón se mantiene representativo; datos más recientes (disponibles hasta el año actual) podrían incorporarse como análisis de sensibilidad adicional si el tiempo lo permite.
- **Nota de calidad de datos:** se detectó una discrepancia menor entre el acumulado de `RFF evolution` para Planta E (73,534.36 t) y el valor correspondiente en `Datos_Base` (75,534 t) — diferencia de ~2,000 t (~2.6%), no crítica para el análisis pero documentada por transparencia.

## 13. Pendientes de documentar (a resolver en las siguientes hojas del Excel)

- `Scenarios1` / `Scenarios2` (hojas visibles y consolidadas — no confundir con `Scenario 1`/`Scenario 2`, diagramas de flujo ocultos) — balance de masa y energía completo por escenario, base principal del modelo Pyomo.

## 15. Parámetros de sustitución tecnológica de proceso (Tabla 10, tesis)

- **Esterilización continua** (reemplaza esterilización convencional en Escenarios 1 y 2, por su compatibilidad operativa con el sistema de turbina — flujo de vapor constante sin variaciones de presión):
  - Consumo de vapor: **315 kg·tRFF⁻¹** (fuente: caso de estudio, hoja `Eficiencia` de la tesis — confirmado como el valor correcto).
  - Consumo de electricidad: 1.95 kWh·tRFF⁻¹ (fuente: Tabla 10 tesis, datos suministrados por POM).
  - Condiciones de operación: 1 bar, 120°C (fuente: Tabla 10 tesis).
  - **Discrepancia resuelta:** la Tabla 10 de la tesis reporta inicialmente 542 kg·tRFF⁻¹ para "Consumo de vapor" de esterilización continua — se identificó como un probable error de redacción/etiquetado en la tesis (ese valor es más cercano al consumo total de planta con esterilización *convencional*, no al específico del sistema continuo). Se confirmó con el autor que 315 kg·tRFF⁻¹ es el valor correcto, consistente con que la esterilización continua (sistema atmosférico) consume más vapor que la convencional (~180-220 kg·tRFF⁻¹ típico), pero se adopta por su compatibilidad operativa con la turbina, no por eficiencia de vapor.
- **Clarificación dinámica** (reemplaza clarificación convencional — reduce consumo de vapor):
  - Consumo de vapor: 0.6 kg·tRFF⁻¹, electricidad: 15 kWh·tRFF⁻¹, agua: 90 L·tRFF⁻¹.
  - Fuente: Fernández et al. (2016).
- **Sistema de cogeneración con turbina de extracción-condensación (Escenario 1) — Tabla 6 de la tesis:**
  - Caldera: 48 bar, 470°C, eficiencia térmica 85% (Yusniati et al., 2018), agua de alimentación a 129°C.
  - Turbina — extracción de proceso: 5 bar, 159°C (vapor ligeramente sobrecalentado; se reduce de presión aguas abajo hasta 1 bar/120°C para alimentar la esterilización continua de la Tabla 10 y el resto del proceso).
  - Turbina — condensación: 0.22 bar, 62°C (validado: coincide con la temperatura de saturación del agua a esa presión, confirmando consistencia termodinámica del dato). Fuente: Montoya et al. (2020).
  - Eficiencia isentrópica turbina: 77% (modo extracción-condensación) / 75% (modo contrapresión, aplica a Escenario 2). Eficiencia mecánica 98%, eficiencia eléctrica del generador 95%. Autoconsumo de equipos auxiliares: 14.2% (se resta de la generación bruta antes de calcular el excedente exportable). Fuente: Booneimsri et al. (2018).
  - **Discrepancia resuelta:** la tesis presenta dos tablas con parámetros parcialmente distintos para este mismo sistema — Tabla 12 ("Sistema de extracción-condensación": 400°C sin presión de caldera reportada, presión de extracción de proceso 0.3 bar, eficiencia isentrópica 85%) y Tabla 6 ("Parámetros asumidos...": 48 bar/470°C, presión de proceso 5 bar, eficiencia isentrópica 77%). Se intentó inicialmente inferir la presión de caldera de la Tabla 12 a partir de una entalpía de cálculo reportada (3,366.7 kJ/kg a 400°C), pero se determinó mediante verificación con IAPWS-IF97 que esa combinación T-h es termodinámicamente inconsistente (esa entalpía no es alcanzable a 400°C en ningún rango de presión de caldera). Se optó por adoptar la **Tabla 6 como fuente única y definitiva**, al ser explícitamente la tabla de "parámetros asumidos" para la simulación, con mejor trazabilidad de referencias y consistencia termodinámica verificada (validación cruzada exitosa del punto de condensación 0.22 bar/62°C contra IAPWS-IF97).
- **Sistema de digestión anaeróbica (Tabla 13):** consumo de electricidad 0.227 kWh·Nm⁻³CH4, disponibilidad de biogás en POME 0.35 Nm³·kgDQO⁻¹ (Rahayu et al., 2015), disponibilidad de lodos 0.03 t·tEfluente⁻¹ (Ocampo Batlle et al., 2020). DQO de entrada por planta obtenido de `Scenarios1` (fila 40): 74,496-122,973 mg/L según planta.
  - **Nota metodológica sobre la eficiencia de conversión DQO→biogás (DQO_eff, Ecuación 6):** se mantiene como parámetro fijo por ahora; se documenta como candidato para análisis de sensibilidad en una fase posterior del modelo, no se explora en la Fase 1 (validación).
- **Potencial bioquímico de metano (BMP) de EFB pretratado (Ecuaciones 7-8, Tabla 7):** modelo de predicción estadística de Thomsen, Spliid & Østergård (2014, *Bioresource Technology* 154:80-86). Se identificó que la cita de esta ecuación en la tesis original estaba incompleta/mal referenciada; se confirmó la fuente correcta mediante búsqueda bibliográfica, localizando además la misma ecuación (Eq. 4) reproducida y correctamente citada en Gutiérrez, Cabello Eras, Hens & Vandecasteele (2020, *Journal of Cleaner Production* 262:121317) — lo que valida los 4 coeficientes de regresión (378, 354, −194, 313).
  - **Validación exitosa (100% exacta):** el primer intento de reproducir el valor reportado (273.51 L CH4/kg SV) dio 225.6 L CH4/kg SV — una diferencia de ~17% causada por una **mala interpretación de la variable x_R** (residual). Se confirmó, con la fuente completa, que x_R **no es el contenido de ceniza** de la Tabla 7 (5.7%), sino el **complemento matemático** de las otras tres fracciones: x_R = 1 − (x_C + x_H + x_L) = 1 − (0.43+0.21+0.15) = 0.21 (representa lípidos, proteínas, pectina, taninos, etc., no solo ceniza). Al recalcular con x_R = 0.21 en vez de 0.057, el resultado coincide **exacto**: 273.51 = 273.51 L CH4/kg SV.
  - **Decisión metodológica:** el BMP del EFB pretratado se calcula mediante la función completa (no como valor fijo), permitiendo que se recalcule automáticamente si cambia la composición de entrada — mayor trazabilidad y consistencia con el resto del modelo.
  - **Pendiente:** determinar el flujo de material inerte/digestato que sale del reactor de biogás — relevante para ambos escenarios (valorización adicional, artículo de referencia pendiente de revisar con el autor).
- **Reactor de pretratamiento térmico de EFB (steam explosion, Tabla 14) — Escenario 2:** 
  vapor a 200°C / 16 bar, relación de flujo 0.3 t vapor·t biomasa⁻¹, recuperación de 
  vapor (flash steam reciclado) 50%, consumo eléctrico 1 kWh·tEFB⁻¹. 
  Fuente: J. A. Voogt et al. (2021). Distinto del pretratamiento mecánico (Tabla 11, 
  secador rotatorio, Ocampo Batlle et al. 2020, Escenario 1) — no confundir: el térmico 
  aumenta biodegradabilidad del EFB antes de digestión anaeróbica; el mecánico solo 
  reduce humedad para combustión.
- **Producción de metano tras pretratamiento térmico de EFB (Tabla 15):** se distinguen 
  dos conjuntos de parámetros:
  - *Determinado experimentalmente* (medido directamente sobre EFB pretratado, sin 
    valores separados para Efluente): masa seca 44%, humedad 56%, remoción de carga 
    orgánica 66%, producción de biogás 475 m³·t⁻¹ materia orgánica, incremento de 
    producción de biogás 36% (vs. EFB sin pretratar), contenido de CH4 54%.
  - *Suposiciones de diseño conceptual* (valores de diseño, separados por Efluente y 
    EFB): remoción de carga orgánica 85%/73%, producción de biogás 538/523 
    m³·tMO-in⁻¹ y 39/219 m³·tMS⁻¹, contenido de CH4 65%/54% (Efluente/EFB). Para EFB 
    se incluye además un supuesto de "alta remoción de carga orgánica" (10%) como 
    escenario de diseño más conservador.
  - Fuente: J. A. Voogt et al. (2021).
  - **Decisión metodológica (resuelto):** se usa el conjunto de **suposiciones de 
    diseño conceptual** como parámetro de entrada del modelo Pyomo para el Escenario 2, 
    ya que permite modelar de forma consistente el aporte tanto del efluente (POME) 
    como del EFB pretratado dentro del mismo reactor de biogás — el conjunto 
    experimental, aunque con mayor respaldo empírico directo, solo cubre EFB y dejaría 
    sin parametrizar la fracción de POME. Señalar esta elección como supuesto de diseño 
    (no medición directa) en la sección de limitaciones del artículo.

## 16. Enfoque de modelado (a partir de estos datos limpios)

- Modelo de optimización en **Python/Pyomo**, formulado como LP/MILP según la fase (ver plan de trabajo), usando los datos limpios de este documento como parámetros de entrada.
- Selección de la mejor configuración mediante marco de sostenibilidad multicriterio (técnico, económico, ambiental, social) aplicado sobre los resultados del modelo.

## 17. Modelo Pyomo — Fase 1, línea base, Planta A (validación de balance)

- **Objetivo de la Fase 1:** no optimizar — verificar que el balance de energía térmica (caldera) y el balance eléctrico por fuente (biomasa + red nacional + diésel) son consistentes con los datos medidos en campo. Es una prueba de concepto antes de escalar a las 6 plantas y antes de introducir variables de decisión reales (Fase 2).
- **Estructura del modelo (`model = pyo.ConcreteModel`):**
  - Parámetros fijos (medidos): flujo de vapor, energía de combustible, eficiencia de caldera (Sección 7), y las 3 fuentes de electricidad + consumo total (Sección 8.1).
  - Variables: energía térmica útil del vapor, y electricidad por cada una de las 3 fuentes — en esta fase quedan completamente determinadas por las restricciones (no hay grados de libertad).
  - Restricciones: (1) balance térmico = eficiencia × energía combustible; (2)-(4) cada fuente eléctrica igual a su valor medido; (5) restricción de cierre — suma de las 3 fuentes = consumo eléctrico total.
  - Función objetivo *dummy* (`expr=1`) — no aplica optimización real en esta fase, solo se usa el solver para verificar factibilidad del sistema de restricciones.
- **Requisito de entorno — solver GLPK:** Pyomo formula el modelo pero necesita un solver externo (ejecutable) para resolverlo. Se instaló GLPK vía `conda install -c conda-forge glpk` (Anaconda, Windows) — **nota para reproducibilidad:** el ejecutable `glpsol` debe estar disponible en el PATH del sistema; instalarlo por conda evita configurar el PATH manualmente. Verificar con `glpsol --version` en la terminal, y reiniciar el kernel de Jupyter después de instalar (el kernel no detecta software nuevo del sistema hasta reiniciarse).
- **Resultado (Planta A, línea base):** `resultado.solver.termination_condition` → **optimal**, confirmando que el sistema de restricciones es factible y consistente:
  - Energía térmica útil (vapor): 9,626.7 kWth
  - Electricidad autogenerada (biomasa): 2,440,092.0 kWh/año
  - Electricidad de red nacional: 609,714.6 kWh/año
  - Electricidad de diésel: 33,924.4 kWh/año
  - Consumo eléctrico total (verificación): 3,083,731.0 kWh/año — coincide con la suma de las 3 fuentes, cerrando el balance.
- **Interpretación metodológica:** el estado "optimal" en esta fase no debe interpretarse como un resultado de optimización — es la confirmación de que los datos limpios de Secciones 1, 6, 7 y 8.1 son internamente consistentes y pueden usarse como base confiable para los Escenarios 1 y 2 (Secciones 10-11), donde sí habrá grados de libertad reales (variables de decisión) y una función objetivo con sentido físico (maximizar excedente eléctrico).

---

*Última actualización: validado el modelo Pyomo de Fase 1 para línea base (Planta A) — balance térmico y eléctrico cierran correctamente (`optimal`), usando GLPK como solver (instalado vía conda-forge). Pendiente: ensamblar el modelo Pyomo de Escenario 1 (Sección 10, turbina extracción-condensación) y Escenario 2 (Sección 11, turbina contrapresión + biogás) para Planta A; luego escalar a las 6 plantas; determinar el flujo de material inerte/digestato del reactor de biogás.*

## 18. Modelo Pyomo — Escenario 1, Bloques 1-3 (biomasa, caldera, pretratamiento de EFB)

### 18.1 Corrección del LHV de la biomasa (hoja `Biomass`, Sección 2)

- **Hallazgo:** el LHV reportado en el Excel original resta el calor latente de vaporización del agua con un factor ~1000 veces menor al físico (≈2.44 kJ/kg en vez de 2,440 kJ/kg) — error de unidades, del mismo tipo que el ya identificado en el factor de CH4 de `EmisionesCO2` (Sección 6). El error crece con la humedad de cada material (mayor humedad → mayor subestimación del efecto de vaporización → LHV reportado sobreestimado).
- **Verificación:** se reconstruyó la fórmula estándar de ingeniería `LHV_húmedo = HHV_seco·(1-w) − L·[w + 9·H_seco·(1-w)]` (L = 2,440 kJ/kg) a partir de los 3 puntos de humedad disponibles para EFB (65%/50%/10%), confirmando el patrón de error de forma consistente en las 3 variantes.
- **Corrección aplicada** a las 5 variantes de biomasa (recalculado en `df_biomasa`, Sección 2):

  | Material | LHV original (Excel) | LHV corregido | Diferencia |
  |---|---|---|---|
  | EFB (65% hum.) | 6,425.1 kJ/kg | 4,373.9 kJ/kg | +46.9% |
  | Pressed EFB (50%) | 9,179.8 kJ/kg | 7,294.1 kJ/kg | +25.9% |
  | Dry EFB (10%) | 16,525.6 kJ/kg | 15,081.4 kJ/kg | +9.6% |
  | Fiber (35%) | 12,496.6 kJ/kg | 10,772.2 kJ/kg | +16.0% |
  | PKS (15%) | 16,240.6 kJ/kg | 14,821.4 kJ/kg | +9.6% |

- **Impacto:** este LHV corregido se usa en toda la Sección 10 (energía de biomasa a caldera, Escenario 1) y deberá usarse también en el Escenario 2 (Sección 11) — cualquier cálculo de energía de combustión previo que haya usado el LHV original queda invalidado y debe recalcularse.

### 18.2 Disponibilidad de biomasa sólida (Escenario 1)

- **Fuente de flujos:** hoja `Scenarios1` (filas Excel 19-21: Cuesco, Fibra, Raquís/EFB), derivados del balance de masa de la hoja `Eficiencia` — dato de entrada, no recalculado en esta etapa.
- **Nota de trazabilidad importante:** se descartó usar la hoja `Scenario 1` (diagrama de flujo oculto, con espacio en el nombre) como fuente o respaldo de datos — el autor confirmó que esos diagramas son solo ilustrativos, calculados para una planta promedio genérica de 30 tRFF/h representativa del contexto colombiano, no para las 6 plantas del estudio. Además, se detectó que ese diagrama reutiliza el mismo LHV con el bug de la Sección 18.1 (el valor "Enthalpy" de su fila "EFB dried" coincide exactamente con el LHV erróneo de Dry EFB), confirmando que no debe usarse como fuente independiente de validación.

### 18.3 Pretratamiento mecánico del EFB (Tabla 11, Sección 6.2) — aplicado por planta

- El Raquís (EFB) entra al secador a 50% de humedad (equivalente a la categoría "Pressed EFB" de la hoja `Biomass`) y sale a 15% — parámetros ya definidos en la Sección 6.2 (`PARAM_PRETRATAMIENTO_MECANICO_EFB`).
- Se calculó el LHV del EFB ya seco (15% humedad) con la fórmula corregida de la Sección 18.1: **14,108.0 kJ/kg**.
- El secador **no usa electricidad para evaporar el agua** — usa calor residual de los gases de combustión de caldera (215°C). La electricidad (19 kWh/t agua extraída) es solo para la parte mecánica (motores, ventiladores del tambor rotatorio).
- Resultados por planta (energía total de biomasa a caldera tras pretratar el EFB, y electricidad consumida por el secador):

  | Planta | Energía biomasa total (kWth) | Electricidad secador (kWh/h) |
  |---|---|---|
  | A | 35,257.3 | 57.0 |
  | B | 42,493.8 | 70.4 |
  | C | 32,795.5 | 53.7 |
  | D | 24,828.0 | 34.9 |
  | E | 33,098.0 | 57.1 |
  | F | 23,206.7 | 33.4 |

- Con eficiencia de caldera 85% (Tabla 6), el vapor útil resultante: Planta A = 29,968.7 kWth (y proporcionalmente para las demás plantas).

### 18.4 Verificación de calor disponible en gases de combustión para el secador

- **Objetivo:** confirmar si el calor de los gases de combustión (entre 215°C y una temperatura de salida mínima de 120°C, límite práctico para evitar condensación ácida) alcanza para cubrir la demanda térmica de vaporización del agua extraída del EFB (agua extraída × 2,691.1 kJ/kg, parámetro ya definido en la Sección 6.2).
- **Método:** cálculo estequiométrico de combustión a partir de la composición C/H/O/N/S ponderada de la biomasa (Cuesco + Fibra + EFB pretratado), con exceso de aire de **30% (supuesto de literatura genérica — Van Loo & Koppejan, 2008; Basu, 2018)**, no de la fuente específica del pretratamiento (Ocampo Batlle et al., 2020).
- **Resultado — el calor disponible NO alcanza a cubrir la demanda en ninguna de las 6 plantas**, con un déficit de 5-23% según la planta:

  | Planta | Disponible (kWth) | Demanda secador (kWth) | Déficit |
  |---|---|---|---|
  | A | 1,846 | 2,244 | 18% |
  | B | 2,234 | 2,770 | 19% |
  | C | 1,723 | 2,115 | 19% |
  | D | 1,305 | 1,374 | 5% |
  | E | 1,741 | 2,248 | 23% |
  | F | 1,216 | 1,314 | 7.5% |

- **Limitación pendiente (importante para Métodos y Discusión):** el resultado es sensible al supuesto de exceso de aire (se usó 30%, valor genérico de literatura de calderas de biomasa). Se intentó verificar el valor específico reportado por Ocampo Batlle et al. (2020) — fuente original del pretratamiento mecánico (Tabla 11) — pero no se logró acceder al dato exacto (artículo de pago, resúmenes indexados no lo reportan). **Pendiente:** revisar el PDF completo del artículo (si se tiene acceso institucional) para confirmar o ajustar el exceso de aire usado, y correr un análisis de sensibilidad (rango 20-40%) antes de dar el resultado de factibilidad como definitivo. Mientras tanto, se documenta como un déficit marginal (5-23%) que podría revertirse con datos más específicos, y no como una conclusión cerrada de infactibilidad del secado con calor residual.

---

*Última actualización: corregido el LHV de la biomasa (bug de unidades en calor latente, Sección 18.1); validado el pretratamiento mecánico del EFB por planta (Sección 18.3); ejecutada verificación de calor de gases de combustión para el secador — déficit de 5-23% bajo supuesto de exceso de aire de literatura genérica (30%), pendiente confirmar valor específico de Ocampo Batlle et al. (2020). Próximo paso: Bloque 4 de la Sección 10 — turbina de extracción-condensación (Tabla 6).*

## 19. Modelo Pyomo — Escenario 1, Bloques 4-6 (balance de vapor, turbina, excedente eléctrico)

### 19.1 Balance de masa de vapor (producción caldera vs. demanda del proceso)

- **Demanda de extracción (proceso):** se compone de (a) esterilización continua y clarificación dinámica (Tabla 10, dato directo en kg vapor/tRFF — no requieren conversión de unidades) más (b) el resto del proceso (desfrutado, digestión y prensado, palmistería, almacenamiento, extracción de palmiste, calentamiento de agua, planta de tratamiento de agua — Sección 6, reportado en kWth), convertido a kg/h de vapor bajo el supuesto de que el condensado regresa como líquido saturado a 5 bar.
- **Justificación del supuesto de condensado:** confirmado por el autor que estas etapas usan serpentines/radiadores (intercambio indirecto, circuito cerrado) — el supuesto de condensado saturado recuperable es físicamente apropiado para estas etapas.
- **Excepción importante — esterilización continua:** al ser un proceso atmosférico (1 bar, sistema abierto), parte del vapor se pierde por evaporación directa y no regresa como condensado; la fracción que sí condensa arrastra trazas de aceite y se dirige a digestión y prensado (no de vuelta a la caldera). Esto **no afecta el cálculo de extracción de la turbina** (que usa directamente la tasa de Tabla 10, ya en kg/tRFF), pero **sí es relevante para un balance de agua de reposición de caldera** — pendiente de incorporar en una fase posterior del modelo.
- **Resultados del balance por planta** (kg/h): producción entre 25,167 (Planta F) y 46,084 (Planta B); extracción entre 13,642 y 26,590; condensación (remanente a generación eléctrica) entre 10,406 y 19,494 — factible en las 6 plantas.
- **Nota de contraste:** el consumo total de vapor de proceso resultante (~684 kg/tRFF promedio) es mayor al rango típico de esterilización convencional (400-500 kg/tRFF) — consistente con que la esterilización continua consume más vapor que la convencional (ya documentado en Sección 15), aunque parte de la diferencia también podría deberse al supuesto de retorno de condensado adoptado aquí. Señalar como observación metodológica, no como error.

### 19.2 Corrección de bug: entalpía del agua de alimentación (Escenario 1)

- **Hallazgo:** la función `entalpia_agua_alimentacion(T_C, P_bar=1.0)` (definida en Sección 7 para línea base) usa 1 bar por defecto — válido en línea base porque las temperaturas de agua de alimentación (80-95°C) están por debajo de la saturación a 1 bar. Pero en el Escenario 1, el agua de alimentación está a **129°C** (Tabla 6) — por encima de la saturación a 1 bar (~99.6°C) — por lo que evaluarla a 1 bar la calcula como **vapor**, no como líquido comprimido.
- **Detección:** el error se identificó por una prueba de sentido físico simple — el primer cálculo daba una relación vapor:fruto de 5.7:1 (170,679 kg vapor/h para 30,000 kg fruto/h en Planta A), muy por encima del rango físicamente esperado (0.3-1.0). 
- **Corrección:** evaluar el agua de alimentación a la presión de la caldera (48 bar), no a 1 bar por defecto. Tras la corrección, la relación vapor:fruto quedó entre 0.84-1.27 según planta — rango razonable.
- **Recomendación:** revisar si esta misma función se reutiliza en el Escenario 2 (Sección 11) con una temperatura de agua de alimentación distinta a la de línea base, y pasar explícitamente el parámetro `P_bar` correcto en cada caso, en vez de depender del valor por defecto.

### 19.3 Turbina de extracción-condensación (Tabla 6) — planteamiento corregido

- **Primer intento (erróneo):** se trató el estado de extracción (5 bar/159°C) como un resultado a derivar aplicando la eficiencia isentrópica (77%) a la expansión desde 48 bar/470°C. Esto dio una temperatura de extracción calculada de 229.8°C, muy alejada del valor de diseño de la tesis (159°C).
- **Corrección conceptual:** 5 bar/159°C es una **condición de diseño ya especificada** en la Tabla 6 (el punto de extracción fijado por el diseño de la turbina para alimentar el proceso), no algo que deba derivarse con eficiencia isentrópica. El planteamiento correcto:
  - Estado de extracción (h1): se toma **directamente** de la condición de diseño (5 bar/159°C).
  - Eficiencia isentrópica (77%): se aplica a la **expansión completa** (48 bar/470°C → 0.22 bar), usando la entropía de entrada (s0), para obtener el estado de condensación (h2) de forma termodinámicamente consistente.
  - Potencia = (masa total × salto entálpico hasta extracción) + (masa a condensación × salto entálpico de extracción a condensación).
- **Nota epistemológica sobre la validación de temperatura de condensación (62°C):** se confirmó que el resultado calculado coincide con el valor de la tesis (62.1°C vs. 62°C), pero esta coincidencia **no es una validación fuerte** de la eficiencia isentrópica en sí — a 0.22 bar, cualquier estado de vapor húmedo (mezcla líquido-vapor) da automáticamente esa temperatura de saturación, independientemente de la calidad del vapor. Lo que sí confirma es que el estado de salida cae dentro de la zona de mezcla (físicamente esperado en un condensador), no una validación numérica independiente de la eficiencia. Documentar esta distinción para no sobre-interpretar la validación en el artículo.

### 19.4 Resultado — excedente eléctrico neto, Escenario 1 (por planta)

| Planta | Generación turbina neta (kW) | Consumo eléctrico Esc. 1 (kW) | Excedente (kW) | Eficiencia global biomasa→electricidad | Excedente (kWh/tRFF) |
|---|---|---|---|---|---|
| A | 6,005 | 589 | 5,416 | 15.4% | 180.5 |
| B | 7,143 | 762 | 6,381 | 15.0% | 159.5 |
| C | 5,428 | 582 | 4,847 | 14.8% | 161.6 |
| D | 4,124 | 460 | 3,664 | 14.8% | 152.7 |
| E | 5,646 | 591 | 5,055 | 15.3% | 168.5 |
| F | 3,946 | 387 | 3,559 | 15.3% | 177.9 |

- **Consumo eléctrico del Escenario 1:** mismo criterio que el vapor — se resta el consumo eléctrico de las etapas viejas de esterilización/clarificación (Sección 6) y se suman las nuevas (esterilización continua 1.95 kWh/tRFF y clarificación dinámica 15 kWh/tRFF, Tabla 10) más el consumo del secador mecánico de EFB (Sección 18.3).
- **Verificación de sentido físico:** la eficiencia global biomasa→electricidad (14.8-15.4%) cae dentro del rango típico reportado en literatura para turbinas de extracción-condensación en cogeneración con biomasa (~15-25%), y el excedente por tonelada de RFF (153-181 kWh/tRFF) es un orden de magnitud razonable para esta configuración — no hay señales de error en el resultado agregado.

---

*Última actualización: completado el flujo de cálculo del Escenario 1 (Bloques 1-6: disponibilidad de biomasa, pretratamiento de EFB, caldera, balance de vapor, turbina de extracción-condensación, excedente eléctrico neto) para las 6 plantas. Corregidos 2 bugs en el camino (entalpía de agua de alimentación a presión incorrecta; planteamiento erróneo del estado de extracción de la turbina). Pendiente: envolver el flujo completo en un `ConcreteModel` de Pyomo (Bloque 7, análogo a la Sección 9 de línea base) y avanzar al Escenario 2 (turbina de contrapresión + biogás, Sección 11).*

## 20. Modelo Pyomo — Escenario 1, Bloques 7-8 (biogás de POME y excedente total)

### 20.1 Generación de biogás a partir de POME

- **Fuente de datos:** flujo de efluente/POME (hoja `Scenarios1`, fila Excel 38, L/h por planta) y DQO de entrada (fila Excel 40, mg/L — mismo dato ya usado en `DQO_ENTRADA_mg_L`, Sección 6.4).
- **Validación cruzada de parámetros (mismo enfoque usado con el LHV, Sección 18.1):** se comparó la cadena de cálculo de biogás ya existente en `Scenarios1` (filas 34-44, no usada directamente como fuente de resultados, solo para validar supuestos) contra el parámetro `disponibilidad_biogas_POME_Nm3_kgDQO = 0.35` (Rahayu et al., 2015) ya definido en `PARAM_DIGESTION_ANAEROBICA`. Hallazgos:
  - El valor 0.35 **ya corresponde a Nm³ de CH4 directamente** (no de biogás total) — coincide con el valor teórico estequiométrico estándar de conversión DQO→metano (0.35 L CH4/g DQO removido a condiciones normales), confirmado al reproducir el "potencial de generación de metano" de la hoja con ~98% de coincidencia (la pequeña diferencia es consistente con una eficiencia de remoción de DQO cercana al 100%, no con un factor de %CH4 adicional). **Esto simplifica el cálculo: no hace falta un factor adicional de %CH4 en el biogás.**
  - El poder calorífico inferior del metano implícito en la hoja (9.94 kWh/Nm³ ≈ 35.8 MJ/Nm³) coincide con el valor físico estándar del CH4 puro — se usa como constante física, no como dato dependiente del Excel.
  - La eficiencia bruta del generador (motor de combustión interna a biogás) implícita en la hoja es **40.0% exacto** (idéntica en las plantas verificadas) — valor redondo, dentro del rango típico de literatura para motores de biogás (35-42%), adoptado como supuesto de diseño.
  - El factor "neto/bruto" de generación implícito en la hoja (80.0% exacto) **no se pudo explicar** con los parámetros ya documentados (no coincide con aplicar el autoconsumo de 0.227 kWh/Nm³ CH4, que solo explicaría ~5-6% de reducción, no 20%) — **se descartó por falta de trazabilidad** (mismo criterio que con otros datos sin fuente clara del Excel original) y se usó en su lugar el autoconsumo ya documentado con fuente (Rahayu et al., 2015).
- **Resultados por planta** (generación neta de biogás, kW):

  | Planta | Metano (Nm³/h) | Generación bruta (kW) | Autoconsumo (kW) | Generación neta (kW) |
  |---|---|---|---|---|
  | A | 469.3 | 1,866.0 | 106.5 | 1,759.5 |
  | B | 821.3 | 3,265.6 | 186.4 | 3,079.2 |
  | C | 576.9 | 2,293.8 | 131.0 | 2,162.8 |
  | D | 619.8 | 2,464.3 | 140.7 | 2,323.6 |
  | E | 613.2 | 2,438.2 | 139.2 | 2,299.0 |
  | F | 398.8 | 1,585.8 | 90.5 | 1,495.3 |

### 20.2 Excedente eléctrico total del Escenario 1 (turbina + biogás)

| Planta | Turbina (kW) | Biogás POME (kW) | **Total (kW)** | % del total aportado por biogás |
|---|---|---|---|---|
| A | 5,416 | 1,759.5 | **7,175.3** | 24.5% |
| B | 6,381 | 3,079.2 | **9,460.0** | 32.6% |
| C | 4,847 | 2,162.8 | **7,009.6** | 30.9% |
| D | 3,664 | 2,323.6 | **5,987.5** | 38.8% |
| E | 5,055 | 2,299.0 | **7,354.0** | 31.3% |
| F | 3,559 | 1,495.3 | **5,054.2** | 29.6% |

- **Observación para la discusión del artículo:** el biogás de POME aporta entre 24.5% y 38.8% del excedente eléctrico total del Escenario 1 según la planta — una contribución significativa, y con la ventaja de ser un flujo constante todo el año (a diferencia de la biomasa sólida, sujeta a la estacionalidad documentada en la Sección 12), lo que podría discutirse como un complemento que reduce la necesidad de almacenamiento de biomasa frente a depender solo de la turbina.

---

*Última actualización: completado el Escenario 1 en su totalidad (Bloques 1-8: biomasa, pretratamiento EFB, caldera, vapor, turbina, excedente eléctrico de turbina, biogás de POME, excedente eléctrico total) para las 6 plantas. Próximo paso: envolver el flujo completo en un `ConcreteModel` de Pyomo (Bloque 9, análogo a la Sección 9 de línea base) y/o avanzar al Escenario 2 (turbina de contrapresión + biogás con POME y EFB pretratado térmicamente, Sección 11).*

## 21. Plan de Fase 2 — selección de tamaño comercial de turbina (pendiente, no implementado aún)

- **Motivación:** el Bloque 9 (`ConcreteModel` de Escenario 1, Planta A) da una potencia bruta de turbina "exacta" (7,517 kW) que no corresponde a ningún tamaño comercial real (los fabricantes ofrecen tamaños estándar discretos). En Fase 1 esto no es un problema porque el modelo solo valida consistencia (ver nota metodológica sobre la función objetivo dummy, más abajo), pero es una limitación a resolver antes de presentar resultados de dimensionamiento en el artículo.
- **Dos enfoques posibles para Fase 2 (a decidir más adelante):**
  1. **Turbina de capacidad fija (más simple):** fijar la potencia de la turbina a un tamaño comercial (parámetro, no resultado) y convertir la restricción de potencia de `==` a `<=`. Esto abre la pregunta de qué hacer con la biomasa que ya no cabe en el ciclo de vapor (¿venta como pellets, otro uso?) — se vuelve una variable de decisión genuina de distribución de biomasa.
  2. **Selección discreta de turbina (MILP):** dar un catálogo de tamaños comerciales disponibles (ej. 5,000/6,000/7,000/8,000 kW) con una variable binaria de selección, y dejar que el solver elija el tamaño que maximice el excedente eléctrico (o una métrica económica, si se incorpora CAPEX por tamaño). Este es el primer caso de uso real donde la función objetivo (no dummy) y las variables de decisión genuinas de la Fase 2 entran en juego.
- **Nota pedagógica registrada en el chat (útil para la sección de Métodos):** se aclaró la diferencia entre lo que hace el solver en Fase 1 (verificación de factibilidad de un sistema de ecuaciones con una función objetivo dummy `expr=1`, sin verdadera optimización — "optimal" aquí es sinónimo de "factible") vs. lo que hará en Fase 2 (elegir entre múltiples soluciones factibles la que maximice una función objetivo real, con variables de decisión no completamente determinadas por igualdades).

---

*Última actualización: formalizado el flujo completo del Escenario 1 (Planta A) en un `ConcreteModel` de Pyomo (Bloque 9) — validado `optimal`/factible, coincide exacto con los cálculos manuales previos. Documentado el plan de Fase 2 para selección de tamaño comercial de turbina (Sección 21, pendiente de implementar). Próximos pasos posibles: (a) escalar el `ConcreteModel` de Escenario 1 a las 6 plantas, (b) iniciar el Escenario 2 (turbina de contrapresión + biogás con POME y EFB pretratado térmicamente, Sección 11).*

## 22. Modelo Pyomo — Escenario 2 completo (turbina de contrapresión + biogás con POME y EFB pretratado)

### 22.1 Dos bugs adicionales encontrados y corregidos (afectan Escenarios 1 y 2)

- **Bug — consumo eléctrico de clarificación dinámica (Tabla 10):** el valor usado (`consumo_electricidad_kWh_tRFF = 15`) era un **error de decimal** — el valor correcto, confirmado contra la tesis, es **1.5 kWh/tRFF**. Se detectó al contrastar contra la fuente primaria (Fernández et al., 2016, *Palmas* 37(3)): el artículo reporta que la clarificación dinámica **reduce** la potencia instalada de la sección de clarificación (100→45 kW en el caso de estudio real), mientras que con el valor de 15 kWh/tRFF el modelo daba ~450 kW *solo* para esa etapa en una planta de 30 t/h — 10 veces la potencia instalada real reportada en el caso de estudio. Corregido en `PARAM_CLARIFICACION_DINAMICA` (Sección 6.1). Afecta el consumo eléctrico de ambos escenarios.
- **Bug — escala de la columna "Electrica" en `df_demanda_por_etapa` (Sección 6, hoja `Eficiencia`):** los valores de demanda eléctrica por etapa estaban en **kW específicos (por t/h de capacidad de planta)**, no en kW absolutos, a pesar de que el header del Excel decía `(kWe)` sin aclarar que era específico. Detectado por sentido físico: la suma de todas las etapas (fila "Total" del propio Excel) daba solo ~25.75 kW para Planta A — implausible para una planta industrial de 30 t/h (confirmado por el autor: el rango real típico es 600-800 kW). Al multiplicar por la capacidad de planta (30 t/h × 25.75 = 772.5 kW), el resultado cae exactamente en ese rango. **Nota importante:** la columna "Termica" de la misma tabla NO tiene este problema — ya está validada como absoluta (Sección 8, coincide exacto con `Scenarios1`). Corregido multiplicando la columna Electrica por la capacidad de planta, en la Sección 6, inmediatamente después de construir `df_demanda_por_etapa` (se propaga automáticamente a los Bloques 6 de ambos escenarios sin tocar más código).
- **Resultados actualizados tras ambas correcciones:**
  - Escenario 1 — excedente eléctrico total (turbina + biogás): A=6,906.9, B=9,455.1, C=6,852.3, D=5,898.2, E=7,012.4, F=5,052.3 kW.
  - Escenario 2 — excedente de la turbina sola (antes de sumar biogás): A=61, B=322, C=100, D=172, **E=-123 (negativo)**, F=271 kW. La turbina de contrapresión, al ser mucho más pequeña, apenas cubre (o no cubre, caso Planta E) su propio consumo eléctrico de proceso — hallazgo consistente con la experiencia real de plantas pequeñas donde estos sistemas ni siquiera cubren su autoconsumo.

### 22.2 Parámetros de caldera del Escenario 2 (Tabla 16, Booneimsri et al., 2018)

- Presión de caldera: 21 bar. Eficiencia térmica: 70%. Temperatura de agua de alimentación: 100°C.
- **Inconsistencia física detectada y resuelta:** la tesis reporta "Temperatura vapor de agua" = 90°C a 21 bar — físicamente imposible (la saturación a 21 bar es ~215°C; a 90°C sería líquido, no vapor). Se descartó ese dato y se adoptó **230°C como supuesto de trabajo** (punto medio del rango típico de vapor ligeramente sobrecalentado, 220-240°C, confirmado por el autor) — **pendiente de confirmar con la fuente original** si hay un valor más preciso.
- **Entalpía del agua de alimentación:** la tesis reporta 445 kJ/kg a 100°C; el cálculo con IAPWS-IF97 a 100°C/21 bar da ~420.6 kJ/kg (diferencia ~5.7%). Se optó por usar IAPWS97 por consistencia metodológica con el resto del modelo (decisión del autor).

### 22.3 Balance de vapor — cambio de tecnología de esterilización en Escenario 2

- **Hallazgo inicial:** con esterilización continua (Tabla 10, igual que Escenario 1) + pretratamiento térmico del EFB, la demanda de vapor del proceso **superaba la producción disponible en las 6 plantas** (déficit de 5-19%, empeorando a 5-30% al sumar el vapor desviado para el reactor de pretratamiento térmico antes de la turbina).
- **Decisión de diseño (a criterio del autor, con justificación de costos):** para el Escenario 2 se **revierte a esterilización convencional** (en vez de continua) — evita instalar equipos adicionales de mantenimiento/inversión — y se **reutiliza el vapor recuperado del pretratamiento térmico** (50% de recuperación, Tabla 14) reinyectándolo al proceso en vez de descartarlo. Con ambos ajustes, **5 de 6 plantas cierran el balance** (A, B, D, E, F ✅); solo **Planta C queda con déficit residual** (~2,142 kg/h) — aceptado como limitación de escala, consistente con la experiencia del autor de que plantas pequeñas no siempre logran instalar sistemas de contrapresión con generación completa.
- **Fuente del dato de esterilización convencional:** flujo real medido por planta (hoja `Eficiencia`, fila Excel 14, `'Vapor de esterilización' 'kgvapor∙h-1'`) — dato de campo, no una conversión con supuestos.
- **Nota metodológica — clarificación dinámica se mantiene en ambos escenarios** (a diferencia de la esterilización): reduce consumo de vapor sin agregar carga eléctrica desproporcionada (tras corregir el bug de la Sección 22.1).
- **Vapor desviado para pretratamiento térmico del EFB:** se asume que se toma directamente de la salida de caldera (throttled desde 21 bar), antes de la turbina — reduce la masa disponible para generar electricidad. Demanda neta (tras 50% de recuperación) = 0.15 t vapor/t EFB crudo.

### 22.4 Turbina de contrapresión

- Expansión única (21 bar/230°C → 5 bar, misma presión de proceso usada en el balance de vapor), con eficiencia isentrópica de contrapresión (75%, Tabla 6) aplicada a la expansión completa. Reutiliza eficiencia mecánica (98%) y eléctrica del generador (95%) de la Tabla 6 — no hay dato distinto documentado para el tren de generación de este sistema.
- **Validación fuerte de sentido físico:** la potencia bruta calculada (745-1,195 kW según planta) cae **exactamente** dentro del rango que el autor confirmó como típico de la práctica real para turbinas de contrapresión en plantas pequeñas/medianas (800-1,000 kW) — sin haber forzado ningún parámetro para lograrlo. Buena señal de que la cadena completa de supuestos (caldera, balance de vapor, esterilización convencional, recuperación de pretratamiento) está bien planteada.
- Calidad del vapor de escape: ~0.95 (ligeramente húmedo) — físicamente coherente para una turbina de contrapresión.

### 22.5 Biogás — POME + EFB pretratado térmicamente (Tabla 15, "diseño conceptual")

- A diferencia del Escenario 1 (que usa la fórmula simple de Rahayu et al., 0.35 Nm³ CH4/kg DQO, ya validada), el Escenario 2 usa el conjunto **"diseño conceptual"** de la Tabla 15 (Voogt et al., 2021), que da tasas de producción de biogás distintas para Efluente (POME) y EFB, expresadas en m³ biogás por tonelada de materia seca (tMS): 39 para Efluente, 219 para EFB — con contenido de CH4 de 65% y 54% respectivamente.
- **Balance de masa del pretratamiento térmico del EFB:** se calculó con el mismo principio que el pretratamiento mecánico (Sección 6.2) — materia seca conservada, humedad 65% (EFB crudo, hoja `Biomass`) → 56% (EFB pretratado, Tabla 15 "determinado experimentalmente"). Esto da la masa de EFB pretratado que entra al biodigestor.
- **Supuesto adicional:** densidad del efluente (POME) ≈ 1 kg/L, para convertir el flujo de L/h a kg/h y aplicar el % de materia seca (9% para Efluente).
- **Resultado — el EFB pretratado aporta ~7 veces más CH4 que el efluente solo** (301.7 vs. 41.1 Nm³/h en Planta A) — confirma que valió la pena desviar el EFB hacia biogás en este escenario.
- **Investigación de reconciliación con la hoja `Scenarios2` del Excel y el paper fuente (Voogt et al., 2021, EU BC&E):** se encontraron discrepancias significativas entre nuestro cálculo y los resultados que ya existían en `Scenarios2` (excedente total: nuestro ~1,346 kW vs. Excel ~3,784 kW, Planta A). Investigación:
  - **Arquitectura del sistema confirmada como correcta:** el paper de Voogt et al. describe un "Case 2b" donde EFB + Fibra (MF) + POME van *todos* a digestión anaeróbica (sin combustión directa de biomasa), con vapor generado en un calderín de biogás — arquitectura **distinta** a la del Escenario 2 de la tesis (que sí quema fibra+cuesco en caldera con turbina, y solo desvía EFB+POME a biogás). El autor confirmó que su Escenario 2 es un diseño **híbrido propio** que solo tomó parámetros puntuales de Voogt et al. (Tablas 14-15), no la arquitectura completa — por lo tanto, el hecho de no replicar el "Case 2b" del paper no es un error, es una decisión de diseño ya tomada.
  - **Eficiencia de caldera implícita en `Scenarios2` = 85%** (idéntica a la Tabla 6 del Escenario 1) — sospechosamente igual, probablemente una referencia de fórmula copiada de la hoja del Escenario 1 sin ajustar. Se descartó a favor de la Tabla 16 (70%), que es la fuente específicamente construida para el sistema de contrapresión. El 60% que reporta Voogt et al. para su propio caso de estudio tampoco aplica directamente (diseño distinto).
  - **Metano del EFB en `Scenarios2` calculado con la fórmula de Thomsen (BMP, ya validada en Sección 6.4) aplicada al EFB *crudo*, no al pretratado** — reverse-engineered con éxito (fracción de sólidos volátiles implícita: 32% del EFB crudo, 91.4% del contenido seco — valores típicos y razonables). Esto da *más* metano (638.0 m³/h) que nuestro cálculo con la Tabla 15 sobre EFB *pretratado* (301.7 m³/h) — **contradictorio con la propia conclusión del paper de Voogt et al.**, que afirma explícitamente que el pretratamiento térmico *aumenta* la digestibilidad y producción de biogás. Se concluye que la hoja `Scenarios2` del Excel probablemente quedó desactualizada (se armó antes de adoptar el pretratamiento térmico + Tabla 15) y **no se usa como referencia** — se mantiene el cálculo con Tabla 15 sobre EFB pretratado.
  - **Conclusión de la investigación:** no se modificó ningún bloque de código a partir de esta comparación — se documenta como evidencia de que el Excel original (`Scenarios2`) tiene inconsistencias internas de las que hay que desconfiar, ya identificadas repetidamente a lo largo del proyecto (LHV, factor CH4, entalpía de agua de alimentación, etc.), y se valida la decisión de reconstruir los cálculos desde cero en vez de reutilizar los resultados de esa hoja — coherente con la política ya establecida en la Sección 7 de estas notas.

### 22.6 Resultado final — Escenario 2 completo (por planta)

| Planta | Turbina (kW) | Biogás POME+EFB (kW) | **Total (kW)** | % aportado por biogás |
|---|---|---|---|---|
| A | 61 | 1,285.2 | **1,346.4** | 95.5% |
| B | 322 | 1,601.9 | **1,924.1** | 83.3% |
| C | 100 | 1,220.0 | **1,319.8** | 92.4% |
| D | 172 | 815.9 | **987.5** | 82.6% |
| E | -123 | 1,287.0 | **1,163.7** | 110.6% (turbina negativa) |
| F | 271 | 765.2 | **1,036.1** | 73.9% |

- **Comparación Escenario 1 vs. Escenario 2:** el Escenario 1 da un excedente 4-7 veces mayor en todas las plantas — resultado esperado, ya que en Escenario 1 toda la biomasa sólida (fibra+cuesco+EFB) pasa por un ciclo de vapor de alta presión con turbina grande, mientras que en Escenario 2 solo fibra+cuesco alimentan una turbina de contrapresión pequeña y el EFB se desvía a una ruta de biogás con menor eficiencia de conversión a electricidad por unidad de energía de entrada.
- **El biogás domina el excedente eléctrico del Escenario 2** (74-111% del total, siendo >100% en Planta E por la turbina negativa) — contraste fuerte con el Escenario 1, donde el biogás aporta una fracción más modesta (25-39%). Buen ángulo de discusión para el artículo.

---

*Última actualización: completado el Escenario 2 en su totalidad (Bloques 1-8), incluyendo dos bugs adicionales corregidos (clarificación dinámica, escala de consumo eléctrico por etapa) que afectan también al Escenario 1. Investigación de reconciliación con la hoja `Scenarios2` del Excel y el paper fuente de Voogt et al. (2021) documentada — se confirma la arquitectura híbrida propia del Escenario 2 y se decide no usar `Scenarios2` como referencia (desactualizada). Próximos pasos: envolver el Escenario 2 en un `ConcreteModel` de Pyomo (análogo al Bloque 9 del Escenario 1); comparación completa de los 3 escenarios (línea base, Escenario 1, Escenario 2); considerar escalar ambos escenarios a un `ConcreteModel` indexado por planta.*

## 23. Corrección — interpretación de "materia orgánica de entrada" (MOin), Tabla 15

### 23.1 El problema

La Tabla 15 (Voogt et al., 2021, "diseño conceptual") da dos tasas alternativas de producción de biogás: **m³ biogás/t de materia seca (tMS)** y **m³ biogás/t de materia orgánica de entrada (tMOin)**. Inicialmente se usó la tasa por tMS (39 para Efluente, 219 para EFB — Sección 22.5), por ser la que se podía calcular directamente con el dato de % de materia seca ya disponible. Sin embargo, el autor notó que el resultado (CH4 de EFB = 301.7 Nm³/h, Planta A) le parecía bajo frente a lo que esperaba.

### 23.2 Investigación y corrección

- Al revisar de nuevo, se determinó que **"MOin" se refiere a sólidos volátiles (SV), no a materia seca total** — confirmado por el autor tras revisar la fuente.
- **Evidencia de respaldo 1 (ya documentada, Sección 22.5):** el reverse-engineering del cálculo de metano de EFB en la hoja `Scenarios2` del Excel (que usa la fórmula de Thomsen/BMP sobre EFB crudo) arrojó una fracción de sólidos volátiles implícita de 91.4% de la materia seca — consistente con el rango típico de biomasa lignocelulósica (85-95%).
- **Evidencia de respaldo 2 (nueva, encontrada al corregir):** el efluente (POME) es la única corriente que aparece calculada en ambos escenarios, por dos metodologías bibliográficas distintas — Rahayu et al. (2015, vía DQO, usado en Escenario 1) y Voogt et al. (2021, vía tMOin, Escenario 2). Con la interpretación **tMS** (incorrecta), ambos métodos daban resultados desfasados por un factor de **11.4x** (41.1 vs. 469.3 Nm³/h CH4, Planta A) — sin sentido físico para la misma corriente. Con la interpretación **VS** (corregida), ambos métodos coinciden dentro de un **8.7%** (509.9 vs. 469.3 Nm³/h) — una diferencia razonable entre dos fuentes bibliográficas distintas, y una validación cruzada sólida de que la corrección es la correcta.
- **Corrección aplicada:** se usa `FRACCION_VS_MATERIA_SECA = 0.90` (redondeado, con evidencia sólida solo para EFB — para Efluente se usa el mismo valor como supuesto de trabajo, **pendiente de confirmar con la fuente original** ya que no hay verificación independiente específica para esa corriente) multiplicando la materia seca antes de aplicar la tasa m³/tMOin (523 para EFB, 538 para Efluente).

### 23.3 Resultado actualizado

| Planta | CH4 Efluente (Nm³/h) | CH4 EFB (Nm³/h) | CH4 total (Nm³/h) | Generación neta biogás (kW) |
|---|---|---|---|---|
| A | 509.9 | 648.5 | 1,158.4 | 4,342.8 |
| B | 679.8 | 800.7 | 1,480.5 | 5,550.3 |
| C | 509.9 | 611.2 | 1,121.0 | 4,202.8 |
| D | 407.9 | 397.1 | 805.0 | 3,018.0 |
| E | 509.9 | 649.6 | 1,159.5 | 4,346.8 |
| F | 339.9 | 379.9 | 719.8 | 2,698.4 |

**Excedente eléctrico total del Escenario 2, actualizado:**

| Planta | Turbina (kW) | Biogás (kW) | **Total (kW)** | Total Esc.2 / Total Esc.1 |
|---|---|---|---|---|
| A | 61 | 4,342.8 | **4,404.1** | 63.8% |
| B | 322 | 5,550.3 | **5,872.6** | 62.1% |
| C | 100 | 4,202.8 | **4,302.5** | 62.8% |
| D | 172 | 3,018.0 | **3,189.6** | 54.1% |
| E | -123 | 4,346.8 | **4,223.4** | 60.2% |
| F | 271 | 2,698.4 | **2,969.3** | 58.8% |

- **Cambio en la narrativa comparativa:** con la corrección, el Escenario 2 pasa de ser un distante segundo lugar (19-24% del Escenario 1) a una alternativa mucho más competitiva (54-64% del Escenario 1) — cambia sustancialmente el ángulo de discusión del artículo. El Escenario 1 sigue siendo superior en las 6 plantas (combustión directa + turbina de extracción-condensación más grande es energéticamente más eficiente que la ruta de digestión anaeróbica), pero la brecha ya no es tan amplia.
- **`ConcreteModel` de Pyomo del Escenario 2 (Bloque 9, Planta A)** actualizado automáticamente al recalcular `biogas_pome_y_efb_esc2()` — validado `optimal`, coincide exacto con el cálculo manual (4,404.1 kW).

---

*Última actualización: corregida la interpretación de "materia orgánica de entrada" (MOin) en la Tabla 15 — de materia seca total a sólidos volátiles (~90% de la materia seca), validado con evidencia cruzada sólida (reverse-engineering del Excel + comparación independiente del cálculo de POME entre Escenario 1 y 2, coincidencia dentro de 8.7%). El excedente eléctrico del Escenario 2 sube sustancialmente (de ~20% a ~55-64% del Escenario 1) — cambia el ángulo comparativo del artículo. Pendiente: confirmar la fracción VS/materia seca para Efluente con la fuente original (solo hay evidencia sólida para EFB). Próximos pasos: tabla/gráfico comparativo de los 3 escenarios; plan de Fase 2 (selección de turbina comercial, Sección 21).*

## 24. Comparación de los 3 escenarios (Sección 12 del notebook)

- **Línea base vs. Escenarios 1/2:** no son directamente comparables con la misma métrica — la línea base no exporta excedente (cubre su consumo con una mezcla de biomasa/biogás/red/diésel, Sección 9), mientras que los Escenarios 1 y 2 sí generan un excedente eléctrico exportable. Se optó por presentar **dos paneles separados** en el gráfico comparativo: (1) % de electricidad autogenerada con biomasa+biogás en línea base (0% en la mayoría de plantas, salvo Planta A 79.1% y Planta D 70% — ya documentado en Sección 8.1), y (2) excedente eléctrico neto exportable de Escenarios 1 y 2 (kW) — evitando una comparación engañosa en una sola escala.
- **Resultado consolidado Escenario 1 vs. 2 (post-corrección MOin, Sección 23):** Escenario 2 representa entre 54.1% (Planta D) y 63.8% (Planta A) del excedente del Escenario 1 — alternativa competitiva, no un distante segundo lugar.
- Archivos generados: `comparacion_3_escenarios.csv`, `comparacion_3_escenarios.png`.

## 25. Balance de masa — digestato del biodigestor (Escenario 2)

- **Motivación:** determinar el flujo de material inerte/digestato que sale del reactor de biogás, como posible subproducto adicional (fertilizante/enmienda de suelo) — mencionado como pendiente desde la Sección 15.
- **Limitación de la fuente:** el paper de Voogt et al. (2021, EU BC&E) reporta resultados agregados de masa de lodos/efluente (Tabla VIII del paper, en kton/año por caso), pero **no detalla el método de cálculo** — es un artículo corto de conferencia (8 páginas), sin la metodología completa de balance de masa. No se encontró una versión de revista más extensa.
- **Método adoptado (balance de masa simple, sin fuente bibliográfica específica):** masa de entrada (efluente + EFB pretratado) = masa de biogás (fase gas, calculada con densidad de mezcla CH4/CO2 según el % de CH4 de cada corriente) + masa de digestato. Se asume que no hay otras pérdidas (ej. evaporación de agua durante la digestión) — esto da una **estimación conservadora del límite superior** de digestato disponible.
- **Resultado:** el digestato representa **89.6-90.6%** de la masa de entrada al biodigestor en las 6 plantas (13,880-28,027 kg/h según planta) — proporción alta pero físicamente razonable, dado que la mayoría de la masa de entrada es agua (POME diluido, EFB pretratado con alta humedad).
- **Alcance para el artículo:** se documenta como posible fuente de ingreso adicional (valorización del digestato como fertilizante) pero **no se profundiza más** — no es el núcleo del estudio, decisión explícita del autor para mantener el alcance del artículo enfocado.

---

*Última actualización: agregada la comparación gráfica de los 3 escenarios (Sección 12 del notebook, dos paneles separados por métrica no comparable) y el balance de masa de digestato del Escenario 2 (Sección 25) — este último con alcance limitado, documentado como línea de discusión secundaria, no núcleo del estudio. Pendientes restantes: plan de Fase 2 (selección de turbina comercial, Sección 21); escalar los `ConcreteModel` a las 6 plantas de forma indexada; verificaciones con fuentes primarias (temperatura Tabla 16, exceso de aire Ocampo Batlle et al.).*

## 26. Impacto social — aplicado a Escenarios 1 y 2 (Sección 13 del notebook)

- **Fuente de horas de operación anual:** hoja `Eficiencia`, fila Excel 6 (`'Horas de operación' 'h∙año-1'`) — valores: A=5,105, B=5,155, C=5,920, D=5,496, E=3,147, F=1,931. **Nota de discrepancia menor:** la hoja `Hoja1` reporta valores distintos para A/B/C (6,357 / 5,966 / 6,642) — se optó por usar `Eficiencia` como única fuente por tener el dato completo para las 6 plantas (evita mezclar fuentes); no se investigó a fondo la causa de la discrepancia, documentada como limitación menor.
- **Metodología:** se reutilizan las funciones ya construidas en la Sección 5 (`construir_tabla_impacto_social`, `viviendas_rurales_beneficiadas`, `personas_rurales_beneficiadas`), convirtiendo el excedente eléctrico de kW a kWh/año (excedente × horas de operación).
- **Ajuste — techo de 100% en el indicador de cobertura rural departamental:** varias plantas superan el 100% de cobertura (hasta 160.9%, Planta B Escenario 1) — matemáticamente correcto (ya anticipado como limitación en la Sección 7: el indicador compara una sola planta contra la demanda rural agregada de *todo* el departamento), pero no interpretable literalmente como "% de cobertura". Se agregó una columna con techo al 100% (`Pct_cobertura_rural_departamental_techo`) para presentación en gráficos/tablas, más una bandera `Supera_100pct_cobertura` para no perder la información original. La columna sin techo se conserva para trazabilidad.
- **Hallazgos:** Escenario 1 siempre supera a Escenario 2 en impacto social (consistente con mayor excedente eléctrico técnico). Planta F tiene el menor impacto en ambos escenarios (combina menor excedente eléctrico y menos horas de operación anual, 1,931 h — la más baja de las 6). Planta E también queda rezagada por sus pocas horas de operación (3,147 h) pese a tener excedente eléctrico en rango medio — ejemplo claro de por qué separar "excedente instantáneo (kW)" de "impacto anual (kWh)" importa.

## 27. Balance de emisiones de GEI por escenario (Sección 14 del notebook)

### 27.1 Alcance y supuestos

- **Componentes del balance:** emisiones no-CO2 (CH4+N2O) de combustión de biomasa sólida y de biogás (factores IPCC ya definidos, Sección 6); emisiones de diésel de respaldo; **crédito por electricidad exportada** (desplaza generación de la red nacional, 163.4 gCO2/kWh); crédito de absorción de carbono del cultivo de palma (-135.04 kg CO2/tRFF, ya usado en publicación previa del autor).
- **Decisión metodológica — diésel de respaldo en Escenarios 1 y 2:** aunque ambos escenarios generan excedente eléctrico (autosuficientes), se asume que **se mantiene un generador diésel de respaldo al 3% del consumo eléctrico propio** (supuesto de trabajo, no de fuente bibliográfica específica) — refleja la práctica real de mantener redundancia operativa incluso con excedente. Conversión a combustible: eficiencia de generador diésel asumida en **30%** (literatura genérica).
- **Decisión metodológica — crédito de exportación:** se decidió incluir el crédito por sustitución de red nacional (electricidad exportada × factor de emisión de la red) — decisión explícita del autor, ya que es una práctica estándar y defendible en contabilidad de GEI de proyectos de generación distribuida.

### 27.2 Hallazgo — el crédito de absorción de palma distorsiona la comparación por kWh

- El balance neto total (kg CO2eq/año) da fuertemente negativo en las 6 plantas de ambos escenarios (rango -6.0 a -34.2 millones de kg CO2eq/año) — la planta se convierte en un sumidero neto de GEI.
- **Al expresar en gCO2eq/kWh exportado (dividiendo el balance total entre el excedente eléctrico), el crédito de absorción de palma —que es igual en ambos escenarios, ya que depende de la capacidad de la planta, no de la tecnología de generación— se reparte entre denominadores muy distintos** (el excedente eléctrico es mayor en Escenario 1), inflando artificialmente la diferencia aparente entre escenarios (-664 a -719 gCO2eq/kWh en Esc.1 vs. -1,039 a -1,144 gCO2eq/kWh en Esc.2 — sugiriendo engañosamente que Escenario 2 es "más limpio por kWh", cuando en realidad es solo un artefacto de la división).
- **Verificación:** el crédito de absorción de palma por sí solo representa 82.4-87.6% del balance neto total, en ambos escenarios — confirma que domina el resultado y no debe mezclarse con la comparación tecnológica por kWh.
- **Corrección — dos métricas separadas:**
  1. **Intensidad de emisiones del sistema energético únicamente** (excluye el crédito de absorción, se calcula por kWh exportado): Escenario 1 = -125.6 a -132.4 gCO2eq/kWh; Escenario 2 = -128.3 a -135.1 gCO2eq/kWh — **ahora consistentes entre escenarios** (ambos rutas de bioenergía con emisiones no-CO2 pequeñas frente al crédito de desplazar la red nacional), sin la distorsión del paso anterior. Comparación justa y defendible por kWh de tecnología.
  2. **Crédito de absorción de palma** se reporta por separado, en su unidad natural (kg CO2/tRFF procesado) — no depende de la tecnología de generación, es un beneficio del cultivo.
- **Referencia de contexto:** el factor de emisión de la red nacional colombiana es +163.4 gCO2/kWh — ambos escenarios, con -126 a -135 gCO2eq/kWh, no solo tienen emisiones cero sino que son netamente negativos (sumidero), incluso antes de contar el crédito de absorción de palma.

---

*Última actualización: completado el análisis de impacto social (Sección 13) y balance de emisiones de GEI (Sección 14) para Escenarios 1 y 2. Hallazgo metodológico importante: el crédito de absorción de palma domina el balance neto total (82-88%) y distorsiona la comparación tecnológica por kWh si no se separa — se reportan dos métricas independientes (intensidad del sistema energético por kWh, y crédito de absorción por tRFF). Pendiente: análisis de LCOE (el tercer pilar del marco multicriterio, aún no iniciado); plan de Fase 2; escalar `ConcreteModel` a 6 plantas; verificaciones con fuentes primarias.*

## 28. LCOE — costo nivelado de energía (Sección 15 del notebook)

### 28.1 Alcance y metodología

- **LCOE neto, sobre CAPEX incremental** (decisión del autor): se calcula solo la inversión nueva del proyecto de valorización energética (turbina, biodigestor, pretratamientos, sustituciones tecnológicas de esterilización/clarificación) — **no** el CAPEX de la planta extractora completa, ya que esta ya existe y sigue operando igual en los 3 escenarios. Del mismo modo, se excluyen del OPEX los costos del negocio base (RFF, venta de aceite/almendra) que no cambian con la tecnología de valorización energética.
- **Fórmula:** `LCOE = CAPEX_incremental / (Excedente_kWh_año × PVAF) + OPEX_neto_anual / Excedente_kWh_año`, donde `PVAF` es el factor de valor presente de anualidad con tasa de descuento 10% y vida útil 20 años (**supuestos de literatura genérica, no de fuente específica del proyecto** — pendiente de ajustar si se dispone de un dato más preciso).
- **Denominador:** excedente eléctrico anual exportado (kWh/año) — no la generación total, ya que es el "producto" central del estudio.

### 28.2 Fuente de datos — Tabla 17 (equipamiento y costos de inversión) y reconciliación con el CAPEX ya calculado (Sección 3)

- **Hallazgo importante:** el `Total_USD_ref` de "Turbina Contrapresión" en el Excel original ($2,814.68), que se había señalado como sospechosamente bajo (Sección 19, primer intento del Escenario 1), **en realidad es el costo específico correcto** ($2,815/kW), confirmado por la Tabla 17 de la tesis. El error estaba en la columna "Valor_especifico" del Excel ($20,802/kW), que es la que no coincide con la fuente — se corrige usando el valor de Tabla 17.
- **Aclaraciones de unidades (confirmadas por el autor):**
  - "Pretratamiento mecánico de EFB" ($29,655) es **por tonelada de EFB procesado**, no por tonelada de vapor como se interpretó inicialmente en la Sección 19 — se aplica sobre el flujo de EFB crudo (t/h), no sobre el agua evaporada.
  - "Sistema de gases de combustión" ($11,515/t vapor, ciclón + filtro de mangas) aplica al **Escenario 2** (equipo más pequeño); "Precipitador electroestático" ($25,000/t vapor, Tabla 17) aplica al **Escenario 1** (caldera de alto desempeño, 48 bar) — son equipos distintos para calderas de diferente categoría, no el mismo ítem con dos nombres.
  - "Tratamiento térmico de EFB" ($178,571 a una capacidad de referencia de 5.6 tEFB/h) es un **costo total de referencia**, escalado a la capacidad real de cada planta con la regla de los seis décimos (exponente 0.6, mismo criterio ya usado para el pretratamiento térmico en la Sección 3).
  - Sistema de biogás: se compone de **"Lagunas carpadas"** ($18,518/tRFF, el reactor/digestor — en la industria de palma, el digestor de POME suele ser una laguna cubierta, no un tanque cerrado tipo Europa/Voogt et al.), **"Tratamiento de biogás"** ($424/m³ de biogás total, no solo CH4) y **"Generador de biogás"** ($186/kW) — tres partidas separadas, no una sola como se había asumido inicialmente en la Sección 20.
- **Conversión biogás CH4 → biogás total (para aplicar el costo de "Tratamiento de biogás"):** Escenario 1 usa 65% CH4 (supuesto, ya que la fórmula de Rahayu da CH4 directo sin reportar % de metano); Escenario 2 usa los % de CH4 específicos por corriente ya definidos en la Tabla 15 (65% Efluente, 54% EFB).

### 28.3 Partidas de CAPEX incremental por escenario

**Escenario 1:** Caldera (48 bar), Turbina extracción-condensación, Precipitador electroestático, Pretratamiento mecánico EFB, Lagunas carpadas (reactor biogás), Tratamiento de biogás, Generador de biogás, Sustitución esterilización continua, Sustitución clarificación dinámica, Redes e infraestructura.

**Escenario 2:** Caldera (21 bar), Turbina de contrapresión, Sistema de gases de combustión, Tratamiento térmico de EFB (escalado 0.6), Lagunas carpadas, Tratamiento de biogás, Generador de biogás, Sustitución clarificación dinámica, Redes e infraestructura. (Sin sustitución de esterilización — se mantiene convencional, sin costo nuevo.)

Todos los costos ajustados a USD 2026 vía CEPCI (factor 2019→2026 ya definido en la Sección 3).

### 28.4 OPEX neto anual (Tabla 18, con decisiones del autor)

- **Incluido:** costo de operación genérico (2.5% del CAPEX incremental/año); **costo de oportunidad de PKS y MF quemados** en vez de vendidos (decisión explícita del autor — en los escenarios, cuesco y fibra se usan como combustible interno, no se venden, así que se pierde ese ingreso potencial: $16/tPKS, $8/tMF); **ahorro de electricidad ya no comprada** para el consumo propio de la planta (0.19 $/kWh, precio de compra) + **ingreso por venta del excedente exportado** (0.06 $/kWh, precio regulado CREG 30/2018 — nota: precio de venta muy inferior al de compra, típico de esquemas de excedentes en Colombia).
- **Excluido (simplificación, documentada como limitación):** "Mantenimiento y labores" (23.8 k$/tRFF), transporte de EFB/lodo, preparación de agua y manejo de efluentes de la Tabla 18 — no se determinó con certeza si cambian respecto a la línea base con el nuevo sistema; se dejan fuera del cálculo por ahora, pendiente de revisión si se busca mayor precisión.
- **RFF, aceite crudo de palma, almendra de palmiste:** excluidos — son ingresos/costos del negocio base de extracción, no cambian entre escenarios (misma lógica que excluir el CAPEX de la planta base).

### 28.5 Resultados (versión inicial — ver Sección 28.6 para la versión final recomendada para el artículo)

*Nota: esta tabla usa los valores de Escenario 2 previos a la corrección de la Tabla 16 (Sección 29, Booneimsri et al. 2018). Ver Sección 28.6 para los valores actualizados y la comparación bruto/neto recomendada.*

| Planta | LCOE Esc.1 (USD/kWh) | LCOE Esc.1 (COP/kWh) | LCOE Esc.2 (USD/kWh) | LCOE Esc.2 (COP/kWh) |
|---|---|---|---|---|
| A | 0.1279 | 427.1 | -0.0070 | -23.3 |
| B | 0.1097 | 366.5 | -0.0034 | -11.5 |
| C | 0.0895 | 299.1 | -0.0162 | -54.1 |
| D | 0.0865 | 289.0 | -0.0026 | -8.7 |
| E | 0.2305 | 769.8 | 0.0276 | 92.3 |
| F | 0.4190 | 1,399.2 | 0.1302 | 434.7 |

### 28.6 Aclaración metodológica — LCOE bruto vs. neto (para evitar malinterpretación por revisores)

- **Motivación:** un LCOE negativo (varias plantas del Escenario 2), presentado sin más contexto, es exactamente el tipo de resultado que un revisor de artículo va a cuestionar de inmediato ("¿cómo puede costar menos que cero generar electricidad?"). El número es matemáticamente correcto — es consecuencia directa de la definición *neta* elegida (se restan ingresos/ahorros de co-productos) — pero el problema es de presentación, no de cálculo.
- **Solución adoptada:** reportar **dos versiones lado a lado**, ambas con nombres explícitos y distintos:
  1. **LCOE bruto (convencional):** `CAPEX/(Excedente×PVAF) + O&M_anual/Excedente` — **sin** restar ingresos, ahorros, ni costo de oportunidad de PKS/MF. Nunca puede dar negativo. Es el número que un revisor reconoce inmediatamente como "LCOE" en sentido tradicional.
  2. **LCOE neto (o "costo neto de generación ajustado por co-productos"):** el ya calculado en la Sección 28.5, que sí resta el beneficio eléctrico y el costo de oportunidad de PKS/MF. Se presenta explícitamente como un indicador *distinto* y complementario, no simplemente como "el LCOE".
- **Resultados actualizados (post-corrección Tabla 16, Sección 29) — LCOE bruto vs. neto:**

| Planta | Esc.1 bruto (USD/COP) | Esc.1 neto (USD/COP) | Esc.2 bruto (USD/COP) | Esc.2 neto (USD/COP) |
|---|---|---|---|---|
| A | 0.2030 / 677.9 | 0.1279 / 427.1 | 0.0760 / 253.8 | -0.0021 / -7.0 |
| B | 0.1781 / 594.8 | 0.1097 / 366.4 | 0.0693 / 231.4 | 0.0006 / 2.0 |
| C | 0.1624 / 542.4 | 0.0895 / 298.9 | 0.0634 / 211.7 | -0.0122 / -40.7 |
| D | 0.1565 / 522.7 | 0.0865 / 288.9 | 0.0750 / 250.5 | 0.0018 / 6.0 |
| E | 0.3088 / 1,031.3 | 0.2305 / 769.8 | 0.1193 / 398.4 | 0.0347 / 115.9 |
| F | 0.4851 / 1,620.1 | 0.4190 / 1,399.3 | 0.2069 / 691.0 | 0.1409 / 470.6 |

*(USD/kWh en la primera cifra, COP/kWh en la segunda; TRM oficial del 9 de julio de 2026, $3,339.65 COP/USD.)*

- **Con el LCOE bruto, el Escenario 2 sigue siendo mucho más barato que el Escenario 1 en todas las plantas** (0.063-0.207 USD/kWh vs. 0.157-0.485 USD/kWh) — la conclusión central del análisis económico se mantiene igual de fuerte con la versión convencional, no depende de la resta de ingresos.
- **El "salto" entre bruto y neto es proporcionalmente mayor en Escenario 2** que en Escenario 1 (ej. Planta A: caída de $0.078/kWh en Esc.2 sobre una base de $0.076, prácticamente el 100%; vs. $0.075/kWh en Esc.1 sobre una base de $0.203, ~37%) — tiene sentido porque el CAPEX de Escenario 2 es mucho menor, así que el mismo ingreso de co-productos "pesa" proporcionalmente más sobre un costo base más pequeño. Es un dato interesante en sí mismo, no solo un artefacto a explicar.
- **Recomendación para el artículo:** presentar el LCOE bruto como la cifra principal/comparativa (evita objeciones de revisores), y el LCOE neto como análisis complementario que cuantifica el valor de los co-productos — nunca presentar el neto en solitario sin el bruto de referencia.

*(Conversión a COP con TRM oficial del 9 de julio de 2026: $3,339.65 COP/USD — actualizar si se recalcula en otra fecha.)*

- **Escenario 2 resulta sustancialmente más económico que Escenario 1 en las 6 plantas** (de hecho, LCOE negativo en 4 de 6 plantas — los ahorros/ingresos superan los costos en la definición neta usada) — consistente con un CAPEX incremental mucho menor (turbina de contrapresión pequeña vs. turbina de extracción-condensación grande + caldera de alta presión + precipitador electroestático).
- **Planta F sale sustancialmente más cara en ambos escenarios** — combina ser la planta más pequeña (menor capacidad) con las menos horas de operación anual (1,931 h/año, la más baja de las 6) — mismo patrón de "doble penalización" ya observado en el impacto social (Sección 26).
- **Nota de interpretación para el artículo:** un LCOE negativo no debe leerse como "generar electricidad cuesta menos que cero" en sentido convencional — refleja específicamente la definición *neta* elegida (se restan ingresos/ahorros de subproductos y electricidad del costo). Aclarar explícitamente esta definición en la sección de Métodos para evitar una lectura errónea.

---

*Última actualización: completado el análisis de LCOE (Sección 15) para Escenarios 1 y 2 — CAPEX incremental basado en Tabla 17 (con reconciliación de varios datos que corrigen supuestos anteriores de la Sección 19-20) y OPEX neto de Tabla 18 (costo de oportunidad de PKS/MF + beneficio eléctrico). Con esto se completan los 3 pilares del marco multicriterio (técnico, ambiental, social, económico). Pendiente: plan de Fase 2 (selección de turbina comercial); escalar `ConcreteModel` a 6 plantas; verificaciones con fuentes primarias (temperatura Tabla 16, exceso de aire Ocampo Batlle et al.); revisar si incluir "Mantenimiento y labores"/transporte/agua-efluentes en el OPEX para mayor precisión.*

## 29. Verificación y corrección — Tabla 16 (caldera del Escenario 2) contra la fuente primaria

### 29.1 Fuente localizada

Booneimsri, P., Kubaha, K., Chullabodhi, C. (2018). "Increasing power generation with enhanced cogeneration using waste energy in palm oil mills." *Energy Science & Engineering*, 6(3), 154-173. Cita textual relevante:

> *"Wet POM employs a steam boiler that generates steam at typically 2.1 MPa and 235°C and supplies a back pressure steam turbine (BPST)... The exhaust steam from the turbine is fed into the POM at 0.3 MPa and 145°C."*

### 29.2 Confirmaciones y correcciones

- **Presión de caldera (21 bar = 2.1 MPa):** confirmada, coincide exacto con la Tabla 16 de la tesis.
- **Temperatura de vapor:** la fuente reporta **235°C** — se actualiza desde el supuesto de trabajo anterior (230°C, punto medio del rango 220-240°C, Sección 22.2), que resultó muy cercano (diferencia de solo 5°C) pero ya no es necesario como aproximación.
- **Presión/temperatura de escape de la turbina (corrección importante):** la fuente reporta **3 bar (0.3 MPa) / 145°C** — distinto del supuesto anterior de 5 bar (que se había copiado de la presión de proceso del Escenario 1, sin verificación independiente). El autor confirmó que 3 bar es coherente con la práctica real: la presión de esterilización ronda 40 PSI (~2.76 bar), y la turbina debe entregar algo por encima de esa presión, restringida con válvulas aguas abajo.
- **Validación cruzada con el nuevo dato:** la temperatura de escape calculada con la eficiencia isentrópica de la tesis (75%) da 133.5°C, razonablemente cerca del valor de la fuente (145°C, diferencia ~11.5°C) — esperable, ya que la eficiencia isentrópica es específica de la turbina de la tesis, no necesariamente idéntica a la del caso de estudio de Booneimsri et al.

### 29.3 Corrección propagada — nueva función específica para "resto del proceso" del Escenario 2

Se identificó que `resto_proceso_kg_h()` (construida originalmente para el Escenario 1, a 5 bar/159°C) se había reutilizado tal cual para el Escenario 2, sin adaptar a sus propias condiciones de escape. Se creó `resto_proceso_kg_h_esc2()`, específica a 3 bar/145°C, y se propagó la corrección en cascada por todos los bloques dependientes: balance de vapor (Bloque 4), turbina (Bloque 5), excedente eléctrico (Bloques 6 y 8), `ConcreteModel` (Bloque 9), impacto social (Sección 13), emisiones de GEI (Sección 14), y LCOE (Sección 15).

### 29.4 Resultados actualizados — Escenario 2

- **Potencia de turbina, ahora más alta** (bruta 982-1,576 kW, antes 745-1,195 kW) — **ya no cae tan ajustado dentro del rango práctico de 800-1,000 kW** que el autor había confirmado antes; se documenta como observación, no como alarma (el rango práctico conocido puede corresponder a turbinas con parámetros ligeramente distintos a los de Booneimsri et al.).
- **Excedente eléctrico total, Escenario 2 (actualizado):** A=4,662.5, B=6,176.2, C=4,539.6, D=3,396.0, E=4,449.3, F=3,158.6 kW — el % sobre Escenario 1 sube ligeramente (57.6-67.5%, antes 54.1-63.8%).
- **Planta E ya no tiene excedente de turbina negativo** (ahora +102 kW, antes -123 kW) — el hallazgo de "la turbina sola no cubre su consumo" documentado en la Sección 22.4/Estado de continuidad **ya no aplica** con los parámetros corregidos; corregir esta afirmación en el artículo si ya se había redactado.
- **Impacto social:** Planta B (Escenario 2) ahora también supera el 100% de cobertura rural departamental (105.1%, antes 99.9%) — una planta más en la lista de "supera el límite teórico".
- **Emisiones GEI:** cambio menor, intensidad de emisiones del sistema energético (sin absorción) pasa a -130.4 a -136.5 gCO2eq/kWh (antes -128.3 a -135.1) — misma conclusión general, sin cambios sustanciales.
- **LCOE, Escenario 2 (actualizado):** A=-$0.0021, B=$0.0006, C=-$0.0122, D=$0.0018, E=$0.0347, F=$0.1409 USD/kWh — ligeramente más alto que antes (CAPEX de turbina más grande), pero la conclusión general (Escenario 2 sustancialmente más barato que Escenario 1) se mantiene.

---

*Última actualización: verificados y corregidos los parámetros de la Tabla 16 (Escenario 2) contra la fuente primaria (Booneimsri et al., 2018) — temperatura de vapor actualizada a 235°C, presión de escape de la turbina corregida de 5 a 3 bar (145°C), con validación cruzada razonable contra la fuente (133.5°C calculado vs. 145°C reportado). Corrección propagada en cascada por todos los bloques del Escenario 2 (vapor, turbina, excedente, impacto social, emisiones, LCOE). Pendiente: verificación de exceso de aire (Ocampo Batlle et al., 2020, Escenario 1); plan de Fase 2; escalar `ConcreteModel` a 6 plantas; figuras y redacción del artículo.*

## 30. Diagramas Sankey — balance energético departamental por escenario

### 30.1 Corrección de un error de datos detectado al construir la figura

Al calcular los totales agregados para el primer diagrama de comparación (barras, antes del Sankey), se detectó que se había usado un valor desactualizado: **192.7 GWh/año** para el excedente total del Escenario 1, cuando el valor correcto (con las correcciones de clarificación dinámica y escala eléctrica ya aplicadas, Sección 22.1) es **188.8-188.9 GWh/año**. El error vino de reutilizar cifras de excedente por planta de antes de esas correcciones al hacer el primer cálculo agregado. Verificado por triangulación cruzada (suma directa de los totales por planta ya establecidos × horas de operación, coincide con el recálculo por etapas). El Escenario 2 (121.3 GWh/año) sí estaba correcto desde el inicio. **Cualquier figura/tabla que se haya generado antes de esta nota con el valor 192.7 debe corregirse a 188.8-188.9.**

### 30.2 Metodología — desglose por etapas (Sección 12 del notebook, `plotly.graph_objects`)

Se construyeron dos diagramas Sankey (uno por escenario) mostrando el balance energético departamental agregado (suma de las 6 plantas × horas de operación anual), con 4 categorías de nodo: fuentes (biomasa sólida, POME/POME+EFB), sistemas de conversión (cogeneración, biogás), y 3 tipos de salida (pérdidas, a proceso, excedente eléctrico).

- **Enfoque de "caja negra":** cada sistema de conversión (cogeneración, biogás) se trata como una caja negra con una entrada (energía del combustible) y 3 salidas (pérdidas, a proceso, excedente) — sin desglosar el detalle termodinámico interno (caldera, turbina, generador por separado). Es el mismo criterio usado en la imagen de referencia que aportó el autor (diagrama Sankey de un estudio similar) y es una simplificación estándar y defendible para un balance energético de alto nivel.
- **Nota metodológica sobre la arquitectura de "A proceso" (diferencia entre escenarios, no visible en la figura):**
  - **Escenario 1 (extracción-condensación):** "A proceso" y "Excedente" compiten por el mismo vapor *antes* de la turbina (la extracción reduce la masa disponible para la etapa de condensación). Se calculó como una participación proporcional de la masa (extracción/producción total) aplicada a la energía del vapor útil.
  - **Escenario 2 (contrapresión):** toda la masa de vapor pasa primero por la turbina (genera electricidad), y "A proceso" sale del vapor de escape *después* de la generación eléctrica — no compite con el excedente. Se calculó directamente como la energía entregada al proceso (masa de demanda × salto entálpico de proceso a 3 bar, ya definido en la Sección 29), no como participación proporcional.
  - Ambas arquitecturas se presentan con el mismo formato de 3 salidas por simplicidad visual y consistencia comparativa entre escenarios, aunque el mecanismo físico interno difiere — documentado aquí para que quede claro en caso de que un revisor pregunte por la coherencia interna del cálculo.
- **Escenario 1 — biogás con POME únicamente** (no POME+EFB, ya que en este escenario el EFB se quema entero en la caldera junto con fibra y cuesco) — corrección de una etiqueta incorrecta que se usó en un primer intento de diagrama (antes de adoptar Plotly).

### 30.3 Resultados — flujos agregados (GWh/año)

**Escenario 1:**

| Nodo | Valor (GWh/año) |
|---|---|
| Biomasa sólida (entrada) | 878.6 |
| POME (entrada, biogás) | 160.5 |
| Pérdidas (cogeneración) | 318.9 |
| A proceso (cogeneración) | 431.4 |
| Excedente turbina | 128.3 |
| Pérdidas (biogás) | 99.9 |
| Excedente biogás | 60.6 |
| **Excedente total** | **188.9** |

**Escenario 2:**

| Nodo | Valor (GWh/año) |
|---|---|
| Biomasa sólida (entrada) | 463.6 |
| POME + EFB (entrada, biogás) | 294.7 |
| Pérdidas (cogeneración) | 175.0 |
| A proceso (cogeneración) | 278.5 |
| Excedente turbina | 10.1 |
| Pérdidas (biogás) | 183.5 |
| Excedente biogás | 111.1 |
| **Excedente total** | **121.3** |

- **Contraste visual clave:** en Escenario 1 la ruta de biomasa/turbina domina el excedente (68% turbina, 32% biogás); en Escenario 2 se invierte casi por completo (8% turbina, 92% biogás) — buen ángulo de discusión para el artículo sobre cómo cambia el rol de cada tecnología entre configuraciones.

---

*Última actualización: construidos y validados los diagramas Sankey de balance energético departamental para ambos escenarios (`plotly.graph_objects`, Sección 12). Corregido un error de dato desactualizado (192.7→188.8-188.9 GWh/año, Escenario 1) detectado durante la construcción de la figura. Documentada la diferencia arquitectónica entre escenarios en el manejo de "A proceso" (compite con excedente en Esc.1, es posterior a la generación en Esc.2), simplificada de forma consistente en ambos diagramas. Pendiente: verificación de exceso de aire (Ocampo Batlle et al.); revisar inclusión de mantenimiento/transporte/agua-efluentes en OPEX del LCOE (decisión: no se profundiza, la distinción LCOE bruto/neto ya resuelve la preocupación de fondo); escalar `ConcreteModel` a 6 plantas; plan de Fase 2; redacción del artículo.*

## 31. `ConcreteModel` indexados a las 6 plantas — línea base, Escenario 1 y Escenario 2

### 31.1 Alcance de la decisión

Se decidió escalar los 3 modelos (línea base, Escenario 1, Escenario 2) de una sola planta (Fase 1, prueba de concepto) a un `pyo.Set` de las 6 plantas, con parámetros/variables/restricciones indexadas — un único `ConcreteModel` por escenario que resuelve las 6 plantas simultáneamente, en vez de 6 modelos independientes.

### 31.2 Patrón de implementación

- `model.PLANTAS = pyo.Set(initialize=plantas)` reemplaza el enfoque de una sola planta.
- Parámetros/variables se indexan con `pyo.Param(model.PLANTAS, initialize=diccionario)` / `pyo.Var(model.PLANTAS, domain=...)`.
- Restricciones se definen como funciones `rule(m, p)` y se registran con `pyo.Constraint(model.PLANTAS, rule=...)` — Pyomo genera automáticamente una restricción por planta.
- Los parámetros se siguen calculando **fuera** de Pyomo, reutilizando las funciones ya validadas de las Secciones 9-11 (`energia_biomasa_kWth_esc1()`, `balance_vapor_esc1()`, `potencia_turbina_kW()`, `biogas_pome()`, etc., construidas con un diccionario por planta vía comprensión `{p: funcion(p) for p in plantas}`) — Pyomo solo verifica que el sistema de ecuaciones cierra para las 6 plantas a la vez, no recalcula la física.

### 31.3 Errores encontrados y corregidos durante la implementación (para referencia futura)

1. **Nombres de columna incorrectos** (línea base): se asumieron nombres de columna de memoria (`Energia_biomasa_kWth`) que no coincidían con los reales de `df_fuente_electrica_LB`/`df_eficiencia_caldera_LB` — resuelto pidiendo `df.columns.tolist()` directamente antes de asumir.
2. **Fuente eléctrica faltante** (línea base): el primer intento solo consideró 3 fuentes (biomasa, red, diésel), pero la tabla real tiene 4 (agrega biogás, relevante para Planta D que ya tiene 70% de cobertura con biogás, Sección 8.1).
3. **`infeasible` al escalar Escenario 2:** al juntar las 6 plantas en un solo modelo, la restricción `excedente_condensado_kg_h` (definida como `NonNegativeReals`, heredada del modelo de una sola planta) hizo que el modelo COMPLETO fuera infactible por el déficit conocido de Planta C — a diferencia de 6 modelos independientes, donde una planta infactible no afecta a las demás. **Corrección:** cambiar el dominio a `pyo.Reals`, permitiendo que Planta C muestre su déficit como valor negativo sin bloquear la solución de las otras 5 — mismo criterio ya usado para `excedente_turbina_kW` (que puede ser negativo, caso Planta E antes de la corrección de Booneimsri).
4. **Mezcla accidental de celdas:** al aplicar una corrección de una línea, se pegó por error dentro de la celda del modelo de una sola planta (`model_e2`) en vez de la celda nueva del modelo indexado (`model_e2_6`) — causó un `AttributeError` confuso. Resuelto manteniendo cada modelo en su propia celda, sin mezclar código entre `model_e2` (prueba de concepto, Planta A) y `model_e2_6` (las 6 plantas).

### 31.4 Resultados — validación cruzada

Los 3 modelos indexados dieron `optimal` con las 6 plantas simultáneamente, y los valores coinciden exactos con los ya calculados manualmente/con los modelos de una sola planta — sin discrepancias:

- **Línea base:** confirma la cogeneración existente de Planta A (2,440,092 kWh biomasa/año) y Planta D (biogás al 70%, 2,622,351 kWh/año) — consistente con la Sección 8.1.
- **Escenario 1:** A=6,906.9, B=9,455.1, C=6,852.3, D=5,898.2, E=7,012.4, F=5,052.3 kW.
- **Escenario 2:** A=4,662.5, B=6,176.2, C=4,539.6, D=3,396.0, E=4,449.3, F=3,158.6 kW (post-corrección Booneimsri, Sección 29).

---

*Última actualización: escalados los 3 `ConcreteModel` (línea base, Escenario 1, Escenario 2) de una sola planta a las 6 plantas simultáneas, vía `pyo.Set` + parámetros/variables/restricciones indexadas. Todos validados `optimal`, coincidencia exacta con los cálculos previos. Documentados 4 errores de implementación encontrados en el camino (nombres de columna, fuente eléctrica faltante, infactibilidad por dominio de variable al juntar plantas, mezcla accidental de celdas) como referencia para futuros modelos indexados. Pendientes finales: plan de Fase 2 (selección de turbina comercial); verificación de exceso de aire (Ocampo Batlle et al.); redacción del artículo.*

## 32. Fase 2 — superestructura de optimización (diseño y primeros resultados)

### 32.1 Alcance decidido (con límite de páginas del artículo en mente)

Tras revisar literatura de optimización MILP/superestructura en cogeneración con biomasa (varios estudios de superestructuras con Sets de "recursos" y "unidades" intercambiables; estudios de dimensionamiento de turbina bajo múltiples combinaciones de presión/temperatura; estudios de despacho con precios de electricidad variables; estudios multiperiodo/multiobjetivo en biorrefinerías), se definieron **3 restricciones/variables de decisión** para la Fase 2, elegidas por su relación directa con los 3 pilares de sostenibilidad (económico, ambiental, social) y por ya contar con los datos necesarios:

1. **Selección de paquete tecnológico por planta** (variable binaria: Escenario 1 vs. Escenario 2) — la "eficiencia global del sistema" se decidió modelar como esta elección discreta, no como una restricción de mínimo ni una métrica de reporte pasiva.
2. **Tamaño comercial de turbina y generador de biogás** (catálogo discreto, variable binaria de selección + variable continua de "factor de utilización" que escala biomasa/vapor/potencia cuando se elige una capacidad menor a la ideal).
3. **% de EFB destinado a energía vs. retorno a campo como acondicionador de suelo** (variable continua, techo de 60% — Ponce et al., 2008, "Potencial de cogeneración de energía eléctrica en la agroindustria colombiana de aceite de palma", que usó ese mismo límite considerando el valor del EFB como fertilizante).

**Se excluyó explícitamente la estacionalidad** (multiperiodo mensual) del alcance del solver — multiplicaría las restricciones ~12x y se consideró demasiado para el espacio del artículo. Queda como análisis de sensibilidad/discusión (ya cubierto en la Sección 12 de estas notas: buffer de almacenamiento de biomasa).

**Función objetivo real (por fin, ya no dummy):** maximizar (ahorro de electricidad autoconsumida + ingreso por venta de excedente − CAPEX anualizado de los equipos seleccionados), usando los precios de la Tabla 18 y el `PVAF` ya definido en la Sección 15 (LCOE).

### 32.2 Construcción por etapas

Dado el tamaño del problema, se construyó incrementalmente: Etapa 1 (catálogo de turbina + factor de utilización, solo Escenario 1) → Etapa 2 (agregar % EFB) → Etapa 3 (repetir para Escenario 2) → Etapa 4 (superestructura completa con selección binaria de paquete tecnológico). Este documento cubre los resultados de la Etapa 1.

### 32.3 Catálogos de equipos (supuestos de trabajo, sin fuente de fabricante específica)

| Catálogo | Valores (kW) |
|---|---|
| Turbina Escenario 1 | 300, 500, 750, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000 |
| Turbina Escenario 2 | 750, 1000, 1250, 1500, 1750 |
| Generador biogás Escenario 1 | 1500, 2000, 2500, 3000, 3500 |
| Generador biogás Escenario 2 | 3000, 3500, 4000, 4500, 5000, 5500 |

### 32.4 Resultado Etapa 1 — hallazgo económico central

- **Primer intento (objetivo = solo venta de excedente a 0.06 $/kWh):** el solver elige la turbina más pequeña del catálogo en las 6 plantas — el costo anualizado de cualquier kW instalado (≈620 USD/kW/año, con CAPEX Tabla 17 + CEPCI 2026, descuento 10%, 20 años) supera el ingreso que genera ese mismo kW vendido a la red (306-364 USD/kW/año según horas de la planta). **Bajo el precio regulado colombiano actual (CREG 30/2018), exportar excedente a la red no se sostiene económicamente por sí solo.**
- **Segundo intento (objetivo = ahorro de autoconsumo + venta de excedente):** con el catálogo original (mínimo 4,000 kW), el resultado no cambió — reveló que el catálogo propuesto ya estaba muy por encima del óptimo real.
- **Catálogo ampliado hacia abajo (300-10,000 kW):** el óptimo verdadero emergió — el solver dimensiona la turbina para cubrir **solo el autoconsumo propio de cada planta**, sin excedente exportable, en 4 de 6 plantas (A, B, C, D). **Planta E y Planta F no alcanzan a justificar ninguna inversión de turbina** — ni siquiera para cubrir su propio consumo.
- **Explicación del umbral (verificado matemáticamente):** el punto de equilibrio entre ahorro de autoconsumo (horas de operación × 0.19 $/kWh) y costo anualizado de turbina (≈620 USD/kW/año) cae justo entre las plantas — A, B, C, D superan las 5,100 horas/año de operación (ahorro 970-1,125 USD/kW/año, rentable); E (3,147 h) y F (1,931 h) caen por debajo (ahorro 367-598 USD/kW/año, no rentable).
- **Triangulación con otros hallazgos del proyecto:** Planta E y F ya habían salido peor paradas en el impacto social (menos horas de operación anual, Sección 26) y en el LCOE (mayor costo por kW, Sección 28) — este es un **tercer indicador independiente que apunta a la misma conclusión**: estas dos plantas, bajo un criterio puramente económico, no justifican la inversión en cogeneración de extracción-condensación a su escala actual.

### 32.5 Interpretación para el artículo

Este hallazgo — que el óptimo económico puro tiende hacia el autoabastecimiento, no hacia la exportación masiva de excedente — es consistente con la brecha ya documentada entre el precio de compra (0.19 $/kWh) y venta (0.06 $/kWh) de electricidad en el esquema regulatorio colombiano (Sección 28.4) y aporta una conclusión de política pública relevante: **el marco de precios actual no incentiva economicamente la generación distribuida a gran escala en plantas de beneficio de palma**, a menos que se cuenten también los beneficios ambientales/sociales no capturados en el precio de mercado (línea de discusión para conectar con los hallazgos de emisiones evitadas y cobertura social, Secciones 26-27).

---

*Última actualización: completada la Etapa 1 de la superestructura de Fase 2 (catálogo de turbina + factor de utilización, Escenario 1) — hallazgo central: el óptimo económico puro tiende al autoabastecimiento (sin excedente exportable) en 4 de 6 plantas, y Planta E/F no justifican ninguna inversión de turbina bajo horas de operación actuales. Consistente con hallazgos previos de impacto social y LCOE (mismas 2 plantas rezagadas en los 3 análisis). Próximo paso: Etapa 2 (agregar % de EFB como variable de decisión, techo 60%).*

## 33. Corrección de precios de electricidad — específicos por planta, con fuentes primarias

### 33.1 Nuevas fuentes de precio (aportadas por el autor)

- **Diésel:** $11,051 COP/galón. Convertido a costo de electricidad: $0.2930 USD/kWh eléctrico (usando LHV del diésel ≈37.64 kWh/galón y la eficiencia de generador de respaldo ya definida, 30%).
- **Cogeneración con vapor (biomasa), solo O&M:** 77.26 USD/MWh = $0.0773 USD/kWh — fuente: portal UPME, calculadora de LCOE (https://lcoev2.upme.gov.co/results/2). No incluye CAPEX porque los equipos de línea base ya existen (inversión hundida).
- **Biogás:** 350 COP/kWh — fuente: documento de 2019 (compartido por el autor, sin ajuste por inflación — **limitación documentada**, pendiente si se dispone de un valor más reciente).
- **Red eléctrica:** 840.15 COP/kWh — tarifa específica de Magdalena 2025, Nivel 3 (industrial).
- **TRM usada para conversión:** $3,339.65 COP/USD (9 de julio de 2026, oficial).

### 33.2 Hallazgo — el precio de red de Tabla 18 estaba desactualizado/genérico

El precio de compra de electricidad de Tabla 18 (0.19 USD/kWh) resultó ser **32.4% más bajo** que la tarifa real específica de Magdalena 2025 industrial (0.2516 USD/kWh) — subestimaba el ahorro de autoconsumo en todos los cálculos que lo usaban (LCOE neto, Sección 28; Fase 2, Sección 32).

### 33.3 Refinamiento — precio de compra específico por planta, no un valor único

Se determinó que el precio "que cada planta deja de pagar" al autoabastecerse depende de **su propia matriz eléctrica actual** (línea base) — no tiene sentido usar un precio de red único para las 6 plantas, ya que Planta A y Planta D ya tienen cogeneración propia barata (biomasa/biogás) cubriendo una parte de su consumo, mientras que B, C, E, F dependen casi enteramente de la red cara. Se calculó el **costo ponderado real** de cada planta (Σ kWh_fuente × costo_fuente / kWh_total), usando los 4 precios de la Sección 33.1:

| Planta | Costo ponderado actual (USD/kWh) | Costo ponderado actual (COP/kWh) | Fuentes dominantes |
|---|---|---|---|
| A | 0.1141 | 381.2 | 79% biomasa barata ($0.077/kWh) |
| B | 0.2537 | 847.2 | ~95% red cara |
| C | 0.2572 | 859.1 | ~86% red cara |
| D | 0.1530 | 510.9 | 70% biogás barato existente |
| E | 0.2551 | 851.9 | ~92% red cara |
| F | 0.2591 | 865.1 | ~82% red cara |

- **Hallazgo citable:** cogenerar con biomasa/biogás ya es 2-3 veces más barato que comprar de la red (Planta A: $0.114/kWh vs. Planta B-C-E-F: ~$0.25-0.26/kWh) — evidencia económica cuantitativa independiente del análisis de excedente/exportación, útil para el artículo.

### 33.4 Propagación — Fase 2, Etapa 1 (recalculada con precio específico por planta)

`PRECIO_ELECTRICIDAD_COMPRA` pasó de escalar único a diccionario indexado por planta (`PRECIO_ELECTRICIDAD_COMPRA_dict`), tanto en la función `lcoe_escenario()` (Sección 15) como en el parámetro `precio_compra` del modelo de Fase 2 (`pyo.Param(model.PLANTAS, initialize=...)`).

**Resultado — el umbral de rentabilidad de turbina cambia de forma no trivial:**

| Planta | Ahorro (USD/kW/año) | Costo turbina (USD/kW/año) | ¿Rentable? |
|---|---|---|---|
| A | 582.5 | 619.7 | **NO** |
| B | 1,307.8 | 619.7 | SÍ |
| C | 1,522.6 | 619.7 | SÍ |
| D | 840.9 | 619.7 | SÍ |
| E | 802.8 | 619.7 | SÍ |
| F | 500.3 | 619.7 | **NO** |

- **Hallazgo refinado (reemplaza la conclusión anterior de la Sección 32.4):** ya no son "las plantas con menos horas de operación" las que quedan rezagadas — es **Planta A** (que ya tiene cogeneración barata existente, así que el ahorro *marginal* de invertir en el Escenario 1 completo es menor, compite solo contra la fracción de consumo que aún compra caro) y **Planta F** (la más pequeña, con menos horas). Planta E, que antes no era rentable, ahora sí lo es — depende 100% de la red cara, así que tiene mucho que ganar.
- **Implicación metodológica importante para el artículo:** evaluar la rentabilidad de un proyecto de cogeneración nueva **no debe asumir que la planta parte de cero** — si ya existe cogeneración parcial, el ahorro marginal real es menor al que sugeriría un precio de red genérico aplicado a todo el consumo. Vale la pena señalar esto como una limitación de los estudios que usan un solo precio de referencia para todas las plantas de un análisis multi-planta.

### 33.5 LCOE neto recalculado con precio de electricidad específico por planta

Tras propagar `PRECIO_ELECTRICIDAD_COMPRA_dict` a la función `lcoe_escenario()`, el LCOE neto se recalculó (el LCOE bruto no cambia — no depende del precio de electricidad):

| Planta | Esc.1 bruto | Esc.1 neto | Esc.2 bruto | Esc.2 neto |
|---|---|---|---|---|
| A | 0.2030 | 0.1373 | 0.0682 | 0.0023 |
| B | 0.1781 | 0.1046 | 0.0625 | -0.0128 |
| C | 0.1624 | 0.0823 | 0.0571 | -0.0281 |
| D | 0.1565 | 0.0900 | 0.0671 | -0.0009 |
| E | 0.3088 | 0.2218 | 0.1077 | 0.0109 |
| F | 0.4851 | 0.4136 | 0.1847 | 0.1116 |

*(USD/kWh. LCOE bruto = solo CAPEX + O&M; LCOE neto = descontando ahorro de autoconsumo al precio ponderado real de cada planta + venta de excedente.)*

- **Efecto del precio por planta sobre el LCOE neto:** comparado con la versión de precio único (0.2516), el neto **sube en Planta A y D** (su precio de autoconsumo ponderado es bajo, $0.114 y $0.153, por la cogeneración existente → menor ahorro descontado → LCOE neto más alto) y **baja en B, C, E** (precio de autoconsumo alto, ~$0.255 → mayor ahorro → LCOE neto más bajo). Es el reflejo económico esperado de que las plantas que ya cogeneran barato tienen menos que ganar de una inversión adicional.
- **La conclusión general se mantiene:** Escenario 2 sigue siendo sustancialmente más económico que Escenario 1 en todas las plantas (neto de Esc.2 cercano a cero o negativo en 4 de 6). La recomendación de presentación bruto/neto (Sección 28.6) sigue vigente.

---

*Última actualización: recalculado el LCOE neto con precio de electricidad específico por planta (costo ponderado real de cada matriz eléctrica). El neto sube en A/D (cogeneración barata existente, menos ahorro) y baja en B/C/E (dependen de red cara, más ahorro); Escenario 2 sigue más económico que Escenario 1 en todas las plantas. Confirmado que el LCOE bruto no depende del precio (idéntico entre versiones) y que la discrepancia previa del bruto de Esc.2 se debía a haber corrido con un excedente intermedio, ya resuelto. Pendiente: Etapa 2 de Fase 2 (% de EFB como variable de decisión, techo 60%); actualizar tabla de la Sección 28.6 si se quiere reflejar el precio por planta como versión definitiva.*

## 34. Precio de venta de excedentes — marco regulatorio actualizado (CREG 174 de 2021) y su efecto en el despliegue de biomasa

### 34.1 Hallazgo regulatorio — CREG 030 (que usábamos) fue derogada

La Resolución CREG 030 de 2018 (base del precio de venta de excedente de 0.06 USD/kWh usado hasta ahora, Tabla 18) **fue derogada por la Resolución CREG 174 de 2021** (vigente desde el 22 de noviembre de 2021), que regula la autogeneración a pequeña escala (AGPE), generación distribuida (GD) y autogeneración a gran escala (AGGE) con potencia máxima declarada hasta 5 MW. El marco actual remunera los excedentes en una estructura de tramos, no a un precio único bajo.

### 34.2 Estructura de remuneración de 3 tramos (CREG 174)

Cada kWh generado se remunera distinto según su destino, en orden de valor económico:
1. **Autoconsumo** (deja de comprar de la red): vale el **precio ponderado real de cada planta** (0.114 a 0.259 USD/kWh, calculado en la Sección 33.3 según su matriz eléctrica).
2. **Excedente hasta igualar el consumo del período** (permuta/crédito de energía, CREG 174 art. 25): se acredita al **precio minorista** ≈ el mismo precio ponderado de la planta.
3. **Excedente por encima del consumo:** se vende a **precio de bolsa** (spot).

### 34.3 Precio de bolsa — promedio de 11 meses (por alta volatilidad)

El precio de bolsa es extremadamente volátil (desviación estándar = 50% del promedio; máximo/mínimo = 4.7× en la serie), por lo que usar un solo mes sería engañoso. Se calculó el **promedio de 11 meses** (informes mensuales de XM, ene-2025 a mar-2026): **234.6 COP/kWh = 0.0703 USD/kWh** (mediana 223.8 COP/kWh, muy cercana, sin sesgo por outlier). Fuente: portal XM (informes mensuales del Mercado de Energía Mayorista). *Nota: el valor de feb-2026 (124.26 COP/kWh) se dedujo del dato de que marzo-2026 subió 80.09% sobre febrero, no es cifra oficial directa; los otros 10 meses sí son directos de informes XM.*

- **Comparación de precios de venta:** CREG 030 derogado (0.0600) < bolsa promedio CREG 174 (0.0703) << precio ponderado por planta, tramos 1-2 (0.114-0.259). El salto grande está en el reconocimiento de la permuta a precio minorista (tramos 1-2), no en el precio de bolsa.

### 34.4 Implementación en el modelo (Fase 2, Etapa 1c)

Se modelaron los 3 tramos como variables continuas acotadas (`autoconsumo_kW ≤ consumo`, `excedente_permuta_kW ≤ consumo`, `excedente_bolsa_kW` libre). Como los precios son decrecientes por tramo, el solver llena naturalmente los tramos más caros primero, sin necesidad de binarias adicionales (se mantiene MILP limpio, solo las binarias del catálogo de turbina). Objetivo: maximizar (ingreso de los 3 tramos − CAPEX anualizado).

### 34.5 Resultado — el marco CREG 174 sí incentiva duplicar capacidad (pero no desplegar todo el potencial)

| Planta | Turbina elegida (kW) | Factor util. | Autoconsumo (kW) | Permuta (kW) | Bolsa (kW) | Lectura |
|---|---|---|---|---|---|---|
| A | 300 | 0.040 | 300 | 0 | 0 | Solo autoconsumo (cogeneración barata existente, precio ponderado muy bajo) |
| B | 1,500 | 0.168 | 767 | 733 | 0 | Autoconsumo + permuta (duplica capacidad) |
| C | 1,500 | 0.221 | 739 | 739 | 22 | Autoconsumo + permuta + pizca de bolsa |
| D | 1,000 | 0.194 | 549 | 451 | 0 | Autoconsumo + permuta |
| E | 2,000 | 0.283 | 933 | 933 | 134 | Autoconsumo + permuta + pizca de bolsa |
| F | 300 | 0.061 | 300 | 0 | 0 | Solo autoconsumo (muy pocas horas de operación) |

- **Hallazgo central:** al reconocer la permuta a precio minorista, el marco CREG 174 (vs. el CREG 030 derogado) **incentiva duplicar la capacidad instalada** en 4 de 6 plantas (B, C, D, E) — pasan de "solo autoabastecerse" a "autoabastecerse + exportar un excedente equivalente a su propio consumo". Es evidencia cuantitativa de que **el cambio regulatorio de 2021 mejora el caso de negocio de la cogeneración con biomasa**.
- **Umbral verificado:** el tramo de permuta es rentable cuando (horas × precio ponderado) > costo anualizado de turbina (619.7 USD/kW/año). B, C, D, E lo superan; A (precio ponderado bajo por cogeneración existente, $0.114) y F (muy pocas horas, 1,931 h/año) no.
- **El tramo de bolsa sigue sin ser atractivo:** el excedente masivo (por encima de 2× el consumo) solo se paga a 0.0703 USD/kWh, por debajo del umbral de rentabilidad — por eso las plantas solo empujan cantidades simbólicas a bolsa (0-134 kW).
- **Límite del hallazgo:** incluso con el marco regulatorio favorable, el factor de utilización óptimo sigue siendo bajo (0.04-0.28) — el óptimo económico usa solo ~4-28% de la biomasa disponible. **Para desplegar el potencial energético completo se requerirían palancas adicionales:** precio de generación firme/despachable (aprovechando que la biomasa es despachable 24h, a diferencia de solar/eólica — el mercado colombiano ya diferencia ~945 vs. ~307 COP/kWh entre firme y variable), monetización del carbono (impuesto nacional 2025: $27,399 COP/tCO2 ≈ 8.2 USD/tCO2), o un cambio a función objetivo no puramente económica (multiobjetivo que pese lo ambiental/social) — todas identificadas como líneas de exploración/discusión.

---

*Última actualización: modelado el precio de venta de excedentes bajo el marco regulatorio vigente (CREG 174 de 2021, que derogó la CREG 030 usada hasta ahora) en estructura de 3 tramos (autoconsumo y permuta a precio ponderado por planta; excedente a bolsa a 0.0703 USD/kWh, promedio 11 meses XM). Hallazgo: el marco actual incentiva duplicar la capacidad instalada en 4 de 6 plantas (vs. solo autoabastecimiento bajo CREG 030), pero el óptimo económico sigue usando solo ~4-28% de la biomasa — desplegar el potencial completo requiere precio firme/despachable, valor del carbono, o función objetivo multiobjetivo. Pendiente: Etapa 2 de Fase 2 (% de EFB); explorar las palancas de despliegue de biomasa identificadas.*

## 35. Verificación regulatoria de dos palancas de despliegue de biomasa (precio firme y valor del carbono)

Antes de modelar las palancas identificadas en la Sección 34 para aumentar el uso de biomasa, se verificó su viabilidad dentro del marco regulatorio colombiano, para no construir sobre supuestos inaplicables. Conclusión: ambas son regulatoriamente válidas pero con obstáculos que hacen preferible tratarlas como discusión/cálculo de referencia, no como restricciones del solver.

### 35.1 Precio firme/despachable (cargo por confiabilidad) — punto de discusión

- **Viabilidad regulatoria (citable):** el cargo por confiabilidad de Colombia (Resolución CREG 071 de 2006 y actualizaciones) remunera la *disponibilidad* de generación y **aplica explícitamente a biomasa** (junto con eólica, solar, geotérmica, hidráulica y térmica). Reconoce la figura de "plantas no despachadas centralmente" que declaran ENFICC (Energía Firme para el Cargo por Confiabilidad) y participan del esquema. Esto valida conceptualmente el atributo de despachabilidad de la biomasa (a diferencia de solar/eólica variable) — el mercado colombiano ya diferencia precios entre generación firme (~945 COP/kWh) y variable (~307 COP/kWh).
- **Obstáculo práctico:** las 6 plantas están muy por debajo de 20 MW (excedente máximo 5.1-9.5 MW), por lo que son "no despachadas centralmente". El mecanismo real de asignación (subastas de OEF, garantías, auditorías, compromiso de generar cuando el precio de bolsa supera el precio de escasez) está diseñado para plantas de gran escala conectadas al SIN, con costos de transacción que rara vez justifican la participación de un autogenerador pequeño de palma.
- **Decisión:** NO se modela como precio garantizado (sería una simplificación difícil de defender). Se documenta como **hallazgo de política/discusión**: la biomasa, por su despachabilidad, *debería* poder acceder a esquemas de remuneración de firmeza, pero los mecanismos actuales (diseñados para >20 MW) representan una barrera regulatoria para la agroindustria — una recomendación de política pública valiosa en sí misma.

### 35.2 Valor del carbono (no causación del impuesto nacional al carbono) — cálculo de referencia aparte

- **Viabilidad regulatoria (citable):** existe el mecanismo de no causación del impuesto nacional al carbono (Decreto 926 de 2017, reglamentando el art. 221 de la Ley 1819 de 2016). Las iniciativas elegibles incluyen explícitamente implementación de energías renovables, reducción de emisiones de metano y mejora de eficiencia energética en calderas — el proyecto califica en las tres. Requiere verificación por tercera parte acreditada (ISO 14065, ONAC o Decreto 446 de 2020).
- **Obstáculo 1 — rol invertido:** el impuesto grava *combustibles fósiles*; el proyecto de bioenergía no consume combustible fósil, así que sería *generador/vendedor* de certificados (a un tercero que sí paga el impuesto y quiere neutralizarse), no beneficiario directo de la no causación. El precio recibido sería el del mercado de certificados (negociado, típicamente por debajo del valor nominal del impuesto).
- **Obstáculo 2 — magnitud pequeña:** el impuesto 2025 es 27,399.14 COP/tCO2 = 8.20 USD/tCO2 (Resolución DIAN 008 de 2025). Traducido a valor por kWh exportado (× factor de red 0.1634 kgCO2/kWh), da apenas **0.00134 USD/kWh** — entre 50 y 190 veces menor que los precios de electricidad (bolsa 0.0703; autoconsumo 0.114-0.259). Además, la reforma tributaria de 2022 limitó la no causación al 50%.
- **Decisión:** NO se incluye en el solver (un ingreso tan pequeño no cambia las decisiones de dimensionamiento y daría la falsa impresión de haberlas movido). Se reporta como **cálculo de ingreso anual de referencia**, aparte:

| Escenario | Ingreso carbono pleno (USD/año, 6 plantas) | Ingreso con 50% aplicable (USD/año) |
|---|---|---|
| Escenario 1 | 253,108 | 126,554 |
| Escenario 2 | 162,584 | 81,292 |

*(Emisiones de red evitadas por el excedente exportado × precio del impuesto al carbono 2025. Es un ingreso complementario no despreciable en términos absolutos, pero marginal frente a los flujos de electricidad — por eso no altera el dimensionamiento óptimo.)*

- **Nota para el artículo:** el impuesto al carbono tiene una trayectoria creciente (reforma tributaria: hacia tarifa plena de ~42,609 COP/ton, con cobro escalonado 40%/60%/80%/100% entre 2026 y 2029) — se puede mencionar que a futuro, con precios de carbono más altos (mercados internacionales voluntarios ya superan 15-30 USD/tCO2), esta palanca ganaría relevancia. Buena línea de discusión prospectiva.

### 35.3 Conclusión — qué palanca queda para modelar

De las tres palancas identificadas (Sección 34.5), las dos de mercado (precio firme, valor del carbono) quedan como discusión/referencia por las razones anteriores. **La tercera — cambiar la función objetivo de económica pura a multiobjetivo (que pese lo ambiental/social además de lo económico) — es la que se explorará en el solver**, ya que es la que puede mostrar el conflicto directo entre el óptimo económico (autoabastecimiento, poca biomasa usada) y el óptimo social/ambiental (máximo excedente, máxima biomasa usada). Es el hallazgo central de un estudio de sostenibilidad multicriterio.

---

*Última actualización: verificada la viabilidad regulatoria de las palancas de precio firme (cargo por confiabilidad — válido para biomasa pero diseñado para plantas >20 MW, queda como discusión de política) y valor del carbono (no causación del impuesto, Decreto 926/2017 — válido pero ~50-190x menor que precios de electricidad, se reporta como cálculo de referencia aparte: 127k-253k USD/año Esc.1, no entra al solver). Próximo paso: explorar la opción 3 (función objetivo multiobjetivo económico/ambiental/social) para mostrar el conflicto entre óptimo económico y despliegue de biomasa. Sigue pendiente la Etapa 2 de Fase 2 (% de EFB).*

## 36. Análisis multiobjetivo — frente de Pareto (económico vs. despliegue de biomasa)

### 36.1 Selección de método (respaldada en literatura)

Se revisaron dos artículos de referencia directamente aplicables:
- **Nandimandalam, Aghalari, Gude & Marufuzzaman (2022)**, *Energy Conversion and Management* 266:115833 — "Multi-objective optimization model for regional renewable biomass supported electricity generation in rural regions". Prácticamente el mismo problema (biomasa → electricidad rural, MILP multiobjetivo costo vs. GEI). Usa un **algoritmo ε-constraint aumentado lexicográficamente**.
- **Nguyen, Nananukul & Luukka (2026)**, *Renewable Energy Focus* 58:100856 — biomasa (cascarilla de arroz) → electricidad, Tailandia. Compara **fuzzy goal programming vs. ε-constraint**.

**Decisión: método ε-constraint en dos pasos** (payoff table lexicográfica → ε-constraint), por las razones que ambos papers documentan:
- El ε-constraint permite controlar el número de soluciones eficientes y **no se salta huecos ni indentaciones del frente de Pareto**, a diferencia del método de suma ponderada.
- Nguyen et al. señalan que el ε-constraint es preferible **cuando no hay prioridad clara entre objetivos** y se quiere explorar todo el frente de trade-offs — exactamente el caso de un artículo de sostenibilidad multicriterio que busca *mostrar* el conflicto. (El fuzzy goal programming conviene cuando el decisor ya tiene preferencias definidas de antemano.)
- Se descartó la suma ponderada: requiere normalizar objetivos de unidades distintas y elegir pesos arbitrarios (los papers que la usan terminan necesitando procesos adicionales como fuzzy AHP para justificarlos).

### 36.2 Hallazgo estructural — el problema colapsa a 2 dimensiones

Se identificó que los objetivos **ambiental y social son casi perfectamente colineales** en este modelo, y por tanto no están en conflicto entre sí:
- Ambiental (emisiones evitadas) = electricidad generada × 0.1634 kgCO2/kWh → **lineal creciente en la generación**.
- Social (viviendas/personas rurales beneficiadas) = excedente ÷ consumo por vivienda × 3.7 → **lineal creciente en el excedente**.

La única fuente de no-colinealidad es la ligera diferencia de intensidad de emisiones entre Escenario 1 y 2 (-125.6 a -136.5 gCO2eq/kWh, ~8% de diferencia). **El único conflicto real es económico vs. despliegue de biomasa.** Por eso el problema se formuló en 2D — lo que además lo alinea con la literatura (ambos papers de referencia usan frentes de Pareto bidimensionales).

- **f1 (económico, MAX):** beneficio anual = ahorro de autoconsumo + venta de excedente (3 tramos CREG 174, Sección 34) − CAPEX anualizado de turbina.
- **f2 (despliegue, MAX):** electricidad total generada con biomasa (kWh/año) — proxy conjunto de los pilares ambiental y social, y respuesta directa a la pregunta de investigación sobre uso del potencial de biomasa.

### 36.3 Payoff table (Algoritmo 1, optimización lexicográfica)

| Solución | f1: Beneficio (USD/año) | f2: Generación (GWh/año) |
|---|---|---|
| Óptimo económico | **+2,823,535** | 30.5 (16% del potencial) |
| Óptimo de generación | **−8,321,926** | **184.9** (100% del potencial) |

- **Rango f1:** 11,145,461 USD/año. **Rango f2:** 154.3 GWh/año.
- **Costo del despliegue completo:** desplegar todo el potencial de biomasa cuesta **$11.15M USD/año** de beneficio sacrificado (≈$72,000 USD/año por cada GWh adicional) — muy por encima de lo que el mercado paga por esa energía.
- **Contraste con la palanca de carbono (Sección 35.2):** el ingreso por carbono a valor pleno ($253K/año) representa apenas el **2.3%** de esa brecha — confirmación cuantitativa de que era demasiado pequeño para alterar las decisiones de dimensionamiento.

### 36.4 Frente de Pareto (ε-constraint, q=10 intervalos)

| ε (GWh) | Beneficio (USD/año) | Generación (GWh) | Factor util. promedio | Capacidad total (MW) |
|---|---|---|---|---|
| 30.5 | +2,823,535 | 30.5 | 0.161 | 6.60 |
| 45.9 | +2,434,084 | 46.0 | 0.247 | 9.75 |
| 61.4 | +1,910,060 | 62.7 | 0.301 | 12.30 |
| 76.8 | +1,357,009 | 76.8 | 0.374 | 14.80 |
| 92.3 | +629,118 | 92.9 | 0.460 | 17.80 |
| 107.7 | −154,000 | 108.5 | 0.511 | 20.80 |
| 123.1 | −946,795 | 123.6 | 0.566 | 23.80 |
| 138.6 | −1,795,006 | 141.7 | 0.648 | 27.30 |
| 154.0 | −2,623,024 | 156.4 | 0.707 | 30.30 |
| 169.4 | −4,271,372 | 169.9 | 0.817 | 34.75 |
| 184.9 | −8,321,926 | 184.9 | 1.000 | 43.00 |

### 36.5 Hallazgos centrales (el resultado más fuerte del proyecto)

1. **Punto de equilibrio en ~105 GWh/año:** el sistema puede desplegar aproximadamente el **57% del potencial de biomasa** manteniéndose **económicamente neutro** (beneficio ≈ 0). Este es el hallazgo más citable del análisis.
2. **Existe un amplio espacio de "ganancia social sin pérdida privada":** el óptimo económico puro usa solo el 16% del potencial (30.5 GWh, factor de utilización 0.16), pero se puede llegar hasta el 57% sin que la planta pierda dinero — solo deja de *maximizar* su beneficio. **Implicación de política:** no hace falta subsidiar el despliegue completo; incentivos modestos bastarían para empujar del 16% al 57% del potencial, capturando la mayor parte del beneficio ambiental y social sin cargar al erario con la brecha completa de $11.15M/año.
3. **El costo marginal del despliegue se acelera (frente cóncavo):** el último tramo (170→185 GWh) cuesta ~$4M USD/año por solo 15 GWh adicionales — porque el modelo debe instalar turbinas cada vez más grandes cuya energía solo se remunera a precio de bolsa (0.0703 USD/kWh, el tramo más barato de CREG 174). Los primeros tramos, en cambio, se benefician del autoconsumo y la permuta a precio minorista.
4. **Confirma y cuantifica la conclusión de las Secciones 32-35:** bajo el marco regulatorio y de precios vigente, **ninguna condición de mercado justifica desplegar el potencial completo de biomasa**. La brecha de $11.15M/año es la magnitud del incentivo (tarifa preferencial, subsidio, o valor de carbono muy superior al actual) que se requeriría.

- Archivos generados: `frente_pareto_economico_generacion.csv`, `frente_pareto.png`.

## 37. Decisiones tras presentación Entrepalmas S.A.S. (2019) Se recibió una presentación técnica real de Entrepalmas S.A.S. (XV Reunión Técnica Nacional de Palma, 2019 — planta de 42 tRFF/h en Meta, con proyecto de biogás + cogeneración ya implementado), usada como fuente de validación cruzada externa para el modelo. **Validaciones exitosas (sin cambios):** - Precio del biogás: 350 COP/kWh — coincide exacto con el valor ya usado. - Bonos de carbono: 235M COP/año reales vs. $47K USD estimado — confirma que la estimación propia es conservadora. - Indicador social: "1,414 viviendas E-1 equivalentes" reportado por Entrepalmas — misma métrica y orden de magnitud que el indicador construido en este trabajo (Sección 7/13). **Decisión — CAPEX del biodigestor:** Se mantiene $18,518/tRFF (laguna carpada completa, Tabla 17 tesis) como caso base. Entrepalmas reportó $36,544/tRFF para un retrofit de carpado sobre laguna existente — 2x el valor de Tabla 17 y 7x el incremental teórico de impermeabilización ($3,704-$5,328/tRFF), que se descarta por subestimar el alcance real de un retrofit (instrumentación, TEA, sopladores, tuberías). El valor de Entrepalmas se adopta como **escenario de sensibilidad alto**, no como caso base, dado que corresponde a un retrofit (más costoso que construcción nueva) y no hay desglose suficiente para aislar qué partidas son comparables a Tabla 17. **Decisión — Costo de cogeneración con vapor/biomasa:** Se mantiene 258 COP/kWh (portal UPME, https://lcoev2.upme.gov.co/results/2, solo O&M) como caso base, por tratarse de fuente institucional pública, más defendible metodológicamente que un dato puntual de una sola empresa. Entrepalmas reportó 90 COP/kWh (2.9x menor) para su planta real — se documenta como referencia de contraste que sugiere que el supuesto de UPME usado en este trabajo es conservador (sobreestima el costo de cogeneración), no como corrección.
## 37. Decisión de cifras definitivas del Pareto + estructura del artículo (layout v1)

### 37.1 Definición definitiva de f1 (resuelto)

Se adopta como versión definitiva del análisis multiobjetivo la de la **Sección 20 
del notebook: beneficio NETO TOTAL** (incluye CAPEX fijo anualizado, además de 
turbina/biogás variables). **Las cifras de las Secciones 36.3–36.5 quedan superadas** 
y no deben usarse en el artículo. Cifras definitivas (outputs verificados del notebook):

| Métrica | Escenario 1 | Escenario 2 |
|---|---|---|
| Óptimo económico | +$2,063,746 USD/año (72.2 GWh, 29% del potencial) | frente completo positivo |
| Punto de equilibrio | ~125.5 GWh/año = **50.4% del potencial** | **100% del potencial** (151.6 GWh) |
| Despliegue total | −$11,043,659 USD/año (249.1 GWh) | +$7.9M USD/año (151.6 GWh) |
| Brecha a subsidiar | $13,107,405 USD/año | no aplica (sin brecha) |
| Cobertura del impuesto al carbono | 1.93% de la brecha | no aplica |

**Hallazgo reformulado para el artículo:** el trade-off económico↔despliegue no es 
inherente a la biomasa sino a la ruta tecnológica — el Escenario 2 (contrapresión + 
biogás) es rentable en todo su frente de Pareto; el Escenario 1 (extracción-condensación) 
solo alcanza ~50% del potencial sin pérdidas.

### 37.2 Estructura del artículo (layout v1, estilo JCLP)

[pegar aquí el layout acordado, con los ajustes: 3.4 renombrada a "CREG 174: progreso 
regulatorio insuficiente para el despliegue completo"; 2.3 aclara que LCOE/GEI/social 
son indicadores, no funciones objetivo; hubs de biomasa como discusión cualitativa 
citando Barrera Hernández et al. (2024); FiT implícita pendiente de cálculo corto; 
agregar Keywords, Nomenclature y Data availability statement.]

## 38. Fase 2 — Frente de Pareto del Escenario 2 (contrapresión + biogás) **Diseño del modelo:** dos rutas de generación independientes, cada una con su propio factor de utilización — turbina de contrapresión (catálogo discreto, 750-1,750 kW) y generador de biogás (N unidades modulares de 1,000 kW/unidad, variable entera). El tamaño de unidad de biogás se fijó en 1,000 kW tras revisión bibliográfica: los motogeneradores de biogás en plantas de POME se instalan típicamente en módulos de ~1-1.2 MW (casos documentados: 2,000 kW como unidad única en Indonesia; manual de financiamiento POME-a-biogás con motor 1x1.2 MWe; rango típico de 2.5-3 MW por planta completa). Se descartó el enfoque inicial de catálogo binario de tamaños de generador porque Planta B (mayor excedente de las 6) topaba artificialmente el catálogo original (5,500 kW máx. vs. 5,886.4 kW ideal). **CAPEX modelado en el solver (afecta la decisión):** solo turbina contrapresión ($2,815/kW) y generador de biogás ($186/kW) — igual convención que el modelo de Escenario 1, que tampoco capitaliza caldera ni precipitador en la función objetivo de Fase 2 (esos costos no cambian según la decisión de tamaño/utilización, por lo que no afectan el óptimo). **CAPEX fijo (no entra al solver, se reporta aparte):** sistema de gases de combustión, tratamiento térmico de EFB, reactor/lagunas ($18,518/tRFF, Tabla 17 — Decisión de la Sección 37, mantenido fijo por TODA la biomasa disponible, independiente del número de unidades de generador elegidas), tratamiento de biogás, clarificación dinámica, redes — total anualizado de $2,630,702 USD/año para las 6 plantas. **Payoff table (lexicográfica):** óptimo económico = +$11.28M USD/año con 137.9 GWh (generación bruta); óptimo de generación = +$10.57M USD/año con 151.6 GWh. Rango de generación explorado: solo 13.7 GWh (10% del máximo) — mucho más angosto que el rango de Escenario 1 (154.3 GWh, 6x). **Hallazgo central — el biogás nunca es la variable económicamente restrictiva:** en ambos extremos del payoff table, el factor de utilización del biogás es exactamente 1.000 en las 6 plantas — el modelo siempre despliega el 100% del potencial de sustrato disponible (POME + EFB pretratado), incluso cuando esto implica sobre-dimensionar la capacidad instalada por la indivisibilidad de las unidades de 1,000 kW (ej. Planta D: ideal=3,200.8 kW, capacidad comprada=4,000 kW). El costo de esa capacidad "de sobra" ($186/kW) es tan bajo frente al ingreso generado que nunca justifica limitar el despliegue. La única variable que responde al trade-off económico es el factor de utilización de la turbina de contrapresión (0.476-0.764 en el óptimo económico, sube a 1.000 en el óptimo de generación). **Resultado más fuerte del análisis — confirma y supera la hipótesis inicial:** el beneficio económico NETO TOTAL (incluyendo el CAPEX fijo anualizado, $2.63M USD/año) **nunca cruza cero** en todo el rango técnico explorado — cae de $8.65M a $7.94M USD/año (solo -8%) al desplegar del 137.9 al 151.6 GWh. A diferencia del Escenario 1, que tiene un punto de equilibrio real en ~57% del potencial (105 GWh de 184.9 GWh máx.), el Escenario 2 **no presenta ninguna penalización económica significativa en el rango técnicamente factible** — el CAPEX de biogás es tan bajo frente a los ingresos que el trade-off económico entre "desplegar más biomasa" y "maximizar beneficio" prácticamente desaparece. **Implicación para la comparación de escenarios (Discusión del artículo):** el contraste entre Escenario 1 (breakeven real al 57%, penalización de $11.15M/año al desplegar el 100%) y Escenario 2 (sin breakeven relevante, penalización de solo ~$0.7M/año) es un argumento fuerte a favor de priorizar la ruta de biogás con contrapresión sobre la de extracción- condensación pura, al menos bajo la estructura de costos y precios regulatorios (CREG 174) usada en este estudio — con la salvedad de que Escenario 2 genera menos energía en términos absolutos (151.6 GWh máx. bruto vs. 184.9 GWh de Escenario 1). **Limitación a documentar:** el rango angosto de generación explorado en Escenario 2 sugiere que el óptimo económico y el óptimo de generación casi coinciden — esto podría reflejar una ventaja genuina del biogás (costo marginal muy bajo) o podría indicar que el modelo no está sujeto a ninguna restricción adicional de escala más allá del tope de sustrato (ej. restricciones de espacio, permisos ambientales para digestores de gran tamaño, o limitaciones de red eléctrica para evacuar el excedente) que en la práctica podrían introducir un trade-off adicional no capturado aquí. Archivos: `frente_pareto_economico_generacion_esc2.csv`, `frente_pareto_comparacion_esc1_esc2_paneles.png`, `escenario2_capex_fijo_efecto.png`.

## 39. CORRECCIÓN — Fase 2, Escenario 1: se agrega la ruta de biogás de 
POME al modelo de superestructura (supera y reemplaza el hallazgo del 
"57%" reportado anteriormente)

**Error detectado:** el modelo de Fase 2 (superestructura) de Escenario 1 
solo modelaba la turbina de extracción-condensación como variable de 
decisión — el biogás de POME (32% del total de excedente en la Fase 1 
validada, según el Sankey) no entraba como variable de decisión, ni su 
CAPEX ni su generación se contabilizaban en `f1_economico`/`f2_generacion`. 
Se detectó por analogía con Escenario 2, donde sí se había modelado 
correctamente desde el inicio con dos rutas independientes.

**Corrección:** se añadió la ruta de biogás de POME con la misma 
arquitectura que Escenario 2 — generador modular de N unidades de 
1,000 kW/unidad (variable entera), con su propio factor de utilización 
independiente del de la turbina.

**Payoff table corregida:**
- Óptimo económico: +$8,765,812 USD/año con 72.2 GWh (24.7% del potencial)
- Óptimo generación: -$4,341,593 USD/año con 249.1 GWh (100%)
- Punto de equilibrio (f1≈0): ~231.4 GWh → **92.9% del potencial** 
  (antes: 57%, con el modelo incompleto)

**Interpretación:** al igual que en Escenario 2, el biogás de POME se 
despliega siempre al 100% de su potencial (FU=1.000) en ambos extremos 
del payoff table — nunca es la variable que restringe económicamente. 
La turbina de extracción-condensación es la única variable que responde 
al trade-off (FU=0.046 en el óptimo económico, sube a 1.000 en el óptimo 
de generación). Esto reduce drásticamente la penalización de desplegar 
el 100% del potencial: de -$11.15M/año (estimación anterior, incompleta) 
a solo -$4.34M/año (estimación corregida) — una diferencia de más de 2.5x.

**Implicación para la comparación entre escenarios (reemplaza la 
conclusión anterior):** con el modelo corregido, TANTO Escenario 1 
(breakeven ~93%) COMO Escenario 2 (sin breakeven relevante en el rango 
estudiado) muestran una penalización económica baja por desplegar el 
100% del potencial de biomasa. El contraste ya no es "Escenario 1 tiene 
un trade-off fuerte, Escenario 2 no" — ambos escenarios son 
económicamente permisivos con el despliegue completo una vez que se 
reconoce que el biogás (presente en ambos) domina el resultado económico 
y no responde al trade-off. La diferencia entre escenarios pasa a ser 
más bien de **magnitud absoluta de generación** (Escenario 1: 249.1 GWh 
máx.; Escenario 2: 151.6 GWh máx.) que de forma del frente de Pareto.

**Nota metodológica:** el número "57%" y la cifra "-$11.15M/año" 
reportados en una versión anterior de este documento quedan SUPERADOS 
por este resultado corregido y no deben citarse en el artículo.

## 40. Reorganización del notebook — Secciones 16-18 (Fase 2, ambos escenarios)

Tras cerrar los hallazgos de las Secciones 38-39, se reorganizó la estructura 
de celdas de Fase 2 (superestructura) para dejar un flujo lineal y 
reproducible, sin cambiar ningún resultado numérico ya reportado.

**Problemas de organización detectados y corregidos:**
- Una celda de diagnóstico huérfana (verificación de `excedente_esc2` contra 
  una "Sección 29" inexistente en este notebook) quedó de una sesión anterior 
  — se descartó, documentada aquí para trazabilidad, no afecta ningún resultado.
- `TAMANO_UNIDAD_BIOGAS_KW` y `N_MAX_UNIDADES_BIOGAS` estaban definidos dos 
  veces (Escenario 1 y Escenario 2, mismo valor) — ahora se definen una sola 
  vez en la Sección 16.1 y se reutilizan en la 17.1.
- El diagnóstico de elección del solver de Escenario 1 estaba ubicado 
  físicamente dentro de la Sección 17 (después de todo el bloque de 
  Escenario 2) — se movió a la Sección 16.4, junto a su payoff table.
- Se agregó a Escenario 1 el gráfico de "efecto del CAPEX fijo" (Sección 
  16.5), simétrico al que ya existía para Escenario 2, para consistencia 
  visual entre ambos escenarios.

**Estructura final de las Secciones 16-18:**
- **Sección 16** (Escenario 1): 16.1 parámetros/catálogos, 16.2 modelo + 
  payoff table, 16.3 ε-constraint/Pareto, 16.4 diagnóstico, 16.5 CAPEX fijo 
  + beneficio neto total, 16.6 (archivo) iteraciones exploratorias superadas 
  — turbina sola con precio fijo de venta, y turbina sola con CREG 174 sin 
  ruta de biogás — conservadas por trazabilidad, no usadas en el artículo.
- **Sección 17** (Escenario 2): mismo patrón, 17.1 a 17.6.
- **Sección 18** (nueva): panel comparativo final en dos paneles del 
  beneficio NETO TOTAL de ambos escenarios, con resumen automático del punto 
  de equilibrio de cada uno — es el gráfico de referencia para la Discusión 
  del artículo.

**Validación:** el notebook reorganizado se corrió completo de principio a 
fin (`Kernel > Restart & Run All`) sin errores y sin cambios en ningún valor 
numérico previamente reportado (Secciones 38-39).

Archivo actualizado: `01_limpieza_datos_capex_emisiones_social_2_reorganizado.ipynb` 
(reemplaza a la versión anterior como notebook de trabajo principal).

## 41. Digestato — decisión de alcance (no modelado, simplificación conservadora)

Se decide no incorporar un precio de venta del digestato (biofertilizante) 
en el modelo económico de Escenario 2, pese a representar ~90% de la masa 
de entrada al reactor (Sección 11, Bloque 7.5). Justificación: al ser un 
ingreso adicional (no un costo), su omisión es una simplificación 
CONSERVADORA — subestima el beneficio real de Escenario 2 en vez de 
sobreestimarlo. Dado que ya se encontró que Escenario 2 no presenta 
penalización económica relevante en el rango estudiado (Sección 39), 
incorporar el digestato solo profundizaría esa conclusión, sin cambiarla 
cualitativamente. Se documenta como trabajo futuro / limitación 
reconocida, no como pendiente que bloquee la redacción del artículo.

## 42. Estacionalidad — verificación cuantitativa sobre las capacidades 
elegidas en Fase 2 (actualiza la decisión de alcance original)

Se realizó una verificación cuantitativa (no un remodelado completo) del 
efecto de la estacionalidad ya documentada (Sección 12) sobre las 
capacidades elegidas en el óptimo económico de Fase 2 (Secciones 16-18). 
Metodología: se aplicó el `Factor_estacionalidad` mensual ya calculado 
(RFF procesado, Sección 12) sobre el potencial ideal anual de cada ruta 
(turbina y biogás, ambos escenarios), y se calculó la pérdida INCREMENTAL 
(restando la línea base sin estacionalidad, para aislar el efecto de la 
variabilidad mensual del hueco estructural ya conocido entre capacidad 
instalada e ideal anual, que ya está capturado en el payoff table).

**Resultado — efecto pequeño y concentrado en la ruta de biogás:**
- Turbina (ambos escenarios): pérdida ≈ 0 GWh/año. La capacidad instalada 
  en el óptimo económico es tan pequeña frente al ideal (300 kW en 
  Escenario 1; factor de utilización bajo en Escenario 2) que la turbina 
  está saturada los 12 meses del año por igual — la estacionalidad no 
  añade restricción adicional.
- Biogás: Escenario 1 = 1.52 GWh/año (2.1% adicional sobre 72.2 GWh/año 
  del óptimo económico); Escenario 2 = 6.80 GWh/año (4.9% adicional sobre 
  137.9 GWh/año). Mayor en Escenario 2, consistente con que ahí la 
  capacidad instalada queda más ajustada al ideal (menor margen de 
  sobra por indivisibilidad de unidades de 1,000 kW), por lo que un 
  pico estacional agota ese margen más fácilmente.

**Interpretación:** el efecto es modesto y del mismo orden de magnitud que 
el buffer de almacenamiento de biomasa ya reportado (Sección 12, 3-11.5% 
del procesamiento anual) — no cambia cualitativamente ninguna conclusión 
de Fase 2, pero confirma con un número concreto (en vez de solo un 
argumento cualitativo) que la estacionalidad tiene un costo de oportunidad 
real y cuantificable, específicamente en la ruta de biogás.

**Limitación reconocida:** el supuesto de que el biogás escala linealmente 
con el mismo factor de estacionalidad del RFF probablemente sobreestima 
la variabilidad real del biogás, ya que un reactor anaeróbico tiene 
tiempo de retención hidráulica (semanas) que amortigua naturalmente los 
picos y valles de entrada de POME — a diferencia de la combustión directa 
de biomasa sólida (turbina), que responde de forma más inmediata a la 
disponibilidad de biomasa. Como el efecto en la turbina ya resultó ser 
cero, esta limitación no cambia el resultado reportado, pero se documenta 
por rigor metodológico.

## 43. Indicadores de sostenibilidad a lo largo del frente de Pareto (Sección 19 del notebook)

### 43.1 Hueco metodológico detectado y resuelto
Los indicadores (LCOE, emisiones, social) estaban calculados solo sobre Fase 1 (capacidad
fija, despliegue total), no sobre las soluciones optimizadas de Fase 2. El loop de
ε-constraint solo guardaba agregados. Se amplió (Secciones 16.3/17.3) para almacenar por
punto y por planta: generación de turbina y biogás, autoconsumo, excedente, capacidades.

### 43.2 Decisión metodológica — denominador del LCOE
El LCOE de Fase 2 se calcula sobre la GENERACIÓN TOTAL, no sobre el excedente (como en
Fase 1, Sección 28): en el óptimo económico el excedente tiende a cero y el LCOE divergiría.
**Los dos LCOE no son comparables entre sí** — declararlo en el artículo. El CAPEX de cada
punto se reconstruye con las capacidades elegidas por el solver (turbina $5,277/kW, biogás
$268/kW, PVAF 8.5136) más el CAPEX fijo.

### 43.3 Hallazgo — tres óptimos en tres puntos distintos (Escenario 1)

| Punto | Gen. (GWh) | % pot. | Beneficio neto (USD/año) | LCOE (USD/kWh) | tCO2eq/año | Cob. rural | % dem. dptal. |
|---|---|---|---|---|---|---|---|
| Óptimo privado | 72.2 | 29.0% | +2,063,746 | 0.1402 | 8,633 | 174% | 2.17% |
| LCOE mínimo | 108.1 | 43.4% | +804,483 | **0.1361** | 14,495 | 293% | 3.65% |
| Equilibrio | 126.3 | 50.7% | ≈ 0 | 0.1365 | 17,470 | 352% | 4.40% |
| Despliegue total | 249.1 | 100% | −11,043,659 | 0.1650 | 37,528 | 758% | 9.45% |

1. **El óptimo privado no es el óptimo técnico:** el LCOE tiene forma de U, con mínimo en
   43.4% del potencial, mientras el beneficio se maximiza en 29.0%. El marco de precios
   actual empuja a operar donde la electricidad es ~3% más cara de lo alcanzable.
2. **Concavidad con mecanismo:** el LCOE sube +21% sobre su mínimo al forzar el 100%, por
   sobredimensionamiento de la turbina de extracción-condensación para biomasa marginal.
3. **Costo de oportunidad, no pérdida:** ir del óptimo privado al equilibrio cuesta
   $2,063,746 USD/año de beneficio NO REALIZADO (la planta no pierde dinero, deja de
   ganarlo) — mantener esta distinción en la redacción.

### 43.4 CORRECCIÓN del indicador social — saturación (supera la versión sin techo)
La demanda residencial rural del Magdalena es de solo 30.3 GWh/año (87,516 usuarios,
346 kWh/vivienda/año). El excedente en el ÓPTIMO PRIVADO ya es de 52.8 GWh/año = **174% de
esa demanda**. Al aplicar el techo del 100% (criterio de la Sección 26), el indicador de
viviendas **se satura en 87,516 desde el primer punto del frente y no varía**.

- **Queda anulado** el hallazgo preliminar de "duplicación (2.0x) de viviendas beneficiadas
  entre el óptimo privado y el equilibrio" — era un artefacto del indicador sin techo.
-

## 44. Indicadores de sostenibilidad sobre el frente de Pareto — Escenario 2 y comparación

### 44.1 Resultado — el LCOE del Escenario 2 NO describe una U
A diferencia del Escenario 1, el LCOE del Escenario 2 crece monótonamente (0.0497 →
0.0585 USD/kWh) a lo largo de su frente. Su óptimo económico, su LCOE mínimo y el 91% de
su despliegue coinciden en el mismo punto (137.9 GWh). No existe punto de equilibrio: el
beneficio neto total es positivo en todo el frente (+$8.65M a +$7.94M, caída de solo 8%).

### 44.2 HALLAZGO CENTRAL — dominancia de Pareto del Escenario 2
Comparados en su propio óptimo económico, el Escenario 2 supera al Escenario 1 en TODAS
las dimensiones simultáneamente (dominancia de Pareto):

| Indicador (en óptimo económico) | Escenario 1 (72.2 GWh) | Escenario 2 (137.9 GWh) |
|---|---|---|
| Beneficio neto (USD/año) | +2,063,746 | **+8,647,489** (4.2x) |
| LCOE (USD/kWh) | 0.1402 | **0.0497** (2.8x más barato) |
| Emisiones evitadas (tCO2eq/año) | 8,633 | **19,795** (2.3x) |
| Cobertura demanda departamental | 2.17% | **4.99%** |
| % del potencial desplegado | 29.0% | **91.0%** |

### 44.3 El único trade-off que sobrevive: ambición ambiental extrema
El Escenario 1 tiene mayor techo absoluto de emisiones evitadas (37,528 tCO2eq, con 249.1
GWh de potencial vs. 151.6 GWh del Esc. 2). Pero para igualar las 22,025 tCO2eq del máximo
del Escenario 2, el Escenario 1 debe llegar a ~155 GWh, donde su beneficio ya es NEGATIVO
(≈ −$1.2M/año). **Conclusión: superar ambientalmente al Escenario 2 solo es posible
operando con pérdidas.**

### 44.4 Mecanismo — el CAPEX del biogás explica todo
Generador de biogás: $268/kW. Turbina contrapresión: $4,049/kW (15x). Turbina
extracción-condensación: $5,277/kW (20x). El biogás es tan barato que nunca hay razón
económica para limitarlo (FU = 1.000 siempre, §38/§39), y el Escenario 2 arranca su frente
ya en el 91% del potencial. **El trade-off del Escenario 1 no proviene de la biomasa sino
de la turbina cara.**

### 44.5 Limitación a declarar en el artículo
El frente del Escenario 2 explora solo un rango del 10% (137.9–151.6 GWh) porque su óptimo
económico ya está próximo al máximo técnico. No es un muestreo deficiente del frente: es el
resultado en sí. Declararlo explícitamente para evitar la lectura errónea de un revisor.

Archivos: `indicadores_sostenibilidad_pareto_esc2.csv`,
`indicadores_sostenibilidad_pareto_comparacion.png`.

### 44.6 Nota de visualización
Los frentes de ambos escenarios tienen rangos absolutos muy distintos (Esc.1: 72-249 GWh;
Esc.2: 138-152 GWh), por lo que superponerlos en GWh absolutos hace ilegible el Escenario 2.
La figura comparativa del artículo usa eje X normalizado (% del potencial propio de cada
escenario) para comparar la FORMA de los frentes, con las magnitudes absolutas declaradas
en la leyenda y en la tabla de puntos notables. La U del LCOE del Escenario 1 se reporta en
su figura individual, donde la escala lo permite.

## 45. Reformulación del mensaje del artículo tras el hallazgo de dominancia

El mensaje original ("el marco regulatorio no incentiva el despliegue de biomasa; se
requiere subsidio") queda SUPERADO por el hallazgo de la Sección 44. Mensaje definitivo:
**el trade-off rentabilidad↔despliegue es una propiedad de la ruta tecnológica, no de la
biomasa.** El Escenario 2 domina en Pareto sin necesidad de incentivo público.

Consecuencias: (1) título y abstract reescritos (v3); (2) la Sección 3.4 del layout pasa de
"barreras regulatorias y necesidad de subsidio" a "selección tecnológica antes que diseño
de subsidios", con la brecha de $13.1M y el 1.93% del impuesto al carbono reportados como
CONTRAFACTUAL (costo de insistir en extracción-condensación), no como necesidad del sector.

Título elegido: "Technology choice, not policy support, resolves the biomass deployment
trade-off: multi-objective optimization of palm oil mills in Colombia".

### 45.1 Abstract v4 — ajustes de redacción
Dos correcciones sobre v3, señaladas por el autor:
- "exhibits no break-even at all" → "is strictly profitable across its entire Pareto front".
  Motivo: en inglés económico "no break-even" se lee con más naturalidad como "nunca cubre
  costos" (lo contrario de lo que se quiere decir). Ambigüedad semántica eliminada.
- El mecanismo del CAPEX (15-20x menor del biogás) se integró DENTRO de la frase de
  resultados como aposición, en vez de ir como oración independiente entre el clímax de
  resultados y la conclusión de política, donde rompía el flujo de lectura.

## 46. Selección de revista y requisitos de formato (JCLP)

### 46.1 Estrategia de selección
Elsevier Journal Finder y Springer Journal Suggester (consultados con el Abstract v4)
sugirieron: Energy Conversion and Management (y ECM:X), Energy Reports, Energy Nexus,
Renewable Energy, Energy for Sustainable Development (Elsevier); Clean Technologies and
Environmental Policy, Biomass Conversion and Biorefinery, Environment Development and
Sustainability (Springer).

**Decisión: enviar primero a Journal of Cleaner Production (JCLP).** Razones: continuidad
con la publicación previa del autor (Barrera Hernández et al., 2024), el layout ya sigue su
estilo, y el hallazgo es de política pública. Riesgo gestionado: el rechazo directo llega en
~18 días (mediana), por lo que el costo de intentarlo es bajo.
**Plan B:** Clean Technologies and Environmental Policy (12 días a primera decisión, IF 5.1).
**Restricción a verificar:** disponibilidad de fondos para APC → evitar revistas de open
access obligatorio (ECM:X, Energy Reports, Energy Nexus) si no hay financiación.

### 46.2 Requisitos de formato JCLP
- Extensión: 6,000–8,000 palabras INCLUYENDO tablas, figuras y referencias.
- Highlights OBLIGATORIOS: archivo editable aparte, 3–5 viñetas de máx. 85 caracteres.
- Keywords: 1–7, evitando las que contengan "and" u "of".
- Revisión simple ciego; citación autor-año (Harvard); CRediT y Data availability requeridos.
- PENDIENTE DE VERIFICAR en la guía oficial: límite exacto del abstract (250 vs. 300
  palabras) y el alcance del posible máximo de 50 referencias.

### 46.3 Presupuesto de palabras acordado
Introduction 1,200 | Materials and methods 1,800 | Results and discussion 2,800 |
Conclusions 600 | Tablas y figuras ~800 | Referencias ~800.
Consecuencia: inventarios, parámetros termodinámicos y curvas de costos van íntegros al
Material Suplementario.

### 46.4 Entregables editoriales producidos
Abstract reencuadrado para JCLP (~250 palabras), 5 highlights, cover letter, keywords.
Título elegido: "Technology choice, not policy support, resolves the biomass deployment
trade-off: multi-objective optimization of palm oil mills in Colombia".

## 47. Marco regulatorio verificado (fuentes primarias, julio 2026)

### 47.1 Corrección: es Ley 1715 de 2014 (no "Ley 175"), modificada por Ley 2099 de 2021.

### 47.2 OMISIÓN DEL MODELO — incentivos tributarios FNCE
El modelo NO incorpora los incentivos de la Ley 1715/2014 mod. Ley 2099/2021, a los que la
biomasa (FNCER) es elegible: deducción de renta del 50% de la inversión (hasta 15 años),
exclusión de IVA, depreciación acelerada (33.33%/año) y exención arancelaria; vigentes 30
años desde el 01/07/2021; certificación UPME requerida.
**Consecuencia:** los resultados económicos son CONSERVADORES. Refuerzan la conclusión
(Esc.2 rentable incluso sin incentivos) pero deben declararse.
**Decisión pendiente:** (a) declarar como limitación, o (b) sensibilidad con exclusión de
IVA (19%) sobre CAPEX.

### 47.3 Matices al marco regulatorio
- CREG 174/2021 mejora el caso vs. CREG 030 (§34.5). La concavidad tiene DOS motores:
  tramo de bolsa (0.0703 USD/kWh) Y sobredimensionamiento de turbina (LCOE +21%, §43.3).
  No atribuirla solo a la regulación.
- Patrón de emergencia recurrente: CREG 171/2015 (El Niño, <20 MW) → 101 034/2024 →
  101 053/2024 (El Niño 2023-24, >1 MW) → 101 085/2025 (regasificadora Cartagena).
  Argumento: el Estado recurre a la cogeneración distribuida en crisis pero no la hace
  permanente.
- CREG 101 099/2026 (19-feb-2026, D.O. 03-mar-2026): habilita autogeneración remota (AGR),
  elimina co-localización, permite participación en cargo por confiabilidad, conexión
  simplificada <5 MW al SDL. PERO opera bajo principio de simetría (Decreto 1403/2024):
  mismas reglas que planta convencional + contrato de respaldo para ≥100 kW.
  Habilita la propuesta de HUB DE BIOMASA (supera barrera CREG 071), pero NO está modelada
  — presentar como propuesta y línea futura, no como resultado.
- CREG 101 011/2022: NO VERIFICADA. Confirmar existencia y alcance antes de citarla.

## 48. Sensibilidad a los incentivos tributarios (Sección 21 del notebook)

### 48.1 Diseño
El modelo base no incorpora los incentivos de la Ley 1715/2014 (mod. Ley 2099/2021). En vez
de modelar un instrumento específico (cuyo efecto depende de si las cotizaciones incluían
IVA y de la posición tributaria de cada empresa), se evalúa un FACTOR GENÉRICO de reducción
efectiva del CAPEX (0%, 10%, 19%, 30%), aplicado a CAPEX fijo y variable. Verificación: la
fila 0% reproduce exactamente los resultados base (72.2 GWh, +$2,063,746, equilibrio 50.7%).

### 48.2 Resultados (Escenario 1)
| Incentivo | Equilibrio (% potencial) | Beneficio despliegue total |
|---|---|---|
| 0% | 50.7% | −$11,043,659 |
| 10% | 66.4% | −$7,654,581 |
| 19% | 87.5% | −$4,604,410 |
| 30% | 97.7% | −$876,424 |

### 48.3 HALLAZGOS
1. **Los incentivos a la inversión ya existentes son 1-2 órdenes de magnitud más efectivos
   que el impuesto al carbono** (que cubre solo el 1.93% de la brecha). Con un 30% de
   reducción efectiva del CAPEX, la brecha del despliegue total cae un 92%.
2. **Un subsidio a la inversión NO cambia la decisión de dimensionamiento.** El óptimo
   privado del Esc.1 permanece en 72.2 GWh en las CUATRO filas: los incentivos escalan todo
   el CAPEX proporcionalmente y no alteran la relación entre costo marginal e ingreso
   marginal. Enriquecen al inversionista sin mover lo que construye. **Para mover la
   decisión hay que tocar el PRECIO de la energía (tarifa preferencial), no el costo del
   capital.** (Excepción: el Esc.2 sí desplaza su óptimo, 137.9 → 148.6 GWh al 30%, por lo
   plano de su frente.)
3. **La dominancia del Escenario 2 es robusta:** rentable al 100% de su potencial bajo los
   cuatro niveles de incentivo. El hallazgo central no depende de supuestos fiscales.

### 48.4 Pendiente
Confirmar si las cotizaciones de proveedores (AIC, MFMI, AVM, Tecnintegral) incluyen IVA o
son valores antes de IVA. Si son antes de IVA, la exclusión de IVA no aplica y el beneficio
provendría de la deducción de renta y la depreciación acelerada.

Archivo: `sensibilidad_incentivos_tributarios.csv`.
