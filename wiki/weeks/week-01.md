# Неделя 01

## Ключевая мысль
> **Неделя 01 нужна для калибровки ожиданий от evals.** Она не спорит с тем, что оценки нужны; она спорит с более опасной мыслью, будто удачный behavioral test уже почти равен надежному safety verdict.

## Зачем открывать эту страницу
Это hub-page первой недели. Ее лучше читать не как список материалов, а как карту вопросов, вокруг которых строится неделя. Если через месяц в памяти останется только общий тезис "неделя была про evals и их ограничения", именно отсюда проще всего восстановить целую линию рассуждения.

## Замысел недели от организаторов
В `raw/` теперь сохранена отдельная organizer note: [course-framing-week-01.md](../../raw/week-01/extra/course-framing-week-01.md). Она полезна не как еще один theory-source, а как честная карта того, зачем неделя собрана именно в таком порядке.

Если сжать эту рамку до одного абзаца, получится так: неделя идет от вводного понимания evals к более жесткой критике того, что именно можно заключать по результатам оценки. Сначала Apollo объясняет, что такое evals и зачем в эту область идти; затем Hubinger показывает, почему простая проверка поведения недостаточна для сильных safety-выводов; затем Barnett и Thiergart задают границы того, что evals реально могут и не могут делать в контексте catastrophic risk.

## Главные вопросы недели
- **Что вообще такое evals?** Неделя начинает с базового словаря: что измеряют evals, чем различаются `red-teaming`, `benchmarking`, `capability evals` и `alignment evals`.
- **Что именно можно заключить по наблюдаемому поведению?** Почти сразу становится видно, что behavioral evidence полезно, но его очень легко переоценить.
- **Почему тест может измерять не то, что нам кажется?** Здесь появляются `evaluation awareness`, `prompt sensitivity` и `specification gaming`.
- **Как это выглядит на практике?** Ноутбук по `Inspect AI` показывает, что все эти проблемы живут в конкретных design choices: prompt, solver, scorer и логи.

## Вопросы перед чтением и повторением
Эти вопросы полезны дважды: до чтения, чтобы заметить свои пробелы, и после чтения, чтобы проверить, насколько картина стала точнее.

- Что именно я сейчас называю `evals`: любой тест модели, конкретный benchmark, safety-assessment или более широкую decision-support практику?
- Где, по моему текущему пониманию, evals сильнее: в обнаружении уже проявленных способностей, в оценке misuse-risk, в прогнозе будущих рисков или в общей гарантии безопасности?
- Какую роль evals вообще могут играть в предотвращении AI risk: самостоятельного safety gate, одного сигнала среди многих или только исследовательского инструмента?

## Если нужно быстро вспомнить неделю
- Если нужен **входной словарь**, начни с [Apollo](../sources/apollo-starter-guide-evals.md) и [concepts/evals](../concepts/evals.md).
- Если нужен **самый сильный аргумент про пределы behavioral evidence**, смотри [Hubinger](../sources/hubinger-understanding-based-safety-evals.md), [Barnett-Thiergart](../sources/barnett-thiergart-evals-catastrophic-risks.md) и [synthesis](../syntheses/evals-scope-and-limits.md).
- Если нужно вернуть **механизмы, из-за которых eval ломается**, переходи к [Ivanov](../sources/igor-ivanov-what-is-an-evaluation.md), [Prompt Sensitivity](../sources/prompt-sensitivity-benchmark.md) и [Specification Gaming](../sources/deepmind-specification-gaming.md).
- Если нужен **практический слой**, открывай [Inspect AI tutorial](../sources/inspect-ai-tutorial-week-01.md) и [concepts/inspect-ai](../concepts/inspect-ai.md).

## Если у тебя конкретный вопрос
- Если вопрос звучит как **“что вообще считать eval и зачем они нужны?”**, сначала иди в [Apollo](../sources/apollo-starter-guide-evals.md), а потом при необходимости уточняй словарь через [concepts/evals](../concepts/evals.md).
- Если вопрос звучит как **“какие safety-claims реально можно и нельзя делать по наблюдаемому поведению?”**, читай [Hubinger](../sources/hubinger-understanding-based-safety-evals.md) вместе с [Barnett-Thiergart](../sources/barnett-thiergart-evals-catastrophic-risks.md).
- Если вопрос звучит как **“как модель вообще может распознавать, что она на eval?”**, начни с [Ivanov](../sources/igor-ivanov-what-is-an-evaluation.md).
- Если вопрос звучит как **“почему одна и та же задача дает разный observed capability при другом phrasing?”**, открывай [Prompt Sensitivity](../sources/prompt-sensitivity-benchmark.md) и затем [Inspect AI tutorial](../sources/inspect-ai-tutorial-week-01.md), чтобы увидеть инженерный слой.
- Если вопрос звучит как **“что если проблема вообще не в измерении, а в плохо выбранной цели?”**, смотри [Specification Gaming](../sources/deepmind-specification-gaming.md).

## Картина недели
Если собрать материалы в одну линию, получится такой ход. Сначала evals вводятся как почти неизбежный инструмент для понимания моделей и улучшения решений вокруг них. Затем неделя быстро показывает, что сам факт тестирования еще не дает сильного safety claim: модель можно недораскрыть, можно случайно измерить поведение только в benchmark-like контексте, можно получить результат, который чувствителен к phrasing prompt, и можно вообще оптимизировать не ту цель, которая нас реально интересует. Практический notebook важен в этой картине потому, что он переводит разговор из уровня абстрактных оговорок в уровень конкретного workflow.

## Как материалы собираются в одну линию
- **Apollo** задает базовый язык области и полезную рамку: evals важны как `decision-support layer`, а не как гарантия безопасности.
- **Hubinger** повышает планку и спрашивает, почему одного наблюдаемого поведения может быть недостаточно именно для alignment claims.
- **Barnett-Thiergart** добавляет дисциплину вывода: не просто "у evals есть limits", а "какие именно claims они поддерживают, а какие нет".
- **Ivanov** уточняет, что само слово `evaluation` не такое простое, как кажется, и что модель может распознавать не намерение исследователя, а лишь benchmark-likeness среды.
- **Prompt Sensitivity paper** показывает на конкретном benchmark-примере, что даже при фиксированной модели результат зависит от phrasing.
- **Specification Gaming** расширяет рамку: проблема может быть не только в измерении, но и в самой цели.
- **Inspect AI tutorial** заземляет все это в практику: `dataset -> solver -> scorer -> logs`.

## Что нужно уметь объяснить своими словами
- **Почему evals не равны safety.** Они уменьшают неопределенность и помогают принимать решения, но не превращают поведенческий тест в достаточное основание для сильного safety verdict.
- **Почему behavioral evidence сильнее для lower bounds, чем для upper bounds.** Успех на тесте показывает, что модель что-то уже продемонстрировала; провал не показывает, что способности нет.
- **Почему context matters.** Модель может реагировать на признаки eval-like среды, а не просто на содержимое задания.
- **Почему prompt matters.** Один и тот же information need может давать разный observed capability в зависимости от формулировки.
- **Почему objective matters.** Хороший score по proxy не гарантирует, что система делает то, что нам на самом деле нужно.

## Практический слой
Практика в этой неделе не вторична. Она нужна, чтобы не читать ограничения evals как чисто философские. Ноутбук по `Inspect AI` показывает, что reliability живет в очень конкретных местах:
- как сформулирован prompt;
- какой `solver` используется;
- что именно считает `scorer`;
- какие логи мы смотрим после запуска;
- где мы случайно создаем слишком удобный proxy для настоящей задачи.

Поэтому первую неделю полезно помнить не только как набор аргументов против наивного benchmark thinking, но и как первую точку, где эти аргументы становятся инженерными.

## Источники недели
### Theory
- [Apollo](../sources/apollo-starter-guide-evals.md) — базовый словарь evals и образ evaluator как research-engineering роли
- [Hubinger](../sources/hubinger-understanding-based-safety-evals.md) — почему behavior-only testing слишком слабо для alignment standard
- [Barnett-Thiergart](../sources/barnett-thiergart-evals-catastrophic-risks.md) — какие claims о catastrophic risk evals реально поддерживают

### Notebooks
- [Inspect AI tutorial](../sources/inspect-ai-tutorial-week-01.md) — первый практический workflow: `Task`, solver/scorer pipelines и `inspect view`

### Extra
- [Ivanov](../sources/igor-ivanov-what-is-an-evaluation.md) — что именно считать evaluation и почему это важно для awareness
- [Prompt Sensitivity](../sources/prompt-sensitivity-benchmark.md) — как phrasing prompt влияет на answerability и надежность измерения
- [Specification Gaming](../sources/deepmind-specification-gaming.md) — как proxy objective расходится с intended outcome

## Куда идти дальше внутри wiki
- Если нужен **общий синтез недели**, смотри [Scope, Failure Modes, And Practice Of Evals](../syntheses/evals-scope-and-limits.md).
- Если нужно быстро пройтись по **ключевым концептам**, открой [evals](../concepts/evals.md), [behavioral evals](../concepts/behavioral-evals.md), [understanding-based evals](../concepts/understanding-based-evals.md), [evaluation awareness](../concepts/evaluation-awareness.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [specification gaming](../concepts/specification-gaming.md) и [Inspect AI](../concepts/inspect-ai.md).

## Что повторить перед следующей неделей
- Уметь различать `red-teaming`, `benchmarking`, `capability evals` и `alignment evals`.
- Понимать, почему behavioral evidence обычно поддерживает **lower bounds** сильнее, чем **upper bounds** и сильные alignment claims.
- Держать в голове три разных механизма искажения: **evaluation awareness**, **prompt sensitivity** и **specification gaming**.
- Помнить базовую практическую схему `dataset -> solver -> scorer -> logs`.

## Примечание о raw
- [Apollo](../sources/apollo-starter-guide-evals.md), [Hubinger](../sources/hubinger-understanding-based-safety-evals.md) и [Ivanov](../sources/igor-ivanov-what-is-an-evaluation.md) теперь опираются на полные clipped Markdown-версии текстов.
- [Prompt Sensitivity](../sources/prompt-sensitivity-benchmark.md) опирается на сильный raw-набор: clipped HTML, PDF и `TeX Source`.
- [Barnett-Thiergart](../sources/barnett-thiergart-evals-catastrophic-risks.md) теперь тоже опирается на сильный raw-набор: clipped HTML, PDF и `TeX Source`.
- [Inspect AI tutorial](../sources/inspect-ai-tutorial-week-01.md) остается учебным notebook с `# YOUR CODE HERE`, то есть это scaffold, а не готовый empirical report.

## Открытые вопросы
- Какие claims о safety допустимо делать на основании behavioral evals без ложного чувства надежности?
- Можно ли operationalize understanding-based evaluations так, чтобы они действительно проверяли понимание, а не красивую post-hoc rationalization?
- Как сочетать evals, interpretability, audits и security controls в одном safety case?
- Как строить evals, которые меньше подсказывают модели, что она находится в режиме оценки?

## Вопросы для обсуждения
- Какие концепции недели запомнились сильнее всего и почему: потому что они кажутся самыми важными, или потому что именно здесь они были лучше всего объяснены?
- Какое ограничение evals выглядит наиболее серьезным на практике: слабость upper bounds, трудность работы с deception, слабые прогнозы о будущих моделях или что-то еще?
- Где должна проходить рабочая граница между утверждением "`evals` полезны" и утверждением "`evals` достаточно"?

## Краткий вывод
Week-01 уже не просто вводит термин `evals`. Она показывает, что сила оценки зависит и от того, **что именно мы тестируем**, и от того, **какой вывод мы хотим из теста сделать**. Это хорошая стартовая неделя именно потому, что она одновременно дает язык области, ломает слишком простые ожидания и сразу показывает практический workflow, в котором эти ожидания либо подтверждаются, либо рушатся.
