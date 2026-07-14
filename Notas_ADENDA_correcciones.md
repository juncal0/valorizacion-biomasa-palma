# ADENDA — Correcciones mayores (Secciones 37-42)

> **Cómo integrar este documento:** las Secciones 37-42 se **añaden al final** de `Notas_metodologicas_articulo.md`. Además, las Secciones **28, 32, 33, 34 y 36** del documento original deben marcarse como **SUPERADAS** (ver Sección 42 de esta adenda para el mapa exacto de qué reemplaza a qué).

---

## 37. Corrección crítica del CAPEX — regla de los seis décimos y doble conteo de la caldera

### 37.1 Origen del hallazgo

Al revisar el desglose del CAPEX del Escenario 2, el autor observó que el costo de la turbina de contrapresión ($5,428,511 en Planta A) representaba el **43% del CAPEX total** mientras aportaba apenas el **7% del excedente eléctrico** — una desproporción que no pasaba la prueba de sentido físico. La investigación reveló **dos errores acumulados, ambos en la misma dirección (sobreestimar el CAPEX)**.

### 37.2 Error 1 — Escalamiento lineal en vez de la regla de los seis décimos

La **Tabla 17** de la tesis reporta cada costo a una **capacidad de referencia específica**:

| Equipo | Costo unitario | Capacidad de referencia |
|---|---|---|
| Turbina extracción-condensación | $3,669/kW | 1,000 kW |
| Turbina contrapresión | $2,815/kW | 1,000 kW |
| Caldera biomasa media presión | $76,070/t vapor | 15 t vapor |
| Precipitador electroestático | $25,000/t vapor | 15 t vapor |
| Pretratamiento mecánico EFB | $29,655/tEFB | 3 tEFB |
| Lagunas carpadas | $18,518/tRFF | 27 t/h |
| Tratamiento de biogás | $424/m³ | 660 m³/h |
| Generador de biogás | $186/kW | 1,500 kW |
| Esterilización continua | $38,400/tRFF | 20 t/h |
| Clarificación dinámica | $23,368/tRFF | 15 t/h |
| Tratamiento térmico EFB | $178,571 (total) | 5.6 tEFB/h |

Y la **Tabla 18** aporta explícitamente el exponente de escalamiento: **0.6** ("Potencia de escalamiento", Sinnot & Taylor; Peters et al.) — la regla de los seis décimos.

**El error:** el modelo multiplicaba **linealmente** ($/unidad × capacidad real) en todos los equipos **excepto** el tratamiento térmico de EFB, donde sí se aplicaba la regla 0.6. Esta inconsistencia sobreestimaba gravemente los equipos alejados de su capacidad de referencia. El caso más severo: la turbina del Escenario 1 opera a **7.5× su capacidad de referencia** (7,517 kW vs. 1,000 kW), por lo que el escalamiento lineal la sobreestimaba en **más del doble**.

**Corrección adoptada:** aplicar `Costo = Costo_ref_total × (Capacidad_real / Capacidad_ref)^0.6 × factor_CEPCI` a **todos** los equipos con capacidad de referencia conocida.

**Excepciones documentadas:**
- *Sistema de gases de combustión* ($11,515/t vapor, Esc.2 — ciclón+filtro): no figura en Tabla 17, no tiene capacidad de referencia documentada. Se asume **15 t vapor** por analogía con el precipitador electroestático (supuesto de trabajo).
- *Redes e infraestructura* ($7,153/tRFF): se mantiene **lineal**, por ser infraestructura cuyo costo escala aproximadamente de forma proporcional (decisión del autor).
- *Generador de biogás*: se modela como **N unidades modulares de 1,000 kW**. La regla 0.6 aplica al **dimensionar una unidad** respecto a su referencia (1,500 kW), **no a replicar unidades idénticas**: N módulos iguales cuestan N × costo_unidad. Por tanto el CAPEX es **lineal en N**.

### 37.3 Error 2 — Doble conteo de la caldera

Los costos de turbina de la Tabla 17 **incluyen la caldera** (confirmado por el autor tras revisar la fuente: tanto los $3,669/kW de la turbina de extracción-condensación —citando IRENA, cuyos rangos son de planta completa— como los $2,815/kW de la de contrapresión son costos de *turbina + caldera*). El modelo sumaba **además** una partida separada de "Caldera" ($76,070/t vapor).

**Corrección:** la partida "Caldera" se **elimina** del CAPEX incremental de ambos escenarios.

### 37.4 Efecto combinado

| Planta | CAPEX Esc.1 (antes → ahora) | CAPEX Esc.2 (antes → ahora) |
|---|---|---|
| A | $50.3M → **$23.0M** | $12.6M → **$8.79M** |
| B | — → $26.1M | — → $10.1M |
| C | — → $22.0M | — → $8.57M |
| D | — → $18.9M | — → $7.71M |
| E | — → $22.5M | — → $8.50M |
| F | — → $18.0M | — → $7.10M |

**Reducción: −54% (Esc.1) y −30% (Esc.2).**

**Consecuencia estructural — aparecen economías de escala:** el costo específico de la turbina deja de ser constante y **cae con el tamaño**:

| Tamaño (kW) | $/kW | $/kW/año (anualizado) |
|---|---|---|
| 1,000 | 5,277 | 619.7 |
| 4,000 | 3,097 | 363.8 |
| 7,000 | 2,423 | 284.6 |
| 10,000 | 2,101 | 246.8 |

Esto es lo que invierte la conclusión del artículo (Sección 41): el parámetro de $619.7/kW/año que sostenía todo el análisis previo de Fase 2 **solo era válido para turbinas de 1 MW**.

### 37.5 Bug latente detectado de paso

La función `capex_fijo_esc1()` excluía la turbina del CAPEX fijo buscando la clave exacta `'Turbina extracción-condensación'`. Al renombrar las claves, la exclusión habría fallado **en silencio** y la turbina se habría contado dos veces. Se estandarizaron las claves a `'Turbina'` y `'Generador de biogás'` en ambos escenarios.

---

## 38. Homogeneización del cálculo de metano del POME (vía Rahayu en ambos escenarios)

### 38.1 El problema

El POME se calculaba con **dos métodos distintos** según el escenario:
- **Escenario 1:** Rahayu et al. (2015), vía **DQO** (0.35 Nm³ CH4/kg DQO).
- **Escenario 2:** Voogt et al. (2021), Tabla 15, vía **sólidos volátiles** (538 m³/tSV, 65% CH4).

Esto era inconsistente (misma corriente física, dos metodologías), y además **no correspondía a la intención de diseño del autor**, que siempre fue estimar el POME con Rahayu en ambos escenarios y reservar la ruta de sólidos volátiles para el EFB pretratado.

### 38.2 Corrección adoptada

- **POME: siempre Rahayu et al. (2015), vía DQO**, en ambos escenarios.
- **EFB pretratado: Voogt et al. (2021), Tabla 15, vía sólidos volátiles** (523 m³/tSV, 54% CH4), con `FRACCION_VS_MATERIA_SECA = 0.90`.

**Beneficio metodológico central:** esto **elimina por completo** la limitación previamente documentada de que la fracción de sólidos volátiles del POME (0.90) era un supuesto no verificado. Al calcularse el POME por DQO, la fracción de SV **solo se aplica al EFB**, que es justamente donde hay evidencia sólida (91.4%, reverse-engineered contra la correlación de Thomsen et al. 2014, ya validada al 100%).

### 38.3 Aclaración crítica para Materials & Methods

**La correlación de Thomsen et al. (2014) — `bmp_efb()`, 273.51 L CH4/kg SV — NO es la ecuación operativa de ningún escenario.** No alimenta ningún resultado del modelo. Cumplió dos funciones auxiliares:
1. Era la ecuación usada por la hoja `Scenarios2` del Excel original, que se **descartó** por desactualizada (aplicaba el BMP al EFB *crudo*, no al pretratado).
2. Al hacerle reverse-engineering a ese cálculo, se derivó la fracción de sólidos volátiles del EFB (91.4%).

**No debe presentarse en el cuerpo del artículo como ecuación de cálculo.** A lo sumo, mencionarse en la validación metodológica.

### 38.4 Efecto

El CH4 del Escenario 2 **sube en 5 de 6 plantas** (baja solo en Planta A). La diferencia por planta se explica porque Rahayu escala con la **DQO** (que varía mucho: 74,496 a 122,973 mg/L) mientras que Voogt escalaba con el volumen de efluente:

| Planta | CH4 total antes (Nm³/h) | CH4 total ahora | Cambio |
|---|---|---|---|
| A | 1,158.4 | 1,117.9 | −3.5% |
| B | 1,480.5 | 1,622.0 | +9.6% |
| C | 1,121.0 | 1,188.1 | +6.0% |
| D | 805.0 | 1,016.9 | **+26.3%** (DQO más alta) |
| E | 1,159.5 | 1,262.8 | +8.9% |
| F | 719.8 | 778.7 | +8.2% |

**Excedente eléctrico total del Escenario 2 (actualizado):** A=4,510.5, B=6,706.8, C=4,791.0, D=4,190.4, E=4,836.8, F=3,379.6 kW.

El Escenario 1 **no cambia** (ya usaba Rahayu), por lo que su análisis de Fase 1 permanece intacto.

---

## 39. Integración del OPEX y del costo de oportunidad de la biomasa en la función objetivo

### 39.1 Problema detectado

La función objetivo `f1_economico` de la Fase 2 solo restaba el **CAPEX anualizado** de turbina y generador. Faltaban dos costos que **el optimizador no percibía**:

1. **O&M (2.5% del CAPEX/año, Tabla 18)** — nunca entraba al objetivo.
2. **Costo de oportunidad de la biomasa quemada** — el modelo trataba fibra y cuesco como un **recurso gratuito e ilimitado**, cuando tienen valor de mercado (PKS $16/t; MF $8/t, Tabla 18). Esto inflaba artificialmente el beneficio de desplegar más biomasa.

### 39.2 Corrección adoptada

**O&M:** se resta el 2.5% anual del **CAPEX variable** (turbina + generador de biogás) dentro del objetivo. El O&M del **CAPEX fijo** se resta **fuera** del objetivo (junto al CAPEX fijo anualizado): al ser una constante que no depende de las decisiones del solver, no altera qué configuración elige — solo desplaza el frente. Mantenerlo fuera deja el MILP más limpio con resultado idéntico.

**Costo de oportunidad:** se resta **escalado por el factor de utilización de la turbina** (decisión del autor):

```
costo_oportunidad_efectivo[p] = factor_utilizacion[p] × costo_oportunidad_anual[p]
```

La lógica: si el modelo quema solo el 40% de la biomasa disponible, solo renuncia al 40% del ingreso potencial por venta de PKS/MF. Si se modelara como costo fijo, el solver no percibiría que **ahorra biomasa** al reducir la turbina, y el sesgo se mantendría.

**Nota para el Escenario 2:** la turbina quema **solo fibra+cuesco** (el EFB va íntegro a biogás), por lo que el costo de oportunidad escala con `factor_util_turbina` y **no** con `factor_util_biogas`.

### 39.3 Magnitud

Costo de oportunidad anual si se quema el 100% de la biomasa disponible:

| Planta | USD/año |
|---|---|
| A | 297,724 |
| B | 342,136 |
| C | 308,314 |
| D | 251,153 |
| E | 154,046 |
| F | 82,486 |
| **Total** | **1,435,859** |

Significativo pero no dominante. Al escalar con el factor de utilización, penaliza específicamente los puntos de alto despliegue del frente de Pareto — que es exactamente el sesgo que se buscaba corregir.

### 39.4 Ajustes menores de robustez

- **Tolerancia del solver:** la relajación lexicográfica pasó de `f1_max - 1e-4` (absoluta, frágil ante errores de redondeo) a una **tolerancia relativa** (`f1_max - abs(f1_max)*1e-6`) o a valores lógicos ($1 USD; 100 kWh).
- **Claridad de nombres:** `objetivo='excedente'` → `objetivo='generacion'`, ya que `f2_generacion` maximiza la **generación total**, no el excedente exportable (que sería generación menos autoconsumo).

---

## 40. Frente de Pareto — huecos por discretización del catálogo comercial

Al recalcular el frente con el CAPEX corregido, varios valores de ε devolvían **exactamente la misma solución** (ej. Escenario 1: ε = 195.4, 201.4, 207.3 y 213.3 GWh → todos dan 215.29 GWh).

**No es un bug.** Es un **hueco real del frente de Pareto**, causado por la **discretización del catálogo comercial de turbinas**: para generar más energía, el modelo debe subir un escalón entero de capacidad instalada (23.9 → 28.6 MW), y una vez pagado ese escalón le conviene aprovecharlo al máximo. **No existe ninguna configuración factible entre 189.45 y 215.29 GWh.**

Esto es un resultado legítimo y publicable — y valida la elección metodológica: la literatura (Nandimandalam et al., 2022) recomienda ε-constraint precisamente porque **no se salta los huecos ni las indentaciones del frente**, a diferencia de la suma ponderada.

**Implicación práctica citable:** *las capacidades comerciales disponibles condicionan qué puntos del frente de Pareto son alcanzables en la práctica.*

**Tratamiento:** los puntos duplicados se colapsan con `drop_duplicates(subset='generacion_GWh', keep='first')`, conservando el primer ε que alcanza cada solución.

**Hallazgo derivado (Escenario 1):** el punto inmediatamente posterior al óptimo económico ofrece **+14% de generación (189.5 → 215.3 GWh) a cambio de solo −0.5% de beneficio**. Es un argumento de política mucho más potente que un frente suave.

---

## 41. RESULTADO CENTRAL — la conclusión del artículo se invierte

### 41.1 Comparación con la conclusión anterior (ahora superada)

| | **Antes (CAPEX inflado)** | **Ahora (corregido)** |
|---|---|---|
| Óptimo económico (Esc.1) | 30.5 GWh (**16%** del potencial), +$2.8M | **189.5 GWh (76%), +$4.87M** |
| Despliegue 100% (Esc.1) | 184.9 GWh, **−$8.3M (pérdida)** | **249.1 GWh, +$2.67M (ganancia)** |
| Punto de equilibrio | 57% del potencial | **No existe: todo el frente es rentable** |
| Subsidio requerido | $11.15M/año | **Ninguno** |

### 41.2 Resultado final — ambos escenarios

| | **Escenario 1** | **Escenario 2** |
|---|---|---|
| Óptimo económico | 189.5 GWh (**76%** del potencial) → **+$4.87M/año** | 147.5 GWh (**91%** del potencial) → **+$7.71M/año** |
| Despliegue 100% | 249.1 GWh → **+$2.67M/año** | 161.6 GWh → **+$6.80M/año** |
| Costo de desplegar todo | $2.19M (**45%** del óptimo) | $0.91M (**12%** del óptimo) |
| ¿Rentable en todo el frente? | **SÍ** (mínimo $2.67M) | **SÍ** (mínimo $6.80M) |

### 41.3 Tres mensajes centrales para el artículo

1. **No existe punto de equilibrio: ambos escenarios son rentables incluso desplegando el 100% de la biomasa disponible.** No se requieren subsidios bajo el marco regulatorio vigente (CREG 174/2021).

2. **El Escenario 2 es más rentable Y tiene menos conflicto entre pilares.** Genera 35% menos energía que el Escenario 1, pero produce **58% más beneficio**, y maximizar el impacto socioambiental cuesta apenas el **12%** del beneficio (vs. **45%** en el Escenario 1). Es la configuración donde el óptimo privado y el óptimo público casi coinciden.

3. **El Escenario 1 ofrece el mayor aporte energético al departamento** (249 vs. 162 GWh/año) pero con un trade-off real: desplegar todo su potencial sacrifica el 45% del beneficio. Sigue siendo rentable, pero ahí sí hay una decisión de política que tomar.

**Titular defendible:**
> *"La valorización energética de biomasa residual de palma de aceite es financieramente viable por sí sola bajo el marco regulatorio colombiano vigente (CREG 174/2021), sin necesidad de subsidios. La tensión entre rentabilidad privada y beneficio socioambiental existe, pero es modesta: entre 12% y 45% del beneficio según la configuración tecnológica adoptada."*

### 41.4 Validación externa — coherencia con la realidad

El resultado corregido es **consistente con la evidencia de campo**: explica por qué plantas reales como **Entrepalmas S.A.S.** (Meta, 42 tRFF/h) efectivamente realizaron la inversión en cogeneración con biogás y reportan ahorros de ~$600 millones COP/año. **El modelo anterior no podía explicar ese hecho** — predecía que la inversión destruía valor. Esta discrepancia con la realidad era, en retrospectiva, una señal de alarma que no se leyó a tiempo.

**Segunda validación:** los LCOE corregidos (0.04–0.26 USD/kWh) caen ahora dentro del **rango típico de bioenergía reportado en literatura**. Los valores anteriores del Escenario 1 (0.20–0.49 USD/kWh) estaban fuera de ese rango — otra señal de alarma no detectada a tiempo.

---

## 42. Mapa de secciones superadas

| Sección original | Estado | Reemplazada por |
|---|---|---|
| **28** (LCOE) | Tablas de LCOE **obsoletas** (CAPEX inflado) | Sección 42.1 (abajo) |
| **32** (Fase 2, Etapa 1) | **Obsoleta**: el hallazgo de "$619.7/kW/año constante" y "óptimo = autoabastecimiento" ya no aplica | Secciones 37 y 41 |
| **33** (precios por planta) | Precios **siguen válidos**; las conclusiones de rentabilidad por planta (A y F no rentables) deben reverificarse | Sección 41 |
| **34** (CREG 174) | Marco regulatorio **sigue válido**; la conclusión de "el óptimo usa solo 4-28% de la biomasa" **ya no aplica** | Sección 41 |
| **36** (Frente de Pareto) | **Completamente obsoleta**: el punto de equilibrio al 57% y la brecha de $11.15M no existen | Secciones 40 y 41 |

### 42.1 LCOE actualizado (reemplaza las tablas de la Sección 28)

| Planta | Esc.1 bruto | Esc.1 neto | Esc.2 bruto | Esc.2 neto |
|---|---|---|---|---|
| A | 0.0929 | 0.0272 | 0.0544 | −0.0117 |
| B | 0.0763 | 0.0027 | 0.0417 | −0.0323 |
| C | 0.0773 | −0.0028 | 0.0431 | −0.0407 |
| D | 0.0831 | 0.0166 | 0.0477 | −0.0188 |
| E | 0.1451 | 0.0581 | 0.0796 | −0.0143 |
| F | 0.2623 | 0.1908 | 0.1549 | 0.0827 |

*(USD/kWh. Bruto = solo CAPEX + O&M. Neto = descontando ahorro de autoconsumo al precio ponderado de cada planta + venta de excedente + costo de oportunidad de PKS/MF.)*

**La recomendación de presentación bruto/neto (Sección 28.6) sigue plenamente vigente:** reportar el bruto como cifra principal (evita que un LCOE negativo sea malinterpretado por revisores) y el neto como análisis complementario del valor de los co-productos.

---

## 43. Pendientes derivados de estas correcciones

1. **`f2_generacion` mide potencia BRUTA en bornes**, no energía neta exportada. Como es el eje del frente de Pareto y el proxy de los pilares ambiental y social, o se renombra explícitamente ("generación bruta") o se cambia a energía neta. **Riesgo:** un revisor puede objetar que las emisiones evitadas y las viviendas beneficiadas se calculan sobre energía *exportada*, no sobre generación bruta.
2. **Indicador de cobertura rural:** da 561–758% en el frente actual. Aunque ya hay techo aplicado, conviene revisar si el denominador (demanda rural departamental) es el adecuado o debe reformularse.
3. **Costo de cogeneración con vapor:** se usa 258 COP/kWh (UPME) pero Entrepalmas (planta real) reporta **90 COP/kWh** (2.9× menor). Afecta el precio ponderado de Plantas A y D, y por tanto el LCOE neto y la Fase 2. **Decisión pendiente.**
