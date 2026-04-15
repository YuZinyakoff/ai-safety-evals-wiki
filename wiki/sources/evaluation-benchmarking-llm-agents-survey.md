# Evaluation And Benchmarking Of LLM Agents: A Survey

- **Тип источника:** theory
- **Неделя:** week-04
- **Raw:** [clipped `.md`](<../../raw/week-04/theory/Evaluation and Benchmarking of LLM Agents A Survey.md>), [PDF](<../../raw/week-04/theory/2507.21504v1.pdf>), [TeX source](<../../raw/week-04/theory/arXiv-2507.21504v1.tar.gz>)
- **Оригинал:** [arXiv](https://arxiv.org/abs/2507.21504)
- **Полнота raw:** сильный raw-набор: clipped Markdown, PDF и TeX source

## Ключевая мысль
> **Оценка агентов — это уже не просто benchmarking ответов модели.** Поле приходится раскладывать по двум осям: `what to evaluate` и `how to evaluate`, потому что агентское поведение складывается из целей, траекторий, инструментов, среды и форм взаимодействия.

## Зачем источник в базе
Это главный обзорный текст недели. Он нужен как карта problem space: какие свойства агентов вообще хотят измерять, какие evaluation processes для этого используют и почему agent evaluation пока остается фрагментированной областью. Без этой страницы week-04 легко распадается на набор отдельных тем вроде reliability, elicitation и autonomy.

## Эпистемический статус и как на него смотреть
Это broad survey and taxonomy paper, а не нормативный standard for agent evaluation. Его полезно читать как map of the problem space: он помогает ориентироваться в `what to evaluate` and `how to evaluate`, но не закрывает methodological disputes.

## На какие вопросы источник помогает отвечать
- Что именно вообще можно считать объектом agent evaluation?
- Почему authors разводят `what to evaluate` и `how to evaluate`?
- Какие evaluation objectives beyond task success становятся центральными для агентов?
- Почему context, tooling and interaction mode нельзя считать merely implementation details?

## Краткое содержание
Статья устроена как широкий survey по области agent evaluation. Сначала авторы объясняют, почему стандартные LLM evals плохо переносятся на агента, который действует в динамической среде, использует tools и может идти по длинной траектории. Затем paper вводит двухмерную taxonomy: по оси `evaluation objectives` обсуждаются `behavior`, `capabilities`, `reliability` и `safety`; по оси `evaluation process` — `interaction modes`, `datasets and benchmarks`, `metrics`, `tooling` и `contexts`. После этого текст проходит по каждому блоку подробнее: чем task completion отличается от оценки planning, tool use, memory или multi-agent collaboration; почему для агентов важны both offline and online evaluation; какие benchmark families и tooling ecosystems уже существуют; и какие enterprise-specific constraints вроде RBAC, compliance и long-term interaction field пока плохо закрывает. Paper больше полезен как карта и vocabulary, чем как законченный стандарт.

## Как читать источник быстро
- Если нужен общий frame, читай introduction and the two-axis taxonomy around `evaluation objectives` and `evaluation process`.
- Если вопрос про concrete agent properties, переходи к sections on behavior, capabilities, reliability and safety.
- Если нужен practical benchmarking layer, смотри parts on benchmarks, metrics, tooling and context constraints.

## Что здесь особенно важно
- **Что оценивать** и **как оценивать** здесь разделены явно, и это помогает не путать target of evaluation с самой процедурой.
- **Task completion** в survey остается важной метрикой, но уже не выглядит достаточной.
- **Reliability** и **safety** здесь выведены в отдельные evaluation objectives, а не прячутся внутри одного общего score.
- **Tooling и context** становятся частью evaluation process, а не просто engineering details.

## Что это добавляет к теме недели
Этот текст задает базовую структуру всей недели. На его фоне Princeton paper можно читать как углубление блока `reliability`, а METR — как сильное вмешательство в блок `how to evaluate`, особенно там, где процедура сама начинает влиять на измеряемый результат.

## Что стоит запомнить при повторении
- **Agent evaluation шире, чем benchmarking answer quality.**
- **Нужно различать evaluation objective и evaluation process.**
- **Agent behavior без учета context, tooling и interaction mode легко интерпретировать слишком грубо.**

## Связанные концепты
- [concepts/agent-evaluation](../concepts/agent-evaluation.md)
- [concepts/agent-reliability](../concepts/agent-reliability.md)
- [concepts/agent-scaffolding](../concepts/agent-scaffolding.md)
- [concepts/agent-autonomy](../concepts/agent-autonomy.md)

## Что осталось неясным / спорным
- Насколько эта taxonomy реально помогает выбирать evaluation protocol, а не только описывать уже существующие практики?
- Не остается ли survey слишком описательным там, где field больше всего нуждается в методической дисциплине?

## Связанные страницы
- [weeks/week-04](../weeks/week-04.md)
- [sources/science-ai-agent-reliability](science-ai-agent-reliability.md)
- [sources/metr-guidelines-capability-elicitation](metr-guidelines-capability-elicitation.md)
- [syntheses/agent-evals-beyond-task-success](../syntheses/agent-evals-beyond-task-success.md)
