# Consolidado de comentarios de coautores — Alexis y Electo

## ✅ ESTADO GENERAL (actualizado tras la ronda de trabajo de hoy)

**Todo lo de Electo (D1-D4, E1-E8) está resuelto.** Queda pendiente la Tabla A (18 comentarios
anclados de Alexis) y la Tabla B (9 notas generales de Alexis) — ver más abajo, sin tocar todavía.

---

## Resumen de decisiones estratégicas — todas cerradas

- **D1 (tono narrativo)** — Resuelto. Títulos de Results/Discussion revertidos a neutros
  (ver tabla en la sección D1 más abajo), pero la estructura AND-BUT-THEREFORE se mantiene dentro
  de la prosa de cada sección, sin tocarla.
- **D2 (falta Arrieta et al. 2007)** — Resuelto. Tres citas nuevas confirmadas e incorporadas:
  Arrieta et al. (2007) en Introduction; Yáñez & García (2011) en Sección 2.5; Briceño et al.
  (2015) en Introduction/2.5. Todas verificadas contra fuente primaria (PDF o búsqueda directa).
- **D3 (diseño de escenarios sin justificar: codigestión, esterilización continua, variables
  simultáneas)** — Resuelto sin rehacer los escenarios. Texto nuevo en 2.3 (justificación técnica
  de por qué la codigestión solo va en Escenario 2 y por qué la esterilización continua va con
  Escenario 1), más dos párrafos nuevos en Limitations (4.5): (1) los beneficios de la
  esterilización continua no están cuantificados en el modelo, y (2) el modelo no acredita el
  valor de reventa del equipo desplazado, con la asimetría entre escenarios reconocida
  explícitamente. Se agregó también una tercera extensión en Future Work, reconociendo que el
  reparto EFB combustión/codigestión y la tecnología de esterilización fueron fijados por diseño,
  no probados independientemente.
- **D4 (Conclusions)** — Resuelto. Versión fusionada y recortada (no la de Electo tal cual, que
  diluía el hallazgo de horas de operación al meterlo en la misma categoría de incertidumbre que
  codigestión/esterilización). Conclusions abre ahora con la distinción potencial técnico vs.
  económicamente viable, mantiene las tres cifras centrales (divergencia de rentabilidad, horas de
  operación, impuesto al carbono), y cierra reconociendo el alcance (6 plantas, 1 departamento) sin
  perder cifras concretas.

## Los 8 puntos de Electo — todos resueltos

| # | Tema | Cómo se resolvió |
|---|---|---|
| E1 | Falta Arrieta et al. (2007) | D2 |
| E2 | Codigestión solo en Escenario 2 sin justificar | D3 |
| E3 | Esterilización continua sin cuantificar | D3 — reconocido en Limitations, no cuantificado |
| E4 | Múltiples variables cambiando simultáneamente | D3 + Future Work — reconocido como alcance fijo por diseño |
| E5 | Subtítulos poco científicos | D1 — títulos neutros |
| E6 | Conclusions descriptivas | D4 |
| E7 | Evaluación general (ChatGPT) | Informativo, sin acción puntual |
| E8 | Tamaño de planta y horas de operación sin análisis cuantitativo | **Resuelto con figura nueva** — ver abajo |

### E8 — detalle de la resolución
Se generó una figura de tres paneles (beneficio neto en el óptimo económico vs. horas de
operación, vs. capacidad instalada, vs. throughput anual combinado horas×capacidad) usando los
datos reales de la Tabla 1 del manuscrito. Hallazgo más preciso que la afirmación original de 4.2:
con solo 6 plantas, horas y capacidad correlacionan de forma similar con la rentabilidad (~0.7-0.79
cada una) — no hay separación limpia entre las dos. Lo que sí separa mejor a las plantas viables de
las que no lo son es el **throughput anual combinado** (correlación ~0.87), visible directamente en
el panel (c) de la figura sin necesidad de citar el coeficiente en el texto. Texto de 4.2 ajustado
para reflejar esto con honestidad estadística (n=6, patrón descriptivo, no regresión formal).
Archivo: `figura_horas_vs_capacidad.png` / `fig_horas_capacidad.py`.

---

## Tabla de títulos neutros (D1) — para referencia rápida

| Sección | Título ABT (descartado) | Título neutro (confirmado) |
|---|---|---|
| 3.3 | Sustainability across the deployment front... | Economic, environmental, and social performance across the deployment front |
| 3.4 | From private optimum to full deployment... | Plant-level profitability analysis |
| 3.5 | Volume, not exposure: robustness to the spot price | Robustness to the spot market price |
| 4.1 | Reframing the policy question | Policy instrument sensitivity and implications |
| 4.2 | Operating hours, not technology choice, determine profitability | Effect of operating hours and plant scale on profitability |
| 4.3 | Existing infrastructure changes the investment calculus | Sensitivity to the cost of existing self-generation infrastructure |
| 4.4 | Why carbon pricing alone will not close the gap | Adequacy of the carbon tax as a policy instrument |
| 4.5 | What would have to be wrong for this conclusion to change | Limitations |
| 4.6 | Bioenergy as a discretionary business decision | *(sin cambio)* |

---

## Lo que sigue pendiente: Tabla A y Tabla B (Alexis, sin tocar todavía)

**Fuentes:**
- `Manuscrito_completo_coautores_1_Alexis.docx` — 18 comentarios anclados + 9 notas generales
  resaltadas en amarillo. **Alexis aclara explícitamente que solo revisó hasta la Sección 2**
  ("revise hasta la sección 2, a partir de la sección 3 es mejor revisar cuando lo anterior quede
  mejor organizado y presentado").
- `Comentarios_articulo_Electo.docx` — 7 puntos extensos (1-6 co-redactados con ayuda de ChatGPT
  según el propio Electo; el punto 7 es la evaluación integral directa del modelo).

**⚠️ Advertencia de versión:** el archivo de Alexis parece ser una versión **anterior** a la
reestructuración completa que hicimos en la sesión pasada (tiene "2.5 Colombian regulatory
framework" como subsección, que no coincide con nuestra numeración final 2.1-2.10 actual, y el
texto de Introduction difiere ligeramente del que reescribimos). Al mapear cada comentario, hay que
verificar contra la versión actual si el pasaje señalado sigue existiendo igual, cambió, o ya se
resolvió con la reestructuración.

---

## 🔴 Decisiones estratégicas — requieren tu criterio antes de tocar texto

Estos no son correcciones puntuales; son choques de fondo entre lo que hicimos la sesión pasada y
lo que sugieren los coautores. Conviene decidirlos primero porque afectan cómo se resuelven varios
comentarios menores.

### D1. Tono narrativo de los subtítulos (Electo, punto 5) — choca directo con la narrativa ABT
Electo objeta explícitamente títulos como *"Beyond technical potential..."*, *"Scenario 1
collapses..."*, *"Neither route dominates outright"*, *"What separates viable mills from unviable
ones..."* — los llama "más periodísticos que científicos" y propone volver a subtítulos neutros
tipo *"3.1 Baseline and optimized electricity generation"*, *"3.4 Plant-level profitability
analysis"*. Esto es una reversión parcial de toda la reescritura ABT de la sesión pasada.
**Necesito que decidas**: ¿mantenemos el enfoque narrativo y respondemos a Electo defendiéndolo
(está respaldado por el propio handout de storytelling científico que trajiste al inicio), lo
revertimos parcialmente, o negociamos un punto medio (títulos neutros pero mantenemos la
narrativa ABT dentro de la prosa de cada sección)?

### D2. Falta la cita de Arrieta et al. (2007) — antecedente directo del propio grupo (Electo, punto 1) — ✅ RESUELTO

**Confirmado — 3 citas a incorporar:**
- **Arrieta, F.R.P., Teixeira, F.N., Yáñez, E., Lora, E., Castillo, E. (2007).** "Cogeneration
  potential in the Colombian palm oil industry: three case studies." Biomass and Bioenergy, 31(7),
  503-511. https://doi.org/10.1016/j.biombioe.2007.01.016 — antecedente directo del propio grupo
  (Silva Lora, coautor de este manuscrito, también coautor aquí); va en Introduction, vacío de
  literatura.
- **Yáñez, E., García, J.A. (2011).** "Cogeneration with oil palm biomass in the Colombian
  electricity system: barriers, prospects and opportunities." Palmas, 32(3), 49-62. — barreras
  regulatorias específicas; va en Sección 2.5 (marco regulatorio), responde también al comentario
  #15 de Alexis.
- **Briceño, I., Valencia, J., Posso, M. (2015).** "Potencial de generación de energía de la
  agroindustria de la palma de aceite en Colombia." Palmas, 36(3), 43-53. — potencial nacional
  (340 MW), detalle de Ley 1715/2014, estructura de mercado CREG, modelo financiero de
  prefactibilidad para planta representativa de 30 t RFF/h. **Verificado con el PDF real
  compartido por el usuario** — resuelve una confusión de atribución previa (aparecía mal citado
  como "Álvarez" en una fuente secundaria; el apellido correcto de citación es Briceño, el primer
  apellido de la autora principal, Ivonne Cristina Briceño Álvarez). Va en Introduction
  (potencial nacional) y/o Sección 2.5.

### D3. Diseño de escenarios no está justificado — dos preguntas relacionadas (Electo, puntos 2-4)
Tres objeciones relacionadas que probablemente se resuelven juntas:
- ¿Por qué la codigestión solo se evalúa en Escenario 2 y no en Escenario 1?
- ¿Qué aporta cuantitativamente la esterilización continua? (Electo señala que esto introduce una
  **segunda variable de cambio simultánea** entre escenarios, además de la turbina)
- Como consecuencia de lo anterior: los escenarios cambian *múltiples* variables a la vez (turbina,
  destino del EFB, digestión vs. codigestión, esterilización continua vs. por lotes), no solo la
  tecnología de conversión — lo cual dificulta atribuir el resultado a una sola causa.

Esto es un comentario metodológico de fondo, no de redacción. Requiere decidir si se responde con
una justificación textual más fuerte (por qué el diseño de escenarios está construido así,
probablemente ligado a la lógica técnica real: EFB es el combustible sólido principal del
Escenario 1, por eso no se desvía a digestión) o si amerita alguna aclaración adicional en
Limitations.

### D4. Conclusions — Electo propone una versión alternativa completa (punto 6)
Electo considera las Conclusions actuales "descriptivas, no analíticas" y adjunta una versión
reescrita propia, con más énfasis en interpretación, limitaciones explícitas, y líneas de trabajo
futuro (Monte Carlo/incertidumbre, LCA, aplicación a otros países). Vale la pena comparar su
versión con la que dejamos la sesión pasada antes de decidir qué tomar.

### D5. Introducción demasiado extensa (ambos coautores coinciden)
Alexis: *"Hay que dejar más clara la novedad en la introducción"* + *"EN GENERAL, CREO QUE HAY QUE
MEJORAR LA INTRODUCCIÓN"*. Electo: recortar ~15-20% adicional y mover detalle descriptivo a
Discussion. **Ya recortamos la Introduction de 1,095 a 871 palabras la sesión pasada** — este
comentario pide ir más allá de ese recorte, y además pide reforzar (no solo acortar) la claridad de
la novedad, lo cual puede ir en direcciones opuestas al recorte puro.

---

## Tabla A — Comentarios anclados de Alexis (18)

| # | Sección (versión de Alexis) | Texto anclado | Comentario | Estado |
|---|---|---|---|---|
| 0 | Introduction | "The trade-offs between privately optimal and technically and environmentally optimal has received limited attention..." | Esto no se resalta en los párrafos anteriores. ¿De dónde sale esta conclusión? | Pendiente |
| 1 | Introduction | "privately optimal" | ¿A qué te refieres con este término? | Pendiente |
| 2 | Introduction | "Available studies assessing this issue typically discusses single-mill technical screenings..." | Esta oración no la entiendo bien, reescríbela de forma más clara | Pendiente |
| 3 | Introduction | "here" | ¿A qué se refiere "here"? | Pendiente |
| 4 | Introduction | "CPO" | Inclúyelo en la nomenclatura | Pendiente |
| 5 | Introduction | "at a national rather than mill-specific scale" | Hay que explicar por qué la escala es importante — ¿por qué es importante conocer a escala de molinos más que a escala nacional? | Pendiente |
| 6 | Introduction | "and what would closing it cost in forgone private profitability" | Esto no se entiende, hay que reescribirlo | Pendiente |
| 7 | Introduction | "A distinct literature applies" | ¿Cuál? | Pendiente |
| 8 | Introduction | "In Colombia, regardless of the significant biomass-based potentialities..." | Esto hay que escribirlo mejor, me quedó un poco confuso con la redacción | Pendiente — **nota: este pasaje con "(REF)" como placeholder literal sugiere texto sin terminar** |
| 9 | 2. Materials and Methods (intro) | "This study assesses whether the deployment of biomass-based energy systems..." | Esto debe quedar más claro desde la introducción | Pendiente |
| 10 | 2. Materials and Methods (intro) | "A multi-objective mixed-integer linear programming (MILP)" | ¿Por qué usas este método y no otro? Hay que justificarlo | Pendiente — **relacionado con Mavrotas (2009), ya citado; puede que solo falte reforzar la justificación en prosa** |
| 11 | 2.3 System boundary and scenarios | "The system boundary is drawn at the mill gate..." | Esto no lo entiendo, debes explicarlo mejor | Pendiente |
| 12 | 2.4 Optimization model | "XXXX" | Aquí define qué catálogo y qué variables usaste en la selección | **Placeholder sin completar en el documento — revisar si sigue en la versión actual** |
| 13 | 2.4 Optimization model | "Surplus electricity is not remunerated at a unique price..." | Este párrafo es un poco confuso, hay que explicarlo de forma más clara | Pendiente |
| 14 | 2.4 Optimization model | "Table 3 — Governing equations" | No entiendo la tabla. Mejor presentar las ecuaciones y explicarlas; agrupar todo lo que se usa en subsecciones siguientes | Pendiente — **coincide con la nota general sobre 2.10 (ver Tabla B)** |
| 15 | 2.5 Colombian regulatory framework | "Three families of instruments govern the economics of distributed bioenergy..." | Aquí más que señalar las leyes, es mejor describir los detalles que afectan el precio de la electricidad y cómo lo afectan | Pendiente |
| 16 | 2.6 Techno-economic parameters | "Capital costs are derived from supplier quotations..." | Esto hay que fundamentarlo mejor | **Reforzado por Alexis vía telefónica — más peso del que sugiere el texto corto.** Probablemente pide: cuántas cotizaciones se obtuvieron y de qué proveedores, fecha de las cotizaciones, cómo se manejó la conversión de moneda/escalamiento a USD 2026 (ya se menciona el Chemical Engineering Plant Cost Index, pero falta detallar el procedimiento), y si los valores son específicos por planta o un promedio genérico aplicado a las 6. Antes de redactar la respuesta, confirmar con Alexis qué nivel de detalle espera (¿nombrar proveedores? ¿anexar las cotizaciones como material suplementario?) |
| 17 | 2.7 Sustainability indicators | "Three indicators, the levelized cost of electricity, the greenhouse gas balance..." | ¿Por qué estos indicadores son indicadores de sostenibilidad? ¿Por qué se usan indicadores de sostenibilidad? | Pendiente |

## Tabla B — Notas generales de Alexis (resaltadas, no ancladas a un punto específico)

| # | Ubicación | Nota | Estado |
|---|---|---|---|
| G1 | Bloque de comentarios al inicio | Usar Mendeley para las referencias | Pendiente — gestión de referencias, no contenido |
| G2 | Bloque de comentarios al inicio | Hay que dejar más clara la novedad en la introducción | Ver decisión D5 |
| G3 | Bloque de comentarios al inicio | Decidir terminología: "Palm Oil Mill (POM)", "mill", o "plant" — usarla consistentemente | Pendiente — **auditoría de consistencia terminológica en todo el manuscrito** |
| G4 | Bloque de comentarios al inicio | Usar abreviaturas de biomasa de forma consistente | Pendiente |
| G5 | Bloque de comentarios al inicio | En la Nomenclatura, incluir abreviaturas usadas en el trabajo + variables de las ecuaciones; considerar separar variables de subíndices | Pendiente |
| G6 | Bloque de comentarios al inicio | Mejorar las keywords; revisar las usadas en el "artículo anterior" (Barrera Hernandez et al. 2024) | **Ya cambiamos las keywords la sesión pasada — revisar si las nuevas satisfacen esta observación o si Alexis las vio antes del cambio** |
| G7 | Introduction | "EN GENERAL, CREO QUE HAY QUE MEJORAR LA INTRODUCCIÓN. FALTA RESALTAR LA NOVEDAD DEL ESTUDIO DE FORMA MÁS CLARA." | Ver decisión D5 |
| G8 | 2.4 Optimization model | "XXXX" (mismo placeholder que #12) | Ver #12 |
| G9 | 2.10 Modeling workflow | "ESTAS SUBSECCIONES DEBEN COMBINARSE CON LA SUBSECCIÓN DE LA TABLA 3. ESO DEBE ORGANIZARSE MEJOR." | Pendiente — reorganización de Methods, relacionado con #14 |

## Tabla C — Puntos de Electo (7, resumidos; ver documento completo para el detalle)

| # | Tema | Resumen | Estado |
|---|---|---|---|
| E1 | Falta cita Arrieta et al. (2007) | Antecedente directo del propio grupo (Silva Lora coautor); ausencia notoria para un revisor | Ver decisión D2 |
| E2 | Codigestión solo en Escenario 2 | Falta justificar por qué no se evaluó también en Escenario 1; sugiere incluso un modelo que optimice la fracción de EFB entre combustión/codigestión | Ver decisión D3 |
| E3 | Aporte de esterilización continua sin cuantificar | Introduce una segunda variable de cambio simultánea entre escenarios; pide cuantificar vapor adicional, electricidad ganada, costo | Ver decisión D3 |
| E4 | Comparación con múltiples variables simultáneas | Consecuencia de E2+E3: no se puede aislar qué causa la diferencia de rentabilidad entre escenarios; sugiere diseño factorial | Ver decisión D3 |
| E5 | Subtítulos "poco científicos" | Objeta el tono narrativo ABT; propone subtítulos neutros | Ver decisión D1 |
| E6 | Conclusions "descriptivas, no analíticas" | Propone versión alternativa completa | Ver decisión D4 |
| E7 | Evaluación integral (directo de ChatGPT) | Calificación 8.8-9.2/10; puntos fuertes y débiles generales; recomienda JCP como mejor opción (60-70% aceptación estimada), recorte adicional de Introduction 15-20%, incertidumbre tipo Monte Carlo, más comparación internacional en Discussion, LCA más completo | Informativo — no requiere acción puntual, pero contextualiza las prioridades |
| E8 | Tamaño de planta y horas de operación sin analizar en profundidad | El manuscrito ya identifica (4.2) que las horas de operación determinan la rentabilidad más que la tecnología, pero **nunca lo prueba cuantitativamente** ni discute el mecanismo a fondo. Electo pide: (1) una subsección dedicada 4.X; (2) responder explícitamente si capacidad instalada (t FFB/h) o horas efectivas pesa más; (3) si existe un umbral mínimo de horas/capacidad para viabilidad; (4) por qué plantas grandes pueden ser menos rentables que medianas con mayor utilización; (5) si el bajo factor de utilización viene de disponibilidad de biomasa, estacionalidad, o problemas operativos; (6) idealmente un análisis cuantitativo — gráfico o regresión simple de beneficio vs. horas y beneficio vs. capacidad, para separar el efecto de cada variable | **Pendiente — requiere cálculo nuevo en el notebook** (regresión/dispersión beneficio vs. horas vs. capacidad, con las 6 plantas); ver nota de vínculo con D1/4.2 abajo |

**Nota de vínculo:** E8 se conecta directamente con la Sección 4.2 ya escrita ("Operating hours,
not technology choice, determine profitability"). Ahora mismo esa sección afirma la conclusión sin
mostrar el análisis cuantitativo que la respalda — con solo 6 plantas no alcanza para una regresión
formal con significancia estadística, pero sí se puede mostrar un gráfico de dispersión (beneficio
neto vs. horas anuales, y beneficio neto vs. capacidad instalada) que deje ver visualmente cuál de
las dos variables separa mejor a las plantas rentables de las no rentables — en el mismo espíritu
de las figuras de rango que ya construimos esta sesión. Si D1 se resuelve manteniendo parte de la
narrativa, este es un buen candidato para reforzar con datos en vez de solo prosa.

---

## Cómo seguimos

Sugiero resolver primero las 5 decisiones estratégicas (D1-D5), ya que varias de las correcciones
puntuales de la Tabla A dependen de esas decisiones (por ejemplo, si D1 se resuelve revirtiendo el
tono narrativo, eso afecta directamente cómo se reescriben varios títulos de sección). Después
seguimos con la Tabla A en orden (son casi todas de Introduction y Methods, que es justo lo que
Alexis pidió revisar primero).

¿Empezamos por D1 (tono narrativo), o prefieres otro orden?
