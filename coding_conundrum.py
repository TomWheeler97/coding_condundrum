# The general problem is that I want to give the player the choice of what clothes they want the character to be in.

# As an example :-


label clothes_designation:
    menu:
        "clothes_1":
            $ clothes = 1
            jump new

        "clothes_2":
            $ clothes = 2
            jump new

        "clothes_3":
            $ clothes = 3
            jump new

        "clothes_4":
            $ clothes = 4
            jump new

    # This would be simple but there are multiple character I need to assign clothes options to.

    label new:
    menu:
        "chara1_clothes_1":
            $ chara_1_clothes = 1
            jump new

        "chara1_clothes_2":
            $ chara_1_clothes = 2
            jump new

        "chara1_clothes_3":
            $ chara_1_clothes = 3
            jump new

        "chara1_clothes_4":
            $ chara_1_clothes = 4
            jump new

        "chara2_clothes_1":
            $ chara_2_clothes = 1
            jump new

        "chara2_clothes_2":
            $ chara_2_clothes = 2
            jump new

        "chara2_clothes_3":
            $ chara_2_clothes = 3
            jump new

        "chara2_clothes_4":
            $ chara_2_clothes = 4
            jump new

        "chara3_clothes_2":
            $ chara_3_clothes = 2
            jump new

        "chara3_clothes_3":
            $ chara_3_clothes = 3
            jump new

        "chara3_clothes_4":
            $ chara_3_clothes = 4
            jump new

# So now when I show an image, I need it to show all the characters in the clothes the player chose.
# My idea was to give every image in a folder a number (ex. pic1, pic2, ect.) and combine all the variable above into one.

    if chara1_clothes == 1 and chara2_clothes == 1 and chara3_clothes == 1:
        $ combine = 1
    if chara1_clothes == 2 and chara2_clothes == 1 and chara3_clothes == 1:
        $ combine = 2
    #ect.

# Then you would have something like:-

    scene pic($ combine)
    with dissolve

# First, I don't know how to tell the computer to show the correct image with this specific number.

# I'm also fully aware that this is such an inefficient way of doing it and it doesn't even get into the fact that each character has different personalities that will also affect the images used.

# What do I do?
