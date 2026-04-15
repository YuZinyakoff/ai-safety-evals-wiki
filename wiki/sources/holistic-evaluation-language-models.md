# Holistic Evaluation Of Language Models

- **Тип источника:** theory
- **Неделя:** week-03
- **Raw:** [clipped `.md`](<../../raw/week-03/theory/Holistic Evaluation of Language Models.md>), [PDF](<../../raw/week-03/theory/775_Holistic_Evaluation_of_Lan (1).pdf>), [TeX source](<../../raw/week-03/theory/arXiv-2211.09110v2.tar.gz>)
- **Оригинал:** [OpenReview / arXiv](https://openreview.net/pdf?id=iO4LZibEqW)
- **Полнота raw:** сильный raw-набор: clipped Markdown, PDF и TeX source

## Ключевая мысль
> **Хороший benchmark для LLM не должен сводиться к одному dataset и одной accuracy-метрике.** Он должен явно покрывать разные сценарии, разные desiderata и общие правила сравнения.

## Зачем источник в базе
Это главный текст недели про `holistic evaluation`. Он нужен, чтобы увидеть benchmark не как один тест, а как целую рамку выбора сценариев, метрик и правил сравнения. Через него week-03 поднимает вопрос не только о том, какие результаты получили модели, но и о том, какую картину мира вообще создает сам benchmark.

## Эпистемический статус и как на него смотреть
Это не учебник по benchmark design и не окончательный стандарт evaluation. Это programmatic paper и benchmark proposal: authors не просто описывают HELM, а предлагают более широкий способ думать о coverage, multi-metric measurement и standardization. Поэтому читать его лучше как источник рабочей рамки и design vocabulary, а не как закрывающий спор текст.

## На какие вопросы источник помогает отвечать
- Что такое HELM и зачем authors вообще вводят его как отдельный framework?
- Какую рамку сравнения language models authors считают более честной, чем single-dataset benchmarking?
- Какие сценарии, метрики и targeted evaluations входят в HELM-style view?
- Где сами authors признают неполноту coverage и limits своей конструкции?

## Краткое содержание
Статья сначала задает мотивацию: language models уже стали общим интерфейсом для множества задач, а привычные benchmark practices дают слишком фрагментарную картину их способностей, рисков и trade-offs. Затем авторы формулируют три элемента `holistic evaluation`: широкое покрытие с явным признанием неполноты, multi-metric measurement и стандартизацию условий сравнения. После этого paper переходит от общей рамки к HELM как конкретной реализации: вводит taxonomy сценариев и метрик, объясняет выбор core и targeted evaluations, показывает, почему одни и те же модели надо сравнивать по множеству desiderata, а не только по accuracy. В завершающей части работа обсуждает ограничения покрытия и подчеркивает, что HELM должен быть living benchmark, который со временем расширяется и делает свои пробелы явными.

## Структура материала
- `Abstract` и `1 Introduction`: зачем authors вводят `HELM` и какие три принципа считают центральными.
- `2 Preliminaries`: definitions для `scenarios`, `adaptation` и `metrics`.
- `3 Core scenarios`, `4 General metrics`, `5 Targeted evaluations`: собственно каркас HELM.
- `6 Models` и `7 Adaptation via prompting`: правила сравнения и setup.
- `8 Experiments and results`: empirical layer.
- `9 Related work and discussion`, `10 What is missing`, `11 Limitations and future work`, `12 Conclusion`: reflexive and critical layer.

## Как читать источник быстро
- Если нужен first-pass на 10 минут, открой `Abstract`, `1.1 HELM`, `1.2 Empirical findings` и `12 Conclusion`.
- Если вопрос именно про рамку HELM, переходи в `2 Preliminaries`, затем читай `3 Core scenarios`, `4 General metrics` и `5 Targeted evaluations`.
- Если интересует empirical слой, основной раздел — `8 Experiments and results`; appendices нужны уже точечно.
- Если нужен критический reading, не пропускай `10 What is missing` и `11 Limitations and future work`.

## Что здесь особенно важно
- **Taxonomy before benchmark.** Сначала нужно явно сказать, что вообще считаем значимыми сценариями и метриками, а уже потом выбирать конкретную реализацию.
- **Multi-metric evaluation** нужна не ради красоты, а чтобы не прятать fairness, toxicity, robustness и efficiency за одной accuracy.
- **Standardization** важна, если объектом сравнения считается сама модель, а не произвольная scenario-specific system.
- **Recognition of incompleteness** здесь не слабость, а честное свойство benchmark design.

## Что это добавляет к теме недели
HELM задает широкий и в некотором смысле оптимистичный взгляд на benchmark design: можно пытаться строить более честные и более прозрачные benchmark ecosystems за счет coverage, multiple metrics и living updates. Именно на этом фоне особенно хорошо читаются и ECBD, и The Benchmark Lottery, которые затем уточняют, где одной широты уже недостаточно.

## Что стоит запомнить при повторении
- **Benchmark design начинается до выбора dataset.**
- **Широта покрытия не отменяет необходимость явной рамки и признания пробелов.**
- **Если сравнение моделей не стандартизировано, вывод о различиях быстро размывается.**

## Связанные концепты
- [concepts/holistic-evaluation](../concepts/holistic-evaluation.md)
- [concepts/benchmark-design](../concepts/benchmark-design.md)
- [concepts/benchmarking](../concepts/benchmarking.md)
- [concepts/benchmark-lottery](../concepts/benchmark-lottery.md)

## Что осталось неясным / спорным
- Насколько справедливо требование стандартизации, если разным моделям оптимально подходят разные adaptation strategies?
- Когда широкий benchmark еще помогает видеть trade-offs, а когда уже превращается в тяжелый каталог метрик?

## Связанные страницы
- [weeks/week-03](../weeks/week-03.md)
- [sources/evidence-centered-benchmark-design-nlp](evidence-centered-benchmark-design-nlp.md)
- [sources/benchmark-lottery](benchmark-lottery.md)
- [syntheses/benchmark-design-evidence-and-incentives](../syntheses/benchmark-design-evidence-and-incentives.md)
- [syntheses/reading-course-sources](../syntheses/reading-course-sources.md)
