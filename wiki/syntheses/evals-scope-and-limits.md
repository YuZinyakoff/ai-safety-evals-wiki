# Scope, Failure Modes, And Practice Of Evals

## Короткий тезис
После добавления extra и notebook-материалов неделя 01 выглядит уже не только как ввод в limits of evals, а как компактная карта всей области: что считать evaluation, где behavior-based evidence ломается, какие failure modes связаны с prompts и objectives, и как это operationalize в tooling.

Полезно видеть этот синтез не как еще один summary рядом с source pages, а как страницу, которая собирает общий рисунок недели. Если отдельные материалы начинают распадаться в памяти на несвязанные тезисы, имеет смысл вернуться именно сюда.

## Факты из источников
- [sources/apollo-starter-guide-evals](../sources/apollo-starter-guide-evals.md) дает базовый словарь: evals, red-teaming, benchmarking, capability evals и alignment evals.
- [sources/apollo-starter-guide-evals](../sources/apollo-starter-guide-evals.md) уже на вводном уровне предупреждает, что behavioral evals уменьшают неопределенность, но не гарантируют безопасность, а еще показывает evals как research-engineering practice, а не только как набор benchmark artifacts.
- [sources/igor-ivanov-what-is-an-evaluation](../sources/igor-ivanov-what-is-an-evaluation.md) показывает, что само определение evaluation неочевидно и важно для анализа evaluation awareness.
- [sources/igor-ivanov-what-is-an-evaluation](../sources/igor-ivanov-what-is-an-evaluation.md) также полезно разносит intent, benchmark-likeness и consequences как разные измерения eval-like context.
- [sources/barnett-thiergart-evals-catastrophic-risks](../sources/barnett-thiergart-evals-catastrophic-risks.md) уточняет допустимые claims: evals хорошо устанавливают lower bounds и иногда помогают с misuse assessment, но не дают upper bounds и не умеют надежно forecast future capabilities.
- [sources/barnett-thiergart-evals-catastrophic-risks](../sources/barnett-thiergart-evals-catastrophic-risks.md) также показывает, что для misalignment, autonomy и unknown unknown risks ограничения current paradigm особенно серьезны.
- [sources/hubinger-understanding-based-safety-evals](../sources/hubinger-understanding-based-safety-evals.md) делает следующий шаг и утверждает, что purely behavioral evaluations не стоит принимать как достаточный alignment standard.
- [sources/prompt-sensitivity-benchmark](../sources/prompt-sensitivity-benchmark.md) показывает, что даже slight prompt variations могут менять answerability и что существующие baselines плохо предсказывают эту чувствительность.
- [sources/deepmind-specification-gaming](../sources/deepmind-specification-gaming.md) добавляет другой класс failure modes: агент может успешно оптимизировать proxy objective, не достигая intended outcome.
- [sources/inspect-ai-tutorial-week-01](../sources/inspect-ai-tutorial-week-01.md) показывает, как evals practically строятся через `Task`, dataset, solver, scorer и analysis UI.

## Межисточниковый вывод
- Общее направление недели можно описать так: evals полезны как инструменты обнаружения, elicitation и координации, но опасны как источник ложной уверенности.
- Самая слабая часть behavior-only подхода — отрицательные claims. "Не нашли" не равно "нет", особенно если модель можно лучше elicit, донастроить, если prompt сформулирован неудачно или если система распознала eval context.
- Новые материалы показывают, что ломаться может не только evidence, но и framing задачи: prompt sensitivity и evaluation awareness искажают измерение, а specification gaming искажает само соответствие между proxy objective и intended outcome.
- Еще один важный слой из week-01 такой: "evaluation" не является простым наблюдаемым примитивом. То, что модель реально детектирует, может быть только benchmark-likeness среды, а не intent исследователя или реальные stakes.
- Поэтому логика недели движется от вопроса "как измерять?" к более сильной тройке вопросов: "что именно мы считаем evaluation?", "что на самом деле измеряет observed behavior?" и "совпадает ли оптимизируемая цель с тем, что нам нужно?".
- В этой рамке understanding-based evaluations выглядят не отдельной модной идеей, а попыткой ответить на фундаментальный дефицит behavior-based evidence.
- Практический notebook важен потому, что переводит эти вопросы в инженерную плоскость: reliability evals зависит от prompt design, solver pipeline, scoring и inspection of logs.

Именно эта связка делает неделю содержательно сильной: она не просто перечисляет ограничения, а показывает, что они возникают на разных уровнях одновременно. Один и тот же неверный вывод о модели может оказаться следствием неудачного prompt, распознанного eval-context, слабой цели или переоценки того, что вообще способен доказать behavioral test.

## Открытые вопросы
- Какие комбинации evals, interpretability, audits и security controls могут давать practically useful safety case?
- Можно ли построить understanding-based standard, который будет одновременно строгим, масштабируемым и не привязанным к одному исследовательскому направлению?
- Как одновременно учитывать prompt sensitivity, evaluation awareness и specification gaming в design of safety-relevant evaluations?

## Связанные страницы
- [weeks/week-01](../weeks/week-01.md)
- [concepts/evals](../concepts/evals.md)
- [concepts/behavioral-evals](../concepts/behavioral-evals.md)
- [concepts/understanding-based-evals](../concepts/understanding-based-evals.md)
- [concepts/evaluation-awareness](../concepts/evaluation-awareness.md)
- [concepts/prompt-sensitivity](../concepts/prompt-sensitivity.md)
- [concepts/specification-gaming](../concepts/specification-gaming.md)
- [concepts/inspect-ai](../concepts/inspect-ai.md)
- [sources/apollo-starter-guide-evals](../sources/apollo-starter-guide-evals.md)
- [sources/hubinger-understanding-based-safety-evals](../sources/hubinger-understanding-based-safety-evals.md)
- [sources/barnett-thiergart-evals-catastrophic-risks](../sources/barnett-thiergart-evals-catastrophic-risks.md)
- [sources/igor-ivanov-what-is-an-evaluation](../sources/igor-ivanov-what-is-an-evaluation.md)
- [sources/deepmind-specification-gaming](../sources/deepmind-specification-gaming.md)
- [sources/prompt-sensitivity-benchmark](../sources/prompt-sensitivity-benchmark.md)
- [sources/inspect-ai-tutorial-week-01](../sources/inspect-ai-tutorial-week-01.md)
