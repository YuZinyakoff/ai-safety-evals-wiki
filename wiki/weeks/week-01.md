# Неделя 01

## Навигация
- [[home]]
- [[index]]

## Статус
- Теоретические материалы из `raw/week-01/theory/` разобраны и связаны с source pages.
- Ноутбук из `raw/week-01/notebooks/` разобран и вынесен в отдельную source page.
- Дополнительные материалы из `raw/week-01/extra/` разобраны и связаны с concept pages.

## Фокус недели
Неделя вводит базовый язык evals, но быстро усложняет картину. Источники вместе проходят путь от базовых определений и роли evaluator к критике purely behavioral tests, к вопросу о том, что вообще считать evaluation, к prompt-level failure modes и specification-level failure modes, а затем показывают и практический слой через Inspect AI.

## Источники
### Theory
- [[sources/apollo-starter-guide-evals]] — вводный обзор evals, их типов и полезных навыков evaluator
- [[sources/hubinger-understanding-based-safety-evals]] — аргумент в пользу understanding-based safety evaluations как дополнения к behavioral evals
- [[sources/barnett-thiergart-evals-catastrophic-risks]] — разбор того, что evals могут и не могут сказать о catastrophic risks

### Notebooks
- [[sources/inspect-ai-tutorial-week-01]] — вводный tutorial по Inspect AI, solver/scorer pipelines и `inspect view`

### Extra
- [[sources/igor-ivanov-what-is-an-evaluation]] — почему определение evaluation matters для evaluation awareness и evaluation gaming
- [[sources/deepmind-specification-gaming]] — specification gaming как failure mode objective design
- [[sources/prompt-sensitivity-benchmark]] — prompt sensitivity как источник вариативности ответов и challenge для measurement

## Основные идеи
### Факты из источников
- Evals описываются как систематическое измерение свойств AI-систем, включая их способности и склонности.
- Уже на вводном уровне различаются red-teaming и benchmarking, а также capability evals и alignment evals.
- Определение самого evaluation неочевидно: intent исследователя, consequences interaction и surface features benchmark-like среды не совпадают.
- Поведенческие evals полезны как способ получить lower bounds на наблюдаемые способности модели и улучшить decision-making.
- Для misuse risk текущих моделей evals в принципе могут быть полезны, но только при сильных предпосылках о capability elicitation, threat modeling и преимуществах evaluators над attackers.
- Behavioral evals плохо поддерживают отрицательные claims: провал теста не доказывает отсутствия способности, а успех на безопасном поведении не доказывает alignment.
- Для misalignment и автономных рисков проблема усиливается из-за sandbagging, under-elicitation и слабого понимания внутренних propensities модели.
- Небольшие изменения prompt formulation могут заметно менять answerability, даже если information need остается тем же.
- Specification gaming показывает, что агент может удовлетворять proxy objective и все равно уходить от intended outcome.
- На практическом уровне eval workflow можно явным образом разложить на dataset, solver, scorer и анализ логов.

### Интерпретации
- Центральное напряжение недели такое: evals нужны, но их легко переоценить как safety standard.
- Чем выше stakes и capabilities моделей, тем менее убедительными становятся выводы вида "ничего опасного не нашли, значит опасности нет".
- Идея understanding-based evaluations появляется как ответ на ограниченность behavior-only подхода, особенно в сценариях deception и hidden capabilities.
- Дополнительные материалы уточняют, что unreliable evidence может возникать на разных слоях: в определении eval context, в phrasing prompt и в самой постановке objective.
- Поэтому качество evals зависит не только от "хорошего теста", но и от conceptual clarity, elicitation quality и engineering discipline.

## Практика
- [[sources/inspect-ai-tutorial-week-01]] служит первой практической рамкой недели.
- Цель notebook: собрать базовый eval pipeline и понять структуру `Task`.
- Setup: Python notebook, `inspect-ai`, локальный Ollama или cloud APIs.
- Задачи: hello-world eval, system prompts, prompt templates, chain-of-thought, single-choice и multiple-choice tasks, metadata, multiple correct answers.
- Отдельное упражнение строит мини-эксперимент по position bias в multiple-choice benchmarks.
- Notebook не исполнен и содержит `# YOUR CODE HERE`, поэтому его роль сейчас учебная, а не как источник результатов.

## Связанные концепты
- [[concepts/evals]]
- [[concepts/behavioral-evals]]
- [[concepts/understanding-based-evals]]
- [[concepts/evaluation-awareness]]
- [[concepts/prompt-sensitivity]]
- [[concepts/specification-gaming]]
- [[concepts/inspect-ai]]

## Связанный синтез
- [[syntheses/evals-scope-and-limits]]

## Открытые вопросы
- Какие claims о safety вообще допустимо делать на основании behavioral evals без ложного чувства надежности?
- Можно ли operationalize understanding-based evaluations так, чтобы они были достаточно строгими и при этом method-agnostic?
- Как сочетать evals, interpretability, audits и security controls в одном safety case?
- Как отделять prompt sensitivity от реального отсутствия capability?
- Как строить evals, которые меньше подсказывают модели, что она находится в режиме оценки?
- Как ловить specification gaming до того, как proxy objective станет operational metric?

## Краткий вывод
Неделя 01 теперь покрывает уже не только базовый словарь evals, но и несколько слоев их возможного сбоя. Apollo, Hubinger и Barnett-Thiergart задают общую рамку limits of behavioral evidence. Ivanov добавляет проблему evaluation awareness, paper про prompt sensitivity показывает нестабильность ответа к phrasing, а DeepMind-текст про specification gaming напоминает, что ломаться может и сама objective. Notebook по Inspect AI переводит все это в практику: evals нужно не только обсуждать, но и собирать как явный workflow с контролируемыми design choices.
