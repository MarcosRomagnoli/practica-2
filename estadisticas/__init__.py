
def generate_statistics(names_list, goals, goals_avoided, assists):
    combined_data = zip(names_list, goals, goals_avoided, assists)
    statistics = list(map(lambda data: {
        "Name": data[0],
        "Goals": data[1],
        "Avoided goals": data[2],
        "Assists": data[3]
    }, combined_data))
    
    return statistics


def get_top_scorer(statistics):
    top_scorer = max(statistics, key=lambda x: x["Goals"])
    return top_scorer["Name"], top_scorer["Goals"]


def calculate_score(player):
    return player["Goals"] * 1.5 + player["Avoided goals"] * 1.25 + player["Assists"]

def most_influential_player(statistics):
    most_influential_player = max(statistics, key=calculate_score)
    return most_influential_player["Name"]


def average_goals_per_match_team(statistics):
    total_goals = sum(player["Goals"] for player in statistics)
    return total_goals / 25


def average_goals_per_match_top_scorer(statistics):
    top_scorer = max(statistics, key=lambda x: x["Goals"])
    return top_scorer["Goals"] / 25