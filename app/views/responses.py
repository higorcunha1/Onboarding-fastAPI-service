from flask import jsonify

def hello_world_response():
    # Retorna um JSON com a mensagem "Hello, World!"
    return jsonify(message="Hello, World!")

def echo_response(value):
    # Retorna um JSON com o valor recebido
    return jsonify(message=f"Received: {value}")
