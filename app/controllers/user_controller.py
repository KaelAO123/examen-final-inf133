from werkzeug.security import check_password_hash
from flask import Blueprint,request,jsonify
from app.models.user_model import User
from flask_jwt_extended import create_access_token

user_bp = Blueprint("user", __name__)

@user_bp.route("/register",methods=["POST"])
def registrar_usuario():
    data = request.json
    name = data.get("name")
    password = data.get("password")
    phone = data.get("phone")
    email = data.get("email")
    role = data.get("role")
    if not name or not password or not phone or not email:
        return jsonify({"error":"Datos faltantes"}),400
    
    existe_usuario = User.find_user(email)
    if existe_usuario:
        return jsonify({"error":"El usuario existe"}),400
    
    new_usuario = User(name,email,password,phone,role)
    new_usuario.save()

    return jsonify({"message":"Usuario creado"})

@user_bp.route("/login",methods=["POST"])
def login_usuario():
    data = request.json
    username = data.get("name")
    email = data.get("email")
    password = data.get("password")
    user = User.find_user(email)
    if user and check_password_hash(user.email,password):
        access_token = create_access_token(
            identity={"username":username,"role":user.role},
        )
        return jsonify(access_token=access_token),200
    return jsonify({"error":"Crendeciales invalidas"}),401

