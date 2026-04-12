# ReAct Agents

## Коротко
> **ReAct** — это agent pattern, в котором модель чередует reasoning и action, а затем использует observation from tools or environment для следующего шага.

## Почему это важный концепт
Week-04 использует ReAct не как историческую справку, а как простой и наглядный пример того, как loop structure меняет поведение агента. Через ReAct хорошо видно, что agent eval зависит от того, как организована сама траектория.

## Что здесь происходит
- Модель формулирует промежуточный reasoning step.
- Делает tool call или другое действие.
- Получает observation.
- Переосмысляет план и идет дальше.

Это отличает ReAct и от purely single-shot generation, и от менее структурированного tool use, где tool calls не образуют явного feedback loop.

## Что именно здесь ломает наивный вывод
- **Дать tools** еще не значит **получить хорошего агента**.
- **Больше шагов** еще не значит **лучший reasoning**.
- **ReAct success** может зависеть от prompt and tool schema не меньше, чем от core model.

## Практическая интуиция
ReAct полезно видеть как минимальную форму agent scaffolding: достаточно сложную, чтобы появились trajectory-level failures, и достаточно простую, чтобы их еще можно было руками проследить.

## С чем легко перепутать
- ReAct легко принять за саму сущность agentness.
- Его легко считать гарантированным улучшением по сравнению с simpler loops.
- Его легко обсуждать как reasoning technique, забывая, что для eval это еще и measurement setup.

## Где смотреть дальше
- [ReAct source](../sources/react-synergizing-reasoning-acting.md)
- [Inspect AI tutorial week-04](../sources/inspect-ai-tutorial-week-04.md)
- [agent scaffolding](agent-scaffolding.md)

## Открытые вопросы
- В каких task families ReAct достаточно силен, а где нужен richer scaffold?
- Какие failure modes именно ReAct делает видимыми, а какие наоборот маскирует?

## Связанные страницы
- [concepts/agent-scaffolding](agent-scaffolding.md)
- [concepts/agent-evaluation](agent-evaluation.md)
- [sources/react-synergizing-reasoning-acting](../sources/react-synergizing-reasoning-acting.md)
