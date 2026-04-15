# Inspect AI Tutorial Week 04

- **Тип источника:** notebook
- **Неделя:** week-04
- **Raw:** [`.ipynb`](<../../raw/week-04/notebooks/inspect_ai_tutorial_week_4 (1).ipynb>)
- **Полнота raw:** учебный notebook

## Ключевая мысль
> **Agent eval становится наглядным только когда видно саму траекторию агента.** Notebook показывает, как prompts, tools, ReAct loop, message limits и dev/test split меняют не только score, но и тип agent failures.

## Зачем источник в базе
Это практическая опора недели. Notebook нужен, чтобы перевести разговор про elicitation, scaffolding и agent reliability в concrete workflow на `Inspect AI`: собрать ReAct agent, дать ему tools, отделить dev set от test set и посмотреть, как agent performance зависит от design choices.

## Эпистемический статус и как на него смотреть
Это учебный agent-eval notebook, а не finished benchmark report. Его полезно читать как scaffold, где хорошо видно, как ReAct loop, tools, message limits и dev/test discipline меняют сам объект измерения.

## На какие вопросы источник помогает отвечать
- Как practically собрать простого ReAct-style агента в `Inspect AI`?
- Почему tool schema, loop structure и prompt wording влияют на measured agent behavior?
- Зачем в agent eval так быстро появляется `dev/test split`?
- Как traces помогают увидеть failure modes beyond final score?

## Краткое содержание
Notebook начинается с постановки различия между обычным LLM eval и agent eval: агент идет по многошаговой траектории и поэтому создает новые failure modes. Затем tutorial вводит базовые инструменты `Inspect AI`, собственные arithmetic tools и объясняет разницу между naive tool loop и `ReAct`-style loop. После этого идет серия небольших упражнений: пользователь создает `modular_arithmetic` и `sympy_solve` tools, сравнивает plain generation, naive tool use и ReAct agent на toy problems и смотрит на traces. Во второй половине notebook переходит к более реалистичному benchmark layer: подгружает `MATH-500`, выделяет tool-friendly subjects и жестко вводит `dev/test split`, чтобы не переобучать scaffolding под final eval. По смыслу это toy version elicitation pipeline, а не finished empirical study.

## Как читать источник быстро
- Если нужен shortest route, смотри distinction between LLM eval and agent eval, then ReAct/tool loop sections.
- Если интересует practical elicitation layer, переходи к exercises with tools, traces and `dev/test split`.
- Если нужен benchmark context, смотри final blocks on `MATH-500` and tool-friendly subject selection.

## Что здесь особенно важно
- **Scaffolding choices are measurement choices.**
- **Dev/test split** здесь прямо связан с METR-style elicitation discipline.
- **Message limits, tool schema и prompt wording** видимо влияют на agent behavior.
- **Notebook intentionally incomplete.** Здесь много `# YOUR CODE HERE`, это scaffold для обучения, а не finished result.

## Цель ноутбука
- Собрать простого ReAct-style агента в `Inspect AI`.
- Понять, как tools and loop structure меняют agent trajectories.
- Практически почувствовать dev/test discipline for elicitation.
- Применить agent setup к `MATH-500`-style benchmark slice.

## Setup
- **Среда:** Python 3 / Jupyter notebook.
- **Инструмент:** `Inspect AI`.
- **Agent pattern:** ReAct-style loop with custom tools.
- **Режим:** educational scaffold with `# YOUR CODE HERE`.

## Данные / задача / модели / scorer
- **Toy tasks:** arithmetic-style exercises with custom tools like `modular_arithmetic` and `sympy_solve`.
- **Benchmark layer:** `MATH-500` with tool-friendly subject selection.
- **Object of evaluation:** agent trajectories under different loop and tool setups.
- **Methodological layer:** dev/test split, message limits, tool schema and prompt wording as measurement choices.

## Что это добавляет к теме недели
Notebook делает week-04 инженерной. Он показывает, что разговор про agent evaluation — это не только taxonomy и philosophy of measurement, но и набор очень конкретных решений о loop structure, tools, datasets и limits.

## Что стоит запомнить при повторении
- **ReAct** дает не магию, а другую структуру траектории.
- **Доступ к tools сам по себе мало что гарантирует.**
- **Даже учебный eval быстро упирается в discipline around dev/test and iteration.**

## Результаты и ограничения
- Notebook intentionally incomplete and functions as a scaffold, not a finished empirical report.
- Core output is qualitative understanding of trajectory structure and elicitation discipline, not one final benchmark number.
- `MATH-500` is a narrow reasoning-heavy benchmark slice and does not stand in for general agent competence.
- Improvements found in the notebook may mix real elicitation with benchmark-specific tuning.

## Связанные концепты
- [concepts/inspect-ai](../concepts/inspect-ai.md)
- [concepts/agent-scaffolding](../concepts/agent-scaffolding.md)
- [concepts/react-agents](../concepts/react-agents.md)
- [concepts/capability-elicitation](../concepts/capability-elicitation.md)

## Что осталось неясным / спорным
- Насколько результаты на MATH-500 реально переносятся на более open-ended agents?
- Какие improvements в notebook являются содержательным elicitation, а какие — просто benchmark tuning?

## Связанные страницы
- [weeks/week-04](../weeks/week-04.md)
- [sources/react-synergizing-reasoning-acting](react-synergizing-reasoning-acting.md)
- [sources/math-dataset](math-dataset.md)
- [sources/metr-guidelines-capability-elicitation](metr-guidelines-capability-elicitation.md)
