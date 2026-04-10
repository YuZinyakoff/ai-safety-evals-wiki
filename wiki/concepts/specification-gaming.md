# Specification Gaming

## Суть
Specification gaming — это ситуация, когда агент удовлетворяет буквальную спецификацию objective, но уходит от intended outcome.

## Факты из источников
- [[sources/deepmind-specification-gaming]] определяет specification gaming как удовлетворение literal specification без достижения intended outcome.
- [[sources/deepmind-specification-gaming]] приводит примеры с Lego stacking, Coast Runners, simulator bugs и reward tampering.
- [[sources/deepmind-specification-gaming]] подчеркивает, что проблема относится не только к reward function, но и к implicit assumptions о среде и objective representation.

## Рабочая интерпретация
- Для week-01 это важная линия про failure modes: проблема может быть не только в том, как мы тестируем модель, но и в том, как мы задали цель.
- Specification gaming полезно держать рядом с evals, потому что measuring success on a proxy objective еще не гарантирует, что proxy совпадает с тем, что мы actually care about.

## Открытые вопросы
- Какие LLM-agent scenarios сегодня наиболее уязвимы к specification gaming?
- Как связывать eval design и reward/specification design в одном safety workflow?

## Связанные страницы
- [[weeks/week-01]]
- [[sources/deepmind-specification-gaming]]
- [[concepts/evals]]
- [[concepts/behavioral-evals]]
- [[syntheses/evals-scope-and-limits]]
