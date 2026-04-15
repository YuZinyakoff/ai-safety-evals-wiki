# Benchmark Design

## Коротко
> **Benchmark design** — это не только выбор dataset и метрики. Это вся конструкция того, какое evidence benchmark вообще собирает, какие trade-offs он делает видимыми и какие claims о модели он позволяет или не позволяет делать.

## Почему это важный концепт
Week-03 по сути строится вокруг этого понятия. До нее benchmarking можно было понимать как “запустить набор задач и посмотреть на score”. После нее становится видно, что benchmark сам задает структуру наблюдения: какие задачи считать показательными, какие метрики считать значимыми, как агрегировать ответы и что потом из этого выводить.

## Что сюда входит
- Выбор capability или свойства, про которое benchmark должен что-то сказать.
- Выбор content: tasks, prompts, data slices, сценариев использования.
- Выбор adaptation и evaluation protocol.
- Выбор metrics и правил агрегации.
- Явная или неявная теория того, какое evidence считать достаточным.

## Что именно здесь ломает наивный вывод
- **Benchmark score** легко принять за свойство модели, хотя это всегда свойство модели-в-конструкции-benchmark'а.
- **Один benchmark** легко принять за нейтральный тест, хотя он уже воплощает чьи-то priorities и assumptions.
- **Documentation** часто считают вторичной, хотя без нее benchmark design плохо читается и еще хуже используется.

## Практическая интуиция
Полезно держать такой вопрос: **если бы я изменил задачи, метрики, adaptation или правила агрегации, остался бы мой вывод тем же?** Если ответ нет, значит benchmark design здесь не фон, а часть самого результата.

## С чем легко перепутать
- Benchmark design легко спутать с просто benchmark implementation.
- Его легко свести к engineering details, хотя week-03 показывает, что это еще и epistemic design.
- Его легко считать синонимом validity, хотя validity — только один из аспектов benchmark design.

## Где смотреть дальше
- [HELM](../sources/holistic-evaluation-language-models.md) — широкий взгляд на coverage, multi-metric evaluation и standardization.
- [ECBD](../sources/evidence-centered-benchmark-design-nlp.md) — как design decisions превращаются в evidence chain.
- [The Benchmark Lottery](../sources/benchmark-lottery.md) — как benchmark design влияет на research incentives.

## Открытые вопросы
- Где проходит граница между “достаточно хорошим design” и design, который уже слишком тяжело поддерживать?
- Как делать benchmark design прозрачнее, не превращая каждую оценку в непрактично сложную систему?

## Связанные страницы
- [concepts/benchmarking](benchmarking.md)
- [concepts/holistic-evaluation](holistic-evaluation.md)
- [concepts/evidence-centered-benchmark-design](evidence-centered-benchmark-design.md)
- [concepts/benchmark-lottery](benchmark-lottery.md)
- [syntheses/benchmark-design-evidence-and-incentives](../syntheses/benchmark-design-evidence-and-incentives.md)
