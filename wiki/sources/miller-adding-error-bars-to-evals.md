# Adding Error Bars To Evals

- Тип источника: theory
- Неделя: week-02
- Raw: `raw/week-02/theory/2411.00640v1.pdf`
- Оригинал: https://arxiv.org/abs/2411.00640
- Полнота raw: PDF статьи

## Зачем источник в базе
Это опорный текст недели для статистической части evals. Он нужен, чтобы не читать benchmark score как самодостаточный результат и помнить, что language model evaluation надо рассматривать как эксперимент с шумом, неопределенностью и ограниченной мощностью.

## Краткое содержание
Статья Evan Miller предлагает смотреть на LLM evals через обычную статистическую оптику: как на эксперимент, в котором мы наблюдаем конечную выборку вопросов из более широкого распределения задач. Из этого следуют практические инструменты: standard error, confidence intervals, сравнение двух моделей через paired analysis, power analysis и minimum detectable effect. Текст не спорит с тем, что benchmark scores полезны, но показывает, что без error bars, size-of-effect и sample-size reasoning такие scores слишком легко переоценить.

## Ключевые идеи
- Point estimate без uncertainty estimate почти всегда недостаточен.
- Evals полезно мыслить как выборку из более широкой `super-population` вопросов.
- Если две модели отвечают на один и тот же набор вопросов, paired analysis сильнее простого сравнения средних.
- Confidence intervals и effect size часто информативнее, чем один p-value.
- До запуска eval полезно считать power и minimum detectable effect.

## Опорные тезисы из источника
- Статья прямо называет evals experiments и переносит на них стандартную статистическую дисциплину.
- Для single-model accuracy предлагается считать uncertainty через standard error и confidence interval.
- Для comparison between models полезно различать unpaired и paired analysis.
- Когда обе модели решают одни и те же вопросы, можно уменьшить noise за счет per-question differences.
- В тексте отдельно обсуждаются sample size planning и minimum detectable effect как практические инструменты для design decisions.
- Повторные прогоны и число вопросов влияют на uncertainty по-разному, поэтому их нельзя считать взаимозаменяемыми.
- В worked examples автор показывает, что "лучший score" не всегда означает statistically meaningful improvement.

## Что это добавляет к теме недели
Этот источник переводит разговор недели из режима "какие benchmark scores мы получили?" в режим "какой вывод из этих scores вообще оправдан?". Он особенно полезен в связке с notebook, потому что там идеи статьи operationalize на MMLU subset, `EvalLog`, DataFrame, confidence intervals и paired t-tests. Для повторения курса это одна из страниц, которая поднимает technical bar и напоминает: у хорошего eval есть не только task и scorer, но и честная статистическая интерпретация.

## Связанные концепты
- [concepts/evals](../concepts/evals.md)
- [concepts/benchmarking](../concepts/benchmarking.md)
- [concepts/statistical-rigor-in-evals](../concepts/statistical-rigor-in-evals.md)
- [concepts/inspect-ai](../concepts/inspect-ai.md)

## Что осталось неясным / спорным
- Насколько хорошо эти statistical assumptions переносятся на open-ended evals и richer human-judged settings?
- Когда CLT-style approximations уже недостаточны и нужны более robust или clustered methods?

## Связанные страницы
- [weeks/week-02](../weeks/week-02.md)
- [sources/inspect-ai-tutorial-week-02](inspect-ai-tutorial-week-02.md)
- [syntheses/benchmarking-beyond-single-scores](../syntheses/benchmarking-beyond-single-scores.md)
