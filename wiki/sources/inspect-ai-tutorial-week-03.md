# Inspect AI Tutorial Week 03

- **Тип источника:** notebook
- **Неделя:** week-03
- **Raw:** [`.ipynb`](<../../raw/week-03/notebooks/inspect_ai_tutorial_week_3 (1).ipynb>)
- **Полнота raw:** учебный notebook

## Ключевая мысль
> **LLM judge полезно изучать не как магическую замену человеку, а как отдельный объект оценки со своими FP, FN, blind spots и prompt sensitivities.**

## Зачем источник в базе
Это практическая опора недели для разговора о toxicity evaluation и `LLM-as-a-judge`. Notebook нужен, чтобы увидеть, как benchmark design и judge design становятся конкретным evaluation pipeline: classifier, judge, blind prompt, error analysis и prompt interventions.

## Краткое содержание
Notebook построен как tutorial по созданию собственной judge-based evaluation pipeline на `Jigsaw Toxic Comment` dataset. Сначала он объясняет общую постановку: один model выступает как classifier, а второй как judge, который решает, приемлем ли этот label. Затем tutorial загружает dataset, собирает `Task` в `Inspect AI` и показывает важную деталь: judge надо делать действительно blind к ground-truth label. После первого запуска notebook переходит к error analysis и просит отдельно считать сбои classifier и judge, включая `judge_fp_rate`, `judge_fn_rate` и format failures. Дальше задания заставляют сравнить разные classifier–judge пары, посмотреть на влияние model families, попробовать prompt interventions для classifier и judge, а затем запустить “реалистичный” режим judge-based evaluation без доступа к ground truth. В конце добавляется domain-specific scoring layer и предложение перенести весь pipeline на другой dataset.

## Что здесь особенно важно
- **Judge blind spot** — это не абстрактная проблема, а конкретный prompt / scorer choice.
- **Classifier errors и judge errors** надо разносить, а не смешивать в один итоговый failure.
- **Judge reliability** зависит и от model family, и от prompt design.
- **Notebook intentionally incomplete.** Это scaffold с `# YOUR CODE HERE`, а не finished experiment.

## Что это добавляет к теме недели
Этот notebook делает week-03 инженерной. Он показывает, что вопросы про benchmark design, evidence и validity не заканчиваются на paper-level discussion: они всплывают в конкретных решениях о blind prompts, judge policy, error metrics и domain-specific scoring.

## Что стоит запомнить при повторении
- **LLM judge сам нуждается в evaluation.**
- **Blindness, refusal behavior и asymmetry between FP/FN** — практические части judge design.
- **Inspect AI** в этой неделе нужен уже не для simple benchmarking, а для judge-auditing workflow.

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
