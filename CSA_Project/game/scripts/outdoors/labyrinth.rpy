label labyrinth:
    scene entrance at force_stretch
    with dissolve
    "The entrance of the labyrinth doesn't seem too nice..."
    "You look inside"
    "The inner space seems to be much larger than you ever imagined"
    p2 "Get inside! Nothing scary there"
    p1 "You sure?"
    p2 "Of course! You doubting me?"
    p1 "Fine then..."
    scene labyrinth_entrance_2 at force_stretch
    with dissolve
    "Are you sure you want to enter the labyrinth?"
    "A map is reccommended. You might as well want to save the game. "
    menu:
        "Enter?"
        "Enter":
            jump inside
            pass
        "No thanks":
            jump street_choice
            pass

label laby_death:
    scene labyrinth_smoke at force_stretch
    with dissolve
    p1 "It's a dead end... and what's that smoke?"
    scene labyrinth_death at force_stretch
    with dissolve
    p1 "Uh... I can't breath!"
    p1 "(Cough... Cough...)"
    p1 "(Gasp...)"
    scene killed at force_stretch
    with dissolve
    "You're dead"
    p2 "Ha..."
    return


label inside:
    scene labyrinth_3 at force_stretch
    with dissolve
    "You slowly walk into the labyrinth"
    menu:
        "Which way are you going? There's no turning back beyond this point"
        "Forward":
            scene labyrinth_2 at force_stretch
            with dissolve
            menu:
                "Which way are you going?"
                "To the left":
                    jump laby_death
                "To the right":
                    jump laby_death
        "To the left":
            scene labyrinth_2 at force_stretch
            with dissolve
            menu:
                "Which way are you going?"
                "To the left":
                    jump laby_death
                "To the right":
                    scene labyrinth_3 at force_stretch
                    with dissolve
                    menu:
                        "Which way are you going?"
                        "Forward":
                            jump laby_death
                        "To the left":
                            scene labyrinth_2 at force_stretch
                            with dissolve
                            menu:
                                "Which way are you going?"
                                "To the left":
                                    jump laby_death
                                "To the right":
                                    scene labyrinth_3 at force_stretch
                                    with dissolve
                                    menu:
                                        "Which way are you going?"
                                        "Forward":
                                            scene labyrinth_3 at force_stretch
                                            with dissolve
                                            menu:
                                                "Which way are you going?"
                                                "Forward":
                                                    jump laby_death
                                                "To the left":
                                                    jump laby_death
                                                "To the right":
                                                    jump laby_death
                                        "To the left":
                                            scene labyrinth_3 at force_stretch
                                            with dissolve
                                            menu:
                                                "Which way are you going?"
                                                "Forward":
                                                    jump laby_death
                                                "To the left":
                                                    scene labyrinth_2 at force_stretch
                                                    with dissolve
                                                    menu:
                                                        "To the left":
                                                            jump laby_death
                                                        "To the right":
                                                            jump laby_end
                                                            pass
                                                "To the right":
                                                    jump laby_death
                                        "To the right":
                                            jump laby_death
                        "To the right":
                            jump laby_death

        "To the right":
            scene labyrinth_3 at force_stretch
            with dissolve
            "You slowly walk into the labyrinth"
            menu:
                "Which way are you going?"
                "Forward":
                    jump laby_death
                "To the left":
                    jump laby_death
                "To the right":
                    jump laby_death
        "Backwards":
            scene entrance at force_stretch
            with dissolve
            p1 "I'm outta here"
            p2 "Seriously? Oh come on, you can't be serious"
            p2 "We just decided to get in!"
            jump street_choice

label laby_end:
    scene yamato_get at force_stretch
    with dissolve
    "You arrive at the final room at the center of the labyrinth"
    p2 "Congradulations! You've made here alive!"
    p1 "Why do you sound a bit... dissappointed?"
    p2 "Nonsense! I'm more than happy to see you here!"
    "You find 1000... No, just 60 dollars piled up at the corner"
    p2 "Feeling dissappointed? Look, that\'s the Yamato!"
    p2 "The legendary devil sword! Its value should be more than enough to buy all industries in the US!"
    p2 "Bet you can use this as a tool..."
    p1 "Really? I'll take it, I guess"
    scene yamato_get2 at force_stretch
    with dissolve
    p1 "Alright, time to leave this maze"
    $ yamato = True
    scene street at force_stretch
    with dissolve
    $ laby = True
    play sound "audio/earthquake.mp3"
    $ cash += 60
    p1 "Huh?"
    "The entrance of the labyrynth has collapsed."
    "You can no longer go there anymore."
    p1 "Well... kind of lucky that I didn't get buried there alive"
    p1 "I should show it to the stationary store\'s owner for my reward. He promised me something as a price of beading that maze"
    jump street_choice
    