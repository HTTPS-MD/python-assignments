import logger

if __name__ == "__main__":

    u_split = input("Anong workout split mo ngayon? ")
    u_exercise = input("Anong exercise ang gagawin mo? ")

    logger.save_workout(u_split, u_exercise)

    print("Workout recorded! Good luck sa session mo!")