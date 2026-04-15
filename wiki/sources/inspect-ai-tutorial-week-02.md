# Inspect AI Tutorial Week 02

- **Тип источника:** notebook
- **Неделя:** week-02
- **Raw:** [`.ipynb`](<../../raw/week-02/notebooks/inspect_ai_tutorial_week_2.ipynb>)
- **Полнота raw:** учебный notebook

## Ключевая мысль
> **Benchmark run полезно доводить до полноценного analysis workflow:** `EvalLog -> DataFrame -> uncertainty estimates -> model comparison -> sample-size planning`.

## Зачем источник в базе
Это практическая опора недели для benchmark evaluation и статистической интерпретации результатов. Ноутбук нужен не ради финального числа, а как scaffold, который показывает, как превратить benchmark run в осмысленный statistical analysis.

## Эпистемический статус и как на него смотреть
Это учебный ноутбук для анализа, а не finished benchmark report. Его полезно читать как пошаговый workflow от run logs к uncertainty estimates, model comparison и sample-size planning.

## На какие вопросы источник помогает отвечать
- Как превратить `EvalLog` в analysis-ready object, а не оставить его сырым output?
- Как confidence intervals, paired tests и power analysis встраиваются в обычный benchmark workflow?
- Почему aggregate accuracy недостаточна даже для учебного MMLU run?
- Какие planning questions стоит задавать до следующего дорогого запуска?

## Краткое содержание
Notebook устроен как постепенный tutorial по статистически более взрослому benchmarking workflow. В начале он показывает, как загрузить `MMLU`-данные, собрать `Task` в `Inspect AI` и получить `EvalLog`. Затем tutorial переводит run logs в tabular form и шаг за шагом добавляет analysis layer: `confidence intervals`, визуализацию того, как uncertainty уменьшается при росте числа вопросов и повторов, `paired comparison` двух моделей, interval estimation для разницы, `power analysis` и `required sample size`. В финальных заданиях notebook просит сравнить baseline с `chain_of_thought` и отдельно подумать про `clustered standard errors`. Это не finished experiment, а учебный каркас, который показывает, как benchmark перестает быть просто запуском модели и становится reproducible analysis pipeline.

## Как читать источник быстро
- Если нужен самый короткий маршрут, смотри sections `MMLU task -> EvalLog -> DataFrame -> confidence intervals`.
- Если интересует model comparison, переходи сразу к paired comparison and interval estimation blocks.
- Если нужен pre-run discipline layer, не пропускай power analysis, required sample size and note on clustered standard errors.

## Что здесь особенно важно
- **`EvalLog`** сам по себе уже полезный объект, но его нужно уметь переводить в analysis-ready form.
- **`n` и `K`** снижают uncertainty разными способами.
- **`Paired tests`** особенно важны для честного comparison на одном и том же question set.
- **Planning matters.** `Power analysis` и `required sample size` лучше делать до следующего дорогого запуска.
- **Notebook intentionally incomplete.** Он полезен именно как учебный scaffold с `# YOUR CODE HERE`.

## Цель ноутбука
- Превратить benchmark run в reproducible analysis workflow.
- Научиться доставать question-level data из `EvalLog`.
- Построить confidence intervals и paired comparisons для model evaluation.
- Прикинуть power and sample-size needs до следующего запуска.

## Setup
- **Среда:** Python 3 / Jupyter notebook.
- **Инструмент:** `Inspect AI`.
- **Dataset family:** `MMLU`.
- **Режим работы:** analysis-oriented tutorial with `# YOUR CODE HERE`.

## Данные / задача / модели / scorer
- **Задача:** benchmark evaluation on `MMLU`.
- **Основные объекты:** `Task`, `EvalLog`, `DataFrame` with question-level outcomes.
- **Analysis blocks:** confidence intervals, paired model comparison, interval estimation, power analysis, required sample size.
- **Interventions:** comparison of baseline and `chain_of_thought`; note on clustered standard errors.

## Что это добавляет к теме недели
Этот notebook делает week-02 practically useful. Он связывает taxonomy evals, benchmark practice и statistical rigor в один workflow: dataset, task, run, log extraction, uncertainty estimation, model comparison и planning следующего эксперимента. Для повторения курса это очень полезная страница, если нужно помнить не только abstract principles, но и concrete order of operations.

## Что стоит запомнить при повторении
- **Не останавливаться на aggregate accuracy.**
- **Question-level data** часто важнее, чем кажется по одному финальному score.
- **Хороший benchmark workflow** включает и запуск, и анализ, и планирование следующего запуска.

## Результаты и ограничения
- Notebook является учебным scaffold, а не finished benchmark report.
- Основной результат здесь методический: pipeline from run logs to statistically disciplined interpretation.
- Несколько шагов оставлены как упражнения / `# YOUR CODE HERE`.
- Выводы завязаны на `MMLU`-style multiple-choice setting и не переносятся автоматически на richer eval regimes.

## Связанные концепты
- [concepts/inspect-ai](../concepts/inspect-ai.md)
- [concepts/benchmarking](../concepts/benchmarking.md)
- [concepts/statistical-rigor-in-evals](../concepts/statistical-rigor-in-evals.md)

## Что осталось неясным / спорным
- Насколько выводы из `MMLU` subset переносятся на другие subjects, benchmark families и open-ended tasks?
- Какие parts of analysis стоит менять, если scorer уже не бинарный и задача не multiple-choice?

## Связанные страницы
- [weeks/week-02](../weeks/week-02.md)
- [sources/miller-adding-error-bars-to-evals](miller-adding-error-bars-to-evals.md)
- [syntheses/benchmarking-beyond-single-scores](../syntheses/benchmarking-beyond-single-scores.md)
