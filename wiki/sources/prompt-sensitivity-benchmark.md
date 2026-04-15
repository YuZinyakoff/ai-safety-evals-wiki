# Benchmarking Prompt Sensitivity In Large Language Models

- **Тип источника:** extra
- **Неделя:** week-01
- **Raw:** [HTML-clipped `.md`](<../../raw/week-01/extra/Benchmarking Prompt Sensitivity in Large Language Models.md>), [PDF](<../../raw/week-01/extra/2502.06065v1.pdf>), [TeX source](<../../raw/week-01/extra/arXiv-2502.06065v1.tar.gz>)
- **Оригинал:** [arXiv](https://arxiv.org/abs/2502.06065)
- **Полнота raw:** сильный raw-набор: clipped HTML, PDF и TeX source

## Ключевая мысль
> **Даже когда information need не меняется, observed capability может заметно меняться из-за phrasing prompt.** Это делает prompt sensitivity не бытовой темой prompt engineering, а проблемой reliability самого eval.

## Зачем источник в базе
Это полезный empirical counterweight к более общим рассуждениям про under-elicitation. Источник нужен, чтобы на конкретном benchmark-материале увидеть: observed capability зависит не только от модели, но и от того, как именно сформулирован запрос.

## Эпистемический статус и как на него смотреть
Это empirical benchmark paper, а не просто prompt-engineering advice. Его полезно читать как попытку превратить prompt sensitivity в отдельную measurement problem со своим dataset и baselines.

## На какие вопросы источник помогает отвечать
- Насколько сильно phrasing может менять observed capability при fixed information need?
- Как authors превращают prompt sensitivity в benchmarkable task?
- Что такое `PromptSET` и зачем он нужен?
- Насколько current methods умеют предсказывать, какая формулировка сработает лучше?

## Краткое содержание
Paper устроен как полноценный benchmark work, а не как короткая заметка про prompt engineering. Сначала авторы мотивируют саму проблему: для одного и того же `information need` небольшие изменения phrasing могут заметно менять answerability, а значит prompt sensitivity стоит изучать как отдельную **measurement problem**. Затем они формализуют задачу `Prompt Sensitivity Prediction` и описывают построение датасета `PromptSET`: берут вопросы из `TriviaQA` и `HotpotQA`, генерируют для каждого набора близкие prompt variations, а затем фильтруют их по semantic similarity и качеству. После этого paper переходит к benchmark layer: сравниваются разные baselines, включая `LLM self-evaluation`, text-classification approaches и query performance prediction methods, чтобы понять, насколько хорошо они предсказывают, какая формулировка окажется answerable. Финальный вывод двоякий: prompt sensitivity действительно систематична и practically important, а существующие методы предсказания этой чувствительности пока довольно слабы. Для week-01 важно именно это: статья превращает интуицию “prompt matters” в отдельный объект измерения и анализа.

## Как читать источник быстро
- Если нужен core point, читай problem setup and dataset motivation around `information need` versus phrasing.
- Если интересует benchmark layer, смотри sections про `PromptSET` construction and baselines.
- Если нужен practical takeaway for evals, не пропускай empirical result that current predictors remain weak and conclusions about measurement reliability.

## Что источник утверждает прямо
- Небольшие изменения phrasing могут заметно менять answerability, even when the underlying information need is fixed.
- `PromptSET` превращает prompt sensitivity в benchmarkable prediction task rather than anecdotal prompt-engineering issue.
- Existing baselines for predicting which reformulation will work better remain weak.
- Следовательно, prompt wording itself materially shapes observed evaluation evidence.

## Что здесь особенно важно
- **Это не просто prompt engineering advice.** Paper показывает, что prompt sensitivity можно и нужно изучать как benchmark problem.
- **Один и тот же information need не гарантирует один и тот же observed result.** Это сильный удар по наивному чтению behavior as capability.
- **`PromptSET` делает тему измеримой.** За счет этого проблема перестает быть anecdotal.
- **Baselines слабы.** То есть речь не о легко решаемой nuisance-помехе.
- **Связь с elicitation quality прямая.** Если phrasing меняет answerability, то качество eval partly depends on interface design.

## Интерпретация для курса
Для курса это один из самых удобных bridge papers от абстрактной критики к инженерной практике. Он позволяет говорить про under-elicitation не как про философскую possibility, а как про наблюдаемую measurement problem внутри конкретного benchmark setup.

## Что это добавляет к теме недели
Этот источник делает более конкретной общую проблему under-elicitation. Если Barnett и Hubinger говорят о пределе поведенческих выводов на уровне safety claims, то prompt sensitivity paper показывает, **как именно эта хрупкость может проявляться на уровне одного benchmark interaction**. Поэтому эта страница полезна как мост между абстрактной критикой и практикой task design.

## Что стоит запомнить при повторении
- **Prompt sensitivity** — это проблема measurement, а не только usability.
- **Observed capability** зависит и от модели, и от phrasing.
- **Надежный eval** требует внимания не только к dataset и scorer, но и к prompt construction.

## Связанные концепты
- [concepts/prompt-sensitivity](../concepts/prompt-sensitivity.md)
- [concepts/behavioral-evals](../concepts/behavioral-evals.md)
- [concepts/evals](../concepts/evals.md)
- [concepts/inspect-ai](../concepts/inspect-ai.md)

## Что осталось неясным / спорным
- Как строить eval prompts так, чтобы prompt sensitivity меньше искажала измерение capabilities?
- Можно ли заранее предсказывать удачные reformulations достаточно надежно для production pipelines?

## Связанные страницы
- [weeks/week-01](../weeks/week-01.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
