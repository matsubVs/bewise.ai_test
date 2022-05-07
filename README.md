# bewise.ai_test
Тестовое задания для компании bewise.ai
>## Деплой проекта
>1. git clone https://github.com/matsubVs/bewise.ai_test.git
>2. cd bewise.ai_test
>> Создать два файла app.env и db.env <br>
>> Заполнить по шаблону оба файла:
>> 1. POSTGRES_USER=your_user
>> 2. POSTGRES_DB=your_db
>> 3. POSTGRES_PASSWORD=safe_password
>> 4. POSTGRES_HOST=pg
>3. docker-compose build
>4. docker-compose up
>5. Перейти по адресу localhost:8001/

Для проверки: <br>
```curl -X POST -F 'question_num=10' localhost:8001/```<br>
Ответ вида: <br>
```[{"id":72574,"answer":"the cheeseburger","question":"Kaelin's Restaurant claims to have originated this all-American meat-\u0026-dairy item","value":200,"airdate":"2006-03-08T12:00:00.000Z","created_at":"2014-02-11T23:33:16.409Z","updated_at":"2014-02-11T23:33:16.409Z","category_id":9478,"game_id":null,"invalid_count":null,"category":{"id":9478,"title":"going down to louisville","created_at":"2014-02-11T23:33:16.336Z","updated_at":"2014-02-11T23:33:16.336Z","clues_count":5}}]```

GET запрос: <br>
```curl -X GET localhost:8001/```

