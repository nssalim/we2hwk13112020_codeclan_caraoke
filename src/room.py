class Room:
    
    def __init__(self):
        self.song = song []
        self.guest = guest []
        self.room = 20
        self.entry_fee = 10

    def add_song_to_room_playlist(self, song):
        self.song.append(song)
    
    def guest_count(self):
        return len(self.guest)
    
    def add_guest_to_room(self, guest):
        self.guest.append(guest)
    
    def serve(self, room, guest):
        if self.guest.count(guest) == 0:
            return
        self.guest.remove(guest)
        room.pay_entry_fee(guest)
        self.till += guest.wallet    
        