# Evals

## Что это такое
В этой wiki под evals понимаются методы систематического измерения свойств AI-систем: их способностей, склонностей и поведенческих ограничений. Важно держать в голове, что это не один конкретный benchmark и не один формат теста, а целое семейство практик измерения, elicitation и интерпретации результатов.

## Почему это важно в курсе
Первая неделя вводит этот термин и показывает пределы behavior-based evidence. Вторая неделя делает шаг дальше: уточняет виды evaluation, усиливает benchmark-centered часть поля и добавляет вопрос о статистической интерпретации результатов. Поэтому эта страница полезна уже не только как стартовый словарь, но и как место, где разные линии курса снова сходятся.

## Что видно по источникам
- [sources/apollo-starter-guide-evals](../sources/apollo-starter-guide-evals.md) задает базовое определение evals и основные различия внутри поля.
- [sources/barnett-thiergart-evals-catastrophic-risks](../sources/barnett-thiergart-evals-catastrophic-risks.md) показывает, что evals полезны для lower bounds, misuse assessment при сильных условиях и policy coordination.
- [sources/hubinger-understanding-based-safety-evals](../sources/hubinger-understanding-based-safety-evals.md) фиксирует, что evals и standards становятся центральной частью разговора о безопасности advanced models.
- [sources/igor-ivanov-what-is-an-evaluation](../sources/igor-ivanov-what-is-an-evaluation.md) добавляет, что само определение "что считается evaluation" неочевидно и важно для разговора про evaluation awareness.
- [sources/inspect-ai-tutorial-week-01](../sources/inspect-ai-tutorial-week-01.md) переводит разговор об evals в concrete workflow: `Task`, dataset, solver, scorer и логирование результатов.
- [sources/cset-ai-safety-evaluations-explainer](../sources/cset-ai-safety-evaluations-explainer.md) различает model safety и contextual safety evaluations и добавляет design frame `what / how / what it means`.
- [sources/miller-adding-error-bars-to-evals](../sources/miller-adding-error-bars-to-evals.md) показывает, что evaluation results нужно читать как noisy estimates, а не как self-explanatory scores.
- [sources/cao-generalizable-evaluation-llm-era](../sources/cao-generalizable-evaluation-llm-era.md) расширяет разговор до limits of static benchmarks и evaluation generalization.
- [sources/inspect-ai-tutorial-week-02](../sources/inspect-ai-tutorial-week-02.md) показывает, как benchmark run соединяется со statistical analysis.

## Что удобно помнить при повторении
- Evals полезнее всего мыслить как decision-support layer, а не как автоматическую safety guarantee.
- Особенно важно не путать "мы что-то померили" и "мы теперь можем делать сильный вывод о безопасности или превосходстве модели".
- Если становится непонятно, о каком именно типе eval идет речь, сначала полезно восстановить различия ниже.

Именно поэтому эта страница полезна как стартовая: она не отвечает на все вопросы о reliability evals, но помогает не потерять базовую опору, без которой остальные страницы недели начинают смешиваться между собой.

## Важные различия
- Red-teaming vs benchmarking: первое активно ищет наличие свойства, второе пытается оценить частоту или вероятность поведения на выбранном распределении задач.
- Capability vs alignment evals: первое про "может ли модель", второе про "склонна ли модель".
- Model safety vs contextual safety evals: первое оценивает outputs модели, второе пытается схватить ее downstream usefulness или impact in context.
- Misuse vs misalignment: риски от злоумышленника, использующего модель, и риски от самой системы требуют разных стандартов evidence.
- Eval context vs deployment context: вопрос не только в формальной задаче, но и в том, как модель распознает текущую среду взаимодействия.
- Point estimate vs uncertainty-aware result: score сам по себе и score вместе с CI, paired comparison и power reasoning — это разная сила evidence.

## С чем легко перепутать
- Evals легко свести к одному benchmark или leaderboard, хотя на первой неделе они выступают как гораздо более широкое семейство практик измерения.
- Evals легко спутать с red-teaming, хотя red-teaming здесь только один из режимов работы, а не вся область целиком.
- Наличие eval pipeline не означает, что safety case уже собран: измерение и достаточное обоснование безопасности не одно и то же.
- Большой benchmark landscape тоже не означает, что проблема evaluation validity уже решена.

## Открытые вопросы
- Какие именно claims о безопасности допустимо строить на основании evals?
- Как сочетать evals с interpretability, audits и governance measures, чтобы не переоценивать силу одного инструмента?
- Что именно должно считаться evaluation в исследованиях evaluation awareness и evaluation gaming?

## Связанные страницы
- [weeks/week-01](../weeks/week-01.md)
- [weeks/week-02](../weeks/week-02.md)
- [sources/apollo-starter-guide-evals](../sources/apollo-starter-guide-evals.md)
- [sources/hubinger-understanding-based-safety-evals](../sources/hubinger-understanding-based-safety-evals.md)
- [sources/barnett-thiergart-evals-catastrophic-risks](../sources/barnett-thiergart-evals-catastrophic-risks.md)
- [sources/igor-ivanov-what-is-an-evaluation](../sources/igor-ivanov-what-is-an-evaluation.md)
- [sources/inspect-ai-tutorial-week-01](../sources/inspect-ai-tutorial-week-01.md)
- [sources/cset-ai-safety-evaluations-explainer](../sources/cset-ai-safety-evaluations-explainer.md)
- [sources/miller-adding-error-bars-to-evals](../sources/miller-adding-error-bars-to-evals.md)
- [sources/cao-generalizable-evaluation-llm-era](../sources/cao-generalizable-evaluation-llm-era.md)
- [sources/inspect-ai-tutorial-week-02](../sources/inspect-ai-tutorial-week-02.md)
- [concepts/behavioral-evals](behavioral-evals.md)
- [concepts/benchmarking](benchmarking.md)
- [concepts/model-safety-evals](model-safety-evals.md)
- [concepts/contextual-safety-evals](contextual-safety-evals.md)
- [concepts/statistical-rigor-in-evals](statistical-rigor-in-evals.md)
- [concepts/evaluation-awareness](evaluation-awareness.md)
- [concepts/inspect-ai](inspect-ai.md)
- [concepts/understanding-based-evals](understanding-based-evals.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
- [syntheses/benchmarking-beyond-single-scores](../syntheses/benchmarking-beyond-single-scores.md)
