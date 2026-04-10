# Prompt Sensitivity

## Суть
Prompt sensitivity — это зависимость качества ответа модели от небольших изменений формулировки одного и того же запроса.

## Факты из источников
- [[sources/prompt-sensitivity-benchmark]] формализует prompt sensitivity как benchmark problem и вводит задачу Prompt Sensitivity Prediction.
- [[sources/prompt-sensitivity-benchmark]] показывает, что slight prompt variations могут менять answerability даже при сохранении одного information need.
- [[sources/apollo-starter-guide-evals]] подчеркивает важность prompting и LLM steering как базовых навыков evaluator.
- [[sources/inspect-ai-tutorial-week-01]] на практике работает с `prompt_template`, solver design и несколькими типами prompt formatting.

## Рабочая интерпретация
- Prompt sensitivity важна для evals не только как UX-проблема prompt engineering, но и как источник measurement noise.
- Если оценка capability сильно зависит от phrasing, то reliability eval partly depends on elicitation quality, а не только на самой модели.

## Открытые вопросы
- Как отделить prompt sensitivity от реального отсутствия capability?
- Какие prompt-construction practices уменьшают искажения в eval settings?

## Связанные страницы
- [[weeks/week-01]]
- [[sources/prompt-sensitivity-benchmark]]
- [[sources/apollo-starter-guide-evals]]
- [[sources/inspect-ai-tutorial-week-01]]
- [[concepts/behavioral-evals]]
- [[concepts/inspect-ai]]
- [[syntheses/evals-scope-and-limits]]
