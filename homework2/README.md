# Использованные паттерны

## 1. Декторатор
Добавлен класс RandomWeather, который позволяет получать динамическую скорость ветра

## 2. Фабричный метод
Добавлен класс CarFactory, позволяющий создавать автомобили по названию с заранее заданными характеристиками

## 3. Шаблонный метод
Класс Competition объявлен абстрактным, и он описывает общую логику проведения соревнования.
Для создания конкретных сорвнований нужно относледоваться от Competition 
и определить логику вычисления затраченного участниками времени.  
Для конкретного соревновния автомобилей создан класс RacingCompetition.