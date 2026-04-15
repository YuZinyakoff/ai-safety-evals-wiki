# Limits To Scalable Evaluation At The Frontier

- **Тип источника:** extra
- **Неделя:** week-03
- **Raw:** [clipped `.md`](<../../raw/week-03/extra/Limits to scalable evaluation at the frontier LLM as Judge won’t beat twice the data.md>), [TeX source](<../../raw/week-03/extra/arXiv-2410.13341v3.tar.gz>)
- **Оригинал:** [OpenReview](https://openreview.net/forum?id=NO6Tv6QcDs)
- **Полнота raw:** clipped Markdown и TeX source

## Ключевая мысль
> **На evaluation frontier judge-based debiasing не дает почти бесплатной масштабируемой оценки.** Если judge не лучше оцениваемой модели, выигрыш по ground-truth labels ограничен примерно двукратным фактором.

## Зачем источник в базе
Это самый строгий антихайповый текст недели про `LLM-as-a-judge`. Он нужен, чтобы не спутать факт “judge иногда полезен” с более сильным и часто подразумеваемым claim “judge почти решает проблему масштабируемой оценки frontier-моделей”.

## Эпистемический статус и как на него смотреть
Это theory-plus-empirics critique of judge-based evaluation at the frontier, а не anti-judge manifesto. Его полезно читать как paper про statistical ceiling judge-debiasing, а не как отрицание любой полезности automated judges.

## На какие вопросы источник помогает отвечать
- Почему high agreement judge'а с ground truth не гарантирует cheap scalable evaluation?
- Что authors называют структурным limit judge-based debiasing at the frontier?
- Когда proxy judgments помогают меньше, чем интуитивно обещает hype?
- Как empirical results on MMLU and MT-Bench соотносятся с theoretical claim?

## Краткое содержание
Paper формализует ситуацию, в которой model-as-judge дает дешевые proxy scores, а human / expert labels остаются дорогим ground truth. Сначала авторы показывают, что judge bias может серьезно искажать rankings, даже если agreement judge'а выглядит высоким. Затем работа вводит debiasing setup, близкий к `prediction-powered inference`: небольшое количество ground-truth labels используется для корректировки большого числа cheap proxy judgments. После этого paper приходит к главному теоретическому результату: когда judge model не лучше evaluated model, correlation between proxy and ground truth не позволяет сэкономить больше чем примерно вдвое по объему ground-truth data. В финале авторы проверяют это эмпирически на MMLU и MT-Bench и показывают, что на практике выигрыш часто еще скромнее.

## Структура материала
- `Abstract`, `1 Introduction`, `1.1 Our contributions`: постановка main claim.
- `2 Formal setup and motivation`: judge bias и почему high agreement rate insufficient.
- `3 Debiasing LLM judgments`: PPI, sample efficiency factor `tau` и theoretical limits.
- `4 Going beyond binary evaluation`: расширение beyond the binary case плюс experiments on `MMLU`.
- `5 Related work` и `6 Discussion`: positioning and implications.
- Appendices: дополнительные proofs и experiment details.

## Как читать источник быстро
- Если нужен главный результат, читай `Abstract`, `1 Introduction` и затем `2 Formal setup and motivation`.
- Если интересует mechanism, основной раздел — `3 Debiasing LLM judgments`.
- Если нужен reality check, не пропускай `3.7 Experiments` и `4 Going beyond binary evaluation`.

## Что источник утверждает прямо
- Высокий agreement proxy judge'а с ground truth сам по себе не гарантирует cheap scalable evaluation.
- В debiasing setup authors получают главный результат: если judge model не лучше evaluated model, выигрыш по числу дорогих ground-truth labels ограничен примерно двукратным фактором.
- Frontier evaluation особенно сложна, потому что оцениваемая модель может быть сильнее judge model.
- Empirical results на MMLU и MT-Bench согласуются с теоретическим claim и показывают, что практический выигрыш часто еще меньше.

## Что здесь особенно важно
- **Agreement rate** сам по себе ничего надежного не гарантирует о usefulness judge'а.
- **Debiasing** помогает, но не отменяет structural limit frontier evaluation.
- **Proxy scores** легко выглядят дешевыми и удобными, но их bias model-dependent.
- **Frontier case** принципиально сложнее, потому что judged model может быть лучше judge model.

## Интерпретация для курса
Для курса этот paper важен как строгий антихайповый corrective к judge optimism. Он помогает удерживать дисциплину вывода: `LLM-as-a-judge` иногда полезен как proxy, но это совсем не то же самое, что “judge решает проблему frontier evaluation”.

## Что это добавляет к теме недели
Этот paper делает разговор о `LLM-as-a-judge` заметно трезвее. Если MT-Bench paper показывает, почему judge-based evaluation выглядит привлекательной, то здесь становится ясно, почему эта привлекательность резко падает именно там, где оценка особенно нужна: на frontier и в tight model comparisons.

## Что стоит запомнить при повторении
- **Judge can help, but judge cannot magically replace ground truth at the frontier.**
- **Высокий agreement не равен low bias.**
- **Scalable evaluation** — это не только engineering problem, но и statistical limitation.

## Связанные концепты
- [concepts/llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [concepts/statistical-rigor-in-evals](../concepts/statistical-rigor-in-evals.md)
- [concepts/benchmarking](../concepts/benchmarking.md)

## Что осталось неясным / спорным
- Какие practical regimes judge-based evaluation все же улучшает materially, если речь не о frontier, а о weaker baselines или narrower tasks?
- Какие hybrid protocols между ground truth и proxy judgments дают лучший cost-quality trade-off на практике?

## Связанные страницы
- [weeks/week-03](../weeks/week-03.md)
- [sources/llm-as-a-judge-mt-bench-chatbot-arena](llm-as-a-judge-mt-bench-chatbot-arena.md)
- [sources/no-free-labels-llm-as-a-judge](no-free-labels-llm-as-a-judge.md)
- [sources/hardt-emerging-science-ml-benchmarks](hardt-emerging-science-ml-benchmarks.md)
