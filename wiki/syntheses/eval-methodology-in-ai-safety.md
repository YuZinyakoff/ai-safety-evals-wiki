# Eval Methodology in AI Safety

## Короткий тезис
> **Цикл лекций показывает, что методология evals важна для AI safety не только потому, что от нее зависят benchmark scores, а потому, что она влияет на саму способность поля накапливать осмысленное знание, operationalize safety-relevant concepts и не застревать в удобных, но слабых формах эмпирики.**

## Как устроен цикл
- **Лекция 1** строит контекст: почему AI safety находится в unusually тяжелом epistemic положении и почему улучшение методологии evals может быть leverage point.
- **Лекция 2** уточняет роль evals как эмпирического инструмента: поле ломается не только без проверки, но и из-за плохих проверок и слабых теорий.
- **Лекция 3** переводит разговор в research direction: проблема methodology упирается в операционализацию самих constructs, например целей системы и онтологии измерения.

## Что этот цикл добавляет к курсу
- Он делает явным то, что в недельных материалах было распределено по разным темам: **measurement practice влияет на темп knowledge accumulation**, а не только на качество одного benchmark.
- Он помогает связать **benchmark design**, **measurement validity**, **science of evals** и **research taste** в одну линию.
- Он показывает, что слабость evals может начинаться очень рано: не на уровне статистики, а на уровне того, **что именно поле пытается operationalize**.

## Где он особенно хорошо стыкуется с основной дугой курса
- С **week-01**: потому что limits of behavioral evidence здесь становятся частью более общего methodological bottleneck.
- С **week-03**: потому что benchmark здесь понимается как содержательная конструкция и даже как частичная онтология измерения.
- С **week-05**: потому что идея `Science of Evals` получает более глубокий фон про предпарадигмальное состояние поля и слабость текущей эмпирической дисциплины.

## Что именно ломает наивный вывод
- **Много evals не значит хорошая methodology.**
- **Наличие эмпирики не значит наличие хорошей проверки.**
- **Хорошая проверка не спасает, если объект измерения плохо operationalized.**
- **Даже полезные benchmark results не гарантируют, что поле движется к действительно важным safety questions.**

## Практическая польза этого слоя
Этот shared-цикл полезен не как replacement для недельных материалов, а как корректирующая оптика. Он помогает задавать более ранние и более жесткие вопросы:

- Что именно считается evidence в нашем eval?
- На какой теории или хотя бы рабочей модели строится переход от score к claim?
- Не подменили ли мы важную safety-problem удобной операционализацией?
- Помогает ли наш evaluation regime реально накапливать знание, или только производит локальные numbers?

## Где остается напряжение
- **Empirical necessity vs weak theory.** Без эмпирики поле не двигается, но сама эмпирика в условиях слабой теории легко становится fragile.
- **Operationalization vs distortion.** Чтобы что-то измерять, нужно operationalize construct; но сама операционализация может сузить или исказить исходную задачу.
- **Methodology improvement vs deeper alignment difficulty.** Улучшение evals может сильно помочь, но не снимает трудность самих alignment objects.

## Открытые вопросы
- Какие pieces of better eval methodology наиболее tractable уже сейчас?
- Где improvement in methodology действительно ускоряет safety progress, а где упирается в lack of theory?
- Какие AI safety constructs вообще достаточно сформированы, чтобы под них строить сильные evals?

## Связанные страницы
- [sources/slava-meriton-evals-methodology-lecture-01](../sources/slava-meriton-evals-methodology-lecture-01.md)
- [sources/slava-meriton-evals-methodology-lecture-02](../sources/slava-meriton-evals-methodology-lecture-02.md)
- [sources/slava-meriton-evals-methodology-lecture-03](../sources/slava-meriton-evals-methodology-lecture-03.md)
- [concepts/eval-methodology](../concepts/eval-methodology.md)
- [concepts/science-of-evals](../concepts/science-of-evals.md)
- [concepts/measurement-validity](../concepts/measurement-validity.md)
- [syntheses/course-arc-from-evals-to-reliable-safety](course-arc-from-evals-to-reliable-safety.md)
