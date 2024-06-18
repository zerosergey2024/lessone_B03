#- Создайте таблицу `person` с пятью столбцами:
#- `id` — идентификатор человека, целое число, первичный ключ.
#- `first_name` — имя человека, строка.
#- `last_name` — фамилия человека, строка.
#- `age` — возраст человека, целое число.
#- `email` — электронная почта человека, строка.

CREATE TABLE person (
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    age INTEGER,
    email VARCHAR(50)
)