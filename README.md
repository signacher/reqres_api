<table width="100%" border='0'>
 <tr><td width="40%" valign="bottom"><img src="https://github.com/signacher/signacher/blob/main/images/reqres.png" title="reqres" alt="reqres" width="380" height="200"/></td><td valign="middle">
 <h2>Пример организации автотестирования API для сайта <a target="_blank" href="https://reqres.in/">www.reqres.in</a></h2>
 </td></tr>
</table>


## :open_book: Содержание:
- [Описание проекта](#heavy_check_mark-описание)
- [Технологии и инструменты](#gear-технологии-и-инструменты)
- [Реализованные проверки](#ballot_box_with_check-реализованные-проверки)
- [Запуск тестов в Jenkins](#-как-запускать-тесты)
- [Allure отчет](#-allure-отчет-о-прохождении-тестов)
- [Уведомления в Telegram](#-уведомление-в-telegram)
- [Интеграция с Allure TestOps](#-интеграция-с-allure-test-ops)
- [Интеграция с Jira](#-интеграция-с-jira)
  
## :heavy_check_mark: Описание:
> - Демо проект по автоматизации тестирования API сайта <a target="_blank" href="https://reqres.in/"> www.reqres.in</a>
> - Проект создан в рамках обучения на курсе <a target="_blank" href="https://qa.guru/python"> QA GURU Автоматизация тестирования на Python</a>
> - Тесты написаны на языке <code>Python</code> с помощью библиотеки <code>Requests</code>
> - Запуск тестов осуществляется в <code>Jenkins</code>
> - В тестах проверяется бизнес-логика, коды ответа, валидируется схема ответа с помощью библиотеки <code>JsonSchema</code>
> - По результатам тестов формируется <a target="_blank" href="https://jenkins.autotests.cloud/job/my_reqres_api/allure/"><code>Allure</code></a> отчет с вложениями (код ответа, курл, параметры и тд.) 
> - Отправляется уведомление о результатах прохождения тестов в <code>Telegram</code> 
> - Реализована интеграция с <code>AllureTestOps</code> и <code>Jira</code> 
## :gear: Технологии и инструменты:
<div align="center">
  <img src="https://github.com/signacher/signacher/blob/main/images/python.png" title="Python" alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/pycharm.png" title="Pycharm" alt="Pycharm" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/pytest.png" title="Pytest" alt="Pytest" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/requests.png" title="Requests" alt="Requests" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/jenkins.png" title="Jenkins" alt="Jenkins" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/github.png" title="GitHub" alt="GitHub" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/allure.png" title="Allure" alt="Allure" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/allure_testops.png" title="Allure TestOps" alt="Allure TestOps" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/jira.png" title="Jira" alt="Jira" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/tg.png" title="Telegram" alt="Telegram" width="40" height="40"/>&nbsp;
</div>

## :ballot_box_with_check: Реализованные проверки:
- [x] Создание пользователя
- [x] Создание пользователя без одного, без всех параметров
- [x] Удаление пользователя
- [x] Получение информации о пользователе
- [x] Получение информации о  несуществующем пользователе
- [x] Изменение данных пользователя.
- [x] Валидация схемы ответа

## <img width="3%" title="Jenkins" src="https://avatars.githubusercontent.com/u/2520748?v=4"> Как запускать тесты:
<h3>Тесты запускаются в <a target="_blank" href="https://jenkins.autotests.cloud/job/my_reqres_api/"> Jenkins.</a></h3>

> Для запуска тестов нажать кнопку Собрать сейчас(Build Now)
<br></br>
  ![Screen Actions1](images/Jenkins1.png)
<br></br>
## <img width="3%" title="Allure" src="https://github.com/signacher/signacher/blob/main/images/allure_report.png"> Allure отчет о прохождении тестов

Пример отчета по ссылке <a target="_blank" href="https://jenkins.autotests.cloud/job/my_reqres_api/allure/"> https://jenkins.autotests.cloud/job/my_reqres_api/allure/</a>
> Для перехода в отчет из Jenkins иконки 1,2 или 3 на скрине

![Screen jenkins1](images/Jenkins3.png)

###### Главный экран (Overview)
![Screen Allure1](images/AllureReport1.png)

*Главная страница Allure-отчета содержит следующие информационные блоки:*

> - [x] <code><strong>*ALLURE REPORT*</strong></code> - отображается дату и время прохождения теста, общее количество тест кейсов, а также диаграмма с указанием процента и количества успешных, упавших и сломавшихся в процессе выполнения тестов
>- [x] <code><strong>*TREND*</strong></code> - отображает тренд прохождения тестов от сборки к сборке
>- [x] <code><strong>*SUITES*</strong></code> - отображает распределение результатов тестов по тестовым наборам
>- [x] <code><strong>*CATEGORIES*</strong></code> - отображает распределение неуспешно прошедших тестов по видам дефектов
>- [x] <code><strong>*ENVIRONMENT*</strong></code> - отображает тестовое окружение, на котором запускались тесты 
>- [x] <code><strong>*FEATURES BY STORIES*</strong></code> - отображает распределение тестов по функционалу, который они проверяют
>- [x] <code><strong>*EXECUTORS*</strong></code> - отображает исполнителя текущей сборки (ссылка на сборку в Jenkins)

<details><summary><strong>Структура тестов</strong></summary>

![Screen Allure2](images/AllureReport2.png)
</details> 

<details><summary><strong>Вложения для каждого теста: Время запроса, код ответа, курл запроса,передаваемые параметры, json ответа </strong></summary>
 
![Screen Allure3](images/AllureReport3.png)
</details>



## <img width="3%" title="Telegram" src="https://github.com/signacher/signacher/blob/main/images/tg.png"> Уведомление в Telegram

После прохождения тестов в телеграмм канал бот присылает уведомление с краткой информацией и ссылкой на отчет. Так же можно добавить уведомления на почту, в `Discord`, `Slack` и другие мессенджеры

<img width="40%" title="Telegram" src="images/telegram.jpg">

### <img width="3%" title="Allure TestOps" src="https://github.com/signacher/signacher/blob/main/images/allure_testops.png"> Интеграция с Allure Test Ops
### [Dashboard](https://allure.autotests.cloud/project/4025/dashboards)
> Для перехода из Jenkins нажать 1

![Testops1](images/Jenkins2.png)

Все данные о запусках тестов также хранятся в Allure TestOps
![Testops1](images/AllureTestOps1.png)

> <details><summary><strong>TestOps автоматически формирует тест кейсы на основе результатов прохождения тестов</strong></summary>
>
>![Testops4](images/AllureTestOps4.png)
></details>
>
><details><summary><strong>Можно фильтровать тесты и запускать их выборочно непосредственно из TestOps</strong></summary>
>
>![Testops3](images/AllureTestOps3.png)
></details>
>
> - Можно создавать ручные тест кейсы и импортировать их в IDE с помощью плагина
> - Результаты тестирования отображаются в реальном времени во время прохождения теста
> - Можно настроить интеграцию с `Jira`

### <img width="3%" title="Jira" src="https://github.com/signacher/signacher/blob/main/images/jira.png"> Интеграция с Jira
#### [Задача в Jira](https://jira.autotests.cloud/browse/HOMEWORK-1105)

В задачу Jira из Allure TestOps можно добавить список тест кейсов и ссылку на запуски тестов. 
![Jira1](images/jira1.png)

