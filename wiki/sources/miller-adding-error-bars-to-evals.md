# Adding Error Bars To Evals

- **Тип источника:** theory
- **Неделя:** week-02
- **Raw:** [HTML-clipped `.md`](<../../raw/week-02/theory/Adding Error Bars to Evals A Statistical Approach to Language Model Evaluations.md>), [PDF](<../../raw/week-02/theory/2411.00640v1.pdf>), [TeX source](<../../raw/week-02/theory/arXiv-2411.00640v1.tar.gz>)
- **Оригинал:** [arXiv](https://arxiv.org/abs/2411.00640)
- **Полнота raw:** сильный raw-набор: clipped HTML, PDF и TeX source

## Ключевая мысль
> **LLM eval нужно читать как эксперимент с шумом и ограниченной выборкой, а не как одно число на лидерборде.**

## Зачем источник в базе
Это опорный текст недели для статистической части evals. Он нужен, чтобы не читать benchmark score как самодостаточный результат и помнить, что language model evaluation надо рассматривать как эксперимент с неопределенностью, sampling assumptions и ограниченной мощностью.

## Эпистемический статус и как на него смотреть
Это methodological statistics paper, а не очередной benchmark result paper. Его лучше читать как попытку привить LLM evals нормальную experimental discipline, а не как набор формул ради формул.

## На какие вопросы источник помогает отвечать
- Почему benchmark score лучше понимать как estimate, а не verdict?
- Когда нужен `paired analysis`, а когда хватает unpaired comparison?
- Как `standard error`, `confidence intervals`, `power` и `MDE` входят в LLM eval practice?
- Что меняется, если вопросы clustered или repeated runs добавляют дополнительную структуру шума?

## Краткое содержание
Статья Miller устроена как попытка перенести обычную статистическую дисциплину на LLM evals. В начале paper задает общую рамку: evaluation questions стоит мыслить как выборку из более широкой `super-population`, а значит score сам по себе — это estimate, а не self-explanatory truth. Затем автор шаг за шагом разбирает базовый statistical toolkit: `standard error`, `confidence intervals` и различие между `unpaired` и `paired analysis` для сравнения моделей. После этого paper добавляет практические extensions: clustered questions, variance reduction через resampling и next-token probabilities, а в финальной части переходит к `power analysis` и `minimum detectable effect` как инструментам планирования eval до запуска. За счет такой структуры текст полезен не только как набор формул, но и как более строгий стандарт чтения benchmark results.

## Структура материала
- `1 Introduction`: почему point estimates недостаточны и зачем evals нужны `error bars`.
- `2 Analysis framework`: independent vs clustered questions.
- `3 Variance reduction`: resampling, next-token probabilities и связанные tricks.
- `4 Comparing models`: `unpaired` и `paired` analysis.
- `5 Power analysis`: planning before running the evaluation.
- `6 Conclusion` и appendices: clustered standard errors и sample-size details.

## Как читать источник быстро
- Если нужен главный сдвиг, читай `1 Introduction` и затем `2 Analysis framework`.
- Если задача про model comparison, иди прямо в `4 Comparing models`.
- Если нужен planning layer, главный раздел — `5 Power analysis`.
- Если benchmark setup richer than iid questions, не пропускай `2.2 Clustered questions` и appendices про clustered standard errors.

## Что источник утверждает прямо
- LLM evaluation results should be interpreted as statistical estimates with uncertainty, not self-explanatory facts.
- `Paired analysis` often yields stronger and more appropriate comparisons when models answer the same questions.
- Sample size, repeats and dependence structure all materially affect what conclusions the data support.
- Good eval practice includes planning around power and minimum detectable effect before expensive runs, not only after them.

## Что здесь особенно важно
- **Point estimate почти всегда недостаточен.**
- **`Paired analysis`** особенно важен, когда две модели решают одни и те же вопросы.
- **`n` и `K`** уменьшают uncertainty по-разному и не взаимозаменяемы.
- **Power analysis** нужен до запуска expensive eval, а не только после.
- **Error bars** не делают benchmark идеальным, но хотя бы ограничивают силу вывода тем, что данные реально поддерживают.

## Интерпретация для курса
В логике курса этот paper важен не как урок статистики ради статистики. Он повышает technical bar for reading benchmarks at all: after Miller, single-number reading starts looking not merely crude, but methodologically unserious for many practical evaluation claims.

## Что это добавляет к теме недели
Этот paper переводит разговор недели из режима “какие benchmark scores мы получили?” в режим “какой вывод из этих scores вообще оправдан?”. Он особенно хорошо работает в связке с notebook, потому что там идеи статьи operationalize на `MMLU`, `EvalLog`, `DataFrame`, `confidence intervals` и `paired tests`. Для повторения курса это одна из самых полезных страниц недели, если нужно поднять technical bar без потери общей логики.

## Что стоит запомнить при повторении
- **Benchmark result** полезнее читать как `estimate with assumptions`, а не как verdict.
- **`Paired differences`** часто дают более сильный и честный comparison signal, чем сравнение средних.
- **Хороший eval design** включает не только dataset и scorer, но и план статистической интерпретации.

## Связанные концепты
- [concepts/evals](../concepts/evals.md)
- [concepts/benchmarking](../concepts/benchmarking.md)
- [concepts/statistical-rigor-in-evals](../concepts/statistical-rigor-in-evals.md)
- [concepts/inspect-ai](../concepts/inspect-ai.md)

## Что осталось неясным / спорным
- Насколько хорошо эти statistical assumptions переносятся на open-ended evals и richer human-judged settings?
- Когда `CLT`-style approximations уже недостаточны и нужны более robust или clustered methods?

## Связанные страницы
- [weeks/week-02](../weeks/week-02.md)
- [sources/inspect-ai-tutorial-week-02](inspect-ai-tutorial-week-02.md)
- [syntheses/benchmarking-beyond-single-scores](../syntheses/benchmarking-beyond-single-scores.md)
