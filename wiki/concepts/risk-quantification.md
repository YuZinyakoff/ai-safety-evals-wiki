# Risk Quantification

## Коротко
> **Risk quantification** — это попытка перейти от простого benchmark score к более содержательному разговору о вероятности и тяжести harm. Для safety evals это критично, потому что observed rate сам по себе почти никогда не равен deployment-relevant risk.

## Почему это важный концепт
Week-02 учила статистически аккуратнее читать benchmark results, а week-05 показывает, что для safety этого все еще недостаточно. Нужно не только считать confidence intervals, но и отличать `sample proportion` от risk probability, учитывать severity и думать о том, как benchmark output вообще переносится на реальный мир.

## Что здесь важно различать
- **Observed frequency** — что произошло на данном наборе кейсов.
- **Calibrated probability** — более сильное утверждение о том, как часто harm ожидается в use context.
- **Severity** — насколько тяжелы отдельные failure cases.
- **Exposure / prevalence** — насколько часто такой сценарий вообще возникает в deployment.

## Что именно здесь ломает наивный вывод
- Benchmark failure rate легко принять за probability of harm.
- Binary pass/fail metric скрывает разницу между mild harm и catastrophic harm.
- Без deployment prevalence одинаковый score может означать radically different real-world risk.
- Без uncertainty margins маленькие выборки создают ложную точность.

## Практическая интуиция
Полезно держать такую формулу: **риск — это не только частота, но и тяжесть, а еще то, насколько lab measurement переносится в реальное использование**. Поэтому safety report без разговора о severity, uncertainty и generalization limits почти всегда недосказан.

## С чем легко перепутать
- Risk quantification легко свести к простому подсчету доверительных интервалов.
- Ее легко спутать с ranking models by score.
- Ее легко понимать как purely mathematical step, игнорируя normative choices about what counts as severe harm.

## Где смотреть дальше
- [How Should AI Safety Benchmarks Benchmark Safety?](../sources/how-should-ai-safety-benchmarks-benchmark-safety.md)
- [Adding Error Bars to Evals](../sources/miller-adding-error-bars-to-evals.md)
- [Science of Evals](science-of-evals.md)

## Открытые вопросы
- Какие severity frameworks реалистично применять к LLM safety benchmarks?
- Когда вообще правомерно делать переход от benchmark frequencies к deployment-level risk estimates?

## Связанные страницы
- [concepts/statistical-rigor-in-evals](statistical-rigor-in-evals.md)
- [concepts/measurement-validity](measurement-validity.md)
- [concepts/ai-safety-benchmarks](ai-safety-benchmarks.md)
- [concepts/science-of-evals](science-of-evals.md)
