# Evals

## Коротко
> **Evals** — это практики систематического измерения свойств AI-систем. Важно помнить, что это не один benchmark и не один тип теста, а целое семейство способов что-то выяснить о модели, раскрыть ее capability и интерпретировать полученный результат.

## Почему это важный концепт
Эта страница нужна как центральная точка сборки. Первая неделя вводит базовый язык области и показывает пределы behavior-based evidence. Вторая неделя делает шаг дальше и спрашивает, как именно интерпретировать benchmark results статистически и насколько вообще эти результаты переносятся за пределы конкретного suite. Третья и четвертая недели показывают, что benchmark design и evaluation procedure сами конструируют то, что мы видим. Пятая неделя поднимает стандарт еще выше и спрашивает, что вообще нужно, чтобы evals могли быть основанием для high-stakes safety decisions. Поэтому `evals` здесь полезно держать не как одно определение, а как карту всего поля.

## На какие вопросы обычно отвечают evals
- **Что модель умеет?** Это линия `capability evals`.
- **К чему модель склонна?** Это линия `alignment evals`.
- **Можно ли вообще выявить опасное свойство при активном поиске?** Это линия `red-teaming`.
- **Как часто поведение проявляется на выбранном распределении задач?** Это линия `benchmarking`.
- **Насколько устойчив и интерпретируем результат?** Это уже вопрос не только measurement, но и statistical rigor.

## Главные различия, которые полезно держать в голове
- **`Red-teaming` vs `benchmarking`.** Первое активно ищет наличие свойства, второе пытается измерить его проявление на контролируемом наборе задач.
- **`Capability evals` vs `alignment evals`.** В одном случае вопрос звучит “может ли модель?”, в другом “склонна ли она?”.
- **`Model safety` vs `contextual safety evals`.** Одни фокусируются на outputs модели, другие на downstream impact и поведении в задаче вместе с контекстом применения.
- **`Point estimate` vs uncertainty-aware result.** Один score сам по себе и score вместе с confidence interval, paired comparison и power reasoning — это разная сила evidence.

## Где здесь чаще всего ломается вывод
- **Measurement путают с safety case.** Сам факт оценки еще не означает, что собрана достаточная аргументация о безопасности.
- **Behavior принимают за всю модель.** Это особенно опасно в сценариях under-elicitation, sandbagging и evaluation awareness.
- **Score читают слишком буквально.** Week-02 добавляет важную оговорку: benchmark result — это noisy estimate, а не self-explanatory verdict.
- **Proxy принимают за реальную цель.** Здесь в поле зрения попадает specification gaming.
- **High-stakes use поднимает планку.** Если по evals хотят принимать deployment или policy decisions, обычной benchmark hygiene уже недостаточно.

## С чем легко перепутать
- Evals легко свести к одному leaderboard или benchmark suite, хотя в этой wiki они рассматриваются как более широкая measurement practice.
- Evals легко спутать с `red-teaming`, хотя red-teaming — только один режим работы внутри более широкой области.
- Наличие хорошего toolchain легко принять за качество eval как такового, хотя tool не отменяет слабую постановку задачи или слишком сильный claim.

## Где смотреть дальше
- [Apollo](../sources/apollo-starter-guide-evals.md) — самый удобный входной словарь.
- [Barnett-Thiergart](../sources/barnett-thiergart-evals-catastrophic-risks.md) — самая полезная страница про границы claims.
- [Miller](../sources/miller-adding-error-bars-to-evals.md) — статистическая честность benchmark results.
- [We Need A Science of Evals](../sources/we-need-a-science-of-evals.md) — почему поле должно становиться более зрелой дисциплиной.
- [Eval Methodology](eval-methodology.md) — что именно ломается на уровне качества самой measurement practice.
- [week-01](../weeks/week-01.md), [week-02](../weeks/week-02.md) и [week-05](../weeks/week-05.md) — хронологическая логика курса от вводного языка к high-stakes measurement.

## Открытые вопросы
- Какие именно claims о безопасности допустимо строить на основании evals?
- Как сочетать evals с interpretability, audits и governance measures, чтобы не переоценивать силу одного инструмента?
- Что именно должно считаться `evaluation` в исследованиях evaluation awareness и evaluation gaming?

## Связанные страницы
- [concepts/behavioral-evals](behavioral-evals.md)
- [concepts/understanding-based-evals](understanding-based-evals.md)
- [concepts/evaluation-awareness](evaluation-awareness.md)
- [concepts/benchmarking](benchmarking.md)
- [concepts/statistical-rigor-in-evals](statistical-rigor-in-evals.md)
- [concepts/inspect-ai](inspect-ai.md)
- [concepts/eval-methodology](eval-methodology.md)
- [concepts/science-of-evals](science-of-evals.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
- [syntheses/benchmarking-beyond-single-scores](../syntheses/benchmarking-beyond-single-scores.md)
