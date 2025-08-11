class AllOne:

    def __init__(self):
        self.strings = {}

    def inc(self, key: str) -> None:
        if key in self.strings:
            self.strings[key] += 1
        else:
            self.strings[key] = 1

    def dec(self, key: str) -> None:
        count = self.strings[key]
        if (count - 1) == 0:
            del self.strings[key]
        else:
            self.strings[key] -= 1

    
            

    def getMaxKey(self) -> str:
        

    def getMinKey(self) -> str:
        


# ["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"]
# [[],["hello"],["hello"],[],[],["leet"],[],[]]