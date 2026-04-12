# Reliable AI Safety Evals

## Короткий тезис
> **Week-05 показывает, что надежный AI safety eval требует одновременно трех вещей:** честного разговора о том, что именно benchmark измеряет, более зрелой discipline вокруг coverage and trustworthiness, и исследовательского вкуса, который не дает полю застрять в easy-to-measure proxies.

## Где источники согласны
- **Текущих evaluation practices недостаточно для сильных safety claims.** Ни один из трех текстов не поддерживает идею, что нынешние benchmark scores можно просто читать как safety verdict.
- **Measurement должен быть честнее по отношению к своим ограничениям.** Это видно и в paper про safety benchmarks, и в Apollo-тексте про maturation field.
- **Нужно явно различать локальный результат и его downstream interpretation.** В одном случае это выражается через `measurement validity` и `risk quantification`, в другом — через language of `Science of Evals`.
- **Выбор проблем сам по себе влияет на качество поля.** Хэмминг добавляет здесь человеческий и карьерный слой, но он хорошо стыкуется с общей темой недели.

## Как источники усиливают друг друга
- **Safety benchmark paper** дает наиболее конкретный инженерный каркас: `construct coverage`, `risk quantification`, `measurement validity`, плюс checklist.
- **Apollo** превращает эту локальную critique в более широкий research program: зрелая science of evals должна уметь объяснять, что измеряется и насколько trustworthy result.
- **Hamming** не спорит с техническими требованиями, а защищает их от другого типа провала: даже хороший measurement stack бесполезен, если поле в целом выбирает не те задачи.

## Что именно ломает наивный вывод
- **Сначала benchmark ограничивает пространство рисков тем, что он вообще умеет видеть.**
- **Потом observed rate начинают читать как probability of harm, хотя для этого часто нет оснований.**
- **Дальше proxy metric принимают за саму safety property, хотя между ними может быть длинная и невалидированная цепочка.**
- **И наконец исследовательская экосистема награждает решение удобных benchmark problems, что может закреплять слабые proxies вместо движения к важным вопросам.**

Именно поэтому фраза "у нас есть safety benchmark и хороший score" почти всегда слишком слаба для consequential decisions.

## Практическая дисциплина после этой недели
После любого safety-relevant evaluation полезно спрашивать:

- **Какой harm construct здесь вообще измеряется?**
- **Какие blind spots и excluded risks документированы явно?**
- **Говорим ли мы о sample frequency или уже о более сильном risk claim?**
- **Чем proxy score связан с реальным deployment context?**
- **Не является ли сама задача удобной, но слишком узкой заменой более важной проблемы?**

## Где остается напряжение
- **Narrow but rigorous benchmark vs broader but fuzzier safety case.** Чем ближе к deployable score, тем сильнее желание упростить картину; чем честнее к сложности, тем труднее сравнивать и стандартизировать.
- **Policy relevance vs epistemic humility.** Политике и governance нужны actionable thresholds, а сама область пока слишком молода для многих таких claims.
- **Important problems vs easy problems.** Поле может очень эффективно прогрессировать в измерении того, что было удобно operationalize, и при этом плохо двигаться в сторону действительно consequential questions.

## Открытые вопросы
- Какие элементы mature science of evals можно реально построить в ближайшие годы, а какие пока остаются aspirational?
- Как сочетать benchmark evidence с broader safety case, не подменяя одно другим?
- Какие AI safety evals problems сейчас одновременно и important, и practically tractable?

## Связанные страницы
- [weeks/week-05](../weeks/week-05.md)
- [concepts/ai-safety-benchmarks](../concepts/ai-safety-benchmarks.md)
- [concepts/science-of-evals](../concepts/science-of-evals.md)
- [concepts/measurement-validity](../concepts/measurement-validity.md)
- [concepts/risk-quantification](../concepts/risk-quantification.md)
- [concepts/research-taste](../concepts/research-taste.md)
