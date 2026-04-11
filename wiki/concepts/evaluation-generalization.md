# Evaluation Generalization

## Коротко
> **Evaluation generalization** — это вопрос о том, насколько выводы из ограниченного evaluation pipeline действительно переносятся на более широкий класс задач, поведений и будущих capability regimes. Иными словами: generalize должен не только model behavior, но и сам evaluation conclusion.

## Почему это важный концепт
Week-02 поднимает этот вопрос уже в явной форме. После первой недели понятно, что behavior-based evidence ограничено; вторая неделя добавляет более конкретный механизм: даже очень аккуратный benchmark suite может не успевать за ростом моделей и потому слабо generalize.

## Как именно здесь ломается вывод
- **Большой suite** легко принять за сильное coverage.
- **Чистый benchmark** легко спутать с generalizable benchmark.
- **Contamination** можно считать единственной проблемой, хотя даже uncontaminated suite может плохо покрывать нужный capability space.
- **Static protocol** может быстро устаревать по отношению к scaling models.

## Практическая интуиция
Эта страница полезна как antidote к интуиции “чем длиннее benchmark list, тем надежнее оценка”. Даже если evaluation suite выглядит внушительно, все равно стоит спрашивать: **что осталось вне coverage, каков risk of contamination, и на какой ширины claim мы вообще замахиваемся?**

## С чем легко перепутать
- Evaluation generalization легко спутать с generalization модели, хотя здесь речь о переносимости самого evaluation conclusion.
- Больше benchmarks не всегда означает better coverage.
- Contamination и generalization overlap, но не совпадают: даже чистый benchmark может слабо покрывать нужный capability space.

## Где смотреть дальше
- [Generalizable Evaluation survey](../sources/cao-generalizable-evaluation-llm-era.md) — главный source по теме.
- [Benchmarking](benchmarking.md) — controlled slice behavior как отправная точка проблемы.
- [Awesome LLM Eval](../sources/awesome-llm-eval.md) — хороший reminder, что landscape size не равен solved external validity problem.

## Открытые вопросы
- Какие признаки показывают, что benchmark suite действительно становится more generalizable, а не просто более длинной?
- Можно ли строить evaluation pipelines, которые масштабируются вместе с capabilities без резкого роста costs?

## Связанные страницы
- [concepts/benchmarking](benchmarking.md)
- [concepts/statistical-rigor-in-evals](statistical-rigor-in-evals.md)
- [syntheses/benchmarking-beyond-single-scores](../syntheses/benchmarking-beyond-single-scores.md)
