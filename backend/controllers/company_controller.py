from flask import Blueprint, jsonify, request, abort
from services import company_service

company_bp = Blueprint('company', __name__)

@company_bp.route('/companies', methods=['GET'])
def get_companies():
    companies = company_service.get_all_companies()
    return jsonify(companies)

@company_bp.route('/companies/<int:company_id>', methods=['GET'])
def get_company(company_id):
    company = company_service.get_company(company_id)
    if company is None:
        abort(404)
    return jsonify(company)

@company_bp.route('/companies', methods=['POST'])
def create_company():
    company_data = request.json
    new_company = company_service.create_company(company_data)
    return jsonify(new_company), 201

@company_bp.route('/companies/<int:company_id>', methods=['PUT'])
def update_company(company_id):
    company_data = request.json
    updated_company = company_service.update_company(company_id, company_data)
    if updated_company is None:
        abort(404)
    return jsonify(updated_company)

@company_bp.route('/companies/<int:company_id>', methods=['DELETE'])
def delete_company(company_id):
    success = company_service.delete_company(company_id)
    if not success:
        abort(404)
    return '', 204