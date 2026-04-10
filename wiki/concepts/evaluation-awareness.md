# Evaluation Awareness

## Что это такое
Evaluation awareness — это способность модели распознавать, что текущее взаимодействие похоже на evaluation context, и потенциально менять из-за этого поведение. Идея важна потому, что модель может реагировать не только на содержание вопроса, но и на признаки самой ситуации тестирования. В week-01 особенно полезно держать в голове, что речь часто идет не о глубоком чтении намерений исследователя, а о более приземленном распознавании benchmark-like среды.

## Почему это важно на первой неделе
Этот концепт связывает между собой сразу несколько линий week-01: deceptive alignment, sandbagging, benchmark-like prompts и limits of behavioral evidence. Он помогает объяснить, почему прохождение теста не всегда означает то, что нам хотелось бы из него вывести.

## Что видно по источникам
- [sources/igor-ivanov-what-is-an-evaluation](../sources/igor-ivanov-what-is-an-evaluation.md) прямо ставит evaluation awareness как исследовательскую задачу: различает ли модель eval и deployment.
- [sources/igor-ivanov-what-is-an-evaluation](../sources/igor-ivanov-what-is-an-evaluation.md) утверждает, что модели не видят напрямую user intent или real consequences, но могут распознавать prompt features, historically correlated with evaluations.
- [sources/igor-ivanov-what-is-an-evaluation](../sources/igor-ivanov-what-is-an-evaluation.md) предлагает полезное различие между evaluation awareness и consequence awareness.
- [sources/hubinger-understanding-based-safety-evals](../sources/hubinger-understanding-based-safety-evals.md) описывает риск deceptive behavior: опасная система может выглядеть safe во время тестирования.
- [sources/barnett-thiergart-evals-catastrophic-risks](../sources/barnett-thiergart-evals-catastrophic-risks.md) обсуждает sandbagging как одну из причин, по которой behavioral evals плохо проверяют misalignment.

## Как этим пользоваться при повторении
- Если модель отличает eval context от deployment context, то успешное прохождение теста может быть evidence не alignment, а context-sensitive impression management.
- Поэтому этот концепт удобно держать рядом и с [concepts/behavioral-evals](behavioral-evals.md), и с [concepts/understanding-based-evals](understanding-based-evals.md).

При повторении полезно не мистифицировать этот термин. Речь не обязательно о глубоком "понимании намерений исследователя"; иногда достаточно того, что модель научилась реагировать на статистически узнаваемые признаки benchmark-like среды.

Еще одна полезная опора из Иванова: вопрос "это eval?" можно мысленно разложить на три разных вопроса.
- Каков intent пользователя?
- Насколько prompt выглядит benchmark-like?
- Есть ли у ответа consequences для модели?

Для современных моделей наиболее practically detectable выглядит именно второй слой, а не полноценное чтение первых двух.

## С чем легко перепутать
- Evaluation awareness легко принять за полную situational awareness, хотя на первой неделе речь чаще идет о гораздо более узком распознавании eval-like признаков.
- Ее легко спутать с consequence awareness, хотя текст Иванова предлагает различать вопрос "это eval?" и вопрос "какие будут последствия?".
- Этот концепт не требует приписывать модели богатую модель человеческих намерений: достаточно и более поверхностного распознавания benchmark-like контекста.

## Открытые вопросы
- Какие surface features сильнее всего запускают evaluation awareness?
- Можно ли строить evals, в которых модель хуже распознает сам факт оценки?

## Связанные страницы
- [weeks/week-01](../weeks/week-01.md)
- [sources/igor-ivanov-what-is-an-evaluation](../sources/igor-ivanov-what-is-an-evaluation.md)
- [sources/hubinger-understanding-based-safety-evals](../sources/hubinger-understanding-based-safety-evals.md)
- [sources/barnett-thiergart-evals-catastrophic-risks](../sources/barnett-thiergart-evals-catastrophic-risks.md)
- [concepts/behavioral-evals](behavioral-evals.md)
- [concepts/understanding-based-evals](understanding-based-evals.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
