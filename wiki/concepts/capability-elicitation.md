# Capability Elicitation

## Коротко
> **Capability elicitation** — это попытка измерять не только "как модель работает в исходной конфигурации", но и какие способности разумно достижимы через prompting, tooling, scaffolding и другие умеренные улучшения.

## Почему это важный концепт
Week-04 показывает, что agent eval легко занижает реальные capabilities. Если слабый prompt, неудачный tool interface или плохой loop structure мешают агенту проявить свои способности, итоговый score будет частично измерять ошибку evaluators.

## Что сюда обычно входит
- Базовая, но не заведомо слабая конфигурация агента.
- Итерация на dev set, а не на финальном test set.
- Разбор failures по типам: `spurious`, `real`, `tradeoff`.
- Проверки на overfitting, gaming и benchmark artifacts.
- Финальный отчет с качественным разбором failures.

## Что именно здесь ломает наивный вывод
- **"Модель не справилась"** легко означает **"процедура плохо раскрыла capability"**.
- **Лучший observed score** не всегда равен reachable capability ceiling.
- **Benchmark tuning** легко перепутать с честным elicitation.

## Практическая интуиция
Полезно держать три вопроса:
- Что здесь является легко устранимым bottleneck?
- Что похоже на реальное capability limit?
- Какие исправления улучшают этот task distribution ценой ухудшения в других режимах?

Именно здесь полезна тройка `spurious failure` / `real failure` / `tradeoff`.

## С чем легко перепутать
- Elicitation легко принять просто за "хитрый prompt engineering".
- Его легко использовать как оправдание безграничного benchmark optimization.
- Его легко читать как способ поднять score, хотя методологически он нужен, чтобы лучше интерпретировать результат.

## Где смотреть дальше
- [METR elicitation guidelines](../sources/metr-guidelines-capability-elicitation.md)
- [METR resources](../sources/metr-autonomy-evaluation-resources.md)
- [Inspect AI tutorial week-04](../sources/inspect-ai-tutorial-week-04.md)
- [SWE-bench Verified](../sources/swe-bench-verified.md)

## Открытые вопросы
- Где проходит практическая граница между разумным elicitation и over-optimization под eval?
- Можно ли стандартизовать elicitation достаточно хорошо для cross-model comparison?

## Связанные страницы
- [concepts/agent-evaluation](agent-evaluation.md)
- [concepts/agent-scaffolding](agent-scaffolding.md)
- [sources/metr-guidelines-capability-elicitation](../sources/metr-guidelines-capability-elicitation.md)
- [syntheses/agent-evals-beyond-task-success](../syntheses/agent-evals-beyond-task-success.md)
