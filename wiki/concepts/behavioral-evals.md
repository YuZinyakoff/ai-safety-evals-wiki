# Behavioral Evals

## Что это такое
Behavioral evals судят о модели по наблюдаемому поведению: ответам, действиям, выполнению задач и реакциям в тестовых сценариях. Это самый естественный и самый распространенный тип evaluation, потому что его проще всего запускать и интерпретировать на поверхности.

## Почему это важно на первой неделе
Week-01 почти целиком крутится вокруг силы и пределов behavior-based evidence. Сначала этот подход вводится как базовый язык области, а затем шаг за шагом показывается, где именно он начинает давать слишком слабые или слишком хрупкие сигналы.

## Что видно по источникам
- [sources/apollo-starter-guide-evals](../sources/apollo-starter-guide-evals.md) отмечает, что современные evals в основном являются behavioral measurements.
- [sources/apollo-starter-guide-evals](../sources/apollo-starter-guide-evals.md) прямо предупреждает, что такие оценки покрывают только малую часть input space и уменьшают неопределенность лишь частично.
- [sources/hubinger-understanding-based-safety-evals](../sources/hubinger-understanding-based-safety-evals.md) утверждает, что behavioral evaluations недостаточны как final standard for alignment, потому что опасная система может скрывать свои свойства.
- [sources/barnett-thiergart-evals-catastrophic-risks](../sources/barnett-thiergart-evals-catastrophic-risks.md) показывает, что behavioral evals надежнее всего устанавливают lower bounds, но не upper bounds на capabilities.
- [sources/barnett-thiergart-evals-catastrophic-risks](../sources/barnett-thiergart-evals-catastrophic-risks.md) отдельно подчеркивает проблемы under-elicitation, sandbagging, weak forecasting и unknown unknown threat vectors.
- [sources/igor-ivanov-what-is-an-evaluation](../sources/igor-ivanov-what-is-an-evaluation.md) добавляет, что модели могут распознавать benchmark-like prompt features и вести себя по-разному в eval-like и deployment-like contexts.
- [sources/prompt-sensitivity-benchmark](../sources/prompt-sensitivity-benchmark.md) показывает, что результаты модели могут заметно меняться даже при slight prompt variations.

## Как этим пользоваться при повторении
- Behavioral evals особенно полезны как инструменты обнаружения, elicitation и грубой калибровки риска.
- Их ключевая слабость в отрицательных выводах: если тест ничего не нашел, из этого плохо следует, что опасной способности или склонности нет.
- Для misuse risk они могут быть частично полезны при сильных организационных и security assumptions, но для misalignment и autonomy risks behavior-only evidence выглядит гораздо слабее.
- Дополнительная слабость behavior-only подхода в том, что observed behavior зависит не только от capability модели, но и от phrasing prompt, perceived context и качества elicitation.

Полезная проверка при перечитывании такая: если вывод из eval звучит как сильное "значит модель безопасна" или "значит этой способности точно нет", стоит вернуться к этой странице и посмотреть, не требуем ли мы от behavioral evidence больше, чем она обычно может дать.

## С чем легко перепутать
- Behavioral evals легко принять за все evals вообще, хотя week-01 как раз показывает, что это только один тип evidence.
- Провал или успех behavioral test легко прочитать как сильный вывод об отсутствии или наличии свойства, хотя такие тесты надежнее работают как lower bounds и грубая калибровка.
- Высокий score на поведении легко спутать с evidence об alignment, хотя в источниках эта экстраполяция как раз систематически критикуется.

## Открытые вопросы
- Можно ли существенно расширить coverage behavioral evals без перехода к другому типу evidence?
- Какие режимы red-teaming и elicitation реально меняют силу выводов, а какие только создают иллюзию полноты?
- Как минимизировать влияние evaluation awareness и prompt sensitivity на результаты behavioral evals?

## Связанные страницы
- [weeks/week-01](../weeks/week-01.md)
- [sources/apollo-starter-guide-evals](../sources/apollo-starter-guide-evals.md)
- [sources/hubinger-understanding-based-safety-evals](../sources/hubinger-understanding-based-safety-evals.md)
- [sources/barnett-thiergart-evals-catastrophic-risks](../sources/barnett-thiergart-evals-catastrophic-risks.md)
- [sources/igor-ivanov-what-is-an-evaluation](../sources/igor-ivanov-what-is-an-evaluation.md)
- [sources/prompt-sensitivity-benchmark](../sources/prompt-sensitivity-benchmark.md)
- [concepts/evals](evals.md)
- [concepts/evaluation-awareness](evaluation-awareness.md)
- [concepts/prompt-sensitivity](prompt-sensitivity.md)
- [concepts/understanding-based-evals](understanding-based-evals.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
