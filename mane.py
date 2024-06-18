#- Создайте таблицу `person` с пятью столбцами:

CREATE TABLE "person" (
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    age INTEGER,
    email VARCHAR(50)
);
#Заполняем таблицу данными на 6 строк:

INSERT INTO "person" ("id", "first_name", "last_name", "age", "email")
VALUES    (1, 'Катя', 'Иварова', 30, '3@gmail.com'),
VALUES    (2, 'Коля', 'Сидоров', 25, '3@gmail.com'),
VALUES    (3, 'Кирил', 'Петров', 40, '3@gmail.com'),
VALUES    (4, 'Ксюша', 'Данилова', 35,'3@gmail.com'),
VALUES    (5, 'Костя', 'Васильев', 30,'3@gmail.com'),
VALUES    (6, 'Клава', 'Сергеева', 25,'3@gmail.com')

#Переименование таблицы `person` в `employee`

ALTER TABLE "person" RENAME  TO "employee";

#Удалите из таблицы `employee` столбец `email`:

ALTER TABLE "employee" DROP COLUMN "email";
