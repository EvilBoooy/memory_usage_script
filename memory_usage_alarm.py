import psutil
import requests

# Установите URL API, на который будет отправлен запрос
api_url = "https://example.com/api/alarm"

# Установите пороговое значение потребления памяти в процентах
threshold = 80

# Получите текущее потребление памяти
memory_usage = psutil.virtual_memory().percent

# Проверьте, превышает ли потребление памяти пороговое значение
if memory_usage > threshold:
    # Отправьте HTTP запрос на API
    response = requests.post(
        api_url,
        json={"message": "Тревога! Высокое потребление памяти!"}
        )

    # Проверьте статус код ответа
    if response.status_code == 200:
        print("Тревога успешно отправлена!")
    else:
        print("Не удалось отправить тревогу.")
else:
    print("Потребление памяти находится ниже порога.")
