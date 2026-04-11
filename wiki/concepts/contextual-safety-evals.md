# Contextual Safety Evals

## Коротко
> **Contextual safety evaluations** пытаются измерять не только outputs модели, но и влияние доступа к модели на реальные действия, планы, решения и outcomes. Здесь в фокусе уже не просто “что модель может сказать”, а “что пользователь или система с этой моделью реально сможет сделать”.

## Почему это важный концепт
Week-02 делает полезный conceptual shift: одна и та же модель может быть capable of producing information, но это еще не говорит, насколько она useful для malicious actor или как меняет human behavior. Без этого различия легко переоценить model-side benchmarks и недооценить сложность реальных safety claims.

## На какой вопрос отвечают contextual evals
- **Снижает ли модель барьер входа в вредоносную деятельность?**
- **Меняет ли она решения или performance человека в realistic workflow?**
- **Как использование модели влияет на downstream outcomes?**

То есть здесь объект оценки уже включает не только модель, но и человека, процесс и задачу.

## Где здесь чаще всего ломается вывод
- Contextual protocols легко переоценить как прямой прогноз будущего harm.
- Human-heavy setup делает signal более шумным и труднее стандартизируемым.
- Даже realistic-seeming protocol остается proxy, а не прямым окном в весь risk landscape.

## Практическая интуиция
Contextual safety evals потенциально ближе к реальному риску, чем чисто model-side benchmarks, но платой за это становится больший noise и более сложная интерпретация. Поэтому их полезно читать не как “лучший benchmark”, а как другой тип evidence со своей ценой и своей полезностью.

## С чем легко перепутать
- Contextual safety evals легко спутать с model-side red flags, хотя они измеряют другой объект: interaction between model, user and task context.
- Их легко читать как прямой forecast будущего harm, хотя сами источники подчеркивают proxy nature и interpretive uncertainty.
- `Red-teaming` не покрывает весь класс contextual evals, а только один из подходов внутри него.

## Где смотреть дальше
- [CSET explainer](../sources/cset-ai-safety-evaluations-explainer.md) — главный вход в distinction.
- [Model Safety Evals](model-safety-evals.md) — соседний тип evidence, с которым эту страницу особенно полезно читать вместе.
- [Awesome LLM Eval](../sources/awesome-llm-eval.md) — reminder, что benchmark catalogs не заменяют contextual thinking.

## Открытые вопросы
- Какие contextual protocols лучше всего балансируют realism и reproducibility?
- Насколько можно стандартизировать human-heavy evaluations без потери содержательной валидности?

## Связанные страницы
- [concepts/model-safety-evals](model-safety-evals.md)
- [concepts/evals](evals.md)
- [concepts/benchmarking](benchmarking.md)
- [syntheses/benchmarking-beyond-single-scores](../syntheses/benchmarking-beyond-single-scores.md)
