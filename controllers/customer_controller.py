from flask import Blueprint, request, jsonify
from models.customer_model import get_all_customers
customer_bp = Blueprint('customer', __name__)

#  Route to get all customers
@customer_bp.route('/get_customers', methods=['GET'])
def get_customers_route():
    response = get_all_customers()
    if "error" in response:
        return jsonify({"error": response["error"]}), 500
    return jsonify({"customers": response})