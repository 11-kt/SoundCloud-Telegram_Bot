# Первая стадия
FROM python:3.10 AS build

COPY requirements.txt requirements.txt

# Скачиваем зависимости
RUN pip install --user -r requirements.txt

# Вторая стадия
FROM python:3.10-slim

# Копируем необходимые зависимости
COPY --from=build /root/.local /root/.local
COPY src .

# Обновляем путь
ENV PATH=/root/.local:$PATH

# Передаем токен бота
ARG bot_token
ENV BOTTOKEN=$bot_token

# Передаем login/password и ip/port прокси сервера
ARG proxy_login
ENV PROXYCONF=$proxy_login

# Запускаем
CMD ["python", "./Sound_Cloud_Bot/main.py"]