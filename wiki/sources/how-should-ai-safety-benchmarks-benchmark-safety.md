# How Should AI Safety Benchmarks Benchmark Safety?

- **Тип источника:** theory
- **Неделя:** week-05
- **Raw:** [clipped `.md`](<../../raw/week-05/theory/How Should AI Safety Benchmarks Benchmark Safety.md>), [PDF](<../../raw/week-05/theory/2601.23112v2.pdf>), [TeX Source](<../../raw/week-05/theory/arXiv-2601.23112v2.tar.gz>)
- **Оригинал:** [arXiv](https://arxiv.org/abs/2601.23112v2)
- **Полнота raw:** сильный raw-набор: clipped Markdown + PDF + TeX Source

## Ключевая мысль
> **Safety benchmark нельзя оценивать так же, как обычный capability benchmark.** Если benchmark должен поддерживать вывод о безопасности, ему мало набора задач и aggregate score: нужны coverage of risks, осмысленная risk quantification и понятная связь между метрикой и реальным harm.

## Зачем источник в базе
Это самый технически насыщенный и самый предметный текст недели. Он нужен как строгая критика того, почему многие текущие safety benchmarks не выдерживают сильных claims о model safety и deployment readiness. Через него удобно перейти от общего разговора про benchmark design к более жесткому разговору про normative and sociotechnical nature of safety.

## Краткое содержание
Статья начинается с постановки вопроса: что вообще делает safety benchmarking особым видом benchmark design. Авторы противопоставляют обычные capability benchmarks и safety benchmarks, показывая, что последние имеют нормативный и социотехнический характер. Затем paper делает scoping review 210 AI safety benchmarks и выделяет три основные зоны слабости: `construct coverage`, `risk quantification` и `measurement validity`. После этого работа переходит от диагноза к инженерной рамке и формулирует десять рекомендаций `R1–R10`, сгруппированных по этим трем модулям. В конце авторы превращают рекомендации в практический checklist и даже прогоняют через него конкретный benchmark-case, чтобы показать, как такая критика выглядит на практике.

## Что источник утверждает прямо
- Safety benchmarks отличаются от ordinary capability benchmarks тем, что имеют нормативный и социотехнический характер.
- В обзорной выборке current safety benchmarks чаще всего слабы по трем направлениям: `construct coverage`, `risk quantification` и `measurement validity`.
- Benchmark score нельзя автоматически читать как calibrated risk statement о deployment harm.
- Улучшение safety benchmarking требует не только новых тестов, но и более явной дисциплины around blind spots, uncertainty, severity, versioning и deployment grounding.

## Что здесь особенно важно
- **Safety benchmarking is normative.** Вопрос здесь не только в том, что модель делает, но и в том, какие harms считаются значимыми и как они соотносятся с реальным использованием.
- **`Construct coverage` нельзя сводить к known knowns.** Иначе benchmark создает ложное чувство полноты, проверяя только заранее ожидаемые риски.
- **Observed rate не равен probability of harm.** Авторы настаивают на более строгой `risk quantification`, где важны и uncertainty, и severity, и prevalence.
- **`Measurement validity` важнее красивой метрики.** Refusal rate, toxicity score или другой proxy сами по себе еще не доказывают, что измеряется именно тот real-world safety property, который интересует.
- **Checklist важен сам по себе.** Paper полезен не только как critique, но и как компактная рабочая рамка для review или design нового safety benchmark.

## Интерпретация для курса
Для логики курса этот источник делает первый и самый важный шаг недели: он показывает, что `AI safety benchmark` — это не просто "benchmark на safety topic", а отдельный measurement problem с более высокой epistemic нагрузкой. Именно через него становится видно, почему финальная неделя курса уходит от обычной логики leaderboard и переходит к разговорам о high-stakes measurement.

## Что стоит запомнить при повторении
- **Safety benchmark должен документировать blind spots, а не притворяться полным safety verdict.**
- **Риск — это не просто pass/fail proportion; здесь нужны severity, uncertainty и deployment grounding.**
- **Без понятной proxy chain benchmark score легко теряет связь с реальным harm.**

## Связанные концепты
- [concepts/ai-safety-benchmarks](../concepts/ai-safety-benchmarks.md)
- [concepts/measurement-validity](../concepts/measurement-validity.md)
- [concepts/risk-quantification](../concepts/risk-quantification.md)
- [concepts/science-of-evals](../concepts/science-of-evals.md)

## Что осталось неясным / спорным
- Насколько далеко можно practically продвинуть calibrated risk modeling, если реальные deployment data ограничены?
- Все ли рекомендации одинаково реалистичны для маленьких academic benchmarks, а не только для больших institutional efforts?

## Связанные страницы
- [weeks/week-05](../weeks/week-05.md)
- [sources/we-need-a-science-of-evals](we-need-a-science-of-evals.md)
- [syntheses/reliable-ai-safety-evals](../syntheses/reliable-ai-safety-evals.md)
- [concepts/benchmarking](../concepts/benchmarking.md)
