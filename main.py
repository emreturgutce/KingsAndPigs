import pygame as pg
import os
import time
import random
vec = pg.math.Vector2

# CONSTS
WIDTH = 800
HEIGHT = 600
FPS = 30

# Image Directory
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'img')

# ** IMAGES
# King Images
kingGround = pg.image.load(os.path.join(image_path, 'ground.png'))
kingRun = [pg.image.load(os.path.join(image_path, 'tile000.png')), pg.image.load(os.path.join(image_path, 'tile001.png')), pg.image.load(os.path.join(image_path, 'tile002.png')), pg.image.load(os.path.join(image_path, 'tile003.png')),
           pg.image.load(os.path.join(image_path, 'tile004.png')), pg.image.load(os.path.join(image_path, 'tile005.png')), pg.image.load(os.path.join(image_path, 'tile006.png')), pg.image.load(os.path.join(image_path, 'tile007.png'))]
kingRunL = [pg.image.load(os.path.join(image_path, 'tile000L.png')), pg.image.load(os.path.join(image_path, 'tile001L.png')), pg.image.load(os.path.join(image_path, 'tile002L.png')), pg.image.load(os.path.join(image_path, 'tile003L.png')),
            pg.image.load(os.path.join(image_path, 'tile004L.png')), pg.image.load(os.path.join(image_path, 'tile005L.png')), pg.image.load(os.path.join(image_path, 'tile006L.png')), pg.image.load(os.path.join(image_path, 'tile007L.png'))]
kingAttack = [pg.image.load(os.path.join(image_path, 'tile000A.png')), pg.image.load(
    os.path.join(image_path, 'tile001A.png')), pg.image.load(os.path.join(image_path, 'tile002A.png'))]
kingAttackL = [pg.transform.flip(pg.image.load(os.path.join(image_path, 'tile000A.png')), True, False), pg.transform.flip(pg.image.load(os.path.join(image_path,
                                                                                                                                                     'tile001A.png')), True, False), pg.transform.flip(pg.image.load(os.path.join(image_path, 'tile002A.png')), True, False)]
kingIdle = [pg.image.load(os.path.join(image_path, 'tile001I.png')), pg.image.load(os.path.join(image_path, 'tile002I.png')), pg.image.load(os.path.join(image_path, 'tile003I.png')), pg.image.load(os.path.join(image_path, 'tile004I.png')), pg.image.load(os.path.join(image_path, 'tile005I.png')),
            pg.image.load(os.path.join(image_path, 'tile006I.png')), pg.image.load(os.path.join(image_path, 'tile007I.png')), pg.image.load(os.path.join(image_path, 'tile008I.png')), pg.image.load(os.path.join(image_path, 'tile009I.png')), pg.image.load(os.path.join(image_path, 'tile010I.png'))]
kingJump = [pg.image.load(os.path.join(image_path, 'jump.png')), pg.image.load(
    os.path.join(image_path, 'jumpL.png'))]
kingHit = [pg.image.load(os.path.join(image_path, 'tile000KingH.png')), pg.image.load(
    os.path.join(image_path, 'tile001KingH.png'))]
kingDead = [pg.image.load(os.path.join(image_path, 'tile000KingD.png')), pg.image.load(os.path.join(image_path, 'tile001KingD.png')), pg.image.load(
    os.path.join(image_path, 'tile002KingD.png')), pg.image.load(os.path.join(image_path, 'tile003KingD.png'))]

# KingPig Images
kingPigKIdle = [pg.image.load(os.path.join(image_path, 'tile000KingPigI.png')), pg.image.load(os.path.join(image_path, 'tile001KingPigI.png')), pg.image.load(os.path.join(image_path, 'tile002KingPigI.png')), pg.image.load(os.path.join(image_path, 'tile003KingPigI.png')), pg.image.load(os.path.join(image_path, 'tile004KingPigI.png')), pg.image.load(os.path.join(image_path, 'tile005KingPigI.png')),
                pg.image.load(os.path.join(image_path, 'tile006KingPigI.png')), pg.image.load(os.path.join(image_path, 'tile007KingPigI.png')), pg.image.load(os.path.join(image_path, 'tile008KingPigI.png')), pg.image.load(os.path.join(image_path, 'tile009KingPigI.png')), pg.image.load(os.path.join(image_path, 'tile010KingPigI.png')), pg.image.load(os.path.join(image_path, 'tile011KingPigI.png'))]
kingPigRunRight = [pg.image.load(os.path.join(image_path, 'tile000KingPigRunR.png')), pg.image.load(os.path.join(image_path, 'tile001KingPigRunR.png')), pg.image.load(os.path.join(image_path, 'tile002KingPigRunR.png')),
                   pg.image.load(os.path.join(image_path, 'tile003KingPigRunR.png')), pg.image.load(os.path.join(image_path, 'tile004KingPigRunR.png')), pg.image.load(os.path.join(image_path, 'tile005KingPigRunR.png'))]
kingPigRunLeft = [pg.image.load(os.path.join(image_path, 'tile000KingPigRunL.png')), pg.image.load(os.path.join(image_path, 'tile001KingPigRunL.png')), pg.image.load(os.path.join(image_path, 'tile002KingPigRunL.png')),
                  pg.image.load(os.path.join(image_path, 'tile003KingPigRunL.png')), pg.image.load(os.path.join(image_path, 'tile004KingPigRunL.png')), pg.image.load(os.path.join(image_path, 'tile005KingPigRunL.png'))]
kingPigDead = [pg.image.load(os.path.join(image_path, 'tile000KingPigD.png')), pg.image.load(os.path.join(image_path, 'tile001KingPigD.png')),
               pg.image.load(os.path.join(image_path, 'tile002KingPigD.png')), pg.image.load(os.path.join(image_path, 'tile003KingPigD.png'))]
kingPigAttack = [pg.image.load(os.path.join(image_path, 'tile000KingPigA.png')), pg.image.load(os.path.join(image_path, 'tile001KingPigA.png')), pg.image.load(os.path.join(
    image_path, 'tile002KingPigA.png')), pg.image.load(os.path.join(image_path, 'tile003KingPigA.png')), pg.image.load(os.path.join(image_path, 'tile004KingPigA.png'))]
kingPigAttackLeft = [pg.transform.flip(kingPigAttack[0], True, False), pg.transform.flip(kingPigAttack[1], True, False), pg.transform.flip(
    kingPigAttack[2], True, False), pg.transform.flip(kingPigAttack[3], True, False), pg.transform.flip(kingPigAttack[4], True, False)]

# Pig Images
pigIdle = [pg.image.load(os.path.join(image_path, 'tile000PigI.png')), pg.image.load(os.path.join(image_path, 'tile001PigI.png')), pg.image.load(os.path.join(image_path, 'tile002PigI.png')), pg.image.load(os.path.join(image_path, 'tile003PigI.png')), pg.image.load(os.path.join(image_path, 'tile004PigI.png')), pg.image.load(os.path.join(image_path, 'tile004PigI.png')), pg.image.load(
    os.path.join(image_path, 'tile005PigI.png')), pg.image.load(os.path.join(image_path, 'tile006PigI.png')), pg.image.load(os.path.join(image_path, 'tile007PigI.png')), pg.image.load(os.path.join(image_path, 'tile008PigI.png')), pg.image.load(os.path.join(image_path, 'tile009PigI.png')), pg.image.load(os.path.join(image_path, 'tile010PigI.png'))]
pigRunRight = [pg.image.load(os.path.join(image_path, 'tile000PigRun.png')), pg.image.load(os.path.join(image_path, 'tile001PigRun.png')), pg.image.load(os.path.join(image_path, 'tile002PigRun.png')), pg.image.load(
    os.path.join(image_path, 'tile003PigRun.png')), pg.image.load(os.path.join(image_path, 'tile004PigRun.png')), pg.image.load(os.path.join(image_path, 'tile005PigRun.png'))]
pigRunLeft = [pg.transform.flip(pg.image.load(os.path.join(image_path, 'tile000PigRun.png')), True, False), pg.transform.flip(pg.image.load(os.path.join(image_path, 'tile001PigRun.png')), True, False), pg.transform.flip(pg.image.load(os.path.join(image_path, 'tile002PigRun.png')), True, False), pg.transform.flip(
    pg.image.load(os.path.join(image_path, 'tile003PigRun.png')), True, False), pg.transform.flip(pg.image.load(os.path.join(image_path, 'tile004PigRun.png')), True, False), pg.transform.flip(pg.image.load(os.path.join(image_path, 'tile005PigRun.png')), True, False)]

# Box Images
boxIdle = pg.image.load(os.path.join(image_path, 'tile000BoxI.png'))
boxHit = [boxIdle, pg.image.load(os.path.join(image_path, 'tile000BoxH.png'))]

# Diamond Images
diamondIdle = [pg.image.load(os.path.join(image_path, 'tile000DiamondI.png')), pg.image.load(os.path.join(image_path, 'tile001DiamondI.png')), pg.image.load(os.path.join(image_path, 'tile002DiamondI.png')), pg.image.load(os.path.join(image_path, 'tile003DiamondI.png')), pg.image.load(os.path.join(image_path, 'tile004DiamondI.png')), pg.image.load(os.path.join(image_path, 'tile005DiamondI.png')), pg.image.load(os.path.join(image_path, 'tile006DiamondI.png')), pg.image.load(os.path.join(image_path, 'tile007DiamondI.png')), pg.image.load(os.path.join(image_path, 'tile008DiamondI.png')), pg.image.load(os.path.join(image_path, 'tile009DiamondI.png'))]

# BG Images
startScreen = pg.image.load(os.path.join(image_path, 'start_screen.png'))
startScreen = pg.transform.scale(startScreen, (WIDTH, HEIGHT))  # Fitting images to screen
gameOver = pg.image.load(os.path.join(image_path, 'gameover_screen.png'))
gameOver = pg.transform.scale(gameOver, (WIDTH, HEIGHT))    # Fitting images to screen
background = pg.image.load(os.path.join(image_path, 'background.png'))
background = pg.transform.scale(background, (WIDTH, HEIGHT))    # Fitting images to screen
bgX = 0
bgX2 = background.get_width()

# ** Classes
# Game Class
class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Kings And Pigs')
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font('arial')
        self.highscore = 0
        self.deadCount = 0
        self.isPigsExist = False
        self.x = False
        self.y = False
        self.z = False
        self.ctrl = 0
        self.isBoxesExist = False

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.kingPigs = pg.sprite.Group()
        self.king = King(self)
        self.kings = pg.sprite.Group()
        self.kings.add(self.king)
        self.all_sprites.add(self.king)
        self.kingPig = KingPig()
        self.kingPig2 = KingPig(posV=vec(80, 200))
        self.kingPigs.add(self.kingPig)
        self.kingPigs.add(self.kingPig2)
        self.all_sprites.add(self.kingPig)
        self.all_sprites.add(self.kingPig2)
        self.pigs = pg.sprite.Group()
        self.platform = Platform(0, HEIGHT-40, WIDTH, 40)
        self.platforms = pg.sprite.Group()
        self.platforms.add(self.platform)
        self.all_sprites.add(self.platform)
        self.run()

    def loadData(self):
        pass

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        global bgX
        global bgX2
        if self.king.vel.x > 0:
            bgX -= self.king.vel.x + 0.5 * self.king.acc.x
            bgX2 -= self.king.vel.x + 0.5 * self.king.acc.x

        if bgX < background.get_width() * -1:
            bgX = background.get_width()

        if bgX2 < background.get_width() * -1:
            bgX2 = background.get_width()
       
        # Game Loop - Update
        self.all_sprites.update()
       
        # check if player hits a platform - only if falling(=GRAVITY)
        self.hitControl()
        
        #self.mobFocus()

        if self.king.vel.y > 0:
            hits = pg.sprite.spritecollide(self.king, self.platforms, False)
            if hits:
                self.king.pos.y = hits[0].rect.top
                self.king.vel.y = 0
        if self.kingPig.vel.y > 0:
            hits = pg.sprite.spritecollide(self.kingPig, self.platforms, False)
            if hits:
                self.kingPig.pos.y = hits[0].rect.top
                self.kingPig.vel.y = 0
        if self.kingPig2.vel.y > 0:
            hits = pg.sprite.spritecollide(
                self.kingPig2, self.platforms, False)
            if hits:
                self.kingPig2.pos.y = hits[0].rect.top
                self.kingPig2.vel.y = 0
        if self.isBoxesExist:
            if self.box.vel.y > 0:
                hits = pg.sprite.spritecollide(self.box, self.platforms, False)
                if hits:
                    self.box.pos.y = hits[0].rect.top
                    self.box.vel.y = 0
            if self.box2.vel.y > 0:
                hits = pg.sprite.spritecollide(self.box2, self.platforms, False)
                if hits:
                    self.box2.pos.y = hits[0].rect.top
                    self.box2.vel.y = 0

        if self.isPigsExist:
            if self.pig.vel.y > 0:
                hits = pg.sprite.spritecollide(
                    self.pig, self.platforms, False)
                if hits:
                    self.pig.pos.y = hits[0].rect.top
                    self.pig.vel.y = 0
        
        self.xd = pg.time.get_ticks()
        if self.x == True:
            if self.xd - self.now >= 500:
                self.now = pg.time.get_ticks()
                pg.sprite.spritecollide(self.king, self.kingPigs, True)
                self.x = False
        if self.y == True:
            if self.xd - self.now2 >= 500:
                self.now2 = pg.time.get_ticks()
                pg.sprite.spritecollide(self.king, self.kingPigs, True)
                self.y = False
        if self.z == True:
            if self.xd - self.nowK >= 300:
                self.nowK = pg.time.get_ticks()
                pg.sprite.spritecollide(self.kingPig, self.kings, True)
                self.z = False
                self.playing = False

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP and not self.king.dead:
                    self.king.jump()
                if event.key == pg.K_SPACE and not self.king.dead:
                    self.king.attacking = True
                    self.killControl()
                    self.boxHitControl()
                if event.key == pg.K_ESCAPE:
                    if self.playing:
                        self.playing = False
                    self.running = False
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.attacking = False

    def killControl(self):
        if (self.king.rect.x + self.king.rect.width > self.kingPig.rect.x and self.king.rect.x + self.king.rect.width < self.kingPig.rect.x + self.kingPig.rect.width) or (self.king.rect.x > self.kingPig.rect.x and self.king.rect.x < self.kingPig.rect.x + self.kingPig.rect.width):
            # if pg.sprite.collide_rect(self.king, self.kingPig):
            self.kingPig.dying = True
            self.x = True
            self.now = pg.time.get_ticks()
            # self.kingPig.animate()
            hits = pg.sprite.spritecollide(self.king, self.kingPigs, False)
            # self.all_sprites.remove(self.kingPig)
            # self.kingPigs.remove(self.kingPig)
            self.deadCount += 1
            if self.deadCount >= 2:
                self.pigCreate()
                self.createBoxes()
        if (self.king.rect.x + self.king.rect.width > self.kingPig2.rect.x and self.king.rect.x + self.king.rect.width < self.kingPig2.rect.x + self.kingPig2.rect.width) or (self.king.rect.x > self.kingPig2.rect.x and self.king.rect.x < self.kingPig2.rect.x + self.kingPig2.rect.width):
            # if pg.sprite.collide_rect(self.king, self.kingPig):
            self.kingPig2.dying = True
            self.y = True
            self.now2 = pg.time.get_ticks()
            # self.kingPig2.animate()
            hits = pg.sprite.spritecollide(self.king, self.kingPigs, False)
            # self.all_sprites.remove(self.kingPig2)
            # self.kingPigs.remove(self.kingPig2)
            self.deadCount += 1
            if self.deadCount >= 2:
                self.pigCreate()
                self.createBoxes()
        if self.isPigsExist:
            # if pg.sprite.collide_rect(self.king, self.pig):
            if (self.king.rect.x + self.king.rect.width > self.pig.rect.x and self.king.rect.x + self.king.rect.width < self.pig.rect.x + self.pig.rect.width) or (self.king.rect.x > self.pig.rect.x and self.king.rect.x < self.pig.rect.x + self.pig.rect.width):
                # self.kingPig.dying = True
                # self.kingPig.animate()
                hits = pg.sprite.spritecollide(self.king, self.pigs, True, pg.sprite.collide_rect)
                self.now3 = pg.time.get_ticks()

    def pigCreate(self):
        self.pig = Pig()
        self.pigs.add(self.pig)
        self.all_sprites.add(self.pig)
        self.isPigsExist = True

    def createBoxes(self):
        self.box = Box()
        self.box2 = Box(posV = vec(WIDTH - 450, HEIGHT - 200))
        self.boxes = pg.sprite.Group()
        self.boxes.add(self.box)
        self.boxes.add(self.box2)
        self.all_sprites.add(self.box)
        self.all_sprites.add(self.box2)
        self.isBoxesExist = True
    # When king get into the mobs' border
    def mobFocus(self):
        count = 0
        for border in self.borders:
            count += 1
            # if king in the border
            if(self.king.rect.x < border[1]):
                # Kingpig 1
                if(count == 1):
                    self.kingPig.facing = 'right'
                    if(self.kingPig.vel.x > 0):
                        self.kingPig.acc.x = 0.35
                    else:
                        self.kingPig.vel.x *= -1
                        self.kingPig.acc.x = 0.35
                # Kingpig 2
                elif(count == 2):
                    if(count == 1):
                        self.kingPig2.facing = 'left'
                        if(self.kingPig2.vel.x > 0):
                            self.kingPig2.acc.x = 0.35
                        else:
                            self.kingPig2.vel.x *= -1
                            self.kingPig2.acc.x = 0.35
            else:
                if(count == 1):
                    if(self.kingPig.vel.x > 0):
                        self.kingPig.acc.x = 0.25
                    else:
                        self.kingPig.acc.x = -0.25
                elif(count == 2):
                    if(self.kingPig2.vel.x > 0):
                        self.kingPig2.acc.x = 0.25
                    else:
                        self.kingPig2.acc.x = -0.25

    def showLevel2(self):
        if self.isPigsExist:
            self.drawLevel2("Level2", 48, WIDTH/2, HEIGHT/2-50)

    def hitControl(self):
        if ((self.king.rect.x + self.king.rect.width > self.kingPig.rect.x and self.king.rect.x + self.king.rect.width < self.kingPig.rect.x + self.kingPig.rect.width) or (self.king.rect.x > self.kingPig.rect.x and self.king.rect.x < self.kingPig.rect.x + self.kingPig.rect.width) and (self.king.attacking == False)):
            # King get hit from kingPig
            self.hit()
            self.king.pos.x -= 15
            self.kingPig.attacking = True
        else:
            self.kingPig.attacking = False
        if ((self.king.rect.x + self.king.rect.width > self.kingPig2.rect.x and self.king.rect.x + self.king.rect.width < self.kingPig2.rect.x + self.kingPig2.rect.width) or (self.king.rect.x > self.kingPig2.rect.x and self.king.rect.x < self.kingPig2.rect.x + self.kingPig2.rect.width) and (self.king.attacking == False)):
            # King get hit from kingPig2
            self.hit()
            self.king.pos.x += 15
            self.kingPig2.attacking = True
        else:
            self.kingPig2.attacking = False

    def boxHitControl(self):
        if self.isBoxesExist:
            if (self.king.rect.x + self.king.rect.width > self.box.rect.x and self.king.rect.x + self.king.rect.width < self.box.rect.x + self.box.rect.width) or (self.king.rect.x > self.box.rect.x and self.king.rect.x < self.box.rect.x + self.box.rect.width):
                if self.box.health > 0:
                    self.box.hitting = True
                    self.box.health -= 35
                else:
                    pg.sprite.spritecollide(self.king, self.boxes, True)
                
            if (self.king.rect.x + self.king.rect.width > self.box2.rect.x and self.king.rect.x + self.king.rect.width < self.box2.rect.x + self.box2.rect.width) or (self.king.rect.x > self.box2.rect.x and self.king.rect.x < self.box2.rect.x + self.box2.rect.width):
                if self.box2.health > 0:
                    self.box2.hitting = True
                    self.box2.health -= 35
                else:
                    pg.sprite.spritecollide(self.king, self.boxes, True)
    def hit(self):
        if self.king.health > 0:
            self.king.health -= 10
            self.king.hitting = True

        else:
            self.king.dying = True
            self.nowK = pg.time.get_ticks()
            self.z = True
            self.king.pos.y -= 5

    def draw_shield_bar(self, surf, x, y, pct):
        if pct < 0:
            pct = 0
        BAR_LENGTH = 100
        BAR_HEIGHT = 10
        fill = (pct / 200) * BAR_LENGTH
        outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
        pg.draw.rect(surf, (0, 255, 0), fill_rect)
        pg.draw.rect(surf, (255, 255, 255), outline_rect, 2)

    def drawLevel2(self, text, size, x, y):
        font = pg.font.Font(pg.font.match_font('arial'), size)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw(self):
        # Game Loop - draw
        self.screen.blit(background, (bgX, 0))
        self.screen.blit(background, (bgX2, 0))
        self.all_sprites.draw(self.screen)
        self.draw_shield_bar(self.screen, self.king.rect.x-15,
                             self.king.rect.y-10, self.king.health)
        # *after* drawing everything, flip the display
        #pg.draw.rect(self.screen, (255,0,0), self.king.rect, 1)
        self.showLevel2()
        pg.display.flip()

    def show_start_screen(self):
        self.screen.blit(startScreen, (0, 0))
        # game splash/start screen
        # self.screen.fill((255, 255, 255))
        # self.draw_text('Project', 48, (255, 255, 255), WIDTH / 2, HEIGHT / 4)
        # self.draw_text("Arrows to move, Space to jump", 22, (255, 255, 255), WIDTH / 2, HEIGHT / 2)
        # self.draw_text("Press a key to play", 22, (255, 255, 255), WIDTH / 2, HEIGHT * 3 / 4)
        # self.draw_text("High Score: " + str(self.highscore), 22, (255, 255, 255), WIDTH / 2, 15)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        # game over/continue
        if not self.running:
            return
        self.screen.blit(gameOver, (0, 0))
        # self.draw_text("GAME OVER", 48, (255, 255, 255), WIDTH / 2, HEIGHT / 4)
        # self.draw_text("Score: " + str(self.score), 22, (255, 255, 255), WIDTH / 2, HEIGHT / 2)
        # self.draw_text("Press a key to play again", 22, (255, 255, 255), WIDTH / 2, HEIGHT * 3 / 4)
        # if self.score > self.highscore:
        #     self.highscore = self.score
        #     self.draw_text("NEW HIGH SCORE!", 22, (255, 255, 255), WIDTH / 2, HEIGHT / 2 + 40)
        #     # with open('HS_FILE.txt', 'w') as f:
        #     #     f.write(str(self.score))
        # else:
        #     self.draw_text("High Score: " + str(self.highscore), 22, (255, 255, 255), WIDTH / 2, HEIGHT / 2 + 40)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(30)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    # def draw_text(self, text, size, color, x, y):
    #     font = pg.font.Font(self.font_name, size)
    #     text_surface = font.render(text, True, color)
    #     text_rect = text_surface.get_rect()
    #     text_rect.midtop = (x, y)
    #     self.screen.blit(text_surface, text_rect)

class TileMap:
    def __init__(self):
        pass

    def loadData(self):
        pass

class King(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = kingGround.convert()
        self.rect = self.image.get_rect()
        #self.rect = self.rect.move(self.rect.x + 55, self.rect.y + 40)
        self.rect = self.rect.inflate(-20, -4)
        # pg.transform.scale(self.rect, (39, 29), (self.rect.x + 10, self.rect.y + 9))
        # self.image.set_colorkey((0, 0, 0))
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.frame_counter = 0
        self.walking = False   
        self.jumping = False
        self.last_update = 0
        self.current_frame = 0
        self.jumpCount = 10
        self.walkingRight = False
        self.attacking = False
        self.facing = True
        self.health = 200
        self.dying = False
        self.dead = False
        self.hitting = False
        self.ctr = 0

    def update(self):
        self.animate()
        self.acc = vec(0, 0.8)
        if self.dead == True:
            self.vel.x = 0
            self.acc.x = 0
        if self.pos.x <= 0 and not self.dead:
            self.pos.x = 0
        if self.pos.x + self.rect.width >= WIDTH and not self.dead:
            self.pos.x = WIDTH - self.rect.width
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and not self.dead:
            self.acc.x = -0.5
            self.walkingRight = False
            self.facing = False
            # scrollBackground(-5,0)
        if keys[pg.K_RIGHT] and not self.dead:
            self.acc.x = 0.5
            self.walkingRight = True
            self.facing = True
            # scrollBackground(5,0)

        # apply friction
        self.acc.x += self.vel.x * (-0.12)
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

    def jump(self):
        # self.vel.y = -10
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 1
        if hits:
            self.vel.y = -10

    def animate(self):
        now = pg.time.get_ticks()
        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False
            self.walkingRight = False
        # Walking
        if self.walking and not (self.dying or self.dead):
            if now - self.last_update > 240:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(kingRun)
                bottom = self.rect.bottom
                if self.vel.x > 0:
                    self.image = kingRun[self.current_frame]
                    self.rect = self.image.get_rect()
                    self.rect = self.rect.inflate(-20, -12)
                else:
                    self.image = kingRunL[self.current_frame]
                    self.rect = self.image.get_rect()
                    self.rect = self.rect.inflate(-15, -12)
                self.rect.bottom = bottom
        # Idling
        if not self.walking and not self.jumping and not (self.dying or self.dead):
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(kingIdle)
                bottom = self.rect.bottom
                self.image = kingIdle[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect = self.rect.inflate(-28, -12)
                self.rect.bottom = bottom
        if self.attacking and not (self.dying or self.dead):
            if self.facing == True:
                self.current_frame = (self.current_frame + 1) % len(kingAttack)
                bottom = self.rect.bottom
                self.image = kingAttack[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect = self.rect.inflate(-5, -12)
                self.rect.bottom = bottom
            else:
                self.current_frame = (
                    self.current_frame + 1) % len(kingAttackL)
                bottom = self.rect.bottom
                self.image = kingAttackL[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect = self.rect.inflate(-40, -12)
                self.rect.bottom = bottom
            self.attacking = False
        if self.hitting and not (self.dying or self.dead):
            if now - self.last_update > 240:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(kingHit)
                bottom = self.rect.bottom
                self.image = kingHit[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect = self.rect.inflate(-20, -12)
                self.rect.bottom = bottom
                self.ctr += 1
                if self.ctr >= 4:
                    self.hitting = False
                    self.ctr = 0

        if self.dying:
            if now - self.last_update > 240:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(kingDead)
                bottom = self.rect.bottom
                self.image = kingDead[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
                if self.current_frame >= 3:
                    self.dying = False
                    self.dead = True
        if self.dead:
            if now - self.last_update > 120:
                self.last_update = now
                self.current_frame = 3
                bottom = self.rect.bottom
                self.image = kingDead[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0, 0, 0))
        self.rect.x = x
        self.rect.y = y

class KingPig(pg.sprite.Sprite):
    def __init__(self, posV=vec(WIDTH - 80, HEIGHT - 50)):
        pg.sprite.Sprite.__init__(self)
        self.image = kingPigKIdle[0]
        self.rect = self.image.get_rect()
        self.rect.center = (posV.x, posV.y)
        self.image.set_colorkey((0, 0, 0))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.pos = posV
        self.posFirst = self.pos.x
        self.frame_counter = 0
        self.last_update = 0
        self.current_frame = 0
        self.dying = False
        self.dead = False
        self.deadCount = 0
        self.facing = 'right'
        self.attacking = False
        self.ctr = 0

    def update(self):
        self.animate()
        self.acc = vec(0.25, 0.8)  # 0.8=GRAVITY
        if self.dead == True:
            self.vel.x = 0
            self.acc.x = 0
        # x <= 100 -100      x <= 0  soldaki mob     sol sınır
        # x <= 700 - 100    x <= 600
        if self.pos.x <= self.posFirst - 50 and not self.dead:
            self.acc.x = 0.25
            self.current_frame = 0
            self.facing = 'right'
        # x >= 200
        # x >= 800
        elif self.pos.x >= self.posFirst + 50 and not self.dead:
            self.acc.x = -0.25
            self.current_frame = 0
            self.facing = 'left'
        # x > 0 and x < 200
        # x > 600 and x < 800
        elif self.pos.x > self.posFirst - 50 and self.pos.x < self.posFirst + 50 and not self.dead:
            if self.vel.x > 0:
                self.acc.x = 0.25
                self.facing = 'right'
            else:
                self.acc.x = -0.25
                self.facing = 'left'

        # apply friction
        self.acc.x += self.vel.x * (-0.12)
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

    def animate(self):
        now = pg.time.get_ticks()
        if self.vel.x > 0.1 or self.vel.x < -0.1:
            self.walking = True
        else:
            self.walking = False
        if self.walking and not (self.dying or self.dead):
            if now - self.last_update > 120:
                self.last_update = now
                self.current_frame = (
                    self.current_frame + 1) % len(kingPigRunRight)
                bottom = self.rect.bottom
                if self.vel.x > 0.1:
                    self.image = kingPigRunRight[self.current_frame]
                else:
                    self.image = kingPigRunLeft[self.current_frame]
                self.rect = self.image.get_rect()
                # if self.walkingRight:
                #     self.rect = self.rect.inflate(-20, -12)
                # else:
                #     self.rect = self.rect.inflate(-20, -12)
                self.rect.bottom = bottom

        if self.attacking and not(self.dying or self.dead):
            self.current_frame = (self.current_frame + 1) % len(kingPigAttack)
            bottom = self.rect.bottom
            if self.facing == 'right':
                self.image = kingPigAttack[self.current_frame]
            else:
                self.image = kingPigAttackLeft[self.current_frame]
            self.rect = self.image.get_rect()
            # if self.walkingRight:
            #     self.rect = self.rect.inflate(-20, -12)
            # else:
            # self.rect = self.rect.inflate(-20, -12)
            self.rect.bottom = bottom

        # DEAD ANIMATION
        if self.dying:
            # if self.deadCount >= 3*len(kingPigDead):
            #     self.deadCount = 11
            # self.image = kingPigDead[self.deadCount//3]
            # if self.deadCount != 11:
            #     self.deadCount += 1
            # else:
            #     self.dead = True
            #     self.dying = False
            if now - self.last_update > 240:
                self.last_update = now
                self.current_frame = (
                    self.current_frame + 1) % len(kingPigDead)
                bottom = self.rect.bottom
                self.image = kingPigDead[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
                if self.current_frame >= 3:
                    self.dying = False
                    self.dead = True

        if self.dead:
            if now - self.last_update > 120:
                self.last_update = now
                self.current_frame = 3
                bottom = self.rect.bottom
                self.image = kingPigDead[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

class Pig(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pigIdle[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH - 280, HEIGHT - 200)
        self.image.set_colorkey((0, 0, 0))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.pos = vec(WIDTH - 280, HEIGHT - 200)
        self.posFirst = self.pos.x
        self.frame_counter = 0
        self.last_update = 0
        self.current_frame = 0
        self.dying = False
        self.dead = False
        self.deadCount = 0

    def update(self):
        self.animate()
        self.acc = vec(0.25, 0.8)  # 0.8=GRAVITY
        if self.dead == True:
            self.vel.x = 0
            self.acc.x = 0
        # x <= 100 -100      x <= 0  soldaki mob     sol sınır
        # x <= 700 - 100    x <= 600
        if self.pos.x <= self.posFirst - 50 and not self.dead:
            self.acc.x = 0.25
            self.current_frame = 0
        # x >= 200
        # x >= 800
        elif self.pos.x >= self.posFirst + 50 and not self.dead:
            self.acc.x = -0.25
            self.current_frame = 0
        # x > 0 and x < 200
        # x > 600 and x < 800
        elif self.pos.x > self.posFirst - 50 and self.pos.x < self.posFirst + 50 and not self.dead:
            if self.vel.x > 0:
                self.acc.x = 0.25
            else:
                self.acc.x = -0.25
        # apply friction
        self.acc.x += self.vel.x * (-0.12)
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

    def animate(self):
        now = pg.time.get_ticks()
        if self.vel.x > 0.1 or self.vel.x < -0.1:
            self.walking = True
        else:
            self.walking = False
        if self.walking:
            if now - self.last_update > 120:
                self.last_update = now
                self.current_frame = (
                    self.current_frame + 1) % len(pigRunRight)
                bottom = self.rect.bottom
                if self.vel.x > 0.1:
                    self.image = pigRunLeft[self.current_frame]
                else:
                    self.image = pigRunRight[self.current_frame]
                self.rect = self.image.get_rect()
                # if self.walkingRight:
                #     self.rect = self.rect.inflate(-20, -12)
                # else:
                #     self.rect = self.rect.inflate(-20, -12)
                self.rect.bottom = bottom
        # # DEAD ANIMATION
        # if self.dying:
        #     if self.deadCount >= 3*len(kingPigDead):
        #         self.deadCount = 11
        #     self.image = kingPigDead[self.deadCount//3]
        #     if self.deadCount != 11:
        #         self.deadCount += 1
        #     else:
        #         self.dead = True
        #         self.dying = False
        #     # if now - self.last_update > 500:
        #     #     self.last_update = now
        #     #     self.current_frame = (self.current_frame + 1) % len(kingPigDead)
        #     #     bottom = self.rect.bottom
        #     #     self.image = kingPigDead[self.current_frame]
        #     #     self.rect = self.image.get_rect()
        #     #     self.rect.bottom = bottom
        #     # self.dying = False
        #     # self.dead = True

class Box(pg.sprite.Sprite):
    def __init__(self, posV = vec(WIDTH - 280, HEIGHT - 200)):
        pg.sprite.Sprite.__init__(self)
        self.image = boxIdle
        self.rect = self.image.get_rect()
        self.rect.center = (posV.x, posV.y)
        self.image.set_colorkey((0, 0, 0))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.pos = posV
        self.idling = True
        self.hitting = False
        self.current_frame = 0
        self.ctr = 0
        self.health = 100
        self.last_update = 0
    def update(self):
        self.animate()
        self.acc = vec(0, 0.8)
        # apply friction
        self.acc.x += self.vel.x * (-0.12)
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
    def animate(self):
        now = pg.time.get_ticks()
        # Idling
        if self.idling:
            if now - self.last_update > 200:
                    self.last_update = now
                    bottom = self.rect.bottom
                    self.image = boxIdle
                    self.rect = self.image.get_rect()
                    #self.rect = self.rect.inflate(-28, -12)
                    self.rect.bottom = bottom
        if self.hitting:
            if now - self.last_update > 800:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(boxHit)
                bottom = self.rect.bottom
                self.image = boxHit[self.current_frame]
                self.rect = self.image.get_rect()
                #self.rect = self.rect.inflate(-20, -12)
                self.rect.bottom = bottom
                self.ctr += 1
                if self.ctr >= 6:
                    self.hitting = False
                    self.ctr = 0

game = Game()
game.show_start_screen()
while game.running:
    game.new()
    game.show_go_screen()
pg.quit()
