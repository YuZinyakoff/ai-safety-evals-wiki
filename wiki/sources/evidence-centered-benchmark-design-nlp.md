# ECBD: Evidence-Centered Benchmark Design For NLP

- **Тип источника:** theory
- **Неделя:** week-03
- **Raw:** [clipped `.md`](<../../raw/week-03/theory/ECBD Evidence-Centered Benchmark Design for NLP.md>), [PDF](<../../raw/week-03/theory/2406.08723v1.pdf>), [TeX source](<../../raw/week-03/theory/arXiv-2406.08723v1.tar.gz>)
- **Оригинал:** [arXiv HTML](https://arxiv.org/html/2406.08723v1)
- **Полнота raw:** сильный raw-набор: clipped Markdown, PDF и TeX source

## Ключевая мысль
> **Benchmark полезен только тогда, когда можно объяснить, почему его задачи, метрики и правила агрегации вообще собирают нужное evidence о целевой способности.**

## Зачем источник в базе
Это самый строгий текст недели про benchmark design. Он нужен, чтобы перевести разговор из режима “у benchmark есть dataset и metric” в режим “какую цепочку evidence этот benchmark реально строит и где она может ломаться”.

## Эпистемический статус и как на него смотреть
Это не settled standard для всего поля, а framework paper, который переносит `evidence-centered design` из educational measurement в NLP benchmarking. Его лучше читать как попытку резко поднять стандарт аргументации о benchmark validity, а не как доказательство, что без полной ECBD-формализации benchmark бесполезен.

## На какие вопросы источник помогает отвечать
- Что именно должно быть обосновано, чтобы benchmark можно было считать содержательно валидным?
- Как связаны `capability`, `content`, `adaptation`, `assembly` и `evidence`?
- В каком месте benchmark design чаще всего ломает цепочку вывода от score к capability claim?
- Как критиковать benchmark не только по dataset quality, но и по общей justificatory logic?

## Краткое содержание
Paper переносит логику `evidence-centered design` из educational testing в benchmark design для NLP. Сначала авторы объясняют, почему у поля нет систематического способа анализировать design decisions benchmark'а и их влияние на validity. Затем они вводят ECBD как рамку из пяти модулей: `capability`, `content`, `adaptation`, `assembly` и `evidence`. После формализации paper предлагает guiding questions и worksheet, который можно использовать как при создании нового benchmark'а, так и при критике уже существующего. В заключительной части авторы применяют эту рамку к BoolQ, SuperGLUE и HELM и показывают повторяющиеся проблемы: слабое определение capability, недостаточную аргументацию выбора данных, слабое описание assembly decisions и привычку оправдывать метрики тем, что они “стандартные”, а не тем, что они действительно извлекают нужное evidence.

## Структура материала
- `Abstract` и `1 Introduction`: зачем benchmark design переводить в evidence-centered language.
- `2 Background & Related Work`: benchmarking critiques, measurement theory и связь с `Evidence-Centered Design`.
- `3 Evidence-Centered Benchmark Design`: пять модулей `intended use`, `capability`, `content`, `adaptation`, `assembly`, `evidence`.
- `4 Case Studies`: применение рамки к существующим benchmark cases.
- `5 Conclusion`, `Limitations` и `Appendix A Worksheet Template`: общий вывод, limits и рабочий worksheet.

## Как читать источник быстро
- Если нужен общий frame, хватит `Abstract`, `1 Introduction`, `3 Evidence-Centered Benchmark Design` и `5 Conclusion`.
- Если вопрос про саму рамку, концентрируйся на `3.1–3.5`: именно там задаются модули.
- Если нужен practical reading, переходи к `4 Case Studies`, а затем к `Appendix A Worksheet Template`.
- Если важно понять limits paper, не пропускай `Limitations`.

## Что здесь особенно важно
- **Capability** нужно не просто назвать, а определить и привязать к intended use.
- **Content** должен быть обоснован как источник нужного evidence, а не просто удобный пул задач.
- **Adaptation** может сама искажать измерение, если одни объекты оценки ставятся в неравные условия.
- **Assembly** влияет на то, хватает ли benchmark вообще данных для claims о capability.
- **Evidence** требует оправдать и extraction, и aggregation, а не только сослаться на prior work.

## Что это добавляет к теме недели
ECBD делает benchmark design заметно строже, чем HELM. Если HELM говорит “нам нужна широкая и прозрачная картина”, то ECBD спрашивает: “почему вы уверены, что ваша конкретная конструкция вообще измеряет то, что заявляет?”. Это один из лучших текстов недели, если нужно поднять планку аргументации о validity benchmark'ов.

## Что стоит запомнить при повторении
- **Benchmark design — это не список технических choices, а цепочка justificatory choices.**
- **Даже очень известные benchmarks часто плохо оправдывают собственные claims.**
- **Worksheet mindset полезен и для критики существующих benchmark'ов, и для проектирования новых.**

## Связанные концепты
- [concepts/evidence-centered-benchmark-design](../concepts/evidence-centered-benchmark-design.md)
- [concepts/benchmark-design](../concepts/benchmark-design.md)
- [concepts/construct-validity](../concepts/construct-validity.md)
- [concepts/benchmark-documentation](../concepts/benchmark-documentation.md)

## Что осталось неясным / спорным
- Насколько practically feasible полная ECBD-дисциплина для быстро меняющегося LLM field?
- Где проходит граница между полезной строгостью и слишком тяжелой бюрократизацией benchmark design?

## Связанные страницы
- [weeks/week-03](../weeks/week-03.md)
- [sources/holistic-evaluation-language-models](holistic-evaluation-language-models.md)
- [sources/benchmarkcards-llm-benchmarks](benchmarkcards-llm-benchmarks.md)
- [syntheses/benchmark-design-evidence-and-incentives](../syntheses/benchmark-design-evidence-and-incentives.md)
- [syntheses/reading-course-sources](../syntheses/reading-course-sources.md)
