# Неделя 05

## Ключевая мысль
> **Week-05 завершает курс сдвигом от “как строить benchmark” к вопросу, когда evaluation вообще заслуживает доверия в high-stakes safety context.** После этой недели полезно помнить, что хороший safety eval требует не только score, но и честного разговора о coverage, risk quantification, measurement validity, reproducibility и о том, работаем ли мы вообще над важными проблемами.

## Зачем открывать эту страницу
Это hub-page пятой недели и одновременно завершающая страница всего текущего курса. Она нужна, чтобы собрать в одну линию три слоя разговора: чем safety benchmarking отличается от обычного benchmarking, почему evals должны становиться более зрелой дисциплиной и почему даже хорошие methodological frames бесполезны, если исследователь систематически выбирает удобные, но неважные задачи.

## Замысел недели от организаторов
В `raw/` теперь сохранена отдельная organizer note: [course-framing-week-05.md](../../raw/week-05/extra/course-framing-week-05.md). Она полезна как финальная рамка курса.

Если сжать ее до одного абзаца, получится так: первые недели уже показали limits of evals, проблемы benchmark design и сложности agent evaluation. Week-05 делает последний шаг и спрашивает, что вообще должно быть истинно, чтобы safety evaluation можно было воспринимать серьезно, если по нему хотят принимать решения о deployment, policy и risk thresholds. Здесь важно не только качество benchmark'а, но и зрелость всей measurement discipline.

## Главные вопросы недели
- **Чем safety benchmark отличается от обычного capability benchmark?** Безопасность нормативна, социотехнически встроена и плохо сводится к `fixed prompts` и `single scores`.
- **Что должно быть у зрелой evaluation discipline?** Здесь в центр выходят `coverage`, `reproducibility`, conceptual clarity, measurement validity и statistical rigor.
- **Как связать benchmark output с реальным risk?** Нужно различать observed rate, calibrated probability, severity и deployment context.
- **Почему research taste тоже относится к evals?** Потому что поле легко скатывается в easy-to-measure proxies вместо really important safety problems.

## Вопросы перед чтением и повторением
Эти вопросы полезны и до чтения, и после него: сначала они помогают заметить собственные мотивации и blind spots, а потом проверить, как изменилась оптика после курса.

- Почему вы вообще решили пройти курс по AI safety evals?
- Кажется ли вам, что работа в этой области — это интересная траектория именно для вас?

## Если нужно быстро вспомнить неделю
- Если нужен **самый строгий текст про то, что именно не так с современными safety benchmarks**, начинай с [How Should AI Safety Benchmarks Benchmark Safety?](../sources/how-should-ai-safety-benchmarks-benchmark-safety.md) и [AI Safety Benchmarks](../concepts/ai-safety-benchmarks.md).
- Если нужен **более широкий взгляд на maturational shift поля**, открывай [We Need A Science of Evals](../sources/we-need-a-science-of-evals.md) и [Science of Evals](../concepts/science-of-evals.md).
- Если нужен **финальный corrective на уровень research strategy**, смотри [You and Your Research](../sources/you-and-your-research.md) и [Research Taste](../concepts/research-taste.md).
- Если нужен **межисточниковый вывод недели**, переходи к [Reliable AI Safety Evals](../syntheses/reliable-ai-safety-evals.md).

## Если у тебя конкретный вопрос
- Если вопрос звучит как **“что именно safety benchmark должен мерить, чтобы говорить о safety, а не просто о capability?”**, начни с [How Should AI Safety Benchmarks Benchmark Safety?](../sources/how-should-ai-safety-benchmarks-benchmark-safety.md).
- Если вопрос звучит как **“какими признаками вообще должна обладать зрелая evaluation discipline?”**, читай [We Need A Science of Evals](../sources/we-need-a-science-of-evals.md).
- Если вопрос звучит как **“почему benchmark output нельзя напрямую читать как probability of real-world harm?”**, снова возвращайся к [How Should AI Safety Benchmarks Benchmark Safety?](../sources/how-should-ai-safety-benchmarks-benchmark-safety.md), а затем уточняй общую рамку через [We Need A Science of Evals](../sources/we-need-a-science-of-evals.md).
- Если вопрос звучит как **“как не соскользнуть в удобные, но неважные proxy-проблемы?”**, открывай [You and Your Research](../sources/you-and-your-research.md).

## Картина недели
Week-05 полезно читать как финальное сужение стандарта. Сначала safety benchmark paper показывает, что обычная benchmark logic плохо переносится на безопасность: здесь нужно думать не только о наборе задач, но и о normative constructs, severity, uncertainty и deployment relevance. Затем Apollo расширяет этот тезис до уровня поля: если evals служат основанием для real-world decisions, они должны проходить maturation от art-like craft к более строгой дисциплине. Наконец, Хэмминг поднимает разговор еще выше и напоминает, что даже правильные standards не спасут поле, если исследователи систематически работают над задачами, которые легко измерять, а не над задачами, которые действительно важны.

## Как материалы собираются в одну линию
- **Safety benchmark paper** дает самый конкретный технический разбор: `construct coverage`, `risk quantification` и `measurement validity`.
- **Apollo** делает шаг от critique отдельного benchmark'а к critique зрелости всей дисциплины и задает research program для `Science of Evals`.
- **Hamming** добавляет мета-слой: поле может иметь хорошие принципы и при этом все равно тратить основное внимание на неверно выбранные проблемы.

## Что нужно уметь объяснить своими словами
- **Почему safety benchmark нельзя читать как обычный capability benchmark.** Потому что он должен быть связан не только с observed behavior, но и с normatively defined harm и deployment context.
- **Почему observed failure rate не равен probability of harm.** Между sample score и real-world risk лежат severity, prevalence, uncertainty и системный контекст применения.
- **Почему `Science of Evals` — это не просто призыв делать больше benchmark'ов.** Речь идет о conceptual clarity, reproducibility, stronger statistical culture и о более зрелых claims.
- **Почему research taste относится к AI safety evals.** Потому что поле особенно уязвимо к соблазну работать над тем, что проще посчитать, вместо того, что действительно меняет safety picture.

## Практический слой
У week-05 нет notebook, но практический смысл здесь все равно очень конкретный. После этой недели полезно держать под рукой такой рабочий checklist:

- сначала явно формулировать, какой именно `harm construct` и какой claim поддерживает evaluation;
- отдельно документировать blind spots, excluded risks и assumptions about deployment;
- не называть sample proportion вероятностью, если нет calibrated risk model;
- связывать proxy-метрики с реальным deployment context, а не только с удобным benchmark setup;
- регулярно спрашивать себя, не сводится ли работа к удобным proxy-задачам вместо важных проблем.

## Источники недели
### Theory
- [How Should AI Safety Benchmarks Benchmark Safety?](../sources/how-should-ai-safety-benchmarks-benchmark-safety.md) — critique safety benchmarking через `construct coverage`, `risk quantification` и `measurement validity`
- [We Need A Science of Evals](../sources/we-need-a-science-of-evals.md) — призыв к maturation evals как дисциплины
- [You and Your Research](../sources/you-and-your-research.md) — финальный research-taste layer про важные проблемы и долгую траекторию

### Notebooks
- В `week-05` notebook нет; практический слой здесь в первую очередь методологический и исследовательский.

### Extra
- Дополнительные материалы пока не добавлены.

## Куда идти дальше внутри wiki
- Если нужен **один финальный synthesis по всему курсу**, смотри [From Evals To Reliable AI Safety Evals](../syntheses/course-arc-from-evals-to-reliable-safety.md).
- Если нужен **синтез всей недели**, смотри [Reliable AI Safety Evals](../syntheses/reliable-ai-safety-evals.md).
- Если нужен **язык про safety benchmark standards**, открывай [AI Safety Benchmarks](../concepts/ai-safety-benchmarks.md), [Measurement Validity](../concepts/measurement-validity.md) и [Risk Quantification](../concepts/risk-quantification.md).
- Если нужен **язык про зрелость поля в целом**, смотри [Science of Evals](../concepts/science-of-evals.md).
- Если нужен **финальный разговор о выборе задач**, переходи к [Research Taste](../concepts/research-taste.md).

## Что повторить после курса
- Evals полезны, но не самообъяснимы: claim зависит от measurement design и interpretation discipline.
- Benchmark не нейтрален: он определяет, что считается evidence и what progress even looks like.
- Agent evaluation добавляет проблему scaffolding, trajectories и elicitation.
- Safety evaluation поднимает еще более строгий вопрос: насколько measurement вообще связано с harm and deployment.
- Работа над evals требует не только техники, но и вкуса к важным проблемам.

## Примечание о raw
- Все три обязательных текста уже имеют хороший локальный текстовый raw.
- Для статьи про safety benchmarks дополнительно есть `PDF` и `TeX Source`, так что это сильный raw-набор.
- Для `week-05` нет notebook и пока нет дополнительных материалов поверх organizer note.

## Открытые вопросы
- Какие safety claims вообще реалистично поддерживать benchmark evidence, а какие требуют более широкого safety case?
- Насколько далеко можно продвинуть probabilistic risk quantification без хороших in-the-wild data?
- Как не допустить, чтобы `Science of Evals` превратилась просто в более формализованный набор слабых proxy-метрик?
- Какие проблемы в AI safety evals являются действительно важными, а не просто convenient research targets?

## Вопросы для обсуждения
- Как отличить важную проблему от просто громкой или модной?
- Какие проблемы в AI safety evals кажутся вам самыми важными после всех пяти недель?

## Краткий вывод
Week-05 полезна тем, что завершает курс не очередным benchmark recipe, а повышением стандарта. После нее уже трудно говорить о “хорошем eval” только в терминах dataset, score и leaderboard. В фокус попадает связь между measurement и harm, зрелость всей дисциплины и выбор тех проблем, которые вообще стоит делать центром поля.
