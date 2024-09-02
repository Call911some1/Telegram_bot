# Name Converter Bot

Этот телеграмм бот конвертирует имена с кириллицы на латиницу, а так же записывает и логирует все действия в отдельный фаил в Docker-контейнере.

## Для запуска нужно:

- Docker
- telegram bot API Token

## Как запустить?

1. **Клонируй репозиторий**

```bash
git clone https://github.com/Call911some1/name_converter_bot.git
cd name_converter_bot

2. **Создайте Docker**

```bash
docker build -t name_converter_bot .

3. **Запустите Docker**

```bash
docker run -e TOKEN='вставте_ваш_ТОКЕН_сюда' -v "$(pwd):/app" name_converter_bot

3. **Проверка Docker на работоспособность**

3.1 ***Проверка если Doker установлен***
```bash
sudo docker images

3.2 ***Запустите контейнер в фоновом режиме***
```bash
sudo docker run -d -p 80:80 name_converter_bot

3.3 ***Проверяем работает ли контейнер***
```bash
sudo docker ps -a

- Если всё прошло успешно, то ваш бот работает в контейнере!


