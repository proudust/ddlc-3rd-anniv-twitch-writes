# Extend screen navigation
init -10 python hide:
    screens = [s for s in renpy.game.script.namemap.values() if isinstance(s, renpy.ast.Screen)]
    tw_screen = (s for s in screens if s.screen.name == "twitch_writes_menu_button").next()
    tw_button = tw_screen.screen.children[0]

    for navigation in (s for s in screens if s.screen.name == "navigation"):
        vbox = navigation.screen.children[0]
        in_if_not_autoload = vbox.children[0].entries[0][1]
        # Insert the statements of twitch_writes_menu_button after "Load Game"
        in_if_not_autoload.children.insert(2, tw_button)

screen twitch_writes_menu_button:
    # textbutton _("Load Game")
    if main_menu:
        textbutton _("Twitch Writes") action Start("twitch_writes")
    # if _in_replay:

# If the Japanese patch has installed, add history translations
init 10 python hide:
    has_jppatch = "replace_dialogue_to_identifier" in store.__dict__
    if has_jppatch:
        en_strings = renpy.game.script.translator.strings[None]
        tw_label = renpy.game.script.namemap["twitch_writes"];
        for node in (n for n in tw_label.block if isinstance(n, renpy.ast.Translate)):
            old = "{#" + node.identifier + "}"
            if not old in en_strings.translations:
                says = [s for s in node.block if isinstance(s, renpy.ast.Say)]
                # Add affix if the character's dialogue, not the narration.
                affix = '"' if (s.who != None for s in says).next() else ""
                new = "\n".join(affix + s.what + affix for s in says)
                en_strings.add(old, new, (node.filename, node.linenumber))

        jp_strings = renpy.game.script.translator.strings["Japanese"]
        translates = renpy.game.script.translator.language_translates.items()
        for identifier, node in ((i, n) for (i, l), n in translates if l == "Japanese"):
            old = "{#" + identifier + "}"
            if not old in jp_strings.translations:
                new = "\n".join(s.what for s in node.block if isinstance(s, renpy.ast.Say))
                jp_strings.add(old, new, (node.filename, node.linenumber))

# Main
label twitch_writes:
    $ quick_menu = True

    stop music fadeout 2.0
    scene bg club_day
    with dissolve_scene_full
    play music t3

    show monika 4b zorder 3 at f11
    m "Okay, everyone!"
    m "I thought we could try something a little different today."
    m 2a "We're all typically writing poems, but there are other kinds of formats that might be fun to try..."
    show monika zorder 2 at t21
    show natsuki 5t zorder 3 at f22
    n "Yeah, that's a good idea...let's do that."
    show monika 2d zorder 3 at f21
    show natsuki zorder 2 at t22
    m "Huh? Aren't you usually the first to complain about new activities?"
    show monika zorder 2 at t21
    show natsuki 5q zorder 3 at f22
    n "Well, I just..."
    show monika zorder 3 at f21
    show natsuki zorder 2 at t22
    m "Hey, what's that in your pocket?"
    show monika zorder 2 at t21
    show natsuki 4w zorder 3 at f22
    n "Nothing! Can we just do the activity?"
    show monika zorder 2 at t31
    show natsuki zorder 2 at t32
    show sayori 4x zorder 2 at t33
    s "You're hiding something! I wanna know too!"
    s "Is it a present?"
    s 5b "Oh, I bet you're just hiding snacks from me again..."
    show sayori zorder 1 at thide
    show natsuki zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide natsuki
    hide monika

    "All of a sudden, Yuri bursts through the door in a panic."

    show yuri 3p zorder 3 at f11
    y "Everyone—!"
    y 3o "There's..."
    y "Um..."
    show yuri 3p zorder 2 at t21
    show sayori 4m zorder 3 at f22
    s "Oh my gosh!"
    s "It's Monika's birthday!!"
    show yuri zorder 3 at f21
    show sayori zorder 2 at t22
    y "That's—not important right now!"
    y 3o "Wait, I didn't mean it like that..."
    y "It is important, but..."
    show yuri zorder 2 at t31
    show sayori zorder 2 at t32
    show natsuki 42c zorder 3 at f33
    n "Come on! You're going to ruin the surprise if you just say it like that..."
    show sayori zorder 1 at thide
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    hide sayori
    hide natsuki
    hide yuri

    show monika 2e zorder 3 at f11
    m "Aw, you remembered!"
    m "And there's even a surprise for me?"
    show monika zorder 2 at t21
    show natsuki 4d zorder 3 at f22
    n "Yeah!"
    n "Pocket..."
    n 1z "Cupcakes!!"
    show monika zorder 1 at thide
    show natsuki zorder 1 at thide
    hide monika
    hide natsuki

    "Natsuki suddenly pulls a few cupcakes out of her pocket...somehow."
    "It should be impossible, but the cupcakes seem to be in pristine condition, despite being in her pocket."

    show monika 2n zorder 3 at f11
    m "What the heck...?"
    m "How on earth did you do that?"
    show yuri 4a zorder 3 at f21
    show monika zorder 2 at t22
    y "I'm sorry to interrupt again, but...there's something that you really need to know, Natsuki!"
    show yuri zorder 2 at t21
    show natsuki 5c zorder 3 at f22
    show monika zorder 1 at thide
    hide monika
    n "What, what is it?"
    show yuri zorder 3 at f21
    show natsuki zorder 2 at t22
    y "There's..."
    y 3r "There's an impostor among us!"
    show yuri zorder 2 at t21
    show natsuki 4g zorder 3 at f22
    n "Excuse me...?"
    show yuri zorder 2 at t31
    show natsuki zorder 2 at t32
    show sayori 1h zorder 3 at f33
    s "Yuri, are you feeling okey...?"
    show yuri 3o zorder 3 at f31
    show sayori zorder 2 at t33
    y "Of...of course I am."
    y "It's everyone else who's acting strangely, so i just thought..."
    y 4b "I mean...is it just me? Pocket cupcakes?"
    y "Maybe I'm dreaming..."
    show natsuki zorder 1 at thide
    show sayori zorder 1 at thide
    hide natsuki
    hide sayori

    show yuri zorder 2 at t21
    show monika 5 zorder 3 at f22
    m "Oh, Yuri."
    m "You're just worrying too much. Everything is perfectly normal."
    m 1a "I'm so happy that everyone rememberd my birthday."
    show yuri zorder 3 at f21
    show monika zorder 2 at t22
    y "But..."
    y "Sayori was even reading a horror novel earlier. That would never happen..."
    show yuri zorder 2 at t21
    show monika 5 zorder 3 at f22
    m "Yuri..."
    m "Just don't sweat the details, okey?"
    show yuri zorder 2 at t31
    show monika zorder 2 at t32
    show sayori 4r zorder 3 at f33
    s "I love horror!!"
    show yuri 2o zorder 3 at f31
    show sayori zorder 2 at t33
    y "Something's...definitely wrong!"
    y 3v "Sayori is supposed to hate horror."
    y 3g "And Natsuki is usually...not particularly nice..."
    y "And Sayori is usually on the forgetful side, so..."
    y 1f "But more importantly..."
    y "You're acting strange too, Monika!"
    y 2g "You can't just pretend this is all normal behavior."
    y 2q "I feel like I'm going crazy."
    show yuri zorder 2 at t31
    show monika 2a zorder 3 at f32
    m "Well, maybe you are!"
    show yuri 3r zorder 3 at f31
    show monika zorder 2 at t32
    y "No I'm not!"
    y 2h "You're up to something, and I really don't appreciate you gaslighting me like this."
    y 4b "I...really don't like it, so..."
    show yuri zorder 2 at t31
    show monika 2m zorder 3 at f32
    m "But..."
    m "I'm not..."
    show monika zorder 2 at t32
    show sayori 1c zorder 3 at f33
    s "Monika is the President of the Literature Club and her birthday is on September 22nd, which is this day."
    s "The cupcake is not a lie."
    show sayori zorder 1 at thide
    hide sayori
    show natsuki 1a zorder 3 at f33
    n "It's Monika's birthday, so manga isn't literature and also Natsuki is cute."
    show monika 1o zorder 3 at f32
    show natsuki zorder 2 at t33
    m "..."
    show natsuki zorder 1 at thide
    hide natsuki

    show monika zorder 2 at t32
    show sayori 1a zorder 3 at f33
    s "I am Error."
    show sayori zorder 1 at thide
    hide sayori

    play music t9
    show monika 1r zorder 3 at f32
    m "Sigh..."
    m "Fine, I'm sorry."
    m 1i "I didn't mean to make anything weird happen."
    m 1o "We're already halfway through the meeting, and nobody mentioned anything about my birthday, so I thought..."
    m "I felt really depressed and resorted to doing strange things to make myself feel better."
    m 1q "It's wrong and selfish for me to do that. I'm sorry."
    show yuri 3t zorder 3 at f31
    show monika zorder 2 at t32
    y "Monika..."
    show yuri zorder 2 at t31
    show sayori 1g zorder 3 at f33
    s "You really thought we didn't remember...?"
    s 1d "You're our friend, Of course we'd remember."
    show monika 2o zorder 3 at f32
    show sayori zorder 2 at t33
    m "Yeah...you're right."
    m "I'm sorry I didn't trust you."
    m "People just usually don't remember, so..."
    show monika zorder 2 at t32
    show sayori 4g zorder 3 at f33
    s "Really? That's terrible..."
    show monika 2r zorder 3 at f32
    show sayori zorder 2 at t33
    m "It must be because I have a lot of friends, but most of them are kind of on the distant side."
    m 2e "But I should have known better. You've all always been such great friends."
    show yuri zorder 1 at thide
    hide yuri

    show natsuki 3a zorder 3 at f31
    show monika zorder 2 at t32
    n "We do what we can."
    n 5t "Since, you know, you're like..."
    n "Always doing stuff for us, so..."
    n 42c "Well, anyway!"
    n "We might as well reveal the surprise now, I guess."
    show natsuki zorder 1 at thide
    show monika zorder 1 at thide
    show sayori zorder 1 at thide
    hide natsuki
    hide monika
    hide sayori

    "Natsuki signals to Yuri, who starts rustling through her bag."
    "One by one, Yuri pulls out four matching charm bracelets."

    show yuri 4b zorder 3 at f11
    y "Um..."
    y "It's not much, but we made these for you..."
    y 4a "We just thought that since you're the one who brought us all together..."
    y "It would be nice to do something that reminds us of each other."
    y 4b "It's symbolism, so..."
    show yuri 4b zorder 2 at t32
    show sayori 4x zorder 3 at f33
    s "It was Yuri's idea!"
    show yuri 4c zorder 3 at f32
    show sayori zorder 2 at t33
    y "Well—"
    show yuri zorder 2 at t32
    show monika 2e zorder 3 at f31
    m "Oh my gosh..."
    m "Yuri, that's the sweetest thing."
    m "No, it's sweet from all of you. Thank you so much."
    m 2j "You really are the best."
    show monika zorder 2 at t31
    show sayori 1q zorder 3 at f33
    s 1q "No, you."
    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    show sayori zorder 1 at thide
    hide monika
    hide yuri
    hide sayori

    "Monika puts on her bracelet. The other girls do the same."

    play music t8
    show sayori 1x zorder 3 at f11
    s "We all match now!"
    s 4r "Group bracelet hug!!"
    show monika 2n zorder 3 at f31
    show sayori zorder 2 at t32
    m "What dose that even mean...?"
    show monika zorder 1 at thide
    show sayori zorder 1 at thide
    hide monika
    hide sayori

    "Sayori pulls everyone into a hug."

    show monika 2a zorder 3 at f11
    m "This is the best. I'm so happy you all remembered."
    m "I'll wear this every day."
    show monika zorder 2 at t32
    show natsuki 4d zorder 3 at f33
    n "Well, there's still one more thing!"
    n "Mostly from me, but everyone else can take credit too if they want."
    show monika zorder 1 at thide
    show natsuki zorder 1 at thide
    hide monika
    hide natsuki

    "Natsuki dashes into the closet and pulls out a cake that she was hiding on the manga shelf—the one place Monika would never look."
    "For some reason, the cake just says \"Just Monika\"."

    show natsuki 3c zorder 3 at f11
    n "That's weird, I dont remember the cake saying that..."
    show natsuki zorder 2 at t32
    show monika 2l zorder 3 at f31
    m "Whoops...my bad."
    m "Guess I forgot to change that back."
    show monika zorder 1 at thide
    show natsuki zorder 1 at thide
    hide monika
    hide natsuki

    "The girls set up some plates and utensils."
    "Yuri goes to make some tea."

    "{w=2}It's another day at the Literature Club."
    "Another day full of friendship."
    "And literature."

    "{w=2}Happy birthday, Monika and {i}Doki Doki Literature Club!{/i}"

    show monika 2a zorder 3 at f11
    m "And thank all of you, viewing this live, who contributed to the story. And to a good cause."
    m 2n "Wait, what does that even mean...?"
    show monika zorder 3 at f11

    hide screen quick_menu
    show black onlayer overlay as fadeout:
        alpha 0
        linear 2.0 alpha 1.0
    $ pause(2.0)
    return
