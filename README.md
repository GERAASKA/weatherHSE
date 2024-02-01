# [🌤️] weatherHSE
[weatherHSE](https://t.me/wheatherpythonhsebot) - это телеграм-бот, который ищет прогноз погоды с интересующего места.

## Содержание

- [Описание](#описание)
- [Начало Работы](#начало-работы)
- [Использование](#использование)
- [Распределение людей внутри команды](#распределение)
- [Используемое API](#используемое-api)
- [Контактная информация](#контактная-информация)

## Описание 

🌤️ weatherHSE  – это удобный и надежный способ получить актуальную информацию о погоде прямо в мессенджере. Наш бот обеспечивает пользователей всей необходимой информацией о текущих погодных условиях, температуре, влажности, скорости ветра и других параметрах.

Просто отправьте боту запрос с названием города или вашим местоположением, и в течение секунды вы получите подробный отчет о текущей погоде.

## Использоание со стороны пользователя
 
1. Пользователь запускает бота, отправляя **/start**.
2. Пользователь вводит город с помощью **/search <запрос>**.
3. Бот выполняет поиск погодных условий по городу, который ввел пользователь.
4. Бот предоставляет информацию о погоде: температуре, влажности, скорости ветра и других параметрах.
5. Пользователь доволен.

## Логика бота

Импорт библиотек и установка логирования:
- **`requests`**: Для выполнения HTTP-запросов к API погоды.
- **`datetime`**: Для работы с датой и временем.
- **`logging`**: Для ведения логов.
- **`config`**: Импорт токенов бота и API погоды из отдельного файла.
- **`Bot, types, Dispatcher, executor`** из aiogram: Компоненты для работы с телеграм-ботом.
Настройка базовой конфигурации логирования в файл **weather_bot.log**.

Инициализация бота и диспетчера:
- Создание объекта бота (Bot) и диспетчера (Dispatcher) для обработки сообщений и команд.

Обработчик команды "/start":
- **`start_command`**: Ответ на команду "/start" приветствует пользователя и предлагает ввести название города для получения погоды.

Обработчик всех остальных сообщений:
- **`get_weather`**: Обрабатывает любые другие сообщения, предполагая, что они содержат название города. Посылает запрос к API OpenWeatherMap, получает информацию о погоде и отправляет ответ пользователю.

Словарь code_to_smile:
Сопоставляет основные типы погоды с соответствующими эмодзи.

Обработка исключений:
Обрабатываются ошибки запросов (requests.exceptions.RequestException) и другие неожиданные ошибки (Exception). В случае ошибок отправляются соответствующие сообщения пользователю.

Запуск бота:
Если скрипт выполняется как основная программа (а не импорт), запускается цикл опроса новых сообщений бота через executor.start_polling(dp).
Логирование:

Логи пишутся в файл weather_bot.log с указанием времени, уровня логирования и текста сообщения.

## Используемое API

1. [Телеграм Bot API](https://t.me/BotFather) - телеграм бот, созданный для разработчиков, cоздающих ботов для Telegram.
2. [OpenWeatherMap](https://openweathermap.org/) - API для тех кто хочет получать все данные о погоде из базы данных максимально быстро в удобном формате.
