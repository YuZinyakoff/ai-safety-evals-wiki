# BenchmarkCards: Standardized Documentation For Large Language Model Benchmarks

- **Тип источника:** extra
- **Неделя:** week-03
- **Raw:** [clipped `.md`](<../../raw/week-03/extra/Formatting Instructions For NeurIPS 2024.md>), [PDF](<../../raw/week-03/extra/2410.12974v3.pdf>), [TeX source](<../../raw/week-03/extra/arXiv-2410.12974v3.tar.gz>)
- **Оригинал:** [arXiv HTML](https://arxiv.org/html/2410.12974v3)
- **Полнота raw:** clipped Markdown, PDF, TeX source; HTML clip сохранен под шумным filename, но содержит правильный текст статьи

## Ключевая мысль
> **Benchmark недостаточно просто запустить; его еще нужно так задокументировать, чтобы другой человек понял, что именно он измеряет, как его выбирать и где у него границы.**

## Зачем источник в базе
Это важный supporting text для week-03, потому что он переводит разговор о benchmark design в разговор о benchmark documentation. Источник нужен, чтобы не потерять еще один слой зрелости eval practice: прозрачность claims и limits должна жить не только в голове автора benchmark'а, но и в стандартизированном описании.

## Эпистемический статус и как на него смотреть
Это design-and-documentation proposal paper с user-study layer, а не benchmark result paper. Его полезно читать как попытку сделать benchmark use более auditably transparent через standardized documentation.

## На какие вопросы источник помогает отвечать
- Почему benchmark documentation влияет на качество использования benchmark'а почти так же, как сам benchmark?
- Что именно должно входить в `BenchmarkCard`?
- Как such documentation помогает benchmark selection and interpretation?
- Какие ограничения и gaming risks возникают у standardized benchmark cards?

## Краткое содержание
Paper начинает с проблемы: benchmark'ов много, их metadata scattered, и пользователю сложно понять, какой benchmark вообще подходит под его задачу и как интерпретировать результаты. Затем авторы предлагают `BenchmarkCards` как documentation framework, который стандартизирует benchmark objectives, methodology, data sources, assumptions, limitations и related benchmarks. После описания template paper переходит к user studies с benchmark users и benchmark authors, чтобы проверить две вещи: полезность такой формы документации и адекватность автоматически сгенерированных cards. В финале работа обсуждает результаты этих studies, идеи community-driven repository и ограничения самого подхода, включая необходимость поддерживать cards актуальными и риск того, что подробное описание limitations может облегчать gaming.

## Как читать источник быстро
- Если нужен общий смысл, читай problem statement and the proposed `BenchmarkCards` template.
- Если интересует practical value, переходи к user-study sections with benchmark users and authors.
- Если нужен критический reading, не пропускай discussion of maintenance costs, stale metadata and gaming concerns.

## Что источник утверждает прямо
- Авторы утверждают, что benchmark users часто плохо видят intended use, assumptions, data sources и limitations, потому что эта информация рассыпана по paper, appendix и external resources.
- `BenchmarkCards` предлагаются как стандартизированный template для documentation benchmark objectives, methodology, data provenance, limitations и related benchmarks.
- User studies в paper показывают, что structured cards помогают и users, и authors лучше понимать benchmark selection and interpretation.
- Авторы отдельно признают costs and risks такого подхода: cards нужно поддерживать актуальными, а подробная transparency иногда может облегчать gaming.

## Что здесь особенно важно
- **Documentation** влияет на benchmark selection почти так же, как сам benchmark.
- **Metadata scattered across papers** — реальная практическая проблема, а не мелочь.
- **“Similar benchmarks”** и explicit limitations важны для сравнения и правильной интерпретации.
- **Стандартизация документации** помогает видеть blind spots benchmark ecosystem.

## Интерпретация для курса
Для курса эта статья важна как расширение benchmark design до documentation and governance layer. Она помогает не смешивать два вопроса: “benchmark хорошо устроен?” и “benchmark хорошо описан так, чтобы другой человек не сделал из него слишком сильный вывод?”.

## Что это добавляет к теме недели
`BenchmarkCards` показывает, что benchmark design не заканчивается на dataset, metric и leaderboard. Есть еще слой “как этот benchmark будет прочитан и использован другими”. Для week-03 это важное продолжение тем transparency, validity и evidence communication.

## Что стоит запомнить при повторении
- **Хороший benchmark без хорошей документации легко использовать плохо.**
- **Benchmark documentation** должна помогать выбирать benchmark, а не только рекламировать его.
- **Documentation framework** — это часть benchmark governance, а не только UX-улучшение.

## Связанные концепты
- [concepts/benchmark-documentation](../concepts/benchmark-documentation.md)
- [concepts/benchmark-design](../concepts/benchmark-design.md)
- [concepts/construct-validity](../concepts/construct-validity.md)

## Что осталось неясным / спорным
- Насколько community-driven benchmark documentation будет реально поддерживаться и обновляться?
- Где проходит граница между полезной transparency и disclosure, который облегчает gaming benchmark'а?

## Связанные страницы
- [weeks/week-03](../weeks/week-03.md)
- [sources/evidence-centered-benchmark-design-nlp](evidence-centered-benchmark-design-nlp.md)
- [sources/holistic-evaluation-language-models](holistic-evaluation-language-models.md)
