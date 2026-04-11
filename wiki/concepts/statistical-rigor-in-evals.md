# Statistical Rigor In Evals

## Коротко
> **Statistical rigor in evals** означает привычку рассматривать evaluation как эксперимент с шумом, ограниченной выборкой и явной неопределенностью. На практике это значит не останавливаться на одном score, а думать про `confidence intervals`, `paired comparisons`, `power`, `sample size` и `minimum detectable effect`.

## Почему это важный концепт
Week-02 делает статистическую часть evals центральной, а не декоративной. Если в week-01 основной вопрос был “какие claims вообще допустимы?”, то здесь вопрос становится строже: **какой вывод о model difference или benchmark performance допустим при данной неопределенности?**

## Как именно здесь ломается вывод
- **Point estimate** читают как итоговый ответ.
- **Statistical significance** путают с practical importance.
- **Большее число повторов `K`** путают с большим числом вопросов `n`.
- **Error bars** принимают за cure-all, хотя они не решают проблему плохого benchmark design.

## Как распознать статистически слабый eval
- В paper или internal report есть один score, но нет uncertainty around estimate.
- Сравниваются две модели, но неясно, был ли question-level overlap и использовался ли paired analysis.
- Не обсуждаются detectable effect sizes и достаточность sample size.
- Делается далеко идущий claim при очень небольшом `n` или noisy setup.

## Практическая интуиция
Полезно помнить: **хороший eval design включает не только dataset и scorer, но и честный ответ на вопрос, насколько наблюдаемый эффект может быть шумом**. Без этого даже аккуратно собранный benchmark workflow легко превращается в красивую, но слабую статистически историю.

## С чем легко перепутать
- Statistical significance легко спутать с practical importance.
- Confidence interval легко принять за признак хорошего benchmark сам по себе.
- Paired analysis легко недооценить как “техническую деталь”, хотя для model comparison он часто меняет силу вывода радикально.

## Где смотреть дальше
- [Miller](../sources/miller-adding-error-bars-to-evals.md) — главный source по статистической дисциплине недели.
- [Inspect AI tutorial](../sources/inspect-ai-tutorial-week-02.md) — где эти идеи operationalize на workflow.
- [Benchmarking](benchmarking.md) — где видно, почему без statistical layer benchmark ranking слишком хрупок.

## Открытые вопросы
- Какие методы uncertainty estimation лучше всего подходят для open-ended или clustered evaluation settings?
- Какой минимум statistical reporting стоит считать обязательным для benchmark comparisons?

## Связанные страницы
- [concepts/benchmarking](benchmarking.md)
- [concepts/evaluation-generalization](evaluation-generalization.md)
- [concepts/inspect-ai](inspect-ai.md)
- [syntheses/benchmarking-beyond-single-scores](../syntheses/benchmarking-beyond-single-scores.md)
