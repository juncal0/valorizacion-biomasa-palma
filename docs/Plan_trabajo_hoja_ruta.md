# Plan de trabajo y hoja de ruta — Valorización de biomasa de palma
**Última actualización:** 29 de julio de 2026

> Este documento consolida el estado del proyecto en dos frentes que corren en paralelo:
> (1) el artículo científico ya publicado/en revisión y su notebook de soporte, y
> (2) la exploración de convertir ese trabajo en un servicio/producto comercial.
> Úsalo como punto de partida al abrir una conversación nueva.

---

## 1. Estado del artículo y el notebook (frente académico)

### 1.1 Resultados centrales — VALIDADOS, no tocar sin re-verificar
- Escenario 1: óptimo económico 32.2% del potencial (+$258,705/año); despliegue total −$6,531,746/año
- Escenario 2: óptimo económico 92.3% del potencial (+$3,427,932/año); despliegue total +$2,315,672/año
- LCOE Escenario 1 en forma de U: 0.1488 USD/kWh en el óptimo, mínimo ~0.0940 cerca del 87%, sube a 0.1033 en despliegue total
- Costos de abatimiento: $294/tCO₂ (Esc.1), $599/tCO₂ (Esc.2) — ambos por encima del impuesto al carbono colombiano ($8.70/tCO₂)

### 1.2 Bugs corregidos (27-28 de julio) — ver `docs/Notas_metodologicas_articulo.md`
1. `consumo_medido_dict` desconectado de `df_ajuste` (ajuste termodinámico IAPWS97)
2. Restauración de CAPEX no garantizada tras simulaciones de incentivo — corregido con `try/finally`
3. `_beneficio_planta_bolsa`/`beneficio_planta_en_punto` con un solo factor de utilización (Esc.2 necesita 2 distintos)
4. Variable global `plantas` pisada por una celda de figura
5. Dos metodologías de LCOE compartiendo la variable `df_sost` (excedente vs. generación total)

**Estado actual del notebook:** `02_notebook_v4_modular.ipynb`, corre limpio de principio a fin, 4 checks + LCOE confirmados. En GitHub (`github.com/juncal0/valorizacion-biomasa-palma`, rama `main`).

### 1.3 Repositorio reorganizado
```
tesis-articulo/
├── 02_notebook_v4_modular.ipynb    (activo)
├── modelo_biomasa/                  (datos.py, termodinamica.py, parametros_comunes.py)
├── Escenarios.xlsx                  (datos 2022, ya validados en el articulo)
├── notebooks_archivados/
├── docs/                             (notas de continuidad y metodológicas)
├── Articulo/                         (manuscrito + comentarios coautores)
└── resultados/
    ├── figuras/
    └── tablas/
```

### 1.4 Modularización (`modelo_biomasa/`) — PARCIAL
- ✅ `datos.py`, `termodinamica.py`, `parametros_comunes.py` (generado 28 jul, **integración al notebook aún pendiente de ejecutar** — instrucciones ya escritas en el chat)
- ⏸️ `esc1.py`/`esc2.py` completos — pausados. **Decisión revisada hoy:** en vez de la extracción genérica original, se necesita algo más específico y acotado — ver Sección 4 (arquitectura de una sola planta).

### 1.5 Figuras regeneradas
`Figure1_Baseline.png`, `Figure2_Scenario1.png`, `Figure3_Scenario2.png` — código matplotlib incluido en el notebook, ya comiteadas.

### 1.6 Pendiente académico
- [ ] Afiliación institucional de Juan Camilo
- [ ] Escenario híbrido de asignación de EFB — diferido a respuesta a revisores
- [ ] Presentación/webinar Cenipalma (septiembre) — prompt de continuidad generado en conversación aparte

---

## 2. Frente de negocio: hacia un producto/servicio comercial

### 2.1 Contexto clave
- Vínculo con MetGas terminó en abril de 2026 (contractual). Proyecto personal, sin atadura institucional de empleador. Optimización (MILP/Pyomo) fue aporte propio.
- **Pendiente:** consulta rápida con abogado de PI antes de comercializar.
- Tiempo disponible: dedicación completa.

### 2.2 Decisión estratégica — AJUSTADA hoy
**Original (28 jul):** no generalizar a "biomasa en general"; esperar 3-5 clientes reales antes de expandir.

**Ajuste (29 jul), tras confirmar la realidad de Magdalena (ver Sección 3):** el eje de expansión más creíble y defendible **no es "biomasa en general"**, sino **expansión geográfica dentro de palma** — llevar el espíritu de la metodología a zonas de Colombia sin la crisis fitosanitaria actual de Magdalena (ej. Meta, Casanare). Mismo cultivo, mismo tipo de modelo, contexto agronómico distinto. Se mantiene la decisión de NO generalizar el motor a otras biomasas todavía.

**Tipo de MVP:** Concierge MVP (entrega manual antes de automatizar). Caso de referencia: Aurora Solar (arquitectura de "motores" validados uno por uno, bootstrapped 5 años).

### 2.3 Fuentes de financiación identificadas (verificar vigencia antes de aplicar)
| Fuente | Monto | Estado |
|---|---|---|
| Energy Ideas Generation Programme 2026 (Baker Hughes + Nana Bianca, Alcaldía de Bogotá) | Hasta €35,000, no diluible | **Mejor opción de corto plazo** — requiere MVP/prototipo, encaja con el plan |
| iNNpulsa Colombia | Hasta USD 30,000 | Verificar portal directo |
| Premio Innovación Sector Eléctrico (ASOCODIS) | No especificado | Abierta hasta 3 nov 2026 |
| Minciencias-MinEnergía-Ecopetrol (línea biomasa) | No especificado | Estado ambiguo, verificar |
| Convocatoria 49 SGR | — | **CERRADA** |

### 2.4 Plantilla del informe (concierge MVP) — 10 secciones, acordada
1. Resumen ejecutivo · 2. Alcance y vigencia de datos · 3. Situación actual de la planta · 4. Rutas tecnológicas (Figure2/3) · 5. Resultado económico · 6. Banda de incertidumbre (Monte Carlo) · 7. Impacto ambiental/social · 8. Sensibilidad a política pública · 9. Recomendaciones · 10. Anexos

**Audiencia:** ambos — resumen ejecutivo (gerencia/inversionistas) + anexo técnico (personal de planta).

**Conexión con la beca:** el informe piloto **es** el informe que ya se debe entregar por compromiso de la beca.

### 2.5 Diseño del Monte Carlo — decidido y AJUSTADO hoy
- **3 variables prioritarias:** precio de bolsa (histórico XM real), CAPEX de equipos (±30-40%, Clase 4-5 AACE), disponibilidad/humedad de biomasa
- **Alcance:** solo en el punto de óptimo económico (no en todo el frente de Pareto), por velocidad
- **AJUSTE NUEVO (29 jul):** al correr Monte Carlo por planta, distinguir entre:
  - **Variables de mercado** (precio de bolsa) — deben sortearse **una sola vez por iteración**, compartidas entre todas las plantas (correlacionadas en la realidad)
  - **Variables específicas de planta** (CAPEX cotizado, humedad, % híbrido) — se sortean independientes por planta
  - Sin esta distinción se subestima el riesgo correlacionado regional — un inversionista experimentado lo notaría

---

## 3. Hallazgos críticos de datos reales (29 de julio) — CAMBIA EL CONTEXTO OPERATIVO

### 3.1 Fuente nueva de datos
`CONSOLIDADO_INDICADORES_DE_PRODUCTIVIDAD_2026_-_ZONA_NORTE.xlsm` — consolidado real de productividad de toda la Zona Norte (14-16 empresas), con hojas 2023, 2024, 2025, 2026 (hasta junio), más hoja INFORME. Cubre: fruto procesado, aceite producido, % TEA (extracción aceite), almendra, y **un bloque completo de seguimiento de fruto híbrido OxG** (regional y por planta) que solo tiene datos consistentes **desde 2025**.

### 3.2 Mapeo Planta A-F → empresa real (confirmado por el usuario)
| Planta (manuscrito) | Empresa real |
|---|---|
| A | Palmaceite S.A. |
| B | Aceites S.A. |
| C | Morano Óleo S.A.S. (antes "Extractora el Roble S.A.S.") |
| D | C.I. Tequendama S.A.S. |
| E | Grasas Y Derivados S.A. |
| F | Extractora de Palma Oleaginosas del Magdalena S.A.S. (Padelma) |

### 3.3 Estado operativo real (NO es "5 de 6 plantas", es más complejo)
| Planta | Estado 2026 |
|---|---|
| A | Estable, operación normal |
| **B** | **Sin producción reportada desde mediados de 2023** (no solo "reciente") |
| **C** | **Declive severo: -90% de producción entre 2023 y 2026** (de ~120,000 t/año a ~8,500 t en 6 meses). Sigue operando pero en trayectoria de riesgo. |
| D | Estable, operación normal |
| E | Estable, operación normal (algo irregular en 2024-2025) |
| **F** (Padelma) | Declive progresivo 2023-2025, **cero datos en 2026** — cese confirmado |

**Implicación para los informes:** tratamiento diferenciado por planta, no uniforme:
- **A, D, E** → informe de decisión de inversión completo (como ya diseñado)
- **C** → el informe debe liderar con el riesgo de continuidad de suministro, recomendar cautela/diseño modular escalable, no una inversión grande asumiendo estabilidad
- **B, F** → la inversión en cogeneración ya no aplica; el valor entregable es análisis retrospectivo/aprendizaje, no recomendación a futuro

### 3.4 % de fruto híbrido OxG procesado — real, por planta y año (reemplaza supuestos)
| Planta | 2024 | 2025 | 2026 (6 meses) |
|---|---|---|---|
| A | 0% | 20.6% | **24.3%** |
| C | 0% | 1.4% | 0% |
| D | 13.9% | 15.0% | **36.2%** (aceleración fuerte) |
| E | 0% | 0% | 0% |
| B, F | No aplica (sin operación) | | |

### 3.5 Composición de biomasa del híbrido — PROXY, no dato local
Rangos de un estudio de la **zona suroccidental** (donde predomina el fruto híbrido) — no medición directa en Magdalena, pero la mejor aproximación disponible:
- Fibra: 16-24% del RFF · Tusa entera/EFB: 19-23% · APC: 20-29% · Efluentes/POME: 30-35% · Nuez: 0.3-3.5%
- **Tratamiento de incertidumbre acordado:** distribución **uniforme** por variable (solo se conoce min/max) + **normalización** de los 5 valores sorteados para que sumen 100% (evita romper el balance de masa) + combinación ponderada con el % híbrido real de cada planta: `composición_efectiva = composición_2022_medida × (1−%hibrido) + composición_hibrido_sorteada × %hibrido`
- **Limitación a declarar explícitamente en el informe** (Sección 2 de la plantilla): esto es proxy de otra zona, no dato de Magdalena.

### 3.6 Documento maestro — actualizado con datos reales
`documento_maestro_variables.xlsx` — ahora con:
- 8 filas de ejemplo (Planta A, 2022)
- 14 filas de % híbrido real por planta/año (verde = dato medido real)
- 5 filas de composición de biomasa híbrida — proxy (naranja = dato externo/proxy, con limitación anotada)
- **Pendiente guardar en el repositorio** (aún solo compartido en el chat)

---

## 4. Arquitectura del modelo para el informe (decidida 29 de julio)

### 4.1 Una corrida independiente por planta, NO las 6 juntas
El acoplamiento entre plantas en `construir_modelo_f2` solo es necesario para el frente de Pareto regional (Sección 17.3). Para el óptimo económico y el despliegue total (lo que necesita el informe), **no hay acoplamiento entre plantas** — cada una resuelve su propio problema de forma independiente. Confirmado: correr una planta sola da el mismo resultado que correrla junto con las otras 5.

**Ventajas:** extensible a plantas nuevas sin reconstruir el problema conjunto; más rápido; encaja con el Monte Carlo por planta.

### 4.2 Próximo paso de código concreto
Escribir una función que reciba los datos de UNA planta (desde el documento maestro, ya convertido a YAML/JSON) y devuelva `m1`/`m2` (óptimo económico y despliegue total) — el "recorte mínimo" de `esc1.py`/`esc2.py`, con un propósito acotado y claro (a diferencia del intento de extracción genérica de hace unos días, que se pausó por falta de objetivo concreto).

---

## 5. Próximos pasos inmediatos (en orden sugerido)

1. **Guardar en el repositorio** lo generado hoy y ayer que aún no está comiteado:
   - `parametros_comunes.py` → integrarlo al notebook (instrucciones ya escritas, pendiente ejecutar)
   - `documento_maestro_variables.xlsx` (versión actualizada con datos reales de híbrido)
   - Este archivo (`Plan_trabajo_hoja_ruta.md`)
   - Un solo `git commit` con los tres
2. **Construir el conversor Excel → YAML/JSON** del documento maestro (siguiente paso técnico, aún no iniciado)
3. **Escribir la función de "una sola planta"** (construir_modelo_f2 recortado, ver Sección 4.2)
4. **Envolver esa función en Monte Carlo**, respetando la distinción variables de mercado (compartidas) vs. variables de planta (independientes) — Sección 2.5
5. **Generar el primer informe piloto** — probablemente Planta A o D (datos más completos y estables), NO empezar por C, B o F dado su situación
6. **Aplicar al Energy Ideas Generation Programme 2026** una vez exista el informe piloto como evidencia de MVP

## 6. Cosas que NO hacer todavía
- No generalizar el modelo a "biomasa en general" — el eje de expansión validado es geográfico (otras zonas de palma), no otro cultivo
- No construir la plataforma/marketplace de proveedores — visión a 2-3 años
- No continuar la extracción completa `esc1.py`/`esc2.py` genérica — solo la función acotada de una planta (Sección 4.2)
- No generar informe de inversión estándar para Plantas B, C o F sin el tratamiento diferenciado de riesgo (Sección 3.3)
- No aplicar a convocatorias con alianza institucional hasta clarificar la situación de PI con asesoría legal
