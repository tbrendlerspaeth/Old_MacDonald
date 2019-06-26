### Old MacDonald Had A Farm

def mcdosong():
    animal = input("Type in the name of an animal: ").lower()
    animal_noise = input("Type in the sound the animal makes: ").lower()
    animal_noise = animal_noise + " " + animal_noise
    
    if animal_noise[0] in ["a","e","u","i","o"]: noise_article = "an"
    else: noise_article = "a"

    if animal[0] in ["a","e","u","i","o"]: animal_article = "an"
    else: animal_article = "a"

    print("Old MacDonald had a farm and on that farm he had " + animal_article + " " + animal + "."
          " With " + noise_article + " \"" + animal_noise + "\"" + " here and " + noise_article +
          " \"" + animal_noise + "\"" + " there.")

mcdosong()
