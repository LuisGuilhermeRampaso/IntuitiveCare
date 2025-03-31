from flask import Blueprint, request, jsonify
import math
from .services.buscar import buscar_operadoras

operadoras_bp = Blueprint('operadoras', __name__)

def sanitize_data(data):
    """Substitui valores NaN por None"""
    if isinstance(data, dict):
        return {k: sanitize_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [sanitize_data(item) for item in data]
    elif isinstance(data, float) and math.isnan(data):
        return None
    return data

@operadoras_bp.route('/buscar', methods=['GET'])
def buscar():
    termo = request.args.get('q', '').strip().lower()

    if not termo:
        return jsonify({"erro": "Nenhum termo de busca fornecido"}), 400

    resultados = buscar_operadoras(termo)
    
    # Sanitiza os resultados antes de converter para JSON
    resultados_sanitizados = sanitize_data(resultados)
    
    return jsonify(resultados_sanitizados)