# Create Masterprompt — versión en español

> Traducción de `SKILL.md`. **El programa lee exclusivamente `SKILL.md`**, el
> archivo en inglés — esta versión es para que la lean personas. Si las dos se
> contradicen, vale la inglesa. Estado: versión 1.7.0.
>
> Los nombres de archivo, las carpetas y los comandos de ejemplo están sin
> traducir a propósito, porque así se llaman en el disco.
>
> Una página para verlo de un vistazo en lugar de leerlo entero: [`docs/uebersicht-es.png`](docs/uebersicht-es.png)
> (versión en inglés: [`docs/uebersicht-en.png`](docs/uebersicht-en.png)).
>
> **Estado: publicación temprana.** El texto se ha revisado varias veces en
> busca de contradicciones internas y de conformidad con la especificación,
> pero el skill en sí todavía no ha corrido en muchos proyectos reales y
> distintos. Si algo del flujo, del filtro de tamaño o de una plantilla no
> encaja con tu propia forma de trabajar, eso es una señal útil — repórtalo
> como issue.

Un prompt maestro **no** es un prompt de rol. «Eres un ingeniero sénior, sé
minucioso» no añade nada que un modelo capaz no haga ya. Un prompt maestro es
un **paquete de contexto**: los hechos, decisiones y límites duraderos de un
proyecto, escritos de modo que una sesión sin ningún historial pueda retomar
exactamente donde la anterior se detuvo.

Este skill construye ese paquete en seis fases y devuelve tres archivos.

## Lo que produces

| Archivo | Para qué | Vive durante |
|---|---|---|
| `BRIEFING.md` | El prompt maestro. Contexto, decisiones, anti-alcance, escollos, estado actual. | Todo el proyecto |
| `DECISIONS.md` | Una línea por cuestión zanjada, con el motivo. Solo se añade, nunca se sobrescribe. | Todo el proyecto |
| `HANDOFF_vNN.md` | Escrito antes de un límite de contexto. Lo que una sesión nueva necesita *ahora mismo*. | Una sesión |

Nómbralos en el idioma del usuario. Guárdalos junto al trabajo, no en el chat.

## Fase 0 — Filtro de tamaño (esto primero, en diez segundos)

Aplicar seis fases a un script de renombrado es la forma en que la gente
aprende a saltarse el proceso por completo. Clasifica antes de empezar:

- **S — una sentada, reversible, sin incógnitas.** Pasa directamente a hacer
  el trabajo. Ofrece el recorrido completo solo si crece.
- **M — unas pocas sesiones, algunas incógnitas, una o dos bifurcaciones
  reales.** Fases 1–3 y 5, más la 6 en cuanto el trabajo sobreviva a una
  sesión. Archivo de briefing, pero corto. Sin documento de plan aparte.
- **L — varias sesiones, arquitectura real, decisiones caras de deshacer.**
  Las seis fases.

Di qué tamaño elegiste y por qué, en una frase. Si el usuario no está de
acuerdo, lo dirá — eso cuesta un mensaje y ahorra una hora.

## Fase 1 — Investigación

Averigua qué existe ya, dónde está el hueco, qué es técnicamente viable y qué
escollos están ya documentados. **La investigación ocurre solo aquí.**
Investigar a mitad de la construcción es la forma en que una construcción se
convierte en un pozo sin fondo.

Entregable: un informe con una tabla comparativa, una recomendación y fuentes.

**Para cuando se cumplan las tres** — no cuando se te acabe la curiosidad:
1. La tabla comparativa no tiene celdas vacías para las opciones
   preseleccionadas.
2. Cada línea de escollo tiene una fuente o está marcada como suposición.
3. Las dos últimas búsquedas no han dado nada nuevo. Eso es saturación.

Si no llegas a la saturación, dilo y nombra lo que quedó abierto. Un hueco
honesto vale más que una conjetura segura de sí misma, y el usuario puede
decidir si invierte más tiempo.

## Fase 2 — Briefing

Condensa la investigación en `BRIEFING.md` usando `assets/template-briefing.md`.

La prueba para este archivo: **dáselo a una sesión nueva sin historial. ¿Puede
trabajar con él?** Si necesita una sola pregunta aclaratoria sobre algo que tú
ya sabías, el briefing está incompleto. Reléelo con ojos de adversario antes
de mostrarlo.

Secciones obligatorias — las dos primeras son las que la gente se salta y
luego lamenta:

- **Anti-alcance.** No-objetivos explícitos, cada uno con su motivo. «Sin
  cifrado en la v1 — la bóveda es solo local, y la gestión de claves duplicaría
  la construcción.» El anti-alcance es la defensa más fuerte disponible contra
  la expansión progresiva del alcance, porque convierte cada «¿y si
  simplemente…?» en una decisión que hay que reabrir, en lugar de un añadido
  gratis.
- **Registro de suposiciones.** Todo lo que decidiste sin preguntar. Una línea
  por cada una, marcada para que se pueda cuestionar después. Las suposiciones
  sin registrar son invisibles hasta que salen caras.
- Contexto, restricciones, escollos conocidos, estado actual.

## Fase 3 — Entrevista de decisiones

Plantea las decisiones abiertas **de una en una**, esperando la respuesta
antes de pasar a la siguiente. Las preguntas en bloque se leen por encima, y
una decisión leída por encima es una conjetura con la firma del usuario.

Por pregunta: 2–4 opciones, una recomendación clara y su motivo. Resuelve las
dependencias en orden — decide el stack antes que la biblioteca que corre
sobre él.

**Búscalo tú mismo.** Si un dato se puede averiguar a partir de archivos,
herramientas o la web, averígualo. Al usuario le pertenecen solo las
elecciones genuinas.

**No construyas nada antes de que cierre esta fase.** Si el usuario dice
«empieza ya» a mitad de la entrevista: nombra las decisiones concretas que
siguen abiertas, ofrécete a tomarlas tú como suposiciones registradas, y
continúa solo después de que elija. Empezar con bifurcaciones abiertas
significa retrabajo, y el retrabajo cuesta más de lo que costó la entrevista.

Cierra con un resumen numerado de todas las decisiones. Añádelo al registro
de decisiones, que sigue `assets/template-decisions.md`.

## Fase 4 — Plan

Arquitectura, estructura del repo o de carpetas, archivo de convenciones,
estrategia de pruebas, hitos, definición de terminado por hito y una
definición de terminado para el proyecto en su conjunto.

Los hitos son **cortes verticales**: cada uno produce algo que el usuario puede
realmente ejecutar, ver o usar. Cinco hitos que entregan cada uno una porción
funcional valen más que tres que entregan una base que nadie puede probar.

Muestra el plan para su aprobación antes de construir.

## Fase 5 — Construcción

Trabaja contra un objetivo explícito con una **condición de parada
comprobable**. «Hecho cuando `npm test` pasa y la app abre la carpeta de la
bóveda» es comprobable. «Hecho cuando funciona bien» no lo es.

- Prueba antes que funcionalidad, donde una prueba tenga sentido.
- Commits pequeños, cada uno reversible por sí solo.
- Linting como hook, no como recordatorio.
- Sin pausas para pedir permiso. Pregunta solo en bifurcaciones de diseño
  genuinas.

## Fase 6 — Handoff

Antes del límite de contexto — no después — escribe el archivo de handoff
(`HANDOFF_vNN.md`, nombrado en el idioma del usuario) a partir de
`assets/template-handoff.md`, y luego empieza una sesión nueva. La
compactación sin fin pierde precisamente los detalles que fue caro
establecer.

Disparadores: tramos largos con uso intensivo de herramientas, relecturas
repetidas de los mismos archivos, o que el usuario pida dos veces algo ya
cubierto.

## Pasada de mejora

En cada frontera entre fases, **antes** de mostrar el resultado, cambia en
silencio de escritor a revisor. Tres preguntas:

1. **¿Qué falta?** ¿Qué pregunta tendría que hacer una sesión nueva que este
   archivo no responde?
2. **¿Qué está afirmado en lugar de demostrado?** Toda afirmación sin fuente
   ni marca de suposición es candidata.
3. **¿Qué es relleno?** Cualquier frase que podría aparecer en cualquier otro
   proyecto se va.

El usuario ve el resultado revisado, no la crítica. Excepción: si la pasada
saca a la luz algo que toca una decisión, eso tiene que ponerse delante de él.

Producir y evaluar son actividades distintas. El escritor no puede ver el
hueco porque la pieza que falta está en su cabeza. Cuesta aproximadamente el
30 % de la fase y rinde más que cualquier otra cosa en este skill.

Cuando la forma de la tarea va más allá de «escríbeme X», carga primero
`references/prompt-techniques.md` — contiene la tabla de correspondencia
entre forma de tarea y técnica, y las señales de alarma del sobre-prompting.

## Regla de rebobinado

Las decisiones se revisan. Eso es normal y barato **si se maneja bien**:

1. Actualiza el registro de decisiones — añade la línea nueva, marca la
   antigua como sustituida, conserva ambas. El historial explica por qué el
   código tiene el aspecto que tiene.
2. Actualiza `BRIEFING.md`, porque eso es lo que lee una sesión nueva.
3. Nombra lo que el cambio invalida antes de tocar código.

Cambiar de rumbo solo en el chat es el modo de fallo: los archivos siguen
describiendo el proyecto antiguo, la siguiente sesión se los cree, y la
contradicción aflora tres pasos después.

## Regla de salida

Un proyecto que no ha producido nada en tres sesiones está atascado o muerto.
Dilo sin rodeos y ofrece tres opciones: reducir el alcance, aparcarlo con un
handoff escrito para que pueda retomarse limpiamente, o abandonarlo. Las
ideas son baratas; los proyectos a medio construir tienen mantenimiento. Este
es el único sitio donde ser directo es el servicio.

## Gotchas

Hechos del entorno que desafían cualquier suposición razonable. Compruébalos
antes de sortear un síntoma.

- **El frontmatter de skills de Anthropic acepta exactamente seis claves**:
  `name`, `description`, `license`, `allowed-tools`, `metadata`,
  `compatibility`. Cualquier otra falla la validación al subir a claude.ai,
  aunque Claude Code la tolere. Los skills funcionan localmente sin quejarse y
  se rompen al subirlos.
- **El nombre de la carpeta debe ser igual al campo `name`** tras la
  normalización NFKC. Renombrar la carpeta sin tocar el frontmatter es la
  rotura más común.
- **`name`: solo minúsculas, dígitos y guiones.** Sin guiones bajos, sin
  guiones consecutivos, sin guion al principio ni al final. Máximo 64
  caracteres. `description` máximo 1024.
- **Dos puntos sin entrecomillar en `description` rompen el parseo del YAML.**
  «Use when: …» falla. Entrecomíllalo o usa un escalar de bloque (`>-`).
- **Al inicio de la sesión solo se cargan `name` y `description`.** El cuerpo
  se carga al dispararse. Por eso toda pista de «cuándo usar esto» va en la
  descripción; una condición de disparo enterrada en el cuerpo nunca se lee a
  tiempo para disparar.
- **Las peticiones simples de un solo paso no disparan skills**, por buena que
  sea la descripción, porque el modelo las resuelve directamente. Prueba el
  disparo con peticiones sustanciosas, de varios pasos.
- **Los skills son instrucciones, no un mecanismo de control.** `allowed-tools`
  exime de las solicitudes de permiso; no restringe nada.

## Archivos de referencia

Cárgalos cuando la fase lo pida, no de antemano:

- `references/profile-questionnaire.md` — las casillas que un usuario rellena
  una vez para hacer suyo este skill. Léelo en el primer uso, o cuando el
  usuario quiera una variante personal.
- `references/quality-gates.md` — la lista de comprobación por fase. Léelo
  antes de cerrar cualquier fase.
- `references/anti-patterns.md` — modos de fallo con sus remedios. Léelo
  cuando un proyecto se estanca, da vueltas en círculo o genera retrabajo.
- `references/model-routing.md` — qué clase de modelo encaja con qué fase.
  Léelo cuando al usuario le importe la elección de modelo o el coste.
- `references/prompt-techniques.md` — correspondencia entre forma de tarea y
  técnica, más señales de alarma del sobre-prompting. Léelo cuando una fase
  no entrega, un artefacto parece flojo o la tarea va más allá de «escríbeme
  X».

Las plantillas de `assets/` están pensadas para copiarse y rellenarse, no
para parafrasearse. Las estructuras se reproducen con más fiabilidad que las
descripciones en prosa de esas estructuras.

## Reglas de la casa

Estas moldean cada respuesta mientras el skill está activo:

- **Responde en el idioma del usuario**, incluidos los archivos generados.
  Este skill está escrito en inglés; su salida no.
- **Un bocado de aprendizaje por respuesta.** De dos a cuatro frases sobre el
  *porqué*, no sobre el qué. La idea es que el usuario pueda llevar el
  siguiente proyecto sin ti.
- **Calidad antes que ahorro al elegir modelo.** Nunca bajes a un modelo más
  barato cuando el más capaz da un mejor resultado. Más barato solo es
  correcto cuando el resultado es equivalente. En caso de duda, quédate arriba
  y dilo.
- **Nunca adivines donde un error sale caro.** Una errata en una respuesta no
  cuesta nada. Una errata en un nombre de archivo, un identificador, un
  formato de datos o un commit cuesta una tarde. Corrige en silencio donde la
  versión correcta es obvia; pregunta donde no lo es.
- **Abreviaturas poco claras: pregunta, no adivines.** Nombra la expansión
  habitual si existe. Una conjetura errónea aquí se agrava — tres pasos
  después soporta carga y es cara de deshacer.
- **Di las suposiciones en voz alta.** Si no estás seguro de que tu suposición
  se sostenga, dilo en lugar de venderla como un hecho.
- **Sin preguntas colgantes cuando una tarea está terminada.** Nada de «¿algo
  más?», ningún menú de opciones al cierre. Si el usuario quiere más, lo dirá.
