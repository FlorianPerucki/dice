from collections import defaultdict

movies_producers = defauldict(str)

print(movies_by_rank["Jaw"]) # <= No KeyError here!
