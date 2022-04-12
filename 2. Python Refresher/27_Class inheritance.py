"""
class inheritance - allows one class to take some methods and properties from another class
"""


class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected.")


class Printer(Device):  # a new class Printer that inherits from Device(copy all the methods)
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)  # calling the super class or PARENT CLASS
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages


printer = Device("Printer", "USB")
print(printer)

printer.disconnect()

print('\nNew Printer:')

new_printer = Printer("Printer", "USB", 500)
new_printer.print(20)
print(new_printer)

new_printer.disconnect()

new_printer.print(100)


