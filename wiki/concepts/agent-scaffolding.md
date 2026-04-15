# Agent Scaffolding

## Коротко
> **Agent scaffolding** — это вся внешняя структура вокруг модели: prompts, tools, loop design, memory handling, stopping rules, message limits, context management и логика оркестрации.

## Почему это важный концепт
В week-04 scaffolding перестает быть "технической обвязкой" и становится частью measurement. Именно scaffolding часто определяет, сможет ли агент показать свои способности, где он будет ошибаться и какой будет цена этих ошибок.

## Что сюда входит
- System prompt и инструкции к задаче.
- Набор и интерфейс tools.
- Loop pattern: одиночный вызов инструмента, ReAct, planner-executor и т.д.
- Управление контекстом, памятью, retries и stopping rules.
- Resource limits: token budget, message limit, timeouts.

## Что именно здесь ломает наивный вывод
- **Слабый scaffold** легко занижает видимую capability.
- **Слишком сильный scaffold** может скрывать собственные limits модели.
- **Изменение tool interface** может менять outcome без изменения core model.

## Практическая интуиция
Если агент провалился, полезно отдельно спросить:
- проблема в модели,
- в scaffold,
- в их взаимодействии,
- или в рассогласовании между scaffold и benchmark/task distribution?

## С чем легко перепутать
- Scaffolding легко принять за "нечестное усиление".
- Его легко считать чисто инженерным слоем, хотя для eval он еще и эпистемический слой.
- Его легко свести к prompt, забыв про tools, limits и loop structure.

## Где смотреть дальше
- [ReAct](../sources/react-synergizing-reasoning-acting.md)
- [Inspect AI tutorial week-04](../sources/inspect-ai-tutorial-week-04.md)
- [METR elicitation guidelines](../sources/metr-guidelines-capability-elicitation.md)

## Открытые вопросы
- Какие scaffolding choices должны считаться частью модели, а какие частью evaluation procedure?
- Как сравнивать агентов честно, если их optimal scaffolds различаются?

## Связанные страницы
- [concepts/capability-elicitation](capability-elicitation.md)
- [concepts/react-agents](react-agents.md)
- [concepts/inspect-ai](inspect-ai.md)
- [sources/react-synergizing-reasoning-acting](../sources/react-synergizing-reasoning-acting.md)
