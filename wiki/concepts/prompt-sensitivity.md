# Prompt Sensitivity

## Что это такое
Prompt sensitivity — это зависимость качества ответа модели от небольших изменений формулировки одного и того же запроса. В контексте evals это важно не только как тема prompt engineering, но и как источник искажения измерения.

## Почему это важно на первой неделе
Week-01 много говорит про under-elicitation и limits of behavioral evidence. Prompt sensitivity делает эту проблему очень наглядной: иногда observed capability меняется не потому, что модель "может / не может", а потому что prompt оказался удачным или неудачным.

## Что видно по источникам
- [sources/prompt-sensitivity-benchmark](../sources/prompt-sensitivity-benchmark.md) формализует prompt sensitivity как benchmark problem и вводит задачу Prompt Sensitivity Prediction.
- [sources/prompt-sensitivity-benchmark](../sources/prompt-sensitivity-benchmark.md) показывает, что slight prompt variations могут менять answerability даже при сохранении одного information need.
- [sources/apollo-starter-guide-evals](../sources/apollo-starter-guide-evals.md) подчеркивает важность prompting и LLM steering как базовых навыков evaluator.
- [sources/inspect-ai-tutorial-week-01](../sources/inspect-ai-tutorial-week-01.md) на практике работает с `prompt_template`, solver design и несколькими типами prompt formatting.

## Как этим пользоваться при повторении
- Prompt sensitivity полезно держать в голове как более конкретный механизм under-elicitation.
- Если оценка capability сильно зависит от phrasing, то reliability eval partly depends on elicitation quality, а не только на самой модели.
- Этот концепт удобно читать вместе с [concepts/inspect-ai](inspect-ai.md), потому что именно там становится видно, как prompt design входит в сам workflow.

Хорошая практическая интуиция такая: prompt sensitivity не всегда означает, что модель "плохая", но почти всегда означает, что measurement fragile. Для недели 01 это и есть главный урок из этого концепта.

## С чем легко перепутать
- Prompt sensitivity легко свести к бытовому prompt engineering, хотя для week-01 это прежде всего проблема надежности измерения.
- Ее легко спутать со случайным шумом, хотя paper показывает систематические и предсказуемо важные различия между формулировками.
- Чувствительность к phrasing не всегда означает отсутствие capability, но почти всегда означает, что observed result нельзя читать слишком прямолинейно.

## Открытые вопросы
- Как отделить prompt sensitivity от реального отсутствия capability?
- Какие prompt-construction practices уменьшают искажения в eval settings?

## Связанные страницы
- [weeks/week-01](../weeks/week-01.md)
- [sources/prompt-sensitivity-benchmark](../sources/prompt-sensitivity-benchmark.md)
- [sources/apollo-starter-guide-evals](../sources/apollo-starter-guide-evals.md)
- [sources/inspect-ai-tutorial-week-01](../sources/inspect-ai-tutorial-week-01.md)
- [concepts/behavioral-evals](behavioral-evals.md)
- [concepts/inspect-ai](inspect-ai.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
