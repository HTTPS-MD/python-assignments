import builder

if __name__ == "__main__":
    user_hero = input("Hero name: ")
    hero_item = input("Hero's core item/counter: ")

    builder.save_build(user_hero, hero_item)

    print("Build saved successfully!")