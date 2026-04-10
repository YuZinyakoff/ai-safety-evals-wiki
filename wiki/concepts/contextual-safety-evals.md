# Contextual Safety Evals

## Что это такое
Contextual safety evaluations пытаются измерять не только outputs модели, но и влияние доступа к модели на реальные действия, планы, решения и outcomes. Здесь в фокусе уже не просто `что модель может сказать`, а `что пользователь или система с этой моделью реально сможет сделать`.

## Почему это важно на второй неделе
Week-02 делает полезный conceptual shift: одна и та же модель может быть capable of producing information, но это еще не говорит, насколько она useful для malicious actor или как меняет human behavior. Без этого различия легко переоценить модельные benchmarks и недооценить сложность real-world safety claims.

## Что видно по источникам
- [sources/cset-ai-safety-evaluations-explainer](../sources/cset-ai-safety-evaluations-explainer.md) вводит contextual safety evaluations как отдельный класс.
- [sources/cset-ai-safety-evaluations-explainer](../sources/cset-ai-safety-evaluations-explainer.md) обсуждает здесь red-teaming и uplift studies.
- [sources/cset-ai-safety-evaluations-explainer](../sources/cset-ai-safety-evaluations-explainer.md) отдельно подчеркивает роль человеческих переменных и трудность стандартизации.
- [sources/awesome-llm-eval](../sources/awesome-llm-eval.md) косвенно полезен как reminder, что каталог benchmarks и tools не заменяет thinking about task context.

## Как этим пользоваться при повторении
- Contextual safety evals нужны, когда нас интересует misuse enablement, barrier lowering, guardrail bypass и другие downstream effects.
- Они потенциально ближе к реальному риску, чем чисто model-side benchmarks, но платой за это становится больший noise и сложность интерпретации.
- При чтении таких результатов полезно помнить: человеческая экспертиза, creativity и process factors могут влиять на outcome не меньше, чем сама модель.

## С чем легко перепутать
- Contextual safety evals легко спутать с model-side red flags, хотя они измеряют другой объект: interaction between model, user and task context.
- Их легко читать как прямой прогноз будущего harm, хотя сами источники подчеркивают proxy nature и interpretive uncertainty.
- Red-teaming не покрывает весь класс contextual evals, а только один из подходов внутри него.

## Открытые вопросы
- Какие contextual protocols лучше всего балансируют realism и reproducibility?
- Насколько можно стандартизировать human-heavy evaluations без потери содержательной валидности?

## Связанные страницы
- [weeks/week-02](../weeks/week-02.md)
- [sources/cset-ai-safety-evaluations-explainer](../sources/cset-ai-safety-evaluations-explainer.md)
- [sources/awesome-llm-eval](../sources/awesome-llm-eval.md)
- [concepts/model-safety-evals](model-safety-evals.md)
- [concepts/evals](evals.md)
- [concepts/benchmarking](benchmarking.md)
