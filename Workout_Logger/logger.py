import json


def save_workout(split, exercise):

    try:
        with open('workout.json', 'r') as file:
            workout_list = json.load(file)

    except FileNotFoundError:
        workout_list = []

    workout_list.append({"Workout Split" : split, "Exercise" : exercise})


    with open('workout.json', 'w') as file:
        json.dump(workout_list, file, indent=4)