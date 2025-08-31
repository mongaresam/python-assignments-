 # Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"

# Child class inheriting from Device
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)
        self.__storage = storage      # encapsulation (private)
        self.__battery = battery      # encapsulation (private)

    # Getter and Setter for storage
    def get_storage(self):
        return self.__storage

    def upgrade_storage(self, new_storage):
        self.__storage = new_storage

    # Method to show battery status
    def battery_status(self):
        return f"Battery at {self.__battery}%"

    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)

# Example usage
phone = Smartphone("Samsung", "Galaxy S23", "128GB", 80)
print(phone.info())             # Samsung Galaxy S23
print(phone.get_storage())      # 128GB
print(phone.battery_status())   # Battery at 80%
phone.upgrade_storage("256GB")
print(phone.get_storage())      # 256GB
phone.charge(30)
print(phone.battery_status())   # Battery at 100%
