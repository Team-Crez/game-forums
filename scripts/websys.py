class WebReader:
    def __init__(self, requester):
        self.requester = requester
    
    def readContent(self, addr):
        return self.requester(addr).text