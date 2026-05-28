label dante:
    scene black_fog at force_stretch
    with dissolve
    "You approach the very end of the street"
    "All you can see is the black smoke up ahead"
    p2 "Yes! Get in there!"
    p2 "If you get to the other side, all of this shall be over!"
    label fog_decision:
        menu:
            "What will you do?"
            "Walk forward":
                jump fight
                pass
            "Use items":
                menu:
                    ""
                    "Use the potion you got from the pharmacy" if potion:
                        jump invisible
                        pass
                    "Eat the pizza" if pizza:
                        if yamato:
                            show dante_pic at right
                            with dissolve
                            "You eat the pizza"
                            "The aroma of the pizza seems to atract someone..."
                            d "Here you are. Well, you look better than before. That sword might actually help."
                            d "The pizza smells nice. So... if you're buying me one, I might be able to help you."
                            d "After all, you can\'t use that sword by yourself"
                            p2 "No no no no no no no!"
                            p2 "Why is him offering help?"
                            p2 "This shouldn\'nt have happened..."
                            p1 "(to ???) What are you talking about?"
                            menu:
                                "Will you buy him pizza?"
                                "Sure, I guess... He doesn\'t seem so hostile by now":
                                    $ dante = True
                                    d "Great. I\'m almost broke by now."
                                    jump pizza
                                    pass
                                "Seriously? No of course":
                                    d "Well then... Just saying. Maybe you should stop listening to that sound in hour head."
                                    p1 "What? How do you..."
                                    p2 "He is only trying to take advantage of you!"
                                    p2 "Seriously, you're gonna abandon me?"
                                    d "It\'s your own choice, pal. I\'ll see you around"
                                    hide dante_pic with dissolve
                                    jump fog_decision
                                    pass
                    "Return":
                        jump fog_decision
                        pass
            "Go back":
                "You decided that it\'s not yet time for you to pass through the smoke."
                p2 "I\'m dissappointed. Why you gotta be so cowardice every time?"
                jump street_choice

default rounds = 0

label fight:
    scene dante_smoke at force_stretch
    with dissolve
    play music "audio/boss_music.mp3"
    d "Hey pal, it\'s pretty dangerous up front. You might wanna back down."
    p2 "Ah... It\'s him! Come on, try to kill him! Else he\'ll kill you!"
    p1 "I\'m just taking a closer look. What\'s up front?"
    d "Well... That\'s not the first time I heard something like this."
    d "Seriously, you should back down. It\'ll be best for both of us"
    label fight_choices:
        scene dante_smoke at force_stretch
        with dissolve
        menu:
            "What will you do now?"
            "Attack":
                jump attack_choices
                pass
            "USe item":
                jump item_choices
                pass
            "Flee":
                "You decide to flee the battle. "
                p1 "Don\'t think I can get rid of him yet..."
                p2 "What are you doing? Seriously?"
                d "Good choice buddy. Seems like you\'re not completely corrupted yet."
                $ rounds = 0
                stop music
                jump street_choice

label item_choices:
    menu:
        "What will you use?"
        "Use the potion found at the pharmacy" if potion:
            "You use the potion"
            "Your body\'s shape fades..."
            "You become invisible"
            d "Well... I don\'t actually need to see you if you\'re doing that right in front of my face."
            d "Come on. You can\'t be serious."
            jump fight_choices
            pass
        "Eat the pizza" if pizza:
            "You eat the pizza"
            "Tastes good"
            p2 "Seriously? Eating it NOW?"
            d "Smells nice. I\'d like to have one as well when I\'ve got time."
            d "But I\'m kinda broke right now."
            jump fight_choices
            pass
        "Return":
            jump fight_choices

label attack_choices:
    scene dante_smoke at force_stretch
    with dissolve
    if rounds == 3:
        d "Sorry man. I don\'t think you\'re sane enough to go back to normal."
        d "Though I hate to do this, it\'s my job."
        scene dante_fall at force_stretch
        with dissolve
        "You fall back on the ground"
        p1 "No no no no no..."
        scene fall_gun at force_stretch
        with dissolve
        p1 "Wait, we can talk..."
        d "No, we can\'t."
        scene fall_shoot_death at force_stretch
        with dissolve
        play sound "audio/gunshot.mp3"
        scene killed at force_stretch
        with dissolve
        stop music
        stop sound
        d "Uh... He surely has a scent of demon on him."
        d "Not sure why... But killing him should be the right choice."
    menu:
        "What will you do?"
        "Punch him":
            scene punch_dante at force_stretch
            with dissolve
            p1 "Aaaaaah!"
            "You punch him at the chest with all your might"
            "But he doesn\'t  even flinch"
            d "Well, either you give up, or you really should try harder than that. My patience\'s limited."
            $rounds += 1
            jump attack_choices
        "Insult him and try to attack him verbally":
            p2 "Let me do this. "
            "You feel that someone else is speaking for you"
            "Your lips are moving, but you\'re not the one who\'s actually talking"
            p2 "Hey isn\'t this the guy who got his family killed?"
            p2 "You couldn\'t save your mother. You couldn\'nt save ANYONE!"
            p2 "And your brother. You KILLED him yourself!"
            scene dante_angry at force_stretch
            with dissolve
            d "Your condition\'s even worse than I thought."
            p2 "The hell you\'re talking about? You might as well go to..."
            scene rebellion_thrust at force_stretch
            with dissolve
            "Dante thrusts his blade into your throat"
            scene rebellion_death at force_stretch
            with dissolve
            d "Sorry man, I don\'nt think you\'re the one in control of the body anymore."
            p1 "(What?)"
            p2 "Grrrrk..."
            scene killed at force_stretch
            stop music
            with dissolve
            d "That was... unfortunate. "
            d "Thought you were in a better shape than that."
            return
        "Attack him with a pipe" if pipe:
            scene pipe_attack at force_stretch
            with dissolve
            "You pull out the pipe you collected at the hardware store"
            d "Ha. I wouldn\'t do this if I were you"
            scene white_screen at force_stretch
            with Fade(0.1, 0.1, 0.1, color="#FFFFFF")
            scene pipe_shatter at force_stretch
            "Before you make any move, [dante_name] steps one step closer and slices the pipe into pieces with his sword"
            p1 "Gesus Christ!"
            p1 "What the hell was that?"
            $ rounds += 1
            $pipe = False
            jump attack_choices
            pass
        "Try to kill him using the Yamato":
            p1 "This shall work. The stationary store owner told me that this can harm Dante"
            d "Still wanna fight?"
            $ rounds += 1
            scene dante_yamato at force_stretch
            with dissolve
            p1 "Take this!"
            "You thrust the Yamato at him with full strength"
            scene thrust_dante at force_stretch
            with dissolve
            "But he didn\'t even flinch"
            d "Nice try, I should say. Didn\'t know you had the guts to get through the labyrinth."
            p1 "What?"
            scene dante_fall at force_stretch
            with dissolve
            "You fall back onto the ground, watching [dante_name] pulling yamato out of his chest, and the wound almost heals instantly"
            d "Sorry pal, I jut gotta do my job."
            scene fall_gun at force_stretch
            with dissolve
            play sound "audio/gunshot.mp3"
            scene fall_shoot_death at force_stretch
            with dissolve
            scene killed at force_stretch
            with dissolve
            stop sound
            stop music
            "You\'re dead. "
            d "You\'ve got some guts. Should\'da known better of your own strengths."
            return

label invisible:
    "Your body\'s shape fades in the air"
    "You become invisible"
    scene dante_smoke at force_stretch
    with dissolve
    p2 "He doesn\'t seem to be seeing you. The potion works!"
    "You sneak by him slowly and silently"
    scene fog_closeup at force_stretch
    with dissolve
    scene altar at force_stretch
    with dissolve
    jump altar_decision