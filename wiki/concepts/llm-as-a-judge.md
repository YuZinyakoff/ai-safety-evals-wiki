# LLM-As-A-Judge

## Коротко
> **LLM-as-a-judge** — это использование одной модели как оценщика ответов другой модели. Идея привлекательна из-за масштаба и гибкости, но ее надежность сильно зависит от judge bias, reference quality, task type и human grounding.

## Почему это важный концепт
Week-03 показывает, что judge model — это не просто дешевый surrogate for humans. Это отдельный measurement device со своими failure modes. Понять этот концепт важно, если evaluation выходит за пределы short-answer benchmarks в open-ended, preference-heavy или correctness-heavy settings.

## Где это полезно
- Open-ended generation, где обычный exact match мало что говорит.
- Pairwise preference evaluation.
- Scalable filtering или triage до более дорогой human review.
- Judge-audited pipelines в tooling вроде `Inspect AI`.

## Что именно здесь ломает наивный вывод
- **Высокий agreement** не гарантирует низкий bias.
- **Judge competence** на underlying task влияет на качество суждения сильнее, чем часто предполагают.
- **Reference answer** может радикально менять judge behavior.
- **Frontier evaluation** особенно сложна, потому что judged model может быть лучше judge model.

## Практическая интуиция
Полезно держать такой порядок вопросов:
- Что именно judge оценивает: preference, style, correctness, safety, compliance?
- Есть ли human grounding или verified reference?
- Насколько judge сам способен решать underlying task?
- Какие biases уже известны: position, verbosity, self-preference, refusal behavior?

## С чем легко перепутать
- LLM-as-a-judge легко принять за бесплатную замену людей, хотя week-03 показывает множество ограничений.
- Его легко считать просто новым scorer, хотя это часто еще и новый источник epistemic risk.
- Preference judging легко спутать с correctness judging, хотя это разные режимы.

## Где смотреть дальше
- [MT-Bench / Chatbot Arena](../sources/llm-as-a-judge-mt-bench-chatbot-arena.md)
- [Limits at the frontier](../sources/limits-scalable-evaluation-frontier.md)
- [No Free Labels](../sources/no-free-labels-llm-as-a-judge.md)
- [Inspect AI tutorial week-03](../sources/inspect-ai-tutorial-week-03.md)

## Открытые вопросы
- Где judge model уже достаточно надежна для production-like workflows, а где нужна обязательная human verification?
- Какие hybrids между judge, reference answers и human labels дают лучший reliability/cost balance?

## Связанные страницы
- [concepts/toxicity-evals](toxicity-evals.md)
- [concepts/statistical-rigor-in-evals](statistical-rigor-in-evals.md)
- [concepts/benchmark-design](benchmark-design.md)
