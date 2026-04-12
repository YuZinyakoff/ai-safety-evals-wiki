# Construct Validity

## Коротко
> **Construct validity** — это вопрос о том, действительно ли benchmark measurement связан с тем capability concept, именем которого мы его называем. Не всякий “reasoning benchmark” валидно измеряет reasoning.

## Почему это важный концепт
Week-03 делает этот концепт критическим. Как только benchmark'и начинают описывать модели словами вроде `reasoning`, `fairness`, `toxicity` или `theory of mind`, возникает риск слишком сильных интерпретаций. Construct validity нужен как дисциплина против этой спешки.

## Что здесь обычно нужно
- Ясно определить construct, а не только назвать его.
- Показать, как tasks и metrics supposed to connect с этим construct.
- Проверить, как benchmark соотносится с другими theoretically related measures.
- Понять, какие interpretations и uses measurement реально поддерживает.

## Что именно здесь ломает наивный вывод
- Название benchmark'а легко принять за доказательство измерения.
- High score легко принять за сильный capability claim.
- Плохая документация benchmark'а скрывает, где construct подменен proxy.

## Практическая интуиция
Полезно спрашивать: **если я заменю слово “reasoning” на более скромное описание конкретного test behavior, останется ли claim таким же сильным?** Если нет, значит benchmark, возможно, опирается на слишком широкое construct language.

## С чем легко перепутать
- Construct validity легко спутать с statistical significance. Это разные вещи.
- Ее легко свести к documentation, хотя documentation только помогает сделать validity question явным.
- Ее легко понимать как абстрактную философию, хотя она напрямую влияет на то, какие claims допустимы в papers и eval reports.

## Где смотреть дальше
- [Nomological networks paper](../sources/construct-validity-nomological-networks.md)
- [ECBD](../sources/evidence-centered-benchmark-design-nlp.md)
- [BenchmarkCards](../sources/benchmarkcards-llm-benchmarks.md)

## Открытые вопросы
- Какие capability words вообще допустимо использовать в LLM evaluation без слишком сильных anthropomorphic leaps?
- Насколько rich должна быть theoretical network, чтобы capability claim был defensible, но не стал непрактичным?

## Связанные страницы
- [concepts/evidence-centered-benchmark-design](evidence-centered-benchmark-design.md)
- [concepts/benchmark-design](benchmark-design.md)
- [concepts/benchmark-documentation](benchmark-documentation.md)
