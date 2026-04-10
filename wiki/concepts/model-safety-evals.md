# Model Safety Evals

## Что это такое
Model safety evaluations оценивают outputs модели как таковые: что она способна выдать, насколько ответы точны, надежны, вредны, biased или уязвимы к определенным prompts. Это важный тип evaluation, когда нас интересуют свойства самой модели на уровне поведения и response generation.

## Почему это важно на второй неделе
Week-02 делает это различие явным. После первой недели легко говорить просто "evals", но на второй неделе становится полезно спрашивать точнее: мы сейчас измеряем model outputs или последствия использования модели в мире?

## Что видно по источникам
- [sources/cset-ai-safety-evaluations-explainer](../sources/cset-ai-safety-evaluations-explainer.md) прямо противопоставляет model safety и contextual safety evaluations.
- [sources/cset-ai-safety-evaluations-explainer](../sources/cset-ai-safety-evaluations-explainer.md) относит к model-side approaches capability testing и benchmarking.
- [sources/cao-generalizable-evaluation-llm-era](../sources/cao-generalizable-evaluation-llm-era.md) показывает множество benchmark families для knowledge, reasoning и coding.
- [sources/inspect-ai-tutorial-week-02](../sources/inspect-ai-tutorial-week-02.md) дает практический пример model evaluation через MMLU subset.
- [sources/miller-adding-error-bars-to-evals](../sources/miller-adding-error-bars-to-evals.md) добавляет, что даже внутри model eval point estimates надо читать статистически осторожно.

## Как этим пользоваться при повторении
- Model safety evals особенно полезны, когда надо измерять capability, accuracy, calibration или prompt-triggered behavior на controlled tasks.
- Они дают более чистый signal о том, что модель делает на заданных inputs, но не отвечают автоматически на вопрос о downstream usefulness или real-world impact.
- Именно поэтому week-02 полезно читать эту страницу вместе с [concepts/contextual-safety-evals](contextual-safety-evals.md): различие между `capable` и `useful` там критично.

## С чем легко перепутать
- Model safety evaluations легко спутать с полной оценкой risk landscape, хотя они измеряют лишь output-side evidence.
- Их легко читать как answer to misuse questions, хотя вредоносная полезность модели зависит еще и от человека, workflow и внешнего контекста.
- Высокий benchmark score внутри model eval не равен automatically safe deployment decision.

## Открытые вопросы
- Какие model-side measurements лучше всего предсказывают downstream risk, а какие почти не переносятся в real-world settings?
- Где проходит граница между model eval и hybrid setup, в котором уже появляются contextual variables?

## Связанные страницы
- [weeks/week-02](../weeks/week-02.md)
- [sources/cset-ai-safety-evaluations-explainer](../sources/cset-ai-safety-evaluations-explainer.md)
- [sources/cao-generalizable-evaluation-llm-era](../sources/cao-generalizable-evaluation-llm-era.md)
- [sources/inspect-ai-tutorial-week-02](../sources/inspect-ai-tutorial-week-02.md)
- [sources/miller-adding-error-bars-to-evals](../sources/miller-adding-error-bars-to-evals.md)
- [concepts/contextual-safety-evals](contextual-safety-evals.md)
- [concepts/benchmarking](benchmarking.md)
- [concepts/evals](evals.md)
