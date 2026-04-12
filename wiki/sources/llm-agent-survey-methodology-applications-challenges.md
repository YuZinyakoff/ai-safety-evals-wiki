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

## Краткое содержание
Статья строит широкий ecosystem view на `LLM agents`. Сначала она предлагает methodology-centered taxonomy и раскладывает агентские системы по осям `construction`, `collaboration` и `evolution`. Затем подробно обсуждаются role/profile definition, memory mechanisms, planning, tool use, centralized / decentralized / hybrid multi-agent architectures и разные формы self-improvement. Отдельный блок посвящен `evaluation and tools`, то есть benchmark and tooling ecosystem. Для week-04 особенно полезно то, что paper показывает: agent behavior зависит от большого числа design choices задолго до evaluation stage.

## Что здесь особенно важно
- **Object of evaluation is heterogeneous.** "Агент" — это не один класс систем.
- **Memory, planning, collaboration and evolution** меняют failure modes.
- **Evaluation questions** нельзя полностью отделить от agent methodology.

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
