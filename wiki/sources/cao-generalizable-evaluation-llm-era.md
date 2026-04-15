# Toward Generalizable Evaluation In The LLM Era: A Survey Beyond Benchmarks

- **Тип источника:** theory
- **Неделя:** week-02
- **Raw:** [clipped `.md`](<../../raw/week-02/theory/Toward Generalizable Evaluation in the LLM Era A Survey Beyond Benchmarks.md>), [PDF](<../../raw/week-02/theory/2504.18838v1.pdf>), [TeX source](<../../raw/week-02/theory/arXiv-2504.18838v1.tar.gz>)
- **Оригинал:** [arXiv](https://arxiv.org/abs/2504.18838)
- **Полнота raw:** clipped Markdown, PDF и TeX source

## Ключевая мысль
> **Даже хорошо устроенный benchmark pipeline остается bounded, а модели становятся все менее bounded.** Отсюда и возникает проблема `evaluation generalization`.

## Зачем источник в базе
Это самый широкий обзорный источник недели. Он нужен, чтобы не застрять на уровне одного benchmark или одной статистической техники и увидеть, как поле evaluation меняется под давлением scaling, contamination, open-ended tasks и automated judging.

## Эпистемический статус и как на него смотреть
Это широкий survey и field map, а не settled answer to evaluation generalization. Его лучше читать как обзор pressure points и possible responses, который помогает понять, почему static benchmark thinking начинает ломаться.

## На какие вопросы источник помогает отвечать
- Почему static benchmarks все хуже справляются с LLM-era evaluation?
- Что authors называют `evaluation generalization`?
- Какие ответы поле предлагает на contamination, saturation и open-ended tasks?
- Какую роль в этом переходе играют dynamic benchmarks и `LLM-as-a-judge`?

## Краткое содержание
Survey устроен как попытка посмотреть на evaluation field уже не изнутри одного benchmark family, а на уровне всей evolving practice. Сначала авторы описывают, как классическая benchmark logic работала на более ранних этапах и почему `static benchmarks` долго были удобным default. Затем paper систематизирует основные pressure points LLM era: contamination, saturation, open-ended outputs, high cost of human judgment и growing mismatch между bounded tests и growing model capability. После этого обзор проходит по направлениям ответа: dynamic and time-aware benchmarks, richer task settings, automated evaluators вроде `LLMs-as-a-judge`, а также более широкая идея generalizable assessment across domains like knowledge, reasoning and coding. В финале survey поднимает главный structural question: как строить evaluation pipelines, которые успевают за scaling и дают выводы, generalizing better than today’s static suites.

## Как читать источник быстро
- Если нужен стратегический обзор, читай introduction и sections on why static benchmarks break in the LLM era.
- Если интересуют responses, переходи к blocks про dynamic benchmarks, open-ended tasks and `LLM-as-a-judge`.
- Если нужен слой research agenda, смотри conclusion и future-looking discussion around what it means for conclusions to generalize beyond a suite.

## Что здесь особенно важно
- **Static benchmarks** полезны, но быстро сталкиваются с contamination, saturation и limited coverage.
- **`LLMs-as-a-judge`** появляются как ответ на scale problem open-ended evaluation, но сами приносят новые validity questions.
- **Dynamic / time-aware protocols** интересны не как модный апгрейд, а как попытка бороться с leakage и boundedness.
- **Evaluation generalization** — это не generalization модели, а generalization самого evaluation conclusion.
- **Больше benchmark lists** не значит автоматически better assessment.

## Что это добавляет к теме недели
Источник расширяет week-02 от тактического разговора о `MMLU + confidence interval` до более стратегического разговора о будущем evaluation. Он показывает, что проблема не только в том, как аккуратно посчитать uncertainty на текущем benchmark, но и в том, насколько сами benchmarks, judging methods и coverage assumptions остаются валидными по мере роста моделей. Это делает страницу особенно полезной как дальнюю рамку для всей недели.

## Что стоит запомнить при повторении
- **Bounded evaluation pipelines** не масштабируются автоматически вместе с model capability.
- **Static benchmark excellence** не гарантирует strong external validity.
- **Generalizable evaluation** требует думать не только о статистике внутри suite, но и о переносимости conclusions за его пределы.

## Связанные концепты
- [concepts/benchmarking](../concepts/benchmarking.md)
- [concepts/evaluation-generalization](../concepts/evaluation-generalization.md)
- [concepts/statistical-rigor-in-evals](../concepts/statistical-rigor-in-evals.md)
- [concepts/evals](../concepts/evals.md)

## Что осталось неясным / спорным
- Насколько надежны `LLMs-as-a-judge` как долговременный ответ на open-ended evaluation?
- Какие practical criteria показывают, что benchmark suite действительно generalizes, а не просто выглядит более разнообразной?

## Связанные страницы
- [weeks/week-02](../weeks/week-02.md)
- [sources/awesome-llm-eval](awesome-llm-eval.md)
- [syntheses/benchmarking-beyond-single-scores](../syntheses/benchmarking-beyond-single-scores.md)
