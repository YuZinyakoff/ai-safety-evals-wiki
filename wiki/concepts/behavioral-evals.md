# Behavioral Evals

## Суть
Behavioral evals судят о модели по наблюдаемому поведению: ответам, действиям, выполнению задач и реакциям в тестовых сценариях.

## Факты из источников
- [[sources/apollo-starter-guide-evals]] отмечает, что современные evals в основном являются behavioral measurements.
- [[sources/apollo-starter-guide-evals]] прямо предупреждает, что такие оценки покрывают только малую часть input space и уменьшают неопределенность лишь частично.
- [[sources/hubinger-understanding-based-safety-evals]] утверждает, что behavioral evaluations недостаточны как final standard for alignment, потому что опасная система может скрывать свои свойства.
- [[sources/barnett-thiergart-evals-catastrophic-risks]] показывает, что behavioral evals надежнее всего устанавливают lower bounds, но не upper bounds на capabilities.
- [[sources/barnett-thiergart-evals-catastrophic-risks]] отдельно подчеркивает проблемы under-elicitation, sandbagging, weak forecasting и unknown unknown threat vectors.
- [[sources/igor-ivanov-what-is-an-evaluation]] добавляет, что модели могут распознавать benchmark-like prompt features и вести себя по-разному в eval-like и deployment-like contexts.
- [[sources/prompt-sensitivity-benchmark]] показывает, что результаты модели могут заметно меняться даже при slight prompt variations.

## Рабочая интерпретация
- Behavioral evals особенно полезны как инструменты обнаружения, elicitation и грубой калибровки риска.
- Их ключевая слабость в отрицательных выводах: если тест ничего не нашел, из этого плохо следует, что опасной способности или склонности нет.
- Для misuse risk они могут быть частично полезны при сильных организационных и security assumptions, но для misalignment и autonomy risks behavior-only evidence выглядит гораздо слабее.
- Дополнительная слабость behavior-only подхода в том, что observed behavior зависит не только от capability модели, но и от phrasing prompt, perceived context и качества elicitation.

## Открытые вопросы
- Можно ли существенно расширить coverage behavioral evals без перехода к другому типу evidence?
- Какие режимы red-teaming и elicitation реально меняют силу выводов, а какие только создают иллюзию полноты?
- Как минимизировать влияние evaluation awareness и prompt sensitivity на результаты behavioral evals?

## Связанные страницы
- [[weeks/week-01]]
- [[sources/apollo-starter-guide-evals]]
- [[sources/hubinger-understanding-based-safety-evals]]
- [[sources/barnett-thiergart-evals-catastrophic-risks]]
- [[sources/igor-ivanov-what-is-an-evaluation]]
- [[sources/prompt-sensitivity-benchmark]]
- [[concepts/evals]]
- [[concepts/evaluation-awareness]]
- [[concepts/prompt-sensitivity]]
- [[concepts/understanding-based-evals]]
- [[syntheses/evals-scope-and-limits]]
