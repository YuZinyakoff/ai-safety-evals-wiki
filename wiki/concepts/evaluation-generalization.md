# Evaluation Generalization

## Что это такое
Evaluation generalization в этой wiki означает проблему соответствия между bounded evaluation pipeline и все менее bounded model capacity. Проще говоря, это вопрос о том, насколько результаты на ограниченном наборе test settings действительно переносятся на более широкий класс задач, поведений и future capabilities.

## Почему это важно на второй неделе
Week-02 поднимает этот вопрос в явной форме. После первой недели уже понятно, что behavior-based evidence ограничено; вторая неделя добавляет более конкретный механизм: даже очень аккуратный benchmark suite может не успевать за ростом моделей и потому слабо generalize.

## Что видно по источникам
- [sources/cao-generalizable-evaluation-llm-era](../sources/cao-generalizable-evaluation-llm-era.md) делает эту проблему центральной для survey beyond benchmarks.
- [sources/cao-generalizable-evaluation-llm-era](../sources/cao-generalizable-evaluation-llm-era.md) связывает ее с contamination, static benchmarks и bounded evaluation practice.
- [sources/cset-ai-safety-evaluations-explainer](../sources/cset-ai-safety-evaluations-explainer.md) напоминает, что многие metrics являются proxy measurements, а значит уже по конструкции не исчерпывают risk.
- [sources/awesome-llm-eval](../sources/awesome-llm-eval.md) полезен как напоминание, что даже очень широкий catalog benchmarks не решает вопрос external validity.

## Как этим пользоваться при повторении
- Эта страница полезна как antidote к интуиции `чем больше benchmark list, тем надежнее оценка`.
- Если evaluation suite выглядит внушительно, все равно стоит спрашивать: что именно осталось вне coverage, каков риск contamination и какие tasks модели могут обобщать за пределы теста.
- Dynamic benchmarks и time-aware protocols здесь выглядят не как модный апгрейд, а как попытка частично закрыть structural mismatch.

## С чем легко перепутать
- Evaluation generalization легко спутать просто с generalization модели, хотя здесь речь о generalization самого evaluation conclusion.
- Больше benchmarks не всегда означает лучшее coverage.
- Contamination и generalization overlap, но не совпадают: даже чистый benchmark может слабо покрывать нужное capability space.

## Открытые вопросы
- Какие признаки показывают, что benchmark suite действительно становится более generalizable, а не просто более длинной?
- Можно ли строить evaluation pipelines, которые масштабируются вместе с capabilities без резкого роста costs?

## Связанные страницы
- [weeks/week-02](../weeks/week-02.md)
- [sources/cao-generalizable-evaluation-llm-era](../sources/cao-generalizable-evaluation-llm-era.md)
- [sources/cset-ai-safety-evaluations-explainer](../sources/cset-ai-safety-evaluations-explainer.md)
- [sources/awesome-llm-eval](../sources/awesome-llm-eval.md)
- [concepts/benchmarking](benchmarking.md)
- [concepts/statistical-rigor-in-evals](statistical-rigor-in-evals.md)
- [syntheses/benchmarking-beyond-single-scores](../syntheses/benchmarking-beyond-single-scores.md)
