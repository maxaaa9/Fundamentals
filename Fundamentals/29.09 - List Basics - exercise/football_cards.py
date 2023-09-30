team_a = []
team_b = []

for i in range(1, 12):
    team_a.append(f"A-{i}")
for i in range(1, 12):
    team_b.append(f"B-{i}")

send_off_players = input().split()
game_was_terminated = False

for check in send_off_players:
    if check in team_a:
        team_a.remove(check)
    elif check in team_b:
        team_b.remove(check)
    if len(team_a) < 7 or len(team_b) < 7:
        game_was_terminated = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_was_terminated:
    print("Game was terminated")
