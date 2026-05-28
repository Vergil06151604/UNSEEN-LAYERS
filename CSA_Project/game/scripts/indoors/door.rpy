label door:
    scene door_1 with dissolve
    "You decided to take a closer look at the door"
    if power + eyecheck + recipe + bath + car + sleep<5:
        jump fail
        pass
    else:
        jump success



label fail:
    "You tried to push it"
    p1 "Hmmm. Won\'t move at all. Almost feels like it\'s a part of the wall"
    p1 "Doesn't even crack when I push it. Can't even shake it either."
    scene door_closeup with dissolve
    p1 "Though it seems like there's a keyhole on the door"
    p1 "Better look out for keys and stuff"
    jump home_decision_2

label success:
    if key:
        scene pills_door at force_stretch
        with dissolve
        p1 "I have a hunch that this may help"
        "???" "Five... memories..."
        window hide None
        scene pills_light at force_stretch
        with dissolve
        with Pause(1.0)
        ""
        scene key at force_stretch
        with dissolve
        with Pause(1.0)
        ""
        scene key_grip at force_stretch
        with dissolve
        with Pause(1.0)
        ""
        scene key_light at force_stretch
        with dissolve
        with Pause(1.0)
        ""
        scene door_1 with dissolve
        with Pause(0.8)
        ""
        scene open_1 with dissolve
        with Pause(0.8)
        ""
        scene open_2 with dissolve
        with Pause(0.8)
        ""
        scene white_screen with dissolve
        with Pause(0.8)
        window show
        "???" "You did this"
        p1 """
        Yes...

        Thanks for the help all this way, I guess
        """
        "???" "Go thank yourself"
        "???" "For that we are one of the same, you and I"
        p1 """
        But I've lost you, and you've lost me

        And now we're connected by that very same memories...
        """
        window hide None
        with Pause(0.5)
        scene street at force_stretch
        with dissolve
        with Pause(0.8)
        p1 "Wow. I thought it was all over. Never knew there's something more."
        p1 "Well, it's nice that I've got most of my memories back by now"
        p1 """
        So... let's get all of this together

        Right now, I should be in a comma...

        Think I got injected by something back at the \"kitchen\" when I was cooking. 

        That \"oil spilling onto my arm\" should just be needles

        And the window... should have been a pupil check to see if I\'m alive or not

        Now it all makes sense...

        The last thing I remember in the real world was a car driving towards me, then it all stopped

        Well then, I guess all what\'s left is to walk out of this spot. 

        And there's no turning back.
        """
        p2 "Right! You finally got it!"
        p1 "Ah! Wait, thought you returned to myself as a part of my personality"
        p2 "Well... (uh, how unfortunate) Doesn't seems so..."
        p1 "What unfortunate?"
        p2 "Nothing. Nevermind. Let's just say that I'm another piece of you that has to be bounded with you."
        p2 "All you gotta do is to believe in me, wholeheartedly"
        p1 "Really? Fine. "
        p1 "(thoughts: Well, I did make it out under that voice\'s directions. Hope it\'ll be similar this time)"
        "But you can\'t help to think that something seems wrong..."
        "You walk along the street, and you find a stationary store, a pizza house, a pharmasy, a hardware store, and a path to a labyrinth"
        "The end of the street is filled with black smoke, almost seems like a natural boundary of the place"
        p2 "The black smoke! Pass through it and you\'ll reach the end!"
        p2 "Hurry, we\'ve got no time left!"
        p1 "(thought: Really? But the burden of the 18 hours seems already diminished... Can't feel that urge anymore)"
        jump street_choice


