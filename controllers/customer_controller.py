from flask import Blueprint, request, jsonify
from models.customer_model import get_all_customers, get_customer_by_id
customer_bp = Blueprint('customer', __name__)

#  Route to get all customers
@customer_bp.route('/get_customers', methods=['GET'])
def get_customers_route():
    response = get_all_customers()
    if "error" in response:
        return jsonify({"error": response["error"]}), 500
    return jsonify({"customers": response})
@customer_bp.route('/get_customer/<int:customer_id>', methods=['GET'])
def get_customer_route(customer_id):
    response = get_customer_by_id(customer_id)
    if not response:
        return jsonify({"error": "Customer not found"}), 404
    return jsonify(response)
