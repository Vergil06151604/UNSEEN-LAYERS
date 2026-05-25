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
        scene wake_up at force_stretch
        with dissolve
        with Pause(0.8)
        ""
        window show
        return
