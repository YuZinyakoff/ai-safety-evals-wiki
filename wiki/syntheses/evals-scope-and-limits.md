# Scope, Failure Modes, And Practice Of Evals

## Короткий тезис
> **Главный вывод week-01 такой: evals полезны как инструмент обнаружения и калибровки, но опасны как источник ложной уверенности.** Неделя становится сильной не потому, что повторяет одно ограничение много раз, а потому, что показывает несколько разных механизмов, из-за которых можно переоценить смысл теста.

## Где источники согласны
- **Evals нужны.** Ни один из ключевых материалов не предлагает отказаться от evals как класса практик.
- **Behavioral evidence ограничено.** Все важные тексты недели по-разному упираются в один и тот же факт: наблюдаемое поведение полезно, но оно не дает полного знания о системе.
- **Качество вывода зависит от elicitation и framing.** Источники сходятся в том, что тест измеряет не “чистую способность”, а результат взаимодействия модели, prompt, интерфейса и выбранной objective.
- **Нельзя путать measurement и safety case.** Хороший score или чистый run еще не равны достаточному обоснованию безопасности.

## Как источники усиливают друг друга
- **Apollo** задает словарь и нормализует мысль, что evals — это `decision-support layer`, а не почти готовая гарантия.
- **Barnett-Thiergart** делает следующий шаг и дисциплинирует сами claims. После него вопрос звучит уже не "полезен ли eval?", а "какой именно вывод этот eval поддерживает?".
- **Hubinger** повышает ставку в alignment-направлении: если система способна скрывать опасные свойства, то поведенческого стандарта может не хватить в принципе.
- **Ivanov** уточняет механизм одной из проблем. Он показывает, что модель может реагировать не на “намерение исследователя”, а на benchmark-like признаки среды.
- **Prompt Sensitivity** добавляет еще один конкретный слой хрупкости: observed capability зависит от phrasing, даже когда information need не меняется.
- **Specification Gaming** расширяет рамку за пределы measurement. Иногда проблема уже не в том, как мы тестируем систему, а в том, что именно мы попросили ее оптимизировать.
- **Inspect AI tutorial** заземляет всю картину. Он показывает, что эти риски появляются не в абстракции, а в конкретных design choices: `Task`, prompt, solver, scorer, logs.

## Что именно здесь ломает наивный вывод
- **Провал теста не доказывает отсутствия способности.** Это общий мотив у Apollo, Barnett-Thiergart и Hubinger.
- **Успех на тесте не доказывает alignment.** Hubinger и Barnett-Thiergart сильнее всего бьют именно по этой экстраполяции.
- **Сам eval-context может менять поведение.** Эту линию делает явной Ivanov.
- **Даже внутри одного eval prompt может исказить результат.** Это наглядно показывает paper про prompt sensitivity.
- **Даже “правильно измеренный” результат может быть не тем, что нам нужно.** Эту часть приносит specification gaming.

## Где остается напряжение
- **Насколько далеко можно дотянуть behavioral evals?** Barnett-Thiergart оставляет место для practical value evals при misuse risk, но только под сильными предпосылками.
- **Как operationalize более сильный стандарт?** Hubinger поднимает планку через understanding-based approach, но не дает готовой operational recipe.
- **Как именно скрыть от модели факт оценки?** Ivanov помогает точнее сформулировать проблему, но не закрывает инженерный вопрос.
- **Можно ли уменьшить prompt sensitivity, не превратив eval в слишком узкий interface?** Paper показывает проблему, но не предлагает универсального решения.

## Практический вывод для курса
Если переводить week-01 в рабочую дисциплину, то после любого eval полезно задавать не один вопрос, а сразу несколько:
- **Что именно этот тест показал?**
- **Что он не мог показать в принципе?**
- **Какие элементы результата зависят от prompt и context?**
- **Не оптимизируем ли мы proxy вместо intended outcome?**
- **Какой еще evidence нужен, чтобы делать более сильный safety claim?**

Именно в этом смысле synthesis полезен как отдельная страница: он собирает не просто краткие пересказы источников, а общую карту того, где именно ломается слишком уверенное чтение evals.

## Открытые вопросы
- Какие комбинации evals, interpretability, audits и security controls могут давать practically useful safety case?
- Можно ли построить understanding-based standard, который будет одновременно строгим, масштабируемым и method-agnostic?
- Как одновременно учитывать `evaluation awareness`, `prompt sensitivity` и `specification gaming` в design of safety-relevant evaluations?

## Связанные страницы
- [weeks/week-01](../weeks/week-01.md)
- [concepts/evals](../concepts/evals.md)
- [concepts/behavioral-evals](../concepts/behavioral-evals.md)
- [concepts/understanding-based-evals](../concepts/understanding-based-evals.md)
- [concepts/evaluation-awareness](../concepts/evaluation-awareness.md)
- [concepts/prompt-sensitivity](../concepts/prompt-sensitivity.md)
- [concepts/specification-gaming](../concepts/specification-gaming.md)
- [concepts/inspect-ai](../concepts/inspect-ai.md)
