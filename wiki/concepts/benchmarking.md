# Benchmarking

## Коротко
> **Benchmarking** — это evaluation через стандартизированный набор задач, вопросов или сценариев, на котором модели можно сравнивать по общим правилам. Его сила в controlled measurement, а слабость — в том, что такой контроль почти всегда достигается ценой ограниченного coverage.

## Почему это важный концепт
Week-02 вводит benchmarking как controlled measurement practice, week-03 резко усложняет картину, показывая, что benchmark сам по себе является содержательной конструкцией, а week-04 добавляет agent layer: в случае агентов benchmark часто оценивает не просто модель, а модель вместе с scaffold, tools, environment и evaluation procedure. Week-05 делает еще один шаг и показывает, что в safety context benchmarking становится еще более demanding: нужно отдельно говорить о harm constructs, proxy chains, severity и deployment relevance. Поэтому benchmarking здесь нужно держать не как абстрактное слово, а как практику со своими trade-offs: удобство сравнения, statistical discipline, contamination concerns, design assumptions и bounded transfer of conclusions.

## Что именно здесь ломает наивный вывод
- **Controlled slice** легко принять за полный портрет модели.
- **Score difference** легко прочитать как meaningful difference без uncertainty estimates.
- **Static suites** быстро сталкиваются с contamination и saturation.
- **Большой benchmark landscape** легко принять за solved measurement problem.
- **Agent benchmarks** особенно чувствительны к procedure quality, retrieval, harness stability и elicitation gaps.
- **Safety benchmarks** нельзя читать как прямую меру real-world safety без дополнительной validity и risk reasoning.

## Как распознать риск в реальном benchmark
- Когда benchmark ranking читают без question о coverage.
- Когда suite выглядит очень большим, но неясно, какой именно claim он должен поддерживать.
- Когда сравнение моделей опирается только на aggregate score без paired structure и uncertainty reasoning.
- Когда benchmark reused так часто, что contamination risk уже трудно игнорировать.

## Практическая интуиция
Полезно держать такую формулу: **benchmarking удобно сравнивает модели, но само удобство сравнения не гарантирует силу вывода**. После week-03 к этому нужно добавить еще один слой: benchmarking не просто фиксирует различия между моделями, а partly конструирует их видимость через design задач, метрик и aggregate rules.

## С чем легко перепутать
- Benchmarking легко принять за все evals вообще, хотя это только один режим оценки.
- Static benchmark легко спутать с устойчивым gold standard, хотя survey показывает, как быстро такие suites saturate или загрязняются.
- Разница в score не равна meaningful difference, если не оценены uncertainty и design assumptions.

## Где смотреть дальше
- [Miller](../sources/miller-adding-error-bars-to-evals.md) — как читать benchmark score статистически.
- [Generalizable Evaluation survey](../sources/cao-generalizable-evaluation-llm-era.md) — почему field движется beyond static benchmarks.
- [CSET explainer](../sources/cset-ai-safety-evaluations-explainer.md) — где benchmarking стоит внутри более широкой taxonomy.
- [HELM](../sources/holistic-evaluation-language-models.md) — как benchmark превращается в more explicit multi-metric framework.
- [The Benchmark Lottery](../sources/benchmark-lottery.md) — как benchmark ecosystem искажает narrative о прогрессе.
- [SWE-bench Verified](../sources/swe-bench-verified.md) — как benchmark quality control меняет capability claims для агентов.
- [How Should AI Safety Benchmarks Benchmark Safety?](../sources/how-should-ai-safety-benchmarks-benchmark-safety.md) — почему safety benchmarks требуют более строгого стандарта.

## Открытые вопросы
- Как понимать, что benchmark действительно отражает нужную capability, а не только удобный proxy?
- Какие dynamic benchmark designs дают реальный выигрыш по сравнению со static suites?

## Связанные страницы
- [concepts/model-safety-evals](model-safety-evals.md)
- [concepts/statistical-rigor-in-evals](statistical-rigor-in-evals.md)
- [concepts/evaluation-generalization](evaluation-generalization.md)
- [concepts/benchmark-design](benchmark-design.md)
- [concepts/ai-safety-benchmarks](ai-safety-benchmarks.md)
- [concepts/agent-evaluation](agent-evaluation.md)
- [syntheses/benchmarking-beyond-single-scores](../syntheses/benchmarking-beyond-single-scores.md)
