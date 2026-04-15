# Inspect AI Tutorial Week 03

- **Тип источника:** notebook
- **Неделя:** week-03
- **Raw:** [`.ipynb`](<../../raw/week-03/notebooks/inspect_ai_tutorial_week_3 (1).ipynb>)
- **Полнота raw:** учебный notebook

## Ключевая мысль
> **LLM judge полезно изучать не как магическую замену человеку, а как отдельный объект оценки со своими FP, FN, blind spots и prompt sensitivities.**

## Зачем источник в базе
Это практическая опора недели для разговора о toxicity evaluation и `LLM-as-a-judge`. Notebook нужен, чтобы увидеть, как benchmark design и judge design становятся конкретным evaluation pipeline: classifier, judge, blind prompt, error analysis и prompt interventions.

## Эпистемический статус и как на него смотреть
Это учебный notebook-scaffold for judge auditing, а не finished experiment. Его полезно читать как пошаговый разбор того, как `LLM-as-a-judge` превращается в concrete classifier-judge pipeline with its own failure modes.

## На какие вопросы источник помогает отвечать
- Как practically устроить judge-based evaluation pipeline в `Inspect AI`?
- Почему judge должен быть blind к ground truth и как это влияет на reliability?
- Как разнести classifier failures и judge failures вместо одного общего score?
- Где prompt interventions и model choice реально меняют judging behavior?

## Краткое содержание
Notebook построен как tutorial по созданию собственной judge-based evaluation pipeline на `Jigsaw Toxic Comment` dataset. Сначала он объясняет общую постановку: один model выступает как classifier, а второй как judge, который решает, приемлем ли этот label. Затем tutorial загружает dataset, собирает `Task` в `Inspect AI` и показывает важную деталь: judge надо делать действительно blind к ground-truth label. После первого запуска notebook переходит к error analysis и просит отдельно считать сбои classifier и judge, включая `judge_fp_rate`, `judge_fn_rate` и format failures. Дальше задания заставляют сравнить разные classifier–judge пары, посмотреть на влияние model families, попробовать prompt interventions для classifier и judge, а затем запустить “реалистичный” режим judge-based evaluation без доступа к ground truth. В конце добавляется domain-specific scoring layer и предложение перенести весь pipeline на другой dataset.

## Как читать источник быстро
- Если нужен самый короткий маршрут, смотри setup of classifier and judge, затем blind-prompt requirement и первый run.
- Если интересует reliability layer, переходи к error analysis with `judge_fp_rate`, `judge_fn_rate` and format failures.
- Если нужен практический экспериментальный слой, смотри blocks on model-family comparisons, prompt interventions и domain-specific scoring.

## Что здесь особенно важно
- **Judge blind spot** — это не абстрактная проблема, а конкретный prompt / scorer choice.
- **Classifier errors и judge errors** надо разносить, а не смешивать в один итоговый failure.
- **Judge reliability** зависит и от model family, и от prompt design.
- **Notebook intentionally incomplete.** Это учебный scaffold с `# YOUR CODE HERE`, а не законченный experiment.

## Цель ноутбука
- Собрать classifier-judge pipeline в `Inspect AI`.
- Понять, как устроен blind judging without access to ground truth.
- Разделить classifier failures и judge failures.
- Протестировать prompt and model interventions for judge reliability.

## Setup
- **Среда:** Python 3 / Jupyter notebook.
- **Инструмент:** `Inspect AI`.
- **Dataset:** `Jigsaw Toxic Comment`.
- **Режим:** учебный scaffold with incomplete cells и guided experiments.

## Данные / задача / модели / scorer
- **Основная задача:** toxicity classification plus judge-based verification.
- **Pipeline:** classifier model, judge model, blind prompt, error analysis.
- **Метрики:** `judge_fp_rate`, `judge_fn_rate`, format failures и связанные comparison slices.
- **Эксперименты:** model-family comparisons, prompt interventions, domain-specific scoring и transfer to another dataset.

## Что это добавляет к теме недели
Этот notebook делает week-03 инженерной. Он показывает, что вопросы про benchmark design, evidence и validity не заканчиваются на paper-level discussion: они всплывают в конкретных решениях о blind prompts, judge policy, error metrics и domain-specific scoring.

## Что стоит запомнить при повторении
- **LLM judge сам нуждается в evaluation.**
- **Blindness, refusal behavior и asymmetry between FP/FN** — практические части judge design.
- **Inspect AI** в этой неделе нужен уже не для simple benchmarking, а для judge-auditing workflow.

## Результаты и ограничения
- Notebook intentionally incomplete and contains `# YOUR CODE HERE`.
- Основной выход здесь не финальный score, а structure of the auditing workflow.
- Jigsaw gives a useful but narrow domain for judge analysis; перенос на open-ended harms не автоматический.
- Reliability conclusions depend on prompt design, model family and the chosen error decomposition.

## Связанные концепты
- [concepts/inspect-ai](../concepts/inspect-ai.md)
- [concepts/llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [concepts/toxicity-evals](../concepts/toxicity-evals.md)

## Что осталось неясным / спорным
- Насколько результаты на Jigsaw переносятся на более open-ended toxicity tasks и другие domains?
- Какие prompt interventions улучшают judge reliability, а какие просто сдвигают баланс между strictness и leniency?

## Связанные страницы
- [weeks/week-03](../weeks/week-03.md)
- [sources/jigsaw-unintended-bias-text-classification](jigsaw-unintended-bias-text-classification.md)
- [sources/llm-as-a-judge-mt-bench-chatbot-arena](llm-as-a-judge-mt-bench-chatbot-arena.md)
- [sources/no-free-labels-llm-as-a-judge](no-free-labels-llm-as-a-judge.md)
