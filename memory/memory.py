from semantics.types import Types

class Memory:
    def __init__(self, start_address):
        self.start_address = start_address
        self.int_counter = -1
        self.float_counter = 1999
        self.string_counter = 3999
        self.char_counter = 5999
        self.bool_counter = 7999

    def get_address(self, value_type):
        if value_type == Types.INT:
            self.int_counter += 1
            return self.start_address + self.int_counter
        elif value_type == Types.FLOAT:
            self.float_counter += 1
            return self.start_address + self.float_counter
        elif value_type == Types.CHAR:
            self.char_counter += 1
            return self.start_address + self.char_counter
        elif value_type == Types.STRING:
            self.string_counter += 1
            return self.start_address + self.string_counter
        elif value_type == Types.BOOL:
            self.bool_counter += 1
            return self.start_address + self.bool_counter
        else:
            print("ERROR finding address")
            return -1
