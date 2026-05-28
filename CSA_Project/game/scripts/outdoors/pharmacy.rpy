label pharmacy:
    scene pharmacy_after at force_stretch
    with dissolve
    o2 "Welcome! What would you want?"
    p1 "Who\'s talking?"
    o2 "Oh, I\'m just making potions behind the shelves. What do you want?"
    label pharmacy_choice :
        scene pharmacy_after at force_stretch
        with dissolve
        menu:
            "What would you like to buy?"
            "A potion that can make you invisible for a short time. Perfect for sneaking by some tough enermies (costs 30 dollars)" if not potion:
                if cash >= 30:
                    scene pharmacy_potion at force_stretch
                    with dissolve
                    o1 "Perfect choice, customer! Take a little sip each time you want yourself invisible for a few minutes."
                    o1 "If you drink too much, you might kill yourself~"
                    p1 "Thanks, ma\'am."
                    jump pharmacy_choice
                    pass
                else:
                    o1 "Not enough cash!"
                    jump pharmacy_choice
                    pass
            "No thanks. I don\'t see anything I like.":
                o1 "That\'s a pity. Come back next time!"
                jump street_choice
