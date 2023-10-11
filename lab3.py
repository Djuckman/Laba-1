list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
left = list_players[:int(len(list_players)/2)]
rigth = list_players[int(len(list_players)/2):]
print(left)
print(rigth)