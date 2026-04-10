# Statistical Rigor In Evals

## Что это такое
Statistical rigor in evals означает привычку рассматривать evaluation как эксперимент с шумом, ограниченной выборкой и явной неопределенностью. На практике это означает не ограничиваться одним score, а думать про confidence intervals, paired comparisons, power analysis, sample size и minimum detectable effect.

## Почему это важно на второй неделе
Week-02 делает статистическую часть evals центральной, а не декоративной. Если в первой неделе основной вопрос был "какие claims вообще допустимы?", то здесь вопрос становится строже: "какой вывод о model difference или benchmark performance допустим при данной неопределенности?".

## Что видно по источникам
- [sources/miller-adding-error-bars-to-evals](../sources/miller-adding-error-bars-to-evals.md) систематически вводит confidence intervals, paired analysis и power analysis для LLM evals.
- [sources/inspect-ai-tutorial-week-02](../sources/inspect-ai-tutorial-week-02.md) operationalize эти идеи на MMLU через `EvalLog`, DataFrame и per-question scores.
- [sources/cset-ai-safety-evaluations-explainer](../sources/cset-ai-safety-evaluations-explainer.md) напоминает, что многие metrics являются proxies и потому требуют осторожной интерпретации.
- [sources/cao-generalizable-evaluation-llm-era](../sources/cao-generalizable-evaluation-llm-era.md) показывает, что benchmarking without statistical care легко приводит к unfair or unstable comparisons.

## Как этим пользоваться при повторении
- Если видишь benchmark score, сразу полезно спросить про uncertainty around estimate.
- Если сравниваются две модели на одних и тех же вопросах, paired analysis обычно информативнее простого сравнения средних.
- До дорогого eval полезно считать, какие effect sizes вообще detectible при текущем `n` и количестве прогонов.

Практическая интуиция week-02 такая: хороший eval design включает не только dataset и scorer, но и честный ответ на вопрос, насколько наблюдаемый эффект может быть шумом. Без этого даже аккуратно собранный benchmark workflow легко превращается в красивую, но слабую статистически историю.

## С чем легко перепутать
- Statistical significance легко спутать с practical importance.
- Большее число повторов `K` легко спутать с большим числом вопросов `n`, хотя это разные источники выигрыша в precision.
- Error bars не решают проблему плохого benchmark design, а только делают честнее выводы на данном дизайне.

## Открытые вопросы
- Какие методы uncertainty estimation лучше всего подходят для open-ended or clustered evaluation settings?
- Какой минимум statistical reporting стоит считать обязательным для benchmark comparisons?

## Связанные страницы
- [weeks/week-02](../weeks/week-02.md)
- [sources/miller-adding-error-bars-to-evals](../sources/miller-adding-error-bars-to-evals.md)
- [sources/inspect-ai-tutorial-week-02](../sources/inspect-ai-tutorial-week-02.md)
- [sources/cao-generalizable-evaluation-llm-era](../sources/cao-generalizable-evaluation-llm-era.md)
- [concepts/benchmarking](benchmarking.md)
- [concepts/evaluation-generalization](evaluation-generalization.md)
- [concepts/inspect-ai](inspect-ai.md)
- [syntheses/benchmarking-beyond-single-scores](../syntheses/benchmarking-beyond-single-scores.md)
