from flask import Flask, jsonify

app = Flask(__name__)
counter = 0  # Ініціалізація лічильника

@app.route('/')
def home():
    # Перенаправлення на '/count-requests' або повідомлення для кореневого URL
    return redirect(url_for('count_requests'))

@app.route('/count-requests', methods=['GET'])
def count_requests():
    global counter  # Використання глобальної змінної counter
    counter += 1    # Збільшення лічильника при кожному запиті
    return jsonify(count=counter)  # Повернення лічильника у форматі JSON

if __name__ == '__main__':
    app.run(debug=True)