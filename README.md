# <img src="https://www.django-rest-framework.org/img/logo.png" width="400"/> 

## ТЗ Телеграм бот IMEI

#### Разработана бэкенд-систему для проверки IMEI устройств, которая будет интегрирована с Telegram-ботом и предоставлять API для внешних запросов.
***
#### Реализованы задачи:
  * Реализован телеграм бот с белым списком.
  * REST API для внешнего сервера, с токеном.
  * Интеграция с API В imeicheck.net 
  
***
### Прежде чем начать использовать проект нужно:
* Создать бота через [BotFather](https://t.me/BotFather)
* Создать файл `.evn` для передачи личных данных в Django настройки.
***

    DEBUG=<BOOL>
    SECRET_KEY=<SECRET_KEY>
    TOKEN_BOT=<TOKEN_BOT>
    LOG_LEVEL=INFO
    WHITE_LIST=<ID_TG>,<ID_TG>
    TOKEN_IMEICHECK=<TOKEN_IMEICHECK>


### Разворачивание ТЗ Телеграм бот IMEI


    git clone https://github.com/4byra6ka/TZ_HatikoTech.git
    cd TZ_HatikoTech
    nano .env
    poetry install
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver <IP>:<PORT>
    python manage.py run_bot
