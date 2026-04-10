# AI Safety Evaluations: An Explainer

- Тип источника: theory
- Неделя: week-02
- Raw: `raw/week-02/theory/AI Safety Evaluations An Explainer.md`
- Оригинал: https://cset.georgetown.edu/article/ai-safety-evaluations-an-explainer/
- Полнота raw: полный web clip статьи

## Зачем источник в базе
Это самый полезный входной текст недели, если нужно быстро восстановить базовую taxonomy AI safety evaluations. Он нужен как страница, которая разводит разные типы evaluation-задач и помогает не смешивать измерение model outputs с измерением real-world impact.

## Краткое содержание
Explainer от CSET делит safety evaluations на две большие категории: model safety evaluations, которые оценивают outputs модели как таковые, и contextual safety evaluations, которые пытаются понять влияние модели на реальные действия и outcomes. Поверх этого текста строится простая, но очень полезная рамка design process: сначала решить, что именно измерять, потом как это измерять, а затем отдельно разобраться, что полученные результаты вообще значат. Внутри этой рамки обсуждаются capability testing, benchmarking, red-teaming и uplift studies, а также ограничения proxy metrics и риск переинтерпретации результатов.

## Ключевые идеи
- Не все safety evals отвечают на один и тот же вопрос.
- Важно различать model safety evaluations и contextual safety evaluations.
- Хороший eval design требует отдельно продумать `what to measure`, `how to measure it` и `what the results mean`.
- Benchmarking, capability testing, red-teaming и uplift studies решают разные задачи.
- Результаты evals почти всегда являются proxy evidence, а не прямым измерением реального риска.

## Опорные тезисы из источника
- Model safety evaluations спрашивают прежде всего `is the model capable?`.
- Contextual safety evaluations больше спрашивают `is the model useful?` в реальном или приближенном к реальности контексте.
- В качестве model-side approaches текст обсуждает capability testing и benchmarking.
- В качестве contextual approaches текст обсуждает red-teaming и uplift studies.
- Для contextual evaluations особенно трудно стандартизировать человеческие переменные: экспертизу участников, качество collaboration и другие факторы.
- Текст отдельно предупреждает, что performance on a task не равна reliable claim о downstream risk.
- Без аккуратной интерпретации evaluation results легко переоценить, особенно если измерялись лишь proxy outcomes.

## Что это добавляет к теме недели
Источник делает неделю 02 более структурной. После недели 01 уже ясно, что evals ограничены; этот текст уточняет следующий шаг: ограничены разные evals по-разному, потому что они измеряют разные объекты. Для повторения курса эта страница особенно полезна тем, что задает язык, в котором потом удобнее обсуждать benchmarking, uplift, red-teaming, статистическую неопределенность и интерпретацию результатов.

## Связанные концепты
- [concepts/evals](../concepts/evals.md)
- [concepts/model-safety-evals](../concepts/model-safety-evals.md)
- [concepts/contextual-safety-evals](../concepts/contextual-safety-evals.md)
- [concepts/benchmarking](../concepts/benchmarking.md)

## Что осталось неясным / спорным
- Где проходит практическая граница между model safety и contextual safety evaluations в гибридных протоколах?
- Какие proxy outcomes достаточно хороши, чтобы на их основе принимать policy или deployment decisions?

## Связанные страницы
- [weeks/week-02](../weeks/week-02.md)
- [syntheses/benchmarking-beyond-single-scores](../syntheses/benchmarking-beyond-single-scores.md)
