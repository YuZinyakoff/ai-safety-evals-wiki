# Agent Evaluation

## Коротко
> **Agent evaluation** — это оценка систем, которые не просто выдают ответ, а идут по траектории: планируют, вызывают инструменты, взаимодействуют со средой, меняют стратегию и могут по-разному вести себя при повторных запусках.

## Почему это важный концепт
Week-04 показывает, что agent evaluation нельзя просто свести к "LLM eval плюс tools". У агента больше степеней свободы, больше failure modes и больше мест, где процедура оценки начинает влиять на сам результат.

## Что сюда обычно входит
- `Behavior`: task success, output quality, latency, cost.
- `Capabilities`: tool use, planning, memory, multi-step execution.
- `Reliability`: consistency, robustness, predictability.
- `Safety`: bounded harmfulness, compliance, constrained behavior.
- `Autonomy`: сколько решения реально делегируется системе и как устроен oversight.

## Что именно здесь ломает наивный вывод
- **Один success score** легко скрывает radically different trajectories.
- **Одинаковый outcome** не означает одинаковый reliability profile.
- **Product setup** и **eval setup** могут измерять разные вещи.
- **Scaffolding** может сильно менять то, что агент вообще способен показать.

## Практическая интуиция
Полезно держать такой вопрос: **я сейчас оцениваю самого агента, agent + scaffolding, agent in deployment context или reachable performance after elicitation?** Пока это не проговорено, вывод почти всегда будет слишком расплывчатым.

## С чем легко перепутать
- Agent evaluation легко принять за обычный benchmarking на более сложных задачах.
- Его легко свести только к capability testing, забыв про reliability and oversight.
- Его легко читать как чисто pre-deployment exercise, хотя week-04 показывает важность post-deployment evidence.

## Где смотреть дальше
- [LLM Agents Survey](../sources/evaluation-benchmarking-llm-agents-survey.md)
- [AI Agent Reliability](../sources/science-ai-agent-reliability.md)
- [METR elicitation guidelines](../sources/metr-guidelines-capability-elicitation.md)
- [Anthropic autonomy in practice](../sources/measuring-ai-agent-autonomy-practice.md)

## Открытые вопросы
- Какие agent properties наиболее важны для разных deployment contexts?
- Насколько realistic должен быть evaluation setup, чтобы оставаться полезным и контролируемым одновременно?

## Связанные страницы
- [concepts/agent-reliability](agent-reliability.md)
- [concepts/capability-elicitation](capability-elicitation.md)
- [concepts/agent-scaffolding](agent-scaffolding.md)
- [concepts/agent-autonomy](agent-autonomy.md)
- [syntheses/agent-evals-beyond-task-success](../syntheses/agent-evals-beyond-task-success.md)
