class CaraokeBar:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.stock = {}

    
    def customer_too_drunk_to_sing(self, guest):
        return guest.rendition_of_song >= 40


    def food(self, food):
        if food in self.stock:
            self.stock[food] += 1
        else:
            self.stock[food] = 1


    def stock_level(self, food):
        if food in self.stock:
            return self.stock[food]
        else:
            return 0

    def stock_value(self):
        total = 0

        for food in self.stock:
            total += (food.price * self.stock[food])

        return total


        def add_drink(self, drink):
        if drink in self.stock:
            self.stock[drink] += 1
        else:
            self.stock[drink] = 1


    def stock_level(self, drink):
        if drink in self.stock:
            return self.stock[drink]
        else:
            return 0

    def stock_value(self):
        total = 0

        for drink in self.stock:
            total += (drink.price * self.stock[drink])

        return total


    def can_serve(self, guest, drink):
        if not self.guest_is_old_enough(guest):
            return False
        if self.guest_too_drunk(guest):
            return False
        if not self.guest_can_afford_drink(guest, drink):
            return False
        if self.stock_level(drink) == 0:
            return False
        return True;

        def serve(self, guest, food):
        if self.can_serve(guest, food):
            self.stock[food] -= 1
            guest.food(food)
            self.till += food.price

    def serve(self, guest, drink):
        if self.can_serve(guest, drink):
            self.stock[drink] -= 1
            guest.buy_drink(drink)
            self.till += drink.price


    def guest_is_old_enough(self, guest):
        return guest.age >= 18


    def guest_can_afford_drink(self, guest, drink):
        return guest.sufficient_funds(drink)


