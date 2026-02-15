from linked_lists.node import Node
from linked_lists.base_linked_list import BaseLinkedList
import os
from graphviz import Digraph
from utils.checks import check_graphviz

OUTPUT_FOLDER = "output"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

class DoublyCircularLinkedList(BaseLinkedList):
    """
    Implementación de una lista doblemente enlazada circular.
    Hereda de BaseLinkedList para reutilizar atributos y métodos comunes.
    """

    def __init__(self):
        """
        Inicializa la lista doblemente enlazada circular.
        """
        super().__init__()

    def addItem(self, item):
        """
        Añade un nuevo elemento al final de la lista circular doble.

        :param item: Objeto a agregar (por ejemplo, una instancia de Song).
        """
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
            self.current = self.head
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def deleteCurrentItem(self):
        """
        Elimina el elemento actual de la lista circular doble.
        Si el elemento actual es la cabeza, actualiza la cabeza.
        """
        if not self.head or not self.current:
            return
        if self.current == self.head and self.head.next == self.head:
            self.head = None
            self.current = None
            return
        prev = self.current.prev
        next_node = self.current.next
        prev.next = next_node
        next_node.prev = prev
        if self.current == self.head:
            self.head = next_node
        self.current = next_node

    def nextItem(self):
        """
        Avanza al siguiente elemento de la lista circular doble.
        """
        if self.current:
            self.current = self.current.next

    def previousItem(self):
        """
        Retrocede al elemento anterior de la lista circular doble.
        """
        if self.current:
            self.current = self.current.prev

    def showAll(self):
        """
        Muestra todos los elementos de la lista circular doble en consola.
        """
        if not self.head:
            return
        temp = self.head
        while True:
            print(temp.data)
            temp = temp.next
            if temp == self.head:
                break

    def grafic(self, filename="nombre_lista"):
        """
        Genera una imagen PNG que representa gráficamente la lista y la guarda en la carpeta output.

        :param filename: Nombre base del archivo PNG generado.
        """
        if not check_graphviz():
            return
        dot = Digraph(comment="Doubly Circular Linked List")
        temp = self.head
        idx = 0
        nodes = []
        if not self.head:
            return
        while True:
            node_name = f"node{idx}"
            label = str(temp.data.title) if hasattr(temp.data, "title") else str(temp.data)
            dot.node(node_name, label)
            nodes.append(node_name)
            temp = temp.next
            idx += 1
            if temp == self.head:
                break
        for i in range(len(nodes)):
            dot.edge(nodes[i], nodes[(i + 1) % len(nodes)], arrowhead='normal')
            dot.edge(nodes[(i + 1) % len(nodes)], nodes[i], arrowhead='vee')
        filepath = os.path.join(OUTPUT_FOLDER, filename)
        dot.render(filepath, format="png", cleanup=True)