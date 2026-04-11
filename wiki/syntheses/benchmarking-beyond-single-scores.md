# Benchmarking Beyond Single Scores

## Короткий тезис
> **Week-02 показывает, что benchmark result становится хорошим evidence только внутри трех слоев сразу:** правильного evaluation frame, честной статистической интерпретации и понимания того, что benchmark вообще не покрывает.

## Где источники согласны
- **Benchmarking полезен.** Ни один из источников недели не спорит с тем, что standardized evaluation остается важным инструментом.
- **Один score почти никогда не достаточен.** И CSET, и Miller, и survey beyond benchmarks по-разному подводят к этому выводу.
- **Нужно различать объект измерения.** Model outputs, contextual usefulness, downstream impact и broad safety claims — это не одно и то же.
- **Coverage всегда ограничено.** Даже сильный benchmark suite остается bounded slice of behavior.

## Как источники усиливают друг друга
- **CSET explainer** задает правильную рамку: сначала понять, **что** мы меряем, **как** меряем и **что вообще значит** полученный результат.
- **Miller** показывает, что даже внутри правильно выбранного frame benchmark result без uncertainty-aware reading слишком слаб.
- **Survey beyond benchmarks** расширяет разговор: даже статистически аккуратный benchmark может упираться в contamination, saturation и bounded coverage.
- **Inspect AI tutorial** делает весь этот reasoning operational: от `Task` и `EvalLog` до `confidence intervals`, `paired comparison` и `power analysis`.
- **Awesome-LLM-Eval** служит напоминанием, что большой catalog benchmarks и tools полезен для навигации, но не заменяет evaluation judgment.

## Что именно ломает наивный вывод
- **Сначала можно выбрать не тот объект оценки.** Например, перепутать `model-side capability` с `contextual usefulness`.
- **Потом можно переоценить само число.** Score без confidence interval и without paired structure слишком легко читать как meaningful difference.
- **Затем можно забыть про coverage.** Даже честно посчитанный результат может слабо переноситься вне benchmark suite.
- **И наконец можно спутать landscape awareness с solved evaluation problem.** Каталог benchmarks не отвечает автоматически на вопрос, какой именно benchmark подходит под задачу и какой claim он реально поддерживает.

## Где остается напряжение
- **Насколько далеко можно дотянуть benchmark evidence до contextual claims?** CSET помогает развести типы evaluation, но operational граница между ними остается подвижной.
- **Насколько достаточно статистической строгости?** Miller поднимает bar, но open-ended tasks и richer human-judged settings быстро делают картину сложнее.
- **Что делать с bounded coverage problem?** Survey описывает dynamic benchmarks, `LLMs-as-a-judge` и другие ответы, но не закрывает вопрос окончательно.

## Практическая дисциплина после этой недели
После любого benchmark result полезно спрашивать не один, а несколько вопросов:
- **Какой именно тип evaluation это был?**
- **Что означает этот score статистически?**
- **Сравниваются ли модели на одной и той же question-level структуре?**
- **Что осталось вне coverage и насколько это важно для claim, который мы хотим сделать?**
- **Не подменяем ли мы evaluation judgment красивым leaderboard reading?**

Именно эта последовательность делает week-02 полезной как отдельный synthesis: она собирает не просто summaries, а рабочую дисциплину чтения benchmark evidence.

## Открытые вопросы
- Какой минимум reporting discipline стоит считать обязательным для benchmark papers и internal eval reports?
- Что сегодня выглядит более перспективным ответом на bounded coverage problem: dynamic benchmarks, automated judges, richer task design или комбинация этих подходов?
- Как связывать benchmark evidence с contextual evaluations, чтобы не оставаться либо слишком абстрактным, либо слишком noisy?

## Связанные страницы
- [weeks/week-02](../weeks/week-02.md)
- [concepts/benchmarking](../concepts/benchmarking.md)
- [concepts/model-safety-evals](../concepts/model-safety-evals.md)
- [concepts/contextual-safety-evals](../concepts/contextual-safety-evals.md)
- [concepts/statistical-rigor-in-evals](../concepts/statistical-rigor-in-evals.md)
- [concepts/evaluation-generalization](../concepts/evaluation-generalization.md)
- [concepts/inspect-ai](../concepts/inspect-ai.md)
