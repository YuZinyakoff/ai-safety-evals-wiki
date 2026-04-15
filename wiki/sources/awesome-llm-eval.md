# Awesome LLM Eval

- **Тип источника:** extra
- **Неделя:** week-02
- **Raw:** [course note](<../../raw/week-02/extra/Awesome LLM Eval.md>)
- **Оригинал:** [GitHub repo](https://github.com/onejune2018/Awesome-LLM-Eval)
- **Полнота raw:** краткая заметка курса с внешней ссылкой на репозиторий

## Ключевая мысль
> **Большой каталог benchmarks полезен как карта поля, но не как готовый ответ на вопрос, какой eval вообще нужен под конкретную задачу.**

## Зачем источник в базе
Это не основной reading source, а навигационный хаб по полю LLM evaluation. Он нужен в базе как ориентир: где быстро смотреть benchmarks, tools, leaderboards и дальнейшие reading paths, если нужно выйти за пределы материалов одной недели.

## Эпистемический статус и как на него смотреть
Это resource index и course note, а не argumentative paper. Его лучше использовать как карту поиска и discovery-layer, а не как источник готовых выводов о качестве benchmark'ов.

## На какие вопросы источник помогает отвечать
- Где быстро искать benchmark catalogs, tools и leaderboard references по LLM evals?
- Какой landscape вообще уже существует за пределами одной недели курса?
- Почему длинный curated repo не заменяет evaluation judgment?
- Как использовать такие каталоги, не превращая их в ложный знак зрелости поля?

## Краткое содержание
Курсная заметка рекомендует `Awesome-LLM-Eval` не как текст для последовательного чтения, а как обновляемый каталог поля. Логика здесь простая: сначала использовать репозиторий как карту landscape, чтобы быстро увидеть типы benchmark-задач, готовые инструменты, публичные сравнения и дальнейшие статьи, а уже потом углубляться в конкретные categories. Одновременно заметка делает важное предупреждение: большой curated repo легко создает ложное ощущение, будто проблема оценки уже решена количеством ссылок, хотя на практике остаются вопросы validity, task fit, freshness каталога и интерпретации benchmark scores.

## Как читать источник быстро
- Здесь почти нечего читать линейно: сначала посмотри top-level categories и реши, что именно ищешь, прежде чем проваливаться в ссылки.
- Используй repo как navigation layer to benchmarks, tools and papers, а не как substitute for methodology.
- Если нужен course-relevant use, возвращайся из каталога в конкретные source pages и week pages, а не доверяй одной только abundance of links.

## Что здесь особенно важно
- **Catalog is not judgment.** Репозиторий полезен как карта, а не как готовый standard of quality.
- **Landscape awareness** ценна, но не заменяет contextual thinking.
- **Curated resources стареют.** Их нужно использовать как starting point, а не как источник окончательных решений.
- **Большой список benchmarks** не отвечает автоматически на вопрос, какой именно benchmark supports the claim you care about.

## Что это добавляет к теме недели
Источник полезен как противовес чрезмерной локальности week-02. Пока остальные материалы недели учат аккуратнее относиться к benchmark design, uncertainty и bounded coverage, эта страница показывает, где вообще искать landscape-wide inventory. Она хорошо напоминает, что field map и solved evaluation problem — это разные вещи.

## Что стоит запомнить при повторении
- **Awesome repos** полезны для ориентации, но не заменяют evaluation reasoning.
- **Benchmark abundance** не равна benchmark validity.
- **Value of evaluator** все еще в умении выбрать подходящий setup под конкретный claim, а не только найти ссылку на подходящий tool.

## Связанные концепты
- [concepts/evals](../concepts/evals.md)
- [concepts/benchmarking](../concepts/benchmarking.md)
- [concepts/evaluation-generalization](../concepts/evaluation-generalization.md)

## Что осталось неясным / спорным
- Насколько быстро curated repositories устаревают для конкретных subdomains?
- Какие критерии помогают отличать полезный benchmark index от просто длинного списка ссылок?

## Связанные страницы
- [weeks/week-02](../weeks/week-02.md)
- [sources/cao-generalizable-evaluation-llm-era](cao-generalizable-evaluation-llm-era.md)
- [syntheses/benchmarking-beyond-single-scores](../syntheses/benchmarking-beyond-single-scores.md)
