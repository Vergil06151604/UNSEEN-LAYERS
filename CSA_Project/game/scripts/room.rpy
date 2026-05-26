label room:
    scene bedroom with dissolve
    "You feel your back sticky with cold sweat"
    "You cannot hold on any longer"
    "You have no more energy for anything more"
    menu:
        "You are exhausted. What will you do now?"
        
        "Use the computer in the room (takes 1 hour)" if not car:
            jump computer
            pass
        "I cannot hold on anymore... I'll have to get some sleep (takes 4 hours)":
            jump sleeping
            pass

label computer:
    scene pc with dissolve
    p1 "The computer looks familiar... "
    p1 "I might as well remember the password of it"
    "You manage to start the computer"
    scene strange_car at truecenter
    with dissolve
    p1 "What?"
    scene strange_car at truecenter, dizzy_blur
    p1 "This shall be the final one. If it doesn't end here, I don't think I can last any longer anyways"
    p1 "Car crash..."
    "???" "You finally got it"
    scene white_screen with dissolve
    with Pause(1.0)
    "You passed out"
    scene pc with dissolve
    "You seem to recall something"
    "1 hour has passed"
    "Memory+1"
    p1 "I have to take a rest..."
    $game_time += 1
    $ car = 1
    jump sleeping

label sleeping:
    scene lie_down with dissolve
    "The bed is big and comfortable"
    "Seems like it was meant for two to sleep on"
    "But who are they?"
    p1 "Emma..."
    p1 "Huh? Who's Emma?"
    scene sleep with dissolve
    "The light in the room automatically goes out, almost like deliberately calling you to sleep"
    scene black with dissolve
    with Pause(1.0)
    scene sea with dissolve
    with Pause(1.0)
    p1 "Where... am I?"
    scene onwater with dissolve
    with Pause(1.0)
    p1 """
    I\'m walking on some water?

    Heard Jesus could walk on water

    He\'s meant to be the savior for humanity...

    And whose savior am I supposed to be?

    Well, I do know none of this makes any sense

    As if I've seen something with a bit more logic since I've been here
    """
    scene underwater with dissolve
    with Pause(1.0)
    p1 "Is that... me?"
    scene sea with dissolve
    "It's about time."
    "To end all of this."
    scene white_screen with dissolve
    with Pause(0.8)
    "You feel something in you hand"
    scene pills_get with dissolve
    p1 "Somehow I feel this is the end to everything"
    $ sleep = 2
    "You remember something more"
    "Memory+2"
    $game_time += 4
    "4 hours have passed"
    $ key = True
    jump home_decision_2
