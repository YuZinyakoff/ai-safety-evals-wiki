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

## Как читать источник быстро
- Если нужен high-level map, читай taxonomy around `construction`, `collaboration` and `evolution`.
- Если вопрос про specific agent properties, переходи к sections on memory, planning, tool use and multi-agent architectures.
- Если интересует direct relevance to the week, смотри evaluation-and-tools block and use it as bridge back to agent eval papers.

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
