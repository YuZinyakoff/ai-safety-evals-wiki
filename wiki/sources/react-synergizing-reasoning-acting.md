# ReAct: Synergizing Reasoning And Acting In Language Models

- **Тип источника:** extra
- **Неделя:** week-04
- **Raw:** [clipped `.md`](<../../raw/week-04/extra/model Synergizing Reasoning and Acting in Language Models.md>), [PDF](<../../raw/week-04/extra/2210.03629v3.pdf>), [TeX source](<../../raw/week-04/extra/arXiv-2210.03629v3.tar.gz>)
- **Оригинал:** [OpenReview](https://openreview.net/forum?id=WE_vluYUL-X)
- **Полнота raw:** сильный raw-набор: clipped Markdown, PDF и TeX source

## Ключевая мысль
> **ReAct полезен не потому, что "делает агент умнее", а потому что по-другому организует цикл reasoning + acting.** Это меняет саму траекторию решения и делает tool use более управляемым.

## Зачем источник в базе
Этот текст нужен как conceptual background для notebook. Он помогает понять, что `ReAct` — не просто один из solver choices в `Inspect AI`, а конкретная идея о том, как interleave reasoning traces и tool actions.

## Краткое содержание
Работа вводит `ReAct` как паттерн, в котором модель чередует internal reasoning и external actions, а затем использует observation from tools or environment для следующего шага. Paper показывает это на нескольких task families и противопоставляет подход как чистому chain-of-thought reasoning, так и purely acting-style agents. По смыслу текст важен не отдельными числами, а тем, что он делает явным structural idea: tool result должен входить обратно в цикл принятия решений, а не просто приклеиваться к ответу.

## Что здесь особенно важно
- **Interleaving matters.** Разделение на thought / action / observation влияет на recovery from errors.
- **ReAct** полезен как scaffolding pattern, а не как универсальный guarantee of better performance.
- **Trace visibility** делает agent behavior легче для анализа и debugging.

## Что это добавляет к теме недели
ReAct помогает week-04 не потерять инженерный смысл. Он показывает, что agent evaluation неизбежно зависит от того, как вообще устроен цикл действий агента.

## Что стоит запомнить при повторении
- **Reasoning loop и action loop нельзя всегда оценивать отдельно.**
- **Scaffolding pattern меняет то, что агент способен показать в eval.**
- **Tool use без structured loop часто слишком хрупок.**

## Связанные концепты
- [concepts/react-agents](../concepts/react-agents.md)
- [concepts/agent-scaffolding](../concepts/agent-scaffolding.md)
- [concepts/agent-evaluation](../concepts/agent-evaluation.md)

## Что осталось неясным / спорным
- Когда `ReAct` действительно помогает, а когда просто увеличивает cost and latency?
- Насколько ReAct-подобные traces отражают "реальное" reasoning, а не только удобную форму для scaffolding?

## Связанные страницы
- [weeks/week-04](../weeks/week-04.md)
- [sources/inspect-ai-tutorial-week-04](inspect-ai-tutorial-week-04.md)
- [sources/llm-agent-survey-methodology-applications-challenges](llm-agent-survey-methodology-applications-challenges.md)
