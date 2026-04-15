# AI Safety & Evals

Это рабочая база знаний по курсу AI Safety & Evals.
Сейчас в ней уже разобраны все пять недель курса, а `wiki/` работает как основной слой для повторения, поиска связей и накопления синтезов поверх `raw/`.
Внутренние ссылки в wiki ведутся в относительном Markdown-формате, чтобы база одинаково читалась в Obsidian, VS Code и GitHub.

## Что это за база

- `raw/` хранит исходники и организаторские рамки недели, оставаясь источником истины.
- `wiki/` хранит поддерживаемый слой знаний: недели, страницы источников, страницы концептов и синтезы.
- `AGENTS.md` задает правила и workflow, чтобы база вела себя как накопительная wiki, а не как набор случайных summary-файлов.

## Как лучше заходить в базу

- Если нужно **восстановить логику курса по порядку**, иди через [week-01](weeks/week-01.md), [week-02](weeks/week-02.md), [week-03](weeks/week-03.md), [week-04](weeks/week-04.md) и [week-05](weeks/week-05.md).
- Если нужен **быстрый проход по всей дуге курса**, начинай с [From Evals To Reliable AI Safety Evals](syntheses/course-arc-from-evals-to-reliable-safety.md).
- Если нужен **общий слой про методологию evals вне логики отдельных недель**, смотри [Eval Methodology in AI Safety](syntheses/eval-methodology-in-ai-safety.md).
- Если нужно **быстро понять, как читать course papers и зачем source pages вообще устроены так, а не иначе**, открывай [Как читать источники курса](syntheses/reading-course-sources.md).
- Если нужен **общий словарь и карта области**, открывай [Evals](concepts/evals.md).
- Если хочется быстро вернуть **главные межисточниковые выводы**, смотри [Scope, Failure Modes, And Practice Of Evals](syntheses/evals-scope-and-limits.md), [Benchmarking Beyond Single Scores](syntheses/benchmarking-beyond-single-scores.md), [Benchmark Design, Evidence, And Incentives](syntheses/benchmark-design-evidence-and-incentives.md), [Agent Evals Beyond Task Success](syntheses/agent-evals-beyond-task-success.md) и [Reliable AI Safety Evals](syntheses/reliable-ai-safety-evals.md).
- Если нужен **практический слой**, удобнее всего заходить через [Inspect AI](concepts/inspect-ai.md) и notebook source pages первых четырех недель.

## Роли верхнего слоя

- [home](home.md) — как пользоваться базой и куда идти по разным сценариям.
- [index](../index.md) — полный каталог страниц wiki с короткими описаниями.
- [log](../log.md) — журнал того, как база развивалась; новые записи добавляются в конец.

## Что уже собрано

- Все 5 недель курса уже имеют полноценные страницы-хабы.
- В `wiki/` сейчас 41 страница источников, 32 страницы концептов и 8 синтезов.
- Для ключевых arXiv-материалов там, где это было полезно, preferred raw уже выбран как clipped Markdown / HTML с `PDF` и `TeX Source` в backup-слое.
- По `week-01..04` есть и теоретический, и практический слой; `week-05` остается более методологической и завершающей.
- В `raw/shared/` теперь есть и вне-недельный слой: цикл лекций про методологию evals как отдельную AI safety задачу.

## Как использовать слои

- Страницы недель нужны, чтобы быстро восстановить картину модуля и маршрут по материалам.
- Source pages нужны, чтобы держать в памяти конкретные тексты, papers и notebooks.
- Concept pages нужны, чтобы собирать повторяющиеся идеи поперек недель.
- Syntheses нужны, чтобы фиксировать межисточниковые tension points и большие выводы, а не только summaries.

## Принцип записи

- Факты из источников должны оставаться отличимыми от wiki-level интерпретаций.
- Интерпретации нужны не как украшение, а как накопительный слой поверх нескольких текстов и недель.
- Открытые вопросы нужны, чтобы база не замыкалась в ложной завершенности.
