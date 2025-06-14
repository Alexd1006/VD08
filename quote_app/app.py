from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = 'ВАШ_API_КЛЮЧ'  # 🔑 Вставьте сюда ваш ключ

@app.route('/')
def quote():
    url = 'https://api.api-ninjas.com/v1/quotes'
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        quote_data = response.json()[0]  # Получаем первую цитату из списка
    else:
        quote_data = {'quote': 'Не удалось получить цитату.', 'author': 'Ошибка'}

    return render_template('quote.html', quote=quote_data)


if __name__ == '__main__':
    app.run(debug=True)
