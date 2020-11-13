class Room:
    def __init__(self, room_name):
        self.room_name = room_name
        self._guests = []
        self._songs = []

    def check_room_occupancy(self):
        return len(self._guests)

    def add_guest_to_list(self, new_guest):
        self._guests.append(new_guest)

    def remove_guest_from_list(self, guest_name):
        for guest in list(self._guests):
            if guest == guest_name:
                self._guests.remove(guest)