
d1 = [(x, y) for x in range(3) for y in range(3)]
print(d1)
print("-" * 40)

d2 = [(x, y) for x in range(1, 6) for y in range(1, x+1)]
print(d2)
print("-" * 40)

d3 = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(1, 11)]
print(d3)
print("-" * 40)

players = {
    'sachin': [290, 350, 460, 401, 380],
    'rahul': [230, 410, 185, 275, 370],
    'sehwag': [380, 430, 485, 390, 350],
    'sourav': [140, 190, 385, 430, 320],
    'yuvraj': [160, 230, 380, 130, 184]
}

print(f"players :{players}")
print("-" * 40)

print(f"sachin :{players['sachin']}")
print(f"sachin :{sum(players['sachin'])}")

print("-" * 40)

scores = {k: sum(v) for k, v in players.items()}
print(scores)
print("-" * 40)

scores = {k :(lambda scores: sum(scores) / len(scores))(v)
            for k, v  in players.items()}
print(scores)
print("-" * 40)

def avg_score(score):
    return sum(score) / len(score)

scores = {k: avg_score(v) for k, v in players.items()}
print(scores)
print("-" * 40)

basic1 = [{x: (lambda par: "Mr." + par) ("sachin {}".format(x))}
            for x in range(1, 6)]
print(basic1)

players = {
    'sachin': [290, 350, 460, 401, 380],
    'rahul': [230, 410, 185, 275, 370],
    'sehwag': [380, 430, 485, 390, 350],
    'sourav': [140, 190, 385, 430, 320],
    'yuvraj': [160, 230, 380, 130, 184]
}

scores = [score for score in players]
print(scores)
print("-" * 40)

scores = [score for score in players.values()]
print(scores)
print("-" * 40)

scores = [scr for score in players.values() for scr in score if scr >= 200]
print(scores)
print("-" * 40)

scores = {name: [scr for scr in score if scr > 200]
          for name, score in players.items()}
print(scores)
