default first_time = True
label hardware:
    if first_time:
        scene hardware_pipe at force_stretch
        with dissolve
        "You walk inside the hardware store."
        menu:
            "You see a pipe on the table of the store. Will you take it?"
            "Take it. Might be useful as a weapon.":
                $ first_time = False
                scene hardware_store at force_stretch
                with dissolve
                "The moment you take the pipe, the appearance of the store shifts a little. "
                p1 "Kinda strange... But considering that it\'s somewhere like my mental world, it can make sense."
                "The pipe feels solid in your hands."
                $ pipe = True
                jump hardware_after
                pass
    else:
        label hardware_after:
            scene hardware_store at force_stretch
            with dissolve
            "You look around the store. "
            "Nothing useful here."
            menu:
                ""
                "Leave":
                    jump street_choice

