# Inspect AI Tutorial Week 02

- **Тип источника:** notebook
- **Неделя:** week-02
- **Raw:** [`.ipynb`](<../../raw/week-02/notebooks/inspect_ai_tutorial_week_2.ipynb>)
- **Полнота raw:** учебный notebook

## Ключевая мысль
> **Benchmark run полезно доводить до полноценного analysis workflow:** `EvalLog -> DataFrame -> uncertainty estimates -> model comparison -> sample-size planning`.

## Зачем источник в базе
Это практическая опора недели для benchmark evaluation и статистической интерпретации результатов. Ноутбук нужен не ради финального числа, а как scaffold, который показывает, как превратить benchmark run в осмысленный statistical analysis.

## Краткое содержание
Notebook устроен как постепенный tutorial по статистически более взрослому benchmarking workflow. В начале он показывает, как загрузить `MMLU`-данные, собрать `Task` в `Inspect AI` и получить `EvalLog`. Затем tutorial переводит run logs в tabular form и шаг за шагом добавляет analysis layer: `confidence intervals`, визуализацию того, как uncertainty уменьшается при росте числа вопросов и повторов, `paired comparison` двух моделей, interval estimation для разницы, `power analysis` и `required sample size`. В финальных заданиях notebook просит сравнить baseline с `chain_of_thought` и отдельно подумать про `clustered standard errors`. Это не finished experiment, а учебный каркас, который показывает, как benchmark перестает быть просто запуском модели и становится reproducible analysis pipeline.

## Что здесь особенно важно
- **`EvalLog`** сам по себе уже полезный объект, но его нужно уметь переводить в analysis-ready form.
- **`n` и `K`** снижают uncertainty разными способами.
- **`Paired tests`** особенно важны для честного comparison на одном и том же question set.
- **Planning matters.** `Power analysis` и `required sample size` лучше делать до следующего дорогого запуска.
- **Notebook intentionally incomplete.** Он полезен именно как scaffold с `# YOUR CODE HERE`.

## Что это добавляет к теме недели
Этот notebook делает week-02 practically useful. Он связывает taxonomy evals, benchmark practice и statistical rigor в один workflow: dataset, task, run, log extraction, uncertainty estimation, model comparison и planning следующего эксперимента. Для повторения курса это очень полезная страница, если нужно помнить не только abstract principles, но и concrete order of operations.

## Что стоит запомнить при повторении
- **Не останавливаться на aggregate accuracy.**
- **Question-level data** часто важнее, чем кажется по одному финальному score.
- **Хороший benchmark workflow** включает и запуск, и анализ, и планирование следующего запуска.

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
