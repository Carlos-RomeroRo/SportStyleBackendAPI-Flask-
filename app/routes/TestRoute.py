from flask import Blueprint

test_bp = Blueprint('test_bp', __name__)

@test_bp.route('/',methods=['GET'])
def test_route():
    return "El servidor está accediendo correctamente a las rutas. Prueba con los siguiente modelos (;"