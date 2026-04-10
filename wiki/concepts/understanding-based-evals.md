# Understanding-Based Evals

## Суть
Understanding-based evals пытаются оценивать не только наблюдаемое поведение модели, но и степень понимания того, что за система получилась, почему она ведет себя именно так и насколько это понимание достаточно для safety claims.

## Факты из источников
- [[sources/hubinger-understanding-based-safety-evals]] прямо предлагает смещать стандарт безопасности от behavior-only testing к оценке понимания модели.
- [[sources/hubinger-understanding-based-safety-evals]] подчеркивает, что такой стандарт должен быть method-agnostic и ужесточаться вместе с ростом capabilities.
- [[sources/hubinger-understanding-based-safety-evals]] обсуждает causal scrubbing, auditing games и prediction-based evaluation как потенциальные компоненты, но не как готовое решение.
- [[sources/apollo-starter-guide-evals]] допускает, что interpretability-based evals в будущем могут давать более точную информацию, чем одни behavioral tests.
- [[sources/barnett-thiergart-evals-catastrophic-risks]] не вводит этот термин напрямую, но подробно описывает ограничения current behavior-based paradigm, на фоне которых запрос на более сильный стандарт становится понятнее.
- [[sources/igor-ivanov-what-is-an-evaluation]] помогает уточнить еще одну проблему behavior-only testing: модели могут реагировать на eval-like context, а значит поведение на тесте и вне теста не обязано совпадать.

## Рабочая интерпретация
- В логике week-01 этот концепт выглядит как ответ на проблему: поведение модели еще не равно знанию о том, почему оно такое и что произойдет вне тестового режима.
- Understanding-based evals не отменяют behavioral evals, а повышают планку для safety claims в тех случаях, где важно не только поймать failure, но и иметь основания ожидать его отсутствия.
- Evaluation awareness и sandbagging усиливают мотивацию для understanding-based подхода: если поведение зависит от распознавания тестового контекста, требуется более глубокий тип evidence.

## Открытые вопросы
- Как именно демонстрировать понимание модели так, чтобы это нельзя было подменить красивым post-hoc explanation?
- Какие инструменты interpretability или audit design могут стать частью такого стандарта без жесткой привязки к одной школе методов?

## Связанные страницы
- [[weeks/week-01]]
- [[sources/apollo-starter-guide-evals]]
- [[sources/hubinger-understanding-based-safety-evals]]
- [[sources/barnett-thiergart-evals-catastrophic-risks]]
- [[sources/igor-ivanov-what-is-an-evaluation]]
- [[concepts/evals]]
- [[concepts/behavioral-evals]]
- [[concepts/evaluation-awareness]]
- [[syntheses/evals-scope-and-limits]]
