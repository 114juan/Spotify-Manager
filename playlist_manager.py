import os
import random
from auth import login, register, upgrade_to_premium
from user import User, load_user, save_user
from linked_lists.simple_linked_list import SimpleLinkedList
from linked_lists.doubly_linked_list import DoublyLinkedList
from linked_lists.circular_linked_list import CircularLinkedList
from linked_lists.doubly_circular_linked_list import DoublyCircularLinkedList
from song import Song
from utils.audio_player import play_audio
from utils.storage import save_playlist, load_playlist
import pygame

DATA_FOLDER = "data"
AUDIO_FOLDER = os.path.join(DATA_FOLDER, "audio-files")

class PlaylistManager:
    """
    Clase principal que gestiona la interacción con el usuario y las playlists.
    Permite seleccionar la estructura de playlist, añadir, eliminar, mostrar, navegar,
    reproducir canciones, pausar/reanudar, guardar/cargar y crear playlists aleatorias para usuarios premium.
    """

    def __init__(self):
        """
        Inicializa el gestor de playlists.
        """
        self.user = None
        self.playlist = None
        self.paused = False
        self.pause_pos = 0  # posición en milisegundos

    def login(self):
        """
        Inicia sesión solicitando credenciales al usuario.
        """
        self.user = login()

    def register(self):
        """
        Registra un nuevo usuario.
        """
        register()

    def select_playlist_structure(self):
        """
        Permite al usuario seleccionar el tipo de estructura de playlist según sus permisos.
        """
        print("\nSeleccione el tipo de playlist:")
        print("1. Lista enlazada simple")
        if self.user.is_premium:
            print("2. Lista doblemente enlazada")
            print("3. Lista circular simple")
            print("4. Lista circular doble")
        choice = input("Opción: ")
        if choice == "1":
            self.playlist = SimpleLinkedList()
        elif choice == "2" and self.user.is_premium:
            self.playlist = DoublyLinkedList()
        elif choice == "3" and self.user.is_premium:
            self.playlist = CircularLinkedList()
        elif choice == "4" and self.user.is_premium:
            self.playlist = DoublyCircularLinkedList()
        else:
            print("Opción no válida o no permitida para su tipo de cuenta.")
            self.playlist = None

    def menu(self):
        """
        Muestra el menú principal de gestión de la playlist y ejecuta las acciones seleccionadas.
        """
        while True:
            print("\n--- Menú Playlist ---")
            print("1. Añadir nueva canción")
            print("2. Reproducir siguiente")
            print("3. Reproducir anterior")
            print("4. Eliminar canción actual")
            print("5. Mostrar playlist completa")
            print("6. Graficar playlist")
            print("7. Cambiar a cuenta premium")
            print("8. Cambiar estructura de playlist")
            print("9. Reproducir canción actual")
            print("10. Pausar")
            print("11. Guardar playlist")
            print("12. Cargar playlist")
            if self.user and self.user.is_premium:
                print("13. Crear playlist aleatoria (30 canciones)")
                print("14. Salir")
            else:
                print("13. Salir")
            option = input("Seleccione una opción: ")

            if option == "1":
                self.add_song()
            elif option == "2":
                self.next_item()
            elif option == "3":
                self.previous_item()
            elif option == "4":
                self.delete_current()
            elif option == "5":
                self.show_all()
            elif option == "6":
                self.grafic_playlist()
            elif option == "7":
                self.upgrade_to_premium()
            elif option == "8":
                self.select_playlist_structure()
            elif option == "9":
                self.play_current_audio()
            elif option == "10":
                self.pause_or_resume_audio()
            elif option == "11":
                self.save_user_playlist()
            elif option == "12":
                self.load_user_playlist()
            elif option == "13" and self.user and self.user.is_premium:
                self.create_random_playlist()
            elif (option == "13" and not (self.user and self.user.is_premium)) or (option == "14" and self.user and self.user.is_premium):
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida.")

    def add_song(self):
        """
        Permite seleccionar una canción de la carpeta audio-files y la añade a la playlist.
        El título y duración se detectan automáticamente, autor y género quedan como 'No encontrado'.
        Después de añadir, limpia la consola y libera los recursos usados.
        """
        files = [f for f in os.listdir(AUDIO_FOLDER) if f.lower().endswith(('.mp3', '.wav', '.ogg'))]
        if not files:
            print("No hay archivos de audio en la carpeta.")
            return
        print("\nCanciones disponibles en la carpeta:")
        for idx, file in enumerate(files, 1):
            print(f"{idx}. {file}")
        try:
            choice = int(input("Seleccione el número de la canción: "))
            if not (1 <= choice <= len(files)):
                print("Selección inválida.")
                return
        except ValueError:
            print("Entrada inválida.")
            return
        filename = files[choice - 1]
        title = os.path.splitext(filename)[0]
        # Obtener duración usando pygame
        try:
            pygame.mixer.init()
            audio_path = os.path.join(AUDIO_FOLDER, filename)
            sound = pygame.mixer.Sound(audio_path)
            duration = sound.get_length() / 60  # minutos
            del sound
            pygame.mixer.quit()
        except Exception as e:
            print(f"No se pudo obtener la duración: {e}")
            duration = 0.0
        song = Song(title, "No encontrado", duration, "No encontrado")
        self.playlist.addItem(song)
        print(f"Canción '{title}' añadida.")
        # Limpiar la consola
        os.system('cls' if os.name == 'nt' else 'clear')

    def next_item(self):
        """
        Avanza al siguiente elemento de la playlist y lo muestra.
        """
        self.playlist.nextItem()
        current = self.playlist.getCurrentItem()
        if current:
            print(f"Reproduciendo: {current}")
        else:
            print("No hay más canciones.")

    def previous_item(self):
        """
        Retrocede al elemento anterior de la playlist y lo muestra (si la estructura lo permite).
        """
        self.playlist.previousItem()
        current = self.playlist.getCurrentItem()
        if current:
            print(f"Reproduciendo: {current}")
        else:
            print("No hay canción anterior o la estructura no lo permite.")

    def delete_current(self):
        """
        Elimina el elemento actual de la playlist.
        """
        self.playlist.deleteCurrentItem()
        print("Elemento eliminado.")

    def show_all(self):
        """
        Muestra todas las canciones de la playlist.
        """
        print("\n--- Playlist ---")
        self.playlist.showAll()

    def grafic_playlist(self):
        """
        Genera una imagen PNG que representa gráficamente la playlist.
        """
        self.playlist.grafic()

    def upgrade_to_premium(self):
        """
        Cambia la cuenta del usuario a premium usando la función de auth.
        """
        upgrade_to_premium(self.user)

    def play_current_audio(self):
        """
        Reproduce el archivo de audio correspondiente a la canción actual de la playlist.
        Si está pausada, reanuda desde donde se pausó.
        """
        current = self.playlist.getCurrentItem()
        if current:
            filename = current.title + ".mp3"
            path_mp3 = os.path.join(AUDIO_FOLDER, filename)
            if not os.path.exists(path_mp3):
                for ext in ('.wav', '.ogg'):
                    alt_path = os.path.join(AUDIO_FOLDER, current.title + ext)
                    if os.path.exists(alt_path):
                        filename = current.title + ext
                        break
            try:
                pygame.mixer.init()
                audio_path = os.path.join(AUDIO_FOLDER, filename)
                pygame.mixer.music.load(audio_path)
                # Si estaba pausada, reanuda desde la posición guardada
                if self.paused and self.pause_pos > 0:
                    pygame.mixer.music.play(start=self.pause_pos / 1000)
                    print(f"Reanudando: {filename} desde {self.pause_pos / 1000:.2f} segundos")
                    self.paused = False
                    self.pause_pos = 0
                else:
                    pygame.mixer.music.play()
                    print(f"Reproduciendo: {filename}")
            except Exception as e:
                print(f"No se pudo reproducir el audio: {e}")
        else:
            print("No hay canción seleccionada para reproducir.")

    def pause_or_resume_audio(self):
        """
        Pausa o reanuda la reproducción de la canción actual usando pygame.
        Guarda la posición de pausa para reanudar desde ahí.
        """
        if pygame.mixer.get_init() and pygame.mixer.music.get_busy():
            if not self.paused:
                # Pausar y guardar la posición
                self.pause_pos = pygame.mixer.music.get_pos()  # en milisegundos
                pygame.mixer.music.pause()
                self.paused = True
                print(f"Canción pausada en el segundo {self.pause_pos / 1000:.2f}")
            else:
                # Reanudar desde la posición guardada
                pygame.mixer.music.unpause()
                print("Canción reanudada.")
                self.paused = False
        else:
            print("No hay canción en reproducción para pausar/reanudar.")

    def save_user_playlist(self):
        """
        Guarda la playlist actual del usuario en un archivo JSON.
        """
        if self.user and self.playlist:
            save_playlist(self.user.username, self.playlist)
            print("Playlist guardada correctamente.")

    def load_user_playlist(self):
        """
        Carga la playlist del usuario desde un archivo JSON si existe.
        """
        if self.user:
            songs = load_playlist(self.user.username)
            if songs and self.playlist:
                for song_data in songs:
                    song = Song(
                        song_data["title"],
                        song_data["artist"],
                        song_data["duration"],
                        song_data["genre"]
                    )
                    self.playlist.addItem(song)

    def create_random_playlist(self):
        """
        Permite a un usuario premium crear una playlist aleatoria de 30 canciones
        en la estructura que desee (simple, doble, circular simple o circular doble).
        """
        print("\nSeleccione el tipo de playlist aleatoria:")
        print("1. Lista enlazada simple")
        print("2. Lista doblemente enlazada")
        print("3. Lista circular simple")
        print("4. Lista circular doble")
        choice = input("Opción: ")
        if choice == "1":
            playlist = SimpleLinkedList()
        elif choice == "2":
            playlist = DoublyLinkedList()
        elif choice == "3":
            playlist = CircularLinkedList()
        elif choice == "4":
            playlist = DoublyCircularLinkedList()
        else:
            print("Opción no válida.")
            return

        files = [f for f in os.listdir(AUDIO_FOLDER) if f.lower().endswith(('.mp3', '.wav', '.ogg'))]
        if len(files) < 30:
            print("No hay suficientes canciones en la carpeta para crear una playlist aleatoria de 30 canciones.")
            return
        random_files = random.sample(files, 30)
        for filename in random_files:
            title = os.path.splitext(filename)[0]
            try:
                pygame.mixer.init()
                audio_path = os.path.join(AUDIO_FOLDER, filename)
                sound = pygame.mixer.Sound(audio_path)
                duration = sound.get_length() / 60  # minutos
                del sound
                pygame.mixer.quit()
            except Exception:
                duration = 0.0
            song = Song(title, "No encontrado", duration, "No encontrado")
            playlist.addItem(song)
        self.playlist = playlist
        print("¡Playlist aleatoria de 30 canciones creada!")

