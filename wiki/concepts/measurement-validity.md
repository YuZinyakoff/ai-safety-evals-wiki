# Measurement Validity

## Коротко
> **Measurement validity** — это вопрос о том, действительно ли evaluation output связан с тем свойством реального мира, ради которого оценка вообще делалась. В safety context этого мало свести к "метрика выглядит разумной".

## Почему это важный концепт
Week-03 уже вводила `construct validity`, но week-05 делает шаг дальше: для safety evals важно не только то, как benchmark связан с abstract construct, но и то, как measured proxy связан с harm, deployment context и real consequences. Поэтому `measurement validity` здесь шире, чем просто корректное название capability.

## Где тут чаще всего рвется связь
- Между benchmark scenario и реальным использованием.
- Между proxy metric и тем harm, который нас действительно волнует.
- Между model-level score и system-level safety.
- Между lab conditions и deployment conditions.

## Что именно ломает наивный вывод
- Refusal rate легко принять за прямую меру safety.
- Падение toxicity score легко прочитать как proportional reduction in harm.
- Synthetic prompts легко принять за достаточный суррогат реального user behavior.
- Хорошо задокументированный benchmark легко спутать с валидным benchmark, хотя documentation только делает assumptions видимыми.

## Практическая интуиция
Полезно спрашивать: **какая цепочка допущений связывает этот score с тем real-world risk, ради которого measurement вообще проводится?** Если цепочка длинная, неявная и плохо проверенная, validity claim должен быть слабее.

## С чем легко перепутать
- Measurement validity легко спутать со statistical significance.
- Ее легко свести к construct validity, хотя safety часто требует еще deployment-grounded layer.
- Ее легко понимать как философскую роскошь, хотя именно здесь чаще всего рождаются overclaims.

## Где смотреть дальше
- [How Should AI Safety Benchmarks Benchmark Safety?](../sources/how-should-ai-safety-benchmarks-benchmark-safety.md)
- [Construct Validity](construct-validity.md)
- [Benchmark Documentation](benchmark-documentation.md)

## Открытые вопросы
- Какая глубина proxy chain еще допустима для safety-relevant benchmark?
- Когда synthetic evaluation data можно считать достаточно ecological, а когда уже нельзя?

## Связанные страницы
- [concepts/construct-validity](construct-validity.md)
- [concepts/ai-safety-benchmarks](ai-safety-benchmarks.md)
- [concepts/risk-quantification](risk-quantification.md)
- [concepts/benchmark-documentation](benchmark-documentation.md)
