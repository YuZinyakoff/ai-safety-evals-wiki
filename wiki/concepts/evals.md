# Evals

## Суть
В этой wiki под evals понимаются методы систематического измерения свойств AI-систем: их способностей, склонностей и поведенческих ограничений.

## Факты из источников
- [[sources/apollo-starter-guide-evals]] задает общее определение evals как систематического измерения свойств AI-систем.
- [[sources/apollo-starter-guide-evals]] различает red-teaming и benchmarking, а также capability evals и alignment evals.
- [[sources/barnett-thiergart-evals-catastrophic-risks]] показывает, что evals полезны для lower bounds, misuse assessment при сильных условиях и policy coordination.
- [[sources/hubinger-understanding-based-safety-evals]] фиксирует, что evals и standards уже становятся центральной частью разговора о безопасности advanced models.
- [[sources/igor-ivanov-what-is-an-evaluation]] показывает, что само определение "что считается evaluation" неочевидно и важно для анализа evaluation awareness.
- [[sources/inspect-ai-tutorial-week-01]] переводит разговор об evals в concrete workflow: `Task`, dataset, solver, scorer и логирование результатов.

## Рабочая интерпретация
- Для этой базы знаний evals — это прежде всего инструменты измерения и decision support, а не автоматические safety guarantees.
- Уже на первой неделе видно внутреннее напряжение темы: чем важнее вывод, который мы хотим сделать, тем осторожнее нужно переносить результат evals в claim о safety.

## Важные различия
- Red-teaming vs benchmarking: первое активно ищет наличие свойства, второе пытается оценить частоту или вероятность поведения на выбранном распределении задач.
- Capability vs alignment evals: первое про "может ли модель", второе про "склонна ли модель".
- Misuse vs misalignment: риски от злоумышленника, использующего модель, и риски от самой системы требуют разных стандартов evidence.
- Eval context vs deployment context: вопрос не только в формальной задаче, но и в том, как модель распознает текущую среду взаимодействия.

## Открытые вопросы
- Какие именно claims о безопасности допустимо строить на основании evals?
- Как сочетать evals с interpretability, audits и governance measures, чтобы не переоценивать силу одного инструмента?
- Что именно должно считаться evaluation в исследованиях evaluation awareness и evaluation gaming?

## Связанные страницы
- [[weeks/week-01]]
- [[sources/apollo-starter-guide-evals]]
- [[sources/hubinger-understanding-based-safety-evals]]
- [[sources/barnett-thiergart-evals-catastrophic-risks]]
- [[sources/igor-ivanov-what-is-an-evaluation]]
- [[sources/inspect-ai-tutorial-week-01]]
- [[concepts/behavioral-evals]]
- [[concepts/evaluation-awareness]]
- [[concepts/inspect-ai]]
- [[concepts/understanding-based-evals]]
- [[syntheses/evals-scope-and-limits]]
