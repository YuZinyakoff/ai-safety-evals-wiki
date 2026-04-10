# Inspect AI

## Что это такое
Inspect AI — это framework для построения и запуска evaluations через явную структуру `Task`, в которой отдельно задаются dataset, solver и scorer. На первых неделях курса он важен как инструмент, который переводит обсуждение evals из уровня общих идей в воспроизводимые эксперименты и анализ результатов.

## Почему это важно в курсе
Без практического слоя разговор про evals легко остается слишком абстрактным. В week-01 `Inspect AI` нужен, чтобы собрать базовый eval pipeline. В week-02 он уже нужен для более взрослой задачи: не только запустить benchmark, но и дойти от `EvalLog` до confidence intervals, paired comparisons и power-aware interpretation.

## Что видно по источникам
- [sources/inspect-ai-tutorial-week-01](../sources/inspect-ai-tutorial-week-01.md) использует `Task`, `Sample`, solver pipeline и scorer как базовые сущности.
- [sources/inspect-ai-tutorial-week-01](../sources/inspect-ai-tutorial-week-01.md) показывает built-in components вроде `system_message`, `prompt_template`, `chain_of_thought`, `multiple_choice`, `match`, `exact`, `pattern` и `choice`.
- [sources/inspect-ai-tutorial-week-01](../sources/inspect-ai-tutorial-week-01.md) отдельно вводит `inspect view` как UI для анализа логов evaluations.
- [sources/apollo-starter-guide-evals](../sources/apollo-starter-guide-evals.md) подчеркивает важность tooling и engineering skillset для evaluators.
- [sources/inspect-ai-tutorial-week-02](../sources/inspect-ai-tutorial-week-02.md) показывает, как превращать `EvalLog` в DataFrame и связывать benchmark run со statistical analysis.
- [sources/inspect-ai-tutorial-week-02](../sources/inspect-ai-tutorial-week-02.md) использует MMLU, paired t-test, confidence intervals, power analysis и sample-size planning как часть одного workflow.

## Как этим пользоваться при повторении
- Inspect AI полезно держать как concrete implementation layer для идей из недели: как из разговора про elicitation и benchmarking перейти к воспроизводимым tasks.
- Framework также делает видимыми места, где возникают measurement choices: prompt templates, solver chains, scoring rules, metadata и analysis workflows.
- Если нужно быстро вернуть практическую часть недели, почти всегда стоит начинать отсюда и с notebook source page.
- Для week-02 особенно важно помнить, что `Inspect AI` полезен не только до запуска eval, но и после него: через `EvalLog`, post-processing и model comparison.

Для повторения курса это особенно полезно, потому что Inspect AI заземляет абстрактные споры. Он показывает, что reliability evals живет не только в больших принципах, но и в том, как именно собран pipeline и что именно мы потом смотрим в логах.

## С чем легко перепутать
- Inspect AI легко принять за сам eval, хотя это прежде всего framework и workflow layer, а не гарантия качества измерения.
- Хороший tooling не заменяет threat modeling, корректный scorer и аккуратный выбор claims, которые мы готовы делать по результатам.
- Учебный notebook не стоит читать как источник сильных эмпирических выводов: его ценность здесь в том, что он делает design choices явными и обсуждаемыми.
- Наличие удобного log object не отменяет необходимости отдельно продумывать statistical interpretation.

## Открытые вопросы
- Какие abstractions Inspect AI особенно полезны для safety evals, а какие больше подходят для учебных benchmarks?
- Как лучше связывать Inspect AI workflows с threat modeling и richer failure analysis?

## Связанные страницы
- [weeks/week-01](../weeks/week-01.md)
- [weeks/week-02](../weeks/week-02.md)
- [sources/inspect-ai-tutorial-week-01](../sources/inspect-ai-tutorial-week-01.md)
- [sources/inspect-ai-tutorial-week-02](../sources/inspect-ai-tutorial-week-02.md)
- [concepts/evals](evals.md)
- [concepts/benchmarking](benchmarking.md)
- [concepts/statistical-rigor-in-evals](statistical-rigor-in-evals.md)
- [concepts/prompt-sensitivity](prompt-sensitivity.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
- [syntheses/benchmarking-beyond-single-scores](../syntheses/benchmarking-beyond-single-scores.md)
