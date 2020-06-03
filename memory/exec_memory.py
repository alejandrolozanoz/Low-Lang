class ExecMemory:
    def __init__(self, start_address):
        self.start_address = start_address
        self.values = {}
        
    def save_value(self, address, value):
        if (abs(address) - self.start_address >= 8000):
            self.values[address] = value == "true"
        
        elif (abs(address) - self.start_address >= 6000):
            self.values[address] = str(value)
        
        elif (abs(address) - self.start_address >= 4000):
            self.values[address] = str(value)
        
        elif (abs(address) - self.start_address >= 2000):
            self.values[address] = float(value)
        
        else:
            self.values[address] = int(value)

