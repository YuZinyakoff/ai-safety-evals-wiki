# Inspect AI Tutorial Week 01

- **Тип источника:** notebook
- **Неделя:** week-01
- **Raw:** [`.ipynb`](<../../raw/week-01/notebooks/inspect_ai_tutorial_week_1 (1).ipynb>)
- **Полнота raw:** учебный notebook

## Ключевая мысль
> **Практика нужна не после теории, а вместе с ней:** notebook показывает, что reliability eval складывается из очень конкретных решений о `Task`, prompt, solver, scorer и логах.

## Зачем источник в базе
Это практическая опора недели. Ноутбук нужен не ради готовых результатов, а как точка, где разговор про evals превращается в воспроизводимый workflow. Его ценность в том, что он делает маленькие engineering choices видимыми и обсуждаемыми.

## Эпистемический статус и как на него смотреть
Это учебный notebook-scaffold, а не finished empirical study. Его полезно читать как guided tour по тому, где в реальном eval pipeline появляются dataset, prompt, solver, scorer и logs.

## На какие вопросы источник помогает отвечать
- Как `Inspect AI` собирает базовый eval из `dataset -> solver -> scorer`?
- Где prompt and scorer choices начинают влиять на measurement еще до всякой статистики?
- Зачем смотреть логи, если есть итоговый score?
- Как даже учебный benchmark быстро превращается в набор design assumptions?

## Краткое содержание
Ноутбук устроен как постепенный tutorial, который наращивает evaluation workflow шаг за шагом. В начале он проходит через setup и первый “hello world” запуск, чтобы показать базовую механику `Inspect AI`. Затем материал переходит к устройству `Task`: как задаются `dataset`, `solver` и `scorer`, как работают `system_message`, `prompt_template`, `chain_of_thought`, `multiple_choice` и простые scoring patterns. После этого tutorial двигается к более содержательным упражнениям: собственные single-choice и multiple-choice tasks, работа с metadata, несколько корректных ответов и мини-эксперимент про `position bias` в benchmark settings. Отдельный слой ноутбука — `inspect view` и просмотр логов, чтобы не сводить eval к одному числу. Это не большой research artifact, а учебный scaffold, который показывает, из каких конкретных инженерных решений собирается даже самый базовый eval.

## Как читать источник быстро
- Если нужен быстрый first pass, смотри setup, sections про `Task`, затем блоки про prompt/scorer choices и `inspect view`.
- Если важен engineering layer, концентрируйся на упражнениях с single-choice / multiple-choice tasks, metadata и scoring patterns.
- Если хочется использовать notebook как anti-score reminder, не пропускай log inspection и position-bias exercise.

## Что здесь особенно важно
- **`Task` как единица анализа.** Это хороший способ мыслить eval не как “один запуск модели”, а как явно собранный pipeline.
- **Prompt и scorer — часть measurement.** Notebook хорошо показывает, что reliability живет не только в dataset.
- **Логи важны не меньше итоговой метрики.** `inspect view` здесь важен именно как antidote к поверхностному чтению score.
- **Учебные benchmarks уже содержат assumptions.** Это полезная интуиция для всей дальнейшей части курса.
- **Материал не завершен как эксперимент.** Несколько мест оставлены как `# YOUR CODE HERE`, так что notebook не надо переоценивать как источник результатов.

## Цель ноутбука
- Подключить `Inspect AI` к модели.
- Запустить первую evaluation.
- Понять структуру `dataset -> solver -> scorer`.
- Научиться смотреть результаты через `inspect view`.
- Собрать собственные single-choice и multiple-choice tasks.

## Setup
- **Среда:** Python 3 / Jupyter notebook.
- **Пакеты:** `inspect-ai`, `openai`.
- **Локальный вариант:** Ollama.
- **Провайдеры в примерах:** Perplexity и SambaNova.

## Данные / задача / модели / scorer
- **Базовая сущность:** `Task`, состоящая из dataset, solver и scorer.
- **Компоненты:** `Sample`, `generate`, `system_message`, `prompt_template`, `chain_of_thought`, `multiple_choice`.
- **Scoring:** `match`, `exact`, `pattern`, `choice`.
- **Демонстрационные модели:** `ollama/llama2`, `perplexity/sonar`, `sambanova/DeepSeek-V3.1`.
- **Упражнения:** hello-world eval, system prompts, prompt templates, CoT, yes/no classification, metadata in MC tasks, multiple correct answers, мини-эксперимент по position bias.

## Что это добавляет к теме недели
Notebook делает week-01 менее абстрактной. После него уже трудно думать об evals как о чисто концептуальной теме: становится видно, где именно в реальном workflow появляются те assumptions, о которых говорят теоретические тексты. Это особенно полезно для повторения курса, потому что многие будущие споры про benchmarking, elicitation и statistical interpretation удобнее держать в голове через concrete pipeline.

## Что стоит запомнить при повторении
- **Good eval** — это не только хороший dataset, но и аккуратный `solver` и `scorer`.
- **Logs matter.** Если не смотришь логи, легко переоценить смысл итоговой метрики.
- **Учебный scaffold** полезен именно тем, что показывает места, где evaluation design может сломаться.

## Результаты и ограничения
- Сохраненных outputs в notebook нет: кодовые ячейки не были выполнены.
- Несколько заданий оставлены как `# YOUR CODE HERE`.
- Практический смысл notebook — учебный scaffold, а не законченный empirical report.

## Связанные концепты
- [concepts/inspect-ai](../concepts/inspect-ai.md)
- [concepts/evals](../concepts/evals.md)
- [concepts/prompt-sensitivity](../concepts/prompt-sensitivity.md)

## Что осталось неясным / спорным
- Какие из показанных шаблонов task design лучше всего подходят для safety-relevant evaluations, а какие в первую очередь учебные?
- Как быстро учебный benchmark превращается в misleading proxy, если его использовать как основную метрику capability?

## Связанные страницы
- [weeks/week-01](../weeks/week-01.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
