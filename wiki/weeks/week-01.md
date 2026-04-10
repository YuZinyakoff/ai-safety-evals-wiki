# Неделя 01

## Навигация
- [home](../home.md)
- [index](../../index.md)

## Зачем открывать эту страницу
Это hub-page первой недели. Ее удобно использовать как точку входа для повторения: отсюда можно быстро вернуть базовый словарь evals, вспомнить, где именно ломаются простые behavioral claims, перейти к дополнительным failure modes и отдельно вернуться к практическому notebook. Если через месяц останется только общее ощущение, что "неделя была про evals и их ограничения", эта страница должна помочь снова разложить тему на понятные части.

## Быстрый маршрут
- Если нужно быстро вернуть базовые определения: начни с [sources/apollo-starter-guide-evals](../sources/apollo-starter-guide-evals.md) и [concepts/evals](../concepts/evals.md).
- Если нужно вспомнить, почему behavioral evidence ограничено: смотри [sources/hubinger-understanding-based-safety-evals](../sources/hubinger-understanding-based-safety-evals.md), [sources/barnett-thiergart-evals-catastrophic-risks](../sources/barnett-thiergart-evals-catastrophic-risks.md) и [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md).
- Если нужно повторить дополнительные failure modes: переходи к [sources/igor-ivanov-what-is-an-evaluation](../sources/igor-ivanov-what-is-an-evaluation.md), [sources/prompt-sensitivity-benchmark](../sources/prompt-sensitivity-benchmark.md) и [sources/deepmind-specification-gaming](../sources/deepmind-specification-gaming.md).
- Если нужен практический вход: открывай [sources/inspect-ai-tutorial-week-01](../sources/inspect-ai-tutorial-week-01.md) и [concepts/inspect-ai](../concepts/inspect-ai.md).

## Статус
- Теоретические материалы из `raw/week-01/theory/` разобраны и связаны с source pages.
- Для Apollo и Hubinger появились clipped Markdown-версии полных текстов; source pages теперь опираются на них как на preferred raw.
- Для Prompt Sensitivity теперь есть более качественный raw-набор: clipped HTML-версия, PDF и TeX source archive.
- Для Barnett-Thiergart пока локально доступен только PDF и fallback-sidecar, поэтому этот источник стоит считать менее удобным для точечной сверки.
- Ноутбук из `raw/week-01/notebooks/` разобран и вынесен в отдельную source page.
- Дополнительные материалы из `raw/week-01/extra/` разобраны и связаны с concept pages.
- Для текста Иванова теперь тоже есть clipped Markdown-версия полного поста.

## Как читать набор материалов
- [sources/apollo-starter-guide-evals](../sources/apollo-starter-guide-evals.md), [sources/hubinger-understanding-based-safety-evals](../sources/hubinger-understanding-based-safety-evals.md) и [sources/igor-ivanov-what-is-an-evaluation](../sources/igor-ivanov-what-is-an-evaluation.md) теперь опираются на clipped Markdown-версии полных текстов. Это не отменяет полезности source pages как учебных маршрутов, но делает их заметно ближе к исходной аргументации.
- [sources/prompt-sensitivity-benchmark](../sources/prompt-sensitivity-benchmark.md) теперь опирается на clipped HTML raw и TeX source, так что его удобнее перечитывать и сверять.
- [sources/barnett-thiergart-evals-catastrophic-risks](../sources/barnett-thiergart-evals-catastrophic-risks.md) по-прежнему сильнее зависит от PDF, чем другие ключевые источники недели.
- [sources/deepmind-specification-gaming](../sources/deepmind-specification-gaming.md) и [sources/inspect-ai-tutorial-week-01](../sources/inspect-ai-tutorial-week-01.md) по-прежнему хорошо работают как полные raw-артефакты для восстановления примеров и структуры.

## Фокус недели
Неделя вводит базовый язык evals, но быстро усложняет картину. Источники вместе проходят путь от базовых определений и роли evaluator к критике purely behavioral tests, к вопросу о том, что вообще считать evaluation, к prompt-level failure modes и specification-level failure modes, а затем показывают и практический слой через Inspect AI.

## Картина недели в одном абзаце
Если совсем сжать материал недели, получается такая линия. Сначала evals вводятся как полезный и почти неизбежный инструмент: без них трудно понимать, что умеет модель и как принимать решения вокруг нее. Затем источники шаг за шагом показывают, что этого инструмента легко потребовать слишком много: поведение модели может быть неполным evidence, prompt может исказить наблюдаемый результат, сама модель может распознавать режим оценки, а целевая метрика вообще может не совпадать с тем, что мы реально хотели получить. Практический notebook нужен в этой картине затем, чтобы было видно: все эти проблемы живут не только в теории, но и в конкретном дизайне task, prompt, scorer и анализа логов.

## Карта недели
- Вход в тему: [sources/apollo-starter-guide-evals](../sources/apollo-starter-guide-evals.md) задает словарь области и базовые различия внутри evals.
- Уточнение границ: [sources/hubinger-understanding-based-safety-evals](../sources/hubinger-understanding-based-safety-evals.md) и [sources/barnett-thiergart-evals-catastrophic-risks](../sources/barnett-thiergart-evals-catastrophic-risks.md) показывают, почему простого наблюдения за поведением недостаточно для сильных safety claims.
- Дополнительные failure modes: [sources/igor-ivanov-what-is-an-evaluation](../sources/igor-ivanov-what-is-an-evaluation.md) проясняет проблему evaluation awareness, [sources/prompt-sensitivity-benchmark](../sources/prompt-sensitivity-benchmark.md) показывает зависимость результатов от phrasing, а [sources/deepmind-specification-gaming](../sources/deepmind-specification-gaming.md) переносит внимание на mismatch между proxy objective и intended outcome.
- Практический слой: [sources/inspect-ai-tutorial-week-01](../sources/inspect-ai-tutorial-week-01.md) переводит разговор из уровня концептов в уровень task design, solver/scorer pipelines и просмотра логов.

## Источники
### Theory
- [sources/apollo-starter-guide-evals](../sources/apollo-starter-guide-evals.md) — стартовая рамка: что такое evals, какие у них базовые типы и чем занимается evaluator
- [sources/hubinger-understanding-based-safety-evals](../sources/hubinger-understanding-based-safety-evals.md) — критика purely behavioral standards и аргумент в пользу understanding-based evaluations
- [sources/barnett-thiergart-evals-catastrophic-risks](../sources/barnett-thiergart-evals-catastrophic-risks.md) — систематическая карта того, какие claims о catastrophic risks evals поддерживают, а какие нет

### Notebooks
- [sources/inspect-ai-tutorial-week-01](../sources/inspect-ai-tutorial-week-01.md) — практический tutorial по Inspect AI, `Task`, solver/scorer pipelines и `inspect view`

### Extra
- [sources/igor-ivanov-what-is-an-evaluation](../sources/igor-ivanov-what-is-an-evaluation.md) — почему само определение evaluation важно для разговора про awareness и gaming
- [sources/prompt-sensitivity-benchmark](../sources/prompt-sensitivity-benchmark.md) — как prompt formulation влияет на answerability и reliability measurement
- [sources/deepmind-specification-gaming](../sources/deepmind-specification-gaming.md) — как цель может быть оптимизирована буквально, но не по intended outcome

## Что стоит вынести
Неделя не спорит с тем, что evals нужны. Она спорит с более сильной и опасной мыслью: будто удачно устроенный behavioral test уже почти равен надежному safety verdict.

### Базовая рамка
- Evals описываются как систематическое измерение свойств AI-систем, включая их способности и склонности.
- Уже на вводном уровне различаются red-teaming и benchmarking, а также capability evals и alignment evals.
- Apollo полезно добавляет еще один слой: evals — это не только taxonomy, но и практическая область, где prompting, scaffolding, fine-tuning и experimental design прямо влияют на качество измерения.
- Определение самого evaluation неочевидно: intent исследователя, consequences interaction и surface features benchmark-like среды не совпадают.
- Поведенческие evals полезны как способ получить lower bounds на наблюдаемые способности модели и улучшить decision-making.

### Где ломаются простые выводы
- Для misuse risk текущих моделей evals в принципе могут быть полезны, но только при сильных предпосылках о capability elicitation, threat modeling и преимуществах evaluators над attackers.
- Behavioral evals плохо поддерживают отрицательные claims: провал теста не доказывает отсутствия способности, а успех на безопасном поведении не доказывает alignment.
- Для misalignment и автономных рисков проблема усиливается из-за sandbagging, under-elicitation и слабого понимания внутренних propensities модели; Hubinger дополнительно подчеркивает, что надежно проверять deception может быть труднее, чем вообще не допустить ее возникновения.
- Небольшие изменения prompt formulation могут заметно менять answerability, даже если information need остается тем же.
- Вопрос "что считать evaluation?" сам по себе распадается на несколько слоев: intent, benchmark-likeness и consequences, а модель может реагировать в основном на второй.
- Specification gaming показывает, что агент может удовлетворять proxy objective и все равно уходить от intended outcome.

### Как это интерпретировать
- Центральное напряжение недели такое: evals нужны, но их легко переоценить как safety standard.
- Чем выше stakes и capabilities моделей, тем менее убедительными становятся выводы вида "ничего опасного не нашли, значит опасности нет".
- Идея understanding-based evaluations появляется как ответ на ограниченность behavior-only подхода, особенно в сценариях deception и hidden capabilities.
- Дополнительные материалы уточняют, что unreliable evidence может возникать на разных слоях: в определении eval context, в phrasing prompt и в самой постановке objective.
- Поэтому качество evals зависит не только от "хорошего теста", но и от conceptual clarity, elicitation quality и engineering discipline.

Проще говоря, неделя 01 нужна для калибровки ожиданий. После нее полезно держать в голове не только вопрос "как устроить eval?", но и вопрос "какой именно вывод этот eval вообще способен поддержать?".

## Практика
Практический материал здесь особенно важен как antidote к излишней абстракции. Он показывает, что разговор про limits of evals быстро упирается в очень конкретные решения: как сформулирован prompt, какой scorer выбран, что видно в логах и где именно мы можем случайно измерять не то, что хотели.

- [sources/inspect-ai-tutorial-week-01](../sources/inspect-ai-tutorial-week-01.md) служит первой практической рамкой недели.
- Цель notebook: собрать базовый eval pipeline и понять структуру `Task`.
- Setup: Python notebook, `inspect-ai`, локальный Ollama или cloud APIs.
- Задачи: hello-world eval, system prompts, prompt templates, chain-of-thought, single-choice и multiple-choice tasks, metadata, multiple correct answers.
- Отдельное упражнение строит мини-эксперимент по position bias в multiple-choice benchmarks.
- Notebook не исполнен и содержит `# YOUR CODE HERE`, поэтому его роль сейчас учебная, а не как источник результатов.

## Связанные концепты
- [concepts/evals](../concepts/evals.md) — базовый словарь и главные различия внутри поля
- [concepts/behavioral-evals](../concepts/behavioral-evals.md) — что именно измеряет behavior-based evidence и где у него слабые места
- [concepts/understanding-based-evals](../concepts/understanding-based-evals.md) — зачем вообще нужен более сильный standard, чем behavior-only testing
- [concepts/evaluation-awareness](../concepts/evaluation-awareness.md) — как модель может распознавать eval-like context
- [concepts/prompt-sensitivity](../concepts/prompt-sensitivity.md) — почему phrasing prompt влияет на observed capability
- [concepts/specification-gaming](../concepts/specification-gaming.md) — как proxy objective уводит от intended outcome
- [concepts/inspect-ai](../concepts/inspect-ai.md) — практический слой: как строить eval tasks и читать результаты

## Связанный синтез
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
 
## Что повторить перед следующей неделей
- Уметь своими словами различать red-teaming, benchmarking, capability evals и alignment evals.
- Понимать, почему behavioral evidence обычно сильнее для lower bounds, чем для upper bounds и alignment claims.
- Держать в голове три разных источника искажения: evaluation awareness, prompt sensitivity и specification gaming.
- Понимать базовую практическую схему `dataset -> solver -> scorer -> logs`.

Если эти четыре пункта восстанавливаются без подсказки, значит основная логика недели уже держится в памяти, а source pages и concept pages нужны скорее для уточнения нюансов.

## Открытые вопросы
- Какие claims о safety вообще допустимо делать на основании behavioral evals без ложного чувства надежности?
- Можно ли operationalize understanding-based evaluations так, чтобы они были достаточно строгими и при этом method-agnostic?
- Как сочетать evals, interpretability, audits и security controls в одном safety case?
- Как отделять prompt sensitivity от реального отсутствия capability?
- Как строить evals, которые меньше подсказывают модели, что она находится в режиме оценки?
- Как ловить specification gaming до того, как proxy objective станет operational metric?

## Краткий вывод
Неделя 01 теперь покрывает уже не только базовый словарь evals, но и несколько слоев их возможного сбоя. Apollo, Hubinger и Barnett-Thiergart задают общую рамку limits of behavioral evidence. Ivanov добавляет более точный разбор evaluation awareness и самого понятия evaluation, paper про prompt sensitivity показывает нестабильность ответа к phrasing, а DeepMind-текст про specification gaming напоминает, что ломаться может и сама objective. Notebook по Inspect AI переводит все это в практику: evals нужно не только обсуждать, но и собирать как явный workflow с контролируемыми design choices. За счет новых clipped и normalized raw-текстов эта картина теперь лучше опирается на локальные источники, а не только на краткие course-notes.
