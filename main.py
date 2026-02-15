from playlist_manager import PlaylistManager

def main():
    manager = PlaylistManager()
    while True:
        print("\n--- Bienvenido a Spotify Console ---")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        option = input("Seleccione una opción: ")
        if option == "1":
            manager.login()
            if manager.user:
                manager.select_playlist_structure()
                if manager.playlist:
                    manager.menu()
        elif option == "2":
            manager.register()
        elif option == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()