# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narratorr = Character("", color = "#ffffff", what_text_align=0.5, what_xalign=0.5, who_xalign=0.5)
define Winston = Character("Winston", color = '#5e77bd', what_text_align=0.5, what_xalign=0.5, who_xalign=0.5)
define Yuki = Character("Yuki" , color = "#dd5757", what_text_align=0.5, what_xalign=0.5, who_xalign=0.5)
define Rusty = Character("Rusty" , color = "#298d2e", what_text_align=0.5, what_xalign=0.5, who_xalign=0.5)
define Tax = Character("Tax evasion" , color = "#fff240", what_text_align=0.5, what_xalign=0.5, who_xalign=0.5)
define Flop = Character("Flop", color="#93c480", what_text_align=0.5, what_xalign=0.5, who_xalign=0.5)
define Cerber_silly = Character("Cerber" , color = "#854f2b", what_text_align=0.5, what_xalign=0.5, who_xalign=0.5)
define Cerber_fellow = Character("Cerber" , color = "#724323", what_text_align=0.5, what_xalign=0.5, who_xalign=0.5)
define Cerber_evil = Character("Cerber" , color = "#50301a", what_text_align=0.5, what_xalign=0.5, who_xalign=0.5)
define everyone = Character("EVERYONE HERE" , color = "#d62ca3", what_text_align=0.5, what_xalign=0.5, who_xalign=0.5)
define golden = Character("g")

image reconnecting_happy:
    Text("RECONNECTING", size=30, color="#ce8d93", bold=True, outlines=[(2, "#ffffff", 0, 0)])
    
    parallel:
        matrixcolor HueMatrix(0)
        linear 4.0 matrixcolor HueMatrix(360) 
        repeat

    parallel:
        ease 0.6 ypos -6
        ease 0.6 ypos 0
        repeat

    parallel:
        ease 1.2 zoom 1.05
        ease 1.2 zoom 0.95
        repeat

    parallel:
        ease 1.0 rotate 6
        ease 1.0 rotate -6
        repeat


image reconnect:
    Text("RECONNECT", size=30, color="#c25c66", bold=True, outlines=[(2, "#ffffffff", 0, 0)])
    
    parallel:
        matrixcolor HueMatrix(0)
        linear 4.0 matrixcolor HueMatrix(360) 
        repeat

    parallel:
        ease 0.6 ypos -6
        ease 0.6 ypos 0
        repeat

    parallel:
        ease 1.2 zoom 1.25
        ease 1.2 zoom 0.75
        repeat

    parallel:
        ease 1.0 rotate 3
        ease 1.0 rotate -3
        repeat

image reconnected:
    Text("RECONNECTED", size=30, color="#fa5667", bold=True, outlines=[(2, "#ffffffff", 0, 0)])
    
    parallel:
        matrixcolor HueMatrix(0)
        linear 4.0 matrixcolor HueMatrix(360) 
        repeat

    parallel:
        ease 0.6 ypos -6
        ease 0.6 ypos 0
        repeat

    parallel:
        ease 1.2 zoom 1.08
        ease 1.2 zoom 0.92
        repeat

    parallel:
        ease 1.0 rotate 45
        ease 1.0 rotate -45
        repeat

image reconnector:
    Text("RECONNECTOR", size=30, color="#fa5667", bold=True, outlines=[(2, "#ffffffff", 0, 0)])
    
    parallel:
        matrixcolor HueMatrix(0)
        linear 4.0 matrixcolor HueMatrix(360) 
        repeat

    parallel:
        ease 0.6 ypos -6
        ease 0.6 ypos 0
        repeat

    parallel:
        ease 2.2 zoom 1.8
        ease 2.2 zoom 0.2
        repeat

    parallel:
        ease 2.0 rotate 180
        ease 2.0 rotate -180
        repeat

image reconnecting_final = Transform("reconnecting_happy", yoffset=-105)
image reconnectp = Transform("reconnect",yoffset = - 105 )
image reconnectedp = Transform("reconnected", yoffset = -105)
image reconnectorp = Transform("reconnector", yoffset = -105)

image bg_classroom = At("backgrounds/bg classroom_silly.png", Transform(size=(1920, 1280), blur=0))
image bg_other_side = At("backgrounds/other_side.png", Transform(size=(1920, 1280), blur=0))
image bg_forest = At("backgrounds/boys.png", Transform(size=(1920, 1280), blur=0))

label start:
    stop music fadeout 2.0


    scene black
    window hide
    with fade

    show text """{size=40}Epilepsy warning or something. 
    {/size}
    There are things that may be too much for some 
    """:
        align (0.5, 0.5)
        alpha 0.0      
        linear 2.0 alpha 1.0 
    
    pause

    scene bg_forest
    with fade

    Winston "It's time... {w=0.5} After 2 year gap..."
    Winston "I will be {image=reconnecting_final} with other classmates."
    show winston normal at left
    Winston "I think my lawyer job is over…"



    scene bg_classroom with fade
    narratorr "*warps to classroom*"
    hide winston

    show tax normal at right
    Tax "Hi Winston!!!"
    hide tax

    show winston normal at left
    Winston "Hi, tax..."
    hide winston

    show tax excited at right
    Tax "You!!! You have a tie too!"
    hide tax

    show winston normal at left
    Winston "Yeah, I got the job as a law…"
    hide winston

    show tax excited at right
    Tax "Now we can be tie buddies!!!"
    Tax "We could tie each other's ties with our ties!"
    Tax "And be tied with ties!!!"
    hide tax

    show winston tired at left
    Winston "..."
    show winston normal at left
    Winston "We could be \"normal\" buddies..."
    hide winston

    show tax souspicious at right
    Tax "Are you sayin… {w=0.5} You are actually scared of blood?"
    hide tax

    show winston shocked at left
    Winston "?! {w=0.5} And… HOW did you reach THAT conclusion?"
    hide winston

    show tax normal at right
    Tax "Hamburger"
    
    show explosion at right with vpunch
    play sound "explosion.mp3"
    hide tax with hpunch
    narratorr "*explodes*"
    stop sound
    hide explosion
    

    show winston tired at left
    Winston "Again?"
    hide winston

    scene bg_other_side with dissolve

    narratorr "*on the other side of the room*"

    show rusty normal at right
    Rusty "H-Hi, Yuki"
    hide rusty

    show yuki normal at left
    Yuki "Hey. Ramsey"
    hide yuki

    show rusty nervous at right
    Rusty "I'm R-Rusty"
    hide rusty

    show yuki angry at left
    Yuki "SILENCE YOURSELF AT ONCE SCALLYWAG!"
    Yuki "Refrain thyself from speaking to me!"
    hide yuki

    jump speak_to_Yuki_or_Rusty

    return

label speak_to_Yuki_or_Rusty:

    scene bg_classroom with dissolve

    default talked_to_Yuki = False
    default talked_to_Rusty = False
    menu:
        "Speak to Yuki" if not talked_to_Yuki:
            jump speak_to_Yuki_route

        "Speak to Rusty" if not talked_to_Rusty:
            jump speak_to_Rusty_route



label speak_to_Rusty_route:
    show winston normal at left
    Winston "How are you Rusty?"
    hide winston

    show rusty blush at right
    Rusty "g-good"
    hide rusty

    show winston normal at left
    Winston "..."
    Winston "Glad to hear that…"
    hide winston

    show rusty normal at right
    Rusty "So… Do you want to watch some anime?"
    hide rusty

    show winston normal at left
    Winston "..."
    Winston "Right now?"
    hide winston

    show rusty nervous at right
    Rusty "Yea! T-There is this one I love called {color=#66f}Singular Part" 
    hide rusty

    show winston tired at left
    Winston "Naaah, maybe… later"
    show winston normal at left
    Winston "(maybe not)"
    hide winston

    $ talked_to_Rusty = True

    if talked_to_Rusty and talked_to_Yuki:
        jump intro_continuation
    else:
        jump speak_to_Yuki_or_Rusty


label speak_to_Yuki_route:
    show winston normal at left
    Winston "Hey Yuki"
    hide winston

    show yuki normal at right
    Yuki "..."
    Yuki "Hi Robert"
    hide yuki

    show winston shocked at left
    Winston "(That's not even on the same letter!)"
    show winston normal at left
    Winston "Winston, it's Winston"
    hide winston

    show yuki normal at right
    Yuki "Of course Waldo"
    hide yuki
    
    show winston tired at left
    Winston "..."
    show winston normal at left
    Winston "No problem Nicole"
    hide winston

    show yuki angry at right
    Yuki "piss off"
    hide yuki

    show winston tired at left
    Winston "right"
    hide winston

    $ talked_to_Yuki = True

    if talked_to_Rusty and talked_to_Yuki:
        jump intro_continuation
    else:
        jump speak_to_Yuki_or_Rusty



label intro_continuation:
    narratorr "*Flop enters to classroom late*"

    Flop "What's up fuckers!"

    narratorr "*Flop comes to Winston*"

    show flop normal at right
    Flop "Hey Winston! You fucking cat!"
    hide flop

    show winston normal at left
    Winston "Hi… Flop"
    hide winston

    show flop happy at right
    Flop "It's been so fucking long since we seen each other!"
    hide flop

    show winston tired at left
    Winston "Yea..." 
    show winston normal at left
    Winston "(Somehow I don't feel the same)"
    hide winston


    show flop normal at right
    Flop "Whatever…"
    show flop angry at right
    Flop "...fuck."
    show flop normal at right
    Flop "I am going to fucking greet others"
    hide flop

    show winston normal at left
    Winston "sure"
    hide winston

    narratorr "*teacher enters*"

    show cerber_fellow at right
    Cerber_fellow "calm down now my kiddos"
    hide cerber_fellow

    show yuki schocked at left
    Yuki "Who are you? Pray tell!"
    hide yuki

    show cerber_fellow at right
    Cerber_fellow "I am… Cerber"
    Cerber_fellow "And I will be your new teacher!!!"
    Cerber_fellow "yupiie!"
    hide cerber_fellow

    show reverse_explosion at left with vpunch
    play sound "reverse_explosion.mp3"
    show tax excited at left
    Tax "Yupiee!!!"
    stop sound
    hide tax
    hide reverse_explosion

    show winston normal at left
    Winston "And she unexploded…"
    hide winston 

    show cerber_fellow at right
    Cerber_fellow "We thought it would be cool to hold a competition today"
    Cerber_fellow "So you will be participating for a golden ball of yarn!!!"
    hide cerber_fellow

    show yuki schocked at left
    Yuki "WHAT?!"
    hide yuki

    show flop schocked at left
    Flop "Fuck! No way!"
    hide flop

    show tax excited at left
    Tax "yupiiee"
    hide tax

    show cerber_fellow at right
    Cerber_fellow "Yes! But before that… You should {image=reconnectp}!!!"
    Cerber_fellow "You have time till… Winston says so"
    Cerber_fellow "Cause he is main character or something"

    hide cerber_fellow

    show cerber_evil at right
    Cerber_evil "Also I hope all of you die!"
    hide cerber_evil

    show winston tired at left
    Winston "..."
    Winston "..."
    show winston normal at left
    Winston "(whatever)"
    hide winston

    narratorr "*FREE TIME*"
    narratorr "Now you will be able to spend time with others. Do well and they might help you in the competition! Or fail and they will be mad at you"

    jump free_time

#THEEEEEEEEEEEEERRRRRRRRRRRRREEEEEEEEEEEEEEEE

label free_time:
    default Yuki_t = False
    default Rusty_t = False
    default Flop_t = False
    default Tax_t = False

    default Yuki_friend = False
    default Rusty_friend = False
    default Flop_friend = False
    default Tax_friend = False
    menu:
        "Ask the teacher for help in preparing":
            jump silly_cerber_free_time
        "Spend some time with Rusty" if not Rusty_t:
            jump free_time_with_Rusty
        "Spend some time with Flop" if not Flop_t:
            jump free_time_with_Flop
        "Spend some time with Tax" if not Tax_t:
            jump free_time_with_Tax
        "Spend some time with Yuki" if not Yuki_t:
            jump free_time_with_Yuki
        "Finish free time and start the minigame":
            jump pick_the_cat


label silly_cerber_free_time:
    show cerber_silly at right
    Cerber_silly "Fortnite"
    hide cerber_silly
    jump free_time
    

label free_time_with_Rusty:
    show winston normal at left
    Winston "What are you doing, Rusty?"
    Winston "Shouldn't you get ready for the 'battle'?"
    hide winston

    show rusty blush at right
    Rusty "I-I am watching the {color=#46d}Dino ball"
    show rusty normal at right
    Rusty "W-would you like to watch with me?"
    hide rusty

    menu:
        "yea...":
            jump yea_Rusty

        "no...":
            jump no_Rusty


label yea_Rusty:
    show winston normal at left
    Winston "Yea… I am not doing that at all."
    Winston "I would rather kill my newborn son…"
    jump Rusty_denial

label no_Rusty:
    show winston normal at left
    Winston "No… I wouldn't like…"
    Winston "I would LOVE to watch {color=#46d}Dino ball{/color} with you!"
    jump Rusty_denial
    

label Rusty_denial:
    show winston shocked at left
    Winston "Wait! That's not what I meant!!!"
    hide winston

    show rusty normal at right
    Rusty "Are you f-feeling okay?"
    hide rusty

    show winston normal at left
    Winston "Shut up!"
    hide winston

    show rusty sad at right
    Rusty "S-s-should I g-go somewhere else?"
    hide rusty

    show winston tired at left
    Winston "no..."
    Winston "I, Winston Deez, born in 2003, hereby formally…"

    menu:
        "state my INTENT to watch {color=#46d}dino ball{/color}. Furthermore, all objections I raise after this sentence is finished are to be considered legally irrelevant. ":
            jump accept_Rusty
        "REJECT any involvement with {color=#46d}dino ball{/color}. Furthermore, any agreement I might utter after this sentence is finished shall be deemed null":
            jump reject_Rusty

label reject_Rusty:
    Winston "… is what I would say! If I were a loser!"
    Winston "I am just messing with you! I could watch an episode or two"
    hide winston

    show rusty nervous at right
    Rusty "..."
    Rusty "Is there another opposite?"
    Rusty "Like you say…"
    hide rusty

    show winston normal at left
    Winston "Nah, Let's just watch it"
    hide winston

    narratorr "*you spent some time watching Kogu fighting Geveta*"

    $Rusty_t = True
    $Rusty_friend = True

    jump free_time

label accept_Rusty:
    Winston "… is what I would say! If I were a loser!"
    hide winston

    show rusty sad at right
    Rusty "I… will watch it alone I guess."
    Rusty "I would love to have depression right now to make you feel bad "
    hide rusty

    narratorr "*Rusty quicly goes away*"

    show winston tired at left
    Winston "I think… I miss my wife"
    hide winston

    narratorr "you did a really good job at not doing what you were supposed to do!"

    $Rusty_t = True
    
    jump free_time


label free_time_with_Flop:
    show winston normal at left
    Winston "Yo, Flop. Want to train together?"
    hide winston 

    show flop angry at right
    Flop "Fuck no! I just ate!"
    show flop normal at right
    Flop "Do you even know who I fucking am? {w=0.2} Like inside?"
    hide flop 

    show winston normal at left
    Winston "Yea… you are fit and… confident"
    hide winston

    show flop normal at right
    Flop "Then answer me fucking this. What's my favorite fucking word?"
    hide flop

    show winston normal at left
    Winston "..."

    menu:
        "France":
            Winston "France?"
            jump wrong_route
        "fabricated":
            Winston "fabricated?"
            jump wrong_route
        "fur":
            Winston "fur?"
            jump wrong_route
        "fuck":
            jump fuck_route


label fuck_route:
    Winston "… 'fuck'?"
    hide winston

    show flop happy at right
    Flop "Woaah! No fucking way! You got it right! {w=0.6} Even my meat-statue d…"
    hide flop

    show winston shocked at left
    Winston "I don't want to know. Stop"
    show winston normal at left
    Winston "Thanks for your time. I… need to talk to others"
    hide winston

    show flop normal at right
    Flop "No fucking problem!"
    hide flop

    $Flop_t = True
    $Flop_friend = True

    jump free_time

label wrong_route:
    hide winston
    narratorr "Are we dead ass? This character has 1 trait. You don't deserve the rest of this dialogue."
    $Flop_t = True
    jump free_time

label free_time_with_Tax:
    show winston normal at left
    Winston "What are you doing Tax?"
    hide winston

    show tax souspicious at right
    Tax "Shhhhhh. I am listening to quiet sounds"
    hide tax 

    show winston normal at left
    Winston "Why?"
    hide winston
    
    show tax normal at right
    Tax "In case there is rebellion and I would have to live in the wild! Want to join?"
    hide tax

    show winston normal at left
    Winston "I forgor you are a royal… but why would cats choose to revolt? You guys are pretty good at your job."
    hide winston

    show tax normal at right
    Tax "Bombs in the heads. Also cheese"
    hide tax

    show winston shocked at left
    Winston "HUH?!"

    menu:
        "ask about bombs":
            jump tax_bombs
        "ask about cheese":
            jump tax_cheese

label tax_bombs:
    Winston "What do you mean bombs in heads?! Am I going to explode if the government is fed up with me?"
    hide winston

    narratorr "yea"

    show tax scared at right
    Tax "ummmmmmmmmmmmmm"
    hide tax 

    show explosion at right with vpunch
    play sound "explosion.mp3"
    pause 1
    show explosion at right with hpunch
    play sound "explosion.mp3"
    narratorr "*explodes*"
    stop sound
    narratorr "*She is going to unexplode somewhere, but you won't spend time with her. You should be more considerate*"
    hide explosion

    $Tax_t = True

    jump free_time


label tax_cheese:
    show winston normal at left
    Winston "Cheese?"
    hide winston

    show tax scared at right
    Tax "Shhhhhhhhhhhh!!!!!!!!!!!!!!!!!!!!!"
    show tax souspicious at right
    Tax "Don't ask questions Winston…"
    hide tax 

    show winston tired at left
    Winston "okay..."
    hide winston

    narratorr "*You spent some time listening to nothing with Tax! She likes you again!*"

    $Tax_t = True
    $Tax_friend = True
    
    jump free_time

label free_time_with_Yuki:
    narratorr "*You bumped into Yuki*"

    show yuki schocked at right
    Yuki "Why you disrespecting me bruv?"
    hide yuki

    show winston normal at left
    Winston "My mistake original gangster"
    hide winston

    show yuki angry at right
    Yuki "No, this can not be forgiven now. Empty the compartments of your pantaloons."
    hide yuki

    show winston shocked at left
    Winston "For what purpose?!"
    hide winston

    show yuki angry at right
    Yuki "And discard all your footwear as well"
    hide yuki

    show winston shocked at left
    Winston "FOR WHAT PURPOSE?!"

    menu:
        "Empty the compartments of your pantaloons":
            jump empty_Yuki
        "Flee (boring)":
            jump flee_Yuki

label empty_Yuki:
    narratorr "*you gave all your money. You lost 17 cents and 2 mints*"
    hide winston

    show yuki jolly at right
    narratorr "*Yuki laughs in rich*"
    Yuki "Peasant! But I suppose I did enjoy this encounter. Now hurry up and go."
    hide yuki

    show winston tired at left
    Winston "Can I have at least my mint back?"
    hide winston

    narratorr "*no. But she might help you later…*"

    $ Yuki_t = True
    $ Yuki_friend = True

    jump free_time


label flee_Yuki:
    Winston "Hell nah!"
    hide winston

    narratorr "*You run away*"

    show yuki angry at right
    Yuki "Come here you rapscallion! What are you doing?"
    hide yuki

    narratorr "*so you run away… cool. Nothing happened*"

    $ Yuki_t = True

    jump free_time


label pick_the_cat:
    narratorr "Hey, so basically you can choose which of your classmates will help you in the minigame!"
    narratorr "You can pick only those who you {image=reconnectedp} with."
    narratorr "Move left or right to avoid obstacles and get to the top!"
    narratorr "good luck"

    default no_one = False
    menu:
        "Pick Rusty! (level is slow (easier level))" if Rusty_friend:
            play music "audio/minigame_music.mp3" volume 0.2 fadein 1.0
            $current_ClimbGame = ClimbGame(True,False,False,False)
            call screen S_ClimbGame
        "Pick Flop! (randomly destroy obstacles)" if Flop_friend:
            play music "audio/minigame_music.mp3" volume 0.2 fadein 1.0
            $current_ClimbGame = ClimbGame(False,True,False,False)
            call screen S_ClimbGame
        "Pick Yuki! (additional live)" if Yuki_friend:
            play music "audio/minigame_music.mp3" volume 0.2 fadein 1.0
            $current_ClimbGame = ClimbGame(False,False,False,True)
            call screen S_ClimbGame
        "Pick Tax! (level goes brrrr (harder level))" if Tax_friend:
            play music "audio/minigame_music.mp3" volume 0.2 fadein 1.0
            $current_ClimbGame = ClimbGame(False,False,True,False)
            call screen S_ClimbGame
        "No one :c (you should be a better friend)":
            play music "audio/minigame_music.mp3" volume 0.2 fadein 1.0
            $ no_one = True
            $current_ClimbGame = ClimbGame(False,False,False,False)
            call screen S_ClimbGame


label ending:
    if no_one == False:
        show winston normal at left
        narratorr "Yaaay! Well done!"
        narratorr "*You received the golden ball of yarn!*"
        show golden:
            xalign 0.5
            yoffset 130

        if Rusty_friend:
            show rusty blush at right
            Rusty "W-wow! You r-really won! Congratulations"
            hide rusty 

        if Flop_friend:
            show flop happy at right
            Flop "You fucking did it! I am so happy for you bro!"
            hide flop 

        if Yuki_friend:
            show yuki jolly at right
            Yuki "Splendidly done!"
            hide yuki
        
        if Tax_friend:
            show tax excited at right
            Tax "Yupiee! You got it!"
            narratorr "*explodes*"
            Winston "..."
            Winston "..."
            show explosion at right with vpunch
            play sound "explosion.mp3"
            narratorr "*actually explodes*"
            stop sound
            hide explosion
            hide tax

        show cerber_evil at right
        Cerber_evil "Tsssk you done it…"
        hide cerber_evil
        show cerber_fellow at right
        Cerber_fellow "As an adult who is of legal age, I must say I am proud of you my kiddo!"
        hide cerber_fellow
        show cerber_silly at right
        Cerber_silly "Fortnite"
        hide cerber_silly

        hide winston 
        
        if Rusty_friend:
            show rusty normal at right
        
        if Flop_friend:
            show flop normal at left

        show cerber_evil

        if Yuki_friend:
            show yuki normal:
                xalign 2.0   
                yalign 0.0   
            
                rotate 180

                yoffset -210

        if Tax_friend:
            show tax normal:
                xalign -1.0   
                yalign 0.0   
            
                rotate 180

                yoffset -210

        everyone "Winston! You are such a {image=reconnectorp}"
        jump credits

    narratorr "*You won all by yourself… The opposite what the game was about, but sure*"
    show rusty normal at right
    show flop normal at left
    show cerber_fellow
    show yuki normal:
                xalign 2.0   
                yalign 0.0   
            
                rotate 180

                yoffset -210
    show tax normal:
                xalign -1.0   
                yalign 0.0   
            
                rotate 180

                yoffset -210
    everyone "Winston! Fuck you"

    hide yuki 
    hide tax 
    hide rusty 
    hide cerber_fellow
    hide flop 

    show winston tired
    Winston "I sure hope the 10 000 ton weight won't fall on me for no reason!"

    show tons:
        xalign 0.5
        yanchor 1.0 
        ypos -0.1  

        easein 0.25 ypos 1.0
        
        yoffset 30
    
    hide winston
    play sound "splat.mp3"
    narratorr "bam" with vpunch

    jump credits


label credits:
    play music "credits.mp3"
    scene black
    window hide
    with fade

    show text """{size=40}Made by Jinrty and PysiaQV(MrPop){/size}
    for StoryBoard hackclub with theme 'RECONNECTED'
    
    font: Gabarito
    title font: Romanesco
    backgrounds: Adobe Stock
    main-menu music - 'On the Farm' : LudoLoon Studio
    minigame music - 'Route 83' : melodyayresgriffiths
    credits music - 'Cipher' : Kevin Macleod
    
    {size=50}Thanks for playing!!!{/size}""":
        align (0.5, 0.5)
        alpha 0.0      
        linear 2.0 alpha 1.0 

    pause

    hide text with dissolve
    pause 1.0

    return