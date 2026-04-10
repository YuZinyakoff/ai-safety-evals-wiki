# Inspect AI Tutorial Week 01

- Тип источника: notebook
- Неделя: week-01
- Raw: `raw/week-01/notebooks/inspect_ai_tutorial_week_1 (1).ipynb`
- Полнота raw: учебный notebook

## Зачем источник в базе
Это практическая опора недели. Ноутбук нужен не ради готовых результатов, а как точка, где разговор про evals превращается в воспроизводимый workflow: task design, solver pipeline, scorer и просмотр логов.

## Краткое содержание
Практический ноутбук по первым шагам в Inspect AI. Он знакомит с базовой структурой `Task`, показывает простые solver/scorer pipelines, вводит `inspect view` и предлагает несколько упражнений, включая собственные benchmark tasks и мини-эксперимент на position bias. Его ценность не в том, что он решает большую safety-задачу, а в том, что делает видимыми маленькие инженерные решения, из которых потом и складывается качество eval.

## Ключевые идеи
- Evals в tooling-слое удобно мыслить как `Task`, где явно разделены dataset, solver и scorer.
- Даже учебные benchmarks уже зависят от design choices: prompt templates, scoring rules, metadata и inspection of logs.
- `inspect view` важен не меньше самого запуска eval, потому что без просмотра логов легко переоценить итоговую метрику.
- Notebook показывает несколько типовых форматов задач, а не один-единственный canonical pattern.
- Материал лучше читать как scaffold для повторения практики, а не как законченный эксперимент.

## Цель ноутбука
- Подключить Inspect AI к модели.
- Запустить первую evaluation.
- Понять структуру `dataset -> solver -> scorer`.
- Научиться смотреть результаты через `inspect view`.
- Собрать собственные single-choice и multiple-choice tasks.

## Setup
- Язык: Python 3 / Jupyter notebook.
- В ноутбуке предлагается установка `inspect-ai` и `openai`.
- Локальный вариант setup опирается на Ollama.
- Дополнительно показаны примеры работы через API-провайдеров Perplexity и SambaNova.

## Данные / задача / модели / scorer
- Базовая сущность — `Task`, состоящая из dataset, solver и scorer.
- В notebook используются `Sample`, `generate`, `system_message`, `prompt_template`, `chain_of_thought`, `multiple_choice`.
- Для scoring используются `match`, `exact`, `pattern` и `choice`.
- Демонстрационные модели: `ollama/llama2`, `perplexity/sonar`, `sambanova/DeepSeek-V3.1`.
- Упражнения включают hello-world eval, system prompts, prompt templates, CoT, yes/no classification, metadata in MC tasks, multiple correct answers и мини-эксперимент по position bias.

## Что это добавляет к теме недели
Notebook делает неделю менее абстрактной: он показывает, где именно на практике появляются те самые measurement choices, о которых говорят теоретические тексты. Через него удобно повторять, что reliability eval зависит не только от концепта, но и от конкретной реализации task, prompt и scorer. Это особенно полезно при обучении: становится видно, что даже простой учебный benchmark уже содержит assumptions, которые потом хочется уметь замечать и обсуждать.

## Результаты и ограничения
- Сохраненных outputs в ноутбуке нет: кодовые ячейки не были выполнены.
- Несколько заданий оставлены как `# YOUR CODE HERE`, так что notebook служит не готовым экспериментом, а учебным scaffold.
- Практический смысл notebook в том, что он переводит абстрактный разговор про evals в воспроизводимый workflow.

## Связанные концепты
- [concepts/inspect-ai](../concepts/inspect-ai.md)
- [concepts/evals](../concepts/evals.md)
- [concepts/prompt-sensitivity](../concepts/prompt-sensitivity.md)

## Что осталось неясным / спорным
- Какие из показанных шаблонов task design лучше всего подходят для safety-relevant evaluations, а какие только для обучения базовой механике?
- Как быстро учебный benchmark переходит в misleading proxy, если его использовать как основную метрику capability?

## Связанные страницы
- [weeks/week-01](../weeks/week-01.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
