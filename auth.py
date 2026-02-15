from user import User, load_user, save_user

def login():
    """
    Solicita credenciales y autentica al usuario.
    :return: Instancia de User autenticado o None.
    """
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    user = load_user(username)
    if user and user.verify_password(password):
        print(f"Bienvenido, {username}!")
        return user
    else:
        print("Usuario o contraseña incorrectos. Inténtelo de nuevo.")
        return None

def register():
    """
    Registra un nuevo usuario.
    """
    username = input("Nuevo nombre de usuario: ")
    password = input("Nueva contraseña: ")
    is_premium = input("¿Desea cuenta premium? (s/n): ").lower() == "s"
    user = User(username, password, is_premium)
    save_user(user)
    print("Usuario registrado correctamente.")

def upgrade_to_premium(user):
    """
    Cambia la cuenta del usuario a premium si no lo es.
    :param user: Instancia de User.
    """
    if user.is_premium:
        print("Ya eres usuario premium.")
    else:
        user.is_premium = True
        save_user(user)
        print("¡Ahora eres usuario premium!")