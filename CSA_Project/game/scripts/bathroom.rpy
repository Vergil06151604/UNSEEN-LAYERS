label bathroom:
    scene bathroom_bg with dissolve
    p1 "There's even a bathroom here?"
    p1 "Impressive. Well, I do feel my body a bit dirty after all that. "
    menu:
        "What will you do now?"
        "Wash your face and brush your teeth (takes 1 hour)":
            jump wash_simple
            pass
        "I'm feeling in the mood of taking a shower. Gotta get myself nice and clean (takes 2 hours)":
            jump bathing
            pass
        "Oh come on, I've got no time to waste":
            jump home_decision_2

label wash_simple:
    p1 "I haven't got all day here. I'll just make it quick. "
    "You decided to brush your teeth first"
    $ renpy.music.set_volume(2.5, delay=0, channel='sound')
    scene brush with dissolve
    play sound "audio/brush_teeth.mp3"
    "The toothpaste tastes fine. Almost... familiar"
    p1 "Think Emma was the one who wanted this"
    p1 "Wait... Emma?"
    p1 "Who's Emma..."
    p1 "Can't remember."
    p1 "Anyways, doesn't matter"
    play sound "audio/water.pm3"
    scene water with dissolve
    stop sound
    scene wash_face with dissolve
    "You wash your face"
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    scene bathroom_bg with dissolve
    "You spent 1 hour to brush your teeth and wash your face"
    "You feel refreshed"
    $ game_time += 1
    jump home_decision_2

label bathing:
    p1 "Uh, I feel sticky. Better take a bath"
    scene bath with dissolve
    scene fog with dissolve
    "The hot water from the bathtub creats fog in the air"
    scene black with dissolve
    $ renpy.music.set_volume(2.5, delay=0, channel='sound')
    play sound "audio/bathing.mp3"
    "You wash yourself clean"
    scene fog with dissolve
    p1"""
    Uh... I can't recall how I washed myself

    What is wrong with my memory...

    This happens everytime I try to do something here

    Seriously, am I dreaming or something? Or am I dying?
    """
    "???" "Can't say you're wrong, I'm afraid"
    p1"Ah, here we go again"
    "The fog in the bathroom is almost condensing"
    "It hangs in the air, onto the wall, and onto the mirror"
    p1 "Huh? What's on that mirror?"
    "You decided to check the mirror"
    scene mirror at truecenter
    with dissolve
    p1 """
    Come on, that's a stupid question

    Seriously, is there a ghost or something around here?

    Remember what? My name?

    Who would actually forget their own names? That's ridiculous. 

    Wait...

    What's my name again?

    I can't seem to recall...
    """
    $ renpy.music.set_volume(5.0, delay=0, channel='sound')
    scene mirror at truecenter, dizzy_blur
    play sound "audio/earring.mp3" loop fadeout 1.0
    p1"""
    Again? I've had enough of this!

    Uhhh... My head spins...

    I\'m going to...

    (Gasp) I can\'t... breath...

    I\'m... outta here...

    ***, I\'m losing it
    """
    scene black with dissolve
    ".{w=0.5}.{w=0.5}."
    stop sound
    scene bath with dissolve
    "The fog in the bathroom seems to fade out"
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    p1 "This place is definitely driving me crazy"
    "You spent 2 hours on cleaning yourself"
    "Memory +1"
    $ game_time += 2
    $ bath = 1
    jump home_decision_2