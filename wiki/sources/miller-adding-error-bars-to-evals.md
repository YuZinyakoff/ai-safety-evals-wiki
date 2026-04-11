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

## Краткое содержание
Статья Miller устроена как попытка перенести обычную статистическую дисциплину на LLM evals. В начале paper задает общую рамку: evaluation questions стоит мыслить как выборку из более широкой `super-population`, а значит score сам по себе — это estimate, а не self-explanatory truth. Затем автор шаг за шагом разбирает базовый statistical toolkit: `standard error`, `confidence intervals` и различие между `unpaired` и `paired analysis` для сравнения моделей. После этого paper добавляет практические extensions: clustered questions, variance reduction через resampling и next-token probabilities, а в финальной части переходит к `power analysis` и `minimum detectable effect` как инструментам планирования eval до запуска. За счет такой структуры текст полезен не только как набор формул, но и как более строгий стандарт чтения benchmark results.

## Что здесь особенно важно
- **Point estimate почти всегда недостаточен.**
- **`Paired analysis`** особенно важен, когда две модели решают одни и те же вопросы.
- **`n` и `K`** уменьшают uncertainty по-разному и не взаимозаменяемы.
- **Power analysis** нужен до запуска expensive eval, а не только после.
- **Error bars** не делают benchmark идеальным, но хотя бы ограничивают силу вывода тем, что данные реально поддерживают.

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
