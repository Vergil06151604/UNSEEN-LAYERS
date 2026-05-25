label window:
    $ window_noti = True
    scene win with dissolve
    "You turn around and look at the window"
    p1 "Strange... Can't see anything outside"
    scene win_02 with dissolve
    p1 "What's going on?"
    p1 "My eyes..."
    scene win_fin with dissolve
    play sound "audio/clap.mp3"
    p1 "No... Someone... There?"
    scene white_screen with dissolve
    play sound "audio/earring.mp3" volume 5.0
    "???" "Pupillary light reflex is present. He\'s still alive."
    stop sound
    play sound "audio/laugh.mp3"
    p1 "Who\'s laughing... "
    "You try to close your eyes to block the light"
    "But it feels like something's forcing you to open them"
    scene win with dissolve
    stop sound
    p1 "I've had enough of this. "
    "You seem to recall something"
    "Memory +1"
    $ eyecheck = 1
    "1 hour has passed"
    $ game_time += 1
    jump home_decision_2

    