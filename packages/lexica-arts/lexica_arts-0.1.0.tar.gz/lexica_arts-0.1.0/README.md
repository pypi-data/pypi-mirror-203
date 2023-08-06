Модуль `lexica_arts` предоставляет класс `Image`, который используется для генерации изображений с помощью API-сервиса Lexica. Для использования модуля необходимо установить библиотеки aiohttp и Pillow (библиотека для работы с изображениями).

Класс Image содержит метод generate, который принимает два параметра: `prompt` и `negative`. Параметр `prompt` содержит описание изображения, которое необходимо сгенерировать, а параметр `negative` содержит негативное описание (необязательно).

Пример использования модуля:

```import lexica_arts

api_key = 'your_api_key'

image = lexica_arts.Image(api_key)

generated_image = await image.generate(prompt="beautiful sunset", negative="cloudy sky")
