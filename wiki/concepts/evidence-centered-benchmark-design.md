# Evidence-Centered Benchmark Design

## Коротко
> **Evidence-centered benchmark design** — это взгляд на benchmark как на систему решений, которая должна собирать и оправдывать evidence о capability, а не просто выдавать score.

## Почему это важный концепт
ECBD дает week-03 самый строгий язык для критики benchmark'ов. Он полезен тем, что не позволяет остановиться на уровне “benchmark вроде разумный”: нужно еще объяснить, почему именно такие tasks, metrics, adaptation и aggregation вообще собирают evidence о целевом свойстве.

## Пять модулей
- **Capability.** Что именно benchmark хочет измерять и для какого intended use.
- **Content.** Какие test items или scenarios должны порождать нужное evidence.
- **Adaptation.** Как объекты оценки приводятся к тестируемому режиму.
- **Assembly.** Какие items реально входят в benchmark и почему этого достаточно.
- **Evidence.** Как evidence извлекается и как агрегируется в measurement.

## Что именно здесь ломает наивный вывод
- Наличие “стандартной” метрики не гарантирует, что она измеряет нужную capability.
- Reusing popular data не гарантирует, что data подходит под новый claim.
- Aggregate score легко скрывает слабую evidence chain.

## Практическая интуиция
Если benchmark нельзя разложить по этим модулям и на каждом шаге объяснить “почему именно так”, значит его claim почти наверняка слабее, чем кажется по paper abstract.

## С чем легко перепутать
- ECBD легко спутать с checklist mentality, но это скорее дисциплина аргументации.
- Его легко принять за pure documentation framework, хотя речь идет не только о записи choices, но и об их justification and validation.
- Его легко принять за anti-benchmark позицию, хотя это скорее pro-benchmark, но с более высоким standard.

## Где смотреть дальше
- [ECBD paper](../sources/evidence-centered-benchmark-design-nlp.md)
- [BenchmarkCards](../sources/benchmarkcards-llm-benchmarks.md)
- [Construct Validity](../sources/construct-validity-nomological-networks.md)

## Открытые вопросы
- Можно ли сделать ECBD-стиль работы нормой для быстро меняющихся LLM benchmark ecosystems?
- Какие parts of the framework наиболее критичны, если ресурс на design and validation ограничен?

## Связанные страницы
- [concepts/benchmark-design](benchmark-design.md)
- [concepts/construct-validity](construct-validity.md)
- [concepts/benchmark-documentation](benchmark-documentation.md)
