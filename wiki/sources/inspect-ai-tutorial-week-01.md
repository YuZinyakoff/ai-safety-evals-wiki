# Inspect AI Tutorial Week 01

- Тип источника: notebook
- Неделя: week-01
- Raw: `raw/week-01/notebooks/inspect_ai_tutorial_week_1 (1).ipynb`

## Краткое содержание
Практический ноутбук по первым шагам в Inspect AI. Он знакомит с базовой структурой `Task`, показывает простые solver/scorer pipelines, вводит `inspect view` и предлагает несколько упражнений, включая собственные benchmark tasks и мини-эксперимент на position bias.

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

## Результаты и ограничения
- Сохраненных outputs в ноутбуке нет: кодовые ячейки не были выполнены.
- Несколько заданий оставлены как `# YOUR CODE HERE`, так что notebook служит не готовым экспериментом, а учебным scaffold.
- Практический смысл notebook в том, что он переводит абстрактный разговор про evals в воспроизводимый workflow.

## Интерпретация
- Это главный практический источник недели: он показывает, как evals operationalize на уровне tooling.
- В связке с теоретическими текстами notebook полезен как напоминание, что надежность evals зависит не только от идей, но и от конкретного task design: samples, prompts, solvers, scorers, logging и анализа результатов.

## Открытые вопросы
- Какие из показанных шаблонов task design лучше всего подходят для safety-relevant evaluations, а какие только для обучения базовой механике?
- Как быстро учебный benchmark переходит в misleading proxy, если его использовать как основную метрику capability?

## Связанные страницы
- [[weeks/week-01]]
- [[concepts/inspect-ai]]
- [[concepts/prompt-sensitivity]]
- [[concepts/evals]]
- [[syntheses/evals-scope-and-limits]]
