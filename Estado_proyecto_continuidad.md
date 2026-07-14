# Estado del proyecto — Resumen para continuar en nuevo chat

**Instrucciones:** pega este documento completo como primer mensaje del chat nuevo, junto con (1) `Notas_metodologicas_articulo.md` y (2) el notebook actualizado.

---

## Qué es este proyecto

Artículo científico (Cap. 5 de tesis doctoral): valorización energética de biomasa residual de palma de aceite, **6 plantas extractoras del Magdalena, Colombia**. Compara 3 configuraciones (Línea base, Escenario 1, Escenario 2) con modelo **Python/Pyomo/GLPK**. El autor aprende Python desde cero.

## Archivos

- **GitHub:** `https://github.com/juncal0/valorizacion-biomasa-palma`
- **Notebook:** versión vigente = `01_notebook_v3_CAPEX_corregido.ipynb` (reorganizado, outputs limpios, ~0.22 MB)
- **Datos:** `Escenarios.xlsx` (confidencial, solo local)
- **Notas metodológicas:** `Notas_metodologicas_articulo.md` — va por la Sección 36, pero **las Secciones 28, 32, 33, 34 y 36 están OBSOLETAS** (ver abajo)

## Flujo de trabajo (respetar)

1. Indicar en qué sección/celda del notebook va cada código.
2. Documentar cada hallazgo en las notas metodológicas.
3. Git tras cada avance: `cd "/c/Users/Legion 5/tesis-articulo"` → `git add .` → `git commit` → `git push`.
4. Validar todo dato sospechoso del Excel antes de usarlo.
5. **Prueba de sentido físico** antes de aceptar cualquier resultado (así se detectaron ~10 bugs reales).
6. Pegar bloques completos en celdas nuevas; **nunca** pegar código de diagnóstico dentro de una celda que se está arreglando (ya causó varios errores de indentación).

---

## ⚠️ TAREA INMEDIATA: DOCUMENTAR 5 CORRECCIONES MAYORES

Se hicieron cinco correcciones grandes que **invalidan conclusiones ya escritas** en las notas. Ninguna está documentada aún.

### Corrección 1 — CAPEX: regla de los seis décimos (antes: escalamiento lineal)
La Tabla 17 da cada costo **a una capacidad de referencia** (turbinas @1,000 kW; caldera @15 t vapor; lagunas @27 t/h; generador biogás @1,500 kW; etc.) y la **Tabla 18 da el exponente 0.6** (Sinnot & Taylor, Peters et al.). Se estaba multiplicando **linealmente**, lo que sobreestimaba gravemente los equipos alejados de su referencia (la turbina de Esc.1 opera a 7.5× su referencia → costo sobreestimado >2×). Solo el pretratamiento térmico usaba la regla.

### Corrección 2 — Doble conteo de la caldera
Los costos de turbina de Tabla 17 ($3,669/kW extracción-condensación; $2,815/kW contrapresión) **YA INCLUYEN la caldera** (confirmado por el autor). Se sumaba además la partida "Caldera" por separado. **Eliminada.**

**Efecto combinado 1+2:** CAPEX Esc.1 **−54%** ($50.3M → $23.0M en Planta A); CAPEX Esc.2 **−30%** ($12.6M → $8.79M). Aparecen **economías de escala**: el costo de turbina cae de $5,277/kW (1 MW) a $2,101/kW (10 MW); el costo anualizado pasa de $619.7/kW/año (constante) a ~$285/kW/año en tamaños grandes.

### Corrección 3 — POME vía Rahayu en AMBOS escenarios
El POME se calculaba con **Voogt/sólidos volátiles** en Esc.2 y **Rahayu/DQO** en Esc.1 — inconsistente y contrario a la intención del autor. Ahora: **POME siempre vía Rahayu et al. (2015), 0.35 Nm³ CH4/kg DQO**; la fracción de sólidos volátiles (Voogt, Tabla 15) se aplica **solo al EFB pretratado**, donde sí hay evidencia sólida (f_VS = 91.4%, reverse-engineered contra Thomsen et al. 2014).
- **Elimina** la limitación previa de `f_VS` no verificado para POME.
- **Thomsen et al. (2014) NO es la ecuación operativa** de ningún escenario — solo se usó para derivar f_VS. **No debe presentarse como tal en Materials & Methods.**
- Efecto: CH4 del Esc.2 sube en 5 de 6 plantas (Planta D +26%, por su DQO alta de 122,973 mg/L).

### Corrección 4 — O&M dentro de la función objetivo de Fase 2
El objetivo `f1_economico` solo restaba el CAPEX anualizado. Ahora resta también el **O&M anual (2.5% del CAPEX variable)**. El O&M del CAPEX fijo se resta fuera del objetivo (es constante, no altera las decisiones del solver).

### Corrección 5 — Costo de oportunidad de la biomasa quemada
El optimizador trataba la biomasa como **recurso gratuito e ilimitado**. Ahora resta el costo de oportunidad de PKS ($16/t) y MF ($8/t), **escalado por el factor de utilización de la turbina** (quemar menos biomasa = perder menos ingreso potencial). Total si se quema el 100%: **$1,435,859 USD/año** (6 plantas).

---

## 🔴 RESULTADO CENTRAL — LA CONCLUSIÓN DEL ARTÍCULO SE INVIRTIÓ

**ANTES (con CAPEX inflado):** el óptimo económico usaba solo el 16% del potencial de biomasa; el punto de equilibrio estaba en 57%; desplegar el 100% costaba **−$8.3M/año** (pérdida) y se necesitaba un subsidio de $11.15M/año.

**AHORA (CAPEX correcto + OPEX + costo de biomasa):**

| | **Escenario 1** | **Escenario 2** |
|---|---|---|
| Óptimo económico | 189.5 GWh (**76%** del potencial) → **+$4.87M/año** | 147.5 GWh (**91%** del potencial) → **+$7.71M/año** |
| Despliegue 100% | 249.1 GWh → **+$2.67M/año** | 161.6 GWh → **+$6.80M/año** |
| Costo de desplegar todo | $2.19M (**45%** del óptimo) | $0.91M (**12%** del óptimo) |
| ¿Rentable en todo el frente? | **SÍ** (mínimo $2.67M) | **SÍ** (mínimo $6.80M) |

**Tres mensajes centrales:**
1. **No existe punto de equilibrio: ambos escenarios son rentables incluso desplegando el 100% de la biomasa.** No se requieren subsidios. Esto además es **consistente con la realidad** (explica por qué plantas como Entrepalmas ya invirtieron; el modelo viejo no podía explicarlo).
2. **El Escenario 2 es más rentable Y tiene menos conflicto entre pilares:** genera 35% menos energía pero 58% más beneficio, y maximizar el impacto socioambiental cuesta solo 12% del beneficio (vs. 45% en Esc.1). Es donde lo privado y lo público casi coinciden.
3. **El Escenario 1 aporta más energía al departamento** (249 vs. 162 GWh) pero con un trade-off real (45% del beneficio).

**Titular defendible:** *"La valorización energética de biomasa de palma es financieramente viable por sí sola bajo el marco regulatorio colombiano vigente (CREG 174/2021), sin subsidios. La tensión entre rentabilidad privada y beneficio socioambiental existe pero es modesta: 12-45% del beneficio según la configuración tecnológica."*

**Hallazgo metodológico adicional:** el frente de Pareto tiene **huecos** (varios ε devuelven la misma solución) por la **discretización del catálogo comercial** — no hay configuraciones factibles intermedias. Es un resultado legítimo y publicable (justifica el uso de ε-constraint sobre suma ponderada, que sí se saltaría esos huecos). Se colapsan los duplicados con `drop_duplicates(subset='generacion_GWh')`.

---

## SECCIONES DE LAS NOTAS QUE HAY QUE REESCRIBIR

- **Sección 28 (LCOE):** todas las tablas de LCOE están obsoletas. Valores correctos actuales (bruto/neto, USD/kWh):
  - Esc.1: A=0.0929/0.0272, B=0.0763/0.0027, C=0.0773/−0.0028, D=0.0831/0.0166, E=0.1451/0.0581, F=0.2623/0.1908
  - Esc.2: A=0.0544/−0.0117, B=0.0417/−0.0323, C=0.0431/−0.0407, D=0.0477/−0.0188, E=0.0796/−0.0143, F=0.1549/0.0827
  - Ahora caen en el rango típico de bioenergía en literatura (0.04–0.26 USD/kWh). Antes (0.20–0.49) estaban fuera de rango — señal de alarma que no se leyó a tiempo.
- **Sección 32 (Fase 2, Etapa 1):** el hallazgo de "$619.7/kW/año constante" y "óptimo = autoabastecimiento" **ya no aplica**.
- **Sección 33 (precios):** los precios siguen válidos, pero las conclusiones de rentabilidad por planta (A y F no rentables) hay que reverificar.
- **Sección 34 (CREG 174):** la conclusión de que "el óptimo usa solo 4-28% de la biomasa" **ya no aplica**.
- **Sección 36 (Pareto):** **completamente obsoleta** — el punto de equilibrio al 57% y la brecha de $11.15M no existen.

---

## YA RESUELTO (no volver a preguntar)

### Modelo técnico (Fase 1) — completo y validado
- 3 escenarios × 6 plantas en `ConcreteModel` indexado (todos `optimal`).
- Horas de operación (hoja `Eficiencia`, fila 6): A=5,105, B=5,155, C=5,920, D=5,496, E=3,147, F=1,931.
- Capacidades: A=30, B=40, C=30, D=24, E=30, F=20 t/h.
- **Escenario 1** (extracción-condensación 48 bar/470°C + biogás POME).
- **Escenario 2** (contrapresión 21 bar/235°C → 3 bar + biogás POME+EFB pretratado). Excedente total tras corrección 3: A=4,510.5, B=6,706.8, C=4,791.0, D=4,190.4, E=4,836.8, F=3,379.6 kW.

### ~10 bugs reales corregidos (todos por sentido físico)
1. LHV biomasa: error de unidades ×1000. 2. Entalpía agua alimentación a presión errónea. 3. Estado de extracción de turbina como dato de diseño, no derivado. 4. Clarificación dinámica: 15 → **1.5 kWh/tRFF**. 5. Columna "Electrica" en kW específicos (× capacidad). 6. **MOin = sólidos volátiles**, no materia seca. 7. Tabla 16: 235°C y escape a 3 bar (Booneimsri et al. 2018). 8. Precio de red: Tabla 18 subestimaba 32.4%. 9. **CAPEX lineal → regla 0.6.** 10. **Doble conteo de caldera.**

### Parámetros clave
- **Precio de electricidad por planta** (costo ponderado real de su matriz): A=$0.1141, B=$0.2537, C=$0.2572, D=$0.1530, E=$0.2551, F=$0.2591/kWh. TRM=$3,339.65.
- **CREG 174/2021** (deroga CREG 030): 3 tramos — autoconsumo y permuta (hasta = consumo) a precio minorista; excedente sobre eso a **bolsa = 0.0703 USD/kWh** (promedio 11 meses XM).
- **CEPCI 2026 ≈ 873.8** (factor 2019→2026 = 1.4383). Descuento 10%, vida útil 20 años (PVAF = 8.5136). O&M = 2.5% CAPEX/año.
- **Catálogos:** turbina Esc.1 [300…10000] kW; turbina Esc.2 [750…1750] kW; generador biogás = N módulos de 1,000 kW (máx. 8). El generador de biogás tiene **CAPEX lineal en N** (módulos idénticos; la regla 0.6 aplica al dimensionar *una* unidad respecto a su referencia de 1,500 kW, no a replicarlas).

### Marco multicriterio
- **Emisiones:** intensidad del sistema energético (sin crédito de absorción de palma): Esc.1 −125.6 a −132.4; Esc.2 −131.0 a −138.6 gCO2eq/kWh (red nacional: +163.4). Crédito de absorción de palma (−135.04 kg CO2/tRFF) domina 82-88% del balance total → se reporta **separado**, por tRFF.
- **Social:** viviendas/personas rurales beneficiadas. **Nota:** el % de cobertura rural departamental supera el 100% ampliamente (561-758% en el frente actual) — hay techo aplicado, pero conviene revisar si el denominador es el adecuado.
- **Método multiobjetivo:** ε-constraint en dos pasos (payoff table lexicográfica → ε-constraint), respaldado en Nandimandalam et al. (2022, *Energy Convers Manag* 266:115833) y Nguyen et al. (2026, *Renewable Energy Focus* 58:100856).
- **Hallazgo estructural:** los pilares ambiental y social son **colineales** (ambos lineales en la generación) → el problema colapsa a **2D**: económico vs. despliegue de biomasa.

### Verificaciones regulatorias (Sección 35, siguen válidas)
- **Precio firme (cargo por confiabilidad):** válido para biomasa pero diseñado para plantas >20 MW (las nuestras son 5-9.5 MW) → **queda como discusión de política**, no se modela.
- **Valor del carbono (Decreto 926/2017):** válido pero ~50-190× menor que los precios de electricidad → **cálculo de referencia aparte**, no entra al solver.

## ESTADO AL CIERRE DE ESTA SESIÓN (julio 2026)

### Verificado en esta sesión
- `capex_fijo_anualizado_total_esc1` = $3,335,578 (CAPEX fijo $28,397,653 / PVAF 8.5136).
  **NO incluye O&M** → el O&M del CAPEX fijo (2.5%) debe restarse aparte, fuera del objetivo.
- Bug de nombre resuelto: `perdida_estacional` → `perdida_estacional_v2` (sensibilidad estacional).

### 🔴 ROTO ESTRUCTURALMENTE — hay que rehacer (NO es bug de nombre)
Tres bloques del notebook reconstruyen el CAPEX como `capacidad × costo_específico_constante`.
Con la regla de los seis décimos (Corrección 1) **el costo específico ya no es constante**
($5,277/kW a 1 MW → $2,101/kW a 10 MW), y los parámetros `costo_especifico_kW` y
`costo_biogas_kW` **ya no existen en el modelo**. Reconstruir el CAPEX así reintroduce el
error lineal ya corregido.

**Solución:** leer el CAPEX del diccionario `CAPEX_TURBINA_ESC1[k]` / `CAPEX_TURBINA_ESC2[k]`
(indexado por tamaño del catálogo, ya con regla 0.6 y sin doble conteo de caldera) y
`CAPEX_UNIDAD_BIOGAS` × N módulos (lineal en N).

- **Sección 19** (indicadores sobre el frente, Esc.1): CORREGIDA, pendiente de correr.
- **Sección 19 bis** (Esc.2): pendiente de rehacer igual.
- **Sección 21** (sensibilidad a incentivos): pendiente. Escalaba constantes globales de
  costo que ya no existen.
- **Sección 22** (tarifa preferencial / feed-in tariff): pendiente. Depende de la anterior.

### 🔴 OBSOLETO EN EL ARTÍCULO (calculado sobre el CAPEX inflado)
- **Results and Discussion v1** — completo. Los "tres óptimos" (29%/43.4%/50.7%), la U del
  LCOE, la dominancia de Pareto del Esc.2, la brecha de $13.1M, la FiT de 0.130 USD/kWh y
  el 1.93% del impuesto al carbono: **todos inválidos**.
- **Abstract v4, título, highlights y cover letter** — construidos sobre el mensaje viejo
  ("technology choice, not policy support"). El mensaje nuevo es otro (ver abajo).
- **Notas metodológicas §43 a §49** — obsoletas.

### ✅ SE SALVA
- **Materials and Methods v3** — casi entero. Corregir: (a) la ecuación de Thomsen NO es la
  operativa (solo se usó para derivar f_VS del EFB); (b) POME siempre vía Rahayu et al.
  (2015), 0.35 Nm³ CH4/kg DQO, en AMBOS escenarios (Corrección 3); (c) el CAPEX ya no es
  lineal (regla 0.6) y las turbinas ya incluyen la caldera.
- **Introduction v1** — salvo el "gap", que hay que reformular al mensaje nuevo.

### MENSAJE NUEVO DEL ARTÍCULO (reemplaza al anterior)
*"La valorización energética de biomasa de palma es financieramente viable por sí sola bajo
CREG 174/2021, sin subsidios. Ambos escenarios son rentables incluso desplegando el 100% de
la biomasa. La tensión entre rentabilidad privada y beneficio socioambiental existe pero es
modesta: cuesta 12% del beneficio en el Esc.2 y 45% en el Esc.1."*

Hallazgo metodológico adicional publicable: **huecos en el frente de Pareto** por la
discretización del catálogo comercial → justifica ε-constraint sobre suma ponderada.

### PENDIENTES QUE AÚN PUEDEN MOVER NÚMEROS (resolver ANTES de reescribir el texto)
1. **`f2_generacion` mide potencia BRUTA en bornes**, pero las emisiones evitadas y las
   viviendas beneficiadas se calculan sobre energía **exportada**. Es el eje del frente de
   Pareto y el proxy de los pilares ambiental y social → inconsistencia interna que un
   revisor objetará. Decidir: renombrar a "generación bruta" o cambiar el eje a energía
   exportada/neta (**esto movería el frente de Pareto**).
2. **Denominador de la cobertura rural** (da 561–758%, implausible).

### ORDEN DE TRABAJO RECOMENDADO
1. Resolver los dos pendientes de arriba (pueden mover el frente).
2. Rehacer Secciones 19 bis, 21 y 22 del notebook leyendo el CAPEX del diccionario.
3. Recalcular indicadores sobre el frente nuevo.
4. Solo entonces reescribir: título → abstract → Results → ajustar Introduction y Methods.
## RESULTADOS DEFINITIVOS (CAPEX corregido) — Secciones 19/19bis/19c

LCOE ahora en rango de literatura (0.047–0.078 USD/kWh) → validación de sentido físico OK.

| | Escenario 1 | Escenario 2 |
|---|---|---|
| Óptimo privado | 189.5 GWh (76.1%) — $4,156,714 — LCOE 0.0715 — 27,785 tCO2 | 147.5 GWh (91.2%) — $7,241,802 — LCOE 0.0466 — 21,354 tCO2 |
| LCOE mínimo | 215.3 GWh (86.4%) — LCOE 0.0704 | 147.5 GWh (91.2%) — coincide con el óptimo privado |
| Despliegue 100% | 249.1 GWh — $1,964,312 — LCOE 0.0781 — 37,528 tCO2 | 161.6 GWh — $6,334,963 — LCOE 0.0507 — 23,665 tCO2 |
| Costo de desplegar el 100% | $2,192,403/año (53% del óptimo) | $906,838/año (13% del óptimo) |
| **Costo por tCO2 adicional** | **$225/tCO2** | **$392/tCO2** |

### HALLAZGOS
1. **Ningún escenario requiere subsidio:** rentables en todo el frente (mín. $1.96M y $6.33M).
2. **El Esc.2 domina en lo privado** (+74% beneficio, LCOE 35% menor) pero genera 35% menos energía.
3. **GIRO IMPORTANTE — la dominancia NO es total:** el Esc.2 compra CO2 evitado MÁS CARO
   ($392 vs. $225/tCO2), porque ya opera al 91% en su óptimo privado y le queda poco margen.
   El Esc.1 arranca en 76% y su expansión es más barata. En términos absolutos el Esc.1 evita
   mucho más (37,528 vs. 23,665 tCO2). → **No escribir "dominancia de Pareto" sin matizar.**
4. Ambos costos marginales ($225 y $392/tCO2) están MUY por encima del impuesto al carbono
   colombiano → el argumento de su ineficacia sobrevive, por otra vía.
5. **Cautela:** en el Esc.1, el óptimo privado y el LCOE mínimo distan solo 0.5% en beneficio
   ($22k/año) — posible ruido de la discretización del catálogo. No construir argumento fuerte.

## RESULTADOS DEFINITIVOS — CAPEX corregido (Secciones 19, 19bis, 19c, 20)

LCOE en rango de literatura (0.047–0.078 USD/kWh) → sentido físico OK.

| | Escenario 1 | Escenario 2 |
|---|---|---|
| Óptimo privado | 189.5 GWh (76.1%) — $4,156,714 — LCOE 0.0715 — 27,785 tCO2 | 147.5 GWh (91.2%) — $7,241,802 — LCOE 0.0466 — 21,354 tCO2 |
| LCOE mínimo | 215.3 GWh (86.4%) — LCOE 0.0704 | coincide con el óptimo privado |
| Despliegue 100% | 249.1 GWh — $1,964,312 — LCOE 0.0781 — 37,528 tCO2 | 161.6 GWh — $6,334,963 — LCOE 0.0507 — 23,665 tCO2 |
| Costo de desplegar el 100% | $2,192,403/año (53% del óptimo) | $906,838/año (13% del óptimo) |
| **Costo implícito de mitigación** | **$225/tCO2** | **$392/tCO2** |

### MENSAJE DEFINITIVO DEL ARTÍCULO
"No hay nada que subsidiar: ambas rutas son rentables incluso al 100% de despliegue.
La decisión pública no es cuánto compensar, sino QUÉ RUTA FAVORECER — y NINGUNA DOMINA:
- Objetivo rentabilidad → Esc.2 (+74% beneficio, LCOE 35% menor, 13% de costo para llegar al 100%)
- Objetivo climático → Esc.1 (+59% tCO2 evitadas en absoluto; mitigación marginal a $225 vs. $392/tCO2)
El impuesto al carbono ($7.49/tCO2) es 30-52x menor que el costo implícito real → incapaz de
movilizar el tramo marginal en ninguna ruta."

⚠️ NO usar el lenguaje de "brecha a subsidiar" ni "dominancia de Pareto" — ambos obsoletos.

### Sección 22 — REFORMULAR (no descartar)
El marco de "tarifa preferencial / FiT" queda obsoleto: no hay brecha de rentabilidad que
cerrar (ambos escenarios rentables al 100%). PERO la pregunta subyacente sigue viva y
reformulada: **¿qué precio del excedente induce a la planta a ELEGIR el 100%?** El óptimo
privado del Esc.1 está en 76% — hay un 24% del potencial que no se despliega aunque sería
rentable. Eso es INCENTIVO, no subsidio.
- Renombrar a "respuesta del despliegue a la señal de precio".
- Eliminar la parte (a) "FiT de equilibrio". Conservar la (b) y la figura.
- Arreglar `barrido_fit()`: NO debe tocar las constantes de costo (ya no existen); solo
  `PRECIO_BOLSA_PROMEDIO`.
- Conectar con el costo implícito de mitigación ($225 y $392/tCO2, Sección 20).

## PLAN DE ANÁLISIS ACORDADO (próxima sesión)

Los resultados corregidos son sólidos pero "cómodos" (todo rentable, nadie necesita subsidio).
Faltan dos análisis para recuperar tensión y blindar el artículo.

### ANÁLISIS 1 — Desagregado por planta (PRIORIDAD)
**Pregunta:** ¿"rentable sin subsidio" vale para las 6 plantas, o solo para las grandes?
**Motivo:** enorme heterogeneidad — F opera 1,931 h/año y E 3,147, contra ~5,500 de A–D;
LCOE por planta va de 0.076 a 0.262 USD/kWh (Esc.1). E y F ya salían rezagadas en análisis
previos (social, LCOE, económico).
**Hipótesis:** si E y F NO son rentables individualmente → hallazgo de EQUIDAD: la viabilidad
es de las plantas grandes, no del sector. Justifica intervención pública FOCALIZADA (no
general) y reactiva la discusión de política.
**Datos:** ya existen en `df_pareto_plantas` / `df_pareto_plantas_e2`. Es análisis, no
modelado nuevo.

### ANÁLISIS 4 — Robustez del resultado central al precio de la electricidad
**Pregunta:** ¿a qué precio deja de ser rentable el despliegue?
**Motivo:** el resultado "rentable sin subsidio" descansa sobre precios de compra que varían
2.3x entre plantas (0.114–0.259 USD/kWh) y sobre un precio de bolsa promediado a 11 meses en
un mercado VOLÁTIL. Es la objeción más obvia de un revisor.
**Alcance:** barrer precio de compra y precio de bolsa; identificar el umbral de rentabilidad.
Reutilizar la maquinaria de `barrido_fit()` PERO arreglada (no debe tocar constantes de costo,
que ya no existen; solo `PRECIO_BOLSA_PROMEDIO`).

### ANÁLISIS 3 — Reportar (ya existe, no explotado)
Huecos en el frente de Pareto por discretización del catálogo comercial (varios ε devuelven
la misma solución). Hallazgo metodológico publicable: un modelo de capacidad CONTINUA daría
respuesta cualitativamente distinta. Justifica ε-constraint sobre suma ponderada.

### ANÁLISIS 5 — TRABAJO FUTURO (declarado, no modelado)
Hub centralizado de biomasa bajo CREG 101 099/2026 (autogeneración remota). La regla 0.6 da
economías de escala fuertes ($5,277/kW a 1 MW → $2,101/kW a 10 MW) → podría volver viables a
E y F. Mencionar en Conclusions como línea futura. Posible segundo artículo.

### PENDIENTES ANTES DE REESCRIBIR EL TEXTO
1. **Unificar `f1_beneficio_neto_total_USD`:** el de `df_pareto` NO resta el O&M del CAPEX
   fijo ($709,941/año); el de la Sección 19b SÍ. Usar el de 19b. (Por eso la Sección 20 daba
   $4,866,656 y la 19b $4,156,714.)
2. **Verificar el impuesto al carbono vigente 2026** (usado: COP 25,000/tCO2 = $7.49, TRM 3,339.65).
3. **`f2_generacion` = potencia BRUTA** vs. energía exportada (emisiones y viviendas se
   calculan sobre exportada). Puede mover el frente.
4. **Denominador de cobertura rural** (561–758%).
5. Secciones 21 (incentivos) y 22 (FiT): rotas. La 22 pierde sentido — ya no hay brecha.

### A REESCRIBIR
Results and Discussion (completo), Abstract, título, highlights, cover letter, notas §43–§49.
Se salvan: Materials and Methods v3 (corregir Thomsen, POME vía Rahayu, CAPEX regla 0.6) e
Introduction v1 (reformular el gap).
