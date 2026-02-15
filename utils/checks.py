import shutil

def check_graphviz():
    if shutil.which("dot") is None:
        print("Graphviz no está instalado o 'dot' no está en el PATH. Por favor, instálalo desde https://graphviz.gitlab.io/download/")
        return False
    return True