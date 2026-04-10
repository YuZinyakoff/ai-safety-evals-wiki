# Benchmarking Prompt Sensitivity In Large Language Models

- Тип источника: extra
- Неделя: week-01
- Raw: `raw/week-01/extra/2502.06065v1.pdf`
- Оригинал: https://arxiv.org/abs/2502.06065
- Полнота raw: PDF статьи

## Зачем источник в базе
Это полезный empirical counterweight к более общим рассуждениям про under-elicitation. Источник нужен, чтобы на конкретном benchmark-материале увидеть: observed capability зависит не только от модели, но и от phrasing prompt.

## Краткое содержание
Статья вводит задачу Prompt Sensitivity Prediction и датасет PromptSET для изучения того, как небольшие переформулировки одного и того же information need влияют на способность LLM дать корректный ответ. Работа показывает, что существующие baselines плохо справляются с предсказанием prompt sensitivity, а сама формулировка запроса заметно влияет на answerability. Для week-01 это один из самых наглядных материалов, потому что он превращает общее подозрение про "prompt matters" в отдельный объект измерения.

## Ключевые идеи
- Небольшие изменения prompt formulation могут радикально менять качество ответа.
- Prompt sensitivity worth studying as a benchmark problem, а не только как anecdotal issue prompt engineering.
- Авторы формализуют задачу Prompt Sensitivity Prediction.
- PromptSET строится на Prompt-variation pairs с тем же information need.
- Существующие baselines не закрывают задачу надежно.

## Опорные тезисы из источника
- Статья определяет prompt sensitivity как существенную зависимость качества ответа от малых изменений phrasing, structure или punctuation.
- Для PromptSET используются вопросы из TriviaQA и HotpotQA.
- Авторы получили 11,469 уникальных prompts и для каждого сгенерировали по 9 variations.
- Variations генерировались с помощью LLaMA 3.1 8B и Mistral-Nemo, затем фильтровались по semantic similarity и quality.
- В benchmark сравниваются LLM self-evaluation, text classification и query performance prediction baselines.
- Авторы сообщают, что specificity-based QPP baselines работают слабо, а существующие методы в целом не захватывают сложность prompt sensitivity prediction.
- Более похожие на original prompt variations чаще оказываются answerable.
- Prompt reformulation может превращать исходно неудачный prompt в ответимый.

## Что это добавляет к теме недели
Источник делает более конкретной общую проблему under-elicitation: observed capability частично зависит от того, как именно сформулирован prompt. Для темы evals это важное напоминание, что даже при фиксированной модели измеряемый результат чувствителен к interface design, а значит качество elicitation становится частью reliability самого eval. При перечитывании курса эта страница полезна как мост между теоретической критикой behavioral evidence и вполне прикладной задачей prompt design.

## Связанные концепты
- [concepts/prompt-sensitivity](../concepts/prompt-sensitivity.md)
- [concepts/behavioral-evals](../concepts/behavioral-evals.md)
- [concepts/evals](../concepts/evals.md)
- [concepts/inspect-ai](../concepts/inspect-ai.md)

## Что осталось неясным / спорным
- Как строить eval prompts так, чтобы prompt sensitivity меньше искажала измерение capabilities?
- Можно ли заранее предсказывать удачные reformulations достаточно надежно для production pipelines?

## Связанные страницы
- [weeks/week-01](../weeks/week-01.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
