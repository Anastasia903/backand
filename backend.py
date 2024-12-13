from flask import Flask, request

app = Flask(__name__)


@app.route('/save', methods=['POST'])
def save_data():
    data = request.json.get('data')
    with open('data.txt', 'w') as file:
        file.write(data + '\n')

    return "Данные сохранены в файл."


if __name__ == '__main__':
    app.run(port=5001, debug=True)
