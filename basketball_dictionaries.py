##Challenge 1: Update the Constructor 

class Player:
    def __init__(self, player_info):
        self.name = player_info["name"]
        self.age = player_info["age"]
        self.position = player_info["position"]
        self.team = player_info["team"]

##Challenge 2: Create Instances using Individual Player Dictionaries 

kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
    
# Create your Player instances here!

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

##Challenge 3: Make a list of PLayer Instances from a List of Dictionaries 

new_team = []
for player_dict in player:
    player = Player(player_dict)
    players_list.append(player)

##Bonus 
class Player:
    def __init__(self, player_info):
        self.name = player_info["name"]
        self.age = player_info["age"]
        self.position = player_info["position"]
        self.team = player_info["team"]

    @classmethod
    def get_team(cls, team_list):
        team_players = []
        for player_dict in team_list:
            player = cls(player_dict)
            team_players.append(player)
        return team_players
