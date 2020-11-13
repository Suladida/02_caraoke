class Room:
    def __init__(self, room_name):
        self.room_name = room_name
        self._guests = []
        self._songs = []

    def check_room_occupancy(self):
        return len(self._guests)

    def add_guest_to_list(self, new_guest):
        self._guests.append(new_guest)













    # def add_guest_to_room(self, new_guest):
    #     self._guests += (new_guest)
    #     return self._guests