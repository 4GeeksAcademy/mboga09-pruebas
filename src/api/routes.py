"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, Course
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/addCourse', methods=["POST"])
def add_course():
    body = request.get_json()
    course = body["course"]
    code = body["code"]
    category = body["cadegory"]
    provider = body["provider"]
    cost = body["cost"]
    description = body["description"]
    modality = body["modality"]
    start_date = body["start_date"]
    finish_date = body["finish_date"]
    contents = body["finish_date"]
    is_active = True
    if body is None:
        raise APIException("Body está vacío", status_code=400)
    if course is None or course=="":
        raise APIException("Llene todos los espacios", status_code=400)
    if code is None or code=="":
        raise APIException("El nombre es necesario", status_code=400)
    if category is None or category=="":
        raise APIException("Los apellidos son necesarios", status_code=400)
    if provider is None or provider=="":
        raise APIException("Los apellidos son necesarios", status_code=400)
    if cost is None or cost=="":
        raise APIException("Los apellidos son necesarios", status_code=400)
    if description is None or description=="":
        raise APIException("Los apellidos son necesarios", status_code=400)
    if modality is None or modality=="":
        raise APIException("Los apellidos son necesarios", status_code=400)
    if start_date is None or start_date=="":
        raise APIException("Los apellidos son necesarios", status_code=400)
    if finish_date is None or finish_date=="":
        raise APIException("Los apellidos son necesarios", status_code=400)
    if contents is None or contents=="":
        raise APIException("Los apellidos son necesarios", status_code=400)
    course = Course.query.filter_by(code=code).first()
    #se verifica si el curso ya existe en BD
    if course:
        raise APIException("El curso ya existe", status_code=400)
    #debería encriptar el password
    #print("password sin encriptar:", password)
    #password = current_app.bcrypt.generate_password_hash(password, 10).decode("utf-8")
    #print("password con encriptación:", password)
    new_course = Course(course=course,
                        code=code,
                        category=category,
                        provider=provider,
                        cost=cost,
                        description=description,
                        modality=modality,
                        start_date=start_date,
                        finish_date=finish_date,
                        contents=contents)
    try:
        db.session.add(new_course)
        db.session.commit()
        return jsonify({"message":"curso añadido"}), 201
    except Exception as error:
        print(str(error))
        return jsonify({"message":"error al añadir el curso en BD"}), 500

