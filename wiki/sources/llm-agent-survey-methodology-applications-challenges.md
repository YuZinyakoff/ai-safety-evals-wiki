# Large Language Model Agent: A Survey On Methodology, Applications And Challenges

- **Тип источника:** extra
- **Неделя:** week-04
- **Raw:** [clipped `.md`](<../../raw/week-04/extra/Large Language Model Agent A Survey on Methodology, Applications and Challenges.md>), [PDF](<../../raw/week-04/extra/2503.21460v1.pdf>), [TeX source](<../../raw/week-04/extra/arXiv-2503.21460v1.tar.gz>)
- **Оригинал:** [arXiv](https://arxiv.org/abs/2503.21460)
- **Полнота raw:** сильный raw-набор: clipped Markdown, PDF и TeX source

## Ключевая мысль
> **Чтобы оценивать агентов, полезно сначала понимать, как они вообще устроены.** Разные memory, planning, collaboration и evolution choices создают разные типы поведения, а значит и разные evaluation challenges.

## Зачем источник в базе
Этот survey нужен как дополнительный взгляд на сам объект оценки. Он полезен не как текст про evaluation в узком смысле, а как карта того, какие architectural and methodological decisions вообще делают agent an agent.

## Эпистемический статус и как на него смотреть
Это broad agent-methodology survey, а не evaluation-first paper. Его полезно читать как pre-evaluation map: сначала понять, какие agent design dimensions существуют, и только потом решать, что и как измерять.

## На какие вопросы источник помогает отвечать
- Какие основные dimensions authors используют, чтобы описывать LLM agents?
- Почему memory, planning, collaboration and evolution важны для evaluation design?
- Чем agent methodology влияет на observed behavior еще до benchmarking?
- Где в таком broad survey вообще находится evaluation and tooling layer?

## Краткое содержание
Статья строит широкий ecosystem view на `LLM agents`. Сначала она предлагает methodology-centered taxonomy и раскладывает агентские системы по осям `construction`, `collaboration` и `evolution`. Затем подробно обсуждаются role/profile definition, memory mechanisms, planning, tool use, centralized / decentralized / hybrid multi-agent architectures и разные формы self-improvement. Отдельный блок посвящен `evaluation and tools`, то есть benchmark and tooling ecosystem. Для week-04 особенно полезно то, что paper показывает: agent behavior зависит от большого числа design choices задолго до evaluation stage.

## Структура материала
- `1 Introduction`: общая постановка survey.
- `2 Agent Methodology`: construction, collaboration и evolution как три большие оси.
- `3 Evaluation and Tools`: benchmarks, datasets и tooling layer.
- `4 Real-World Issues`: security, privacy, ethical concerns.
- `5 Applications`: scientific discovery, gaming, social science, productivity tools.
- `6 Challenges and Future Trends` и `7 Conclusion`: куда authors двигают field дальше.

## Как читать источник быстро
- Если нужен high-level map, читай `2 Agent Methodology`: там лучше всего видно, как survey раскладывает agents по архитектурным блокам.
- Если вопрос про specific agent properties, заходи внутрь `2 Agent Methodology`, особенно в подблоки про memory, planning, action execution и collaboration.
- Если интересует direct relevance to the week, сначала смотри `3 Evaluation and Tools`, а уже потом при необходимости возвращайся к applications или risks.

## Что источник утверждает прямо
- LLM agents существенно различаются по dimensions like construction, collaboration, evolution, memory, planning and tool use.
- Эти design dimensions меняют behavior and failure modes еще до того, как начинается evaluation.
- Evaluation and tools в survey выступают как один блок внутри более широкого agent methodology stack.
- Broad taxonomies полезны для ориентации, но сами по себе не решают, как именно should be measured each agent setup.

## Что здесь особенно важно
- **Object of evaluation is heterogeneous.** "Агент" — это не один класс систем.
- **Memory, planning, collaboration and evolution** меняют failure modes.
- **Evaluation questions** нельзя полностью отделить от agent methodology.

## Интерпретация для курса
Для курса этот survey полезен как pre-evaluation map. Он помогает не забывать, что вопрос “как оценивать агента?” начинается еще раньше с вопроса “что именно мы называем агентом и какие design choices already shape the behavior we observe?”.

## Что это добавляет к теме недели
Этот текст делает week-04 менее узкой. Он напоминает, что evaluation choices должны соотноситься с тем, какой именно тип agent architecture перед нами.

## Что стоит запомнить при повторении
- **Нельзя оценивать всех агентов как будто они устроены одинаково.**
- **Methodology и evaluation связаны сильнее, чем кажется.**
- **Agent survey полезен как pre-evaluation map.**

## Связанные концепты
- [concepts/agent-evaluation](../concepts/agent-evaluation.md)
- [concepts/agent-scaffolding](../concepts/agent-scaffolding.md)
- [concepts/react-agents](../concepts/react-agents.md)

## Что осталось неясным / спорным
- Насколько полезны broad agent taxonomies для конкретного evaluation design?
- Не размывает ли слишком широкая рамка различие между agent architecture и agent deployment setup?

## Связанные страницы
- [weeks/week-04](../weeks/week-04.md)
- [sources/evaluation-benchmarking-llm-agents-survey](evaluation-benchmarking-llm-agents-survey.md)
- [sources/react-synergizing-reasoning-acting](react-synergizing-reasoning-acting.md)
