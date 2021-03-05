class Room:
    
    def __init__(self, name, capacity, free_spaces, entry_fee):
        self.name = name
        self.capacity = capacity
        self.free_spaces = free_spaces
        self.songs = []
        self.guests = []
        self.entry_fee = entry_fee
        self.till = 0
        

    def get_capacity(self):
        return self.capacity

    def get_free_spaces(self):
        return self.free_spaces

    def guest_count(self):
        return len(self.guests)

    def add_guest_to_room(self, guest):
        self.guests.append(guest)
    
    def check_in_guest(self, guest):
        if self.free_spaces() > 0 and guest.can_afford(self.entry_fee):
           guest.pay(self.entry_fee)
           self.till += self.entry_fee
           self.guests.append(guest)

    def check_in_guests(self, guests):
        if self.free_spaces() >= len(guests):
            for guest in guests:
                self.check_in_guest(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def clear_guests(self):
        self.guests.clear()

    def song_count(self):
        return len(self.songs)

    def add_song_to_room_playlist(self, song):
        self.songs.append(song)

    def add_songs(self, songs):
        for song in songs:
            self.songs.append(song)

    def clear_songs(self):
        self.songs.clear()




 
        