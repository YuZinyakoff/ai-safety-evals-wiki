# Inspect AI Tutorial Week 02

- Тип источника: notebook
- Неделя: week-02
- Raw: `raw/week-02/notebooks/inspect_ai_tutorial_week_2.ipynb`
- Полнота raw: учебный notebook

## Зачем источник в базе
Это практическая опора недели для benchmark evaluation и статистической интерпретации результатов. Ноутбук нужен не ради готового финального числа, а как scaffold, который показывает, как превратить benchmark run в осмысленный statistical analysis.

## Краткое содержание
Notebook строится вокруг оценки моделей на MMLU через `inspect_ai`. Сначала он показывает, как загрузить dataset и собрать `Task`, затем переводит `EvalLog` в tabular form и последовательно вводит confidence intervals, визуализацию того, как uncertainty уменьшается при росте числа вопросов и числа прогонов, paired comparison двух моделей, interval estimation для разницы, power analysis и sample-size planning. В конце добавляются задания на сравнение baseline with chain-of-thought и bonus про clustered standard errors. Важная особенность: ноутбук не исполнен до конца и содержит `# YOUR CODE HERE`, поэтому это именно учебный каркас.

## Ключевые идеи
- Benchmark run полезно доводить до `EvalLog -> DataFrame -> statistical analysis`, а не останавливаться на aggregate accuracy.
- `n` и `K` делают разную работу: больше вопросов и больше повторов уменьшают uncertainty разными способами.
- При сравнении моделей на одном и том же наборе вопросов paired analysis сильнее простого сравнения средних.
- Power analysis и required sample size стоит делать до дорогого eval, а не после.
- `Inspect AI` здесь служит не только runner, но и инфраструктурой для честного анализа benchmark results.

## Опорные тезисы из источника
- Notebook использует `hf_dataset` для загрузки `cais/mmlu` и приводит записи к `Sample`.
- В качестве working example предлагается subject subset, достаточно маленький для быстрых экспериментов.
- `eval()` возвращает `EvalLog`, из которого затем извлекаются результаты построчно.
- Отдельные задания реализуют `log_to_df`, basic confidence interval для accuracy и plots зависимости width CI от `K` и `n`.
- Для сравнения моделей предлагается paired t-test на per-question scores.
- В блоке power analysis используются `minimum_detectable_effect` и `required_sample_size`.
- В финальном задании предлагается сравнить один и тот же model setup baseline vs `chain_of_thought`.
- В notebook по умолчанию указаны `MODEL_A = "ollama/llama2"` и `MODEL_B = "ollama/qwen2:latest"` как учебный baseline/comparison pair.

## Что это добавляет к теме недели
Этот notebook делает week-02 practically useful. Он связывает taxonomy evals, benchmark practice и statistical rigor в один workflow: dataset, task, run, log extraction, uncertainty estimation, model comparison и planning следующего эксперимента. Для повторения курса эта страница полезна тем, что она показывает не просто "как запустить benchmark", а как не остановиться слишком рано на одном score.

## Связанные концепты
- [concepts/inspect-ai](../concepts/inspect-ai.md)
- [concepts/benchmarking](../concepts/benchmarking.md)
- [concepts/statistical-rigor-in-evals](../concepts/statistical-rigor-in-evals.md)

## Что осталось неясным / спорным
- Насколько выводы из MMLU subset переносятся на другие subjects, другие benchmark families и open-ended tasks?
- Какие parts of analysis стоит менять, если scorer уже не бинарный и задача не multiple-choice?

## Связанные страницы
- [weeks/week-02](../weeks/week-02.md)
- [sources/miller-adding-error-bars-to-evals](miller-adding-error-bars-to-evals.md)
- [syntheses/benchmarking-beyond-single-scores](../syntheses/benchmarking-beyond-single-scores.md)
