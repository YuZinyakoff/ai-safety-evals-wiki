# Evals

## Что это такое
В этой wiki под evals понимаются методы систематического измерения свойств AI-систем: их способностей, склонностей и поведенческих ограничений. Важно держать в голове, что это не один конкретный benchmark и не один формат теста, а целое семейство практик измерения, elicitation и интерпретации результатов.

## Почему это важно на первой неделе
Первая неделя строится вокруг этого термина. Почти все остальные страницы week-01 либо уточняют, что считать evaluation, либо показывают пределы того, что можно надежно извлечь из evaluation results.

## Что видно по источникам
- [sources/apollo-starter-guide-evals](../sources/apollo-starter-guide-evals.md) задает базовое определение evals и основные различия внутри поля.
- [sources/barnett-thiergart-evals-catastrophic-risks](../sources/barnett-thiergart-evals-catastrophic-risks.md) показывает, что evals полезны для lower bounds, misuse assessment при сильных условиях и policy coordination.
- [sources/hubinger-understanding-based-safety-evals](../sources/hubinger-understanding-based-safety-evals.md) фиксирует, что evals и standards становятся центральной частью разговора о безопасности advanced models.
- [sources/igor-ivanov-what-is-an-evaluation](../sources/igor-ivanov-what-is-an-evaluation.md) добавляет, что само определение "что считается evaluation" неочевидно и важно для разговора про evaluation awareness.
- [sources/inspect-ai-tutorial-week-01](../sources/inspect-ai-tutorial-week-01.md) переводит разговор об evals в concrete workflow: `Task`, dataset, solver, scorer и логирование результатов.

## Что удобно помнить при повторении
- Evals полезнее всего мыслить как decision-support layer, а не как автоматическую safety guarantee.
- На первой неделе особенно важно не путать "мы что-то померили" и "мы теперь можем делать сильный вывод о безопасности".
- Если становится непонятно, о каком именно типе eval идет речь, сначала полезно восстановить различия ниже.

Именно поэтому эта страница полезна как стартовая: она не отвечает на все вопросы о reliability evals, но помогает не потерять базовую опору, без которой остальные страницы недели начинают смешиваться между собой.

## Важные различия
- Red-teaming vs benchmarking: первое активно ищет наличие свойства, второе пытается оценить частоту или вероятность поведения на выбранном распределении задач.
- Capability vs alignment evals: первое про "может ли модель", второе про "склонна ли модель".
- Misuse vs misalignment: риски от злоумышленника, использующего модель, и риски от самой системы требуют разных стандартов evidence.
- Eval context vs deployment context: вопрос не только в формальной задаче, но и в том, как модель распознает текущую среду взаимодействия.

## С чем легко перепутать
- Evals легко свести к одному benchmark или leaderboard, хотя на первой неделе они выступают как гораздо более широкое семейство практик измерения.
- Evals легко спутать с red-teaming, хотя red-teaming здесь только один из режимов работы, а не вся область целиком.
- Наличие eval pipeline не означает, что safety case уже собран: измерение и достаточное обоснование безопасности не одно и то же.

## Открытые вопросы
- Какие именно claims о безопасности допустимо строить на основании evals?
- Как сочетать evals с interpretability, audits и governance measures, чтобы не переоценивать силу одного инструмента?
- Что именно должно считаться evaluation в исследованиях evaluation awareness и evaluation gaming?

## Связанные страницы
- [weeks/week-01](../weeks/week-01.md)
- [sources/apollo-starter-guide-evals](../sources/apollo-starter-guide-evals.md)
- [sources/hubinger-understanding-based-safety-evals](../sources/hubinger-understanding-based-safety-evals.md)
- [sources/barnett-thiergart-evals-catastrophic-risks](../sources/barnett-thiergart-evals-catastrophic-risks.md)
- [sources/igor-ivanov-what-is-an-evaluation](../sources/igor-ivanov-what-is-an-evaluation.md)
- [sources/inspect-ai-tutorial-week-01](../sources/inspect-ai-tutorial-week-01.md)
- [concepts/behavioral-evals](behavioral-evals.md)
- [concepts/evaluation-awareness](evaluation-awareness.md)
- [concepts/inspect-ai](inspect-ai.md)
- [concepts/understanding-based-evals](understanding-based-evals.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
