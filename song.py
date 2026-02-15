class Song:
    """
    Clase que representa una canción.
    """
    def __init__(self, title: str, artist: str, duration: float, genre: str):
        if duration <= 0:
            raise ValueError("La duración debe ser positiva.")
        self.title = title
        self.artist = artist
        self.duration = duration  # en minutos
        self.genre = genre

    def __str__(self):
        return f"{self.title} - {self.artist} | {self.genre} | {self.duration:.2f} min"