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

## Краткое содержание
Статья вводит `SWE-bench` как benchmark из реальных GitHub issues и merged pull requests по 12 Python repositories. Сначала авторы объясняют, как собирают instances: issue text связывается с PR, тестами и repository snapshot. Затем paper формулирует task: агент получает issue description и codebase, генерирует patch, а итог оценивается execution-based через `FAIL_TO_PASS` и `PASS_TO_PASS` tests. Дальше работа показывает, что benchmark реалистичен, но сложен: нужен retrieval of relevant files, длинный context и способность менять несколько мест в большом репозитории. Empirical часть важна исторически: ранние модели решали лишь малую долю задач, даже при oracle retrieval. Для week-04 текст полезен как пример сильного agent benchmark с большим epistemic и engineering overhead.

## Что здесь особенно важно
- **Execution-based verification** здесь сильнее простого exact match.
- **Retrieval and context localization** становятся частью actual difficulty.
- **Agent benchmark** измеряет связку model + procedure, а не "чистую" coding ability.

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
