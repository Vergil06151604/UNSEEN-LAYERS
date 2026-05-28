label pizza:
    scene pizza_house at force_stretch
    with dissolve
    if dante:
        jump dante_pizza
        pass

    else:
        if pizza_noti == False:
            c "Same as always, right?"
            p1 "What?"
            c "I'm saying, pizza with prosciutto, garlic, and potatoes, no olives, and a strawberry sundae as usual. Right?"
            p1 "Uh... Actually, it's my first time here. "
            scene pizza_chef at force_stretch
            with dissolve
            c "Oh, sorry. Thought you\'re Dante. He loves pizzas and strawberry sundaes. "
            p1 "(thoughts: Dante? I\'m quite sure that\'s not my name. Or anyone I knew.)"
            scene pizza_house at force_stretch
            with dissolve
            c "What would you like?"
            $ pizza_noti = True
            jump pizza_decision
            pass
        else:
            jump pizza_decision


label pizza_decision:
    menu:
        "Do you want to order anything?"
        "Strawberry sundae and a pizza (costs 65 dollars)":
            if cash >= 65 :
                "You got a pizza and a strawberry sundae. "
                $ cash -= 65
                "The strawberry sundae melts fast, so you eat it up quickly"
                menu:
                    "Do you want to eat the pizza, or simply take it away with you?"
                    "I'm hungry. I'm eating it":
                        "You eat the pizza"
                        "Tastes nice"
                    "I'll save it for later, I suppose. Might be useful":
                        "You put the pizza into your pocket"
                        "Yes... your pocket"
                        "It\'s quite large. You barely feel it in your pants"
                        "Pizza +1"
                        $ pizza += 1
                        jump pizza_decision
                        pass
            else:
                c "Not enough cash, I'm afraid. "
                if not game1:
                    c "The bookstore owner loves some kind of games, maybe you should find him"
                    c "If you answer his questions correctly, he might actually award you with some sorta thing!"
                    p1 "Thanks... I guess. "
                    c "Oh, by the way..."
                if not laby_quest:
                    c "If you're an adventure kind of guy, maybe try the labyrinth. "
                    c "It's dangerous, but might be rewarding. Just try not to be killed. "
                    p1 "Thank you. I'll think about that. "
                jump pizza_decision
                pass
        "Just pizza, please. (costs 50 dollars)":
            if cash >= 50:
                "You got a pizza. "
                $ cash -= 50
                menu:
                    "Do you want to eat the pizza, or simply take it away with you?"
                    "I'm hungry. I'm eating it":
                        "You eat the pizza"
                        "Tastes nice"
                    "I'll save it for later, I suppose. Might be useful":
                        "You put the pizza into your pocket"
                        "Yes... your pocket"
                        "It\'s quite large. You barely feel it in your pants"
                        "Pizza +1"
                        $ pizza += 1
                        jump pizza_decision
                        pass
            else:
                c "Not enough cash, I'm afraid. "
                if not game1:
                    c "The bookstore owner loves some kind of games, maybe you should find him"
                    c "If you answer his questions correctly, he might actually award you with some sorta thing!"
                    p1 "Thanks... I guess. "
                    c "Oh, by the way..."
                if not laby_quest:
                    c "If you're an adventure kind of guy, maybe try the labyrinth. "
                    c "It's dangerous, but might be rewarding. Just try not to be killed. "
                    p1 "Thank you. I'll think about that. "
                jump pizza_decision
                pass
        "No thanks, I'm good.":
            "You decided to save some money. "
            jump street_choice


label dante_pizza:
    scene pizza_chef with dissolve
    o1 "Dante! Haven\'t seen you in a while!"
    show dante_pic at right
    with dissolve
    d "Yeah. I kinda miss the food here."
    o1 "Just as usual, right?"
    o1 "Oh, you got any cash? Thought you\'re broke by now."
    d "Well, this kid\'s paying this time"
    o1 "Really? Guess I don\'t have to worry about paying anymore."
    o1 "pizza with prosciutto, garlic, and potatoes, no olives, and a strawberry sundae as usual."
    o1 "That\'ll be 65 dollars in total."
    if cash >= 65:
        o1 "Thank you. "
        scene black at force_stretch
        with dissolve
        "After a while..."
        scene pizza_house at force_stretch
        with dissolve
        show dante_pic at right
        with dissolve
        d "Good as always. Thanks for the treat, kid."
        p1 "You\'re welcome"
        d "Alright. Let\'s get straight to the business."
        d "Now, let\'s get to the altar."
        p2 "No no no no no!"
        p2 "It shouldn\'t have been this way!"
        d "That little voice in your head is talking again, right?"
        d "Don\'nt worry. We\'ll get rid of him quickly."
        hide dante_pic with dissolve
        scene altar at force_stretch
        with dissolve
        p1 "We\'re here. "
        scene altar_yamato at force_stretch
        with dissolve
        scene altar_dante1 at force_stretch
        with dissolve
        d "You ready?"
        p1 "Yeah."
        d "Through the power of the yamato, I will seperate you and that voice inside your head"
        d "And that voice is also something I\'ve been trying to eliminate all this time."
        p1 "Why is the shape of your sword different?"
        d "This means that I\'m getting close to finishing my job."
        d "Here goes nothing"
        scene altar_dante2 at force_stretch
        with dissolve
        "You do not feel pain. Nor does blood flow from your body"
        p1 "Feels... strange..."
        p2 "No...."
        "You do not hear that voice anymore."
        d "Good luck, kid."
        scene white_screen at force_stretch
        with dissolve
        p1 "Hope this is truely the end..."
        scene wake_up at force_stretch
        with dissolve
        "True Ending Unlocked"
        "Congradulations! You beat the game!"
        return
    else:
        o1 "The stationary store\'s owner told me that he\'s got one more game now."
        o1 "Maybe try to find him to get another prize."
        p1 "Thanks. Going right away."
        jump street_choice
        



                        

