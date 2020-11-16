class Guest:
    
    def __init__(self, name, age, wallet, fave_song, rendition_of_song):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.fave_song = fave_song
        self.rendition_of_song = rendition_of_song
        
    
    def fave_song_on_room_playlist(self, room):
        return "Whoo!"

    def buy_drink(self, drink):
        if self.sufficient_funds(drink):
            self.wallet -= drink.price
            self.rendition_of_song -= drink.alcohol_level
    
    
    def buy_food(self, food):
        if self.sufficient_funds(food):
            self.wallet -= food.price
            self.rendition_of_song += food.rejuvination_level
    
    def sufficient_funds(self, item):
        return self.wallet >= item.price