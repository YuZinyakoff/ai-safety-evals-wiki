# Science of Evals

## Коротко
> **Science of Evals** — это идея, что evals должны стать более зрелой дисциплиной, а не оставаться набором локальных benchmark practices и craft-эвристик. Если по evals принимаются high-stakes decisions, нужны более ясные объекты измерения, coverage, reproducibility и stronger statistical standards.

## Почему это важный концепт
К пятой неделе уже видно, что отдельные проблемы evals не изолированы: prompt sensitivity, elicitation gaps, weak proxy chains, poor uncertainty treatment и overclaiming складываются в более общую незрелость поля. `Science of Evals` нужен как концепт, чтобы говорить не только о плохом benchmark design, но и о maturation discipline в целом.

## Какие вопросы этот концепт ставит
- **Что именно мы измеряем?** Не только название benchmark'а, а реальный measured construct.
- **Насколько широк coverage?** Что именно попало в tested distribution и что осталось вне нее?
- **Насколько trustworthy result?** Есть ли reproducibility, robustness и разумная статистическая культура?
- **Какой downstream use допустим?** Какие policy, deployment или governance claims реально поддерживаются?

## Что именно здесь ломает наивный вывод
- Наличие большого benchmark landscape легко принять за зрелое measurement field.
- "Хорошо работающий eval harness" легко спутать с хорошей epistemic дисциплиной.
- Improvement in score легко принять за improvement in understanding.
- Репликация одного числа легко выдать за доказательство надежности целого evaluation regime.

## Практическая интуиция
Полезно держать `Science of Evals` как постоянный corrective: хороший eval — это не только хороший task set, но и хорошо понятный measured quantity, аккуратный protocol, reproducible setup и ограниченный, честный interpretation envelope.

## С чем легко перепутать
- Эту идею легко свести к "нужно больше benchmark'ов".
- Ее легко спутать с purely statistical rigor, хотя статистика — только часть вопроса.
- Ее легко понимать как абстрактный лозунг, хотя она напрямую влияет на deployment and policy use of evals.

## Где смотреть дальше
- [We Need A Science of Evals](../sources/we-need-a-science-of-evals.md)
- [How Should AI Safety Benchmarks Benchmark Safety?](../sources/how-should-ai-safety-benchmarks-benchmark-safety.md)
- [Eval Methodology in AI Safety](../syntheses/eval-methodology-in-ai-safety.md)
- [Statistical Rigor in Evals](statistical-rigor-in-evals.md)

## Открытые вопросы
- Какие pieces of mature science of evals реально достижимы в near term, а какие пока остаются aspirational?
- Какие общие standards возможны для frontier safety evals, где сами target properties часто плохо определены?

## Связанные страницы
- [concepts/evals](evals.md)
- [concepts/eval-methodology](eval-methodology.md)
- [concepts/measurement-validity](measurement-validity.md)
- [concepts/risk-quantification](risk-quantification.md)
- [concepts/ai-safety-benchmarks](ai-safety-benchmarks.md)
- [syntheses/reliable-ai-safety-evals](../syntheses/reliable-ai-safety-evals.md)
