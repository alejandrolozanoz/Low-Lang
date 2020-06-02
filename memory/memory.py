from semantics.types import Types

class Memory:
    def __init__(self, start_address):
        self.start_address = start_address
        self.int_counter = -1
        self.float_counter = -1
        self.string_counter = -1
        self.char_counter = -1
        self.bool_counter = -1
def getAddress(self, value_type):
    if value_type == Types.INT:
        self.int_counter += 1
        return self.start_address + self.int_counter
    elif value_type == Types.FLOAT:
        self.float_counter += 1
        return self.start_address + self.float_counter + 2000
    elif value_type == Types.CHAR:
        self.char_counter += 1
        return self.start_address + self.char_counter + 4000
    elif value_type == Types.STRING:
        self.string_counter += 1
        return self.start_address + self.string_counter + 6000
    elif value_type == Types.BOOL:
        self.bool_counter += 1
        return self.start_address + self.bool_counter + 8000
    else:
        print("ERROR finding address")
        return -1
