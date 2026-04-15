# METR’s Autonomy Evaluation Resources

- **Тип источника:** extra
- **Неделя:** week-04
- **Raw:** [clipped `.md`](<../../raw/week-04/extra/Resources.md>)
- **Оригинал:** [METR](https://evaluations.metr.org/)
- **Полнота raw:** хороший web-clipped Markdown

## Ключевая мысль
> **METR предлагает не один paper, а связанный stack для autonomy evaluation.** Важен не только elicitation protocol, но и то, как task suite, workbench, example protocol и research on elicitation impact собираются в единую систему.

## Зачем источник в базе
Эта страница нужна как карта METR ecosystem around autonomy evals. Она помогает не читать `Guidelines for capability elicitation` изолированно, а видеть, из каких еще частей состоит их общий подход.

## Эпистемический статус и как на него смотреть
Это resource hub and ecosystem map, а не single research paper. Его лучше читать как index of a measurement stack: tasks, workbench, protocol, elicitation research and example workflows.

## На какие вопросы источник помогает отвечать
- Из каких компонентов на самом деле состоит METR-style autonomy evaluation?
- Почему task suite, workbench and elicitation research стоит читать вместе?
- Что делает этот stack больше, чем просто benchmark?
- Какие pieces useful even if you are not adopting the whole METR ecosystem?

## Краткое содержание
Resource page описывает набор связанных компонентов для оценки potentially dangerous autonomous capabilities. Сначала идет `task suite`: задачи с human-time difficulty estimates, quality indicators и упором на domains, где frontier models уже сравнительно сильны. Затем описываются `guidelines for capability elicitation`, `task standard and workbench`, `example evaluation protocol` и исследовательский блок `measuring the impact of elicitation`. Важен общий смысл: METR пытается построить не просто benchmark, а целый measurement stack, где tasks, scaffolding, protocol and interpretation layer поддерживают друг друга.

## Как читать источник быстро
- Если нужен map of the stack, просто пройди top-level components: task suite, guidelines, workbench, example protocol and elicitation research.
- Если вопрос про methodology, смотри сначала links around elicitation and example evaluation protocol.
- Если нужен engineering layer, концентрируйся на task standard and workbench as infrastructure pieces.

## Что здесь особенно важно
- **Task suite** здесь связан с difficulty estimates and human-time framing.
- **Workbench** показывает, что evaluation infrastructure — не второстепенная деталь.
- **Impact of elicitation** добавляет empirical слой к методическим рекомендациям.

## Что это добавляет к теме недели
Эта страница расширяет METR guidelines до системы. Она помогает лучше увидеть, что autonomy evals требуют не только хорошего текста про elicitation, но и связки tasks, tooling, reporting and validation checks.

## Что стоит запомнить при повторении
- **Autonomy eval stack** состоит не из одного benchmark.
- **Task suite, scaffolding and protocol** стоит читать вместе.
- **METR openly treats current resources as beta.**

## Связанные концепты
- [concepts/capability-elicitation](../concepts/capability-elicitation.md)
- [concepts/agent-evaluation](../concepts/agent-evaluation.md)
- [concepts/agent-autonomy](../concepts/agent-autonomy.md)

## Что осталось неясным / спорным
- Насколько этот stack масштабируется вне teams, похожих на сам METR?
- Какие части autonomy evaluation stack наиболее критичны, если ресурсов мало?

## Связанные страницы
- [weeks/week-04](../weeks/week-04.md)
- [sources/metr-guidelines-capability-elicitation](metr-guidelines-capability-elicitation.md)
- [sources/measuring-ai-agent-autonomy-practice](measuring-ai-agent-autonomy-practice.md)
