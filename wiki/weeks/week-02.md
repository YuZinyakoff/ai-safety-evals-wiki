# Неделя 02

## Навигация
- [home](../home.md)
- [index](../../index.md)

## Зачем открывать эту страницу
Это hub-page второй недели. Она нужна, чтобы быстро восстановить логику недели, в которой evals перестают быть просто набором общих distinction и становятся вопросом о benchmark design, интерпретации результатов и статистической дисциплине. Если через время останется только смутная мысль "неделя была про MMLU, confidence intervals и benchmarking", эта страница должна собрать картину заново.

## Быстрый маршрут
- Если нужно восстановить taxonomy недели: начни с [sources/cset-ai-safety-evaluations-explainer](../sources/cset-ai-safety-evaluations-explainer.md), [concepts/model-safety-evals](../concepts/model-safety-evals.md) и [concepts/contextual-safety-evals](../concepts/contextual-safety-evals.md).
- Если нужен statistical core: смотри [sources/miller-adding-error-bars-to-evals](../sources/miller-adding-error-bars-to-evals.md), [sources/inspect-ai-tutorial-week-02](../sources/inspect-ai-tutorial-week-02.md) и [concepts/statistical-rigor-in-evals](../concepts/statistical-rigor-in-evals.md).
- Если нужно понять, почему benchmarking не исчерпывается одним leaderboard score: открывай [sources/cao-generalizable-evaluation-llm-era](../sources/cao-generalizable-evaluation-llm-era.md), [concepts/benchmarking](../concepts/benchmarking.md) и [concepts/evaluation-generalization](../concepts/evaluation-generalization.md).
- Если нужен landscape-wide каталог по field: переходи к [sources/awesome-llm-eval](../sources/awesome-llm-eval.md).

## Статус
- Теоретические материалы из `raw/week-02/theory/` разобраны и вынесены в source pages.
- Ноутбук из `raw/week-02/notebooks/` разобран как практический scaffold недели.
- Дополнительный материал из `raw/week-02/extra/` разобран как навигационный source по landscape evals.

## Как читать набор материалов
- [sources/cset-ai-safety-evaluations-explainer](../sources/cset-ai-safety-evaluations-explainer.md) — полный web clip и лучший entry point недели.
- [sources/miller-adding-error-bars-to-evals](../sources/miller-adding-error-bars-to-evals.md) и [sources/cao-generalizable-evaluation-llm-era](../sources/cao-generalizable-evaluation-llm-era.md) опираются на полные PDF-статьи и задают более исследовательскую глубину недели.
- [sources/inspect-ai-tutorial-week-02](../sources/inspect-ai-tutorial-week-02.md) — учебный notebook с `# YOUR CODE HERE`, поэтому его стоит читать как scaffold для практики, а не как готовый empirical report.
- [sources/awesome-llm-eval](../sources/awesome-llm-eval.md) — note-with-link к curated repo; это скорее карта поля, чем основной reading.

## Фокус недели
Неделя 02 смещает разговор от общих пределов evals к более прикладному вопросу: как устроены benchmark-centered evaluations, что именно они измеряют и как не переинтерпретировать их результаты. Источники вместе проходят путь от taxonomy model vs contextual evals к statistical interpretation, а затем к более широкой критике static benchmarks и bounded evaluation pipelines.

## Картина недели в одном абзаце
Если сжать week-02 в одну линию, получится так. Сначала материалы уточняют, что разные evaluation setups отвечают на разные safety questions, поэтому важно не смешивать model outputs и contextual impact. Затем акцент переходит к benchmark discipline: score оказывается не просто числом, а noisy estimate с confidence intervals, paired comparisons и ограниченной statistical power. Наконец, survey beyond benchmarks показывает, что даже аккуратно посчитанный benchmark result не решает проблему coverage, contamination и bounded evaluation practice. Notebook по `Inspect AI` нужен в этой картине затем, чтобы вся эта логика не осталась на уровне принципов, а превратилась в конкретный analysis workflow.

## Карта недели
- Taxonomy и design frame: [sources/cset-ai-safety-evaluations-explainer](../sources/cset-ai-safety-evaluations-explainer.md) задает distinction между model and contextual safety evaluations и рамку `what / how / what it means`.
- Statistical discipline: [sources/miller-adding-error-bars-to-evals](../sources/miller-adding-error-bars-to-evals.md) показывает, почему benchmark result нужно читать с error bars, paired analysis и power calculations.
- Beyond benchmarks: [sources/cao-generalizable-evaluation-llm-era](../sources/cao-generalizable-evaluation-llm-era.md) объясняет, почему static benchmark logic упирается в contamination, automated judging и bounded coverage.
- Practical layer: [sources/inspect-ai-tutorial-week-02](../sources/inspect-ai-tutorial-week-02.md) operationalize MMLU benchmarking и statistical analysis через `Inspect AI`.
- Landscape layer: [sources/awesome-llm-eval](../sources/awesome-llm-eval.md) служит обновляемым каталогом benchmarks, tools и leaderboards.

## Источники
### Theory
- [sources/cset-ai-safety-evaluations-explainer](../sources/cset-ai-safety-evaluations-explainer.md) — taxonomy AI safety evaluations и рамка их проектирования и интерпретации
- [sources/miller-adding-error-bars-to-evals](../sources/miller-adding-error-bars-to-evals.md) — статистический взгляд на benchmark results, confidence intervals и power
- [sources/cao-generalizable-evaluation-llm-era](../sources/cao-generalizable-evaluation-llm-era.md) — survey про evaluation beyond static benchmarks

### Notebooks
- [sources/inspect-ai-tutorial-week-02](../sources/inspect-ai-tutorial-week-02.md) — MMLU, `EvalLog`, confidence intervals, paired t-test и sample-size planning в `Inspect AI`

### Extra
- [sources/awesome-llm-eval](../sources/awesome-llm-eval.md) — curated repo как карта benchmark landscape, tools и leaderboards

## Что стоит вынести
Неделя 02 не отменяет usefulness benchmark evals. Она делает более строгим вопрос, который нужно задавать после получения результата: что именно мы измерили, насколько надежен этот estimate и насколько далеко его можно переносить.

### Базовая рамка
- Важно различать model safety evaluations и contextual safety evaluations.
- Хороший evaluation design начинается с рамки `что измеряем -> как измеряем -> как интерпретируем`.
- Benchmarking остается важным инструментом, но он измеряет только controlled slice поведения.
- Многие safety metrics являются proxy measures, а не прямым измерением реального риска.

### Где ломаются простые выводы
- Один benchmark score без confidence interval и effect-size interpretation слишком легко переоценить.
- Разница между двумя моделями может быть статистическим шумом, если не учитывать paired structure данных и sample size.
- Static benchmarks быстро сталкиваются с contamination, saturation и ограниченным coverage.
- Catalog of benchmarks не решает сам по себе вопрос validity: длинный список ресурсов еще не говорит, какой benchmark действительно подходит под конкретную задачу.
- Bounded evaluation pipeline не масштабируется автоматически вместе с ростом model capacity.

### Как это интерпретировать
- Benchmark result полезнее читать как measurement with assumptions, а не как почти готовый verdict.
- Statistical rigor нужен не как формальность для paper appendix, а как часть самого evaluation claim.
- Чем сильнее модели и шире target capability, тем опаснее делать далеко идущие выводы из одного benchmark suite.
- Practical evaluator value в такой картине состоит не только в запуске toolchain, но и в выборе правильного evaluation frame и уровня интерпретации.

Проще говоря, week-02 калибрует взгляд на benchmark culture. После нее полезно держать в голове не только вопрос "какой score у модели?", но и вопрос "какой именно тип вывода этот score вообще поддерживает?".

## Практика
- [sources/inspect-ai-tutorial-week-02](../sources/inspect-ai-tutorial-week-02.md) служит основной практической рамкой недели.
- Цель notebook: построить benchmark workflow на MMLU и довести его до statistical analysis.
- Setup: Python notebook, `inspect-ai`, Hugging Face dataset loader, `numpy`, `pandas`, `scipy`, `matplotlib`.
- Данные и задача: subject subset из `cais/mmlu`, multiple-choice evaluation.
- Solver/scorer: `multiple_choice()`, `choice()`, затем сравнение baseline и `chain_of_thought`.
- Аналитические шаги: `EvalLog -> DataFrame`, confidence intervals, paired t-test, interval estimation of difference, power analysis, required sample size.
- Ограничение: notebook учебный, не до конца исполнен и содержит `# YOUR CODE HERE`.

## Связанные концепты
- [concepts/benchmarking](../concepts/benchmarking.md) — центральный объект недели: benchmark как controlled measurement, но не финальный verdict
- [concepts/model-safety-evals](../concepts/model-safety-evals.md) — evaluation outputs самой модели
- [concepts/contextual-safety-evals](../concepts/contextual-safety-evals.md) — evaluation downstream impact и human-task context
- [concepts/statistical-rigor-in-evals](../concepts/statistical-rigor-in-evals.md) — confidence intervals, paired comparisons, power, MDE
- [concepts/evaluation-generalization](../concepts/evaluation-generalization.md) — bounded evaluation pipeline vs growing model capacity
- [concepts/inspect-ai](../concepts/inspect-ai.md) — practical tooling layer для benchmark experiments

## Связанный синтез
- [syntheses/benchmarking-beyond-single-scores](../syntheses/benchmarking-beyond-single-scores.md)

## Что повторить перед следующей неделей
- Уметь различать model safety и contextual safety evaluations.
- Понимать, почему benchmark score без uncertainty estimate слишком слаб как самостоятельный вывод.
- Держать в голове difference between `n`, `K`, paired comparison и minimum detectable effect.
- Помнить, что проблема benchmarking не исчерпывается статистикой: coverage, contamination и bounded evaluation practice тоже критичны.

## Открытые вопросы
- Какие benchmark designs сегодня лучше всего балансируют reproducibility и real-world relevance?
- Когда стоит переходить от model-side benchmarks к contextual protocols, а не просто улучшать existing benchmark suite?
- Насколько надежны automated judges как долгосрочная альтернатива expensive human evaluation?
- Как practically измерять evaluation generalization, а не только констатировать ее дефицит?

## Краткий вывод
Неделя 02 делает benchmark culture заметно взрослее. CSET explainer вводит taxonomy safety evaluations, Miller показывает, как читать benchmark results статистически честно, а survey beyond benchmarks поднимает более широкий вопрос о coverage и generalization. Notebook по `Inspect AI` переводит это в hands-on workflow на MMLU, а Awesome-LLM-Eval напоминает, что знать landscape полезно, но недостаточно. Итог недели такой: score важен, но хороший evaluation начинается раньше него и заканчивается позже него.
