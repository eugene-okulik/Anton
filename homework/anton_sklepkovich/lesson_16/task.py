import mysql.connector as mysql
import dotenv
import csv
import os


dotenv.load_dotenv()
db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)
cursor = db.cursor(dictionary=True)

query_select = '''
    SELECT s.name, s.second_name, g.title as group_title, b.title as book_title, m.value as mark_value,
    l.title as lesson_title, su.title  as subject_title
    FROM students s
    JOIN `groups` g ON s.group_id = g.id
    JOIN books b ON s.id = b.taken_by_student_id
    JOIN marks m ON s.id = m.student_id
    JOIN lessons l ON m.lesson_id = l.id
    JOIN subjets su ON l.subject_id = su.id
    WHERE s.name = %s AND s.second_name = %s AND g.title = %s AND b.title = %s
    AND m.value  = %s AND l.title = %s AND su.title = %s
    '''
query_select_empty = {
    'group_title': '''SELECT g.title as group_title
                    FROM students s
                    JOIN `groups` g ON s.group_id = g.id
                    WHERE s.name = %s AND s.second_name = %s AND g.title = %s ''',
    'book_title': '''SELECT s.name, s.second_name, b.title as book_title
                    FROM students s
                    JOIN books b ON s.id = b.taken_by_student_id
                    WHERE s.name = %s AND s.second_name = %s AND b.title = %s ''',
    'mark_value': '''SELECT s.name, s.second_name, m.value as mark_value
                    FROM students s
                    JOIN marks m ON s.id = m.student_id
                    WHERE s.name = %s AND s.second_name = %s AND m.value = %s ''',
    'lesson_title': '''SELECT s.name, s.second_name, l.title as lesson_title
                    FROM students s
                    JOIN marks m ON s.id = m.student_id
                    JOIN lessons l ON m.lesson_id = l.id
                    WHERE s.name = %s AND s.second_name = %s AND l.title = %s ''',
    'subject_title': '''SELECT s.name, s.second_name, su.title  as subject_title
                    FROM students s
                    JOIN marks m ON s.id = m.student_id
                    JOIN lessons l ON m.lesson_id = l.id
                    JOIN subjets su ON l.subject_id = su.id
                    WHERE s.name = %s AND s.second_name = %s AND su.title = %s '''
}
query_select_student = 'SELECT * FROM students WHERE name = %s AND second_name = %s '

base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(base_path, 'eugene_okulik', 'lesson_16', 'hw_data', 'data.csv')

with open(file_path, newline='') as file_data:
    file_data = csv.DictReader(file_data)
    for row in file_data:
        cursor.execute(query_select_student, (row['name'], row['second_name']))
        if not cursor.fetchall():
            print(f"Студент {row['name']} {row['second_name']} не был найден")
            print(f'Полная строка со студентом из файла: {row}')
        else:
            cursor.execute(query_select, (
                row['name'],
                row['second_name'],
                row['group_title'],
                row['book_title'],
                row['mark_value'],
                row['lesson_title'],
                row['subject_title']
            ))
            if not cursor.fetchall():
                missing = {}
                print(f'Не хватает данных в бд из строки: {row}')
                for key, value in query_select_empty.items():
                    cursor.execute(value, (row['name'], row['second_name'], row[key]))
                    if not cursor.fetchall():
                        missing[key] = row[key]
                if missing:
                    print(f'А именно: {missing}')

db.close()
