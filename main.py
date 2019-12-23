import pygame as pg
import os
import time
import random
vec = pg.math.Vector2

# CONSTS
WIDTH = 800
HEIGHT = 600
FPS = 30

# Image & Sound Directory
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'img')
sound_path = os.path.join(current_path, 'music')

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
pigAttackLeft = [pg.image.load(os.path.join(image_path, 'tile000PigA.png')), pg.image.load(os.path.join(image_path, 'tile001PigA.png')), pg.image.load(os.path.join(image_path, 'tile002PigA.png')), pg.image.load(os.path.join(image_path, 'tile003PigA.png')), pg.image.load(os.path.join(image_path, 'tile004PigA.png'))]
pigAttackRight = [pg.transform.flip(pigAttackLeft[0], True, False), pg.transform.flip(pigAttackLeft[1], True, False), pg.transform.flip(pigAttackLeft[2], True, False), pg.transform.flip(pigAttackLeft[3], True, False), pg.transform.flip(pigAttackLeft[4], True, False)]

# Cannon Images
cannonIdle = pg.image.load(os.path.join(image_path, 'tile000CannonI.png'))
cannonShoot = [pg.image.load(os.path.join(image_path, 'tile000CannonS.png')), pg.image.load(os.path.join(image_path, 'tile001CannonS.png')), pg.image.load(
    os.path.join(image_path, 'tile002CannonS.png')), pg.image.load(os.path.join(image_path, 'tile003CannonS.png'))]
cannonBall = pg.image.load(os.path.join(image_path, 'tile000CannonB.png'))

# Lives Image
heartIdle = [pg.image.load(os.path.join(image_path, 'tile000HeartI.png')), pg.image.load(os.path.join(image_path, 'tile001HeartI.png')), pg.image.load(os.path.join(image_path, 'tile002HeartI.png')), pg.image.load(os.path.join(image_path, 'tile003HeartI.png')), pg.image.load(os.path.join(image_path, 'tile004HeartI.png')), pg.image.load(os.path.join(image_path, 'tile005HeartI.png')), pg.image.load(os.path.join(image_path, 'tile006HeartI.png')), pg.image.load(os.path.join(image_path, 'tile007HeartI.png'))]

# Box Images
boxIdle = pg.image.load(os.path.join(image_path, 'tile000BoxI.png'))
boxHit = [boxIdle, pg.image.load(os.path.join(image_path, 'tile000BoxH.png'))]

# Diamond Images
diamondIdle = [pg.image.load(os.path.join(image_path, 'tile000DiamondI.png')), pg.image.load(os.path.join(image_path, 'tile001DiamondI.png')), pg.image.load(os.path.join(image_path, 'tile002DiamondI.png')), pg.image.load(os.path.join(image_path, 'tile003DiamondI.png')), pg.image.load(os.path.join(image_path, 'tile004DiamondI.png')), pg.image.load(
    os.path.join(image_path, 'tile005DiamondI.png')), pg.image.load(os.path.join(image_path, 'tile006DiamondI.png')), pg.image.load(os.path.join(image_path, 'tile007DiamondI.png')), pg.image.load(os.path.join(image_path, 'tile008DiamondI.png')), pg.image.load(os.path.join(image_path, 'tile009DiamondI.png'))]

# Heart Images
heartIdle = [pg.image.load(os.path.join(image_path, 'tile000HeartI.png')), pg.image.load(os.path.join(image_path, 'tile001HeartI.png')), pg.image.load(os.path.join(image_path, 'tile002HeartI.png')), pg.image.load(os.path.join(image_path, 'tile003HeartI.png')), pg.image.load(os.path.join(image_path, 'tile004HeartI.png')), pg.image.load(
    os.path.join(image_path, 'tile005HeartI.png')), pg.image.load(os.path.join(image_path, 'tile006HeartI.png')), pg.image.load(os.path.join(image_path, 'tile007HeartI.png'))]


# Spirit Images
spirit = [pg.image.load(os.path.join(image_path, 'tile000Spirit.png')), pg.image.load(os.path.join(image_path, 'tile001Spirit.png')), pg.image.load(os.path.join(image_path, 'tile002Spirit.png')), pg.image.load(os.path.join(image_path, 'tile003Spirit.png')), pg.image.load(os.path.join(image_path, 'tile004Spirit.png')), pg.image.load(os.path.join(image_path, 'tile005Spirit.png')), pg.image.load(os.path.join(image_path, 'tile006Spirit.png'))]

# GraveStone Images
graveStone = pg.image.load(os.path.join(image_path, 'gravestone.png'))

# Ork Images
orkIdle = [pg.image.load(os.path.join(image_path, 'tile000OrkI.png')), pg.image.load(os.path.join(image_path, 'tile001OrkI.png')), pg.image.load(os.path.join(image_path, 'tile002OrkI.png')), pg.image.load(os.path.join(image_path, 'tile003OrkI.png')), pg.image.load(os.path.join(image_path, 'tile004OrkI.png')), pg.image.load(os.path.join(image_path, 'tile005OrkI.png')), pg.image.load(os.path.join(image_path, 'tile006OrkI.png'))]
orkWalking = [pg.image.load(os.path.join(image_path, 'tile000OrkR.png')), pg.image.load(os.path.join(image_path, 'tile001OrkR.png')), pg.image.load(os.path.join(image_path, 'tile002OrkR.png')), pg.image.load(os.path.join(image_path, 'tile003OrkR.png')), pg.image.load(os.path.join(image_path, 'tile004OrkR.png')), pg.image.load(os.path.join(image_path, 'tile005OrkR.png')), pg.image.load(os.path.join(image_path, 'tile006OrkR.png'))]
orkAttack = [pg.image.load(os.path.join(image_path, 'tile000OrkA.png')), pg.image.load(os.path.join(image_path, 'tile001OrkA.png')), pg.image.load(os.path.join(image_path, 'tile002OrkA.png')), pg.image.load(os.path.join(image_path, 'tile003OrkA.png')), pg.image.load(os.path.join(image_path, 'tile004OrkA.png')), pg.image.load(os.path.join(image_path, 'tile005OrkA.png')), pg.image.load(os.path.join(image_path, 'tile006OrkA.png'))]
orkHit = [pg.image.load(os.path.join(image_path, 'tile000OrkH.png')), pg.image.load(os.path.join(image_path, 'tile001OrkH.png')), pg.image.load(os.path.join(image_path, 'tile002OrkH.png')), pg.image.load(os.path.join(image_path, 'tile003OrkH.png')), pg.image.load(os.path.join(image_path, 'tile004OrkH.png')), pg.image.load(os.path.join(image_path, 'tile005OrkH.png')), pg.image.load(os.path.join(image_path, 'tile006OrkH.png'))]
orkDie = [pg.image.load(os.path.join(image_path, 'tile000OrkD.png')), pg.image.load(os.path.join(image_path, 'tile001OrkD.png')), pg.image.load(os.path.join(image_path, 'tile002OrkH.png')), pg.image.load(os.path.join(image_path, 'tile003OrkD.png')), pg.image.load(os.path.join(image_path, 'tile004OrkD.png')), pg.image.load(os.path.join(image_path, 'tile005OrkD.png')), pg.image.load(os.path.join(image_path, 'tile006OrkD.png'))]

# Explosion Images
explosion = [pg.image.load(os.path.join(image_path, 'tile000Exp.png')), pg.image.load(os.path.join(image_path, 'tile001Exp.png')), pg.image.load(os.path.join(image_path, 'tile002Exp.png')), pg.image.load(os.path.join(image_path, 'tile003Exp.png')), pg.image.load(os.path.join(image_path, 'tile004Exp.png')), pg.image.load(os.path.join(image_path, 'tile005Exp.png'))]

# Boom Dialogbox Images
boomIn = [pg.image.load(os.path.join(image_path, 'tile000BoomIn.png')), pg.image.load(os.path.join(image_path, 'tile001BoomIn.png')), pg.image.load(os.path.join(image_path, 'tile002BoomIn.png'))]
boomOut = [pg.image.load(os.path.join(image_path, 'tile000BoomOut.png')), pg.image.load(os.path.join(image_path, 'tile001BoomOut.png'))]

# WTF Dialogbox Images
WtfIn = [pg.image.load(os.path.join(image_path, 'tile000WTFIn.png')), pg.image.load(os.path.join(image_path, 'tile001WTFIn.png')), pg.image.load(os.path.join(image_path, 'tile002WTFIn.png'))]
WtfOut = [pg.image.load(os.path.join(image_path, 'tile000WTFOut.png')), pg.image.load(os.path.join(image_path, 'tile001WTFOut.png'))]

# Loser Dialogbox Images
loserIn = [pg.transform.scale2x(pg.image.load(os.path.join(image_path, 'tile000LoserIn.png'))), pg.transform.scale2x(pg.image.load(os.path.join(image_path, 'tile001LoserIn.png'))), pg.transform.scale2x(pg.image.load(os.path.join(image_path, 'tile002LoserIn.png')))]
loserOut = [pg.transform.scale2x(pg.image.load(os.path.join(image_path, 'tile000LoserOut.png'))), pg.transform.scale2x(pg.image.load(os.path.join(image_path, 'tile001LoserOut.png')))]


# BG Images
startScreen = [pg.transform.scale(pg.image.load(os.path.join(image_path, 'ss.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'ss1.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'ss2.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'ss3.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'ss4.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'ss5.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'ss6.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'ss7.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'ss8.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'ss9.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'ss10.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'ss11.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'ss12.png')), (WIDTH, HEIGHT))]
gameOver = pg.image.load(os.path.join(image_path, 'gameover_screen.png'))
winScreen = [pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_00_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_01_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_02_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_03_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_04_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_05_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_06_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_07_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_08_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_09_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_10_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_11_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_12_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_13_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_14_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_15_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_16_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_17_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_18_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_19_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_20_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_21_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_22_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_23_delay-0.01s.png')), (WIDTH, HEIGHT)), pg.transform.scale(pg.image.load(os.path.join(image_path, 'frame_24_delay-0.01s.png')), (WIDTH, HEIGHT))]
# Fitting images to screen
gameOver = pg.transform.scale(gameOver, (WIDTH, HEIGHT))
background = pg.image.load(os.path.join(image_path, 'background.png'))
background = pg.transform.scale(
    background, (WIDTH, HEIGHT))    # Fitting images to screen
# successScreen = pg.image.load(os.path.join(image_path, 'win_screen.png'))
# successScreen = pg.transform.scale(successScreen, (WIDTH, HEIGHT))
bgX = 0
bgX2 = background.get_width()



# ** Classes
# Game Class
class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)
        pg.display.set_caption('Kings And Pigs')
        self.explosionSound = pg.mixer.Sound(os.path.join(sound_path, 'Cannon+5.wav'))
        self.axeSound = pg.mixer.Sound(os.path.join(sound_path, 'axe_sound.wav'))
        self.woosh = pg.mixer.Sound(os.path.join(sound_path, 'woosh.wav'))
        self.hitsound = pg.mixer.Sound(os.path.join(sound_path, 'hit.wav'))
        self.log = pg.mixer.Sound(os.path.join(sound_path, 'log.wav')) 
        self.success = pg.mixer.Sound(os.path.join(sound_path, 'success.wav')) 
        self.king_yes = pg.mixer.Sound(os.path.join(sound_path, 'king_yes.wav')) 
        self.stone = pg.mixer.Sound(os.path.join(sound_path, 'stone.aiff')) 
        self.woodcreak = pg.mixer.Sound(os.path.join(sound_path, 'woodcreak.wav')) 
        self.pigattack = pg.mixer.Sound(os.path.join(sound_path, 'pigatack.wav'))
        self.pigattack.set_volume(0.6)
        self.monsterscream = pg.mixer.Sound(os.path.join(sound_path, 'monsterscream.wav'))
        self.monsterscream.set_volume(0.7)
        self.orkAttack = pg.mixer.Sound(os.path.join(sound_path, 'OrkFight.wav'))
        self.orkWalk = pg.mixer.Sound(os.path.join(sound_path, 'OrkWalk.wav'))
        pg.mixer.music.load(os.path.join(sound_path, 'background.mp3'))
        pg.mixer.music.set_volume(0.6)
        pg.mixer.music.play(loops = -1)
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
        self.isDiamondsExist = False
        self.control = 0
        self.control2 = 0
        self.isCannonExist = False
        self.isCannonBallExist = False
        self.isGraveStoneExist = False
        self.isKingPig3Exist = False
        self.isOrkExist = False
        self.background = background
        self.durum = True
        self.ctr3 = 0
        self.isHeartExist = False
        self.last_update = pg.time.get_ticks() 
        self.current_frame = 0
        self.current_frame2 = 0
        self.issuccess = False
        self.c = 0

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
        self.platform = Platform(0, HEIGHT-55, WIDTH, 55)
        self.platforms = pg.sprite.Group()
        self.platforms.add(self.platform)
        self.all_sprites.add(self.platform)
        self.diamonds = pg.sprite.Group()
        self.cannons = pg.sprite.Group()
        self.cannonBalls = pg.sprite.Group()
        self.boxes = pg.sprite.Group()
        self.spirits = pg.sprite.Group()
        self.graveStones = pg.sprite.Group()
        self.orks = pg.sprite.Group()
        self.hearts = pg.sprite.Group()
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

        if self.issuccess:
            self.playing = False

        # check if player hits a platform - only if falling(=GRAVITY)
        self.hitControl()

        self.cannonBallHitControl()
        # Control if diamond has taken
        # self.diamondControl()

        # self.mobFocus()

        if self.king.vel.y > 0:
            hits = pg.sprite.spritecollide(self.king, self.platforms, False)
            if hits:
                self.king.pos.y = hits[0].rect.top
                self.king.vel.y = 0

        for kingpig in self.kingPigs:
            hits = pg.sprite.spritecollide(kingpig, self.platforms, False)
            if hits:
                kingpig.pos.y = hits[0].rect.top
                kingpig.vel.y = 0

        if self.isBoxesExist:
            for box in self.boxes:
                if box.vel.y > 0:
                    hits = pg.sprite.spritecollide(box, self.platforms, False)
                    if hits:
                        box.pos.y = hits[0].rect.top
                        box.vel.y = 0

        if self.isPigsExist:
            for pig in self.pigs:
                if pig.vel.y > 0:
                    hits = pg.sprite.spritecollide(pig, self.platforms, False)
                    if hits:
                        pig.pos.y = hits[0].rect.top
                        pig.vel.y = 0

        if self.isDiamondsExist:
            for diamond in self.diamonds:
                hits = pg.sprite.spritecollide(diamond, self.platforms, False)
                if hits:
                    diamond.pos.y = hits[0].rect.top
                    diamond.vel.y = 0

        if self.isHeartExist:
            for heart in self.hearts:
                hits = pg.sprite.spritecollide(heart, self.platforms, False)
                if hits:
                    heart.pos.y = hits[0].rect.top
                    heart .vel.y = 0

        

        if self.isCannonExist:
            for cannon in self.cannons:
                hits = pg.sprite.spritecollide(cannon, self.platforms, False)
                if hits:
                    cannon.pos.y = hits[0].rect.top
                    cannon.vel.y = 0
        
        if self.isOrkExist:
            for ork in self.orks:
                hits = pg.sprite.spritecollide(ork, self.platforms, False)
                if hits:
                    ork.pos.y = hits[0].rect.top
                    ork.vel.y = 0

        if self.isGraveStoneExist:
            for gravestone in self.graveStones:
                hits = pg.sprite.spritecollide(gravestone, self.platforms, False)
                if hits:
                    gravestone.pos.y = hits[0].rect.top
                    gravestone.vel.y = 0

        
        self.xd = pg.time.get_ticks()

        # if self.z == True:
        #     if self.xd - self.nowK >= 300:
        #         self.nowK = pg.time.get_ticks()
        #         pg.sprite.spritecollide(self.kingPig, self.kings, True)
        #         self.z = False
        #         self.playing = False

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
                    # self.axeSound.play()
                    self.woosh.play()
                    if self.isGraveStoneExist:
                        self.graveStoneControl()
                if event.key == pg.K_ESCAPE:
                    if self.playing:
                        self.playing = False
                    self.running = False
                if event.key == pg.K_e:
                    self.diamondControl()
                    self.heartControl()
                    xd = self.cannonControl()
                    self.createCannonBall()
                    if xd:
                        self.explosionSound.play()
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.attacking = False

    def killControl(self):
        for kingpig in self.kingPigs:
            hits = pg.sprite.spritecollide(self.king, self.kingPigs, False, pg.sprite.collide_rect)
            if hits:
                for hit in hits:
                    self.hitsound.play()
                    hit.dying = True
                    # self.createSpirit(center = kingpig.pos)
                    # hit.rect.width = 0
                    # hit.rect.height = 0
                    if len(self.kingPigs) == 1:
                        if self.ctr3 == 0:
                            self.pigCreate()
                            self.ctr3 += 1
                            self.createBoxes(posV=vec(WIDTH-400,HEIGHT-200))
                    # self.createBoxes(posV = hit.pos)
        # Control if pig dies
        for pig in self.pigs:
            hits = pg.sprite.spritecollide(self.king, self.pigs, True, pg.sprite.collide_rect)
            if hits:
                for hit in hits:
                    self.hitsound.play()
                    self.createSpirit(center = pig.pos)
                    hit.rect.width = 0
                    hit.rect.height = 0
                self.createCannon()
                self.createNewKingPig()
        if self.isOrkExist:
            hits = pg.sprite.spritecollide(self.king, self.orks, False, pg.sprite.collide_rect)
            if hits:
                for hit in hits:
                    if hit.health > 0:
                        hit.health -= 20
                        hit.hitting = True
                    else:
                        hit.dying = True
                        self.king_yes.play()
                        self.issuccess = True

    def cannonBallHitControl(self):
        if self.isCannonBallExist:
            hits = pg.sprite.groupcollide(self.kingPigs, self.cannonBalls, True, True)
            if hits:
                for hit in hits:
                    exp = Explosion(hit.rect.center)
                    self.all_sprites.add(exp)
                    self.cannon.kill()
                    self.createCannon(posX = vec(WIDTH - 100, HEIGHT - 100))
                    self.createMobArmy()
                    wtfin = WTFIn((self.king.rect.center[0] + 5, self.king.rect.center[1] - 45))
                    wtfout = WTFOut((self.king.rect.center[0] + 5, self.king.rect.center[1] - 45))
                    self.all_sprites.add(wtfin)
                    self.all_sprites.add(wtfout)
                    self.king.pos = vec(self.king.pos.x + 70, self.king.pos.y - 50)
                    self.background = pg.transform.scale(pg.image.load(os.path.join(image_path, 'newbackground.png')), (WIDTH,HEIGHT))
                    self.durum = False
                    self.monsterscream.play()
        if self.isOrkExist:
            hits2 = pg.sprite.groupcollide(self.orks, self.cannonBalls, False, True)
            if hits2:
                for hit in hits2:
                    exp = Explosion(hit.rect.center)
                    self.all_sprites.add(exp)
                    if hit.health > 0:
                        hit.health -= 35
                        hit.hitting = True
                    else:
                        hit.dying = True
                        self.king_yes.play()
                        

    def pigCreate(self):
        self.pig = Pig()
        self.pigs.add(self.pig)
        self.all_sprites.add(self.pig)
        self.isPigsExist = True

    def createBoxes(self, posV):
        box = Box(posV)
        self.boxes.add(box)
        self.all_sprites.add(box)
        self.isBoxesExist = True

    def createCannon(self, posX = vec(WIDTH - 350, HEIGHT - 250)):
        self.cannon = Cannon(posV = posX)
        self.cannons.add(self.cannon)
        self.all_sprites.add(self.cannon)
        self.isCannonExist = True
        
    def createNewKingPig(self):
        self.kingPig3 = KingPig(posV = vec(50, 200))
        self.kingPigs.add(self.kingPig3)
        self.isKingPig3Exist = True
        self.all_sprites.add(self.kingPig3)
    
    def createMobArmy(self):
        ork = Ork()
        self.orks.add(ork)
        self.all_sprites.add(ork)
        self.isOrkExist = True

    def createCannonBall(self):
        if self.isCannonExist:
            if self.cannon.shooting:
                self.cannonBall = CannonBall(posV = vec(self.cannon.pos.x, self.cannon.pos.y), facing = 'Left')
                self.cannonBalls.add(self.cannonBall)
                self.all_sprites.add(self.cannonBall)
                self.isCannonBallExist = True

    def createSpirit(self, center):
        self.spirit = Spirit(center)
        self.spirits.add(self.spirit)
        self.all_sprites.add(self.spirit)

    def createGraveStone(self, posV):
        graveStone = GraveStone(posV)
        self.graveStones.add(graveStone)
        self.all_sprites.add(graveStone)
        self.isGraveStoneExist = True

    def graveStoneControl(self):
        if self.isGraveStoneExist:
            hits = pg.sprite.spritecollide(self.king, self.graveStones, False)
            if hits:
                for hit in hits:
                    if hit.health > 0:
                        hit.hitting = True
                        hit.health -= 35
                        self.stone.play()
                    else:
                        posA = hit.pos
                        hit.kill()
                        self.createDiamond(posA)
                        self.isDiamondsExist = True
                        self.stone.play()
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
        if self.isOrkExist:
            self.drawLevel2("Level2", 48, WIDTH/2, HEIGHT/2-50)

    def hitControl(self):
        hits = pg.sprite.spritecollide(self.king, self.kingPigs, False)
        if hits and not self.king.attacking:
            for hit in hits:
                # King get hit from kingPig
                itme = 15
                if hit.pos.x < self.king.pos.x:
                     itme *= -1
                self.king.pos.x -= itme
                self.hit()
                hit.attacking = True
                hit.walking = False
                self.pigattack.play()
                
        # else:
        #     for kingpig in self.kingPigs:
        #         kingpig.attacking = False
                
        if self.isPigsExist:
            hits2 = pg.sprite.spritecollide(self.king, self.pigs, False)
            if hits2 and not self.king.attacking:
                for hit in hits2:
                    # King get hit from kingPig
                    itme = 15
                    if hit.pos.x < self.king.pos.x:
                        itme *= -1
                    self.king.pos.x -= itme
                    self.hit()
                    hit.attacking = True
                    hit.walking = False
                    self.pigattack.play()

        if self.isOrkExist:
            hits3 = pg.sprite.spritecollide(self.king, self.orks, False)
            if hits3:
                for hit in hits3:
                    if not hit.dying:
                        self.orkAttack.play()
                        itme = 20
                        self.king.pos.x += itme
                        self.hit()
                        hit.attacking = True
                        hit.walking = False

    def cannonControl(self):
        if self.isCannonExist:
            hits = pg.sprite.spritecollide(self.king, self.cannons, False)
            if hits:
                for hit in hits:
                    hit.idling =  False
                    hit.shooting = True
                    boomin = BoomIn((self.king.rect.center[0] + 5, self.king.rect.center[1] - 45))
                    boomout = BoomOut((self.king.rect.center[0] + 5, self.king.rect.center[1] - 45))
                    self.all_sprites.add(boomin)
                    self.all_sprites.add(boomout)
                    return True

    def diamondControl(self):
        if self.isDiamondsExist:
            for diamond in self.diamonds:
                if(self.king.rect.contains(diamond.rect)):
                    # if (self.king.rect.x + self.king.rect.width > diamond.rect.x and self.king.rect.x + self.king.rect.width < diamond.rect.x + diamond.rect.width) or (self.king.rect.x > diamond.rect.x and self.king.rect.x < diamond.rect.x + diamond.rect.width):
                    pg.sprite.spritecollide(
                        self.king, self.diamonds, True, pg.sprite.collide_rect)
                    self.success.play()
    
    def heartControl(self):
        if self.isHeartExist:
            for heart in self.hearts:
                if(self.king.rect.contains(heart.rect)):
                    # if (self.king.rect.x + self.king.rect.width > diamond.rect.x and self.king.rect.x + self.king.rect.width < diamond.rect.x + diamond.rect.width) or (self.king.rect.x > diamond.rect.x and self.king.rect.x < diamond.rect.x + diamond.rect.width):
                    pg.sprite.spritecollide(
                        self.king, self.hearts, True, pg.sprite.collide_rect)
                    self.king.health = 200
                    self.success.play()

    def boxHitControl(self):
        if self.isBoxesExist:
            hits = pg.sprite.spritecollide(self.king, self.boxes, False)
            if hits:
                for hit in hits:
                    if hit.health > 0:
                        hit.hitting = True
                        hit.health -= 35
                        self.log.play()
                    else:
                        posA = hit.pos
                        hit.kill()
                        self.createHeart(posA)
                        self.isHeartExist = True
                        self.woodcreak.play()

    def hit(self):
        if self.king.health > 0:
            self.king.health -= 10
            self.king.hitting = True

        else:
            self.king.dying = True
            self.king.pos.y -= 5
            self.playing = False

    def draw_shield_bar(self, surf, x, y):
        if not self.king.dying:
            if self.king.health < 0:
                self.king.health = 0
            BAR_LENGTH = 100
            BAR_HEIGHT = 10
            fill = (self.king.health / 200) * BAR_LENGTH
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
        if self.durum:
            self.screen.blit(self.background, (bgX, 0))
            self.screen.blit(self.background, (bgX2, 0))
        else:
            self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)
        self.draw_shield_bar(self.screen, self.king.rect.x-15,
                             self.king.rect.y-10)
        # pg.draw.rect(self.screen, (255, 0, 0), self.king.rect, 1)
        # *after* drawing everything, flip the display
        #pg.draw.rect(self.screen, (255,0,0), self.king.rect, 1)
        self.showLevel2()
        pg.display.flip()

    def createDiamond(self, pos):
        diamond = Diamond(pos)
        self.diamonds.add(diamond)
        self.all_sprites.add(diamond)
        self.isDiamondsExist = True

    def createHeart(self, pos):
        heart = Heart(pos)
        self.hearts.add(heart)
        self.all_sprites.add(heart)
        self.isHeartExist = True

    def show_win_screen(self):
        if not self.running:
            return
        run = True
        while run:
            now = pg.time.get_ticks()
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame2 = (self.current_frame2 + 1) % len(winScreen)
                if self.c <= 25:
                    self.c += 1
                    self.screen.blit(winScreen[self.current_frame2], (0, 0))
                    pg.display.flip()
                else:
                    self.screen.blit(winScreen[24], (0, 0))
                    pg.display.flip()
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    run = False
                if event.type == pg.KEYUP:
                    self.running = False
                    run = False

    def show_start_screen(self):
        # self.screen.blit(startScreen, (0, 0))
        self.showstartscreen = True
        while self.showstartscreen:
            now = pg.time.get_ticks()
            if now - self.last_update > 150:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(startScreen)
                self.screen.blit(startScreen[self.current_frame], (0, 0))
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYUP:
                    self.showstartscreen = False
                

    def show_go_screen(self):
        # game over/continue
        if not self.running:
            return
        if not self.issuccess:
            self.screen.blit(gameOver, (0, 0))
            pg.display.flip()
            self.wait_for_key()
        else:
            self.show_win_screen()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(30)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                if event.type == pg.KEYUP:
                    waiting = False

    # def draw_text(self, text, size, color, x, y):
    #     font = pg.font.Font(self.font_name, size)
    #     text_surface = font.render(text, True, color)
    #     text_rect = text_surface.get_rect()
    #     text_rect.midtop = (x, y)
    #     self.screen.blit(text_surface, text_rect)

    def wait_for_quit(self):
        waiting = True
        while waiting:
            self.clock.tick(30)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False
                    self.running = False
                    return True

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
        # self.rect = self.rect.inflate(-20, -4)
        # pg.transform.scale(self.rect, (39, 29), (self.rect.x + 10, self.rect.y + 9))
        # self.image.set_colorkey((0, 0, 0))
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.rect.width -= 15
        self.rect.height -= 10
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
        self.ctr3 = 0   

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
        if self.walking and not (self.dying or self.dead) and not self.attacking:
            if now - self.last_update > 60:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(kingRun)
                bottom = self.rect.bottom
                if self.vel.x > 0:
                    self.image = kingRun[self.current_frame]
                    self.rect = self.image.get_rect()
                    self.rect.bottom = bottom
                    self.rect.width -= 20
                    self.rect.height -= 12
                    self.rect.y += 12
                    # self.rect = self.rect.inflate(-20, -12)
                else:
                    self.image = kingRunL[self.current_frame]
                    self.rect = self.image.get_rect()
                    self.rect.bottom = bottom
                    self.rect.width -= 20
                    self.rect.height -= 12
                    self.rect.y += 12

                    # self.rect = self.rect.inflate(-15, -12)
        
        # Idling
        if not self.walking and not self.jumping and not (self.dying or self.dead) and not self.attacking:
            if now - self.last_update > 60:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(kingIdle)
                bottom = self.rect.bottom
                self.image = kingIdle[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.width -= 20
                self.rect.height -= 12
                self.rect.y += 12

                # self.rect = self.rect.inflate(-28, -12)
                self.rect.bottom = bottom
        
        if self.attacking and not (self.dying or self.dead):
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(kingAttack)
                bottom = self.rect.bottom
                if self.facing == True:
                    self.image = kingAttack[self.current_frame]
                elif self.facing == False:
                    self.image = kingAttackL[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.width -= 20
                self.rect.height -= 12
                self.rect.y += 12
                self.rect.bottom = bottom
                if self.ctr3 >= 3:
                    self.ctr3 = 0
                    self.attacking = False
                self.ctr3 += 1
        
        if self.hitting and not (self.dying or self.dead):
            if now - self.last_update > 60:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(kingHit)
                bottom = self.rect.bottom
                self.image = kingHit[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.width -= 20
                self.rect.height -= 12
                self.rect.y += 12
                # self.rect = self.rect.inflate(-20, -12)
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
                self.rect.width -= 20
                self.rect.height -= 12
                self.rect.y += 12
                self.rect.bottom = bottom
                if self.current_frame >= 3:
                    self.dying = False
                    game.createSpirit(self.pos)
                    self.kill()

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
        self.ctr2 = 0
        self.posV = posV

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
                self.facing = 'left'
            else:
                self.acc.x = -0.25
                self.facing = 'right'

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
        if self.walking and not (self.dying or self.dead) and not self.attacking:
            if now - self.last_update > 60:
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
            if now - self.last_update > 60:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(kingPigAttack)
                bottom = self.rect.bottom
                if self.facing == 'right':
                    self.image = kingPigAttack[self.current_frame]
                elif self.facing == 'left':
                    self.image = kingPigAttackLeft[self.current_frame]
                self.rect = self.image.get_rect()
                # if self.walkingRight:
                #     self.rect = self.rect.inflate(-20, -12)
                # else:
                # self.rect = self.rect.inflate(-20, -12)
                self.rect.bottom = bottom
                if self.ctr2 >= 5:
                    self.attacking = False
                    self.walking = True
                    self.ctr2 = 0
                self.ctr2 += 1

        # DEAD ANIMATION
        if self.dying:
            if now - self.last_update > 180:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(kingPigDead)
                bottom = self.rect.bottom
                self.image = kingPigDead[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
                if self.current_frame >= 3:
                    game.createSpirit(self.pos)
                    game.createGraveStone(self.pos)
                    self.kill()

        # if self.dead:
        #     if now - self.last_update > 120:
        #         self.last_update = now
        #         self.current_frame = 3
        #         bottom = self.rect.bottom
        #         self.image = kingPigDead[self.current_frame]
        #         self.rect = self.image.get_rect()
        #         self.rect.bottom = bottom

class Pig(pg.sprite.Sprite):
    def __init__(self, posV = vec(WIDTH - 280, HEIGHT - 200)):
        pg.sprite.Sprite.__init__(self)
        self.image = pigIdle[0]
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
        self.ctr2 = 0

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
                self.facing = 'left'
            else:
                self.acc.x = -0.25
                self.facing = 'right'
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
            if now - self.last_update > 60:
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
        
        if self.attacking:
            if now - self.last_update > 60:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(pigAttackLeft)
                bottom = self.rect.bottom
                if self.facing == 'right':
                    self.image = pigAttackRight[self.current_frame]
                elif self.facing == 'left':
                    self.image = pigAttackLeft[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
                if self.ctr2 >= 5:
                    self.attacking = False
                    self.walking = True
                    self.ctr2 = 0
                self.ctr2 += 1

class Box(pg.sprite.Sprite):
    def __init__(self, posV=vec(WIDTH - 280, HEIGHT - 200)):
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
            if now - self.last_update > 200:
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

class Diamond(pg.sprite.Sprite):
    def __init__(self, posV):
        pg.sprite.Sprite.__init__(self)
        self.image = boxIdle
        self.rect = self.image.get_rect()
        self.rect.center = (posV.x, posV.y - 25)
        self.image.set_colorkey((0, 0, 0))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.pos = vec(posV.x, posV.y - 25)
        self.idling = True
        self.current_frame = 0
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
                self.current_frame = (
                    self.current_frame + 1) % len(diamondIdle)
                bottom = self.rect.bottom
                self.image = diamondIdle[self.current_frame]
                self.rect = self.image.get_rect()
                # self.rect = self.rect.inflate(-28, -12)
                self.rect.bottom = bottom

class Heart(pg.sprite.Sprite):
    def __init__(self, posV):
        pg.sprite.Sprite.__init__(self)
        self.image = boxIdle
        self.rect = self.image.get_rect()
        self.rect.center = (posV.x, posV.y - 25)
        self.image.set_colorkey((0, 0, 0))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.pos = vec(posV.x, posV.y - 25)
        self.idling = True
        self.current_frame = 0
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
                self.current_frame = (
                    self.current_frame + 1) % len(heartIdle)
                bottom = self.rect.bottom
                self.image = heartIdle[self.current_frame]
                self.rect = self.image.get_rect()
                # self.rect = self.rect.inflate(-28, -12)
                self.rect.bottom = bottom

class Cannon(pg.sprite.Sprite):
    def __init__(self, posV = vec(WIDTH/2, HEIGHT/2)):
        pg.sprite.Sprite.__init__(self)
        self.image = cannonIdle
        self.rect = self.image.get_rect()
        self.rect.center = (posV.x, posV.y - 25)
        self.image.set_colorkey((0, 0, 0))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.pos = vec(posV.x, posV.y - 25)
        self.idling = True
        self.current_frame = 0
        self.last_update = 0
        self.idling = True
        self.shooting = False
        self.facing = True
        self.ctr = 0

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
        if self.idling:
            if now - self.last_update > 120:
                self.last_update = now
                bottom = self.rect.bottom
                self.image = cannonIdle
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

        if self.shooting and not self.idling:
            if now - self.last_update > 120:
                self.last_update = now
                if self.facing == True:
                    self.current_frame = (self.current_frame + 1) % len(cannonShoot)
                    bottom = self.rect.bottom
                    self.image = cannonShoot[self.current_frame]
                    self.rect = self.image.get_rect()
                    # self.rect.width -= 20
                    # self.rect.height -= 12
                    # self.rect.y += 12
                    # self.rect = self.rect.inflate(-5, -12)
                    self.rect.bottom = bottom
                else:
                    self.current_frame = (
                        self.current_frame + 1) % len(cannonShoot)
                    bottom = self.rect.bottom
                    self.image = cannonShoot[self.current_frame]
                    self.rect = self.image.get_rect()
                    # self.rect = self.rect.inflate(-40, -12)
                    # self.rect.width -= 20
                    # self.rect.height -= 12
                    # self.rect.y += 12
                    self.rect.bottom = bottom
                self.ctr += 1
                if self.ctr >= 4:
                    self.shooting = False
                    self.idling = True
                    self.ctr = 0

class CannonBall(pg.sprite.Sprite):
    def __init__(self, posV, facing):
        pg.sprite.Sprite.__init__(self)
        self.image = cannonBall
        self.rect = self.image.get_rect()
        self.rect.center = (posV.x, posV.y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.pos = vec(posV.x, posV.y)
        self.facing = facing

    def update(self):
        self.acc = vec(0, 0)
        # Gonna Change to when the ball went out of the screen it's gonna remove
        # if self.pos.x <= 0:
        #     self.pos.x = 0
        # if self.pos.x + self.rect.width >= WIDTH:
        #     self.pos.x = WIDTH - self.rect.width
        if self.facing == 'Left':
            self.acc.x = -0.8
        elif self.facing == 'Right':
            self.acc.x = 0.8

        # apply friction
        self.acc.x += self.vel.x * (-0.12)
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.8 * self.acc
        self.rect.midbottom = self.pos

class Spirit(pg.sprite.Sprite):
    def __init__(self, center):
        pg.sprite.Sprite.__init__(self)
        self.image = spirit[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.last_update = pg.time.get_ticks()
        self.current_frame = 0

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 120:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(spirit)
            if self.current_frame == len(spirit) - 1:
                self.kill()
            else:
                center = self.rect.center
                self.image = spirit[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class GraveStone(pg.sprite.Sprite):
    def __init__(self, posV):
        pg.sprite.Sprite.__init__(self)
        self.image = graveStone
        self.rect = self.image.get_rect()
        self.rect.center = (posV.x, posV.y - 20)
        self.pos = posV
        self.health = 100
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
    
    def update(self):
        self.acc = vec(0, 0.8)
        # apply friction
        self.acc.x += self.vel.x * (-0.12)
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

class Ork(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = orkIdle[0]
        self.rect = self.image.get_rect()
        self.rect.center = (150, 0)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.pos = vec(150, 0)
        self.posFirst = self.pos.x
        self.frame_counter = 0
        self.last_update = 0
        self.current_frame = 0
        self.dying = False
        self.dead = False
        self.deadCount = 0
        self.facing = 'right'
        self.attacking = False
        self.ctr2 = 0
        self.health = 100
        self.walking = False
        self.future = pg.time.get_ticks()
        self.ac = vec(0, 0.8)
        self.ctr3 = 0
        self.hitting = False
        self.drm = True

    def update(self):
        self.animate()
        now = pg.time.get_ticks()
        self.acc = self.ac  # 0.8=GRAVITY
        if now - self.future >= 1500:
            self.walking = True
            self.ac = vec(0.25, 0.8)
        if self.dead == True:
            self.vel.x = 0
            self.acc.x = 0
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
        # if self.vel.x > 0.1 or self.vel.x < -0.1:
        #     self.walking = True
        # else:
        #     self.walking = False
        if not self.walking and not self.attacking and not self.dying and not self.hitting:
            if now - self.last_update > 240:
                self.last_update = now
                self.current_frame = (
                    self.current_frame + 1) % len(orkIdle)
                bottom = self.rect.bottom
                self.image = orkIdle[self.current_frame]
                self.rect = self.image.get_rect()
                # if self.walkingRight:
                #     self.rect = self.rect.inflate(-20, -12)
                # else:
                #     self.rect = self.rect.inflate(-20, -12)
                self.rect.bottom = bottom
        if self.walking and not self.attacking and not self.dying and not self.hitting:
            if now - self.last_update > 200:
                game.orkWalk.play()
                self.last_update = now
                self.current_frame = (
                    self.current_frame + 1) % len(orkWalking)
                bottom = self.rect.bottom
                self.image = orkWalking[self.current_frame]
                self.rect = self.image.get_rect()
                # if self.walkingRight:
                #     self.rect = self.rect.inflate(-20, -12)
                # else:
                #     self.rect = self.rect.inflate(-20, -12)
                self.rect.bottom = bottom
        
        if self.attacking and not self.dying and not self.hitting:
            if now - self.last_update > 240:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(orkAttack)
                bottom = self.rect.bottom
                self.image = orkAttack[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
                if self.ctr2 >= 5:
                    self.attacking = False
                    self.walking = True
                    self.ctr2 = 0
                self.ctr2 += 1
        
        if self.hitting and not self.dying:
            if now - self.last_update > 120:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(orkHit)
                bottom = self.rect.bottom
                self.image = orkHit[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
                if self.ctr3 >= len(orkHit) - 1:
                    self.hitting = False
                    self.walking = True
                    self.ctr3 = 0
                self.ctr3 += 1

        if self.dying:
            if now - self.last_update > 360:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(orkDie)
                bottom = self.rect.bottom
                if self.current_frame >= len(orkDie) - 1:
                    self.image = orkDie[len(orkDie) - 1]
                    self.dying = False
                    while self.drm:
                        now3 = pg.time.get_ticks()
                        if now3 - self.last_update > 1000:
                            self.last_update = now3
                            self.kill()
                            game.monsterscream.stop()
                            game.createSpirit(center = self.rect.center)
                            loserin = LoserIn((game.king.rect.center[0] + 5, game.king.rect.center[1] - 60))
                            loserout = LoserOut((game.king.rect.center[0] + 5, game.king.rect.center[1] - 60))
                            game.all_sprites.add(loserin)
                            game.all_sprites.add(loserout)
                            self.drm = False
                            game.issuccess = True
                else:
                    self.image = orkDie[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

class Explosion(pg.sprite.Sprite):
    def __init__(self, center):
        pg.sprite.Sprite.__init__(self)
        self.image = explosion[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class BoomIn(pg.sprite.Sprite):
    def __init__(self, center):
        pg.sprite.Sprite.__init__(self)
        self.image = boomIn[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 150

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(boomIn):
                self.kill()
            else:
                center = self.rect.center
                self.image = boomIn[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class BoomOut(pg.sprite.Sprite):
    def __init__(self, center):
        pg.sprite.Sprite.__init__(self)
        self.image = boomOut[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 150

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(boomOut):
                self.kill()
            else:
                center = self.rect.center
                self.image = boomOut[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class WTFIn(pg.sprite.Sprite):
    def __init__(self, center):
        pg.sprite.Sprite.__init__(self)
        self.image = WtfIn[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 180

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(WtfIn):
                self.kill()
            else:
                center = self.rect.center
                self.image = WtfIn[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class WTFOut(pg.sprite.Sprite):
    def __init__(self, center):
        pg.sprite.Sprite.__init__(self)
        self.image = WtfOut[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 180

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(WtfOut):
                self.kill()
            else:
                center = self.rect.center
                self.image = WtfOut[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class LoserIn(pg.sprite.Sprite):
    def __init__(self, center):
        pg.sprite.Sprite.__init__(self)
        self.image = loserIn[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 360

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(loserIn):
                self.kill()
            else:
                center = self.rect.center
                self.image = loserIn[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class LoserOut(pg.sprite.Sprite):
    def __init__(self, center):
        pg.sprite.Sprite.__init__(self)
        self.image = loserOut[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 360

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(loserOut):
                self.kill()
            else:
                center = self.rect.center
                self.image = loserOut[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

game = Game()
game.show_start_screen()
while game.running:
    game.new()
    game.show_go_screen()
pg.quit()
