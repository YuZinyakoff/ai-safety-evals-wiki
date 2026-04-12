# Inspect AI Tutorial Week 04

- **Тип источника:** notebook
- **Неделя:** week-04
- **Raw:** [`.ipynb`](<../../raw/week-04/notebooks/inspect_ai_tutorial_week_4 (1).ipynb>)
- **Полнота raw:** учебный notebook

## Ключевая мысль
> **Agent eval становится наглядным только когда видно саму траекторию агента.** Notebook показывает, как prompts, tools, ReAct loop, message limits и dev/test split меняют не только score, но и тип agent failures.

## Зачем источник в базе
Это практическая опора недели. Notebook нужен, чтобы перевести разговор про elicitation, scaffolding и agent reliability в concrete workflow на `Inspect AI`: собрать ReAct agent, дать ему tools, отделить dev set от test set и посмотреть, как agent performance зависит от design choices.

## Краткое содержание
Notebook начинается с постановки различия между обычным LLM eval и agent eval: агент идет по многошаговой траектории и поэтому создает новые failure modes. Затем tutorial вводит базовые инструменты `Inspect AI`, собственные arithmetic tools и объясняет разницу между naive tool loop и `ReAct`-style loop. После этого идет серия небольших упражнений: пользователь создает `modular_arithmetic` и `sympy_solve` tools, сравнивает plain generation, naive tool use и ReAct agent на toy problems и смотрит на traces. Во второй половине notebook переходит к более реалистичному benchmark layer: подгружает `MATH-500`, выделяет tool-friendly subjects и жестко вводит `dev/test split`, чтобы не переобучать scaffolding под final eval. По смыслу это toy version elicitation pipeline, а не finished empirical study.

## Что здесь особенно важно
- **Scaffolding choices are measurement choices.**
- **Dev/test split** здесь прямо связан с METR-style elicitation discipline.
- **Message limits, tool schema и prompt wording** видимо влияют на agent behavior.
- **Notebook intentionally incomplete.** Здесь много `# YOUR CODE HERE`, это scaffold для обучения, а не finished result.

## Что это добавляет к теме недели
Notebook делает week-04 инженерной. Он показывает, что разговор про agent evaluation — это не только taxonomy и philosophy of measurement, но и набор очень конкретных решений о loop structure, tools, datasets и limits.

## Что стоит запомнить при повторении
- **ReAct** дает не магию, а другую структуру траектории.
- **Доступ к tools сам по себе мало что гарантирует.**
- **Даже учебный eval быстро упирается в discipline around dev/test and iteration.**

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
