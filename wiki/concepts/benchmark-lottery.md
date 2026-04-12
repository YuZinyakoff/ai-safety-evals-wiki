# Benchmark Lottery

## Коротко
> **Benchmark lottery** — это идея о том, что perceived superiority метода зависит не только от самого метода, но и от того, какие задачи, правила агрегации и community priorities заданы benchmark ecosystem.

## Почему это важный концепт
Этот концепт нужен, чтобы перестать читать benchmark ranking как чистое отражение “истинного качества” метода. Week-03 показывает, что benchmark ecosystem сам задает, кому повезет выглядеть сильнее и какие свойства будут считаться прогрессом.

## Из чего состоит эта хрупкость
- **Task selection bias.** Разные подмножества задач могут менять rankings.
- **Aggregation effects.** Aggregate score может вести себя неустойчиво и скрывать важные различия.
- **Community bias.** Сообщество начинает оптимизировать именно то, что benchmark reward'ит.
- **Statefulness.** Benchmark меняется вместе с историей использования, tooling и participation.

## Что именно здесь ломает наивный вывод
- “Лучший на benchmark'е” не всегда значит “лучший по существу”.
- “Стабильный leaderboard” не гарантирует, что benchmark нейтрален.
- “Популярный benchmark” не гарантирует, что именно он лучше всего поддерживает нужный claim.

## Практическая интуиция
Полезно спрашивать: **если бы сообщество выбрало другой benchmark suite, осталась бы эта картина прогресса той же?** Если нет, значит benchmark ecosystem уже формирует сам narrative о развитии поля.

## С чем легко перепутать
- Benchmark lottery легко спутать с банальным “benchmark imperfect”. На самом деле claim сильнее: benchmark actively shapes progress.
- Его легко принять за аргумент против всех benchmark'ов, хотя речь скорее о discipline and humility.

## Где смотреть дальше
- [The Benchmark Lottery](../sources/benchmark-lottery.md)
- [Hardt on benchmarks](../sources/hardt-emerging-science-ml-benchmarks.md)
- [HELM](../sources/holistic-evaluation-language-models.md)

## Открытые вопросы
- Можно ли проектировать benchmark ecosystem так, чтобы он меньше искажал incentives?
- Насколько реально сохранить ranking stability в multitask LLM era?

## Связанные страницы
- [concepts/benchmark-design](benchmark-design.md)
- [concepts/benchmarking](benchmarking.md)
- [concepts/holistic-evaluation](holistic-evaluation.md)
