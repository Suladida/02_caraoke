class Room:
    def __init__(self, room_id, price):
        self.room_id = room_id
        self.price = price
        self.guests = []
        self.playlist = []


    # def get_room_price(self, room_id):
    #         if room_id == 11:
    #             return self.price

    def guest_check_in(self, new_guest):
        self.guests.append(new_guest)
        
    def check_room_guests(self):
        return len(self.guests)



    # def add_room(self, new_room):
    #     self.rooms.append(new_room)



