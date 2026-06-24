# Plantilla de repositorio reutilizable para Claude Code y Cowork (2026): investigación crítica

> Marco de evidencia: cada hallazgo se etiqueta **VERIFIED** (con doc oficial o fuente primaria), **OPINION** (criterio razonado / consenso de blogs) u **OPEN TRADE-OFF** (decisión sin respuesta única). El encargo pide escepticismo: donde una premisa tuya no se sostiene, lo digo explícitamente.

## TL;DR
- **Confirmado: el entregable principal debe ser un TEMPLATE REPO, no un plugin.** La documentación oficial de Claude Code afirma textualmente que "A CLAUDE.md file at the plugin root is not loaded as project context" — un plugin solo aporta contexto vía skills/agents/hooks, nunca vía CLAUDE.md. Un CLAUDE.md y un .claude/ a nivel de proyecto **sí** se cargan automáticamente al hacer `cd` a la carpeta. El plugin companion (repo/marketplace aparte) es válido **solo** para skills/commands/hooks transversales a todos los proyectos.
- **Matiz crítico que REFUTA una de tus premisas: Cowork NO lee automáticamente CLAUDE.md/.claude/ como Claude Code.** La documentación oficial de Cowork describe Instrucciones (GUI: global + de carpeta), Contexto añadido y Memoria por proyecto; **nunca menciona CLAUDE.md**. Por tanto el repo debe puentear las reglas a un formato que Cowork sí consuma (el campo "Instructions" o un brief que el prompt de arranque mande leer).
- **GitHub no sustituye variables**, así que el renombrado "armónico" exige un bootstrap. Para 2026 la recomendación es **copier** (re-sync con el template) o, si priorizas cero-dependencias, un **bootstrap en Python** idempotente y autodestructivo. Para "nada suelto" usar **PREVENCIÓN** (PreToolUse hook que bloquea) + un `/tidy` que **PROPONE**, nunca que mueve automáticamente.

---

## Key Findings — tabla (tema → práctica recomendada → fuente → veredicto)

| # | Tema | Práctica recomendada | Fuente | Veredicto |
|---|------|----------------------|--------|-----------|
| Premisa | Template repo vs plugin | Template repo como base; CLAUDE.md+.claude/ de proyecto se cargan solos; el de un plugin se ignora | docs Claude Code "Plugins reference" | VERIFIED |
| 1 | Template GitHub vs clone | "Use this template" copia archivos sin historial; **no** sustituye variables | GitHub community #5336/#23378, issue #1716 | VERIFIED |
| 2 | Scaffolding | copier (re-sync + `_tasks`) preferido 2026; cookiecutter no tiene update nativo (necesita cruft) | copier docs; comparativas 2025 | VERIFIED + OPEN |
| 3 | Renombrado armónico | Reemplazo consistente del placeholder en nombres/contenidos/manifiestos/README | copier Jinja2; patrón "implode" (rclayton) | OPINION |
| 4 | Bootstrap autodestructivo | Python idempotente; escribe `.bootstrapped`; se autoborra; evitar PowerShell | copier `_tasks`/`_exclude`; portabilidad | OPINION |
| 5 | Activación Claude Code | `cd` → lee CLAUDE.md + .claude/ automáticamente; **no** correr /init | docs memory; docs best-practices | VERIFIED |
| 6 | Cowork | GUI Claude Desktop → Cowork → Projects → "+" → "Use an existing folder"; **sin CLI** | support.claude.com (Cowork) | VERIFIED |
| 7 | Prompt de arranque | Orden: leer reglas primero → no inventar → marcar incertidumbre → preguntar → guardar en outputs/ | derivado | OPINION |
| 8 | Contexto previo | `context/` + `PROJECT_BRIEF.md` para Code y Cowork | derivado | OPINION |
| 9 | Nada suelto | PreToolUse hook (prevención) + `/tidy` que propone + policy.md | docs hooks | VERIFIED + OPINION |
| 10 | Higiene archivos | .editorconfig/.gitattributes/.gitignore; **Claude Code no lee AGENTS.md** | docs; SSW; gist/issue #6235 | VERIFIED |
| 11 | Secretos | .env.example + gitleaks pre-commit **y** CI | gitleaks docs | VERIFIED |
| 12 | Reproducibilidad | `uv.lock` commiteado (`--frozen` en CI); Makefile/justfile; devcontainer opcional | docs uv | VERIFIED |
| 13 | Versionado/changelog | SemVer + Conventional Commits + git-cliff regenerable | git-cliff docs | VERIFIED |
| 14 | ADRs | docs/adr/, Nygard, inmutables, supersede; vinculan con changelog | adr.github.io; Fowler | VERIFIED |
| 15 | Lint/format | ruff/black/prettier + pre-commit (+PostToolUse hook) | pre-commit; docs hooks | VERIFIED |
| 16 | CI mínimo | GitHub Actions: validar manifiestos/placeholders, tests, lint | derivado | OPINION |
| 17 | Licencia/meta | LICENSE, CONTRIBUTING, plantillas mínimas por permanencia | derivado | OPINION |
| 18 | Cross-shell | Preferir Python/bash; detectar OS; documentar portable | EOL/portabilidad best practices | OPINION |
| 19 | Testing barato | Smoke/golden + validación de manifiestos; no testear lo trivial | derivado | OPINION |
| 20 | Indexado/RAG | Empezar híbrido (denso+BM25+rerank); GraphRAG solo si multi-hop; commitear la receta, no el índice | Microsoft LazyGraphRAG; T2-RAGBench (EACL 2026) | VERIFIED + OPEN |
| 21 | Anti-deriva | "Constitución" leída primero: cite-or-IDK, verificación, devil's advocate, presupuesto de contexto | Constitutional AI; jurisprudencia 2025-26 | OPINION |

---

## Details

### A. Mecanismo de plantilla y renombrado

**1. Template repo vs clone (VERIFIED).** GitHub "Use this template" crea un repo nuevo con los archivos pero sin historial ni ramas, y sin vínculo de sync con el original. La limitación clave, confirmada en discusiones oficiales de GitHub (community #5336, #23378, issue #1716): **GitHub NO tiene ningún mecanismo de sustitución de variables/placeholders**. Cita literal: *"Unfortunately, Github does not offer any kind of mechanism for substituting placeholders with our own values (there is actually no real concept of a placeholder with Template Repositories)."* Por tanto el renombrado debe hacerlo un script post-instanciación; el botón "Use this template" solo ahorra el `git clone` + borrar `.git`.

**2. copier vs cookiecutter vs script propio (VERIFIED + OPEN TRADE-OFF).** Para 2026 la comunidad converge en **copier** por una característica que cookiecutter no tiene de forma nativa: `copier update` re-aplica el diff del template a proyectos ya generados (re-sync), comparando vía git tags y el archivo `.copier-answers.yml`. copier usa un único `copier.yml` (YAML + Jinja2), soporta `_tasks` (comandos post-generación), `_exclude` y `_migrations`. cookiecutter es más maduro y genera salida más limpia (no deja metadatos), pero el sync requiere la herramienta externa `cruft`.

Veredicto: si quieres que los proyectos hijos puedan **recibir mejoras futuras** del template → **copier**. Si priorizas **cero dependencias** (que no haga falta ni copier ni Python preinstalado) y un solo uso → **bootstrap propio**. Trade-off abierto y real: copier añade una dependencia (`uv tool install copier`) y deja `.copier-answers.yml`; el script propio es más autónomo pero más frágil y no ofrece re-sync.

**3-4. Renombrado armónico y bootstrap autodestructivo (OPINION).** Con nombre fijo (p. ej. "apolo12"), el placeholder (p. ej. `__project_name__`) debe reemplazarse coherentemente en: nombres de carpetas, nombres de archivos, contenidos, manifiestos (pyproject.toml/package.json), README **y** CLAUDE.md. copier lo hace con Jinja2 tanto en nombres como en contenidos (un nombre de archivo que renderiza a cadena vacía se omite). Para script propio, el patrón "implode" (conocido de Create React App, documentado por rclayton): el script pregunta el nombre, reemplaza, mueve archivos a su sitio, escribe el centinela `.bootstrapped`, y **borra** lo que solo sirvió para configurar (incluido él mismo y la sección "primeros pasos" del README). Sin romper rutas: hacer el reemplazo de contenidos y el rename de paths en pasos separados y validados.

**Lenguaje: Python, no PowerShell (OPINION fundamentada).** Python es multiplataforma sin cambios; PowerShell sufre fricción de ExecutionPolicy, divergencias pwsh vs Windows PowerShell y mayor coste de tokens cuando el agente lo depura. copier además ejecuta `_tasks` y puede auto-excluir su propia config con `_exclude`. **Advertencia documentada de copier** (issue #499): cuando hay prompts, los `_tasks` pueden ejecutarse antes y después de la generación — diseña el bootstrap para ser idempotente y seguro ante doble ejecución (de ahí el centinela `.bootstrapped`).

### B. Activación en Claude Code y Cowork

**5. Claude Code activa por `cd` (VERIFIED).** La doc oficial (code.claude.com/docs/en/memory) confirma que Claude Code lee CLAUDE.md al inicio de cada sesión recorriendo el árbol de directorios hacia arriba, y carga el `.claude/` (settings.json, hooks, commands, skills, rules). Jerarquía aditiva: `~/.claude/CLAUDE.md` (global) → `<proyecto>/CLAUDE.md` → CLAUDE.md de subdirectorios → `CLAUDE.local.md` (personal, gitignored), donde lo más específico gana en conflictos. El CLAUDE.md de raíz **sobrevive a la compactación** (se re-lee de disco y se re-inyecta). Punto clave para "nada suelto": la propia doc avisa de que CLAUDE.md es **contexto, no configuración aplicada** — *"To block an action regardless of what Claude decides, use a PreToolUse hook instead."*

**Sobre /init: documentar que NO se ejecute (OPINION, respaldada).** `/init` genera o actualiza un CLAUDE.md analizando el código; si ya existe, la doc indica que lo **actualiza** en vez de sobrescribirlo a ciegas. Pero como tú ya envías un CLAUDE.md curado, correr /init solo añade ruido auto-descubrible (lista de comandos, stack) que infla el presupuesto de instrucciones y "se pudre" al cambiar el código. Una fuente lo expresa sin matices: *"Never run init… the file it generates dumps irrelevant information into your global context, inflates your system prompt, wastes your instruction budget, and rots."* Recomendación: dejar nota explícita en CLAUDE.md y README de que **/init no debe ejecutarse en este repo**.

**6. Cowork (VERIFIED, con REFUTACIÓN de premisa).** Flujo real confirmado en support.claude.com: Claude Desktop → pestaña **Cowork** → **Projects** → botón **"+"** → tres opciones, siendo **"Use an existing folder"** la indicada para apuntar a la carpeta ya renombrada. Confirmado: **no hay CLI de setup** ("now accessible within Claude Desktop and *without opening the terminal*"); es GUI-only. Cowork usa cuatro capas: **Instructions** (global + de carpeta/"folder instructions"), **Context** (carpeta local / link a un proyecto de chat / URL), **Memory** por proyecto, y **Plugins**.

**REFUTACIÓN de una premisa del encargo.** La documentación oficial de Cowork **nunca menciona CLAUDE.md** y **no confirma** que Cowork lea automáticamente un CLAUDE.md/.claude/ de la carpeta como hace Claude Code. Lo documentado es: *"Folder instructions add project-specific context to Cowork when you select a local folder."* Varios blogs influyentes (Substacks de Alex Banks, Ruben Hassid, Tayla Burrell) afirman que "Cowork lee tu CLAUDE.md cada sesión", pero **esto NO está en docs oficiales y es UNVERIFIED y conflictivo**; un repo de ingeniería inversa (johnzfitch/claude-cowork-linux) sugiere que el `.claude` dentro de la VM de Cowork es de **ámbito de sesión**, no la carpeta seleccionada. **Implicación de diseño:** no confíes en que Cowork lea CLAUDE.md. El repo debe incluir (a) un archivo de reglas cuyo contenido el usuario **pegue** en el campo "Instructions" del proyecto Cowork, y/o (b) un PROJECT_BRIEF/README que el **prompt de arranque** mande leer explícitamente al inicio.

**Plugins en Cowork (VERIFIED):** son los **mismos plugins de Claude Code** (skills, connectors, slash commands, sub-agents), basados en archivos, instalados vía GUI (Customize → Plugins → Browse/Install) y guardados **localmente a nivel de máquina (global), no por proyecto**. Anthropic open-sourceó 11 "knowledge-work plugins". Dato clave verificado: *"Hooks and sub-agents run only in Cowork, so they appear grayed out in chat"* — es decir, los **hooks empaquetados dentro de un plugin sí corren en Cowork**. PERO hay reportes (issues anthropics/claude-code #45514 y #63360, este último etiquetado por Anthropic como area:cowork/area:hooks) de que los hooks escritos a mano en `~/.claude/settings.json` **NO se disparan** en Cowork. Conclusión: Cowork soporta hooks **vía plugin**, no como drop-in de settings.json.

**7. Prompt de arranque genérico (OPINION).** Un prompt único para pegar al activar (Code o Cowork), con un placeholder `[CONTEXTO ADICIONAL]`, que ordene en este orden: (1) leer **PRIMERO** los archivos de reglas/contexto (CLAUDE.md / constitution.md / PROJECT_BRIEF.md / `context/`); (2) no inventar datos; (3) declarar la incertidumbre explícitamente; (4) preguntar antes de actuar; (5) guardar salidas en `outputs/`. Este prompt es doblemente importante en Cowork porque compensa que no auto-cargue CLAUDE.md.

**8. Carpeta de intake (OPINION).** `context/` para subir material previo + `PROJECT_BRIEF.md` (plantilla a rellenar), sirviendo a Code y Cowork por igual (en Cowork se añade como "Context": carpeta local / link / URL).

### C. Política "nada suelto"

**9. Prevención vs curación (VERIFIED + OPINION).** La opción más robusta es **PREVENCIÓN** mediante un **PreToolUse hook**. La doc oficial confirma el contrato: el hook recibe JSON por stdin con `tool_name` y `tool_input.file_path`; puede devolver
```json
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"Ruta fuera de la estructura permitida"}}
```
(o salir con exit code 2) para **BLOQUEAR** la escritura. Verificado además: los hooks corren incluso con `--dangerously-skip-permissions` (el bypass salta confirmaciones interactivas, no los hooks); y un hook **nunca** anula una regla de permiso `deny`/`ask`.

La **CURACIÓN** automática (mover después) es peligrosa: rompe rutas, imports y enlaces. Recomendación: un comando `/tidy` (skill) que **PROPONE** reubicaciones y solo ejecuta tras confirmación, más una `policy.md` que el agente lee primero. Riesgo del hook de prevención: falsos positivos que frustran; mitigar con allowlist de carpetas (`src/`, `tests/`, `docs/`, `outputs/`, `context/`) y un `tmp/` efímero permitido e ignorado por git.

### D. Higiene de repo reutilizable (snowball — qué más es estándar hoy)

**10. AGENTS.md — hallazgo importante (VERIFIED).** Claude Code **NO** lee AGENTS.md; solo CLAUDE.md, sin fallback. El issue #6235 (miles de reacciones) lo pide; Anthropic no ha dado roadmap. AGENTS.md es el estándar emergente (mantenido bajo Linux Foundation; Cursor, Codex, Copilot lo leen nativo). Patrón recomendado por la propia Anthropic: poner `@AGENTS.md` en la primera línea del CLAUDE.md (import, funciona en Windows) o `ln -s AGENTS.md CLAUDE.md` (symlink; en Windows requiere Developer Mode — preferir el @import). Además: `.editorconfig` (`indent_style`, `charset=utf-8`, `end_of_line=lf`, `insert_final_newline=true`, `trim_trailing_whitespace=true`) y `.gitattributes` (`* text=auto`, `*.sh text eol=lf`, `*.bat text eol=crlf`, binarios marcados) para EOL consistente entre OS; `.gitignore`/`.dockerignore` curados; carpeta `tmp/` efímera e ignorada para operacionalizar "no commitear basura".

**11. Secretos (VERIFIED).** `.env` + `.env.example`, **gitleaks** como pre-commit (`repo: https://github.com/gitleaks/gitleaks` en `.pre-commit-config.yaml`) **y también** en CI como red de seguridad (los pre-commit se saltan con `--no-verify`, el CI no). Nunca commitear claves; si una se filtró, asumirla comprometida, **rotarla** y limpiar el historial con git-filter-repo/BFG (coordinando el re-clone del equipo).

**12. Reproducibilidad (VERIFIED).** Para Python, **uv** con `uv.lock` **commiteado** (es como package-lock.json, **no** como .venv); en CI usar `uv sync --frozen` o `--locked` para fallar si hay drift (la doc oficial avisa de que el re-lock silencioso en CI "defeats the point of a lockfile"). **Makefile/justfile** como superficie de comandos regenerable. **devcontainer**: evaluar pero **no obligatorio** — da reproducibilidad fuerte a costa de complejidad/peso; recomendable solo si el equipo ya usa contenedores.

**13. Versionado + changelog (VERIFIED).** SemVer + **Conventional Commits** + tags. Changelog regenerable con **git-cliff** (`cliff.toml`, parser de conventional commits, soporta formato "Keep a Changelog"); bump vía GitHub Actions. El changelog es un **artefacto regenerable** desde los commits — no se edita a mano.

**14. ADRs (VERIFIED).** `docs/adr/`, plantilla Nygard (Status/Context/Decision/Consequences), un archivo por decisión, numerados, **inmutables** una vez "Accepted" (cambios → nuevo ADR que "supersedes" al anterior). Relación con el changelog: el **changelog dice QUÉ cambió**; el **ADR dice POR QUÉ** — trazabilidad del razonamiento, justo lo que un agente necesita para no re-litigar decisiones. Variante ligera Y-Statement ("In the context of … we decided … to achieve … accepting …") para decisiones menores.

**15. Lint/format (VERIFIED).** ruff/black (Python) o prettier (JS) vía **pre-commit**, para que el agente no gaste tokens en estilo. Complementar con un **PostToolUse hook** (`matcher: "Edit|Write"`) que formatea tras cada edición — patrón ampliamente documentado.

**16-17. CI mínimo y meta (OPINION).** GitHub Actions que valide manifiestos (incluido un check de que **no quedan placeholders del template**, p. ej. `grep` que falla si encuentra `__project_name__`), corra tests y lint; sin sobre-ingeniería. LICENSE, CONTRIBUTING e issue/PR templates **solo los necesarios por permanencia**.

**18. Cross-shell (OPINION).** Preferir bash/Python o detectar OS (`uname` / `$OS`); documentar comandos de forma portable; minimizar PowerShell (fricción y tokens). Para el bootstrap, Python gana por portabilidad sin reescritura.

**19. Testing barato (OPINION).** Tests deterministas y baratos en tokens: smoke tests, golden tests, validación de manifiestos/JSON. **NO** testear lo trivial ni lo auto-descubrible; el objetivo es señal rápida en CI, no cobertura.

**20. Indexado/RAG con grafos (VERIFIED + OPEN TRADE-OFF).** Evaluación crítica pedida: para indexar el repo como base de conocimiento, **empezar por lo simple**. El consenso 2026 lo respalda con números concretos: en el benchmark **T2-RAGBench** (Strich et al., aceptado en EACL 2026; 23.088 consultas sobre 7.318 documentos), la recuperación **híbrida + Cohere Rerank logró +17,4% de Recall@5 relativo sobre RRF híbrido (0,816 vs 0,695) y +39,0% sobre denso solo (0,816 vs 0,587)**; el reranker cross-encoder aporta **+17,2 puntos de MRR@3 y +12,1 pp de Recall@5** sobre el híbrido sin rerank. Los autores recomiendan: *"hybrid retrieval as the minimum viable baseline for any RAG deployment."*

GraphRAG (Microsoft) solo brilla en consultas **multi-hop / síntesis global** ("¿cuáles son los temas principales?"), a coste de indexado 3-5× y de infraestructura (grafo + vector). **Microsoft LazyGraphRAG** (anunciado el **15 de noviembre de 2024**) reduce el coste de indexado a lo idéntico que vector RAG y al **0,1% del GraphRAG completo**, con calidad comparable a GraphRAG Global Search pero **más de 700× menos coste por consulta** (Microsoft Research). Para un repo individual, GraphRAG completo es casi siempre sobre-ingeniería. **Regla de oro: commitea la RECETA (el script/config que regenera el índice), no el índice** — el índice es un artefacto regenerable y voluminoso. Antes que grafo, prueba parent-child chunking. Veredicto: usa grafo **solo si demuestras con métricas** que el RAG híbrido falla en tus consultas relacionales.

**21. Anti-deriva / anti-alucinación / anti-sesgo (OPINION).** Materializar en un archivo "constitución" (`constitution.md` o sección de CLAUDE.md) que el agente lee primero, con: regla **"cita-o-di-no-lo-sé"**, pasos de verificación (chain-of-verification), checklist de sesgo, devil's advocate y presupuesto de contexto. El coste de no tener esta regla está cuantificado: la base de datos de **Damien Charlotin** (research fellow del Smart Law Hub de HEC Paris) registraba **1.348 casos judiciales con alucinaciones de IA a nivel mundial al 24 de abril de 2026** (915 en tribunales de EE. UU.), creciendo desde 87 casos (18 may 2025) a 486 (28 oct 2025); en abril de 2026 incluso **Sullivan & Cromwell** se disculpó ante el juez Martin Glenn por una moción con ~28 citas erróneas (quiebra Prince Global Holdings), y en **Whiting v. City of Athens** (Sixth Circuit, marzo 2026) se sancionó a dos abogados con **15.000 USD de multa punitiva cada uno** por más de dos docenas de citas falsas o tergiversadas. Conecta conceptualmente con Constitutional AI (Anthropic, 2022) y Chain-of-Verification. **Importante:** este archivo debe ir donde Claude Code lo carga (CLAUDE.md o `@import`) y, para Cowork, **replicarse** en las Instructions del proyecto, dado que Cowork no garantiza leer CLAUDE.md.

---

## Recommendations (escalonadas, accionables)

**Fase 0 — Decisión de arquitectura (ahora).** Construir un **template repo** como entregable principal. Razón verificada: el CLAUDE.md de proyecto se carga solo en Claude Code, y el de un plugin se ignora. Crear el **plugin companion** (repo/marketplace aparte) **solo** para skills/commands/hooks que quieras en TODOS los proyectos sin re-clonar (p. ej. `/tidy`, hook de secretos, hook de "nada suelto"). Ventaja extra: esos hooks de plugin **sí** funcionan en Cowork, mientras que los de settings.json no.

**Fase 1 — Scaffolding.** Elige **copier** si quieres re-sync futuro; **bootstrap Python autodestructivo** si quieres autonomía total. En ambos casos: placeholder único, reemplazo armónico, centinela `.bootstrapped`, auto-borrado de los archivos de configuración inicial y de la sección "primeros pasos" del README. Añade en CI un check anti-placeholder.

**Fase 2 — Doble activación.** Envía CLAUDE.md curado (+ `.claude/` con settings, hooks, skills, rules) para Claude Code, e instruye explícitamente **NO** correr /init. Para Cowork: como **no** auto-lee CLAUDE.md, incluye un `INSTRUCTIONS_COWORK.md` cuyo contenido el usuario pega en el campo Instructions, y un prompt de arranque que mande leer las reglas primero. Documenta el flujo GUI exacto (Cowork → Projects → "+" → "Use an existing folder").

**Fase 3 — Guardarraíles.** PreToolUse hook (bloquea escrituras fuera de estructura + protege `.env`), gitleaks pre-commit + CI, ruff/prettier pre-commit + PostToolUse hook, `/tidy` que propone. Constitución anti-alucinación leída primero.

**Fase 4 — Higiene permanente.** `uv.lock` commiteado, Makefile/justfile, git-cliff + Conventional Commits, ADRs en docs/adr/, CI mínimo, .editorconfig/.gitattributes.

**Umbrales que cambian la decisión (benchmarks de revisión):**
- Si necesitas que varios proyectos reciban mejoras del template → **copier obligatorio** (cookiecutter + cruft es plan B).
- Si el RAG híbrido (denso+BM25+rerank) falla **demostrablemente** en consultas multi-hop con métricas → considerar **LazyGraphRAG** antes que GraphRAG completo.
- Si Anthropic añade lectura nativa de **AGENTS.md** (issue #6235) o de **CLAUDE.md en Cowork** (vigilar docs de Cowork) → simplificar el puenteo y eliminar la duplicación.

## Caveats
- **Velocidad de cambio:** Claude Code y Cowork iteran muy rápido (se citan versiones v2.1.x de 2026). Verifica contra docs oficiales antes de implementar; cualquier comportamiento de plugin/hook/Cowork puede cambiar.
- **Premisa de Cowork parcialmente refutada:** la afirmación de que Cowork lee CLAUDE.md como Claude Code **no** está respaldada por docs oficiales; trátala como falsa hasta confirmación. Los blogs que la repiten son fuentes secundarias.
- **Hooks en Cowork:** funcionan **solo vía plugin**; los de `~/.claude/settings.json` no se disparan (reportes de usuarios con etiquetado/reconocimiento de Anthropic en los issues, no doc formal).
- **Etiquetas OPINION:** muchas "best practices" de higiene provienen de blogs de calidad pero no de fuente primaria; las marqué como OPINION. Las VERIFIED tienen doc oficial (docs.claude.com/code.claude.com, copier, uv, gitleaks, git-cliff, GitHub, Microsoft Research) o paper revisado.
- **Una contradicción de fuentes resuelta:** sobre /init, la doc oficial dice que "actualiza" un CLAUDE.md existente (no lo borra), mientras blogs dicen "nunca lo ejecutes". No es contradicción real: la doc describe el mecanismo; el consejo de no ejecutarlo es una decisión de higiene de contexto cuando ya envías un CLAUDE.md curado.