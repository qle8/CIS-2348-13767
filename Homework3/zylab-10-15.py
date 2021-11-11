# Name: Quang Le
# Student ID: 1768324 

class Team:

    def __init__(self, name = 'none', team_wins = 0, team_losses = 0):
        self.name = name
        self.team_wins = team_wins
        self.team_losses = team_losses

    def get_win_percentage(self):
        # Calorie formula
        win_percent = self.team_wins / (self.team_wins + self.team_losses)
        return win_percent


name = input()
wins = float(input())
losses = float(input())

student_team = Team(name, wins, losses)
percent = student_team.get_win_percentage()
if percent > 0.5:
    print('Congratulations, Team {} has a winning average!'.format(name))
else:
    print('Team {} has a losing average.'.format(name))

idk=0
if student_team.get_win_percentage() == 0.8125:
    idk+=1
if student_team.get_win_percentage() == 0.4:
    idk+=1
if student_team.get_win_percentage() == 0.0:
    idk+=1
