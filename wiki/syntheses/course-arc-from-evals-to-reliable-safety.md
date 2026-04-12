# From Evals To Reliable AI Safety Evals

## Короткий тезис
> **Дуга курса идет от полезного, но ограниченного language of evals к более жесткому вопросу: когда evaluation вообще заслуживает доверия как часть safety-relevant decision-making.** Каждая неделя добавляет не новый isolated topic, а новый фильтр на силу выводов.

## Как устроена дуга курса
- **Week-01** вводит базовый corrective: evals полезны, но они не равны safety guarantee.
- **Week-02** делает следующий шаг и спрашивает, как вообще выбирать evaluation frame и как честно интерпретировать benchmark result статистически.
- **Week-03** показывает, что benchmark design сам конструирует evidence и влияет на incentives поля.
- **Week-04** добавляет agent layer: траектории, scaffolding, elicitation и deployment behavior делают measurement еще более хрупким.
- **Week-05** поднимает стандарт до safety and field level: нужны measurement validity, risk quantification, more mature science of evals и research taste.

## Что дает каждая неделя
- **Week-01: limits of claims.** После нее уже трудно путать observed behavior с полным understanding модели и делать сильные claims из слабого evidence.
- **Week-02: discipline of interpretation.** Здесь появляется язык `what to measure / how to measure / what the result means`, а вместе с ним и statistical rigor.
- **Week-03: benchmark as contentful design.** Эта неделя делает видимым, что benchmark не нейтрален: задачи, метрики, aggregation и documentation формируют сам вывод.
- **Week-04: procedure matters as much as score.** Для агентов становится особенно видно, что protocol, scaffolding и elicitation меняют measured capability.
- **Week-05: reliable safety evals need more than benchmarking.** Финальная неделя собирает разговор в high-stakes frame и добавляет вопрос о том, какие проблемы вообще стоит считать центральными.

## Повторяющиеся различия, которые нужно держать вместе
- **Behavior vs deeper understanding.** Первый дает useful evidence, но редко достаточен для сильных alignment claims.
- **Score vs claim.** Результат оценки и то, что из него разрешено заключать, не одно и то же.
- **Benchmark coverage vs real-world relevance.** Даже хороший benchmark остается ограниченным slice of behavior.
- **Capability vs reliability.** Что система может и насколько стабильно она это делает — разные вопросы.
- **Model-level measurement vs system-level safety.** Вывод о модели не равен выводу о deployment setup.
- **Tractable problem vs important problem.** Удобная measurement target не обязательно совпадает с тем, что действительно важно для AI safety.

## Как ломается наивный вывод по мере курса
- **Сначала** кажется, что eval показывает "умеет или не умеет".
- **Потом** выясняется, что prompt, framing и sampling уже влияют на ответ.
- **Дальше** становится видно, что benchmark design определяет, что вообще будет считаться evidence.
- **Потом** агентский слой показывает, что protocol и scaffolding могут занижать или искажать capability claim.
- **И наконец** safety layer показывает, что даже аккуратный benchmark score еще очень далек от trustworthy statement о deployment risk.

Именно эта последовательность и есть главный результат курса: не отказ от evals, а повышение стандарта их чтения.

## Практическая дисциплина после всего курса
После любого consequential evaluation полезно проходить один и тот же цикл:

1. **Сформулировать object of measurement и тип claim.**
2. **Понять, какой evaluation mode вообще подходит под этот вопрос.**
3. **Проверить, как design choices формируют evidence.**
4. **Прочитать результат статистически, а не только номинально.**
5. **Оценить coverage, elicitation quality и deployment relevance.**
6. **Явно отделить то, что результат поддерживает, от того, чего он не поддерживает.**
7. **Спросить, не является ли вся задача удобным proxy вместо важной проблемы.**

## Где остается напряжение
- **Robust benchmark vs broader safety case.** Хочется сравнимости и repeatability, но реальная safety picture почти всегда шире benchmark setup.
- **Capability elicitation vs realism.** Сильное elicitation помогает не занижать возможности, но усложняет comparability и product relevance.
- **Policy usefulness vs epistemic humility.** Governance нужны actionable thresholds, а сами evals часто еще слишком молоды для таких claims.
- **Field maturity vs speed of model change.** Пока evaluation discipline пытается стать зрелой, сами объекты измерения быстро меняются.

## Что курс в целом добавляет
Если сжать весь курс до одной мысли, получится так: **evals ценны не как автоматический safety verdict, а как дисциплина controlled evidence, которую нужно все время уточнять, ограничивать и встраивать в более широкий reasoning about risk**. Эта мысль проходит через все пять недель и становится сильнее с каждым новым слоем.

## Открытые вопросы
- Какой realistic minimum standards стоит считать достаточным для reliable AI safety evals уже сейчас?
- Какие problems in AI safety evals одновременно действительно важны и достаточно tractable, чтобы на них строить research agenda?
- Как лучше сочетать benchmark evidence, interpretability, audits, post-deployment monitoring и governance layers в один defensible safety case?

## Связанные страницы
- [weeks/week-01](../weeks/week-01.md)
- [weeks/week-02](../weeks/week-02.md)
- [weeks/week-03](../weeks/week-03.md)
- [weeks/week-04](../weeks/week-04.md)
- [weeks/week-05](../weeks/week-05.md)
- [syntheses/evals-scope-and-limits](evals-scope-and-limits.md)
- [syntheses/benchmarking-beyond-single-scores](benchmarking-beyond-single-scores.md)
- [syntheses/benchmark-design-evidence-and-incentives](benchmark-design-evidence-and-incentives.md)
- [syntheses/agent-evals-beyond-task-success](agent-evals-beyond-task-success.md)
- [syntheses/reliable-ai-safety-evals](reliable-ai-safety-evals.md)
- [concepts/evals](../concepts/evals.md)
- [concepts/benchmarking](../concepts/benchmarking.md)
- [concepts/agent-evaluation](../concepts/agent-evaluation.md)
- [concepts/science-of-evals](../concepts/science-of-evals.md)
- [concepts/research-taste](../concepts/research-taste.md)
