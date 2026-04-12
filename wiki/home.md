# AI Safety & Evals

Это рабочая база знаний по курсу AI Safety & Evals.
Wiki уже вышла из чисто стартового состояния: материалы `week-01`, `week-02`, `week-03`, `week-04` и `week-05` разобраны по доступным theory / notebook / extra-слоям.
Внутренние ссылки в wiki ведутся в относительном Markdown-формате, чтобы база одинаково читалась в Obsidian, VS Code и GitHub.

## Как заходить в базу

- Если нужно **восстановить логику курса по порядку**, лучше всего идти через [week-01](weeks/week-01.md), [week-02](weeks/week-02.md), [week-03](weeks/week-03.md) и [week-04](weeks/week-04.md): это сейчас основные hub-pages базы.
- Если нужен **общий словарь и карта области**, открывай [concepts/evals](concepts/evals.md).
- Если хочется быстро вернуть **главные межисточниковые выводы**, смотри [Scope, Failure Modes, And Practice Of Evals](syntheses/evals-scope-and-limits.md) и [Benchmarking Beyond Single Scores](syntheses/benchmarking-beyond-single-scores.md).
- Если нужен **вход в benchmark design, validity и LLM-as-a-judge**, удобнее всего начинать с [Benchmark Design, Evidence, And Incentives](syntheses/benchmark-design-evidence-and-incentives.md).
- Если нужен **вход в agent evaluation, reliability и elicitation**, удобнее всего начинать с [week-04](weeks/week-04.md), [agent evaluation](concepts/agent-evaluation.md) и [Agent Evals Beyond Task Success](syntheses/agent-evals-beyond-task-success.md).
- Если нужен **вход в reliable AI safety evals, science of evals и research taste**, начинай с [week-05](weeks/week-05.md), [AI Safety Benchmarks](concepts/ai-safety-benchmarks.md) и [Reliable AI Safety Evals](syntheses/reliable-ai-safety-evals.md).
- Если нужен **практический слой**, удобнее всего заходить через [Inspect AI](concepts/inspect-ai.md) и notebook source pages первых четырех недель.

## Навигация

- [weeks/week-01](weeks/week-01.md)
- [weeks/week-02](weeks/week-02.md)
- [weeks/week-03](weeks/week-03.md)
- [weeks/week-04](weeks/week-04.md)
- [weeks/week-05](weeks/week-05.md)
- [index](../index.md)
- [log](../log.md)

## Текущее покрытие

- Неделя 01 разобрана по всем текущим материалам: есть 7 source pages, 7 concept pages и 1 synthesis.
- Неделя 02 разобрана по всем текущим материалам: есть 5 source pages, 5 новых concept pages и 1 synthesis, плюс обновлены общие concept pages.
- Неделя 03 тоже разобрана по theory, notebook и extra-материалам: есть 12 source pages, 8 новых concept pages и 1 synthesis.
- Неделя 04 тоже разобрана по theory, notebook и extra-материалам: есть 11 source pages, 6 новых concept pages и 1 synthesis.
- Неделя 05 разобрана по текущим theory-материалам: есть 3 source pages, 5 новых concept pages и 1 synthesis.
- Для ключевых статей первых двух недель теперь в основном есть сильный raw-набор: clipped Markdown, а для arXiv-материалов при необходимости еще PDF и `TeX Source`.
- Для ключевых материалов week-03 raw тоже в основном выровнен: сильные clipped Markdown там, где они были доступны, и fallback sidecar только там, где лучшего локального текста не было.
- Для week-04 raw тоже в основном силен: почти везде есть clipped `.md`, а PDF и `TeX Source` остаются backup-слоем.
- Для week-05 raw тоже силен: все три theory-источника имеют локальный текст, а safety benchmark paper дополнительно сохранен как `PDF` и `TeX Source`.
- В `raw/week-01/` и `raw/week-02/` теперь покрыты theory, notebooks и extra.
- В `raw/week-03/` теперь тоже покрыты theory, notebook и extra, включая отдельную organizer note.
- В `raw/week-04/` теперь тоже покрыты theory, notebook и extra, включая отдельную organizer note.
- В `raw/week-05/` тоже покрыты theory и organizer framing.
- Разделы `wiki/sources/`, `wiki/concepts/` и `wiki/syntheses/` больше не пусты.

## Логика каркаса

- Страницы недель остаются основной осью курса и точкой входа по хронологии.
- Когда в `raw/` появляются конкретные тексты и ноутбуки, они сначала получают source pages.
- Повторяющиеся темы AI safety и evals затем выносятся в concept pages.
- Межисточниковые сравнения и сводки появляются в synthesis pages только когда для этого уже достаточно материала.

## Как пополнять базу

- Новый материал сначала фиксируется в `wiki/sources/`.
- Затем его место и краткий смысл отражаются на странице соответствующей недели.
- Повторяющиеся идеи выносятся в `wiki/concepts/`, а межисточниковые сводки в `wiki/syntheses/`.

## Как использовать базу

- чтобы вспомнить, что было на конкретной неделе — открывать страницу недели
- чтобы быстро понять отдельный текст или ноутбук — открывать соответствующую source page
- чтобы увидеть большую тему поперек нескольких источников — открывать concept page
- чтобы получить сводку или сравнение — открывать synthesis page
- чтобы перейти к полному исходному тексту — идти из source page по ссылке на raw

## Принцип записи

- Факты из источников: что прямо следует из конкретных материалов.
- Интерпретации: рабочие выводы, сравнения и обобщения поверх источников.
- Открытые вопросы: что осталось неясным и требует проверки позже.
