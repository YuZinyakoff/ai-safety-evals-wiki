# Benchmark Design, Evidence, And Incentives

## Короткий тезис
> **Week-03 показывает, что benchmark — это не прозрачное окно в способности модели, а механизм отбора evidence.** Он одновременно определяет, что станет видимым в отдельной оценке и что поле начнет считать прогрессом.

## Где источники согласны
- **Benchmarking остается полезным.** Ни один из текстов недели не предлагает отказаться от benchmark'ов как таковых.
- **Benchmark design matters.** Все ключевые источники сходятся в том, что задачи, метрики, aggregation rules и documentation — это часть результата, а не нейтральный фон.
- **Один score почти всегда слишком слаб.** HELM, ECBD и Benchmark Lottery по-разному приходят к мысли, что single-number reading слишком груба.
- **Нужна большая прозрачность.** То, что benchmark измеряет и чего не измеряет, должно быть описано явнее.

## Как источники усиливают друг друга
- **HELM** показывает, что benchmark можно мыслить шире: как coverage + multi-metric + standardized comparison.
- **ECBD** делает этот подход строже и заставляет спрашивать, почему benchmark вообще собирает нужное evidence.
- **The Benchmark Lottery** добавляет уровень ecosystem critique: benchmark design влияет не только на отдельный вывод о модели, но и на траекторию всей области.
- **Hardt** помещает это в более длинную историю ML benchmarking и объясняет, почему именно сейчас ranking stability и benchmark science становятся центральными вопросами.
- **BenchmarkCards** переводит разговор в слой benchmark governance и показывает, что design без documentation слишком легко неправильно читать и использовать.
- **Construct validity** добавляет последний слой: даже правильно спроектированный benchmark еще не автоматически оправдывает capability words, которыми его описывают.

## Что именно ломает наивный вывод
- **Сначала benchmark выбирает, что считать evidence.** Это уже влияет на вывод.
- **Потом aggregate score скрывает структуру различий.** Trade-offs между сценариями и метриками исчезают.
- **Дальше ecosystem начинает оптимизировать именно это представление о прогрессе.**
- **И наконец language of claims может стать слишком сильным.** Benchmark score начинает читаться как доказательство “reasoning”, “utility” или “alignment”, хотя benchmark поддерживает куда более узкий claim.

## Где остается напряжение
- **Coverage vs validity.** HELM тянет в сторону широты, ECBD — в сторону строгой evidence chain. Обе интуиции важны, но между ними есть реальное напряжение.
- **Standardization vs model-specific adaptation.** Чтобы сравнение было честным, хочется общих правил; чтобы сравнение было содержательным, иногда хочется разных adaptation choices для разных моделей.
- **Living benchmarks vs stable benchmarks.** Динамичность помогает бороться с contamination и boundedness, но усложняет интерпретацию и сравнимость во времени.
- **Documentation vs gaming risk.** Больше прозрачности полезно, но она же может упрощать exploitation benchmark'а.

## Практическая дисциплина после этой недели
После любого сильного benchmark claim полезно спрашивать не только “какой score получился”, но и:
- **Какой capability или риск здесь вообще пытаются измерить?**
- **Какая цепочка design decisions стоит между construct и metric?**
- **Что benchmark делает видимым, а что оставляет вне поля зрения?**
- **Как этот benchmark влияет на incentives и narrative о прогрессе?**
- **Насколько язык итогового claim сильнее, чем реально поддерживаемое evidence?**

Именно эта последовательность и есть главный практический результат week-03.

## Открытые вопросы
- Можно ли совместить HELM-style breadth и ECBD-style justification без слишком тяжелой benchmark machinery?
- Какие benchmark properties сегодня важнее всего для устойчивых model rankings?
- Как строить benchmark ecosystems, которые меньше подталкивают поле к narrow leaderboard optimization?

## Связанные страницы
- [weeks/week-03](../weeks/week-03.md)
- [concepts/benchmark-design](../concepts/benchmark-design.md)
- [concepts/holistic-evaluation](../concepts/holistic-evaluation.md)
- [concepts/evidence-centered-benchmark-design](../concepts/evidence-centered-benchmark-design.md)
- [concepts/benchmark-lottery](../concepts/benchmark-lottery.md)
- [concepts/construct-validity](../concepts/construct-validity.md)
