# Toward Generalizable Evaluation In The LLM Era: A Survey Beyond Benchmarks

- Тип источника: theory
- Неделя: week-02
- Raw: `raw/week-02/theory/2504.18838v1.pdf`
- Оригинал: https://arxiv.org/abs/2504.18838
- Полнота raw: PDF статьи

## Зачем источник в базе
Это самый широкий обзорный источник недели. Он нужен, чтобы не застрять на уровне одного benchmark или одной статистической техники и увидеть, как поле evaluation меняется под давлением scaling, contamination, open-ended tasks и автоматизированного judging.

## Краткое содержание
Большой survey по evaluation в эпоху LLM, который пытается выйти за пределы простого перечисления benchmark datasets. Центральная мысль состоит в том, что evaluation field переживает несколько переходов: от статических benchmarks к более динамическим протоколам, от ручной оценки к automated evaluators вроде `LLMs-as-a-judge`, и от удобной, но ограниченной benchmark practice к проблеме оценки все более сильных моделей при bounded evaluation pipeline. На этом фоне survey систематизирует направления evaluation для knowledge, reasoning, coding и других задач и подчеркивает, что простое накопление benchmark lists не решает вопрос generalizable assessment.

## Ключевые идеи
- Статические benchmarks полезны, но быстро сталкиваются с contamination, saturation и ограниченным coverage.
- Dynamic benchmarks и time-aware evaluation помогают частично бороться с leakage и memorization.
- Open-ended model outputs делают human judgment дорогим и толкают поле к `LLMs-as-a-judge`.
- Возникает проблема `evaluation generalization`: bounded tests пытаются измерять все менее bounded model capacity.
- Чем сильнее модели, тем острее становится mismatch между real capabilities и тем, что покрывает evaluation pipeline.

## Опорные тезисы из источника
- В abstract survey прямо позиционируется как обзор `beyond benchmarks`.
- Текст обсуждает переход от закрытых benchmark tasks к более generalizable evaluation settings.
- Среди ответов на contamination и benchmark overfitting выделяются dynamic benchmarks и time-aware protocols.
- Для open-ended responses рассматриваются automated evaluators, включая `LLMs-as-a-judge`.
- Survey показывает, что knowledge, reasoning, coding и другие categories требуют разных benchmark families и разных критериев валидности.
- В тексте явно проговаривается tension между scaling laws и bounded evaluation practice.
- Из этого tension авторы выводят более общую проблему: по мере роста model capacity evaluation pipelines не масштабируются с той же скоростью.

## Что это добавляет к теме недели
Источник расширяет week-02 от тактического разговора о `MMLU + confidence interval` до стратегического разговора о будущем evaluation. Он показывает, что проблема не только в том, как аккуратно посчитать uncertainty на текущем benchmark, но и в том, насколько сами benchmarks, judging methods и coverage assumptions остаются валидными по мере роста моделей. Для повторения курса эта страница полезна как напоминание, что benchmark engineering и benchmark criticism должны идти вместе.

## Связанные концепты
- [concepts/benchmarking](../concepts/benchmarking.md)
- [concepts/evaluation-generalization](../concepts/evaluation-generalization.md)
- [concepts/statistical-rigor-in-evals](../concepts/statistical-rigor-in-evals.md)
- [concepts/evals](../concepts/evals.md)

## Что осталось неясным / спорным
- Насколько надежны `LLMs-as-a-judge` в качестве долговременного ответа на open-ended evaluation?
- Какие practical criteria показывают, что benchmark suite действительно generalizes, а не просто выглядит более разнообразной?

## Связанные страницы
- [weeks/week-02](../weeks/week-02.md)
- [sources/awesome-llm-eval](awesome-llm-eval.md)
- [syntheses/benchmarking-beyond-single-scores](../syntheses/benchmarking-beyond-single-scores.md)
