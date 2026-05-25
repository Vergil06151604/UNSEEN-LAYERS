label death_scene:
    p1 "Uhhh... My head spins..."
    p1 "I'm losing it"
    "???" "Time, time, time!"
    "???" "I told you that you would not want to find the consequences..."
    "???" "No no no no no no no..."
    "???" "No.{w=0.2}.{w=0.2}."
    scene black with dissolve
    play sound "audio/death_sound.mp3" fadeout 0.5
    "You used up your time, unfortunately"
    "You're dead"
    "Seriously, is 18 hours not enough?"
    "Have you been keep choosing chosen choices so that you can see what happens when you use up all your 18 hours?"
    "Well, hope you saved the game before you decided to randomly choose options to waste the time"
    $ MainMenu(confirm=False)()