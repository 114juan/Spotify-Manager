class BaseLinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def getCurrentItem(self):
        return self.current.data if self.current else None

    def reset(self):
        self.current = self.head
