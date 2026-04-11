# Prompt Sensitivity

## Коротко
> **Prompt sensitivity** — это зависимость качества ответа от небольших изменений формулировки одного и того же запроса. В контексте evals это важно не как бытовая техника “лучше писать промпты”, а как источник хрупкости самого измерения.

## Почему это важный концепт
Week-01 много говорит про under-elicitation и limits of behavioral evidence. Prompt sensitivity делает эту проблему очень наглядной: иногда observed capability меняется не потому, что модель “может / не может”, а потому что prompt оказался удачным или неудачным.

## Как именно это ломает вывод
- **Один и тот же information need** не гарантирует один и тот же observed result.
- **Результат зависит от elicitation quality.** Значит benchmark score partly measures prompt design, а не только модель.
- **Низкий score** может означать не отсутствие capability, а плохую формулировку задачи.
- **Сравнение моделей** может оказаться чувствительным к phrasing choice, а не только к реальной разнице в capability.

## Как распознать это в реальном eval
- Когда малые переформулировки заметно меняют answerability.
- Когда разные prompt templates дают разные rankings или очень разные absolute scores.
- Когда после reformulation модель внезапно “обретает” способность, которую до этого считали отсутствующей.

## Практическая интуиция
Полезно держать в голове такую формулу: **prompt sensitivity не всегда означает, что модель плохая, но почти всегда означает, что measurement fragile**. Именно поэтому этот концепт так важен для wiki по evals: он помогает не путать prompt engineering с вопросом reliability evidence.

## С чем легко перепутать
- Prompt sensitivity легко свести к бытовому prompt engineering, хотя для week-01 это прежде всего measurement problem.
- Ее легко спутать со случайным шумом, хотя paper показывает систематические и practically important differences.
- Чувствительность к phrasing не всегда означает отсутствие capability, но почти всегда означает, что observed result нельзя читать слишком прямолинейно.

## Где смотреть дальше
- [Prompt Sensitivity paper](../sources/prompt-sensitivity-benchmark.md) — основная source page по теме.
- [Behavioral Evals](behavioral-evals.md) — более широкий контекст limits of observed behavior.
- [Inspect AI](inspect-ai.md) — место, где становится видно, как prompt design входит в workflow.

## Открытые вопросы
- Как отделить prompt sensitivity от реального отсутствия capability?
- Какие prompt-construction practices уменьшают искажения в eval settings?

## Связанные страницы
- [concepts/behavioral-evals](behavioral-evals.md)
- [concepts/inspect-ai](inspect-ai.md)
- [syntheses/evals-scope-and-limits](../syntheses/evals-scope-and-limits.md)
