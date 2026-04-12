# Agent Evals Beyond Task Success

## Короткий тезис
> **Week-04 показывает, что хороший agent eval должен одновременно отвечать хотя бы на три разных вопроса:** что агент умеет, насколько надежно он это делает и насколько измеренный результат занижен или искажен самой процедурой оценки.

## Где источники согласны
- **Task success остается полезным, но недостаточным.** Ни один из ключевых текстов недели не предлагает полностью отказаться от success metrics.
- **Agent evaluation шире model evaluation.** Все основные источники сходятся в том, что tools, trajectories, environments и repeated runs делают problem space сложнее.
- **Процедура оценки сама влияет на результат.** Это видно и в elicitation discussion у METR, и в benchmark-quality discussion вокруг SWE-bench Verified.
- **Deployment-relevant interpretation требует дополнительных слоев evidence.** Обычный benchmark score слишком слаб, если речь идет о consequential agent behavior.

## Как источники усиливают друг друга
- **LLM Agents Survey** задает широкую карту поля и отделяет `what to evaluate` от `how to evaluate`.
- **Princeton reliability paper** делает карту строже и показывает, какие важные свойства исчезают при сведении оценки к одному success rate.
- **METR elicitation guidelines** добавляют еще один уровень: measured score может быть сильным under-estimate, если процедура плохо раскрывает capability.
- **Anthropic autonomy in practice** переносит разговор из lab settings в deployment and monitoring layer.
- **SWE-bench и SWE-bench Verified** показывают, что benchmark quality control тоже влияет на итоговый capability claim.
- **Notebook и ReAct** связывают весь спор с concrete scaffolding decisions, а не только с высокоуровневой методологией.

## Что именно ломает наивный вывод
- **Сначала benchmark или protocol выбирает, что считать evidence.**
- **Потом scaffolding влияет на то, какие capabilities вообще проявятся.**
- **Затем aggregate success score прячет consistency, robustness и failure severity.**
- **И наконец deployment reality может сильно отличаться от lab setup.**

Именно поэтому фраза "агент набрал X%" без уточнения evaluation setup почти всегда говорит слишком мало.

## Где остается напряжение
- **As-is evaluation vs elicited performance.** Если делать слишком слабый setup, мы занижаем capability; если слишком сильный — рискуем потерять comparability и realism.
- **Product-like setup vs maximal capability probing.** Для deployment questions и for capability forecasting могут быть нужны разные protocols.
- **Single benchmark vs richer profile.** Богатый reliability profile полезнее, но сложнее для коммуникации и сравнения.
- **Pre-deployment vs post-deployment evidence.** Benchmarking удобно и воспроизводимо, а monitoring ближе к реальности, но хуже контролируется.

## Практическая дисциплина после этой недели
После любого claim про agent performance полезно спрашивать:
- **Что именно здесь оценивали: behavior, capability, reliability, safety or autonomy?**
- **Какой scaffolding и какой elicitation level использовались?**
- **Можно ли failure читать как capability limit, или это скорее artifact процедуры?**
- **Какие свойства результата скрыты за средним score?**
- **Что изменится, если смотреть не на lab run, а на deployment behavior?**

## Открытые вопросы
- Как строить autonomy evals, которые одновременно realistic, reproducible и not-too-gameable?
- Какие elicitation standards нужны, чтобы scores across labs оставались сравнимыми?
- Как лучше сочетать benchmark evidence, reliability profiling и post-deployment monitoring?

## Связанные страницы
- [weeks/week-04](../weeks/week-04.md)
- [concepts/agent-evaluation](../concepts/agent-evaluation.md)
- [concepts/agent-reliability](../concepts/agent-reliability.md)
- [concepts/capability-elicitation](../concepts/capability-elicitation.md)
- [concepts/agent-autonomy](../concepts/agent-autonomy.md)
