# A Starter Guide For Evals

- **Тип источника:** theory
- **Неделя:** week-01
- **Raw:** [clipped `.md`](<../../raw/week-01/theory/A Starter Guide For Evals.md>)
- **Оригинал:** [Apollo Research](https://www.apolloresearch.ai/blog/a-starter-guide-for-evals)
- **Полнота raw:** полный текст статьи в clipped Markdown

## Ключевая мысль
> **Apollo полезен как стартовая рамка: evals нужны не потому, что дают гарантию безопасности, а потому, что улучшают decision-making под неопределенностью.**

## Зачем источник в базе
Это лучший входной текст недели. Он дает базовый словарь evals, помогает не смешивать разные типы оценок и сразу показывает, что evaluator — это не “человек, который просто запускает benchmark”, а исследователь-инженер, который строит метод измерения и следит за качеством elicitation.

## Эпистемический статус и как на него смотреть
Это вводный field memo от Apollo, а не нейтральный учебник и не formal survey. Его полезно читать как хорошо написанную стартовую рамку: она задает vocabulary области и рабочие distinctions, но не закрывает спор о limits evals.

## На какие вопросы источник помогает отвечать
- Зачем evals вообще нужны, если они не дают гарантии безопасности?
- Чем отличаются `red-teaming`, `benchmarking`, `capability evals` и `alignment evals`?
- Что именно current evals обычно измеряют, когда говорят о поведении модели?
- Почему evaluator в этой области больше похож на research engineer, чем на оператора benchmark'а?

## Краткое содержание
Текст устроен как стартовый обзор области. Сначала он отвечает на самый общий вопрос: **зачем evals вообще нужны** и почему они полезны как инструмент улучшения решений под неопределенностью. Затем источник последовательно раскладывает поле на несколько базовых distinctions: `red-teaming` и `benchmarking`, `capability evals` и `alignment evals`, а также более общую идею о том, что современные evals в основном работают как **behavioral measurements**. После этого статья делает важную оговорку про limits of behavior-only evidence и только затем переходит к практическому слою: кто такой evaluator, какие у него должны быть навыки и почему работа в evals почти всегда находится на стыке исследования, prompting, scaffolding и software engineering. За счет такой структуры текст работает не только как словарь, но и как первая карта области.

## Структура материала
- `Why work on evals?`: зачем evals нужны и какие ограничения у них есть уже на входе.
- `What are model evaluations (evals)?`: distinctions between `red-teaming`, `benchmarking`, `capability evals` и `alignment evals`.
- `What skills are helpful for evaluators?`: prompting, steering, `SFT` / `RL`, scaffolding, tool use, research и engineering skills.
- `Potential career paths`: где этот набор навыков применяется на практике.

## Как читать источник быстро
- Для первого прохода хватит `Why work on evals?` и `What are model evaluations (evals)?`: там собирается словарь и базовая карта поля.
- Если нужен только operational vocabulary, иди прямо в `What are model evaluations (evals)?` и не расползайся по skills-блокам.
- Если интересует роль evaluator'а как практики, читай `What skills are helpful for evaluators?` и затем быстро просматривай `Potential career paths`.

## Что источник утверждает прямо
- Evals полезны прежде всего как инструмент улучшения решений под неопределенностью, а не как автоматическая safety guarantee.
- Разные evaluation modes отвечают на разные вопросы: `red-teaming`, `benchmarking`, `capability evals` и `alignment evals` не стоит смешивать.
- Большая часть current evals остается поведенческой по своей природе и поэтому имеет ограниченный evidential reach.
- Хороший evaluator должен уметь работать на стыке measurement design, prompting, scaffolding и engineering practice.

## Что здесь особенно важно
- **Evals как decision-support layer.** Текст полезно читать как антидот против мысли, что сам факт тестирования уже почти решает safety problem.
- **`Red-teaming` и `benchmarking` отвечают на разные вопросы.** Одно ищет существование свойства при активном elicitation, другое пытается оценить его частоту на выбранном распределении задач.
- **`Capability evals` и `alignment evals` не стоит смешивать.** В одном случае вопрос звучит как “может ли модель?”, в другом как “склонна ли она?”.
- **Behavioral nature current evals.** Уже здесь появляется важная оговорка: наблюдаемое поведение покрывает только часть input space.
- **Evaluator как role.** Источник полезен тем, что связывает evals с prompting, fine-tuning, scaffolding, experimental design и software engineering.

## Интерпретация для курса
Для курса этот текст важен не просто как “вводная статья”. Он задает базовый vocabulary, через который потом читаются почти все остальные материалы: limits behavioral evidence, роль elicitation, distinction between task design and interpretation, а также evaluator как measurement engineer rather than benchmark operator.

## Что это добавляет к теме недели
Apollo задает базовый язык всей недели. Без него остальные тексты было бы легко читать как разрозненные критические заметки, а не как обсуждение одной области. Особенно полезно, что источник не только вводит taxonomy, но и заранее вшивает правильную интуицию: **evals нужны, но их сила ограничена типом evidence, которое они реально дают**.

## Что стоит запомнить при повторении
- **Evals** — это не один benchmark, а семейство методов measurement, elicitation и interpretation.
- **Behavioral evals** по умолчанию сильнее для грубой калибровки и lower bounds, чем для сильных safety claims.
- **Evaluator** в этой рамке — это не оператор benchmark, а человек, который управляет prompt, scaffold, scorer и общим дизайном эксперимента.

## Связанные концепты
- [concepts/evals](../concepts/evals.md)
- [concepts/behavioral-evals](../concepts/behavioral-evals.md)
- [concepts/inspect-ai](../concepts/inspect-ai.md)

## Что осталось неясным / спорным
- Где проходит рабочая граница между `red-teaming` и `benchmarking` в реальных pipelines?
- Какие свойства модели вообще можно измерять поведенчески, а какие требуют более сильных инструментов понимания?
- Какие навыки evaluators останутся центральными по мере перехода от LLM-only setups к более agentic systems?

## Связанные страницы
- [weeks/week-01](../weeks/week-01.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
