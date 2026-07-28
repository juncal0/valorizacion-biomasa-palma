# Estado del proyecto — Continuidad v5 (ACTUALIZADO)

**Instrucciones:** pega este documento completo como primer mensaje del chat nuevo, junto con:
1. El archivo `Manuscrito_completo_coautores_v2.docx` (la versión real y actual del manuscrito)
2. `Cambios_confirmados_v2.md` (registro detallado de los ~30 bloques de cambios ya aplicados)
3. `Consolidado_comentarios_coautores.md` (si necesitas el detalle completo de qué pidió cada
   coautor)

**Este documento reemplaza `Estado_proyecto_continuidad_v4.md`.** Desde v4: se recibieron y
resolvieron comentarios reales de dos coautores (Alexis y Electo) sobre una versión anterior del
manuscrito, y **todos los cambios acordados se aplicaron directamente sobre el `.docx` real**
(no solo se documentaron en texto — esta vez se editó el archivo XML del Word directamente,
empaquetó y validó). El resultado es `Manuscrito_completo_coautores_v2.docx`.

---

## Qué cambió estructuralmente en v2 (respecto a v1)

- **Título y keywords** actualizados (sin "cogeneration", con "Colombia" explícito y ángulo de
  optimización).
- **Introduction** reescrita sobre un outline de 6 bloques mapeados al título, con ~24 citas
  (incluye Arrieta 2007, Montoya 2020, Ramirez-Contreras 2020, Boom-Cárcamo 2025, Martinez 2025,
  Sodri & Septriana 2022, Peña González 2021, Orjuela-Castro 2019, González-Salazar 2014, Dovichi
  Filho 2021, entre otras), con el reclamo de novedad verificado y acotado con precisión.
- **Methods reorganizado** de 10 secciones planas (2.1-2.10) a una jerarquía de 6 secciones con
  subsecciones:
  ```
  2.1 Study area and data collection
    2.1.1 Plant characterization and biomass availability
    2.1.2 Current energy configuration
  2.2 Model formulation
    2.2.1 Modeling workflow overview (diagrama movido aquí, antes era 2.10 al final)
    2.2.2 System boundary and scenario definitions
    2.2.3 Optimization model
  2.3 Model parameters
    2.3.1 Regulatory framework represented in the model
    2.3.2 Techno-economic parameters
  2.4 Sustainability indicators
  2.5 Multi-objective solution method
  2.6 Policy instrument analysis
  ```
- **Tabla 3 (Governing equations) eliminada por completo** — las 11 ecuaciones que sobrevivieron
  (se descartaron 2, correlación HHV y eficiencia de caldera ASME, ambas marcadas "internal
  consistency check only" sin ancla en la prosa) se insertaron en línea, cada una en la subsección
  donde se usa, **renumeradas 1-11 en el orden real en que aparecen en el documento** (no en el
  orden original de la vieja tabla).
- **Nomenclatura** ampliada con 18 símbolos nuevos que no estaban documentados (C_i, f1, f2,
  LCOE_i, ΔGHG_i, HH_i, etc.), agregados a la tabla de Parameters.
- **Figuras**: se regeneró el diagrama de flujo (ahora Figura 1, sin referencias a ecuaciones en
  los cuadros), y **toda la numeración de figuras se corrió y consolidó**: secuencia final **1-14
  sin huecos**. Se agregó una figura nueva (ahora Figura 12) en Discussion 4.2, mostrando beneficio
  neto vs. horas de operación / capacidad instalada / throughput combinado, respondiendo al punto
  de Electo sobre profundizar el hallazgo de horas de operación.
- **9 referencias bibliográficas nuevas agregadas** a la lista de References (estaban citadas en
  el texto pero faltaban en la bibliografía): Briceño 2015, Calderón Prieto 2025, González-Salazar
  2014, Haimes et al. 1971, Orjuela-Castro 2019, Peña González 2021, Rahayu 2015, Silva-Imbachi
  2019, Sodri & Septriana 2022.
- **Los 6 títulos neutros de Results/Discussion** (acordados con Electo en D1, sesión anterior)
  finalmente se aplicaron al documento real: 3.3, 3.5, 4.1, 4.2, 4.3, 4.4. Antes de esta sesión,
  **solo 3.4 y 4.5 se habían aplicado correctamente**; el resto seguía con títulos narrativos
  viejos o incluso versiones más informales que nunca pasaron por revisión.
- **Terminología POM/EFB/POME** aplicada de forma consistente en Introduction y gran parte de
  Methods (reemplazando usos sueltos de "mill"/"plant"/términos completos sin abreviar).

---

## ⚠️ Patrón importante detectado esta sesión — leer antes de confiar en "ya está confirmado"

Varias veces durante esta sesión se descubrió que un cambio que aparecía como "confirmado" en el
registro de texto (`Cambios_confirmados_v2.md`, de la sesión anterior) **nunca se había aplicado
realmente al `.docx`**, o se había aplicado de forma incompleta:
- Los 6 títulos neutros de D1 (Results/Discussion) — solo 2 de 8 estaban aplicados.
- La Ecuación 5 (tarifa/ingreso) se insertó con la cita "(Equation 5)" pero **sin la fórmula real**
  — un error propio de esta sesión, ya corregido.
- La corrección de esterilización continua (post-hallazgo IACSA, quitar el argumento de
  "sensibilidad de la turbina") nunca se aplicó — corregida esta sesión.
- La figura de sostenibilidad (panel de 3) sí existía, pero como "Figure 9", no como la "Figure 7"
  que se asumía en el mapeo de renumeración de la sesión anterior.
- 9 referencias citadas en texto nunca llegaron a la bibliografía.

**Lección para el chat nuevo**: no asumir que algo documentado como "acordado" en un registro de
texto ya está en el `.docx` real — siempre verificar contra el archivo real antes de construir
sobre esa base.

---

## 🔴 RESULTADO CENTRAL VIGENTE (sin cambios de fondo, solo de redacción/estructura)

| | **Escenario 1** | **Escenario 2** |
|---|---|---|
| Óptimo económico | 67.0 GWh (32.2% del potencial) → **+$258,705/año** | 136.2 GWh (92.3%) → **+$3,427,932/año** |
| Despliegue 100% | 208.2 GWh → **−$6,531,746/año** | 147.5 GWh → **+$2,315,672/año** |
| Costo por tCO2 adicional | $294/tCO2 | $599/tCO2 |
| Plantas rentables al 100% | 0 de 6 | 4 de 6 (B, C, D, E) |
| Precio de equilibrio (despliegue 100%) | 0.1050 USD/kWh | 0.0500 USD/kWh |

**Mensaje central**: Escenario 2 es más rentable y robusto en todo su rango; Escenario 1 solo es
viable cerca de su propio óptimo (32.2%) y ni el incentivo de capital más generoso disponible en
Colombia (30%) lo revierte. Lo que separa plantas rentables de las que no lo son es más el
throughput anual combinado (horas × capacidad) que la tecnología elegida — Figura 12 (nueva) lo
muestra visualmente.

---

## Qué falta (por prioridad)

### 🔴 Crítico
1. **Conteo de palabras vs. JCP**: confirmado con la fuente oficial de ScienceDirect que el rango
   6,000-8,000 incluye *"tables, illustrations and references"* — es decir, References sí cuenta.
   El manuscrito está en **~12,180-12,200 palabras totales**, entre 4,200 y 6,200 por encima del
   máximo. Ya se intentó recorte moderado en Introduction y Methods (2.2.2, 2.3.2) sin gran efecto,
   porque gran parte del contenido "de sobra" responde directamente a comentarios de coautores que
   pidieron *más* detalle, no menos. **Pendiente decidir entre**: (a) someter igual y confiar en
   flexibilidad editorial, (b) mover contenido sustancial a Material Suplementario (cotizaciones de
   capital completas, parte de Limitations, alguna figura), o (c) confirmar directamente con JCP/
   Editorial Manager si el límite es estricto.

### 🟡 Pendiente de las revisiones de coautores
2. **Data Availability statement** — nunca se escribió (parte del Bloque C pospuesto). Texto
   tentativo ya acordado: repositorio de GitHub + exclusión de datos crudos por confidencialidad.
3. **G1 (Alexis)**: usar Mendeley — administrativo, no requiere mi intervención.
4. **Confirmar con Alexis** si el alcance de las cotizaciones de capital (comentario #16, ya
   resuelto con datos reales de 10 cotizaciones) necesita además anexarse como material
   suplementario, o si el texto ya es suficiente.

### ⚪ Verificación final antes de someter
5. **Barrido final de "cogeneration"/"mill"** fuera de Methods (Results, Discussion, Conclusions)
   — no se verificó exhaustivamente en esta sesión, solo se corrigieron instancias encontradas de
   paso.
6. **Bloque C completo**: cover letter, highlights, CRediT, declaration of interest, funding
   statement — sigue pospuesto desde el inicio del proyecto.
7. Verificación de citas pendientes de sesiones anteriores, nunca resueltas: Voogt et al. (2021)
   contra fuente primaria completa, edición exacta de Mosquera-Montoya et al. (2025) para Figura
   13 (antes 12, sensibilidad A/D), precio de kieserita, afiliación institucional de Juan Camilo
   Barrera-Hernandez.
8. Anomalía de Planta D (costo fuera del rango de benchmarking de Cenipalma) — documentada en el
   pie de la Figura 13, pendiente de confirmación de coautores.

---

## Flujo de trabajo para el chat nuevo

1. Si se van a aplicar más cambios de texto/estructura al `.docx`, usar el mismo método de esta
   sesión: descomprimir con `unzip`, usar `merge_runs.py` (skill de docx), editar
   `word/document.xml` con Python (buscar/reemplazar texto exacto, verificando encoding de
   caracteres especiales como `&amp;`, comillas rectas vs. curvas, y el marcador
   `<w:lastRenderedPageBreak/>` que puede partir texto en runs separados — eliminarlo si aparece),
   reempaquetar con `zip -Xr`, y **validar siempre con `validate.py` antes de dar por bueno
   cualquier cambio**.
2. **Al renumerar figuras o ecuaciones, cuidado con colisiones de subcadena** (ej. "Figure 1" es
   substring de "Figure 10", "Figure 11"...) — usar marcadores temporales únicos o procesar en el
   orden que evite colisión, y verificar el resultado contando apariciones antes/después.
3. Seguir verificando resultados nuevos contra la tabla de resultado central confirmado antes de
   aceptarlos.
4. Antes de citar cualquier fuente nueva, verificarla por búsqueda web (varias correcciones de
   mala atribución ya se detectaron así en sesiones anteriores).
