# Скрипт оповещения о потреблении памяти

Этот скрипт отслеживает потребление памяти системы и отправляет HTTP запрос на указанный API, когда потребление превышает заданный порог.

## Предварительные требования

- Python 3.x

## Установка зависимостей

1. Установите Python 3.x, если его еще нет на вашей системе.

2. Создайте виртуальное окружение и войдите в него:
- `python -m venv venv`
- `source venv/Scripts/activate`

3. Установите зависимости, выполнив следующую команду:
- `**python -m venv venv`

## Использование

1. Клонируйте репозиторий или загрузите файл скрипта.

2. Откройте файл скрипта и установите следующие переменные:
- `api_url`: URL API, на который будет отправлен запрос.
- `threshold`: Пороговое значение потребления памяти в процентах.

3. Запустите скрипт с помощью следующей команды:
python memory_usage_alarm.py


## Как это работает

1. Скрипт использует библиотеку `psutil` для получения текущего потребления памяти системы.

2. Он сравнивает потребление памяти с заданным порогом.

3. Если потребление памяти превышает пороговое значение, отправляется HTTP запрос на указанный URL API с JSON-полезной нагрузкой, содержащей сообщение о тревоге.

4. Скрипт выводит сообщение об успешной отправке запроса, если запрос был успешно отправлен, или сообщение об ошибке, если произошла ошибка.

## Внесение вклада

Внесение вклада приветствуется! Если вы обнаружили проблемы или у вас есть предложения по улучшению, пожалуйста, создайте issue или отправьте pull request.

## Лицензия

Этот скрипт распространяется под [лицензией MIT](LICENSE).
