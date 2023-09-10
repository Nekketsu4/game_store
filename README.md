<h1>Интернет-магазин видеоигр (DRF + Vue JS)</h1>  

<h2>Содержание</h2>  


- [Описание](#описание)
- [Зависимости](#зависимости)
- [Установка](#установка)
  - [Инструкция](#инструкция)
    - [*Серверная часть*](#серверная-часть)
    - [*Клиентская часть*](#клиентская-часть)



## Описание

Проект готов для развертывания на удаленном сервере. В настоящий момент находится в разработке и поэтому на стороне клиента готова лишь главная страница сайта с перечнем предоставляемого продукта клиентам. 

Серверной частью проекта является Django + DRF с уже настроенным SimpleJWT, административной панелью, пагинацией страниц. Так же есть раздел отзывов с возможностью комментировать чужой отзыв

Клиентская часть скомпелирована с помощью Vue CLI. Готова в данный момент только главная страница, с возможностью подгружать новые данные предоставляемого продукта сайтом с помощью скроллинга. Но в дальнейшем добавлю страницу с информацией о каждом продукте, отзывы, авторизацию, платежную систему, а так же адаптацию под разные разрешения экрана.

## Зависимости

- [Python](https://www.python.org/downloads/)
- [Node.js](https://nodejs.org/en)

## Установка

Выполните гит клон на свою локальную/виртуальную машину https://github.com/Nekketsu4/game_store.git


### Инструкция
#### *Серверная часть*
```bash
#Перейдите в директорию проекта
cd game_store

#создайте виртуальное окружение
virtualvenv venv

#сделайте вирт. окружение активным
source venv/bin/activate

#установите зависимости 
pip install -r req.txt

```
Подключите свою БД к проекту (вот тут выполнить подключение вашей БД ==> https://github.com/Nekketsu4/game_store/blob/main/store_project/loc_settings.py#L22)

```bash
#Выполните миграцию
python3 manage.py migrate

#Запустите сервер
python3 manage.py runserver
```

#### *Клиентская часть*

```bash
#Перейдите в директорию фронтенда
cd game_store/games_store

#Установите менеджер пакетов npm
install npm

#Запустите сервер клиентской части(порт `http://localhost:8081`)
npm run serve

#Убедитесь в том что порт  Бэкенда запущен (порт `http://localhost:8000`)

