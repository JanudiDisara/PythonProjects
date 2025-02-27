import random
import game_data
import art

answer = 'y'
score = 0
random_compare = random.choice(game_data.data)
random_against = random.choice(game_data.data)

while answer == 'y':
    print(art.logo)
    print(f"Compare A: {random_compare["name"]}, a {random_compare["description"]}, from {random_compare["country"]}")
    print(art.vs)
    print(f"Against B: {random_against["name"]}, a {random_against["description"]}, from {random_against["country"]}")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice == 'a':
        if random_compare["follower_count"] < random_against["follower_count"]:
            answer = 'n'
            print(f"Sorry that's wrong. Final score: {score}")
        else:
            score += 1
            answer = 'y'
            random_compare = random_against
            random_against = random.choice(game_data.data)
    if choice == 'b':
        if random_compare["follower_count"] > random_against["follower_count"]:
            print(f"Sorry that's wrong. Final score: {score}")
            answer = 'n'
        else:
            score += 1
            answer = 'y'
            random_compare = random_against
            random_against = random.choice(game_data.data)