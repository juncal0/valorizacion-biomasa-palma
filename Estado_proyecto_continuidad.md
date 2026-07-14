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

---

## PENDIENTES

1. **Documentar las 5 correcciones** y reescribir Secciones 28, 32, 33, 34, 36 de las notas. ← PRIORIDAD
2. **`f2_generacion` mide potencia BRUTA en bornes**, no energía neta exportada. Como es el eje del frente de Pareto y el proxy de los pilares ambiental/social, o se renombra explícitamente ("generación bruta") o se cambia a energía neta. Un revisor podría objetar que emisiones evitadas y viviendas beneficiadas se calculan sobre energía *exportada*, no bruta.
3. Verificar el denominador del indicador de cobertura rural (da 561-758%).
4. **Exceso de aire** del secador EFB (Esc.1): se mantiene 30% (literatura genérica); no se pudo confirmar Ocampo Batlle et al. (2020) — paywall.
5. Redacción del artículo.
6. **Decisión pendiente de sesiones anteriores:** costo de cogeneración con vapor — usamos 258 COP/kWh (UPME) pero Entrepalmas (planta real) reporta **90 COP/kWh** (2.9× menor). Afecta el precio ponderado de Plantas A y D.
7. **Discusión sin modelar:** reactores/tanques cerrados vs. lagunas carpadas (los primeros facilitan la remoción del digestato, ~90% de la masa de entrada, pero mayor CAPEX; no hay costos disponibles).
