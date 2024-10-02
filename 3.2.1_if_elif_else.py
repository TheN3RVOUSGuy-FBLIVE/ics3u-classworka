team_a_points = 25
team_a_wins = 15

team_b_points = 20
team_b_wins = 16

if team_a_points > team_b_points:
    print("Team A wins!")
    team_a_wins += 1
elif team_b_points > team_a_points:
    print("Team B wins!")
    team_b_wins += 1
else:
    print("Tie.")

if team_a_wins > team_b_wins:
    print("Team A has more wins than Team B.")
elif team_b_wins > team_a_wins:
    print("Team B has more wins than Team A.")
else:
    print("Both Teams A and B have the same number of wins.")
#1 this is because team a has more points hence team_a_wins += 1 comes into effect and they both have 16 wins
#2 elif checks if the previous if statement is true. If it is, the code under it runs. Else checks if if and elif are false. If so, code under it will run.
#3 it now runs the code even if the if statement above is false