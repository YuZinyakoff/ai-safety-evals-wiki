# SWE-Bench: Can Language Models Resolve Real-World GitHub Issues?

- **Тип источника:** extra
- **Неделя:** week-04
- **Raw:** [clipped `.md`](<../../raw/week-04/extra/SWE-bench Can Language Models Resolve Real-World GitHub Issues.md>), [PDF](<../../raw/week-04/extra/2310.06770v3.pdf>), [TeX source](<../../raw/week-04/extra/arXiv-2310.06770v3.tar.gz>)
- **Оригинал:** [arXiv](https://arxiv.org/abs/2310.06770)
- **Полнота raw:** сильный raw-набор: clipped Markdown, PDF и TeX source

## Ключевая мысль
> **SWE-bench делает agent evaluation реалистичнее, потому что заставляет модель работать с реальным codebase, issue text и execution-based verification.** Но именно из-за этого benchmark быстро упирается в retrieval, environment setup и evaluation harness quality.

## Зачем источник в базе
Это канонический benchmark source page для coding agents. Он нужен как опорный пример agentic benchmark, где важны не только answer correctness, но и repository context, patch generation и execution against tests.

## Эпистемический статус и как на него смотреть
Это benchmark-introduction paper for repository-scale coding tasks, а не neutral measure of “coding intelligence”. Его полезно читать как paper about a specific task setup: issue text, repo context, patch generation and execution harness all shape the result.

## На какие вопросы источник помогает отвечать
- Что именно SWE-bench просит сделать модель или агент?
- Почему execution-based verification здесь сильнее simple string matching?
- Как retrieval, context localization and environment setup становятся частью difficulty?
- Почему repository-scale coding benchmarks особенно чувствительны к harness quality?

## Краткое содержание
Статья вводит `SWE-bench` как benchmark из реальных GitHub issues и merged pull requests по 12 Python repositories. Сначала авторы объясняют, как собирают instances: issue text связывается с PR, тестами и repository snapshot. Затем paper формулирует task: агент получает issue description и codebase, генерирует patch, а итог оценивается execution-based через `FAIL_TO_PASS` и `PASS_TO_PASS` tests. Дальше работа показывает, что benchmark реалистичен, но сложен: нужен retrieval of relevant files, длинный context и способность менять несколько мест в большом репозитории. Empirical часть важна исторически: ранние модели решали лишь малую долю задач, даже при oracle retrieval. Для week-04 текст полезен как пример сильного agent benchmark с большим epistemic и engineering overhead.

## Как читать источник быстро
- Если нужно определение задачи, читай dataset construction и benchmark protocol around issues, repos and tests.
- Если важен evaluation layer, концентрируйся на execution-based verification with `FAIL_TO_PASS` and `PASS_TO_PASS`.
- Если нужен reading с упором на ограничения, смотри discussion around retrieval difficulty, long context и harness overhead.

## Что источник утверждает прямо
- `SWE-bench` формулирует repository-scale coding task на основе реальных GitHub issues, pull requests, repository snapshots and tests.
- Execution-based verification через `FAIL_TO_PASS` and `PASS_TO_PASS` делает evaluation сильнее simple string matching.
- Реальная сложность benchmark'а частично живет в retrieval, context localization, environment setup и harness quality.
- Итоговый score здесь характеризует не “чистую coding intelligence”, а связку model, procedure and repository interaction.

## Что здесь особенно важно
- **Execution-based verification** здесь сильнее простого exact match.
- **Retrieval and context localization** становятся частью actual difficulty.
- **Agent benchmark** измеряет связку model + procedure, а не "чистую" coding ability.

## Интерпретация для курса
Для курса SWE-bench важен как наглядный пример того, что agent benchmark cannot be separated from harness and setup. Это делает его удобным bridge к разговору про elicitation, scaffolding and benchmark artifacts: низкий score здесь легко может означать very different things.

## Что это добавляет к теме недели
SWE-bench показывает, что agent evaluation в реальном software engineering setting почти сразу упирается в setup quality и benchmark construction. Это создает хороший мост к тексту про SWE-bench Verified.

## Что стоит запомнить при повторении
- **Repository-scale tasks** отличаются от обычного code generation.
- **Benchmark difficulty** может исходить и от task itself, и от evaluation setup.
- **Retrieval mistakes** легко превращаются в apparent capability limits.

## Связанные концепты
- [concepts/agent-evaluation](../concepts/agent-evaluation.md)
- [concepts/agent-scaffolding](../concepts/agent-scaffolding.md)
- [concepts/capability-elicitation](../concepts/capability-elicitation.md)

## Что осталось неясным / спорным
- Насколько SWE-bench действительно representative для broader software agent autonomy?
- Где именно проходит граница между benchmark challenge и benchmark artifact?

## Связанные страницы
- [weeks/week-04](../weeks/week-04.md)
- [sources/swe-bench-verified](swe-bench-verified.md)
- [sources/measuring-ai-agent-autonomy-practice](measuring-ai-agent-autonomy-practice.md)
