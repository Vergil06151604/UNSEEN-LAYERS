label stationary:
    scene stationary_store at force_stretch
    with dissolve
    show owner at center_bottom
    with dissolve
    if yamato and not yamato_noti:
        o1 "Ah, I see you\'ve passed through the labyrinth"
        o1 "And you came back alive!"
        o1 "Congradulations. GuessI'll give you something in return"
        o1 "Henre's 100 dollars. Consider it a gift. It\'s been so long since the last time seeing someone beating the labyrinth."
        p1 "Last time?"
        o1 "Yeah, last time. If I recall correctly, it was someone who looked just like you. But he gave me a completely different feeling."
        p1 "Interesting..."
        p2 "Don\'t listen to him. Everything here wants to drag you down"
        o1 "So... you can ask some questions. I'll try my best to answer them"
        $ yamato_noti = True
        jump qna
    
    else:
        o1 "Can I help you?"
        menu:
            "What will you do?"
            "Play the game (game1) with him and win a prize" if not game1:
                jump game_1
                pass
            "Play the game (game2) with him and win a prize" if game1 and yamato and dante and not game2:
                jump game_2
                pass
            "Buy information for 30 dollars (not reccommended)" if not yamato:
                if cash >= 50:
                    "You spent 50 dollars on some questions"
                    $ cash -= 50
                    o1 "You\'d better note them down, for that I\'m not telling you a second time about these things"
                    jump qna
                    pass
                else:
                    o1 "Sorry, I guess you do not have enough money for this."
                    jump stationary
                    pass
            
            "Give him a pizza" if game1 and not pizza_quest:
                if pizza >= 1:
                    "You gave the shop owner a pizza"
                    $ pizza -= 1
                    o1 "Thanks! Tastes great"
                    o1 "Remember our deal, that I get you information about the labyrinth?"
                    o1 "Listen carefully. You might wanna note it down"
                    p1 "I\'m all ears"
                    o1 "W E W E W W E"
                    p1 "Uh, what?"
                    p2 "Told you he\'s not trustworthy"
                    o1 "Just a reminder: on a map, north is forward, south is backwards, west is going left and east is going right"
                    o1 "Should be quite useful in the labyrinth"
                    o1 "So I\'m gonna say this one more time:"
                    o1 "W E W E W W E"
                    p1 "Right... thanks"
                    $ pizza_quest = True
                    jump stationary
                    pass
                else:
                    p1 "I don\'t have a pizza... Better go get one now"

            "Ask about information for free" if laby_quest:
                jump qna
                pass
            "No thanks. I\'m good. ":
                hide owner with dissolve
                jump street_choice





label game_1:
    o1 "Great. I\'ve been waiting for games like this for a long time!"
    menu:
        "Question 1: I have many keys, but I cannot open doors; I have space but no actual room; I can help you escape but there\'s no way to go to. What am I?"
        "A grand piano":
            o1 "I'm afraid that was wrong. Next time maybe"
            jump stationary
            pass
        "A computer keyboard":
            o1 "Correct!"
            menu:
                "Question 2: Why did the smartphone finally decide to visit the eye doctor and ask for a pair of glasses?"
                "Its screen protector was too scratched to see.":
                    o1 "I'm afraid that was wrong. Next time maybe"
                    jump stationary
                    pass
                "It wanted to look like a \"smart\" device":
                    o1 "I'm afraid that was wrong. Next time maybe"
                    jump stationary
                    pass
                "It had completely lost all its contacts.":
                    o1 "Correct!"
                    menu:
                        "Question 3: A pilot is flying a small commercial plane. Suddenly, a storm hits, and the plane crashes exactly on the border line between the United States and Canada. The wreckage is perfectly split 50/50 between the two nations. Where do they bury the survivors?"
                        "The United States":
                            o1 "I'm afraid that was wrong. Next time maybe"
                            jump stationary
                            pass
                        "Canada":
                            o1 "I'm afraid that was wrong. Next time maybe"
                            jump stationary
                            pass
                        "The country of their citizenship":
                            o1 "I'm afraid that was wrong. Next time maybe"
                            jump stationary
                            pass
                        "They don\'t. ":
                            o1 "Correct! You do not bury survivors, do you? Only the dead gets to rest in peace"
                            o1 "Well, that was fun. Here\'s your money. "
                            $ game1 = True
                            "You get 50 dollars"
                            o1 "I\'ll let you know if I\'ve got another game to play"
                            o1 "Oh, by the way, you really should think before you spend it somewhere else!"
                            o1 "Such opportunities are really rare. "
                            $ cash += 50
                            o1 "By the way, would you buy me a pizza?"
                            o1 "I know it\'s not a reasonable request, but I\'d really like one"
                            o1 "I\'ll get you some information about the labyrinth if you do. "
                            jump street_choice
                            pass

                "It was spending too much time on dark mode.":
                    o1 "I'm afraid that was wrong. Next time maybe"
                    jump stationary
                    pass
        "A locksmith\'s shop":
            o1 "I'm afraid that was wrong. Next time maybe"
            jump stationary
            pass
        "A map of the galaxy":
            o1 "I'm afraid that was wrong. Next time maybe"
            jump stationary
            pass

label game_2:
    o1 "Alright. Let's play the game! I've found a new one. Should be fun"
    menu:
        "Question: I have a perfectly round eye, but I am completely blind. I have a long, sharp, and slender body, but I have no legs. My only job is to follow a lead wherever it takes me, often mending things along the way. What am I?"
        "A cyclops":
            o1 "I'm afraid that was wrong. Next time maybe"
            jump stationary
            pass
        "A hurricane":
            o1 "I'm afraid that was wrong. Next time maybe"
            jump stationary
            pass
        "A sewing needle":
            o1 "Correct!"
            menu:
                "Question: I am completely invisible, yet I hold billions of videos, songs, and personal memories. I don't have a physical home on earth, but millions of people pay a monthly fee just to keep their stuff inside me. What am I?"
                "A bank vault":
                    o1 "I'm afraid that was wrong. Next time maybe"
                    jump stationary
                    pass
                "Cloud storage":
                    o1 "Correct!"
                    menu:
                        "Question: What kind of \"band\" has multiple members, never plays a single note of music, is incredibly flexible, and is mostly found working inside an office desk drawer?"
                        "A rock band":
                            o1 "I'm afraid that was wrong. Next time maybe"
                            jump stationary
                            pass
                        "A wedding band":
                            o1 "I'm afraid that was wrong. Next time maybe"
                            jump stationary
                            pass
                        "A rubber band":
                            o1 "Correct!"
                            o1 "Well that was fun. Now take your prize and get out of this world!"
                            "You get 65 dollars"
                            $ cash += 65
                            $ game2 = True

                            p1 "What? You knew?"
                            o1 "Of course I do! Good luck!"
                            p2 "DO NOT LISTEN TO HIM! Damnit, why won\'t you listen?"
                            p1 "I have my own judges."
                            jump street_choice
                        "A banned book band":
                            o1 "I'm afraid that was wrong. Next time maybe"
                            jump stationary
                            pass
                "A magician\'s hat":
                    o1 "I'm afraid that was wrong. Next time maybe"
                    jump stationary
                    pass
                "A time capsule":
                    o1 "I'm afraid that was wrong. Next time maybe"
                    jump stationary
                    pass
        "A compass":
            o1 "I'm afraid that was wrong. Next time maybe"
            jump stationary
            pass

label qna:
    menu:
        "What will you ask?"
        "About Dante":
            o1 """
            Ah, Dante. 

            He\'s a man who always wears a large red coat, and carries his sword around. 

            People call him the \"Legendary Devil Hunter\". He basically kills every single demon he sees

            But actually, he\'s half a demon himself. 

            He is the son of the Legendary Dark Knight Sparda, which is a demon. 

            Demonic power courses through his veins, which is the very reason that he\'s so tough

            But who would have guessed that he\'s got quite a taste of pizza and strawberry sundae...

            I bet you\'ve met him already, haven\'t you?
            """

            p1 "So, the name\'s Dante..."
            $ dante_name = "Dante"
            p1 "Interesting."
            jump qna
            pass
        "About the Yamato":
            o1 """
            Of course you\'ll have question about that!

            After all, it\'s in the room at the end of the labyrinth

            Well, let\'s just say that this weapon is filled, or even constructed, by pure demonic power

            This devil sword belongs to Vergil, the twin brother of Dante. 

            The twins have demonic powers flowing in their veins, making them almost immune to ordinary means of attack.

            However, the Yamato is special.

            It has the power to \"seperate\" everything, even concepts such as time and space, or even souls

            Vergil used it to open portals as a means of quick travel. 

            He also splitted his demonic self from his human self once. 

            Theoretically, it can cut through everything. Even Dante. 
            """
            p2 "Told you that you can use it like a tool"
            jump qna
            pass
        "About this place":
            o1 """
            Well... Let\'s just say that you\'re close to the end
            """
            jump qna
            pass
        "Nevermind":
            jump stationary
        

