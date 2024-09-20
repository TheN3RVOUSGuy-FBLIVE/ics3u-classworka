#2 code has 2 empty lines to separate variables, calculation and main event
team = "Toronto Blue Jays"
current_date = "July 18, 2021"
player = "Vladimir Guerrero Jr."
home_runs_to_date = 31
games_played = 88
total_season_games = 162
home_run_record = 73

#1
# finds number of games remaining by subtracting total_season_games (162) by games_played (88)
games_remaining = total_season_games - games_played
# home_runs_per_game is calculated by dividing home_runs_to_date (31) by games_played (88)
home_runs_per_game = home_runs_to_date / games_played
# projected_home_runs = home_runs_per_game (result of previous line) divided by games_played (88)
projected_home_runs = home_runs_per_game * total_season_games
# sees if player can break record by multiplying home runs per game by season games and checking if it is more than the home run record
can_break_record = projected_home_runs > home_run_record

print(f"{player} of the {team}")
print(f"currently has {home_runs_to_date} home runs as of {current_date}.")
print(f"The current MLB record for most home runs in a season is {home_run_record}.")
print(f"With {games_remaining} games remaining and an average of {round(home_runs_per_game, 2)} home runs per game,")
print(f"it is {can_break_record} that he is on pace to break the record.")
print(f"{player} is projected to hit {round(projected_home_runs)} home runs this season.")

#4
# games_remaining = total_season_games - games_played is correct because total subtracted by ammount