# SoundCloud Downloader
Telegram bot for downloading music from soundcloud.

### Requirements
`requirements.txt`.

### Environment variables:
- BOTTOKEN= `access token for telegram bot management`
- PROXYCONF= `login:pass@ip:port`

## Docker
### С первого октября сервис  `soundcloud.com` заблокирован на территории РФ!
Поэтому подключен прокси сервер.

Так как в проекте используются переменные среды GitHub, то запустить собранный самостоятельно образ не получится.
Используем заранее собранный образ: 

`docker pull kayat0n/soundcloud_bot:feature-7-add_Dockerfile`

`docker run c1f387245e48`

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