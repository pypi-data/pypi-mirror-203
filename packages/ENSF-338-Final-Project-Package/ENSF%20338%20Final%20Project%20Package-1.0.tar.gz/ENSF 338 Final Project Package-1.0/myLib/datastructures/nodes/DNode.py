
class DNode():
    """"A representation of a data node for use in various data structures."""
    
    def __init__(self, data):
        """Initialize data and next variables."""
        self.data = data
        self.next = None
        self.prev = None

