import random

# Ask the user how many stories they want to create
num_stories = int(input("How many stories would you like to generate? "))

# List of random events for variety
events = [
    "found a hidden treasure",
    "met a talking animal",
    "discovered a secret door",
    "won a mysterious contest",
    "flew on a magical carpet"
]

# Open a file to save the stories
with open("stories.txt", "w") as file:
    for i in range(num_stories):
        # Ask for user input
        name = input(f"Story {i+1} - What is your hero's name? ")
        age = input(f"Story {i+1} - How old is {name}? ")
        favorite_food = input(f"Story {i+1} - What is {name}'s favorite food? ")
        favorite_color = input(f"Story {i+1} - Favorite color? ")

        # Pick a random event
        event = random.choice(events)

        # Create the story
        story = f"""
Once upon a time, there was a person named {name}.
At {age} years old, {name} loved eating {favorite_food} every single day.
One day, wearing their favorite {favorite_color} outfit, {name} {event}!
"""

        # Print the story
        print(story)

        # Save the story to the file
        file.write(story + "\n")

print("All stories saved to stories.txt!")
