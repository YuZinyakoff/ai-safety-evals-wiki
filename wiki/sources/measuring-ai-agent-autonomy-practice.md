# Measuring AI Agent Autonomy In Practice

- **Тип источника:** extra
- **Неделя:** week-04
- **Raw:** [clipped `.md`](<../../raw/week-04/extra/Measuring AI agent autonomy in practice.md>)
- **Оригинал:** [Anthropic](https://www.anthropic.com/research/measuring-agent-autonomy)
- **Полнота raw:** хороший web-clipped Markdown

## Ключевая мысль
> **Autonomy агента нельзя понять только из pre-deployment evals.** В реальном использовании autonomy co-constructed моделью, пользователем и продуктом, а значит post-deployment monitoring становится отдельным источником evidence.

## Зачем источник в базе
Это важный deployment-side контрапункт к остальной неделе. Он показывает, что agent evaluation не заканчивается в лаборатории: полезно смотреть и на то, как autonomy, oversight и interruption patterns выглядят в реальном использовании.

## Краткое содержание
Anthropic анализирует миллионы human-agent interactions в Claude Code и public API, чтобы посмотреть, как фактически используются агенты. Текст сначала объясняет methodological difficulty: трудно даже operationalize, что считать агентом и как наблюдать за ним privacy-preserving способом. Затем работа вводит practical proxies for autonomy and risk и показывает несколько эмпирических паттернов: longest autonomous runs в Claude Code растут, опытные пользователи чаще дают auto-approve, но и чаще прерывают агента, а сами агенты нередко останавливаются и просят clarification. Далее paper показывает, что agentic activity уже появляется и в riskier domains, но пока в основном сосредоточена в software engineering. Финал текста важен рекомендациями: model developers и product developers должны вкладываться в post-deployment monitoring, uncertainty-aware behavior и tooling for oversight.

## Что здесь особенно важно
- **Real-world autonomy** не сводится к abstract capability.
- **Oversight** бывает не только human-initiated, но и agent-initiated.
- **Monitoring infrastructure** становится частью safety story.
- **Public API / product data** дают другой тип evidence, чем benchmark scores.

## Что это добавляет к теме недели
Этот текст сильно расширяет meaning of evaluation. После него week-04 перестает быть только неделей про lab protocols и становится неделей про связь pre-deployment assessment с actual deployment behavior.

## Что стоит запомнить при повторении
- **Autonomy in practice** может отставать от reachable capability.
- **User behavior** меняет видимый уровень autonomy не меньше, чем model quality.
- **Monitoring is part of agent safety.**

## Связанные концепты
- [concepts/agent-autonomy](../concepts/agent-autonomy.md)
- [concepts/agent-evaluation](../concepts/agent-evaluation.md)
- [concepts/agent-reliability](../concepts/agent-reliability.md)

## Что осталось неясным / спорным
- Насколько выводы из Claude Code и Anthropic API generalize на другие agent products?
- Как сочетать privacy constraints с полезным monitoring for safety?

## Связанные страницы
- [weeks/week-04](../weeks/week-04.md)
- [sources/metr-autonomy-evaluation-resources](metr-autonomy-evaluation-resources.md)
- [syntheses/agent-evals-beyond-task-success](../syntheses/agent-evals-beyond-task-success.md)
