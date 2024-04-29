# Потихоньку пишу диплом (хелпдеск)

## В планах создание 3-ех модулей:
1. Модуль отправки заявки
2. Модуль авторизации
3. Модуль отчетов
   
### Модуль отправки заявки сделан приблизительно наполовину
1. Требуется связать таблицу пользователей и модель программы.
2. Требуется автоматизировать проставление даты при установке отметки о закрытии.
3. Добавить возможность прикреплять файл?

### Модуль авторизации готов почти полностью:
1. Необходимо закрыть возможность открытия страниц сайта неавторизованным пользователем.

### Модуль отчетов не сделан совсем:
1. В планах просто выводить количество выполненных заявок за указанный пользователем промежуток времени. (Если будет время сделать форму печати).
  
#**Самое важное красиво оформить веб-приложение**


Что было сделано:
1. Заявка отправляется, автоматически проставляюся требуемые поля (даты, приоритет, статус).
2. Авторизация сделана при помощи библиотеки джанго. Заход происходит только при введении правильного логина и пароля, иначе предлагает повторный вход.
3. Редактирование заявки, проставление отметок выполнено при помощи админ панели джанго.
