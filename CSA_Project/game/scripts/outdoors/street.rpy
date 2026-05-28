label street_choice:
    scene street at force_stretch
    with dissolve
    menu:
        "What will you do now?"
        "Go to the pharmacy":
            jump pharmacy
            pass
        "Go to the hardware store":
            jump hardware
            pass
        "Go to the stationary store (which also sells books)":
            jump stationary
            pass
        "Go to the pizza house":
            jump pizza
            pass
        "Explore the labyrinth between the pharmacy and the stationary store (might be dangerous)" if not laby:
            jump labyrinth
            pass
        "Walk forward into the black smoke ahead (you should be prepared for this)" if not dante:
            jump dante
            pass
        "Walk through the black smoke when Dante\'s waiting at the pizza house (you might wanna save the game befor choosing this)" if dante:
            jump fake_ending2


label fake_ending2:
    scene black_fog at force_stretch
    with dissolve
    "You walk to the end of the street"
    scene fog_closeup at force_stretch
    with dissolve
    p1 "I\'m tired of your lies, you parasite!"
    p2 "What are you talking about?"
    scene altar at force_stretch
    with dissolve
    p1 "I know what you are. You\'re just another personality in my body, trying to get me into destroying my own mental world"
    p2 "But... what good will that do for me?"
    p1 "So that you can take over my body! I\'m still here after gaining my memory because I still need to ged rid of you!"
    p2 "Well then, poor guy, what do you plan to do, huh? Ask Dante to kill me for you?"
    p1 "I\'m gonna do it myself."
    scene altar_yamato2 at force_stretch
    with dissolve
    p1 "With the power of the Yamato, I shall seperate you from myself!"
    p2 "Trust me, you don\'nt wanna do that."
    p1 "No more lies!"
    scene fake_ending2 at force_stretch
    with dissolve
    "You thrust the yamato into your body. It slices in as if cutting into some condensed air, smooth and sharp."
    "The pain sends you almost suffocating"
    p2 "Foolishness!"
    scene killed at force_stretch
    with dissolve
    "You killed yourself with the Yamato"
    "You failed to trigger its power to seperate yourself from the other personality."
    p2 "No mere human can harness the full potential of the Yamato. I warned you."
    return



