from linked_lists.node import Node
from linked_lists.base_linked_list import BaseLinkedList
import os
from graphviz import Digraph
from utils.checks import check_graphviz  

OUTPUT_FOLDER = "output"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

class CircularLinkedList(BaseLinkedList):
    """
    Implementación de una lista enlazada circular simple.
    Hereda de BaseLinkedList para reutilizar atributos y métodos comunes.
    """

    def __init__(self):
        """
        Inicializa la lista enlazada circular simple.
        """
        super().__init__()

    def addItem(self, item):
        """
        Añade un nuevo elemento al final de la lista circular.

        :param item: Objeto a agregar (por ejemplo, una instancia de Song).
        """
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.current = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def deleteCurrentItem(self):
        """
        Elimina el elemento actual de la lista circular.
        Si el elemento actual es la cabeza, actualiza la cabeza.
        """
        if not self.head or not self.current:
            return
        if self.current == self.head:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            if self.head == self.head.next:
                self.head = None
                self.current = None
            else:
                temp.next = self.head.next
                self.head = self.head.next
                self.current = self.head
            return
        prev = self.head
        while prev.next != self.current:
            prev = prev.next
        prev.next = self.current.next
        self.current = prev.next

    def nextItem(self):
        """
        Avanza al siguiente elemento de la lista circular.
        """
        if self.current:
            self.current = self.current.next

    def previousItem(self):
        """
        No permitido para lista circular simple.
        """
        pass

    def showAll(self):
        """
        Muestra todos los elementos de la lista circular en consola.
        """
        if not self.head:
            return
        temp = self.head
        while True:
            print(temp.data)
            temp = temp.next
            if temp == self.head:
                break

    def grafic(self, filename="circular_linked_list"):
        """
        Genera una imagen PNG que representa gráficamente la lista enlazada circular simple.

        :param filename: Nombre base del archivo PNG generado.
        """
        if not check_graphviz():
            return
        dot = Digraph(comment="Circular Linked List")
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
            dot.edge(nodes[i], nodes[(i + 1) % len(nodes)])
        filepath = os.path.join(OUTPUT_FOLDER, filename)
        dot.render(filepath, format="png", cleanup=True)