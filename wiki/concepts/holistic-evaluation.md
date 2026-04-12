# Holistic Evaluation

## Коротко
> **Holistic evaluation** — это подход, в котором модели оценивают не по одному узкому benchmark score, а по более широкой матрице сценариев, метрик и trade-offs, с явным признанием неполноты покрытия.

## Почему это важный концепт
HELM делает это понятие центральным для week-03. Оно важно как противовес слишком узкому benchmarking instinct: если модель используется в разных сценариях и может быть хорошей по одним свойствам и плохой по другим, то один score уже почти наверняка недостаточен.

## Что в этой идее особенно важно
- **Coverage.** Нужно думать о разнообразии сценариев использования, а не только о самом удобном test set.
- **Multi-metric view.** Accuracy не может автоматически доминировать над calibration, robustness, toxicity, fairness и efficiency.
- **Standardization.** Сравнение должно контролировать условия адаптации и evaluation protocol.
- **Recognition of incompleteness.** Хороший holistic benchmark не скрывает свои пробелы.

## Что именно здесь ломает наивный вывод
- Большой набор задач не равен автоматической полноте.
- Много метрик не равны автоматической валидности.
- Широта покрытия легко спутать с сильным capability claim, хотя без justification это только широкий measurement surface.

## Практическая интуиция
Holistic evaluation полезно понимать как **управляемое расширение benchmark'а**: не “все подряд”, а более честную попытку показать, где модели различаются и какие trade-offs за этим стоят.

## С чем легко перепутать
- Holistic evaluation легко спутать с просто “большим benchmark'ом”.
- Ее легко принять за решение проблемы validity, хотя ECBD показывает, что coverage и validity — не одно и то же.
- Ее легко свести к leaderboard convenience, хотя исходная мотивация — transparency, а не только ranking.

## Где смотреть дальше
- [HELM](../sources/holistic-evaluation-language-models.md)
- [ECBD](../sources/evidence-centered-benchmark-design-nlp.md)
- [Benchmark Lottery](../sources/benchmark-lottery.md)

## Открытые вопросы
- Когда добавление сценариев и метрик действительно помогает, а когда уже делает benchmark неповоротливым?
- Как совмещать holistic ambition с ограничениями бюджета, времени и compute?

## Связанные страницы
- [concepts/benchmark-design](benchmark-design.md)
- [concepts/benchmarking](benchmarking.md)
- [concepts/benchmark-lottery](benchmark-lottery.md)
