label altar_decision:
    scene altar at force_stretch
    with dissolve
    "You arrave at an altar."
    p2 "Finally we\'re here!"
    p1 "What now?"
    p2 "This is where everything ends."
    p2 "So, in short, this place is the very core of this cursed place. You need to break the altar!"
    p1 "But... how?"
    p2 "The Yamato should do."
    menu:
        "What will you do?"
        "Return":
            "You decide to go back"
            d "There you are! How did you manage to sneak in before letting me notice?"
            p1 "Wha..."
            play sound "audio/gunshot.mp3"
            scene black_background at force_stretch
            with dissolve
            scene killed at force_stretch
            with dissolve
            stop sound
            "You\'re shot from the back by [dante_name]."
            "The effect of the potion doesn\'t seem to last long."
            return
        "Use the power of the Yamato" if yamato:
            scene altar_yamato at force_stretch
            with dissolve
            scene altar_yamato2 at force_stretch
            with dissolve
            p2 "That\'s right! You did this!"
            p2 "What a fool..."
            p1 "What?"
            p2 "Haha... Can\'t you see that I\'m different from that voice in your head from before?"
            p1 "I KNEW THAT! What have you made me done?"
            p2 "Oh, get this straight, sweetheart. You did this, not ME!"
            p2 "You DESTROYED your OWN mental world! Now I get to take place!"
            p1 "Who the hell are you?"
            p2 "Let\'s just say that I\'m another personality thrived from your body after the car crash"
            p2 "I\'ve been wandering around here for a long time waiting for you."
            p2 "I beat the labyrinth once, but I\'ve got no more strength to retrieve the Yamato."
            p2 "And Dante was searching for me, trying to kill me! "
            p2 "How funny... All this time what Dante wanted was to help you to get rid of me"
            p1 "That\'s why... YOU!"
            scene altar_yamato3 at force_stretch
            with dissolve
            p2 "Too late for anything by now!"
            scene white_screen at force_stretch
            with dissolve
            scene wake_up at force_stretch
            with dissolve
            p2 "Ah... Finally some fresh air..."
            "Fake Ending Unlocked"
            return


