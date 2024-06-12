from app.models.reservas_model import Reserva
from flask import request,Blueprint,jsonify
from app.views.reservas_view import render_detail_reserva,render_reservas
from app.utils.decorator import jwt_required,role_required
reserva_bp = Blueprint("reserva", __name__)

@reserva_bp.route("/reservations",methods=["GET"])
@jwt_required
@role_required(["admin","customer"])
def get_restaurantes():
    restaurantes = Reserva.get_all_restaurantes()
    return jsonify(render_reservas(restaurantes))

@reserva_bp.route("/reservations/<int:id>",methods=["GET"])
@jwt_required
@role_required(["admin","customer"])
def get_restaurante(id):
    restaurante = Reserva.get_id_reservacion(id)
    return jsonify(render_detail_reserva(restaurante))

@reserva_bp.route("/reservations",methods=["POST"])
@jwt_required
@role_required(["admin"])
def post_restaurante():
    data = request.json
    user_id = data["user_id"]
    restaurant_id = data["restaurant_id"]
    reservation_date = data["reservation_date"]
    num_guests = data["num_guests"]
    special_requests = data["special_requests"]

    if not user_id or not restaurant_id or not reservation_date or not num_guests or not special_requests:
        return jsonify({"error":"datos faltantes"}),401
    
    restaurante = Reserva(user_id,restaurant_id,reservation_date,num_guests,special_requests)
    restaurante.save()
    return jsonify(render_detail_reserva(restaurante))

@reserva_bp.route("/reservations/<int:id>",methods=["PUT"])
@jwt_required
@role_required(["admin"])
def put_restaurante(id):
    restaurante = Reserva.get_id_reservacion(id)
    if not restaurante:
        return jsonify({"error":"restaurante no encontrado"})
    data = request.json
    user_id = data["user_id"]
    restaurant_id = data["restaurant_id"]
    reservation_date = data["reservation_date"]
    num_guests = data["num_guests"]
    special_requests = data["special_requests"]

    restaurante.update(user_id,restaurant_id,reservation_date,num_guests,special_requests)
    return jsonify(render_detail_reserva(restaurante))

@reserva_bp.route("/reservations/<int:id>",methods=["DELETE"])
@jwt_required
@role_required(["admin"])
def delete_restaurante(id):
    restaurante = Reserva.get_id_reservacion(id)
    if not restaurante:
        return jsonify({"error":"restaurante no encontrado"})
    
    restaurante.delete()
    return "",403