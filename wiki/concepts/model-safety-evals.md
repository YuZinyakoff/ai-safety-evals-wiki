# Model Safety Evals

## Коротко
> **Model safety evaluations** оценивают прежде всего outputs модели как таковые: что она способна выдать, насколько ответы точны, надежны, вредны или уязвимы к определенным prompts. Это useful signal о самой модели, но не автоматический ответ на вопрос о downstream impact.

## Почему это важный концепт
Week-02 делает это различие явным. После первой недели легко говорить просто “evals”, но на второй неделе становится полезно спрашивать точнее: **мы сейчас измеряем свойства outputs модели или последствия ее использования в мире?** Без этого различия benchmark results очень легко переинтерпретировать.

## На какой вопрос отвечают model-side evals
- **Может ли модель сделать X?**
- **Насколько хорошо она решает controlled task?**
- **Насколько outputs вредны, biased или unsafe under specified conditions?**

Эти вопросы полезны и важны. Но они не эквивалентны вопросу “что пользователь реально сможет сделать с этой моделью в контексте?”.

## Где здесь чаще всего ломается вывод
- Высокий benchmark score легко принять за proxy for deployment readiness.
- Model-side capability легко спутать с downstream usefulness для malicious actor.
- Чистый measurement outputs легко переоценить как evidence about whole risk landscape.

## Практическая интуиция
Model safety evals особенно полезны, когда нужно измерять capability, accuracy, calibration или prompt-triggered behavior на controlled tasks. Они дают более чистый signal о том, что модель делает на заданных inputs. Но именно поэтому их полезно читать вместе с [contextual safety evals](contextual-safety-evals.md): различие между **capable** и **useful in context** критично для week-02.

## С чем легко перепутать
- Model safety evaluations легко спутать с полной оценкой risk landscape, хотя они измеряют лишь output-side evidence.
- Их легко читать как answer to misuse questions, хотя вредоносная полезность модели зависит еще и от человека, workflow и внешнего контекста.
- Высокий model-side score не равен automatically safe deployment decision.

## Где смотреть дальше
- [CSET explainer](../sources/cset-ai-safety-evaluations-explainer.md) — лучший вход в distinction.
- [Benchmarking](benchmarking.md) — controlled slice of model behavior.
- [Contextual Safety Evals](contextual-safety-evals.md) — соседний тип evidence, который часто нужен для более сильного claim.

## Открытые вопросы
- Какие model-side measurements лучше всего предсказывают downstream risk, а какие почти не переносятся в real-world settings?
- Где проходит граница между model eval и hybrid setup, в котором уже начинают доминировать contextual variables?

## Связанные страницы
- [concepts/contextual-safety-evals](contextual-safety-evals.md)
- [concepts/benchmarking](benchmarking.md)
- [concepts/evals](evals.md)
- [syntheses/benchmarking-beyond-single-scores](../syntheses/benchmarking-beyond-single-scores.md)
