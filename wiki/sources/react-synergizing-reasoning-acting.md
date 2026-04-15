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

## Эпистемический статус и как на него смотреть
Это agent-pattern proposal paper, а не universal proof that ReAct is best. Его полезно читать как demonstration of a scaffolding idea: how interleaving thought, action and observation changes trajectories.

## На какие вопросы источник помогает отвечать
- Что такое `ReAct` как pattern, а не как buzzword?
- Почему interleaving reasoning and acting может быть лучше, чем pure CoT or pure acting?
- Как такой loop меняет recovery from errors and use of tools?
- Почему choice of scaffolding pattern already changes what the eval is measuring?

## Краткое содержание
Работа вводит `ReAct` как паттерн, в котором модель чередует internal reasoning и external actions, а затем использует observation from tools or environment для следующего шага. Paper показывает это на нескольких task families и противопоставляет подход как чистому chain-of-thought reasoning, так и purely acting-style agents. По смыслу текст важен не отдельными числами, а тем, что он делает явным structural idea: tool result должен входить обратно в цикл принятия решений, а не просто приклеиваться к ответу.

## Как читать источник быстро
- Если нужна основная идея, читай opening explanation of thought/action/observation interleaving и contrast with other patterns.
- Если интересуют empirical examples, смотри a couple of case studies rather than all reported results.
- Если нужна relevance to the week, держи в уме не “does ReAct win”, а “what kind of trajectory structure it induces”.

## Что источник утверждает прямо
- `ReAct` организует траекторию как interleaving thought, action and observation rather than pure reasoning or pure acting.
- Такая структура может улучшать tool use, error recovery and adaptation across multi-step tasks.
- Trace visibility itself is useful for debugging and analyzing agent behavior.
- Paper демонстрирует сильный scaffolding idea, но не доказывает, что `ReAct` universally best for all tasks and agents.

## Что здесь особенно важно
- **Interleaving matters.** Разделение на thought / action / observation влияет на recovery from errors.
- **ReAct** полезен как scaffolding pattern, а не как универсальный guarantee of better performance.
- **Trace visibility** делает agent behavior легче для анализа и debugging.

## Интерпретация для курса
Для курса этот paper важен не как recipe for maximum score, а как напоминание, что scaffolding pattern is part of what the eval measures. Если один и тот же model backbone ведет себя по-разному под другим loop structure, то вывод об “агентских способностях” нельзя отделять от выбранной процедуры.

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
