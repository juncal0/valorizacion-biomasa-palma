# Estado del proyecto — Resumen para continuar en nuevo chat (ACTUALIZADO)

**Instrucciones:** pega este documento completo como primer mensaje del chat nuevo, junto con (1)
el notebook actualizado y (2) `Article_Outline_v1.md` y `Lista_de_tareas_pendientes.md` si los
tienes a mano (son los documentos de trabajo vivos, más detallados que este resumen).

**Este documento reemplaza cualquier versión anterior de "Estado_proyecto_continuidad.md".** La
versión previa describía un estado del modelo que ya no aplica — desde entonces se encontraron y
corrigieron varios bugs adicionales que cambiaron la conclusión central del artículo.

---

## Qué es este proyecto

Artículo científico (Cap. 5 de tesis doctoral), para Journal of Cleaner Production: valorización
energética de biomasa residual de palma de aceite, **6 plantas extractoras del Magdalena,
Colombia** (Plantas A-F). Compara dos configuraciones de cogeneración (Escenario 1: turbina de
extracción-condensación + biogás POME; Escenario 2: turbina de contrapresión + biogás
POME+raquis co-digerido) con un modelo MILP en **Python/Pyomo/GLPK**.

**Título:** "Beyond technical potential: profitability, robustness, and regional sustainability
trade-offs in mature cogeneration pathways for palm oil mill residues"

**Autores:** Juan Camilo Barrera-Hernandez [afiliación pendiente], Electo Eduardo Silva Lora (NEST,
Federal University of Itajubá, Brasil), Alexis Sagastume Gutierrez (Nueva Granada Military
University, Colombia), Jesús Alberto García-Nuñez (Cenipalma, Colombia).

## Archivos y entregables

- **GitHub:** `https://github.com/juncal0/valorizacion-biomasa-palma`
- **Outline de trabajo (el documento vivo más importante):** `Article_Outline_v1.md` — contiene
  el texto completo (Abstract, Methods, Results, Discussion, Conclusions), todas las tablas y
  figuras con sus valores finales, y notas de auditoría de cada corrección/cita hecha.
- **Lista de tareas:** `Lista_de_tareas_pendientes.md` — checklist detallado de qué está hecho y
  qué falta, sesión por sesión.
- **Manuscrito Word:** `Manuscrito_completo_coautores.docx` (32 páginas) — versión completa lista
  para revisión de coautores, sincronizada con el outline (Abstract, Introduction con bibliografía
  robustecida, Methods, Results con Tablas 4-9 y Figuras 1-11, Discussion, Conclusions,
  References). **Importante:** el Word se construye con scripts Node.js
  (`build.js`, `build2.js`, `build3.js` en `/home/claude/docbuild/`) que NO persisten entre
  sesiones — si se retoma la edición del Word en un chat nuevo, hay que reconstruir el pipeline o
  editar el .docx directamente.

## Flujo de trabajo (respetar)

1. Indicar en qué sección/celda del notebook va cada código.
2. Documentar cada hallazgo en las notas metodológicas / el outline.
3. Git tras cada avance.
4. **Validar todo resultado nuevo contra un valor ya confirmado antes de aceptarlo** — esta sesión
   encontró 4 bugs reales precisamente porque se insistió en cruzar cada resultado nuevo contra
   Tabla 5 (o el payoff table) antes de usarlo. No confiar en un resultado aislado, por razonable
   que parezca.
5. Cuando se edite el outline, **recordar propagar el cambio también al Word** — esta sesión
   descubrió tarde que varias actualizaciones grandes (Introduction reescrita, lista de
   referencias, Ecuación 6) se quedaron solo en el outline durante un buen rato sin llegar al
   .docx entregado. **Incluso después de una ronda de "sincronizar todo", aparecieron DOS
   párrafos más con cifras viejas** (uno en Results §3.6 con $169/$593 en vez de $294/$599, y otro
   en Results §3.2 con cifras de varias rondas atrás) que sobrevivieron sin detectarse hasta que
   el usuario preguntó directamente por una discrepancia. **Antes de dar el Word por
   definitivamente sincronizado, hacer una búsqueda de texto exhaustiva** (`grep`/`pdftotext`)
   contra TODOS los valores numéricos históricos conocidos del proyecto, no solo revisar
   sección por sección de memoria.

---

## 🔴 RESULTADO CENTRAL VIGENTE (reemplaza cualquier resultado de sesiones anteriores)

| | **Escenario 1** | **Escenario 2** |
|---|---|---|
| Óptimo económico | 67.0 GWh (**32.2%** del potencial) → **+$258,705/año** | 136.2 GWh (**92.3%** del potencial) → **+$3,427,932/año** |
| Despliegue 100% | 208.2 GWh → **−$6,531,746/año** | 147.5 GWh → **+$2,315,672/año** |
| Costo de desplegar todo | $6,790,451/año (**2,625%** del óptimo) | $1,112,260/año (**32%** del óptimo) |
| Costo por tCO2 adicional | $294/tCO2 | $599/tCO2 |
| ¿Rentable en todo el frente? | **NO** — negativo ya un paso después del óptimo (40.6%, −$413,799) | **SÍ**, en todo el rango 92.3%-100% |
| Plantas rentables al 100% | **0 de 6** | **4 de 6** (B, C, D, E; A y F no) |
| Precio de equilibrio agregado (despliegue forzado 100%) | 0.1050 USD/kWh (actual: 0.0703) | 0.0500 USD/kWh |
| Con 30% de incentivo de capital | Sigue NEGATIVO al 100% (−$697,660) | N/A, no lo necesita |

**Mensaje central:** Escenario 2 es más rentable y mucho más robusto en todo su rango. Escenario 1
solo es viable en una ventana muy angosta cerca de su propio óptimo (32.2%) y se desploma
severamente hacia el despliegue total — ni siquiera el incentivo de capital más generoso
disponible en Colombia (30%) alcanza para revertirlo. El impuesto al carbono colombiano
(USD 8.70/tCO2) cubre solo ~3% (Esc.1) y ~1.5% (Esc.2) del costo implícito de cerrar la brecha.

**Esto es lo OPUESTO al resultado que aparecía en versiones anteriores de este proyecto** (que
decían "ambos escenarios rentables al 100%, sin necesidad de subsidio"). Ese resultado quedó
invalidado por los bugs descritos abajo. No usar ningún número de sesiones anteriores a esta.

---

## Los 4 bugs encontrados y corregidos en esta sesión (además de las correcciones de sesiones previas)

1. **Tope conjunto autoconsumo/permuta**: estaban modelados como dos restricciones independientes,
   cada una topando en `consumo_medido_kW[p]`, permitiendo hasta 2× la demanda a precio retail en
   vez de 1×. Arreglo: una sola restricción `autoconsumo + permuta ≤ consumo_medido`.
2. **`consumo_medido_dict` sin corregir por sustitución tecnológica**: usaba la suma de 11 etapas
   de proceso con tecnología vieja, sin ajustar por las sustituciones de cada escenario
   (esterilización continua, clarificación dinámica). Corregido con deltas específicos por planta
   y por escenario.
3. **Costo de oportunidad del raquis (EFB) — componente nuevo, nunca antes modelado**: se agregó
   vía Net Fertilizer Replacement Value (NFRV), con factores de equivalencia de Caliman et al.
   (2001), precios reales de Fedepalma/DANE-Sipsa Q1 2025 (no inventados), y una eficiencia de
   mineralización del 70% (rango 60-80%, con 3 referencias empíricas). Valor final: **$16.82
   USD/t** de raquis. Entra a la función objetivo escalado por `factor_utilizacion` en Escenario 1
   (combustión) y por `factor_util_biogas` en Escenario 2 (co-digestión).
4. **Reparto autoconsumo/permuta/bolsa reconstruido con una aproximación errónea** (en el análisis
   de robustez al precio, Sección 24 del notebook): usaba `permuta = min(exced, auto)` en vez de
   las columnas reales `excedente_permuta_kWh`/`excedente_bolsa_kWh` ya calculadas por el modelo.
   Daba beneficios sustancialmente distintos (−$3.79M en vez de −$6.53M). Lección: si el modelo ya
   calculó y guardó un dato, usarlo directo — nunca reconstruirlo con una aproximación externa.
5. **(Bug adicional, en la construcción de los diagramas Sankey)**: el modelo del panel de
   "despliegue total" (`m2`) se había resuelto con `objetivo='excedente'` (maximizar generación
   pura) en vez de `objetivo='economico', restriccion_f2=f2_max` — daba un reparto
   autoconsumo/permuta/bolsa arbitrario y un beneficio incorrecto. Lección: **siempre validar el
   beneficio de un modelo resuelto contra un valor de referencia conocido ANTES de usarlo para
   generar una figura o tabla**, no solo al final.

## Variables/funciones críticas que deben existir en memoria (orden de dependencia)

1. `consumo_medido_dict` (Esc.1) y `consumo_medido_esc2_dict` (Esc.2), con las correcciones de
   sustitución tecnológica ya aplicadas.
2. `costo_oport_dict` (fibra+cuesco, de `df_biomasa_disponible` × horas/1000 × precios PKS/MF).
3. `costo_oport_raquis_USD_t = 16.82` y `costo_oport_raquis_dict` (de
   `df_biomasa_disponible['Raquis']` × horas/1000 × 16.82).
4. `construir_modelo_f2` y `construir_modelo_f2_esc2`, ambas con: el tope conjunto
   `r_tope_auto_permuta`, el parámetro `m.costo_oport_raquis`, y el término correspondiente en
   `f1_economico`.
5. Al generar cualquier tabla/figura que dependa de `excedente_permuta_kWh`/`excedente_bolsa_kWh`,
   **usar siempre las columnas ya calculadas por el modelo**, nunca reconstruirlas con fórmulas
   propias.

---

## Bibliografía — estado y hallazgos de esta sesión

- **Citas mal atribuidas, ya corregidas en todo el documento**: "Guerrero et al. (2023)" y
  "Chávez et al. (2026)" → deben ser **Mosquera-Montoya et al. (2022)**, DOI
  10.56866/01212923.13911, y **Mosquera-Montoya et al. (2025)**, DOI 10.56866/01212923.14473
  (ambos en Revista Palmas). Verificar que no queden rastros de los nombres viejos en ningún lugar
  del documento antes de someter (esta sesión encontró rastros olvidados dos veces).
- **Introduction robustecida** con 14 citas nuevas, todas verificadas con rigor (autor, revista,
  volumen, DOI, y el contenido específico usado contrastado contra la fuente real):
  - Contexto/potencial nacional: Sagastume Gutiérrez et al. (2020), Alean et al. (2025),
    Rocha-Meneses et al. (2023), Cabello Eras et al. (2018), Martinez et al. (2025).
  - Vacío de literatura (evaluaciones agregadas de una sola tecnología): Boom-Cárcamo et al.
    (2025), Martinez et al. (2025).
  - Madurez tecnológica: Dovichi Filho et al. (2021); biorefinería: García-Núñez et al. (2016).
  - Estado del arte en optimización matemática aplicada a biomasa de palma (nuevo párrafo):
    Harahap et al. (2019), Ho et al. (2015), Teh et al. (2023), Aprilianto & Rau (2025), Nair et
    al. (2022), Memari et al. (2018) — **ninguno de estos trabaja Colombia**, lo cual es un punto
    de novedad geográfica/metodológica real para el artículo.
- **Pendiente de verificación más profunda**: Voogt et al. (2021, diseño conceptual de
  co-digestión) y Caliman et al. (2001, factores de equivalencia del raquis) — ambos citados pero
  sin confirmación de fuente primaria. Kieserita (fuente de Mg en el NFRV) usa un precio sin
  verificar.
- **No volver a citar** un hallazgo específico de un paper sin haberlo confirmado — esta sesión
  detectó y corrigió a tiempo un caso propio en el que se iba a afirmar un resultado de Memari et
  al. (2018) sin haberlo verificado realmente (solo se confirmó que comparan carbon tax vs.
  cap-and-trade, no cuál "ganó").

---

## Qué falta (ver `Lista_de_tareas_pendientes.md` para el detalle completo)

- Tablas de Apéndice (barrido de precio completo cada 0.01 USD/kWh, caracterización de biomasa) —
  pospuesto.
- Bloque C completo (cover letter, highlights, CRediT, declaration, data availability, funding,
  referencias en formato final de la revista) — pospuesto a después de comentarios de coautores.
- Confirmar afiliación de Juan Camilo Barrera-Hernandez.
- Verificar edición exacta de Mosquera-Montoya et al. (2025) usada para los rangos de costo de la
  Tabla 7.
- Precio de kieserita sin verificar (componente menor del NFRV).
- Anomalía menor documentada (no bloqueante): el precio actual de Planta D cae fuera del rango de
  benchmarking de Cenipalma — ya explicado en el texto como plausible (el rango es de otras 7
  plantas, no de Planta D), pero vale la pena confirmar contra datos de campo antes de someter.

---

## Próximos pasos según lo que el usuario quiera retomar

- **Redacción**: seguir con Bloque C, o pulir prosa de secciones ya escritas.
- **Comentarios de coautores**: cuando lleguen, aplicar el mismo estándar de esta sesión — validar
  cualquier número que cambie contra el ya confirmado en Tabla 5/payoff table antes de aceptarlo.
