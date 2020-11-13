class Room:
    def __init__(self, room_id, price):
        self.room_id = room_id
        self.price = price
        self.occupants = []
        self.playlist = []

    def hello(self):
        return "Hello!"

    def get_room_price(self, room_id):
            if room_id == 11:
                return self.price




