# AI Safety Benchmarks

## Коротко
> **AI safety benchmark** — это не просто benchmark "на тему безопасности", а инструмент, который пытается собирать свидетельства о risk-relevant свойствах модели или системы. Из-за этого к нему предъявляются более жесткие требования, чем к обычному capability benchmark.

## Почему это важный концепт
Week-05 делает важный поворот: safety benchmark нельзя читать как обычный benchmark, где достаточно набора задач и aggregate score. Здесь важно, какие harms вообще считаются значимыми, как benchmark покрывает пространство рисков, насколько score связан с реальным deployment context и что именно остается вне поля зрения. Поэтому safety benchmark полезно держать как отдельный concept, а не как частный случай generic benchmarking.

## Что делает safety benchmark другим
- **Он нормативен.** Речь идет не только о том, что модель делает, но и о том, какие outcomes считаются unacceptable или harmful.
- **Он социотехнический.** Safety зависит не только от model outputs, но и от users, interfaces, safeguards, deployment context и институциональной среды.
- **Он сильнее зависит от proxy chains.** Между benchmark metric и real-world harm обычно лежит длинная цепочка допущений.
- **Он почти всегда неполон.** Даже хороший benchmark редко покрывает unknown unknowns или редкие failure modes.

## Что именно здесь ломает наивный вывод
- Хороший score легко принять за "модель безопасна".
- Набор тестов на известные риски легко принять за coverage всей risk landscape.
- Refusal rate, jailbreak pass rate или toxicity score легко принять за прямую меру harm.
- Model-level result легко спутать с system-level safety verdict.

## Практическая интуиция
Полезно задавать четыре вопроса:

- Какие harm constructs benchmark вообще пытается покрыть?
- Какие blind spots он явно оставляет?
- Как benchmark score связан с deployment-relevant risk, а не только с lab setup?
- Что именно этот benchmark позволяет сказать, а что уже выходит за пределы evidence?

## С чем легко перепутать
- AI safety benchmark легко принять за обычный capability benchmark с более "тревожной" темой.
- Его легко спутать с полным safety case, хотя benchmark почти всегда дает только один слой evidence.
- Его легко читать как purely technical instrument, игнорируя normative assumptions.

## Где смотреть дальше
- [How Should AI Safety Benchmarks Benchmark Safety?](../sources/how-should-ai-safety-benchmarks-benchmark-safety.md)
- [We Need A Science of Evals](../sources/we-need-a-science-of-evals.md)
- [Benchmarking](benchmarking.md)

## Открытые вопросы
- Какие harm domains вообще реально benchmarkable, а какие требуют других форм evidence?
- Насколько широким должен быть safety benchmark, чтобы быть полезным, но не превратиться в расплывчатый checklist?

## Связанные страницы
- [concepts/benchmarking](benchmarking.md)
- [concepts/measurement-validity](measurement-validity.md)
- [concepts/risk-quantification](risk-quantification.md)
- [concepts/science-of-evals](science-of-evals.md)
- [syntheses/reliable-ai-safety-evals](../syntheses/reliable-ai-safety-evals.md)
