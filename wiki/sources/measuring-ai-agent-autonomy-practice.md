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

## Эпистемический статус и как на него смотреть
Это deployment-measurement research note using product telemetry, а не benchmark paper. Его полезно читать как источник другого типа evidence: what autonomy looks like in practice, not just in pre-deployment tasks.

## На какие вопросы источник помогает отвечать
- Как operationalize autonomy и oversight в реальном использовании продукта?
- Какие empirical patterns authors видят в Claude Code and public API usage?
- Почему post-deployment monitoring дает другой тип evidence, чем benchmark scores?
- Как user behavior and product design со-конструируют visible autonomy?

## Краткое содержание
Anthropic анализирует миллионы human-agent interactions в Claude Code и public API, чтобы посмотреть, как фактически используются агенты. Текст сначала объясняет methodological difficulty: трудно даже operationalize, что считать агентом и как наблюдать за ним privacy-preserving способом. Затем работа вводит practical proxies for autonomy and risk и показывает несколько эмпирических паттернов: longest autonomous runs в Claude Code растут, опытные пользователи чаще дают auto-approve, но и чаще прерывают агента, а сами агенты нередко останавливаются и просят clarification. Далее paper показывает, что agentic activity уже появляется и в riskier domains, но пока в основном сосредоточена в software engineering. Финал текста важен рекомендациями: model developers и product developers должны вкладываться в post-deployment monitoring, uncertainty-aware behavior и tooling for oversight.

## Как читать источник быстро
- Если нужна основная эмпирическая картина, читай methodology for autonomy proxies и ключевые наблюдаемые паттерны использования.
- Если важен safety angle, переходи к sections on interruption, oversight and riskier domains.
- Если нужен практический вывод, не пропускай final recommendations on monitoring infrastructure and oversight tooling.

## Что источник утверждает прямо
- Product telemetry можно использовать, чтобы operationalize proxies for autonomy and oversight in real deployments.
- В наблюдаемом использовании Claude Code и public API длина автономных прогонов растет, паттерны oversight различаются между пользователями, а software engineering остается центральным доменом.
- Real-world autonomy определяется не только model capability, но и user behavior, product design and intervention patterns.
- Post-deployment monitoring and oversight tooling are necessary complements to pre-deployment evals.

## Что здесь особенно важно
- **Real-world autonomy** не сводится к abstract capability.
- **Oversight** бывает не только human-initiated, но и agent-initiated.
- **Monitoring infrastructure** становится частью safety story.
- **Public API / product data** дают другой тип evidence, чем benchmark scores.

## Интерпретация для курса
Для курса этот текст важен как расширение самой идеи evaluation. Он показывает, что autonomy evidence не обязано жить только в benchmark suite: deployment-side traces тоже меняют картину, а значит agent evals нужно думать как часть более широкого socio-technical measurement stack.

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
