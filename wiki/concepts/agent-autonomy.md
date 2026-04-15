# Agent Autonomy

## Коротко
> **Agent autonomy** — это степень самостоятельности, с которой система действует без непосредственного участия человека: сколько шагов она делает сама, какие действия может предпринимать и как устроены остановки, подтверждения и вмешательства.

## Почему это важный концепт
Week-04 показывает, что autonomy нельзя читать только как capability number. В реальном использовании она складывается из модели, продукта, настроек подтверждения, пользовательских привычек и agent-initiated stops.

## Что сюда обычно входит
- Scope действий, которые агент может предпринимать.
- Длина автономной траектории.
- Степень human oversight и approval.
- Reversibility и riskiness действий.
- Способность агента самостоятельно останавливаться или запрашивать уточнение.

## Что именно здесь ломает наивный вывод
- **Высокая capability** не обязательно означает высокую exercised autonomy.
- **Низкая autonomy в deployment** не обязательно означает низкую reachable capability.
- **Human in the loop** не гарантирует качественный oversight, если вмешательство устроено плохо.

## Практическая интуиция
Полезно различать:
- what the model could do,
- what the product lets it do,
- what users actually allow it to do,
- и как часто человек или сам агент останавливают выполнение.

## С чем легко перепутать
- Autonomy легко спутать с полной автоматизацией.
- Ее легко понимать только как long-horizon capability, забывая про oversight structure.
- Ее легко читать как чисто техническое свойство, хотя она частично определяется продуктом и взаимодействием пользователя с системой.

## Где смотреть дальше
- [Anthropic autonomy in practice](../sources/measuring-ai-agent-autonomy-practice.md)
- [LLM Agents Survey](../sources/evaluation-benchmarking-llm-agents-survey.md)
- [METR resources](../sources/metr-autonomy-evaluation-resources.md)

## Открытые вопросы
- Какие proxies autonomy достаточно хороши для safety-relevant monitoring?
- Как связывать измерения autonomy in deployment с pre-deployment evaluation claims?

## Связанные страницы
- [concepts/agent-evaluation](agent-evaluation.md)
- [concepts/agent-reliability](agent-reliability.md)
- [sources/measuring-ai-agent-autonomy-practice](../sources/measuring-ai-agent-autonomy-practice.md)
- [syntheses/agent-evals-beyond-task-success](../syntheses/agent-evals-beyond-task-success.md)
