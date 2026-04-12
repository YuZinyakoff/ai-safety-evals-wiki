# Agent Reliability

## Коротко
> **Agent reliability** — это не "насколько часто агент прав", а насколько стабильно, предсказуемо и безопасно он ведет себя при повторных запусках, под возмущениями и в случаях неудачи.

## Почему это важный концепт
Week-04 проводит важное различие между capability и reliability. Агент может решать сложные задачи, но делать это слишком нестабильно, слишком хрупко или слишком опасно для реального deployment.

## Основные измерения
- `Consistency`: одинаково ли агент ведет себя на повторных запусках?
- `Robustness`: как сильно поведение деградирует при изменении prompt, environment или tool failures?
- `Predictability`: умеет ли агент и его confidence signal различать likely success и likely failure?
- `Safety`: насколько тяжелыми оказываются последствия, когда агент ошибается?

## Что именно здесь ломает наивный вывод
- **Средний score** не показывает variance between runs.
- **Успех на benchmark** не показывает, насколько agent brittle вне nominal conditions.
- **Редкие catastrophic failures** нельзя честно усреднить в тот же score, что и benign mistakes.

## Практическая интуиция
Если агент делает что-то consequential, полезно задавать не только вопрос "насколько он часто succeeds", но и:
- как часто он неожиданно меняет trajectory,
- как переносит perturbations,
- умеет ли распознавать uncertainty,
- и насколько плохи его failures.

## С чем легко перепутать
- Reliability легко спутать с raw capability.
- Ее легко свести к consistency only, хотя Princeton paper делает рамку шире.
- Ее легко считать purely safety concept, хотя reliability включает и non-safety operational properties.

## Где смотреть дальше
- [AI Agent Reliability](../sources/science-ai-agent-reliability.md)
- [LLM Agents Survey](../sources/evaluation-benchmarking-llm-agents-survey.md)

## Открытые вопросы
- Какие reliability metrics practical для реальных agent deployments, а какие остаются mainly academic?
- Какие dimensions reliability важнее в разных task families: coding, research, operations, customer service?

## Связанные страницы
- [concepts/agent-evaluation](agent-evaluation.md)
- [concepts/agent-autonomy](agent-autonomy.md)
- [sources/science-ai-agent-reliability](../sources/science-ai-agent-reliability.md)
- [syntheses/agent-evals-beyond-task-success](../syntheses/agent-evals-beyond-task-success.md)
