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

## 16. Enfoque de modelado (a partir de estos datos limpios)

- Modelo de optimización en **Python/Pyomo**, formulado como LP/MILP según la fase (ver plan de trabajo), usando los datos limpios de este documento como parámetros de entrada.
- Selección de la mejor configuración mediante marco de sostenibilidad multicriterio (técnico, económico, ambiental, social) aplicado sobre los resultados del modelo.

---

*Última actualización: pendiente ensamblar el modelo Pyomo completo (Secciones 9-11 del notebook: Línea base, Escenario 1, Escenario 2 para Planta A) y determinar el flujo de material inerte/digestato del reactor de biogás.*
