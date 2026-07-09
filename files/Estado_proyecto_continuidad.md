# Estado del proyecto — Resumen para continuar en nuevo chat

**Instrucciones de uso:** pega este documento completo como primer mensaje en el chat nuevo, junto con: (1) tu notebook `.ipynb` actualizado, (2) el archivo `Notas_metodologicas_articulo.md`. Con eso, Claude puede retomar exactamente donde íbamos.

---

## Qué es este proyecto

Artículo científico basado en el Capítulo 5 de mi tesis doctoral (valorización energética de biomasa residual de palma de aceite, 6 plantas extractoras del Magdalena, Colombia). Comparo 3 configuraciones: **Línea base**, **Escenario 1** (turbina extracción-condensación) y **Escenario 2** (turbina contrapresión + biogás mejorado), usando un modelo de optimización en **Python/Pyomo** — también es mi proyecto de aprendizaje de modelado energético para fortalecer mi CV.

## Repositorio y archivos

- **GitHub:** `https://github.com/juncal0/valorizacion-biomasa-palma`
- **Notebook principal:** `01_limpieza_datos_capex_emisiones_social.ipynb` (organizado en 11 secciones numeradas con Markdown)
- **Datos crudos:** `Escenarios.xlsx` (NO está en GitHub por confidencialidad de cotizaciones — solo local)
- **Notas metodológicas completas:** `Notas_metodologicas_articulo.md` (documento vivo con TODAS las decisiones, discrepancias resueltas y fuentes citadas)

## Flujo de trabajo establecido (importante que Claude lo respete)

1. Cada vez que se agrega código nuevo, indicar en qué sección del notebook va.
2. Cada hallazgo/decisión metodológica se documenta en `Notas_metodologicas_articulo.md`.
3. Respaldo en Git después de cada avance: `git add .` → `git commit -m "..."` → `git push` (recordar siempre `cd "/c/Users/Legion 5/tesis-articulo"` primero).
4. Cuando algo del Excel es sospechoso (fórmula rota, error de unidad, dato huérfano), se **valida antes de usar** — no se asume.
5. Estoy aprendiendo Python/Jupyter desde cero — explicar pasos con calma, recordar imports necesarios al inicio de cada bloque de código.

## YA RESUELTO (no volver a preguntar)

- **Datos limpios:** Datos_Base, Biomass, CAPEX, EmisionesCO2, módulo social (Hoja2), Eficiencia (balance + demanda por etapa + caldera línea base).
- **Alcance del modelo:** Fase 1 = validación con capacidad fija (sin optimizar); Fase 2 futura = superestructura con variables de decisión. Empezamos con prueba de concepto en Planta A antes de escalar a las 6 plantas.
- **Restricción activa:** disponibilidad de biomasa (no se puede calcular más energía de la disponible).
- **Función objetivo (Fase 2):** maximizar excedente eléctrico. Sostenibilidad (LCOE, emisiones, social) se evalúa como análisis posterior (multicriterio/Pareto), no dentro de la función objetivo.
- **Escenario 1 (extracción-condensación):** toda la biomasa sólida (fibra+cuesco+EFB) a combustión → caldera 48 bar/470°C (Tabla 6 tesis) → turbina extrae vapor a 5 bar/159°C para proceso (esterilización continua + resto), remanente a condensación (0.22 bar/62°C) → biogás solo con POME.
- **Escenario 2 (contrapresión):** solo fibra+cuesco a combustión (EFB se retira, va a biogás) → turbina contrapresión, vapor de escape = suministro térmico del proceso → biogás con POME + EFB pretratado térmicamente (steam explosion, aumenta biodegradabilidad).
- **Esterilización continua** reemplaza convencional en ambos escenarios (315 kg vapor/tRFF, confirmado — no 542 como decía inicialmente la Tabla 10 por error de redacción).
- **Clarificación dinámica** también reemplaza la convencional (Tabla 10: 0.6 kg vapor/tRFF, 15 kWh/tRFF, 90 L agua/tRFF).
- **Pretratamiento mecánico de EFB** (tambor rotatorio, Tabla 11, Ocampo Batlle et al. 2020) es DISTINTO del **pretratamiento térmico** (steam explosion, Escenario 2) — no confundir, tienen costos y funciones distintas.
- **BMP de EFB pretratado = 273.51 L CH4/kg SV**, validado 100% exacto con la ecuación de Thomsen et al. (2014) — clave: x_R = 1-(xC+xH+xL) = 0.21, NO es directamente la ceniza (5.7%).
- **CEPCI 2026 ≈ 873.8** (estimado, año en curso) para ajustar todos los costos a USD 2026.
- **Eficiencia de caldera** se calcula con método directo ASME (Ecuación de la tesis) + librería `iapws` (IAPWS-IF97) para entalpías — ya validado contra Planta A línea base (75.7%, dentro del rango tesis 54-76%).

## PENDIENTE / próximo paso inmediato

- Determinar el flujo de material inerte/digestato que sale del reactor de biogás (tengo un artículo de referencia para revisar).
- **Ensamblar el modelo Pyomo completo de Planta A** (línea base primero, luego Escenario 1, luego Escenario 2) usando todas las funciones/parámetros ya validados:
  - `entalpia_vapor()`, `entalpia_agua_alimentacion()`, `eficiencia_caldera_ASME()` (con iapws)
  - `PARAM_CALDERA_ESC1`, `PARAM_TURBINA_EXTRACCION_CONDENSACION` (Tabla 6)
  - `PARAM_ESTERILIZACION_CONTINUA`, `PARAM_CLARIFICACION_DINAMICA` (Tabla 10)
  - `PARAM_PRETRATAMIENTO_MECANICO_EFB` (Tabla 11)
  - `PARAM_DIGESTION_ANAEROBICA`, `DQO_ENTRADA_mg_L`, `bmp_efb()` (Tabla 13 + Thomsen et al.)
  - Funciones de emisiones (`emisiones_diesel`, `emisiones_red_nacional`, `balance_neto_GEI`, etc.)
  - Funciones de impacto social (`viviendas_rurales_beneficiadas`, `personas_rurales_beneficiadas`)
- Después de Planta A: escalar a las 6 plantas.
- Más adelante: figuras de balance de masa/energía (usando el módulo de diagramas de Claude), análisis multicriterio de sostenibilidad, redacción del artículo.

## Plan de trabajo y cronograma de 6 meses

Ya existe un documento separado (`Plan_de_trabajo_Articulo_Capitulo5.md`) con el cronograma completo mes a mes — adjuntarlo también si se necesita retomar el plan general (aprendizaje Python/Pyomo + avance del artículo en paralelo).
