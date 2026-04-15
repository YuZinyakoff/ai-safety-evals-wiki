# METR: Guidelines For Capability Elicitation

- **Тип источника:** theory
- **Неделя:** week-04
- **Raw:** [clipped `.md`](<../../raw/week-04/theory/Guidelines for capability elicitation.md>)
- **Оригинал:** [METR](https://evaluations.metr.org/elicitation-protocol/)
- **Полнота raw:** хороший web-clipped Markdown

## Ключевая мысль
> **Плохая процедура оценки легко занижает реальные возможности агента.** Если не делать хотя бы умеренный elicitation, итоговый score может говорить больше о слабом scaffolding и неудачном prompt setup, чем о собственных capability limits модели.

## Зачем источник в базе
Это главный методический текст недели. Он нужен не как "финальный стандарт", а как concrete proposal того, как именно проводить autonomy-focused eval так, чтобы не слишком недооценить reachable performance. Через него становится ясно, что elicitation — это часть measurement discipline, а не только способ улучшить результат.

## Эпистемический статус и как на него смотреть
Это protocol proposal from METR, а не neutral description of current best practice. Его полезно читать как disciplined recipe for reducing underestimation risk, while remembering that it also encodes trade-offs about labor, overfitting risk and acceptable elicitation intensity.

## На какие вопросы источник помогает отвечать
- Почему weak scaffolding может систематически занижать measured agent capability?
- Что authors считают `basic elicitation` и чем оно отличается от over-optimization?
- Как различать `spurious bottlenecks`, `real bottlenecks` и `tradeoffs`?
- Зачем protocol требует dev set work, red flags and qualitative reporting, а не только final score?

## Краткое содержание
Документ начинается с мотивации: risk-relevant evaluation должен учитывать не только модель "как есть", но и те capabilities, которые plausibly reachable через prompting, tooling, finetuning и scaffolding. Затем METR предлагает пример процесса. Сначала делается `basic elicitation`: модель получает достаточно сильный baseline agent setup. После этого оставшиеся failures не сваливаются в одну кучу, а классифицируются как `spurious bottlenecks`, `real bottlenecks` и `tradeoffs`. Дальше документ объясняет, как работать с dev set: spurious failures надо устранять, real failures — честно пытаться улучшать, а tradeoffs — либо фиксить как локальные узкие места, либо явно считать tradeoff. Отдельный слой текста — это red flags: признаки overfitting, gaming, task-level problems и misleading score aggregation. Финал важен тем, что протокол требует не только итоговый score, но и evaluation report с qualitative failure analysis и attestation о том, что evaluators не знают простых способов резко повысить performance.

## Как читать источник быстро
- Если нужен main protocol, читай sections on `basic elicitation` and the failure taxonomy `spurious / real / tradeoff`.
- Если вопрос про methodology, переходи к dev-set workflow and red flags.
- Если нужен deployment-relevant takeaway, не пропускай reporting requirements and the final attestation logic.

## Что источник утверждает прямо
- Weak prompting, scaffolding and setup can systematically underestimate reachable agent capability.
- A reasonable evaluation protocol should include some baseline elicitation before interpreting failures as capability limits.
- Failures should be separated into `spurious bottlenecks`, `real bottlenecks` and `tradeoffs`, rather than treated as one undifferentiated class.
- Meaningful evaluation requires dev-set iteration, red-flag detection and qualitative reporting, not only final scores.

## Что здесь особенно важно
- **Reachable capabilities** важнее "чистой" performance в исходном product setup, если речь идет о safety-relevant capability measurement.
- **Spurious / real / tradeoff** — полезная рабочая тройка для классификации провалов.
- **Dev set** здесь нужен не только для tuning, но и для понимания failure structure.
- **Red flags and reporting** показывают, что meaningful evaluation — это больше, чем просто final score.

## Интерпретация для курса
Для курса METR важен как text that reframes underperformance. После него low score уже нельзя автоматически читать как evidence of low capability; сначала нужно спросить, не измерили ли мы weakness of the protocol itself. Это делает elicitation частью epistemology, а не только engineering.

## Что это добавляет к теме недели
METR делает важный epistemic сдвиг: agent evaluation может ошибаться не только из-за плохого benchmark design, но и из-за плохого elicitation protocol. Это напрямую связывает week-04 с вопросом `what the result means`.

## Что стоит запомнить при повторении
- **Не всякий failure является capability limit.**
- **Плохой scaffolding может сильно занизить measured performance.**
- **Elicitation и overfitting надо различать, а не смешивать.**

## Связанные концепты
- [concepts/capability-elicitation](../concepts/capability-elicitation.md)
- [concepts/agent-scaffolding](../concepts/agent-scaffolding.md)
- [concepts/agent-evaluation](../concepts/agent-evaluation.md)

## Что осталось неясным / спорным
- Где проходит практическая граница между честным elicitation и benchmark over-optimization?
- Насколько labor-intensive этот protocol вне небольших evaluation teams?

## Связанные страницы
- [weeks/week-04](../weeks/week-04.md)
- [sources/evaluation-benchmarking-llm-agents-survey](evaluation-benchmarking-llm-agents-survey.md)
- [sources/metr-autonomy-evaluation-resources](metr-autonomy-evaluation-resources.md)
- [syntheses/agent-evals-beyond-task-success](../syntheses/agent-evals-beyond-task-success.md)
