from linked_lists.node import Node
from linked_lists.base_linked_list import BaseLinkedList
import os
from graphviz import Digraph
from utils.checks import check_graphviz

OUTPUT_FOLDER = "output"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

class DoublyLinkedList(BaseLinkedList):
    """
    Implementación de una lista doblemente enlazada.
    Hereda de BaseLinkedList para reutilizar atributos y métodos comunes.
    """

    def __init__(self):
        """
        Inicializa la lista doblemente enlazada.
        """
        super().__init__()

    def addItem(self, item):
        """
        Añade un nuevo elemento al final de la lista doblemente enlazada.

        :param item: Objeto a agregar (por ejemplo, una instancia de Song).
        """
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            self.current = self.head
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def deleteCurrentItem(self):
        """
        Elimina el elemento actual de la lista doblemente enlazada.
        Si el elemento actual es la cabeza, actualiza la cabeza.
        """
        if not self.head or not self.current:
            return
        if self.current == self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            self.current = self.head
            return
        prev = self.current.prev
        next_node = self.current.next
        if prev:
            prev.next = next_node
        if next_node:
            next_node.prev = prev
        self.current = next_node if next_node else self.head

    def nextItem(self):
        """
        Avanza al siguiente elemento de la lista doblemente enlazada.
        """
        if self.current and self.current.next:
            self.current = self.current.next

    def previousItem(self):
        """
        Retrocede al elemento anterior de la lista doblemente enlazada.
        """
        if self.current and self.current.prev:
            self.current = self.current.prev

    def showAll(self):
        """
        Muestra todos los elementos de la lista doblemente enlazada en consola.
        """
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def grafic(self, filename="nombre_lista"):
        """
        Genera una imagen PNG que representa gráficamente la lista y la guarda en la carpeta output.

        :param filename: Nombre base del archivo PNG generado.
        """
        if not check_graphviz():
            return
        dot = Digraph(comment="Doubly Linked List")
        temp = self.head
        idx = 0
        nodes = []
        while temp:
            node_name = f"node{idx}"
            label = str(temp.data.title) if hasattr(temp.data, "title") else str(temp.data)
            dot.node(node_name, label)
            nodes.append(node_name)
            temp = temp.next
            idx += 1
        for i in range(len(nodes) - 1):
            dot.edge(nodes[i], nodes[i + 1], arrowhead='normal')
            dot.edge(nodes[i + 1], nodes[i], arrowhead='vee')
        filepath = os.path.join(OUTPUT_FOLDER, filename)
        dot.render(filepath, format="png", cleanup=True)