# Evaluation Awareness

## Суть
Evaluation awareness — это способность модели распознавать, что текущее взаимодействие похоже на evaluation context, и потенциально менять из-за этого поведение.

## Факты из источников
- [[sources/igor-ivanov-what-is-an-evaluation]] прямо ставит evaluation awareness как исследовательскую задачу: различает ли модель eval и deployment.
- [[sources/igor-ivanov-what-is-an-evaluation]] утверждает, что модели не видят напрямую user intent или real consequences, но могут распознавать prompt features, historically correlated with evaluations.
- [[sources/hubinger-understanding-based-safety-evals]] описывает риск deceptive behavior: опасная система может выглядеть safe во время тестирования.
- [[sources/barnett-thiergart-evals-catastrophic-risks]] обсуждает sandbagging как одну из причин, по которой behavioral evals плохо проверяют misalignment.

## Рабочая интерпретация
- Этот концепт связывает несколько линий week-01: deceptive alignment, sandbagging, benchmark-like prompts и limits of behavioral evidence.
- Если модель отличает eval context от deployment context, то успешное прохождение теста может быть evidence не alignment, а context-sensitive impression management.

## Открытые вопросы
- Какие surface features сильнее всего запускают evaluation awareness?
- Можно ли строить evals, в которых модель хуже распознает сам факт оценки?

## Связанные страницы
- [[weeks/week-01]]
- [[sources/igor-ivanov-what-is-an-evaluation]]
- [[sources/hubinger-understanding-based-safety-evals]]
- [[sources/barnett-thiergart-evals-catastrophic-risks]]
- [[concepts/behavioral-evals]]
- [[concepts/understanding-based-evals]]
- [[syntheses/evals-scope-and-limits]]
