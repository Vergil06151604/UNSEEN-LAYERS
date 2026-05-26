# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

# 1. 首先定义一个名为 "p_shake" 的抖动效果

# 1. 初始化你的 time 变量（默认从 0 开始）
default game_time = 0
default memories = 0
default power = 0
default eyecheck = 0
default recipe = 0
default bath = 0
default window_noti = False
default pc_noti = False
default car = 0
default sleep = 0
default key = False
default is_dead = False



init python:
    # 2. 定义检测函数
    def check_time_trigger():
        # 如果当前正在进行剧情，且变量超过了 18
        # 🌟 核心防空门：如果游戏还在初始化阶段，或者全局变量仓库里压根还没诞生 game_time
        # 就直接跳出函数（return），什么都不做。直到游戏正式开始后再正式跑它。
        if renpy.is_init_phase() or 'game_time' not in globals():
            return
        # 如果当前正在进行剧情，且变量超过了 10
        if 'is_dead' in globals() and is_dead:
            return
        if game_time > 18 and renpy.is_init_phase() == False:
            global is_dead
            is_dead = True
            # 强制跳转到名为 "death_scene" 的标签+++++++++
            renpy.jump("death_scene")

    # 3. 将这个函数注册到 Ren'Py 的底层计时器中（每隔大约 0.02 秒自动检测一次）
    config.periodic_callback = check_time_trigger

transform dizzy_blur:
    # 初始状态：完全清晰
    blur 0
    
    # 用 1.5 秒的时间，慢慢变得非常模糊（数值 10-15 左右就很有眩晕感了）
    linear 1.5 blur 12
    
    # 再用 1.5 秒的时间，慢慢恢复清晰
    linear 1.5 blur 0
    
    # 循环这个过程，模拟持续的眩晕感
    repeat

transform p_shake:
    # xoffset 和 yoffset 分别控制图片偏离原位置的像素距离
    # linear 0.04 表示在 0.04 秒内平滑移动到该位置
    linear 0.04 xoffset 8 yoffset -8
    linear 0.04 xoffset -8 yoffset 8
    linear 0.04 xoffset -5 yoffset -5
    linear 0.04 xoffset 5 yoffset 5
    linear 0.04 xoffset 8 yoffset -8
    linear 0.04 xoffset -8 yoffset 8
    linear 0.04 xoffset -5 yoffset -5
    linear 0.04 xoffset 5 yoffset 5
    linear 0.04 xoffset 0 yoffset 0  # 回归原点
    
    # 控制抖动次数。如果要一直抖动，直接写 repeat 即可
    repeat 4 

transform bg_centered:
    # 1. 确保大图的中心锚点对齐
    xanchor 0.5 yanchor 0.5
    
    # 2. 将图片挂在屏幕的正中心
    xpos 0.5 ypos 0.5
    
    # 3. 稍微放大图片 (关键步骤！)
    # 放大 10% (1.10) 可以覆盖 ±10 像素级别的抖动幅度。
    # 如果抖动幅度更大（例如 xoffset 50），就需要放大更多（例如 1.25）。
    
    # 4. 在不变上述设置的前提下，应用 'p_shake' 效果

transform force_stretch:
    size (1920, 1080)
    truecenter

define p1 = Character("Player")
define flag = 0
image box:
    "images/open the box.jpg"
    zoom 1.93

image light:
    "images/light.png"
    zoom 1.5

image white_screen:
    "images/white_screen.png"
    zoom 1.5

image ceiling:
    "images/ceiling.png"
    zoom 1.5
image room:
    "images/start room.jpg"
    zoom 2
image black:
    "images/black_background.png"
    zoom 1.7

image kitchen:
    "images/kitchen.png"
    zoom 1.5

image cooking:
    "images/cooking.png"
    zoom 1.5

image wash:
    "images/washing_img.png"
    zoom 1.5

image wash_02:
    "images/washing_abnormal.png"
    zoom 1.5

image blisters:
    "images/blisters.png"
    zoom 1.5

image eat:
    "images/food.png"
    zoom 1.5

image recipe_:
    "images/recipe.png"
    zoom 1.5

image med:
    "images/med_record.png"
    zoom 1.5

image win:
    "images/window.png"
    zoom 1.5

image win_02:
    "images/window_light.png"
    zoom 1.5

image win_fin:
    "images/window_clap.png"
    zoom 1.5

image strange_car:
    "images/car.jpg"
    zoom 1.84

image wash_face:
    "images/wash.png"
    zoom 1.5

image fog:
    "images/fog.png"
    zoom 1.5

image brush:
    "images/brush.png"
    zoom 1.5

image bath:
    "images/bath.png"
    zoom 1.5

image bathroom_bg:
    "images/bathroom.png"
    zoom 1.5

image water:
    "images/water.png"
    zoom 1.5

image mirror:
    "images/mirror.png"
    zoom 1.5

image door_1:
    "images/door.png"
    zoom 1.5

image door_closeup:
    "images/door_closeup.png"
    zoom 1.5

image open_1:
    "images/open_1.png"
    zoom 1.5

image open_2:
    "images/open_2.png"
    zoom 1.5

image pills_door:
    "images/pills_door.png"

image pills_light:
    "images/pills_light.png"

image key:
    "images/key.png"

image key_grip:
    "images/key_grip.png"

image key_light:
    "images/key_light.png"

image grip:
    "images/grip.png"

image wake_up:
    "images/wake_up.png"

image bedroom:
    "images/room.png"
    zoom 1.5

image pc:
    "images/pc.png"
    zoom 1.5

image lie_down:
    "images/lie_down.png"
    zoom 1.5

image sleep:
    "images/sleep.png"
    zoom 1.5

image sea:
    "images/sea.png"
    zoom 1.5

image onwater:
    "images/onwater.png"
    zoom 1.5

image underwater:
    "images/underwater.png"
    zoom 1.5

image pills_get:
    "images/pills_get.png"
    zoom 1.5
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.



    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    scene black
    p1 "Where... am I?"
    p1 "I\'m... lying on something?"
    p1 "Darkness..."
    p1 "Uh... Can't breath..."
    p1 "(have to get out of here)"
label choice1:
    menu:
        "What will you do?"
        "Try to explore the surroundings":
            pass
        "Do nothing":
            "You lie there for a few minutes"
            "Nothing happens..."
            jump choice1
    
    "You reach out your hand and touch something above you, smooth and heavy"
    p1 "A lid...?"
    """
    You push the lid with all the strength you've got

    Nothing happens...

    ...

    Am I gonna stay here forever?

    ...
    """
    play sound "audio/earthquake.mp3"
    scene black at bg_centered, p_shake
    p1 """
    The heck?

    Was that an earthquake?

    Hope this thing is concrete enough to not get me squashed like a pancake.
    """
    play sound "audio/earthquake.mp3"
    scene black at bg_centered, p_shake

    p1"""
    Again?

    Oh, it stops. Great. 
    """

    "You feel the lid above you loosens"
    "(try to push the lid again)"
    "With great effort, you manage to slowly lift the lid"
    

    scene box with dissolve
    with Pause(0.5)
    scene light with dissolve
    with Pause(0.5)
    scene white_screen with dissolve
    with Pause(0.5)
    scene ceiling with dissolve
    pause
    p1 "I should get up..."
    scene room
    p1 "A coffin?"
    p1 "Guess that's where I was lying in. No wonder that was so heavy. "

    scene room at dizzy_blur
    play sound "audio/earring.mp3" loop fadeout 1.0
    $ renpy.music.set_volume(5.0, delay=0, channel='sound')
    p1"""
    Uhhh... What's going on?
    
    My head... It hurts...

    I'm gonna...
    """
    "???" "Who {w=0.5} Are {w=0.5} You?"
    "???" "Five {w=0.5} Memories..."
    "???" "18 hours... left..."
    scene room
    stop sound
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    "You have 18 more hours"
    "Try to find at least 5 memories"
    "???" "What? Consequences for not doing that?"
    "???" "You don't probably wanna find out.{w=0.2}.{w=0.2}."
    
    call home_decision_1 from _call_home_decision_1


    # This ends the game.

    return
