from flask import Flask, request
import os

app = Flask(__name__)

# Указываем абсолютный путь к файлу data.txt
FILE_PATH = 'D:/Учеба/DO/lab/backend/data.txt'  # Замените на ваш абсолютный путь

@app.route('/save', methods=['POST'])
def save_data():
    data = request.json.get('data')
    if not data:
        return "Ошибка: данные не предоставлены.", 400

    # Сохраняем данные в файл
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        file.write(data + '\n')

    return "Данные сохранены в файл."


@app.route('/create_file', methods=['GET'])
def create_file():
    # Создаем файл, если он не существует
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            file.write('')
        return "Файл data.txt создан."
    else:
        return "Файл data.txt уже существует."


if __name__ == '__main__':
    print(f"Сервер запущен. Файл будет создан в: {FILE_PATH}")
    app.run(port=5001, debug=True)