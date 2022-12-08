# SoundCloud Downloader
Telegram bot for downloading music from soundcloud.

## Тесты

Ветка `main`: [![Tests_pipeline](https://github.com/11-kt/SoundCloud-Telegram_Bot/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/11-kt/SoundCloud-Telegram_Bot/actions/workflows/tests.yml)

Ветка `develop`: [![Tests_pipeline](https://github.com/11-kt/SoundCloud-Telegram_Bot/actions/workflows/tests.yml/badge.svg?branch=develop)](https://github.com/11-kt/SoundCloud-Telegram_Bot/actions/workflows/tests.yml)


### Requirements
`requirements.txt`.

### Environment variables:
- BOTTOKEN= `access token for telegram bot management`
- PROXYCONF= `login:pass@ip:port`

## Docker

#### 1. Клонирование репозитория

`git clone https://github.com/11-kt/SoundCloud-Telegram_Bot.git`

#### 2. Папка проекта

`cd SoundCloud-Telegram_Bot`

#### 3. Построение образа

`docker build -t sctg .`

#### 4. Запуск

`docker run -t sctg`

### С первого октября сервис  `soundcloud.com` заблокирован на территории РФ!
Поэтому подключен прокси сервер.

Так как в проекте используются переменные среды GitHub, то запустить собранный самостоятельно образ не получится.
Используем заранее собранный образ: 

`docker pull kayat0n/soundcloud_bot:feature-7-add_Dockerfile`

`docker run b33a014dd927`

## Examples
Для начала начнем взаимодействие с ботом.
Для этого нужно написать ему по адресу: 

`t.me/S0undCl0udBot`.

![](./screens/find_bot.png)

Далее нажимаем кнопку: `ЗАПУСТИТЬ`

![](./screens/start.png)

Теперь нужно поздороваться!

Бот откликается на слово: `Привет`

![](./screens/say_hi.png)

Отправляем ссылку на трек.

Когда бот получит ссылку, он уточнит формат скачивания.

![](./screens/pick_format.png)

После выбора формата, вы получите сообщение с аудиофайлом.

![](./screens/results.png)

## License

[Apache](./LICENSE)