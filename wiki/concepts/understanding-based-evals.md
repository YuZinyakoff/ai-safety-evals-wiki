# Understanding-Based Evals

## Что это такое
Understanding-based evals пытаются оценивать не только наблюдаемое поведение модели, но и степень понимания того, что за система получилась, почему она ведет себя именно так и насколько это понимание достаточно для safety claims. Это попытка сдвинуть стандарт безопасности от surface behavior к более содержательному evidence.

## Почему это важно на первой неделе
На первой неделе этот концепт появляется как ответ на растущую неудовлетворенность behavior-only testing. Если модель может скрывать опасные свойства или менять поведение в eval-like context, одного наблюдения за outputs становится мало.

## Что видно по источникам
- [sources/hubinger-understanding-based-safety-evals](../sources/hubinger-understanding-based-safety-evals.md) прямо предлагает смещать стандарт безопасности от behavior-only testing к оценке понимания модели.
- [sources/hubinger-understanding-based-safety-evals](../sources/hubinger-understanding-based-safety-evals.md) подчеркивает, что такой стандарт должен быть method-agnostic и ужесточаться вместе с ростом capabilities.
- [sources/hubinger-understanding-based-safety-evals](../sources/hubinger-understanding-based-safety-evals.md) обсуждает causal scrubbing, auditing games и prediction-based evaluation как потенциальные компоненты, но не как готовое решение.
- [sources/apollo-starter-guide-evals](../sources/apollo-starter-guide-evals.md) допускает, что interpretability-based evals в будущем могут давать более точную информацию, чем одни behavioral tests.
- [sources/barnett-thiergart-evals-catastrophic-risks](../sources/barnett-thiergart-evals-catastrophic-risks.md) не вводит этот термин напрямую, но подробно описывает ограничения current behavior-based paradigm, на фоне которых запрос на более сильный стандарт становится понятнее.
- [sources/igor-ivanov-what-is-an-evaluation](../sources/igor-ivanov-what-is-an-evaluation.md) помогает уточнить еще одну проблему behavior-only testing: модели могут реагировать на eval-like context, а значит поведение на тесте и вне теста не обязано совпадать.

## Как этим пользоваться при повторении
- В логике week-01 этот концепт полезно держать как ответ на проблему: поведение модели еще не равно знанию о том, почему оно такое и что произойдет вне тестового режима.
- Understanding-based evals не отменяют behavioral evals, а повышают планку для safety claims в тех случаях, где важно не только поймать failure, но и иметь основания ожидать его отсутствия.
- Evaluation awareness и sandbagging усиливают мотивацию для understanding-based подхода: если поведение зависит от распознавания тестового контекста, требуется более глубокий тип evidence.

Через месяц этот концепт легко спутать с просто "более сложными evals". Полезно помнить, что здесь идея не в усложнении benchmark, а в смене типа evidence: нас начинает интересовать не только результат теста, но и основания считать модель понятной и предсказуемой.

## С чем легко перепутать
- Understanding-based evals легко принять за просто более строгий benchmark, хотя смысл концепта в смене типа evidence, а не только в усложнении теста.
- Концепт легко спутать с обещанием, что mechanistic interpretability уже решает задачу, хотя сами источники подчеркивают отсутствие готового метода.
- Этот подход не отменяет behavioral evals, а скорее ограничивает силу выводов, которые можно делать без более глубокого понимания модели.

## Открытые вопросы
- Как именно демонстрировать понимание модели так, чтобы это нельзя было подменить красивым post-hoc explanation?
- Какие инструменты interpretability или audit design могут стать частью такого стандарта без жесткой привязки к одной школе методов?

## Связанные страницы
- [weeks/week-01](../weeks/week-01.md)
- [sources/apollo-starter-guide-evals](../sources/apollo-starter-guide-evals.md)
- [sources/hubinger-understanding-based-safety-evals](../sources/hubinger-understanding-based-safety-evals.md)
- [sources/barnett-thiergart-evals-catastrophic-risks](../sources/barnett-thiergart-evals-catastrophic-risks.md)
- [sources/igor-ivanov-what-is-an-evaluation](../sources/igor-ivanov-what-is-an-evaluation.md)
- [concepts/evals](evals.md)
- [concepts/behavioral-evals](behavioral-evals.md)
- [concepts/evaluation-awareness](evaluation-awareness.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
