import json
import os

DATA_FOLDER = "data"
PLAYLISTS_FILE = os.path.join(DATA_FOLDER, "playlists.json")

def save_playlist(username, playlist):
    """
    Guarda la playlist de un usuario en un archivo JSON.
    :param username: Nombre de usuario.
    :param playlist: Instancia de una lista enlazada personalizada.
    """
    playlists = load_all_playlists()
    # Serializa la playlist a una lista de diccionarios
    items = []
    temp = playlist.head
    if temp:
        visited = set()
        while temp and id(temp) not in visited:
            items.append({
                "title": temp.data.title,
                "artist": temp.data.artist,
                "duration": temp.data.duration,
                "genre": temp.data.genre
            })
            visited.add(id(temp))
            temp = temp.next
            if hasattr(playlist, "is_circular") and temp == playlist.head:
                break
    playlists[username] = items
    with open(PLAYLISTS_FILE, "w", encoding="utf-8") as f:
        json.dump(playlists, f, indent=4)

def load_all_playlists():
    """
    Carga todas las playlists desde el archivo JSON.
    :return: Diccionario de playlists.
    """
    if not os.path.exists(PLAYLISTS_FILE):
        return {}
    with open(PLAYLISTS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except Exception:
            return {}

def load_playlist(username):
    """
    Carga la playlist de un usuario específico.
    :param username: Nombre de usuario.
    :return: Lista de diccionarios de canciones.
    """
    playlists = load_all_playlists()
    return playlists.get(username, [])

def add_song_to_playlist(playlist, song):
    """
    Añade una canción a la playlist.
    :param playlist: Instancia de una lista enlazada personalizada.
    :param song: Instancia de Song.
    """
    playlist.addItem(song)

def delete_current_song(playlist):
    """
    Elimina la canción actual de la playlist.
    :param playlist: Instancia de una lista enlazada personalizada.
    """
    playlist.deleteCurrentItem()

def show_playlist(playlist):
    """
    Muestra todas las canciones de la playlist.
    :param playlist: Instancia de una lista enlazada personalizada.
    """
    playlist.showAll()

def next_song(playlist):
    """
    Avanza al siguiente elemento de la playlist.
    :param playlist: Instancia de una lista enlazada personalizada.
    """
    playlist.nextItem()
    return playlist.getCurrentItem()

def previous_song(playlist):
    """
    Retrocede al elemento anterior de la playlist (si la estructura lo permite).
    :param playlist: Instancia de una lista enlazada personalizada.
    """
    playlist.previousItem()
    return playlist.getCurrentItem()