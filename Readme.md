# Процесс установки
## Создаем папку 
```bash
mkdir testQA
# и сразу в нее переходим
сd testQA
```
## Скачиваем 
```bash
git clone https://github.com/Tokarev-Alexey/QA.git
# заходим в папку проекта
cd QA
```
## Запуск
```bash
docker compose up -d
# или если у вас старая версия docker-compose
docker-compose up -d
```
## Получить все вопросы
````bash
curl -X GET http://localhost:8000/questions/
````

# Основание
- авторизации нет
- база данных пустая
- обработку исключений оставил стандартную от DRF

## Создать новый вопрос
````bash
curl -X POST http://localhost:8000/questions/ \
  -H "Content-Type: application/json" \
  -d '{"text": "Какой твой любимый язык программирования?"}'
````

## Получить вопрос по ID (с ответами)
```bash
curl -X GET http://localhost:8000/questions/1/
```

## Удалить вопрос
```bash
curl -X DELETE http://localhost:8000/questions/1/
```
## Создать ответ к вопросу
```bash
curl -X POST http://localhost:8000/questions/1/answers/ \
  -H "Content-Type: application/json" \
  -d '{"text": "Python - лучший язык!"}'
```

## Получить ответ по ID
```bash
curl -X GET http://localhost:8000/answers/1/
```

## Удалить ответ
```bash
curl -X DELETE http://localhost:8000/answers/1/
```

# Корневой endpoint не настроен!!!
- выдает два основных url относительно ModelViewSet
- POST /questions/{id}/answers/ — добавить ответ к вопросу вышел кастомным, я его не добавлял в API View
