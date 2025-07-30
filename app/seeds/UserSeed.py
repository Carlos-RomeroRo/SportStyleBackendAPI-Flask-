from app.config import db
from app.models.User import User, UserRole


def seed_users():
    if not User.query.first():
        users = [
                User(name="Carlos Romero", email="carlos@example.com", password="123456", role=UserRole.USER),
                User(name="María García", email="maria@example.com", password="abcdef", role=UserRole.ADMIN),
                User(name="Luis Torres", email="luis@example.com", password="pass1234", role=UserRole.USER),
                User(name="Andrea Méndez", email="andrea@example.com", password="andrea99", role=UserRole.USER),
                User(name="Pedro Díaz", email="pedro@example.com", password="pedro321", role=UserRole.SUPERADMIN)
        ]
        db.session.add_all(users)
        db.session.commit()
        print("Se han insertado los usuarios del SEED en la base de datos.")
    else:
        print("La tabla de usuarios ya tiene registros, No se intertaron datos del SEED.")