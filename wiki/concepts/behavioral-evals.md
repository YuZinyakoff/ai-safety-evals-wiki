# Behavioral Evals

## Коротко
> **Behavioral evals** судят о системе по наблюдаемому поведению: ответам, действиям, выполнению задач и реакциям в тестовых сценариях. Это самый естественный и самый распространенный тип evidence, но именно поэтому его особенно легко переоценить.

## Почему это важный концепт
Week-01 почти целиком крутится вокруг силы и пределов behavior-based evidence. Behavioral evals удобны, потому что они напрямую работают с тем, что система делает. Но именно на этой поверхности возникает главная опасность: хочется думать, что раз мы увидели поведение, то мы уже почти поняли систему. Неделя показывает, что это слишком сильный переход.

## Как именно здесь ломается вывод
- **Lower bounds сильнее upper bounds.** Если модель что-то смогла показать, это сильный сигнал о наличии способности. Если не смогла, это слабый сигнал об ее отсутствии.
- **Elicitation matters.** Результат зависит не только от модели, но и от того, насколько хорошо мы сумели ее раскрыть.
- **Context matters.** Модель может реагировать на признаки eval-like среды, а не только на саму задачу.
- **Prompt matters.** Даже малое изменение phrasing может изменить answerability.
- **Objective matters.** Иногда то, что мы измеряем, вообще плохо совпадает с тем, что нас реально интересует.

## Как распознать этот риск в реальном eval
- Когда из провала теста делают вывод “значит способности нет”.
- Когда из безопасного поведения в benchmark setting делают вывод “значит система aligned”.
- Когда score читают без вопроса о prompt design, scaffolding, logs и threat model.
- Когда benchmark output принимают за почти готовый safety case.

## Практическая интуиция
Полезно помнить такую формулу: **behavioral evals хороши для обнаружения, калибровки и lower bounds, но хуже подходят для сильных отрицательных claims и особенно для alignment guarantees**. Это не значит, что их нужно выбросить. Это значит, что нужно аккуратно ограничивать силу вывода.

## С чем легко перепутать
- Behavioral evals легко принять за все evals вообще, хотя это только один тип evidence.
- Высокий score легко спутать с evidence об alignment, хотя источники недели именно против этой экстраполяции и выступают.
- Failure finding легко спутать с полной coverage, хотя under-elicitation и unknown unknowns делают такую уверенность опасной.

## Где смотреть дальше
- [Hubinger](../sources/hubinger-understanding-based-safety-evals.md) — почему behavior-only standard слишком слаб для alignment.
- [Barnett-Thiergart](../sources/barnett-thiergart-evals-catastrophic-risks.md) — где именно проходят границы claims.
- [Prompt Sensitivity](../sources/prompt-sensitivity-benchmark.md) и [Ivanov](../sources/igor-ivanov-what-is-an-evaluation.md) — два конкретных механизма хрупкости.

## Открытые вопросы
- Можно ли существенно расширить coverage behavioral evals без перехода к другому типу evidence?
- Какие режимы `red-teaming` и elicitation реально меняют силу выводов, а какие только создают иллюзию полноты?
- Как минимизировать влияние `evaluation awareness` и `prompt sensitivity` на результаты behavioral evals?

## Связанные страницы
- [concepts/evals](evals.md)
- [concepts/understanding-based-evals](understanding-based-evals.md)
- [concepts/evaluation-awareness](evaluation-awareness.md)
- [concepts/prompt-sensitivity](prompt-sensitivity.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
