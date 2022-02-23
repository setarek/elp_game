games = ({"team": "Arsenal", "played": 38, "won":14, "drawn":14,"lost":10, "diff":8},
         {"team": "Aston Villa", "played": 38, "won":9, "drawn":8,"lost":21, "diff":-26},
         {"team": "Bournemouth", "played": 38, "won":9, "drawn":7,"lost":22, "diff":-26},
         {"team": "Brighton", "played": 38, "won":9, "drawn":14,"lost":15, "diff":-15},
         {"team": "Burnley", "played": 38, "won":15, "drawn":9,"lost":14, "diff":-7},
         {"team": "Chelsea", "played": 38, "won":20, "drawn":6,"lost":12, "diff":15},
         {"team": "Crystal Palace", "played": 38, "won":11, "drawn":10,"lost":17, "diff":-19},
         {"team": "Evertone", "played": 38, "won":13, "drawn":10,"lost":15, "diff":-12},
         {"team": "Leicester City", "played": 38, "won":18, "drawn":8,"lost":12, "diff":26},
         {"team": "Liverpool", "played": 38, "won":32, "drawn":3,"lost":3, "diff":52},
         {"team": "Manchester City", "played": 38, "won":26, "drawn":3, "lost":9, "diff":67},
         {"team": "Manchester Utd", "played": 38, "won":18, "drawn":12, "lost":8, "diff":30},
         {"team": "Newcastle", "played": 38, "won":11, "drawn":11, "lost":16, "diff":-20},
         {"team": "Norwich", "played": 38, "won":5, "drawn":6,"lost":27, "diff":-49},
         {"team": "Sheffield Utd", "played": 38, "won":14, "drawn":12, "lost":12, "diff":0},
         {"team": "Tottenham", "played": 38, "won":16, "drawn":11, "lost":11, "diff":14},
         {"team": "Southampton", "played": 38, "won":15, "drawn":7, "lost":16, "diff":-9},
         {"team": "Watford", "played": 38, "won":8, "drawn":10, "lost":20, "diff":-28},
         {"team": "West Ham", "played": 38, "won":10, "drawn":9, "lost":19, "diff":-13})


def elp_result(name):

    selected_team = {}
    for game in games:
        if game.get("team") == name:
            selected_team["score"] = (game.get("won") * 3) + game.get("drawn")
            selected_team["diff"] = game.get("diff")
            selected_team["name"] = game.get("team")

    if "name" not in selected_team:
        return "this team did not play"

    count = len(game)
    for g in games:
        score = (g.get("won") * 3) + g.get("drawn")
        if score < selected_team["score"]:
            count = count - 1
        if score == selected_team["score"] and g.get("diff") < selected_team["diff"]:
            count = count - 1


    team_info = "{} came {}th with {} points and a goal difference of {}".\
        format(selected_team["name"], count, selected_team["score"], selected_team["diff"])
    return team_info

def main():
    info = elp_result("Norwich")
    print(info)
if __name__ == "__main__":
    main()
