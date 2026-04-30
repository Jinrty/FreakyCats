init python:
    import random
    import time

    renpy.music.register_channel("sound2", mixer="sfx", loop=False)

    FINISH = -1
    TILE = 0
    PLAYER = 1
    ROCK = 2
    EXPLODE = 3

    class ClimbGame:
        def __init__(self, rusty, flop, tax, yuki):
            self.lvl = [
                [-1,-1,-1,-1],
                [0,0,0,0],
                [0,0,0,0], 
                [0,2,2,0], 
                [0,0,0,0],
                [0,0,0,0], 
                [0,0,0,2], 
                [0,0,0,2], 
                [0,0,0,0], 
                [0,2,0,0],
                [2,2,0,0], 
                [0,0,0,0], 
                [0,0,0,0], 
                [0,2,0,0], 
                [0,2,2,0],
                [0,0,2,2], 
                [0,0,0,2], 
                [2,0,0,0], 
                [2,0,0,0], 
                [2,0,2,0],
                [0,0,2,0], 
                [0,0,2,0], 
                [2,2,2,0], 
                [2,2,0,0], 
                [2,0,0,0],
                [0,0,0,0], 
                [0,0,0,0], 
                [0,2,2,2], 
                [0,0,2,2], 
                [0,0,0,2],
                [0,0,0,2], 
                [0,0,0,2], 
                [2,0,0,0], 
                [2,0,2,2], 
                [2,0,0,2],
                [2,2,0,2], 
                [0,0,0,2], 
                [2,0,0,2], 
                [0,0,0,2], 
                [0,0,0,0],
                [2,0,0,0], 
                [0,0,2,0], 
                [0,0,0,0], 
                [0,2,0,0], 
                [0,2,0,0],
                [0,0,0,2], 
                [2,0,0,0], 
                [0,0,2,0], 
                [0,0,0,0], 
                [0,0,0,0],
                [0,0,2,2], 
                [2,0,0,2], 
                [2,0,0,2], 
                [2,2,0,0], 
                [2,2,0,0],
                [2,2,0,0], 
                [0,0,0,0], 
                [0,0,0,0], 
                [0,2,2,0],
                [0,0,0,0],
                [0,0,0,0], 
                [2,0,0,2], 
                [2,0,0,2], 
                [2,0,0,2], 
                [0,0,0,0],
                [0,0,0,0], 
                [0,0,0,0], 
                [0,0,0,0], 
                [0,0,0,0], 
                [0,0,0,0],
                [0,0,0,0], 
                [0,0,0,0], 
                [0,0,0,0], 
                [0,0,0,0]
            ]
            self.width = len(self.lvl[0])
            self.height = len(self.lvl)
            self.cellsize = 120 
            self.offset = 0
            self.movement_accumulator = 0 
            
            self.def_speed = 12
            self.lives = 1
            self.won = False
            self.new_spot = [-1,-1]
            self.player = [len(self.lvl) - 6, 2]
            self.lvl[self.player[0]][self.player[1]] = PLAYER
            self.explosions = []
            self.reviving = 0
            self.invlength = 4
            self.last_boost_time = 0

            self.rusty = rusty
            self.flop = flop
            self.yuki = yuki
            self.tax = tax
            if (yuki): self.lives += 1
            if (tax): self.def_speed = 20
            if (rusty): self.def_speed = 8

            self.scroll_speed = self.def_speed
        
        def update(self):
            if (self.new_spot[0] >= 0 and self.new_spot[0] < self.height) and (self.new_spot[1] >= 0 and self.new_spot[1] < self.width):
                target_tile = self.lvl[self.new_spot[0]][self.new_spot[1]]
                if target_tile == ROCK:
                    if self.reviving <= 0:
                        self.lives -= 1
                        if self.lives > 0:
                            self.reviving = self.invlength
                
                self.lvl[self.player[0]][self.player[1]] = TILE
                self.player = self.new_spot
                self.lvl[self.player[0]][self.player[1]] = PLAYER
                self.new_spot = [-1, -1] 

            self.offset += self.scroll_speed
            self.movement_accumulator += self.scroll_speed

            if self.movement_accumulator >= self.cellsize:
                self.movement_accumulator -= self.cellsize 
                
                if (self.player[0] - 1) >= 0:
                    if (self.reviving > 0):
                        self.reviving -= 1

                    if (self.lvl[self.player[0] - 1][self.player[1]] == ROCK):
                        if not (self.reviving > 0):
                            self.lives -= 1
                            if (self.lives > 0):
                                self.reviving = 6
                    
                    self.lvl[self.player[0]][self.player[1]] = TILE
                    self.player[0] = self.player[0] - 1
                    self.lvl[self.player[0]][self.player[1]] = PLAYER

                    if (self.flop):
                        rand_tile = random.randint(0,3)
                        target_y = max(0, self.player[0] - 3)
                        if self.lvl[target_y][rand_tile] == ROCK:
                            self.lvl[target_y][rand_tile] = EXPLODE
                    
                    for i in self.explosions:
                        if self.lvl[i[0]][i[1]] == EXPLODE:
                            self.lvl[i[0]][i[1]] = TILE
                    self.explosions = []
                
                elif (self.player[0] == 0):
                    self.won = True
        
        def movement(self, move):
            self.new_spot = [self.player[0] + move[0], self.player[1] + move[1]]
        
        def speed_boost(self):
            if not self.rusty:
                self.scroll_speed = self.def_speed * 2
            else:
                self.scroll_speed = 15
        
        def unspeed_boost(self):
            self.scroll_speed = self.def_speed

default current_ClimbGame = ClimbGame(False, False, False, False)

transform fade_in(start,time):
    alpha start
    linear time alpha 1.0

transform fall:
    yoffset -2000
    easeout 0.5 yoffset 0

screen S_ClimbGame():
    modal True
    
    add "images/minigame/sky.png":
        xalign 0.5
        yalign 0.9
        xysize (2600, 4150)
        yoffset current_ClimbGame.offset / 3

    frame:
        xalign 0.5
        yalign 0.96
        xysize (current_ClimbGame.cellsize * current_ClimbGame.width, current_ClimbGame.cellsize * current_ClimbGame.height)
        background Solid("#ffffff00")
        yoffset current_ClimbGame.offset

        if not ((current_ClimbGame.lives <= 0) or current_ClimbGame.won):
            timer 0.05 action Function(current_ClimbGame.update) repeat True

        for y, i in enumerate(current_ClimbGame.lvl):
            for x, j in enumerate(i):
                add "wall":
                    xysize(current_ClimbGame.cellsize, current_ClimbGame.cellsize)
                    xpos x * current_ClimbGame.cellsize
                    ypos y * current_ClimbGame.cellsize
                if j == ROCK:
                    add "window":
                        xysize(current_ClimbGame.cellsize, current_ClimbGame.cellsize)
                        xpos x * current_ClimbGame.cellsize
                        ypos y * current_ClimbGame.cellsize
                elif j == EXPLODE:
                    add "explosion":
                        xysize(current_ClimbGame.cellsize, current_ClimbGame.cellsize)
                        xpos x * current_ClimbGame.cellsize
                        ypos y * current_ClimbGame.cellsize
                    $ current_ClimbGame.explosions.append([y, x])
                elif j == FINISH:
                    add "finish":
                        xysize(current_ClimbGame.cellsize, current_ClimbGame.cellsize)
                        xpos x * current_ClimbGame.cellsize
                        ypos y * current_ClimbGame.cellsize
                elif j == PLAYER:
                    if current_ClimbGame.won:
                        add "finish":
                            xysize(current_ClimbGame.cellsize, current_ClimbGame.cellsize)
                            xpos x * current_ClimbGame.cellsize
                            ypos y * current_ClimbGame.cellsize
                    elif current_ClimbGame.lives <= 0:
                        add "window":
                            xysize(current_ClimbGame.cellsize, current_ClimbGame.cellsize)
                            xpos x * current_ClimbGame.cellsize
                            ypos y * current_ClimbGame.cellsize
                    
                    add "winton[y % 2]":
                        xysize(current_ClimbGame.cellsize, current_ClimbGame.cellsize)
                        xpos x * current_ClimbGame.cellsize
                        ypos y * current_ClimbGame.cellsize
        

        key "keydown_K_UP" action Function(current_ClimbGame.speed_boost)
        key "keyup_K_UP" action Function(current_ClimbGame.unspeed_boost)
        key "keydown_K_w" action Function(current_ClimbGame.speed_boost)
        key "keyup_K_w" action Function(current_ClimbGame.unspeed_boost)
        
        key "K_RIGHT" action Function(current_ClimbGame.movement, [0,1])
        key "K_LEFT" action Function(current_ClimbGame.movement, [0,-1])
        key "d" action Function(current_ClimbGame.movement, [0,1])
        key "a" action Function(current_ClimbGame.movement, [0,-1])
    
    hbox:
        xpos 20 ypos 20 spacing 15
        add "lives"
        if (current_ClimbGame.reviving > 0):
            add "inf"
        elif (current_ClimbGame.lives == 1):
            add "one"
        elif (current_ClimbGame.lives == 2):
            add "two"
        else:
            add "zero"
    
    if (current_ClimbGame.won):
        timer 0.01 action [Play("sound","hapy.mp3"), Play("sound2","applause.mp3"), Stop("music", fadeout = 0.5)]
        add Solid("#00000050"):
            xysize (2000,1100)
            yalign 0.5 xalign 0.5
        add "conffeti" :
            xysize (2000,1100)
            yalign 0.5 xalign 0.5
        timer 4.5 action [Stop("sound", fadeout = 5), Stop("sound2", fadeout = 5), Jump("ending")]

    if (current_ClimbGame.lives <= 0):
        timer 0.01 action [Play("sound","sadge2.mp3"), Play("sound2","sadge.mp3")]
        frame at fade_in(0.0, 0.25):
            xalign 0.5 yalign 0.5
            background "#f3f3f3ff"
            xysize (1920, 1100)
            add "winton_fall" at fall:
                xysize(750, 700)
                xalign 0.5 yalign 0.9
            textbutton "GET UP" action [Stop("sound", fadeout = 1.5), Stop("sound2", fadeout = 1.5), SetVariable("current_ClimbGame", ClimbGame(current_ClimbGame.rusty, current_ClimbGame.flop, current_ClimbGame.tax, current_ClimbGame.yuki))]:
                xalign 0.5 yalign 0.15
                text_size 200
                text_color "#1b1b1b"
                text_hover_color "#3b3b3b"
                keysym "K_SPACE"