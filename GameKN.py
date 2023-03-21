print("Вас приветсвует знаменитая игра Крестики-нолики")

field=[["_","_","_"],
      ["_","_","_"],
      ["_","_","_"]]

print("  0 1 2")
for a in range (len(field)):
    print(str(a),*field[a])