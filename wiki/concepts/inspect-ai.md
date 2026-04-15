# Inspect AI

## Коротко
> **Inspect AI** — это framework для построения и запуска evaluations через явную структуру `Task`, где отдельно заданы dataset, solver и scorer. На первых неделях курса он важен как инструмент, который превращает разговор об evals в воспроизводимый рабочий процесс.

## Почему это важный концепт
Без практического слоя разговор про evals слишком легко остается на уровне общих лозунгов. `Inspect AI` нужен в этой wiki не как “любимый инструмент”, а как способ сделать design choices явными. Через него становится видно, где именно возникают prompt assumptions, scoring decisions, post-processing и interpretation.

## Что этот tool помогает увидеть
- **Eval — это pipeline.** Не один запуск модели, а явно собранная структура из dataset, solver, scorer и логов.
- **Prompt design — часть measurement.** Это особенно важно в связке с week-01.
- **Logs matter.** После запуска eval важна не только итоговая метрика, но и просмотр того, как модель реально проходила задачу.
- **Statistical layer тоже становится явным.** На week-02 через `EvalLog` и post-processing tool уже участвует в paired comparisons, confidence intervals и power analysis.
- **Judge layer тоже становится явным.** На week-03 через classifier–judge pipeline становится видно, что judge сам является measurement device со своими biases и blind spots.
- **Agent layer тоже становится явным.** На week-04 через ReAct agent, tool definitions, message limits и dev/test split становится видно, что agent eval зависит от loop structure и scaffolding не меньше, чем от самой модели.

## Как этим пользоваться при повторении
- Если нужно быстро вернуть практическую часть week-01, почти всегда стоит начинать отсюда и с notebook source page.
- Если хочется понять, где именно живут measurement assumptions, полезно смотреть на `Task` как на минимальную единицу анализа.
- Если кажется, что theoretical limits evals слишком абстрактны, `Inspect AI` помогает увидеть их в конкретном workflow.

## С чем легко перепутать
- `Inspect AI` легко принять за сам eval, хотя это framework и workflow layer, а не гарантия качества measurement.
- Хороший tooling не заменяет threat modeling, корректный scorer и аккуратный выбор claims.
- Учебный notebook не стоит читать как источник сильных empirical выводов: его ценность в том, что он делает design choices явными.

## Где смотреть дальше
- [week-01 tutorial](../sources/inspect-ai-tutorial-week-01.md) — базовая механика `Task`, prompts и scoring.
- [week-02 tutorial](../sources/inspect-ai-tutorial-week-02.md) — связь benchmark run со statistical analysis.
- [week-03 tutorial](../sources/inspect-ai-tutorial-week-03.md) — classifier–judge pipeline, toxicity evaluation и audit judge model.
- [week-04 tutorial](../sources/inspect-ai-tutorial-week-04.md) — ReAct agent, tools, dev/test split и elicitation-style iteration.
- [Prompt Sensitivity](prompt-sensitivity.md) — почему prompt layer неотделим от evaluation reliability.

## Открытые вопросы
- Какие abstractions `Inspect AI` особенно полезны для safety evals, а какие больше подходят для учебных benchmarks?
- Как лучше связывать `Inspect AI` workflows с richer failure analysis и threat modeling?

## Связанные страницы
- [concepts/evals](evals.md)
- [concepts/prompt-sensitivity](prompt-sensitivity.md)
- [concepts/statistical-rigor-in-evals](statistical-rigor-in-evals.md)
- [concepts/llm-as-a-judge](llm-as-a-judge.md)
- [concepts/agent-scaffolding](agent-scaffolding.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
- [syntheses/benchmarking-beyond-single-scores](../syntheses/benchmarking-beyond-single-scores.md)
