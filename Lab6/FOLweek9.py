# Goal: Prove that John likes peanuts

# Knowledge Base
likes = []
food = []
eats = []
alive = []
not_killed = []
# Given facts from PDF
food.append("apple")
food.append("vegetable")

eats.append(("anil", "peanuts"))
alive.append("anil")
# Harry eats everything Anil eats
def harry_eats_all():
    for (_, item) in eats:
        eats.append(("harry", item))

harry_eats_all()
# Anyone alive → not killed
for x in alive:
    not_killed.append(x)

# Anyone not killed → alive
for x in not_killed:
    alive.append(x)
# If someone eats something & is not killed → that thing is food
def derive_food():
    for (person, item) in eats:
        if person in not_killed and item not in food:
            food.append(item)

derive_food()
# John likes all food
def derive_likes():
    for item in food:
        likes.append(("john", item))
derive_likes()
# Query we want to prove
query = ("john", "peanuts")
# Resolution-like check
if query in likes:
    print("Conclusion: John likes peanuts (PROVED).")
else:
    print("NOT PROVED.")
