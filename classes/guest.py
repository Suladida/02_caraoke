class Guest:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash

    def guest_cash(self, name):
            if name == "Trixie":
                return self.cash
            else:
                return "Guest not found."

    # def add_to_guests(self, new_guest):
    #         self.guests.append(new_guest)
    #         pass

    # def count_guests(self):
    #     return len(self.guests)





