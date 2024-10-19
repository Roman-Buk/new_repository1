class Phone:
    def __init__(self, battery_level, contacts):
        self.battery_level = battery_level
        self.contacts = contacts
    def make_call(self, contact_name):
        if self.battery_level > 10:
            if contact_name in self.contacts:
                self.battery_level -= 10
                return f"Calling {contact_name} ({self.contacts[contact_name]})... Battery level: {self.battery_level}%"
            else:
                return "Contact not found!"
        else:
            return "Not enough battery to make a call!"
    def send_message(self, contact_name, message):
        if self.battery_level > 3:
            if contact_name in self.contacts:
                self.battery_level -= 3
                return f"Message sent to {contact_name} ({self.contacts[contact_name]})... Battery level: {self.battery_level}%"
            else:
                return "Contact not found!"
        else:
            return "Not enough battery to text!"
    def charge(self):
        self.battery_level = 100
        return "Phone fully charget!"
class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def use_phone(self, action, contact_name=None, message=None):
        if action == 'call':
            return self.phone.make_call(contact_name)
        elif action == 'message':
            return self.phone.send_message(contact_name, message)
        else:
            return "Invalid action!"
    def charge_phone(self):
        return self.phone.charge()
my_phone = Phone(battery_level=50, contacts={"Vika": "123-456-789", "Bob": "987-654-321", "Kein": "234-567-890", "Tanya": "876-543-210", "Dad": "567-765-890", "Mum": "290-902-758"})
user = User(name="Mike", phone=my_phone)
print(user.use_phone('call', contact_name="Vika"))
print(user.use_phone('message', contact_name="Bob", message="Hey, how are you?"))
print(user.charge_phone())
print(user.use_phone('call', contact_name="Bob"))
print(user.use_phone('call', contact_name="Kein"))
print(user.use_phone('message', contact_name="Vika", message="See you later"))
print(user.use_phone('message', contact_name="Bob", message="Let's go hang out with Vika, Kein and Tanya. What are you think?"))
print(user.use_phone('call', contact_name="Tanya"))
print(user.use_phone('call', contact_name="Vika"))
print(user.use_phone('message', contact_name="Bob", message="Okay"))
print(user.use_phone('call', contact_name="Mum"))
print(user.use_phone('call', contact_name="Dad"))
print(user.use_phone('message', contact_name="Tanya", message="Hello"))
print(user.use_phone('call', contact_name="Mum"))
print(user.use_phone('call', contact_name="Dad"))
print(user.use_phone('call', contact_name="Vika"))
print(user.use_phone('message', contact_name="Vika", message="I'll call you letter i'm have low battery"))



