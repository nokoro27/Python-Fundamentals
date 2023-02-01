class User: 
    def __init__(self, first_name, last_name, email, age, is_rewards_member, gold_card_points):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = None
        self.gold_card_points = 0
    
    def display_info(self):
        print("First Name: ", self.first_name)
        print("Last Name: ", self.last_name)
        print("Email: ", self.email)
        print("Age ", self.age)
        print("Rewards Member: ", self.is_rewards_member)
        print("Gold Card Points: ", self.gold_card_points)
    
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
    
    def spend_points(self, amount):
        self.gold_card_points -= amount

#BONUS 

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200
        return True

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("Not enough gold card points to spend.")
            return False
        self.gold_card_points -= amount
        return True