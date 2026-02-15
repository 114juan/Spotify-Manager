import json
import hashlib
import os

DATA_FOLDER = "data"
USERS_FILE = os.path.join(DATA_FOLDER, "users.json")

class User:
    """
    Clase que representa un usuario del sistema.
    """
    def __init__(self, username: str, password: str, is_premium: bool = False):
        """
        Inicializa un usuario con nombre, contraseña (hasheada) y tipo de cuenta.

        :param username: Nombre de usuario.
        :param password: Contraseña en texto plano (será hasheada).
        :param is_premium: Indica si el usuario es premium.
        """
        self.username = username
        self.password_hash = self.hash_password(password)
        self.is_premium = is_premium

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hashea la contraseña usando SHA-256.

        :param password: Contraseña en texto plano.
        :return: Contraseña hasheada.
        """
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def verify_password(self, password: str) -> bool:
        """
        Verifica si la contraseña proporcionada coincide con la almacenada.

        :param password: Contraseña en texto plano.
        :return: True si coincide, False en caso contrario.
        """
        return self.password_hash == self.hash_password(password)

    def to_dict(self) -> dict:
        """
        Convierte el usuario a un diccionario para guardar en JSON.

        :return: Diccionario con los datos del usuario.
        """
        return {
            "username": self.username,
            "password_hash": self.password_hash,
            "is_premium": self.is_premium
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Crea una instancia de User a partir de un diccionario.

        :param data: Diccionario con los datos del usuario.
        :return: Instancia de User.
        """
        user = User(data["username"], "", data.get("is_premium", False))
        user.password_hash = data["password_hash"]
        return user

def save_user(user: User):
    """
    Guarda un usuario en el archivo users.json.

    :param user: Instancia de User a guardar.
    """
    users = load_all_users()
    users[user.username] = user.to_dict()
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

def load_all_users() -> dict:
    """
    Carga todos los usuarios desde el archivo users.json.

    :return: Diccionario de usuarios.
    """
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def load_user(username: str) -> User or None:
    """
    Carga un usuario específico por su nombre.

    :param username: Nombre de usuario.
    :return: Instancia de User o None si no existe.
    """
    users = load_all_users()
    data = users.get(username)
    if data:
        return User.from_dict(data)
    return None