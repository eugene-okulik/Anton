import mysql.connector as mysql
import random
import string
import os
import dotenv


INSERT_QUERY_STUDENT = "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, NULL)"
INSERT_QUERY_BOOK = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
INSERT_QUERY_GROUP = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
INSERT_QUERY_SUBJECT = "INSERT INTO subjets (title) VALUES (%s)"
INSERT_QUERY_LESSON = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
INSERT_QWERY_MARK = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"

dotenv.load_dotenv()
db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)
cursor = db.cursor(dictionary=True)


def random_data(key):
    match key:
        case 'name':
            return ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(2, 4)))
        case 'second_name':
            return ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 7)))
        case 'subject' | 'book' | 'lesson':
            return f'{key}{random.randint(1, 10000)}'
        case 'group':
            return f'group{random.randint(1, 10000)}', 'jan 2023', 'jan 2024'
        case 'mark':
            return str(random.randint(1, 5))


def create_data(insert, value):
    cursor.execute(insert, value)
    id_in_bd = cursor.lastrowid
    return id_in_bd


def update_data(table, rows, value):
    query = f'UPDATE {table} SET {rows[0]} = %s WHERE {rows[1]} = %s'
    cursor.execute(query, (value[0], value[1]))


def create_lesson(item):
    id_new_lesson = create_data(INSERT_QUERY_LESSON, (random_data('lesson'), item))
    print(select_new_element('lessons', 'id', id_new_lesson))
    return id_new_lesson


def create_mark(item, id_student):
    id_new_mark = create_data(INSERT_QWERY_MARK, (random_data('mark'), item, id_student))
    print(select_new_element('marks', 'id', id_new_mark))
    return id_new_mark


def select_new_element(table, rows, value, select='*'):
    query = f'SELECT {select} FROM {table} WHERE {rows} = %s'
    cursor.execute(query, (value,))
    return cursor.fetchall()


# Создайте студента (student)
value_students = (random_data('name'), random_data('second_name'))
id_new_student = create_data(INSERT_QUERY_STUDENT, value_students)
print(select_new_element('students', 'id', id_new_student))

# Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
value_book = (random_data('book'), id_new_student)
value_book1 = (random_data('book'), id_new_student)
id_new_book = create_data(INSERT_QUERY_BOOK, value_book)
id_new_book1 = create_data(INSERT_QUERY_BOOK, value_book1)
print(select_new_element('books', 'id', id_new_book))
print(select_new_element('books', 'id', id_new_book1))

# print(id_new_book)

# Создайте группу (group) и определите своего студента туда
value_group = random_data('group')
id_new_grop = create_data(INSERT_QUERY_GROUP, value_group)
update_data('students', ('group_id', 'id'), (id_new_grop, id_new_student))
print(select_new_element('`groups`', 'id', id_new_grop))


# Создайте несколько учебных предметов (subjects)
value_subject = (random_data('subject'),)
value_subject1 = (random_data('subject'),)
id_new_subject = create_data(INSERT_QUERY_SUBJECT, value_subject)
id_new_subject1 = create_data(INSERT_QUERY_SUBJECT, value_subject1)
print(select_new_element('subjets', 'id', id_new_subject))
print(select_new_element('subjets', 'id', id_new_subject1))

# Создайте по два занятия для каждого предмета (lessons)
list_subjects = [id_new_subject, id_new_subject1] * 2
list_new_lessons = list(map(lambda item: create_lesson(item), list_subjects))
print(list_new_lessons)

# Поставьте своему студенту оценки (marks) для всех созданных вами занятий
list_marks = list(map(lambda item: create_mark(item, id_new_student), list_new_lessons))
print(list_marks)

# Все оценки студента
print(select_new_element('marks', 'student_id', id_new_student, 'value AS students_mark'))

# Все книги, которые находятся у студента
print(select_new_element('books', 'taken_by_student_id', id_new_student, 'title AS name_book'))

# Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
# (всё одним запросом с использованием Join)
print(select_new_element(
    '''students s
            JOIN `groups` g ON s.group_id = g.id
            JOIN books b ON s.id = b.taken_by_student_id
            JOIN marks m ON s.id = m.student_id
            JOIN lessons l ON m.lesson_id = l.id
            JOIN subjets s2 ON l.subject_id = s2.id''',
    's.id', id_new_student,
    '''s.name,
            s.second_name,
            g.title AS name_group,
            b.title AS name_book,
            m.value AS  grade,
            l.title AS name_lesson,
            s2.title AS name_subjects'''))

db.commit()
db.close()
