import os
import sys

try:
    import pygame
except ImportError:
    print("Instala el paquete 'pygame' para reproducir audio: pip install pygame")
    sys.exit(1)

AUDIO_FOLDER = "audio-files"

def play_audio(filename):
    """
    Reproduce un archivo de audio ubicado en la carpeta audio-files usando pygame.

    :param filename: Nombre del archivo de audio (ejemplo: 'cancion.mp3').
    """
    path = os.path.join(AUDIO_FOLDER, filename)
    if not os.path.exists(path):
        print(f"Archivo de audio no encontrado: {path}")
        return
    try:
        print(f"Reproduciendo: {filename}")
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        # Espera hasta que termine la reproducción
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    except Exception as e:
        print(f"Error al reproducir el audio: {e}")