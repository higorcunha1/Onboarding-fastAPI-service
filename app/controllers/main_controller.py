from flask import Blueprint, request
from app.views.responses import hello_world_response, echo_response

main_bp = Blueprint('main', __name__)

@main_bp.route('/hello', methods=['GET'])
def hello_world():
    # Passa pela "controller" e chama a "view" para retornar a resposta
    return hello_world_response()

@main_bp.route('/echo', methods=['POST'])
def echo():
    # Obtém o valor enviado na requisição
    data = request.json.get('value', '')
    # Passa pela "controller" e chama a "view" para retornar a resposta
    return echo_response(data)
