class Room:
    def __init__(self, room_name):
        self.room_name = room_name
        self._guests = []
        self._songs = []

    def check_room_occupancy(self):
        return len(self._guests)

    def check_room_songs(self):
        return len(self._songs)

    def add_guest_to_room(self, new_guest):
        self._guests.append(new_guest)

    def remove_guest_from_room(self, guest_name):
        for guest in list(self._guests):
            if guest == guest_name:
                self._guests.remove(guest)

    def add_song_to_room(self, song):
        self._songs.append(song)