label home_decision_1:
    scene room with dissolve
    menu:
        "What will you do now?"
        "Explore the room (takes half an hour)":
            "You look around..."
            "You find a kitchen and a bathroom in the house"
            "The room you're in right now seems like a living room"
            $ game_time += 0.5
            "You find a kitchen, a bathroom in the house"
            jump home_decision_2
        "Try hard to remember who you are (takes 1 hour)":
            "You think until your head aches..."
            p1 "Uhhh..."
            p1 "What is this..."
            play sound "audio/Power.mp3"
            "???" "What form of power is this?"
            "You gained a piece of memory"
            $ power = 1
            $ game_time += 1
            "Nothing else happens..."
            jump home_decision_1


label home_decision_2:
    scene room with dissolve
    if sleep:
        p1 "No time to waste"
        p1 "Feels like it's about time for me to leave"
        p1 "This shall be the end..."
        p1 "...Or maybe the start?"
        "???" "You got that right"
        "Time for you to open the door"
    if not window_noti and recipe and bath:
        "You notice that there's a window right behind you..."
        "Strange, why haven't you noticed it before?"
        "Can\'t possibly be the developer\'s little trick, am I right?"
        "Won\'t make any sense if he would only let you see it after you explored the kitchen and the bathroom, right?"
        "...{w=0.5}Right?"
        
    if eyecheck and not pc_noti:
        """
        You can now access the bedroom

        Or, your bedroom.{w=0.2}.{w=0.2}.{w=0.2}?

        Yeah, I know, doesn\'t make any sense, since you\'ve never actually been here before
        """
        "???" "Right?"

        p1 "Great. This \"Swearing Angel\" is talking again. "
        p1 "Why does its voice seem  so familiar?"
        p1 "Must have been my own imaginations..."
        $ pc_noti = True
    menu:
        "What will you do now?"
        "Explore the kitchen" if not sleep:
            jump kitchen
            pass
        "Explore the bathroom" if not sleep:
            jump bathroom
            pass
        "Try to open the door":
            jump door
            pass
        "Look at the window" if recipe and bath and not sleep:
            jump window
        
        "Explore the room that came out of nowhere" if eyecheck and not sleep:
            jump room

label kitchen:
    scene kitchen
    """
    The kitchen looks nice. 

    Surprisingly, you see the ingredients preserved perfectly in the fridge.

    What, you do not see a fridge? Look closer, bet you can see it. 

    You feel a bit hungry by now.
    """

    menu:
        "What will you do now?"
        "Call some food delivery to your house using a phone that appeared out of nowhere (takes 1 hour)":
            jump delivery
            pass
        "Cook your own food using the seemingly fresh ingredients (takes 2 hours)":
            jump cook
            pass
        "Seriously? I'm trying to lose my weight!":
            jump home_decision_2


label eating:
    "Smells nice. "
    "You take a bite"
    "???" "Delicious..."
    p1 "Who's talking?"
    "..."
    p1"Uh... Not this again"
    "You finish the food quickly and clean the dishes"
    jump home_decision_2

label delivery:
    scene black
    "..."
    scene expression Transform("kitchen", size=(1920, 1080)) at truecenter
    with dissolve
    p1"Huh? Did I pass out?"
    p1"Seems I ordered my food... But how?"
    "You waited..."
    "You waited and waited..."
    "Wow. This is a long time. "
    play sound "audio/knock.mp3"
    p1"So it arrives. Finally. "
    p1"Uh... How exactly am I going to take it? Don't think that wooden door outside will open"
    scene expression Transform("eat", size=(1920, 1080)) at truecenter
    with dissolve
    p1"Wow. It just... appears. "
    p1"How unexpected"
    "It took you a whole hour to wait for the delivery"
    $ game_time += 1
    jump eating




label cook:
    "You decide to wash the vegetables first"
    scene wash at truecenter
    with dissolve
    p1 """
    The vegetables seems fine... They smell nice as well

    Wait... Where did I get them from?

    The fridge...?

    I don't remember where the fridge is...
    """
    show wash at truecenter, dizzy_blur
    play sound "audio/earring.mp3" loop fadeout 1.5
    $ renpy.music.set_volume(5.0, delay=0, channel='sound')

    p1"""
    Uh... Again?

    What the hell is going on!

    My head... It's gonna...
    """
    
    scene wash_02 at truecenter 
    with dissolve
    stop sound
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    p1"""
    Great. It just keeps getting better. 

    Now how exactly am I gonna eat these things?
    """

    scene wash at truecenter 
    with dissolve
    p1"""
    Huh. Interesting. Am I in a game or something?

    Or did I lose my sanity completely?

    Well, guess none of that actually matters anymore. Nothing here makes sense.

    The ingredients... They actually smell fine. And I don't see any trace of that dirty water

    Maybe I can still cook with it. Hope I don't get a diarrhae 
    """

    scene expression Transform("cooking", size=(1920, 1080)) at truecenter
    with dissolve

    "You decided to cook anyways, according to the recipe"
    "The aroma of the food hangs in the air. You can't wait to taste the food"

    scene expression Transform("recipe", size=(1920, 1080)) at truecenter
    with dissolve
    "You decided to pick up the recipe to have a second look"
    p1 "Well... It's burned, but still readable"
    p1 "Hmmm... Seems helpful. Anything else?"
    "You try to flip the page"

    scene expression Transform("med", size=(1920, 1080)) at truecenter
    with dissolve
    p1 "What the... ?"
    p1 "What is this thing?"
    """
    Seems like a medical record. The handwriting's barely audible... 

    What? Audible? No, should be \"readable\"

    You can\'t listen to a paper, can you?

    Unless... you\'re not actually looking at it

    Anyways, what does it say?

    \"Patient (unreadable) was admitted with \'loss of consciousness following a motor vehicle accident\'.\"

    \"On examination, the patient was in a comatose state...\"
    """
    scene expression Transform("med", size=(1920, 1080)) at truecenter, dizzy_blur
    play sound "audio/earring.mp3" loop fadeout 1.0
    $ renpy.music.set_volume(5.0, delay=0, channel='sound')

    p1 "Uhhh... Not again..."
    p1 "My head... It hurts..."
    scene expression Transform("recipe", size=(1920, 1080)) at truecenter
    with dissolve
    stop sound
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    p1 "..."
    p1 "Wait, there's still something on the recipe"
    """
    He used to cook for me, and he still would, as always

    Let\'s not lose hope...
    """

    "You put the recipe back"
    scene expression Transform("cooking", size=(1920, 1080)) at truecenter
    with dissolve
    "You seem to remember something"
    "Memory +1"
    $recipe = 1



    play sound "audio/fried.mp3" fadeout 1.0
    scene blisters
    p1"""
    ****! The oil!

    Ah ****, it hurts!

    Almost feels like... needles?

    Why am I thinking of needles...

    """

    "???" """
    Watch your language!

    After all, this is still an end-of-year project!

    You can\'t swear here. It\'s meant for all ages
    """

    p1 "Wow. We even have a \"Swearing Angel \" here. Well, I\'ll behave a little longer"
    scene eat with dissolve
    p1 "Took me quite some efforts to make this. Hope it's good."
    $ game_time += 2
    "Making the meal took you two hours"
    jump eating



    

