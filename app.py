from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

respuestas = {
    "hola": "¡Hola! ¿Cómo puedo ayudarte hoy?",
    "adiós": "¡Hasta luego! Que tengas un buen día.",
    "¿cómo estás?": "Estoy muy bien, ¡gracias por preguntar!",
    "¿qué puedes hacer?": "Por ahora solo respondo preguntas básicas. 😊",
}

# Ruta para mostrar el HTML en el navegador
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')  # Busca en /templates/index.html

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').lower()
    respuesta = respuestas.get(user_message, "Lo siento, no entiendo tu pregunta.")
    return jsonify({"reply": respuesta})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
