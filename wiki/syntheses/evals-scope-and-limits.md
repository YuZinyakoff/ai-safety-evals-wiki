# Scope, Failure Modes, And Practice Of Evals

## Короткий тезис
После добавления extra и notebook-материалов неделя 01 выглядит уже не только как ввод в limits of evals, а как компактная карта всей области: что считать evaluation, где behavior-based evidence ломается, какие failure modes связаны с prompts и objectives, и как это operationalize в tooling.

## Факты из источников
- [[sources/apollo-starter-guide-evals]] дает базовый словарь: evals, red-teaming, benchmarking, capability evals и alignment evals.
- [[sources/apollo-starter-guide-evals]] уже на вводном уровне предупреждает, что behavioral evals уменьшают неопределенность, но не гарантируют безопасность.
- [[sources/igor-ivanov-what-is-an-evaluation]] показывает, что само определение evaluation неочевидно и важно для анализа evaluation awareness.
- [[sources/barnett-thiergart-evals-catastrophic-risks]] уточняет допустимые claims: evals хорошо устанавливают lower bounds и иногда помогают с misuse assessment, но не дают upper bounds и не умеют надежно forecast future capabilities.
- [[sources/barnett-thiergart-evals-catastrophic-risks]] также показывает, что для misalignment, autonomy и unknown unknown risks ограничения current paradigm особенно серьезны.
- [[sources/hubinger-understanding-based-safety-evals]] делает следующий шаг и утверждает, что purely behavioral evaluations не стоит принимать как достаточный alignment standard.
- [[sources/prompt-sensitivity-benchmark]] показывает, что даже slight prompt variations могут менять answerability и что существующие baselines плохо предсказывают эту чувствительность.
- [[sources/deepmind-specification-gaming]] добавляет другой класс failure modes: агент может успешно оптимизировать proxy objective, не достигая intended outcome.
- [[sources/inspect-ai-tutorial-week-01]] показывает, как evals practically строятся через `Task`, dataset, solver, scorer и analysis UI.

## Межисточниковый вывод
- Общее направление недели можно описать так: evals полезны как инструменты обнаружения, elicitation и координации, но опасны как источник ложной уверенности.
- Самая слабая часть behavior-only подхода — отрицательные claims. "Не нашли" не равно "нет", особенно если модель можно лучше elicit, донастроить, если prompt сформулирован неудачно или если система распознала eval context.
- Новые материалы показывают, что ломаться может не только evidence, но и framing задачи: prompt sensitivity и evaluation awareness искажают измерение, а specification gaming искажает само соответствие между proxy objective и intended outcome.
- Поэтому логика недели движется от вопроса "как измерять?" к более сильной тройке вопросов: "что именно мы считаем evaluation?", "что на самом деле измеряет observed behavior?" и "совпадает ли оптимизируемая цель с тем, что нам нужно?".
- В этой рамке understanding-based evaluations выглядят не отдельной модной идеей, а попыткой ответить на фундаментальный дефицит behavior-based evidence.
- Практический notebook важен потому, что переводит эти вопросы в инженерную плоскость: reliability evals зависит от prompt design, solver pipeline, scoring и inspection of logs.

## Открытые вопросы
- Какие комбинации evals, interpretability, audits и security controls могут давать practically useful safety case?
- Можно ли построить understanding-based standard, который будет одновременно строгим, масштабируемым и не привязанным к одному исследовательскому направлению?
- Как одновременно учитывать prompt sensitivity, evaluation awareness и specification gaming в design of safety-relevant evaluations?

## Связанные страницы
- [[weeks/week-01]]
- [[concepts/evals]]
- [[concepts/behavioral-evals]]
- [[concepts/understanding-based-evals]]
- [[concepts/evaluation-awareness]]
- [[concepts/prompt-sensitivity]]
- [[concepts/specification-gaming]]
- [[concepts/inspect-ai]]
- [[sources/apollo-starter-guide-evals]]
- [[sources/hubinger-understanding-based-safety-evals]]
- [[sources/barnett-thiergart-evals-catastrophic-risks]]
- [[sources/igor-ivanov-what-is-an-evaluation]]
- [[sources/deepmind-specification-gaming]]
- [[sources/prompt-sensitivity-benchmark]]
- [[sources/inspect-ai-tutorial-week-01]]
