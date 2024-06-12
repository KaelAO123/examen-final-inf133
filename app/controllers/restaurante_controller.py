from app.models.restaurante_model import Restaurante
from flask import request,Blueprint,jsonify
from app.views.restaurante_view import render_detail_restaurante,render_restaurantes
from app.utils.decorator import jwt_required,role_required
restaurante_bp = Blueprint("restaurante", __name__)

@restaurante_bp.route("/restaurants",methods=["GET"])
@jwt_required
@role_required(roles=["admin","customer"])
def get_restaurantes():
    restaurantes = Restaurante.get_all_restaurantes()
    return jsonify(render_restaurantes(restaurantes))

@restaurante_bp.route("/restaurants/<int:id>",methods=["GET"])
@jwt_required
@role_required(roles=["admin","customer"])
def get_restaurante(id):
    restaurante = Restaurante.get_id_restaurante(id)
    return jsonify(render_detail_restaurante(restaurante))

@restaurante_bp.route("/restaurants",methods=["POST"])
@jwt_required
@role_required(roles=["admin"])
def post_restaurante():
    data = request.json
    name = data["name"]
    address = data["address"]
    city = data["city"]
    phone = data["phone"]
    description = data["description"]
    rating = data["rating"]

    if not name or not address or not city or not phone or not description or rating is None:
        return jsonify({"error":"datos faltantes"}),401
    
    restaurante = Restaurante(name,address,city,phone,description,rating)
    restaurante.save()
    return jsonify(render_detail_restaurante(restaurante))

@restaurante_bp.route("/restaurants/<int:id>",methods=["PUT"])
@jwt_required
@role_required(roles=["admin"])
def put_restaurante(id):
    restaurante = Restaurante.get_id_restaurante(id)
    if not restaurante:
        return jsonify({"error":"restaurante no encontrado"})
    data = request.json
    name = data["name"]
    address = data["address"]
    city = data["city"]
    phone = data["phone"]
    description = data["description"]
    rating = data["rating"]

    restaurante.update(name,address,city,phone,description,rating)
    return jsonify(render_detail_restaurante(restaurante))

@restaurante_bp.route("/restaurants/<int:id>",methods=["DELETE"])
@jwt_required
@role_required(roles=["admin"])
def delete_restaurante(id):
    restaurante = Restaurante.get_id_restaurante(id)
    if not restaurante:
        return jsonify({"error":"restaurante no encontrado"})
    
    restaurante.delete()
    return "",403