from flask import Blueprint, request, Response
import json

# Créer un blueprint
bp = Blueprint('routes', __name__)

# Charger les données du fichier JSON
def load_searches():
    with open('app/searches.json') as f:
        return json.load(f)

# Route pour récupérer toutes les données
@bp.route('/searches/all', methods=['GET'])
def get_all_searches():
    searches = load_searches()
    # Utiliser json.dumps pour contrôler l'ordre des clés
    return Response(json.dumps(searches, ensure_ascii=False, indent=2), mimetype='application/json')

# Route pour récupérer les données paginées
@bp.route('/searches', methods=['GET'])
def get_paginated_searches():
    searches = load_searches()
    # Parse les paramètres de query
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 30))

    # Implémentation simple de la pagination
    start = (page - 1) * limit
    end = start + limit
    paginated = searches[start:end]

    # Utiliser json.dumps pour garantir l'ordre des clés dans la réponse
    response_data = {
        'page': page,
        'limit': limit,
        'total': len(searches),
        'data': paginated
    }

    return Response(json.dumps(response_data, ensure_ascii=False, indent=2), mimetype='application/json')

# Route pour création (non implémentée)
@bp.route('/searches', methods=['POST'])
def create_search():
    return Response(json.dumps({'error': 'Method not implemented'}, ensure_ascii=False, indent=2),
                    status=501, mimetype='application/json')

# Route pour modification (non implémentée)
@bp.route('/searches/<int:id>', methods=['PUT'])
def update_search(id):
    return Response(json.dumps({'error': 'Method not implemented'}, ensure_ascii=False, indent=2),
                    status=501, mimetype='application/json')

# Route pour suppression (non implémentée)
@bp.route('/searches/<int:id>', methods=['DELETE'])
def delete_search(id):
    return Response(json.dumps({'error': 'Method not implemented'}, ensure_ascii=False, indent=2),
                    status=501, mimetype='application/json')