""" Упражнение 6
Разработать методы для программы Камень-Ножницы-Бумага.
Метод rps_game_winner должен принимать на вход массив следующей структуры
[ ["player1", "P"], ["player2", "S"] ], где P - бумага, S - ножницы, R - камень, и
функционировать следующим образом:

• если количество игроков больше 2 необходимо вызывать исключение
WrongNumberOfPlayersError
• если ход игроков отличается от ‘R’, ‘P’ или ‘S’ необходимо вызывать
исключение NoSuchStrategyError
• в иных случаях необходимо вернуть имя и ход победителя, если оба
игрока походили одинаково - выигрывает первый игрок. """

def rps_game_winner (players):

    if players[0][1] == players[1][1]:
        return f"{players[0][0]} {players[0][1]}"

    if len(players) >= 3:
       return "WrongNumberOfPlayersError"

    
    win_postions = {'RS': 'R', 'SR': 'R', 'PS': 'S', 'SP': 'S', 'PR': 'P', 'RP': 'P'}
    winner = players[0][1] + players[1][1]

    if winner not in win_postions:
        return "NoSuchStrategyError"
    else:
        winner = win_postions[winner]

    for player in players:
        if player[1] == winner:
            return f"{player[0]} {player[1]}"
        
print (rps_game_winner ([['player1', 'P'], ['player2','S'], ['player3', 'S']]))
print (rps_game_winner ([['player1', 'P'], ['player2','A']]))
print (rps_game_winner ([['player1', 'P'], ['player2','S']]))
print (rps_game_winner ([['player1', 'S'], ['player2','P']]))
print (rps_game_winner ([['player1', 'P'], ['player2','P']]))