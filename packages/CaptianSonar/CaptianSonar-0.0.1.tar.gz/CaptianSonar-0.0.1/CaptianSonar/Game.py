import pyglet
from pyglet.window import key as k
import math
import os
from contextlib import suppress
import socket
from threading import Thread as T
import datetime
from CaptianSonar.build import BUILD

BUILD()

backgroundPlayer = pyglet.media.Player()
module_path, _ = os.path.split(__file__)
backgroundSound = pyglet.media.load(os.path.join(module_path, 'Game Data/Sound Effects/Background Sound.wav'))
backgroundPlayer.queue(backgroundSound)
backgroundPlayer.play()

def load_sound(old_path):
    path = os.path.join(module_path, old_path)
    audio = pyglet.media.load(path)
    return audio

def load_gif(old_path):
    path = os.path.join(module_path, old_path)
    img = pyglet.image.load_animation(path)
    return img

def load_image(old_path):
    path = os.path.join(module_path, old_path)
    img = pyglet.image.load(path)
    return img

FORMAT = 'utf-8'
PORT = 4445
IP = '73.103.247.204'
ADDR = (IP, PORT)


hackerPassword = 'Caption Sonar SUPER SECRET SPECIAL password'

cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cl.connect(ADDR)
cl.send(hackerPassword.encode(FORMAT))

window = pyglet.window.Window(fullscreen=True, caption='Captain Sonar')
#window = pyglet.window.Window(height=720, width=1280, caption='Captain Sonar')
window.set_icon(load_image("Game Data/sub.png"))
backgroundWelcomePic = load_image('Game Data/Welcome Screen.jpg')
backgroundMapPic = load_image('Game Data/Map selection screen.png')
backgroundGamePic = load_image('Game Data/Board Background.jpg')


def correctSprite(sprite):
    sprite.scale_x = window.width / 1280
    sprite.scale_y = window.height / 720
    return sprite

def center(pic):
    pic.anchor_x = pic.width//2
    pic.anchor_y = pic.height//2
    return pic

def pop_up(pic):
    def Function(dt):
        costume(PopUpBox, pic)

    def function(dt):
        PopUpBox.visible = False
        playsound(load_sound('Game Data/Sound Effects/button press.wav'))

    pyglet.clock.schedule_once(Function, 1 / 100)
    PopUpBox.visible = True
    pyglet.clock.schedule_once(function, 3)

def costume(sprite, pic):
    visible = sprite.visible
    opacity = sprite.opacity
    rotation = sprite.rotation
    scale = sprite.scale
    scale_x = sprite.scale_x
    scale_y = sprite.scale_y
    sprite.__init__(pic, x=sprite.x, y=sprite.y)
    sprite.scale_y = scale_y
    sprite.scale_x = scale_x
    sprite.visible = visible
    sprite.opacity = opacity
    sprite.rotation = rotation
    sprite.scale = scale


games = []
silenceTarget = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Captain Board/Target for Silence.png'))))
silenceTarget.visible = False
silenceTarget.max_move_so_far = 4
enemySubmarine = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Captain Board/enemy Submarine.png'))))
enemySubmarine.visible = False
enemyDamageMeter = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Damage meters/Opponent Damage meter 4.png')))
enemyDamageMeter.visible = False
enemyRedDot = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Navagator Stuff/red dot.png')), x=1089*(window.width/1280), y=524*(window.height/720)))
enemyRedDot.visible = False
drone = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Captain Board/drone.png'))))
drone.max_move_so_far = 12
drone.max_air_drone_move = 8
drone.visible = False
bomber = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Captain Board/Bomber.png'))))
bomber.visible = False
minePic = center(load_image('Game Data/Captain Board/mine.png'))
ListOfMines = []
torpedo = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Captain Board/torpedo.png'))))
torpedo.visible = False
explosion = correctSprite(pyglet.sprite.Sprite(load_gif('Game Data/Gifs/explosion.gif')))
explosion.visible = False
explosion.duration = 1.3333333
directionCommand = ''
chargeCommand = ''
enginnerCommand = ''
commands = ''
xlinePic = center(load_image('Game Data/Navagator Stuff/xline.png'))
ylinePic = center(load_image('Game Data/Navagator Stuff/yline.png'))
yourTrail= []
enemyTrail = []
my_name_Label = pyglet.text.Label(socket.gethostname().replace('-', ' '), anchor_x='center', anchor_y='center', x=634*(window.width/1280), y=340*(window.height/720), color=(255, 94, 115, 255), bold=True, font_size=40*(window.width/1280))
my_name_Label.opacity = 0
litte_my_name_Label = pyglet.text.Label(my_name_Label.text, anchor_x='center', anchor_y='center', x=50*(window.width/1280), y=200*(window.height/720), color=(0, 0, 0, 255), bold=True, font_size=8*(window.width/1280))
litte_my_name_Label.visible = False
litte_enemy_name_Label = pyglet.text.Label('', anchor_x='center', anchor_y='center', x=918*(window.width/1280), y=354*(window.height/720), color=(0, 0, 0, 255), bold=True, font_size=8*(window.width/1280))
litte_enemy_name_Label.visible = False
CommandsLabel = pyglet.text.Label(commands, font_size=20*(window.width/1280), x=830*(window.width/1280), y=628*(window.height/720), color=(255, 94, 115, 255), anchor_x='center', anchor_y='center', bold=True)
CommandsLabel.visible = False
yourTurnPic = load_image('Game Data/Buttons/Your turn.png')
notYourTurnPic = load_image('Game Data/Buttons/Not Your turn.png')
WhooseTurn = correctSprite(pyglet.sprite.Sprite(notYourTurnPic))
WhooseTurn.visible = False
westglow = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/west - glow.png')))
westglow.visible = False
northglow = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/north - glow.png')))
northglow.visible = False
southglow = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/south - glow.png')))
southglow.visible = False
eastglow = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/east - glow.png')))
eastglow.visible = False
background = correctSprite(pyglet.sprite.Sprite(backgroundWelcomePic))
SubmarinePic = center(load_image('Game Data/Captain Board/Captian Submarine.png'))
Submarine = correctSprite(pyglet.sprite.Sprite(SubmarinePic))
Submarine.visible = False
CommitButtonPic1 = load_image('Game Data/Buttons/Commit button.png')
CommitButtonPic2 = load_image('Game Data/Buttons/Commit button2.png')
CommitButtonMap = correctSprite(pyglet.sprite.Sprite(CommitButtonPic1, x=150 * (window.width / 1280), y=-180 * (window.height / 720)))
CommitButtonMap.visible = False
KnobPic1 = load_image('Game Data/Buttons/knob turned up.png')
KnobPic2 = load_image('Game Data/Buttons/knob turned sideways.png')
Knob = correctSprite(pyglet.sprite.Sprite(KnobPic2))
First_mate_switch_chargePic = load_image('Game Data/Buttons/utility charge.png')
First_mate_switch_usePic = load_image('Game Data/Buttons/utility use.png')
First_mate_switch = correctSprite(pyglet.sprite.Sprite(First_mate_switch_chargePic))
First_mate_switch.visible = False
RedButtonPic1 = load_image('Game Data/Buttons/Red Button.png')
RedButtonPic2 = load_image('Game Data/Buttons/Red Button2.png')
RedButton = correctSprite(pyglet.sprite.Sprite(RedButtonPic1))
loadingGifPic = load_gif('Game Data/Gifs/loading.gif')
GifBox = correctSprite(pyglet.sprite.Sprite(loadingGifPic, x=(636 * (window.width / 1280)) - 266 * ((window.width / 1280)), y=(379 * (window.height / 720)) - 150 * (window.height / 720)))
GifBox.visible = False
ShowMapPics = []
ShowMapIndex = 0
GameOver = pyglet.sprite.Sprite(RedButtonPic1)
GameOver.scale_x = window.width/600
GameOver.scale_y = window.height/360
GameOver.visible = False
for map in os.listdir('Game Data/game boards/Show Maps'):
    sprite = center(load_image(f'Game Data/game boards/Show Maps/{map}'))
    sprite.title = map.removesuffix('.jpg')
    ShowMapPics.append(sprite)
ShowMap = correctSprite(pyglet.sprite.Sprite(ShowMapPics[0], x=window.width/2, y=window.height/2))
ShowMap.visible = False
KnobUp = False
Scene = 'Welcome'
Range = 96*(window.width/1280)
ChoiceText = pyglet.text.Label(ShowMapPics[0].title, anchor_x='center', font_name='papyrus', font_size=40 * (window.width / 1280), anchor_y='center', x=window.width / 2, y=675 * (window.height / 720))# the top text for choosing maps and made games
ChoiceText.visible = False
Input_text = pyglet.text.Label('', font_name='arial', bold=True, font_size=20*(window.width/1280), anchor_y='center', anchor_x='center', color=(255, 94, 115, 255), x=450*(window.width/1280), y=69*(window.height/720))
Input_text.visible = False
PlayingBoard = correctSprite(pyglet.sprite.Sprite(RedButtonPic1))
PlayingBoard.visible = False
lives = 4
CommandBox = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/CommandBox.png')))
CommandBox.visible = False
SurfaceUnderWaterPic= load_image('Game Data/Buttons/Surface - down.png')
SurfaceAboveWaterPic = load_image('Game Data/Buttons/Surface - up.png')
SurfaceButton = correctSprite(pyglet.sprite.Sprite(SurfaceUnderWaterPic, y=20*(window.height/720)))
SurfaceButton.visible = False
DamageMeterPic0 = load_image("Game Data/Damage meters/0.png")
DamageMeterPic1 = load_image("Game Data/Damage meters/1.png")
DamageMeterPic2 = load_image("Game Data/Damage meters/2.png")
DamageMeterPic3 = load_image("Game Data/Damage meters/3.png")
DamageMeterPic4 = load_image("Game Data/Damage meters/4.png")
DamageMeter = correctSprite(pyglet.sprite.Sprite(DamageMeterPic4))
CommitButton = correctSprite(pyglet.sprite.Sprite(CommitButtonPic1))
ListOfEnemyMines = []
ShowMineWhenPlayed = True
PopUpBox = correctSprite(pyglet.sprite.Sprite(load_image(
    'Game Data/Pop ups/enemy mine deployed.png')))
enginneringSwitch = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/engineering toggle down.png')))
enginneringSwitch.on = False
enginneringSwitch.visible = False
PopUpBox.visible = False
CommitButton.visible = False
DamageMeter.visible = False
torpedo_overlay = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/Frist Mate Circle.png')), x=951*(window.width/1280), y=287*(window.height/720)))
torpedo_overlay.name = 't'
torpedo_overlay.max = 3
drone_overlay = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/Frist Mate Circle.png')), x=1076*(window.width/1280), y=287*(window.height/720)))
drone_overlay.name = 'd'
drone_overlay.max = 2
silence_overlay = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/Frist Mate Circle.png')), x=1208*(window.width/1280), y=287*(window.height/720)))
silence_overlay.name = 'si'
silence_overlay.max = 8
mine_overlay = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/Frist Mate Circle.png')), x=951*(window.width/1280), y=175*(window.height/720)))
mine_overlay.name = 'm'
mine_overlay.max = 2
sonar_overlay = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/Frist Mate Circle.png')), x=1076*(window.width/1280), y=175*(window.height/720)))
sonar_overlay.name = 'so'
sonar_overlay.max = 1
sheild_overlay = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/Frist Mate Circle.png')), x=1208*(window.width/1280), y=175*(window.height/720)))
sheild_overlay.name = 'sh'
sheild_overlay.max = 5
airStrike_overlay = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/Frist Mate Circle.png')), x=951*(window.width/1280), y=69*(window.height/720)))
airStrike_overlay.name = 'a'
airStrike_overlay.max = 5
recon_overlay = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/Frist Mate Circle.png')), x=1076*(window.width/1280), y=69*(window.height/720)))
recon_overlay.name = 'r'
recon_overlay.max = 4
deepDive_overlay = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/Frist Mate Circle.png')), x=1208*(window.width/1280), y=69*(window.height/720)))
deepDive_overlay.name = 'dd'
deepDive_overlay.max = 1
glowGif = load_gif('Game Data/Gifs/utility glow.gif')
Torpedo_glow = correctSprite(pyglet.sprite.Sprite(glowGif, y=19*(window.height/720), x=61*(window.width/1280)))
Mine_glow = correctSprite(pyglet.sprite.Sprite(glowGif, y=-90*(window.height/720), x=61*(window.width/1280)))
AirStrike_glow = correctSprite(pyglet.sprite.Sprite(glowGif, y=-199*(window.height/720), x=61*(window.width/1280)))
Drone_glow = correctSprite(pyglet.sprite.Sprite(glowGif, x=186*(window.width/1280), y=19*(window.height/720)))
Sonar_glow = correctSprite(pyglet.sprite.Sprite(glowGif, x=186*(window.width/1280), y=-90*(window.height/720)))
Recon_glow = correctSprite(pyglet.sprite.Sprite(glowGif, x=186*(window.width/1280), y=-199*(window.height/720)))
Silence_glow = correctSprite(pyglet.sprite.Sprite(glowGif, x=316*(window.width/1280), y=19*(window.height/720)))
Shield_glow = correctSprite(pyglet.sprite.Sprite(glowGif, x=316*(window.width/1280), y=-90*(window.height/720)))
DeepDive_glow = correctSprite(pyglet.sprite.Sprite(glowGif, x=316*(window.width/1280), y=-199*(window.height/720)))
ListOfGlows = [Torpedo_glow, Mine_glow, AirStrike_glow, Drone_glow, Sonar_glow, Recon_glow, Silence_glow, Shield_glow, DeepDive_glow]
for glow in ListOfGlows:
    glow.visible = False
tell_if_drone_found_me = True
tell_what_hit_me = True
full_charge_dot_silence = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/start with full charge (off).png'), y=0*(window.height/720)))
full_charge_dot_silence.kind = 'silence'
full_charge_dot_silence.click = (1244, 643)
full_charge_dot_shield = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/start with full charge (off).png'), y=-75*(window.height/720)))
full_charge_dot_shield.kind = 'shield'
full_charge_dot_shield.click = (1245, 569)
full_charge_dot_deep_dive = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/start with full charge (off).png'), y=-150*(window.height/720)))
full_charge_dot_deep_dive.kind = 'deep_dive'
full_charge_dot_deep_dive.click = (1245, 494)
full_charge_dot_drone = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/start with full charge (off).png'), y=-225*(window.height/720)))
full_charge_dot_drone.kind = 'drone'
full_charge_dot_drone.click = (1245, 417)
full_charge_dot_sonar = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/start with full charge (off).png'), y=-300*(window.height/720)))
full_charge_dot_sonar.kind = 'sonar'
full_charge_dot_sonar.click = (1244, 343)
full_charge_dot_recon = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/start with full charge (off).png'), y=-375*(window.height/720)))
full_charge_dot_recon.kind = 'recon'
full_charge_dot_recon.click = (1244, 268)
full_charge_dot_torpedo = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/start with full charge (off).png'), y=-450*(window.height/720)))
full_charge_dot_torpedo.kind = 'torpedo'
full_charge_dot_torpedo.click = (1246, 194)
full_charge_dot_mine = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/start with full charge (off).png'), y=-525*(window.height/720)))
full_charge_dot_mine.kind = 'mine'
full_charge_dot_mine.click = (1245, 117)
full_charge_dot_airstrike = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/start with full charge (off).png'), y=-600*(window.height/720)))
full_charge_dot_airstrike.kind = 'airstrike'
full_charge_dot_airstrike.click = (1245, 42)
ListOfFullChargeDots = [full_charge_dot_torpedo, full_charge_dot_mine, full_charge_dot_airstrike, full_charge_dot_drone, full_charge_dot_sonar, full_charge_dot_recon, full_charge_dot_silence, full_charge_dot_shield, full_charge_dot_deep_dive]

silence_Label = pyglet.text.Label(str(silence_overlay.max), x=1120*(window.width/1280), y=647*(window.height/720), anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), bold=True, font_size=25*(window.height/720), font_name="bauhaus 93")
silence_Label.minus = (1100, 646)
silence_Label.plus = (1144, 650)
sheild_Label = pyglet.text.Label(str(sheild_overlay.max), x=1120*(window.width/1280), y=572*(window.height/720), anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), bold=True, font_size=25*(window.height/720), font_name="bauhaus 93")
sheild_Label.minus = (1101, 569)
sheild_Label.plus = (1143, 570)
deepDive_Label = pyglet.text.Label(str(deepDive_overlay.max), x=1120*(window.width/1280), y=497*(window.height/720), anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), bold=True, font_size=25*(window.height/720), font_name="bauhaus 93")
deepDive_Label.minus = (1102, 497)
deepDive_Label.plus = (1143, 500)
drone_Label = pyglet.text.Label(str(drone_overlay.max), x=1120*(window.width/1280), y=418*(window.height/720), anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), bold=True, font_size=25*(window.height/720), font_name="bauhaus 93")
drone_Label.minus = (1100, 415)
drone_Label.plus = (1143, 417)
sonar_Label = pyglet.text.Label(str(sonar_overlay.max), x=1120*(window.width/1280), y=347*(window.height/720), anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), bold=True, font_size=25*(window.height/720), font_name="bauhaus 93")
sonar_Label.minus = (1100, 342)
sonar_Label.plus = (1144, 344)
recon_Label = pyglet.text.Label(str(recon_overlay.max), x=1120*(window.width/1280), y=272*(window.height/720), anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), bold=True, font_size=25*(window.height/720), font_name="bauhaus 93")
recon_Label.minus = (1100, 270)
recon_Label.plus = (1143, 271)
torpedo_Label = pyglet.text.Label(str(torpedo_overlay.max), x=1120*(window.width/1280), y=187*(window.height/720), anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), bold=True, font_size=25*(window.height/720), font_name="bauhaus 93")
torpedo_Label.minus = (1101, 186)
torpedo_Label.plus = (1144, 188)
mine_Label = pyglet.text.Label(str(mine_overlay.max), x=1120*(window.width/1280), y=122*(window.height/720), anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), bold=True, font_size=25*(window.height/720), font_name="bauhaus 93")
mine_Label.minus = (1103, 115)
mine_Label.plus = (1144, 119)
airStrike_Label = pyglet.text.Label(str(airStrike_overlay.max), x=1120*(window.width/1280), y=47*(window.height/720), anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), bold=True, font_size=25*(window.height/720), font_name="bauhaus 93")
airStrike_Label.minus = (1100, 42)
airStrike_Label.plus = (1142, 45)

ListOfMaxNumbers = [torpedo_Label, mine_Label, airStrike_Label, drone_Label, sonar_Label, recon_Label, silence_Label, sheild_Label, deepDive_Label]
for number in ListOfMaxNumbers:
    number.visible = False
for dot in ListOfFullChargeDots:
    dot.visible = False
    dot.on = False
GameNumber_Label = pyglet.text.Label(font_name='arial', font_size=25, color=(0, 0, 0, 255), anchor_y='center', x=383*(window.width/1280), y=576*(window.height/720))
GameNumber_Label.visible = False
winner_Label = pyglet.text.Label(font_name='arial', font_size=25, color=(0, 0, 0, 255), anchor_y='center', x=389*(window.width/1280), y=527*(window.height/720))
winner_Label.visible = False
creator_Label = pyglet.text.Label(font_name='arial', font_size=25, color=(0, 0, 0, 255), anchor_y='center', x=395*(window.width/1280), y=487*(window.height/720))
creator_Label.visible = False
joiner_Label = pyglet.text.Label(font_name='arial', font_size=25, color=(0, 0, 0, 255), anchor_y='center', x=395*(window.width/1280), y=443*(window.height/720))
joiner_Label.visible = False
engineering_Label = pyglet.text.Label(font_name='arial', font_size=25, color=(0, 0, 0, 255), anchor_y='center', x=400*(window.width/1280), y=397*(window.height/720))
engineering_Label.visible = False
date_Label = pyglet.text.Label(font_name='kristen itc', font_size=30, color=(0, 0, 0, 255), anchor_y='center', anchor_x='center', x=401*(window.width/1280), y=82*(window.height/720))
date_Label.visible = False
Stat_map = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/game boards/Show Maps/Alpha.jpg')), x=1017*(window.width/1280), y=132*(window.height/720)))
Stat_map.scale = 0.4
Stat_map.visible = False
Stat_map_Label = pyglet.text.Label(font_name='papyrus', font_size=20, color=(0, 0, 0, 255), anchor_y='center', anchor_x='center', x=1013*(window.width/1280), y=275*(window.height/720), bold=True, italic=True)
Stat_map_Label.visible = False
ListOfStatsTextLabels = [GameNumber_Label, winner_Label, creator_Label, joiner_Label, engineering_Label, date_Label, Stat_map, Stat_map_Label]
StatIndex = 0
enginner_overlay_number_0 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=49*(window.width/1280), y=161*(window.height/720)))
enginner_overlay_number_0.kind = 'w'
enginner_overlay_number_0.pipe = 'y'
enginner_overlay_number_0.id = '0'
enginner_overlay_number_0.direction = 'w'
enginner_overlay_number_1 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=190*(window.width/1280), y=161*(window.height/720)))
enginner_overlay_number_1.kind = 'u'
enginner_overlay_number_1.pipe = 'y'
enginner_overlay_number_1.id = '1'
enginner_overlay_number_1.direction = 'w'
enginner_overlay_number_2 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=270*(window.width/1280), y=162*(window.height/720)))
enginner_overlay_number_2.kind = 'u'
enginner_overlay_number_2.pipe = 'o'
enginner_overlay_number_2.id = '2'
enginner_overlay_number_2.direction = 'n'
enginner_overlay_number_3 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=491*(window.width/1280), y=159*(window.height/720)))
enginner_overlay_number_3.kind = 's'
enginner_overlay_number_3.pipe = 'g'
enginner_overlay_number_3.id = '3'
enginner_overlay_number_3.direction = 's'
enginner_overlay_number_4 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=702*(window.width/1280), y=162*(window.height/720)))
enginner_overlay_number_4.kind = 's'
enginner_overlay_number_4.pipe = 'o'
enginner_overlay_number_4.id = '4'
enginner_overlay_number_4.direction = 'e'
enginner_overlay_number_5 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=191*(window.width/1280), y=100*(window.height/720)))
enginner_overlay_number_5.kind = 's'
enginner_overlay_number_5.pipe = 'y'
enginner_overlay_number_5.id = '5'
enginner_overlay_number_5.direction = 'w'
enginner_overlay_number_6 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=269*(window.width/1280), y=102*(window.height/720)))
enginner_overlay_number_6.kind = 'w'
enginner_overlay_number_6.pipe = 'o'
enginner_overlay_number_6.id = '6'
enginner_overlay_number_6.direction = 'n'
enginner_overlay_number_7 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=411*(window.width/1280), y=103*(window.height/720)))
enginner_overlay_number_7.kind = 'u'
enginner_overlay_number_7.pipe = 'o'
enginner_overlay_number_7.id = '7'
enginner_overlay_number_7.direction = 'n'
enginner_overlay_number_8 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=489*(window.width/1280), y=101*(window.height/720)))
enginner_overlay_number_8.kind = 'u'
enginner_overlay_number_8.pipe = 'g'
enginner_overlay_number_8.id = '8'
enginner_overlay_number_8.direction = 's'
enginner_overlay_number_9 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=632*(window.width/1280), y=101*(window.height/720)))
enginner_overlay_number_9.kind = 'w'
enginner_overlay_number_9.pipe = 'g'
enginner_overlay_number_9.id = '9'
enginner_overlay_number_9.direction = 's'
enginner_overlay_number_10 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=702*(window.width/1280), y=103*(window.height/720)))
enginner_overlay_number_10.kind = 'u'
enginner_overlay_number_10.pipe = 'g'
enginner_overlay_number_10.id = '10'
enginner_overlay_number_10.direction = 'e'
enginner_overlay_number_11 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=845*(window.width/1280), y=101*(window.height/720)))
enginner_overlay_number_11.kind = 'w'
enginner_overlay_number_11.pipe = 'y'
enginner_overlay_number_11.id = '11'
enginner_overlay_number_11.direction = 'e'
enginner_overlay_number_12 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=51*(window.width/1280), y=40*(window.height/720)))
enginner_overlay_number_12.kind = 's'
enginner_overlay_number_12.pipe = 'r'
enginner_overlay_number_12.id = '12'
enginner_overlay_number_12.direction = 'w'
enginner_overlay_number_13 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=123*(window.width/1280), y=40*(window.height/720)))
enginner_overlay_number_13.kind = 'r'
enginner_overlay_number_13.pipe = 'r'
enginner_overlay_number_13.id = '13'
enginner_overlay_number_13.direction = 'w'
enginner_overlay_number_14 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=193*(window.width/1280), y=40*(window.height/720)))
enginner_overlay_number_14.kind = 'r'
enginner_overlay_number_14.pipe = 'r'
enginner_overlay_number_14.id = '14'
enginner_overlay_number_14.direction = 'w'
enginner_overlay_number_15 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=270*(window.width/1280), y=40*(window.height/720)))
enginner_overlay_number_15.kind = 's'
enginner_overlay_number_15.pipe = 'r'
enginner_overlay_number_15.id = '15'
enginner_overlay_number_15.direction = 'n'
enginner_overlay_number_16 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=343*(window.width/1280), y=39*(window.height/720)))
enginner_overlay_number_16.kind = 'w'
enginner_overlay_number_16.pipe = 'r'
enginner_overlay_number_16.id = '16'
enginner_overlay_number_16.direction = 'n'
enginner_overlay_number_17 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=412*(window.width/1280), y=41*(window.height/720)))
enginner_overlay_number_17.kind = 'r'
enginner_overlay_number_17.pipe = 'r'
enginner_overlay_number_17.id = '17'
enginner_overlay_number_17.direction = 'n'
enginner_overlay_number_18 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=491*(window.width/1280), y=40*(window.height/720)))
enginner_overlay_number_18.kind = 'w'
enginner_overlay_number_18.pipe = 'r'
enginner_overlay_number_18.id = '18'
enginner_overlay_number_18.direction = 's'
enginner_overlay_number_19 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=562*(window.width/1280), y=40*(window.height/720)))
enginner_overlay_number_19.kind = 'r'
enginner_overlay_number_19.pipe = 'r'
enginner_overlay_number_19.id = '19'
enginner_overlay_number_19.direction = 's'
enginner_overlay_number_20 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=629*(window.width/1280), y=42*(window.height/720)))
enginner_overlay_number_20.kind = 'u'
enginner_overlay_number_20.pipe = 'r'
enginner_overlay_number_20.id = '20'
enginner_overlay_number_20.direction = 's'
enginner_overlay_number_21 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=702*(window.width/1280), y=40*(window.height/720)))
enginner_overlay_number_21.kind = 'r'
enginner_overlay_number_21.pipe = 'r'
enginner_overlay_number_21.id = '21'
enginner_overlay_number_21.direction = 'e'
enginner_overlay_number_22 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=772*(window.width/1280), y=41*(window.height/720)))
enginner_overlay_number_22.kind = 's'
enginner_overlay_number_22.pipe = 'r'
enginner_overlay_number_22.id = '22'
enginner_overlay_number_22.direction = 'e'
enginner_overlay_number_23 = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/enginener circle.png')), x=841*(window.width/1280), y=41*(window.height/720)))
enginner_overlay_number_23.kind = 'r'
enginner_overlay_number_23.pipe = 'r'
enginner_overlay_number_23.id = '23'
enginner_overlay_number_23.direction = 'e'
usingEnginnering = True
ListOfEnginnerOverlays = [enginner_overlay_number_0, enginner_overlay_number_1, enginner_overlay_number_2, enginner_overlay_number_3, enginner_overlay_number_4, enginner_overlay_number_5, enginner_overlay_number_6, enginner_overlay_number_7, enginner_overlay_number_8, enginner_overlay_number_9, enginner_overlay_number_10, enginner_overlay_number_11, enginner_overlay_number_12, enginner_overlay_number_13, enginner_overlay_number_14, enginner_overlay_number_15, enginner_overlay_number_16, enginner_overlay_number_17, enginner_overlay_number_18, enginner_overlay_number_19, enginner_overlay_number_20, enginner_overlay_number_21, enginner_overlay_number_22, enginner_overlay_number_23]
ListOfUsedEnginneringStuff = []
for thing in ListOfEnginnerOverlays:
    thing.visible = False
enginnerglow = correctSprite(pyglet.sprite.Sprite(load_gif('Game Data/Gifs/engineer glow.gif')))
enginnerglow.visible = False
Pic1_piece_0_glow = load_image('Game Data/power ups/1 piece 0 glow.png')
Pic1_piece_1_glow = load_image('Game Data/power ups/1 piece 1 glow.png')
Pic2_piece_0_glow = load_image('Game Data/power ups/2 piece 0 glow.png')
Pic2_piece_1_glow = load_image('Game Data/power ups/2 piece 1 glow.png')
Pic2_piece_2_glow = load_image('Game Data/power ups/2 piece 2 glow.png')
Pic3_piece_0_glow = load_image('Game Data/power ups/3 piece 0 glow.png')
Pic3_piece_1_glow = load_image('Game Data/power ups/3 piece 1 glow.png')
Pic3_piece_2_glow = load_image('Game Data/power ups/3 piece 2 glow.png')
Pic3_piece_3_glow = load_image('Game Data/power ups/3 piece 3 glow.png')
Pic4_piece_0_glow = load_image('Game Data/power ups/4 piece 0 glow.png')
Pic4_piece_1_glow = load_image('Game Data/power ups/4 piece 1 glow.png')
Pic4_piece_2_glow = load_image('Game Data/power ups/4 piece 2 glow.png')
Pic4_piece_3_glow = load_image('Game Data/power ups/4 piece 3 glow.png')
Pic4_piece_4_glow = load_image('Game Data/power ups/4 piece 4 glow.png')
Pic5_piece_0_glow = load_image('Game Data/power ups/5 piece 0 glow.png')
Pic5_piece_1_glow = load_image('Game Data/power ups/5 piece 1 glow.png')
Pic5_piece_2_glow = load_image('Game Data/power ups/5 piece 2 glow.png')
Pic5_piece_3_glow = load_image('Game Data/power ups/5 piece 3 glow.png')
Pic5_piece_4_glow = load_image('Game Data/power ups/5 piece 4 glow.png')
Pic5_piece_5_glow = load_image('Game Data/power ups/5 piece 5 glow.png')
Pic6_piece_0_glow = load_image('Game Data/power ups/6 piece 0 glow.png')
Pic6_piece_1_glow = load_image('Game Data/power ups/6 piece 1 glow.png')
Pic6_piece_2_glow = load_image('Game Data/power ups/6 piece 2 glow.png')
Pic6_piece_3_glow = load_image('Game Data/power ups/6 piece 3 glow.png')
Pic6_piece_4_glow = load_image('Game Data/power ups/6 piece 4 glow.png')
Pic6_piece_5_glow = load_image('Game Data/power ups/6 piece 5 glow.png')
Pic6_piece_6_glow = load_image('Game Data/power ups/6 piece 6 glow.png')
Pic7_piece_0_glow = load_image('Game Data/power ups/7 piece 0 glow.png')
Pic7_piece_1_glow = load_image('Game Data/power ups/7 piece 1 glow.png')
Pic7_piece_2_glow = load_image('Game Data/power ups/7 piece 2 glow.png')
Pic7_piece_3_glow = load_image('Game Data/power ups/7 piece 3 glow.png')
Pic7_piece_4_glow = load_image('Game Data/power ups/7 piece 4 glow.png')
Pic7_piece_5_glow = load_image('Game Data/power ups/7 piece 5 glow.png')
Pic7_piece_6_glow = load_image('Game Data/power ups/7 piece 6 glow.png')
Pic7_piece_7_glow = load_image('Game Data/power ups/7 piece 7 glow.png')
Pic8_piece_0_glow = load_image('Game Data/power ups/8 piece 0 glow.png')
Pic8_piece_1_glow = load_image('Game Data/power ups/8 piece 1 glow.png')
Pic8_piece_2_glow = load_image('Game Data/power ups/8 piece 2 glow.png')
Pic8_piece_3_glow = load_image('Game Data/power ups/8 piece 3 glow.png')
Pic8_piece_4_glow = load_image('Game Data/power ups/8 piece 4 glow.png')
Pic8_piece_5_glow = load_image('Game Data/power ups/8 piece 5 glow.png')
Pic8_piece_6_glow = load_image('Game Data/power ups/8 piece 6 glow.png')
Pic8_piece_7_glow = load_image('Game Data/power ups/8 piece 7 glow.png')
Pic8_piece_8_glow = load_image('Game Data/power ups/8 piece 8 glow.png')
stats_button = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/Stats button (up).png')))
login_switch = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/Periscope button (up).png')))
login_switch.on = False
perscope = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Misc/Periscope name entry.png')))
perscope.up = 720*(window.height/720)
perscope.y = perscope.up
perscope.speed = 10*(window.height/720)
Torpedo_Charge = correctSprite(pyglet.sprite.Sprite(Pic3_piece_0_glow))
Mine_Charge = correctSprite(pyglet.sprite.Sprite(Pic2_piece_0_glow, y=-109*(window.height/720)))
AirStrike_Charge = correctSprite(pyglet.sprite.Sprite(Pic5_piece_0_glow, y=-218*(window.height/720)))
Drone_Charge = correctSprite(pyglet.sprite.Sprite(Pic2_piece_0_glow, x=125*(window.width/1280)))
Sonar_Charge = correctSprite(pyglet.sprite.Sprite(Pic1_piece_0_glow, x=125*(window.width/1280), y=-109*(window.height/720)))
Recon_Charge = correctSprite(pyglet.sprite.Sprite(Pic4_piece_0_glow, x=125*(window.width/1280), y=-218*(window.height/720)))
Silence_Charge = correctSprite(pyglet.sprite.Sprite(Pic8_piece_0_glow, x=255*(window.width/1280)))
Shield_Charge = correctSprite(pyglet.sprite.Sprite(Pic5_piece_0_glow, x=255*(window.width/1280), y=-109*(window.height/720)))
DeepDive_Charge = correctSprite(pyglet.sprite.Sprite(Pic2_piece_0_glow, x=255*(window.width/1280), y=-218*(window.height/720)))
ListOfPowerUpsOverlay = [torpedo_overlay, mine_overlay, airStrike_overlay, drone_overlay, sonar_overlay, recon_overlay, silence_overlay, sheild_overlay, deepDive_overlay]
back_to_title_screen_button = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/return to title screen button (up).png')))
back_to_title_screen_button.visible = False
for thing in ListOfPowerUpsOverlay:
    thing.visible = False
    thing.charge = 0
ListOfPowerUps = [Torpedo_Charge, Mine_Charge, AirStrike_Charge, Drone_Charge, Sonar_Charge, Recon_Charge, Silence_Charge, Shield_Charge, DeepDive_Charge]
for sprite in ListOfPowerUps:
    sprite.visible = False
tell_what_hit_me_dot = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/yellow light on (weapons).png')))
tell_what_hit_me_dot.visible = False
tell_what_hit_me_dot.on = True
tell_if_drone_found_me_dot = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/yellow light on (location).png')))
tell_if_drone_found_me_dot.on = True
tell_if_drone_found_me_dot.visible = False
ShowMineWhenPlayed_dot = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/yellow light on (mines).png')))
ShowMineWhenPlayed_dot.on = True
ShowMineWhenPlayed_dot.visible = False
SonarIsSetOnSheilds = True
Sonar_switch = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/sonar switch (to shield).png')))
Sonar_switch.visible = False
Sonar_switch.on = 'Shields'
back_to_title_screen_button_for_joining_and_making_a_game = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/return to title screen (up) from map selection screen.png')))
back_to_title_screen_button_for_joining_and_making_a_game.visible = False
back_to_title_screen_button_for_you_win_you_lose = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/back to title screen button ( up) from win-lose screen.png')))
back_to_title_screen_button_for_you_win_you_lose.visible = False
Top_5_Label_1 = pyglet.text.Label(font_name='arial', font_size=18, bold=True, color=(0, 0, 0, 255), x=833*(window.width/1280), y=559*(window.height/720), anchor_y='center')
Top_5_Label_2 = pyglet.text.Label(font_name='arial', font_size=18, bold=True, color=(0, 0, 0, 255), x=833*(window.width/1280), y=529*(window.height/720), anchor_y='center')
Top_5_Label_3 = pyglet.text.Label(font_name='arial', font_size=18, bold=True, color=(0, 0, 0, 255), x=833*(window.width/1280), y=499*(window.height/720), anchor_y='center')
Top_5_Label_4 = pyglet.text.Label(font_name='arial', font_size=18, bold=True, color=(0, 0, 0, 255), x=833*(window.width/1280), y=469*(window.height/720), anchor_y='center')
Top_5_Label_5 = pyglet.text.Label(font_name='arial', font_size=18, bold=True, color=(0, 0, 0, 255), x=833*(window.width/1280), y=439*(window.height/720), anchor_y='center')
Top_5_Label_6 = pyglet.text.Label(font_name='arial', font_size=18, bold=True, color=(0, 0, 0, 255), x=833*(window.width/1280), y=409*(window.height/720), anchor_y='center')
Top_5_Label_7 = pyglet.text.Label(font_name='arial', font_size=18, bold=True, color=(0, 0, 0, 255), x=833*(window.width/1280), y=379*(window.height/720), anchor_y='center')
ListOfTop5Labels = [Top_5_Label_1, Top_5_Label_2, Top_5_Label_3, Top_5_Label_4, Top_5_Label_5, Top_5_Label_6, Top_5_Label_7]
Settings_panel = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Settings Tab/Settings panel.png'), x=-870*(window.width/1280)))
Settings_panel.over = False
Settings_panel.visible = False
Settings_engineer_option = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Settings Tab/engineering option (off).png'), x=-870*(window.width/1280)))
Settings_sonar_option = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Settings Tab/sonar option (shield).png'), x=-870*(window.width/1280)))
Settings_location_option = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Settings Tab/location detection indicator light (on).png'), x=-870*(window.width/1280)))
Settings_mine_option = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Settings Tab/mine detection indicator light (on).png'), x=-870*(window.width/1280)))
Settings_weapons_option = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Settings Tab/weapons detection indicator light (on).png'), x=-870*(window.width/1280)))
Setting_options = [Settings_engineer_option, Settings_sonar_option, Settings_location_option, Settings_mine_option, Settings_weapons_option]
for option in Setting_options:
    option.visible = False
for label in ListOfTop5Labels:
    label.visible = False
drone_switch = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/drone toggle (sea).png')))
drone_switch.on = 'water'
drone_switch.visible = False
mine_switch = correctSprite(pyglet.sprite.Sprite(load_image('Game Data/Buttons/Mine Switch (mine).png')))
mine_switch.on = 'plant'
mine_switch.visible = False

@window.event
def on_draw():
    window.clear()
    ShowMap.draw()
    background.draw()
    RedButton.draw()
    Knob.draw()
    ChoiceText.draw()
    stats_button.draw()
    for Label in ListOfStatsTextLabels:
        Label.draw()
    login_switch.draw()
    CommitButtonMap.draw()
    PlayingBoard.draw()
    for dot in ListOfFullChargeDots:
        dot.draw()
    tell_what_hit_me_dot.draw()
    tell_if_drone_found_me_dot.draw()
    ShowMineWhenPlayed_dot.draw()
    DamageMeter.draw()
    enemyDamageMeter.draw()
    for sprite in ListOfPowerUps:
        sprite.draw()
    mine_switch.draw()
    enginneringSwitch.draw()
    Sonar_switch.draw()
    SurfaceButton.draw()
    CommitButton.draw()
    back_to_title_screen_button.draw()
    westglow.draw()
    eastglow.draw()
    northglow.draw()
    southglow.draw()
    WhooseTurn.draw()
    CommandBox.draw()
    CommandsLabel.draw()
    for overlay in ListOfPowerUpsOverlay:
        overlay.draw()
    First_mate_switch.draw()
    for overlay in ListOfEnginnerOverlays:
        overlay.draw()
    for thing in ListOfUsedEnginneringStuff:
        thing.draw()
    for glow in ListOfGlows:
        glow.draw()
    for Label in ListOfTop5Labels:
        Label.draw()
    enginnerglow.draw()
    for line in yourTrail:
        line.draw()
    for mine in ListOfMines:
        mine.draw()
    for basesSprite in basesSprites:
        basesSprite.draw()
    Submarine.draw()
    back_to_title_screen_button_for_joining_and_making_a_game.draw()
    torpedo.draw()
    bomber.draw()
    drone.draw()
    silenceTarget.draw()
    explosion.draw()
    litte_my_name_Label.draw()
    litte_enemy_name_Label.draw()
    for line in enemyTrail:
        line.draw()
    enemyRedDot.draw()
    for mine in ListOfEnemyMines:
        mine.draw()
    for number in ListOfMaxNumbers:
        number.draw()
    drone_switch.draw()
    PopUpBox.draw()
    enemySubmarine.draw()
    GifBox.draw()
    Input_text.draw()
    perscope.draw()
    my_name_Label.draw()
    Settings_panel.draw()
    for option in Setting_options:
        option.draw()
    GameOver.draw()
    back_to_title_screen_button_for_you_win_you_lose.draw()

rooms = []

def make_join_board(dt):
    global Scene
    try:
        ChoiceText.text = rooms[0][1]
        for map in ShowMapPics:
            if map.title == rooms[0][0]:
                costume(ShowMap, map)
        for index in range(len(rooms)):
            if rooms[index][1] == ChoiceText.text:
                if rooms[index][8] == 'Shields':
                    costume(Sonar_switch, load_image('Game Data/Buttons/sonar switch (to shield).png'))
                    costume(Setting_options[Setting_options.index(Settings_sonar_option)],
                            load_image('Game Data/Settings Tab/sonar option (shield).png'))

                else:
                    costume(Sonar_switch, load_image('Game Data/Buttons/sonar switch (to utility).png'))
                    costume(Setting_options[Setting_options.index(Settings_sonar_option)],
                            load_image('Game Data/Settings Tab/sonar option (utility).png'))
                if rooms[index][5]:
                    costume(tell_what_hit_me_dot, load_image('Game Data/Buttons/yellow light on (weapons).png'))
                    costume(Setting_options[Setting_options.index(Settings_weapons_option)],
                            load_image('Game Data/Settings Tab/weapons detection indicator light (on).png'))

                else:
                    costume(tell_what_hit_me_dot, load_image('Game Data/Buttons/yellow light off (weapons).png'))
                    costume(Setting_options[Setting_options.index(Settings_weapons_option)],
                            load_image('Game Data/Settings Tab/weapons detection indicator light (off).png'))
                if rooms[index][6]:
                    costume(ShowMineWhenPlayed_dot, load_image('Game Data/Buttons/yellow light on (mines).png'))
                    costume(Setting_options[Setting_options.index(Settings_mine_option)],
                            load_image('Game Data/Settings Tab/mine detection indicator light (on).png'))

                else:
                    costume(ShowMineWhenPlayed_dot, load_image('Game Data/Buttons/yellow light off (mines).png'))
                    costume(Setting_options[Setting_options.index(Settings_mine_option)],
                            load_image('Game Data/Settings Tab/mine detection indicator light (off).png'))
                if rooms[index][7]:
                    costume(tell_if_drone_found_me_dot, load_image('Game Data/Buttons/yellow light on (location).png'))
                    costume(Setting_options[Setting_options.index(Settings_location_option)],
                            load_image('Game Data/Settings Tab/location detection indicator light (on).png'))

                else:
                    costume(tell_if_drone_found_me_dot, load_image('Game Data/Buttons/yellow light off (location).png'))
                    costume(Setting_options[Setting_options.index(Settings_location_option)],
                            load_image('Game Data/Settings Tab/location detection indicator light (off).png'))

                for number in range(len(rooms[index][2])):  # what starts fully charged
                    ListOfMaxNumbers[number].text = str(rooms[index][3][number])
                for number in range(len(rooms[index][2])):  # what starts fully charged
                    if rooms[index][2][number]:
                        costume(ListOfFullChargeDots[number], load_image('Game Data/Buttons/start with full charge (on).png'))
                    else:
                        costume(ListOfFullChargeDots[number], load_image('Game Data/Buttons/start with full charge (off).png'))
    except IndexError:
        costume(RedButton, RedButtonPic1)
        return
    back_to_title_screen_button_for_joining_and_making_a_game.visible = True
    perscope.visible = False
    stats_button.visible = False
    login_switch.visible = False
    tell_if_drone_found_me_dot.visible = True
    tell_what_hit_me_dot.visible = True
    ShowMineWhenPlayed_dot.visible = True
    enginneringSwitch.visible = True
    Sonar_switch.visible = True
    for index in range(len(rooms)):
        if rooms[index][1] == ChoiceText.text:
            if rooms[index][4]:
                costume(enginneringSwitch, load_image('Game Data/Buttons/engineering toggle up.png'))
                costume(Setting_options[Setting_options.index(Settings_engineer_option)], load_image('Game Data/Settings Tab/engineering option (on).png'))
            else:
                costume(enginneringSwitch, load_image('Game Data/Buttons/engineering toggle down.png'))
                costume(Setting_options[Setting_options.index(Settings_engineer_option)], load_image('Game Data/Settings Tab/engineering option (off).png'))
    for text in ListOfMaxNumbers:
        text.visible = True
    for dot in ListOfFullChargeDots:
        dot.visible = True
    ShowMap.visible = True
    costume(background, backgroundMapPic)
    RedButton.visible = False
    Knob.visible = False
    Scene = 'join'
    ChoiceText.visible = True
    CommitButtonMap.visible = True

def make_map_board(dt):
    global Scene
    back_to_title_screen_button_for_joining_and_making_a_game.visible = True
    perscope.visible = False
    stats_button.visible = False
    login_switch.visible = False
    tell_what_hit_me_dot.visible = True
    tell_if_drone_found_me_dot.visible = True
    ShowMineWhenPlayed_dot.visible = True
    for number in ListOfMaxNumbers:
        number.visible = True
    ShowMap.visible = True
    enginneringSwitch.visible = True
    Sonar_switch.visible = True
    costume(background, backgroundMapPic)
    RedButton.visible = False
    Knob.visible = False
    Scene = 'maps'
    ChoiceText.visible = True
    CommitButtonMap.visible = True
    for dot in ListOfFullChargeDots:
        dot.visible = True

def playsound(sound):
    player = pyglet.media.Player()
    player.queue(sound)
    player.play()

ShifedPressed = False

@window.event
def on_key_release(s, m):
    global  ShifedPressed, leftpressed, rightpressed, uppressed, downpressed
    if s in [k.LSHIFT, k.RSHIFT]:
        ShifedPressed = False
    if s == k.LEFT:
        leftpressed = False
    if s == k.RIGHT:
        rightpressed = False
    if s == k.DOWN:
        downpressed = False
    if s == k.UP:
        uppressed = False

def make_welcome_screen(dt):
    global Scene
    for Label in ListOfTop5Labels:
        Label.visible = False
    ChoiceText.visible = False
    for Label in ListOfStatsTextLabels:
        Label.visible = False
    Scene = 'Welcome'
    login_switch.visible = True
    perscope.visible = True
    costume(back_to_title_screen_button_for_joining_and_making_a_game, load_image('Game Data/Buttons/return to title screen (up) from map selection screen.png'))
    costume(stats_button, load_image('Game Data/Buttons/Stats button (up).png'))
    costume(back_to_title_screen_button, load_image('Game Data/Buttons/return to title screen button (up).png'))
    costume(RedButton, RedButtonPic1)
    costume(background, load_image('Game Data/Welcome Screen.jpg'))
    CommitButtonMap.visible = False
    for dot in ListOfFullChargeDots:
        dot.visible = False
    for number in ListOfMaxNumbers:
        number.visible = False
    tell_what_hit_me_dot.visible = False
    tell_if_drone_found_me_dot.visible = False
    ShowMineWhenPlayed_dot.visible = False
    enginneringSwitch.visible = False
    Sonar_switch.visible = False
    back_to_title_screen_button_for_joining_and_making_a_game.visible = False
    stats_button.visible = True
    Knob.visible = True
    RedButton.visible = True
    back_to_title_screen_button.visible = False


def make_stats_board(dt):
    global Scene
    Scene = 'stats'
    for Label in ListOfTop5Labels:
        Label.visible = True
    winners = []
    joiners = []
    creators = []
    for game in games:
        winners.append(game['winner'].capitalize().replace(' ', ''))
    for game in games:
        joiners.append(game['joiner'].capitalize().replace(' ', ''))
    for game in games:
        creators.append(game['creator'].capitalize().replace(' ', ''))
    names = []
    NumberOfWinsList = []
    NumberOfGamesPlayed = []
    joinerCreatorList = []
    for name in winners:
        if name not in names:
            names.append(name)
    for name in names:
        NumberOfWinsList.append(winners.count(name))

    for name in names:
        for joiner in joiners:
            if joiner == name:
                joinerCreatorList.append(joiner)
        for creator in creators:
            if creator == name:
                joinerCreatorList.append(creator)
    for name in names:
        NumberOfGamesPlayed.append(joinerCreatorList.count(name))

    for i in range(len(NumberOfWinsList)):
        number = max(NumberOfWinsList)
        name = names[NumberOfWinsList.index(number)]
        GamesPlayed = NumberOfGamesPlayed[NumberOfWinsList.index(number)]
        names.remove(name)
        NumberOfWinsList.remove(number)
        NumberOfGamesPlayed.remove(GamesPlayed)
        try:
            eval(f"ListOfTop5Labels[ListOfTop5Labels.index(Top_5_Label_{i+1})]").text = f"{name}: {number}    {GamesPlayed}   {int((number/GamesPlayed)*100)}%"
        except NameError:
            pass



    with suppress(IndexError):
        game = games[StatIndex]
        ListOfStatsTextLabels[ListOfStatsTextLabels.index(winner_Label)].text = game['winner']
        ListOfStatsTextLabels[ListOfStatsTextLabels.index(joiner_Label)].text = game['joiner']
        ListOfStatsTextLabels[ListOfStatsTextLabels.index(creator_Label)].text = game['creator']
        ListOfStatsTextLabels[ListOfStatsTextLabels.index(GameNumber_Label)].text = str(games.index(game) + 1)
        ListOfStatsTextLabels[ListOfStatsTextLabels.index(date_Label)].text = game['date']
        ListOfStatsTextLabels[ListOfStatsTextLabels.index(engineering_Label)].text = 'Off'
        costume(ListOfStatsTextLabels[ListOfStatsTextLabels.index(Stat_map)], center(load_image(f"Game Data/game boards/Show Maps/{game['board']}.jpg")))
        ListOfStatsTextLabels[ListOfStatsTextLabels.index(Stat_map_Label)].text = game['board']
        if game['engineering']:
            ListOfStatsTextLabels[ListOfStatsTextLabels.index(engineering_Label)].text = 'On'
    for Label in ListOfStatsTextLabels:
        Label.visible = True
    perscope.visible = False
    stats_button.visible = False
    login_switch.visible = False
    back_to_title_screen_button.visible = True
    costume(background, load_image('Game Data/stat screen.jpg'))
    RedButton.visible = False
    Knob.visible = False

def make_game_board(dt):
    for option in Setting_options:
        option.visible = True
    mine_switch.visible = True
    drone_switch.visible = True
    global Scene, usingEnginnering, tell_if_drone_found_me, tell_what_hit_me, ShowMineWhenPlayed, SonarIsSetOnSheilds
    Settings_panel.visible = True
    back_to_title_screen_button_for_joining_and_making_a_game.visible = False
    litte_my_name_Label.visible = True
    litte_my_name_Label.text = my_name_Label.text
    tell_what_hit_me_dot.visible = False
    tell_if_drone_found_me_dot.visible = False
    ShowMineWhenPlayed_dot.visible = False
    enginneringSwitch.visible = False
    Sonar_switch.visible = False

    for text in ListOfMaxNumbers:
        text.visible = False
    for dot in ListOfFullChargeDots:
        dot.visible = False
    for index in range(len(rooms)):
        if rooms[index][1] == ChoiceText.text:
            if not rooms[index][5]:
                tell_what_hit_me = False
            if not rooms[index][6]:
                ShowMineWhenPlayed = False
            if not rooms[index][7]:
                tell_if_drone_found_me = False
            for number in range(len(rooms[index][2])):
                overlay = ListOfPowerUpsOverlay[number]
                overlay.max = rooms[index][3][number]
    for index in range(len(rooms)):
        if rooms[index][1] == ChoiceText.text:
            usingEnginnering = rooms[index][4]
            if rooms[index][8] == 'Shields':
                SonarIsSetOnSheilds = True
            else:
                SonarIsSetOnSheilds = False
    Scene = 'playing'
    enemyDamageMeter.visible = True
    CommandBox.visible = True
    for index in range(len(rooms)):
        if rooms[index][1] == ChoiceText.text:
            for number in range(len(rooms[index][2])):#what starts fully charged
                overlay = ListOfPowerUpsOverlay[number]
                powerUp = ListOfPowerUps[number]
                if rooms[index][2][number]:
                    overlay.charge = overlay.max
                costume(powerUp, eval(f"Pic{overlay.max}_piece_{overlay.charge}_glow"))
    CommitButtonMap.visible = False
    ChoiceText.visible = False
    costume(background, backgroundGamePic)
    SurfaceButton.visible = True
    DamageMeter.visible = True
    PlayingBoard.visible = True
    CommitButton.visible = True
    First_mate_switch.visible = True
    for sprite in ListOfPowerUps:
        sprite.visible = True

def make_loading_board(dt):
    global Scene, usingEnginnering, tell_if_drone_found_me, tell_what_hit_me, ShowMineWhenPlayed, SonarIsSetOnSheilds
    back_to_title_screen_button_for_joining_and_making_a_game.visible = False
    mine_switch.visible = True
    drone_switch.visible = True
    Settings_panel.visible = True
    litte_my_name_Label.visible = True
    litte_my_name_Label.text = my_name_Label.text
    ShowMineWhenPlayed = ShowMineWhenPlayed_dot.on
    tell_what_hit_me = tell_what_hit_me_dot.on
    tell_if_drone_found_me = tell_if_drone_found_me_dot.on
    usingEnginnering = enginneringSwitch.on
    Sonar_switch.visible = False
    for option in Setting_options:
        option.visible = True
    if Sonar_switch.on == 'Shields':
        SonarIsSetOnSheilds = True
    else:
        SonarIsSetOnSheilds = False
    enginneringSwitch.visible = False
    ShowMineWhenPlayed_dot.visible = False
    tell_what_hit_me_dot.visible = False
    tell_if_drone_found_me_dot.visible = False
    for dot in ListOfFullChargeDots:
        dot.visible = False
    for number in ListOfMaxNumbers:
        number.visible = False
        overlay = ListOfPowerUpsOverlay[ListOfMaxNumbers.index(number)]
        overlay.max = int(number.text)
    Scene = 'loading'
    enemyDamageMeter.visible = True
    CommandBox.visible = True
    CommitButtonMap.visible = False
    ChoiceText.visible = False
    for dot in ListOfFullChargeDots:
        if dot.on:
            overlay = ListOfPowerUpsOverlay[ListOfFullChargeDots.index(dot)]
            powerUp = ListOfPowerUps[ListOfFullChargeDots.index(dot)]
            overlay.charge = overlay.max
        else:
            overlay = ListOfPowerUpsOverlay[ListOfFullChargeDots.index(dot)]
            powerUp = ListOfPowerUps[ListOfFullChargeDots.index(dot)]
        costume(powerUp, eval(f"Pic{overlay.max}_piece_{overlay.charge}_glow"))
    costume(background, backgroundGamePic)
    First_mate_switch.visible = True
    SurfaceButton.visible = True
    DamageMeter.visible = True
    PlayingBoard.visible = True
    GifBox.visible = True
    CommitButton.visible = True
    for sprite in ListOfPowerUps:
        sprite.visible = True

position = [-1, -1]
islands = []
bases = []
basesSprites = []
coordsITraveledSo = []

def cancel_explosion(dt):
    explosion.visible = False
    costume(explosion, load_gif('Game Data/Gifs/explosion.gif'))

@window.event
def on_key_press(s, m):
    global ShowMapIndex, ShifedPressed, Input_text, position, Scene, my_turn, navagatorStartLineHere, uppressed, downpressed, leftpressed, rightpressed, torpedoMoveSoFar, torpedoPosition, utility_being_used, placingMine, bomberMoveSoFar, drone_move_so_far, silenceTargetMoveSoFar, chargeCommand, commands, directionCommand, StatIndex, sheilds
    if s in [k.RSHIFT, k.LSHIFT]:
        ShifedPressed = True
    if s == k.ESCAPE:
        window.close()
        cl.close()
        quit()
    if Scene == 'stats':
        if s == k.RIGHT:
            StatIndex += 1
            if StatIndex > (len(games) - 1):
                StatIndex = 0
            with suppress(IndexError):
                game = games[StatIndex]
                ListOfStatsTextLabels[ListOfStatsTextLabels.index(winner_Label)].text = game['winner']
                ListOfStatsTextLabels[ListOfStatsTextLabels.index(joiner_Label)].text = game['joiner']
                ListOfStatsTextLabels[ListOfStatsTextLabels.index(creator_Label)].text = game['creator']
                ListOfStatsTextLabels[ListOfStatsTextLabels.index(GameNumber_Label)].text = str(games.index(game) + 1)
                ListOfStatsTextLabels[ListOfStatsTextLabels.index(date_Label)].text = game['date']
                ListOfStatsTextLabels[ListOfStatsTextLabels.index(engineering_Label)].text = 'Off'
                costume(ListOfStatsTextLabels[ListOfStatsTextLabels.index(Stat_map)], center(load_image(f"Game Data/game boards/Show Maps/{game['board']}.jpg")))
                ListOfStatsTextLabels[ListOfStatsTextLabels.index(Stat_map_Label)].text = game['board']
                if game['engineering']:
                    ListOfStatsTextLabels[ListOfStatsTextLabels.index(engineering_Label)].text = 'On'
            playsound(load_sound('Game Data/Sound Effects/knob turning sound.wav'))
        if s == k.LEFT:
            StatIndex -= 1
            if StatIndex < 0:
                StatIndex = len(games) - 1
            with suppress(IndexError):
                game = games[StatIndex]
                ListOfStatsTextLabels[ListOfStatsTextLabels.index(winner_Label)].text = game['winner']
                ListOfStatsTextLabels[ListOfStatsTextLabels.index(joiner_Label)].text = game['joiner']
                ListOfStatsTextLabels[ListOfStatsTextLabels.index(creator_Label)].text = game['creator']
                ListOfStatsTextLabels[ListOfStatsTextLabels.index(GameNumber_Label)].text = str(games.index(game) + 1)
                ListOfStatsTextLabels[ListOfStatsTextLabels.index(date_Label)].text = game['date']
                ListOfStatsTextLabels[ListOfStatsTextLabels.index(engineering_Label)].text = 'Off'
                costume(ListOfStatsTextLabels[ListOfStatsTextLabels.index(Stat_map)], center(load_image(f"Game Data/game boards/Show Maps/{game['board']}.jpg")))
                ListOfStatsTextLabels[ListOfStatsTextLabels.index(Stat_map_Label)].text = game['board']
                if game['engineering']:
                    ListOfStatsTextLabels[ListOfStatsTextLabels.index(engineering_Label)].text = 'On'
            playsound(load_sound('Game Data/Sound Effects/knob turning sound.wav'))
    if Scene == "Welcome":
        if s == k.DELETE:
            my_name_Label.text = ''
            playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
        if s == k.BACKSPACE:
            with suppress(IndexError):
                my_name_Label.text = my_name_Label.text.removesuffix(my_name_Label.text[len(my_name_Label.text) - 1])
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
        if len(my_name_Label.text) < 14:
            if s == k.Q and not ShifedPressed:
                my_name_Label.text += 'q'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.W and not ShifedPressed:
                my_name_Label.text += 'w'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.E and not ShifedPressed:
                my_name_Label.text += 'e'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.R and not ShifedPressed:
                my_name_Label.text += 'r'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.T and not ShifedPressed:
                my_name_Label.text += 't'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.Y and not ShifedPressed:
                my_name_Label.text += 'y'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.U and not ShifedPressed:
                my_name_Label.text += 'u'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.I and not ShifedPressed:
                my_name_Label.text += 'i'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.O and not ShifedPressed:
                my_name_Label.text += 'o'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.P and not ShifedPressed:
                my_name_Label.text += 'p'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.A and not ShifedPressed:
                my_name_Label.text += 'a'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.S and not ShifedPressed:
                my_name_Label.text += 's'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.D and not ShifedPressed:
                my_name_Label.text += 'd'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.F and not ShifedPressed:
                my_name_Label.text += 'f'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.G and not ShifedPressed:
                my_name_Label.text += 'g'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.H and not ShifedPressed:
                my_name_Label.text += 'h'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.J and not ShifedPressed:
                my_name_Label.text += 'j'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.K and not ShifedPressed:
                my_name_Label.text += 'k'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.L and not ShifedPressed:
                my_name_Label.text += 'l'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.Z and not ShifedPressed:
                my_name_Label.text += 'z'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.X and not ShifedPressed:
                my_name_Label.text += 'x'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.C and not ShifedPressed:
                my_name_Label.text += 'c'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.V and not ShifedPressed:
                my_name_Label.text += 'v'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.B and not ShifedPressed:
                my_name_Label.text += 'b'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.N and not ShifedPressed:
                my_name_Label.text += 'n'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.M and not ShifedPressed:
                my_name_Label.text += 'm'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            if s == k.Q and ShifedPressed:
                my_name_Label.text += 'Q'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.W and ShifedPressed:
                my_name_Label.text += 'W'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.E and ShifedPressed:
                my_name_Label.text += 'E'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.R and ShifedPressed:
                my_name_Label.text += 'R'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.T and ShifedPressed:
                my_name_Label.text += 'T'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.Y and ShifedPressed:
                my_name_Label.text += 'Y'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.U and ShifedPressed:
                my_name_Label.text += 'U'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.I and ShifedPressed:
                my_name_Label.text += 'I'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.O and ShifedPressed:
                my_name_Label.text += 'O'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.P and ShifedPressed:
                my_name_Label.text += 'P'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.A and ShifedPressed:
                my_name_Label.text += 'A'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.S and ShifedPressed:
                my_name_Label.text += 'S'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.D and ShifedPressed:
                my_name_Label.text += 'D'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.F and ShifedPressed:
                my_name_Label.text += 'F'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.G and ShifedPressed:
                my_name_Label.text += 'G'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.H and ShifedPressed:
                my_name_Label.text += 'H'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.J and ShifedPressed:
                my_name_Label.text += 'J'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.K and ShifedPressed:
                my_name_Label.text += 'K'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.L and ShifedPressed:
                my_name_Label.text += 'L'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.Z and ShifedPressed:
                my_name_Label.text += 'Z'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.X and ShifedPressed:
                my_name_Label.text += 'X'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.C and ShifedPressed:
                my_name_Label.text += 'C'

                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.V and ShifedPressed:
                my_name_Label.text += 'V'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.B and ShifedPressed:
                my_name_Label.text += 'B'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.N and ShifedPressed:
                my_name_Label.text += 'N'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.M and ShifedPressed:
                my_name_Label.text += 'M'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.APOSTROPHE:
                my_name_Label.text += "'"
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s == k.SPACE:
                my_name_Label.text += ' '
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s in [k.NUM_1, k._1, k.EXCLAMATION] and ShifedPressed:
                my_name_Label.text += '!'
                playsound(load_sound('Game Data/Sound Effects/Sonar ping 4.wav'))
            if s in [k.NUM_1, k._1] and not ShifedPressed:
                my_name_Label.text += '1'
            if s in [k.NUM_2, k._2] and not ShifedPressed:
                my_name_Label.text += '2'
            if s in [k.NUM_3, k._3] and not ShifedPressed:
                my_name_Label.text += '3'
            if s in [k.NUM_4, k._4] and not ShifedPressed:
                my_name_Label.text += '4'
            if s in [k.NUM_5, k._5] and not ShifedPressed:
                my_name_Label.text += '5'
            if s in [k.NUM_6, k._6] and not ShifedPressed:
                my_name_Label.text += '6'
            if s in [k.NUM_7, k._7] and not ShifedPressed:
                my_name_Label.text += '7'
            if s in [k.NUM_8, k._8] and not ShifedPressed:
                my_name_Label.text += '8'
            if s in [k.NUM_9, k._9] and not ShifedPressed:
                my_name_Label.text += '9'
            if s in [k.NUM_0, k._0] and not ShifedPressed:
                my_name_Label.text += '0'
    if Scene == "maps":
        if s == k.LEFT:
            ShowMapIndex -= 1
            if ShowMapIndex < 0:
                ShowMapIndex = len(ShowMapPics)-1
            costume(ShowMap, ShowMapPics[ShowMapIndex])
            ChoiceText.text = ShowMapPics[ShowMapIndex].title
            playsound(load_sound('Game Data/Sound Effects/knob turning sound.wav'))
        if s == k.RIGHT:
            ShowMapIndex += 1
            if ShowMapIndex > (len(ShowMapPics)-1):
                ShowMapIndex = 0
            costume(ShowMap, ShowMapPics[ShowMapIndex])
            ChoiceText.text = ShowMapPics[ShowMapIndex].title
            playsound(load_sound('Game Data/Sound Effects/knob turning sound.wav'))
    if Scene == 'join':
        if s == k.LEFT:
            ShowMapIndex -= 1
            if ShowMapIndex < 0:
                ShowMapIndex = len(rooms)-1
            for map in ShowMapPics:
                if map.title == rooms[ShowMapIndex][0]:
                    costume(ShowMap, map)
            ChoiceText.text = rooms[ShowMapIndex][1]
            for index in range(len(rooms)):
                if rooms[index][1] == ChoiceText.text:
                    if rooms[index][8] == 'Shields':
                        costume(Sonar_switch, load_image('Game Data/Buttons/sonar switch (to shield).png'))
                        costume(Setting_options[Setting_options.index(Settings_sonar_option)],
                                load_image('Game Data/Settings Tab/sonar option (shield).png'))

                    else:
                        costume(Sonar_switch, load_image('Game Data/Buttons/sonar switch (to utility).png'))
                        costume(Setting_options[Setting_options.index(Settings_sonar_option)],
                                load_image('Game Data/Settings Tab/sonar option (utility).png'))
                    if rooms[index][5]:
                        costume(tell_what_hit_me_dot,
                                load_image('Game Data/Buttons/yellow light on (weapons).png'))
                        costume(Setting_options[Setting_options.index(Settings_weapons_option)],
                                load_image('Game Data/Settings Tab/weapons detection indicator light (on).png'))

                    else:
                        costume(tell_what_hit_me_dot,
                                load_image('Game Data/Buttons/yellow light off (weapons).png'))
                        costume(Setting_options[Setting_options.index(Settings_weapons_option)],
                                load_image('Game Data/Settings Tab/weapons detection indicator light (off).png'))
                    if rooms[index][6]:
                        costume(ShowMineWhenPlayed_dot,
                                load_image('Game Data/Buttons/yellow light on (mines).png'))
                        costume(Setting_options[Setting_options.index(Settings_mine_option)],
                                load_image('Game Data/Settings Tab/mine detection indicator light (on).png'))

                    else:
                        costume(ShowMineWhenPlayed_dot,
                                load_image('Game Data/Buttons/yellow light off (mines).png'))
                        costume(Setting_options[Setting_options.index(Settings_mine_option)],
                                load_image('Game Data/Settings Tab/mine detection indicator light (off).png'))
                    if rooms[index][7]:
                        costume(tell_if_drone_found_me_dot,
                                load_image('Game Data/Buttons/yellow light on (location).png'))
                        costume(Setting_options[Setting_options.index(Settings_location_option)],
                                load_image('Game Data/Settings Tab/location detection indicator light (on).png'))

                    else:
                        costume(tell_if_drone_found_me_dot,
                                load_image('Game Data/Buttons/yellow light off (location).png'))
                        costume(Setting_options[Setting_options.index(Settings_location_option)],
                                load_image(
                                    'Game Data/Settings Tab/location detection indicator light (off).png'))
                    if rooms[index][4]:
                        costume(enginneringSwitch, load_image('Game Data/Buttons/engineering toggle up.png'))
                        costume(Setting_options[Setting_options.index(Settings_engineer_option)],
                                load_image('Game Data/Settings Tab/engineering option (on).png'))
                    else:
                        costume(enginneringSwitch, load_image('Game Data/Buttons/engineering toggle down.png'))
                        costume(Setting_options[Setting_options.index(Settings_engineer_option)],
                                load_image('Game Data/Settings Tab/engineering option (off).png'))
                    for number in range(len(rooms[index][2])):  # what starts fully charged
                        ListOfMaxNumbers[number].text = str(rooms[index][3][number])
                    for number in range(len(rooms[index][2])):  # what starts fully charged
                        if rooms[index][2][number]:
                            costume(ListOfFullChargeDots[number], load_image('Game Data/Buttons/start with full charge (on).png'))
                        else:
                            costume(ListOfFullChargeDots[number], load_image('Game Data/Buttons/start with full charge (off).png'))
            playsound(load_sound('Game Data/Sound Effects/knob turning sound.wav'))
        if s == k.RIGHT:
            ShowMapIndex += 1
            if ShowMapIndex > (len(rooms)-1):
                ShowMapIndex = 0
            for map in ShowMapPics:
                if map.title == rooms[ShowMapIndex][0]:
                    costume(ShowMap, map)
            ChoiceText.text = rooms[ShowMapIndex][1]
            for index in range(len(rooms)):
                if rooms[index][1] == ChoiceText.text:
                    if rooms[index][8] == 'Shields':
                        costume(Sonar_switch, load_image('Game Data/Buttons/sonar switch (to shield).png'))
                        costume(Setting_options[Setting_options.index(Settings_sonar_option)],
                                load_image('Game Data/Settings Tab/sonar option (shield).png'))

                    else:
                        costume(Sonar_switch, load_image('Game Data/Buttons/sonar switch (to utility).png'))
                        costume(Setting_options[Setting_options.index(Settings_sonar_option)],
                                load_image('Game Data/Settings Tab/sonar option (utility).png'))
                    if rooms[index][5]:
                        costume(tell_what_hit_me_dot,
                                load_image('Game Data/Buttons/yellow light on (weapons).png'))
                        costume(Setting_options[Setting_options.index(Settings_weapons_option)],
                                load_image('Game Data/Settings Tab/weapons detection indicator light (on).png'))

                    else:
                        costume(tell_what_hit_me_dot,
                                load_image('Game Data/Buttons/yellow light off (weapons).png'))
                        costume(Setting_options[Setting_options.index(Settings_weapons_option)],
                                load_image('Game Data/Settings Tab/weapons detection indicator light (off).png'))
                    if rooms[index][6]:
                        costume(ShowMineWhenPlayed_dot,
                                load_image('Game Data/Buttons/yellow light on (mines).png'))
                        costume(Setting_options[Setting_options.index(Settings_mine_option)],
                                load_image('Game Data/Settings Tab/mine detection indicator light (on).png'))

                    else:
                        costume(ShowMineWhenPlayed_dot,
                                load_image('Game Data/Buttons/yellow light off (mines).png'))
                        costume(Setting_options[Setting_options.index(Settings_mine_option)],
                                load_image('Game Data/Settings Tab/mine detection indicator light (off).png'))
                    if rooms[index][7]:
                        costume(tell_if_drone_found_me_dot,
                                load_image('Game Data/Buttons/yellow light on (location).png'))
                        costume(Setting_options[Setting_options.index(Settings_location_option)],
                                load_image('Game Data/Settings Tab/location detection indicator light (on).png'))

                    else:
                        costume(tell_if_drone_found_me_dot,
                                load_image('Game Data/Buttons/yellow light off (location).png'))
                        costume(Setting_options[Setting_options.index(Settings_location_option)],
                                load_image(
                                    'Game Data/Settings Tab/location detection indicator light (off).png'))
                    if rooms[index][4]:
                        costume(enginneringSwitch, load_image('Game Data/Buttons/engineering toggle up.png'))
                        costume(Setting_options[Setting_options.index(Settings_engineer_option)],
                                load_image('Game Data/Settings Tab/engineering option (on).png'))
                    else:
                        costume(enginneringSwitch, load_image('Game Data/Buttons/engineering toggle down.png'))
                        costume(Setting_options[Setting_options.index(Settings_engineer_option)],
                                load_image('Game Data/Settings Tab/engineering option (off).png'))
                    for number in range(len(rooms[index][2])):  # what starts fully charged
                        ListOfMaxNumbers[number].text = str(rooms[index][3][number])
                    for number in range(len(rooms[index][2])):  # what starts fully charged
                        if rooms[index][2][number]:
                            costume(ListOfFullChargeDots[number], load_image('Game Data/Buttons/start with full charge (on).png'))
                        else:
                            costume(ListOfFullChargeDots[number], load_image('Game Data/Buttons/start with full charge (off).png'))
            playsound(load_sound('Game Data/Sound Effects/knob turning sound.wav'))
    if Scene == 'Select':
        if s == k.BACKSPACE:
            with suppress(IndexError):
                Input_text.text = Input_text.text.removesuffix(Input_text.text[len(Input_text.text)-1])
        letterli = list('ABCDEFGHIJKLMNO')
        numli = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        if (s == k.RETURN) or (s == k.ENTER) or (s == k.NUM_ENTER):
            with suppress(IndexError):
                if Input_text.text[0] not in letterli:
                    playsound(load_sound('Game Data/Sound Effects/You Cant use that position.wav'))
                else:
                    position = [numli[letterli.index(Input_text.text[0])]]
                    if len(Input_text.text) == 3:
                        try:
                            if int(Input_text.text[1]+Input_text.text[2]) not in numli:
                                playsound(load_sound('Game Data/Sound Effects/You Cant use that position.wav'))
                            else:
                                position.append(int(Input_text.text[1] + Input_text.text[2]))
                                for island in islands:
                                    if island == position:
                                        playsound(load_sound('Game Data/Sound Effects/You Cant use that position.wav'))
                                        return
                                playsound(load_sound('Game Data/Sound Effects/big splash.wav'))
                                Scene = 'playing'
                                GifBox.visible = False
                                Input_text.visible = False
                                Submarine.x = (84*(window.width/1280) + (47*(window.width/1280) * position[0])) - 47*(window.width/1280)
                                Submarine.y = (651*(window.height/720) - (30*(window.height/720) * position[1])) + 30*(window.height/720)
                                Submarine.visible = True
                                if my_turn:
                                    my_turn = True
                                    costume(WhooseTurn, yourTurnPic)
                                else:
                                    costume(WhooseTurn, notYourTurnPic)
                                WhooseTurn.visible = True
                        except ValueError:
                            playsound(load_sound('Game Data/Sound Effects/You Cant use that position.wav'))
                    elif len(Input_text.text) == 2:
                        try:
                            if int(Input_text.text[1]) not in numli:
                                playsound(load_sound('Game Data/Sound Effects/You Cant use that position.wav'))
                            else:
                                position.append(int(Input_text.text[1]))
                                for island in islands:
                                    if island == position:
                                        playsound(load_sound('Game Data/Sound Effects/You Cant use that position.wav'))
                                        return
                                playsound(load_sound('Game Data/Sound Effects/big splash.wav'))
                                Scene = 'playing'
                                GifBox.visible = False
                                Input_text.visible = False
                                Submarine.x = (84 * (window.width / 1280) + (47 * (window.width / 1280) * position[0])) - 47 * (window.width / 1280)
                                Submarine.y = (651 * (window.height / 720) - (30 * (window.height / 720) * position[1])) + 30 * (window.height / 720)
                                Submarine.visible = True
                                if my_turn:
                                    my_turn = True
                                    costume(WhooseTurn, yourTurnPic)
                                else:
                                    costume(WhooseTurn, notYourTurnPic)
                                WhooseTurn.visible = True
                        except ValueError:
                            playsound(load_sound('Game Data/Sound Effects/You Cant use that position.wav'))
                    else:
                        playsound(load_sound('Game Data/Sound Effects/You Cant use that position.wav'))
            print(f"POSITION {position}")

        if len(Input_text.text) < 3:
            if s == k.A:
                Input_text.text += 'A'
            if s == k.B:
                Input_text.text += 'B'
            if s == k.C:
                Input_text.text += 'C'
            if s == k.D:
                Input_text.text += 'D'
            if s == k.E:
                Input_text.text += 'E'
            if s == k.F:
                Input_text.text += 'F'
            if s == k.G:
                Input_text.text += 'G'
            if s == k.H:
                Input_text.text += 'H'
            if s == k.I:
                Input_text.text += 'I'
            if s == k.J:
                Input_text.text += 'J'
            if s == k.K:
                Input_text.text += 'K'
            if s == k.L:
                Input_text.text += 'L'
            if s == k.M:
                Input_text.text += 'M'
            if s == k.N:
                Input_text.text += 'N'
            if s == k.O:
                Input_text.text += 'O'
            if (s == k._1) or (s == k.NUM_1):
                Input_text.text += '1'
            if (s == k._2) or (s == k.NUM_2):
                Input_text.text += '2'
            if (s == k._3) or (s == k.NUM_3):
                Input_text.text += '3'
            if (s == k._4) or (s == k.NUM_4):
                Input_text.text += '4'
            if (s == k._5) or (s == k.NUM_5):
                Input_text.text += '5'
            if (s == k._6) or (s == k.NUM_6):
                Input_text.text += '6'
            if (s == k._7) or (s == k.NUM_7):
                Input_text.text += '7'
            if (s == k._8) or (s == k.NUM_8):
                Input_text.text += '8'
            if (s == k._9) or (s == k.NUM_9):
                Input_text.text += '9'
            if (s == k._0) or (s == k.NUM_0):
                Input_text.text += '0'
    if Scene == 'playing':
        if s in [k.NUM_1, k._1] and placingMine:
            mine = ListOfMines[len(ListOfMines)-1]
            futureMinePosition = [position[0]-1, position[1] + 1]
            for island in islands:
                if island == futureMinePosition:
                    playsound(load_sound('Game Data/Sound Effects/You can\'t place your mine here.wav'))
                    return
            utility_being_used = False
            mine.y -= 30*(window.height/720)
            mine.x -= 47*(window.width/1280)
            mine.Position = futureMinePosition.copy()
            placingMine = False
            utility_being_used = False
            if ShowMineWhenPlayed:
                cl.send(str(['TO MY PARTNER', 'Played Mine']).encode(FORMAT))

        if s in [k.NUM_3, k._3] and placingMine:
            mine = ListOfMines[len(ListOfMines) - 1]
            futureMinePosition = [position[0] + 1, position[1] + 1]
            for island in islands:
                if island == futureMinePosition:
                    playsound(load_sound('Game Data/Sound Effects/You can\'t place your mine here.wav'))
                    return
            utility_being_used = False
            mine.y -= 30 * (window.height / 720)
            mine.x += 47 * (window.width / 1280)
            mine.Position = futureMinePosition.copy()
            placingMine = False
            utility_being_used = False
            if ShowMineWhenPlayed:
                cl.send(str(['TO MY PARTNER', 'Played Mine']).encode(FORMAT))

        if s in [k.NUM_9, k._9] and placingMine:
            mine = ListOfMines[len(ListOfMines) - 1]
            futureMinePosition = [position[0] + 1, position[1] - 1]
            for island in islands:
                if island == futureMinePosition:
                    playsound(load_sound('Game Data/Sound Effects/You can\'t place your mine here.wav'))
                    return
            utility_being_used = False
            mine.y += 30 * (window.height / 720)
            mine.x += 47 * (window.width / 1280)
            mine.Position = futureMinePosition.copy()
            placingMine = False
            utility_being_used = False
            if ShowMineWhenPlayed:
                cl.send(str(['TO MY PARTNER', 'Played Mine']).encode(FORMAT))

        if s in [k.NUM_7, k._7] and placingMine:
            mine = ListOfMines[len(ListOfMines) - 1]
            futureMinePosition = [position[0] - 1, position[1] - 1]
            for island in islands:
                if island == futureMinePosition:
                    playsound(load_sound('Game Data/Sound Effects/You can\'t place your mine here.wav'))
                    return
            utility_being_used = False
            mine.y += 30 * (window.height / 720)
            mine.x -= 47 * (window.width / 1280)
            mine.Position = futureMinePosition.copy()
            placingMine = False
            utility_being_used = False
            if ShowMineWhenPlayed:
                cl.send(str(['TO MY PARTNER', 'Played Mine']).encode(FORMAT))

        if s in [k.NUM_8, k._8] and placingMine:
            mine = ListOfMines[len(ListOfMines) - 1]
            futureMinePosition = [position[0], position[1] - 1]
            for island in islands:
                if island == futureMinePosition:
                    playsound(load_sound('Game Data/Sound Effects/You can\'t place your mine here.wav'))
                    return
            utility_being_used = False
            mine.y += 30 * (window.height / 720)
            mine.Position = futureMinePosition.copy()
            placingMine = False
            utility_being_used = False
            if ShowMineWhenPlayed:
                cl.send(str(['TO MY PARTNER', 'Played Mine']).encode(FORMAT))

        if s in [k.NUM_4, k._4] and placingMine:
            mine = ListOfMines[len(ListOfMines) - 1]
            futureMinePosition = [position[0]-1, position[1]]
            for island in islands:
                if island == futureMinePosition:
                    playsound(load_sound('Game Data/Sound Effects/You can\'t place your mine here.wav'))
                    return
            utility_being_used = False
            mine.x -= 47 * (window.width / 1280)
            mine.Position = futureMinePosition.copy()
            placingMine = False
            utility_being_used = False
            if ShowMineWhenPlayed:
                cl.send(str(['TO MY PARTNER', 'Played Mine']).encode(FORMAT))

        if s in [k.NUM_6, k._6] and placingMine:
            mine = ListOfMines[len(ListOfMines) - 1]
            futureMinePosition = [position[0]+1, position[1]]
            for island in islands:
                if island == futureMinePosition:
                    playsound(load_sound('Game Data/Sound Effects/You can\'t place your mine here.wav'))
                    return
            utility_being_used = False
            mine.x += 47 * (window.width / 1280)
            mine.Position = futureMinePosition.copy()
            placingMine = False
            utility_being_used = False
            if ShowMineWhenPlayed:
                cl.send(str(['TO MY PARTNER', 'Played Mine']).encode(FORMAT))

        if s in [k.NUM_2, k._2] and placingMine:
            mine = ListOfMines[len(ListOfMines) - 1]
            futureMinePosition = [position[0], position[1]+1]
            for island in islands:
                if island == futureMinePosition:
                    playsound(load_sound('Game Data/Sound Effects/You can\'t place your mine here.wav'))
                    return
            utility_being_used = False
            mine.y -= 30 * (window.height / 720)
            mine.Position = futureMinePosition.copy()
            placingMine = False
            utility_being_used = False
            if ShowMineWhenPlayed:
                cl.send(str(['TO MY PARTNER', 'Played Mine']).encode(FORMAT))

        if s in (k.RETURN, k.ENTER, k.NUM_ENTER):
            if torpedo.visible:
                torpedo.visible = False
                explosion.x = torpedo.x - 50 * (window.width / 1280)
                explosion.y = torpedo.y - 50 * (window.height / 720)
                explosion.visible = True
                playsound(load_sound('Game Data/Sound Effects/explosion.wav'))
                pyglet.clock.schedule_once(cancel_explosion, 1.3333)
                cl.send(str(['TO MY PARTNER', 'EXPLOSION', torpedoPosition, 'torpedo']).encode(FORMAT))
                torpedoMoveSoFar = 0
                utility_being_used = False
            elif bomber.visible:
                bomber.visible = False
                explosion.x = bomber.x - 50 * (window.width / 1280)
                explosion.y = bomber.y - 50 * (window.height / 720)
                explosion.visible = True
                playsound(load_sound('Game Data/Sound Effects/explosion.wav'))
                pyglet.clock.schedule_once(cancel_explosion, 1.3333)
                cl.send(str(['TO MY PARTNER', 'EXPLOSION', bomber.Position, 'bomber']).encode(FORMAT))
                bomberMoveSoFar = 0
                utility_being_used = False
            elif drone.visible:
                drone.visible = False
                costume(explosion, load_gif('Game Data/Gifs/scanner.gif'))
                explosion.x = drone.x-(25*(window.width/1280))
                explosion.y = drone.y-(25*(window.height/720))
                explosion.visible = True
                playsound(load_sound('Game Data/Sound Effects/3 ping sonar for drone.wav'))
                pyglet.clock.schedule_once(cancel_explosion, 3)
                cl.send(str(['TO MY PARTNER', 'Drone Scan', drone.Position]).encode(FORMAT))
                drone_move_so_far = 0
                utility_being_used = False
            elif silenceTarget.visible:
                silenceTarget.visible = False
                silenceTargetMoveSoFar = 0
                utility_being_used = False
                costume(CommitButton, CommitButtonPic2)
                my_turn = False
                playsound(load_sound('Game Data/Sound Effects/button press.wav'))
                cl.send(str(['TO MY PARTNER', 'My Turn Done', 'used silence']).encode(FORMAT))
                for glow in ListOfGlows:
                    glow.visible = False
                chargeCommand = ''
                directionCommand = ''
                commands = ''
                Submarine.x = silenceTarget.position[0]
                Submarine.y = silenceTarget.position[1]
                position = silenceTarget.Position.copy()
                costume(WhooseTurn, notYourTurnPic)
                pyglet.clock.schedule_once(put_back_up, 1)
                CommandsLabel.text = ''
                deepDiveOn = False
                enemySubmarine.visible = False
                if sheilds > 0:
                    sheilds -= 1
                    if sheilds == 0:
                        costume(Submarine, center(load_image('Game Data/Captain Board/Captian Submarine.png')))

        if s == k.LEFT:
            if torpedo.visible:
                if torpedoMoveSoFar < 4:
                    torpedo.scale_x = abs(torpedo.scale_x)
                    torpedoPosition[0] -= 1
                    for island in islands:
                        if island == torpedoPosition:
                            torpedoPosition[0] += 1
                            return
                    torpedoMoveSoFar +=1
                    torpedo.x -= (47*(window.width/1280))
                else:
                    torpedo.visible = False
                    explosion.x = torpedo.x - 50 * (window.width / 1280)
                    explosion.y = torpedo.y - 50 * (window.height / 720)
                    explosion.visible = True
                    playsound(load_sound('Game Data/Sound Effects/explosion.wav'))
                    pyglet.clock.schedule_once(cancel_explosion, 1.3333)
                    cl.send(str(['TO MY PARTNER', 'EXPLOSION', torpedoPosition, 'torpedo']).encode(FORMAT))
                    torpedoMoveSoFar = 0
                    utility_being_used = False

            elif bomber.visible:
                if bomberMoveSoFar < 6:
                    bomber.rotation = -90
                    bomber.Position[0] -= 1
                    bomberMoveSoFar +=1
                    bomber.x -= (47*(window.width/1280))
                else:
                    bomber.visible = False
                    explosion.x = bomber.x - 50 * (window.width / 1280)
                    explosion.y = bomber.y - 50 * (window.height / 720)
                    explosion.visible = True
                    playsound(load_sound('Game Data/Sound Effects/explosion.wav'))
                    pyglet.clock.schedule_once(cancel_explosion, 1.3333)
                    cl.send(str(['TO MY PARTNER', 'EXPLOSION', bomber.Position, 'bomber']).encode(FORMAT))
                    bomberMoveSoFar = 0
                    utility_being_used = False

            elif drone.visible:
                if drone_switch.on == 'water':
                    if drone_move_so_far < drone.max_move_so_far:
                        drone.rotation = -90
                        drone.Position[0] -= 1
                        for island in islands:
                            if island == drone.Position:
                                drone.Position[0] += 1
                                return
                        drone_move_so_far += 1
                        drone.x -= (47 * (window.width / 1280))
                    else:
                        drone.visible = False
                        costume(explosion, load_gif('Game Data/Gifs/scanner.gif'))
                        explosion.x = drone.x - (25 * (window.width / 1280))
                        explosion.y = drone.y - (25 * (window.height / 720))
                        explosion.visible = True
                        playsound(load_sound('Game Data/Sound Effects/3 ping sonar for drone.wav'))
                        pyglet.clock.schedule_once(cancel_explosion, 3)
                        cl.send(str(['TO MY PARTNER', 'Drone Scan', drone.Position]).encode(FORMAT))
                        drone_move_so_far = 0
                        utility_being_used = False
                if drone_switch.on == 'air':
                    if drone_move_so_far < drone.max_air_drone_move:
                        drone.rotation = -90
                        drone.Position[0] -= 1
                        drone_move_so_far += 1
                        drone.x -= (47 * (window.width / 1280))
                    else:
                        drone.visible = False
                        costume(explosion, load_gif('Game Data/Gifs/scanner.gif'))
                        explosion.x = drone.x - (25 * (window.width / 1280))
                        explosion.y = drone.y - (25 * (window.height / 720))
                        explosion.visible = True
                        playsound(load_sound('Game Data/Sound Effects/3 ping sonar for drone.wav'))
                        pyglet.clock.schedule_once(cancel_explosion, 3)
                        cl.send(str(['TO MY PARTNER', 'Drone Scan', drone.Position]).encode(FORMAT))
                        drone_move_so_far = 0
                        utility_being_used = False

            elif silenceTarget.visible:
                if silenceTargetMoveSoFar < silenceTarget.max_move_so_far:
                    silenceTarget.Position[0] -= 1
                    if silenceTarget.Position[0] < 1:
                        silenceTarget.Position[0] += 1
                        return
                    for island in islands:
                        if island == silenceTarget.Position:
                            silenceTarget.Position[0] += 1
                            return
                    for coord in coordsITraveledSo:
                        if coord == silenceTarget.Position:
                            silenceTarget.Position[0] += 1
                            return
                    silenceTargetMoveSoFar += 1
                    silenceTarget.x -= (47 * (window.width / 1280))
                else:
                    silenceTarget.visible = False
                    silenceTargetMoveSoFar = 0
                    utility_being_used = False
                    costume(CommitButton, CommitButtonPic2)
                    my_turn = False
                    playsound(load_sound('Game Data/Sound Effects/button press.wav'))
                    cl.send(str(['TO MY PARTNER', 'My Turn Done', 'used silence']).encode(FORMAT))
                    for glow in ListOfGlows:
                        glow.visible = False
                    chargeCommand = ''
                    directionCommand = ''
                    commands = ''
                    Submarine.x = silenceTarget.x
                    Submarine.y = silenceTarget.y
                    position = silenceTarget.Position.copy()
                    costume(WhooseTurn, notYourTurnPic)
                    pyglet.clock.schedule_once(put_back_up, 1)
                    CommandsLabel.text = ''
                    deepDiveOn = False
                    enemySubmarine.visible = False
                    if sheilds > 0:
                        sheilds -= 1
                        if sheilds == 0:
                            costume(Submarine, center(load_image('Game Data/Captain Board/Captian Submarine.png')))


            else:
                leftpressed = True
        if s == k.RIGHT:
            if torpedo.visible:
                if torpedoMoveSoFar < 4:
                    torpedo.scale_x = -abs(torpedo.scale_x)
                    torpedoPosition[0] += 1
                    for island in islands:
                        if island == torpedoPosition:
                            torpedoPosition[0] -= 1
                            return
                    torpedoMoveSoFar += 1
                    torpedo.x += (47 * (window.width / 1280))
                else:
                    torpedo.visible = False
                    explosion.x = torpedo.x - 50 * (window.width / 1280)
                    explosion.y = torpedo.y - 50 * (window.height / 720)
                    explosion.visible = True
                    playsound(load_sound('Game Data/Sound Effects/explosion.wav'))
                    pyglet.clock.schedule_once(cancel_explosion, 1.3333)
                    cl.send(str(['TO MY PARTNER', 'EXPLOSION', torpedoPosition, 'torpedo']).encode(FORMAT))
                    torpedoMoveSoFar = 0
                    utility_being_used = False

            elif bomber.visible:
                if bomberMoveSoFar < 6:
                    bomber.rotation = 90
                    bomber.Position[0] += 1
                    bomberMoveSoFar +=1
                    bomber.x += (47*(window.width/1280))
                else:
                    bomber.visible = False
                    explosion.x = bomber.x - 50 * (window.width / 1280)
                    explosion.y = bomber.y - 50 * (window.height / 720)
                    explosion.visible = True
                    playsound(load_sound('Game Data/Sound Effects/explosion.wav'))
                    pyglet.clock.schedule_once(cancel_explosion, 1.3333)
                    cl.send(str(['TO MY PARTNER', 'EXPLOSION', bomber.Position, 'bomber']).encode(FORMAT))
                    bomberMoveSoFar = 0
                    utility_being_used = False

            elif drone.visible:
                if drone_switch.on == 'water':
                    if drone_move_so_far < drone.max_move_so_far:
                        drone.rotation = 90
                        drone.Position[0] += 1
                        for island in islands:
                            if island == drone.Position:
                                drone.Position[0] -= 1
                                return
                        drone_move_so_far += 1
                        drone.x += (47 * (window.width / 1280))
                    else:
                        drone.visible = False
                        costume(explosion, load_gif('Game Data/Gifs/scanner.gif'))
                        explosion.x = drone.x - (25 * (window.width / 1280))
                        explosion.y = drone.y - (25 * (window.height / 720))
                        explosion.visible = True
                        playsound(load_sound('Game Data/Sound Effects/3 ping sonar for drone.wav'))
                        pyglet.clock.schedule_once(cancel_explosion, 3)
                        cl.send(str(['TO MY PARTNER', 'Drone Scan', drone.Position]).encode(FORMAT))
                        drone_move_so_far = 0
                        utility_being_used = False
                if drone_switch.on == 'air':
                    if drone_move_so_far < drone.max_air_drone_move:
                        drone.rotation = 90
                        drone.Position[0] += 1
                        drone_move_so_far += 1
                        drone.x += (47 * (window.width / 1280))
                    else:
                        drone.visible = False
                        costume(explosion, load_gif('Game Data/Gifs/scanner.gif'))
                        explosion.x = drone.x - (25 * (window.width / 1280))
                        explosion.y = drone.y - (25 * (window.height / 720))
                        explosion.visible = True
                        playsound(load_sound('Game Data/Sound Effects/3 ping sonar for drone.wav'))
                        pyglet.clock.schedule_once(cancel_explosion, 3)
                        cl.send(str(['TO MY PARTNER', 'Drone Scan', drone.Position]).encode(FORMAT))
                        drone_move_so_far = 0
                        utility_being_used = False

            elif silenceTarget.visible:
                if silenceTargetMoveSoFar < silenceTarget.max_move_so_far:
                    silenceTarget.Position[0] += 1
                    if silenceTarget.Position[0] > 15:
                        silenceTarget.Position[0] -= 1
                        return
                    for island in islands:
                        if island == silenceTarget.Position:
                            silenceTarget.Position[0] -= 1
                            return
                    for coord in coordsITraveledSo:
                        if coord == silenceTarget.Position:
                            silenceTarget.Position[0] -= 1
                            return
                    silenceTargetMoveSoFar += 1
                    silenceTarget.x += (47 * (window.width / 1280))
                else:
                    silenceTarget.visible = False
                    silenceTargetMoveSoFar = 0
                    utility_being_used = False
                    costume(CommitButton, CommitButtonPic2)
                    my_turn = False
                    playsound(load_sound('Game Data/Sound Effects/button press.wav'))
                    cl.send(str(['TO MY PARTNER', 'My Turn Done', 'used silence']).encode(FORMAT))
                    for glow in ListOfGlows:
                        glow.visible = False
                    chargeCommand = ''
                    directionCommand = ''
                    commands = ''
                    Submarine.x = silenceTarget.x
                    Submarine.y = silenceTarget.y
                    position = silenceTarget.Position.copy()
                    costume(WhooseTurn, notYourTurnPic)
                    pyglet.clock.schedule_once(put_back_up, 1)
                    CommandsLabel.text = ''
                    deepDiveOn = False
                    enemySubmarine.visible = False
                    if sheilds > 0:
                        sheilds -= 1
                        if sheilds == 0:
                            costume(Submarine, center(load_image('Game Data/Captain Board/Captian Submarine.png')))

            else:
                rightpressed = True
        if s == k.DOWN:
            if torpedo.visible:
                if torpedoMoveSoFar < 4:
                    torpedoPosition[1] += 1
                    for island in islands:
                        if island == torpedoPosition:
                            torpedoPosition[1] -= 1
                            return
                    torpedoMoveSoFar += 1
                    torpedo.y -= (30 * (window.height/720))
                else:
                    torpedo.visible = False
                    explosion.x = torpedo.x - 50 * (window.width / 1280)
                    explosion.y = torpedo.y - 50 * (window.height / 720)
                    explosion.visible = True
                    playsound(load_sound('Game Data/Sound Effects/explosion.wav'))
                    pyglet.clock.schedule_once(cancel_explosion, 1.3333)
                    cl.send(str(['TO MY PARTNER', 'EXPLOSION', torpedoPosition, 'torpedo']).encode(FORMAT))
                    torpedoMoveSoFar = 0
                    utility_being_used = False

            elif bomber.visible:
                if bomberMoveSoFar < 6:
                    bomber.rotation = 180
                    bomber.Position[1] += 1
                    bomberMoveSoFar += 1
                    bomber.y -= (30 * (window.height / 720))
                else:
                    bomber.visible = False
                    explosion.x = bomber.x - 50 * (window.width / 1280)
                    explosion.y = bomber.y - 50 * (window.height / 720)
                    explosion.visible = True
                    playsound(load_sound('Game Data/Sound Effects/explosion.wav'))
                    pyglet.clock.schedule_once(cancel_explosion, 1.3333)
                    cl.send(str(['TO MY PARTNER', 'EXPLOSION', bomber.Position, 'bomber']).encode(FORMAT))
                    bomberMoveSoFar = 0
                    utility_being_used = False

            elif drone.visible:
                if drone_switch.on == 'water':
                    if drone_move_so_far < drone.max_move_so_far:
                        drone.rotation = 180
                        drone.Position[1] += 1
                        for island in islands:
                            if island == drone.Position:
                                drone.Position[1] -= 1
                                return
                        drone_move_so_far += 1
                        drone.y -= (30 * (window.height / 720))
                    else:
                        drone.visible = False
                        costume(explosion, load_gif('Game Data/Gifs/scanner.gif'))
                        explosion.x = drone.x - (25 * (window.width / 1280))
                        explosion.y = drone.y - (25 * (window.height / 720))
                        explosion.visible = True
                        playsound(load_sound('Game Data/Sound Effects/3 ping sonar for drone.wav'))
                        pyglet.clock.schedule_once(cancel_explosion, 3)
                        cl.send(str(['TO MY PARTNER', 'Drone Scan', drone.Position]).encode(FORMAT))
                        drone_move_so_far = 0
                        utility_being_used = False
                if drone_switch.on == 'air':
                    if drone_move_so_far < drone.max_air_drone_move:
                        drone.rotation = 180
                        drone.Position[1] += 1
                        drone_move_so_far += 1
                        drone.y -= (30 * (window.height / 720))
                    else:
                        drone.visible = False
                        costume(explosion, load_gif('Game Data/Gifs/scanner.gif'))
                        explosion.x = drone.x - (25 * (window.width / 1280))
                        explosion.y = drone.y - (25 * (window.height / 720))
                        explosion.visible = True
                        playsound(load_sound('Game Data/Sound Effects/3 ping sonar for drone.wav'))
                        pyglet.clock.schedule_once(cancel_explosion, 3)
                        cl.send(str(['TO MY PARTNER', 'Drone Scan', drone.Position]).encode(FORMAT))
                        drone_move_so_far = 0
                        utility_being_used = False

            elif silenceTarget.visible:
                if silenceTargetMoveSoFar < silenceTarget.max_move_so_far:
                    silenceTarget.Position[1] += 1
                    if silenceTarget.Position[1] > 15:
                        silenceTarget.Position[1] -= 1
                        return
                    for island in islands:
                        if island == silenceTarget.Position:
                            silenceTarget.Position[1] -= 1
                            return
                    for coord in coordsITraveledSo:
                        if coord == silenceTarget.Position:
                            silenceTarget.Position[1] -= 1
                            return
                    silenceTargetMoveSoFar += 1
                    silenceTarget.y -= (30 * (window.height / 720))
                else:
                    silenceTarget.visible = False
                    silenceTargetMoveSoFar = 0
                    utility_being_used = False
                    costume(CommitButton, CommitButtonPic2)
                    my_turn = False
                    playsound(load_sound('Game Data/Sound Effects/button press.wav'))
                    cl.send(str(['TO MY PARTNER', 'My Turn Done', 'used silence']).encode(FORMAT))
                    for glow in ListOfGlows:
                        glow.visible = False
                    chargeCommand = ''
                    directionCommand = ''
                    commands = ''
                    Submarine.x = silenceTarget.position[0]
                    Submarine.y = silenceTarget.position[1]
                    position = silenceTarget.Position.copy()
                    costume(WhooseTurn, notYourTurnPic)
                    pyglet.clock.schedule_once(put_back_up, 1)
                    CommandsLabel.text = ''
                    deepDiveOn = False
                    enemySubmarine.visible = False
                    if sheilds > 0:
                        sheilds -= 1
                        if sheilds == 0:
                            costume(Submarine, center(load_image('Game Data/Captain Board/Captian Submarine.png')))

            else:
                downpressed = True
        if s == k.UP:
            if torpedo.visible:
                if torpedoMoveSoFar < 4:
                    torpedoPosition[1] -= 1
                    for island in islands:
                        if island == torpedoPosition:
                            torpedoPosition[1] += 1
                            return
                    torpedoMoveSoFar += 1
                    torpedo.y += (30 * (window.height/720))
                else:
                    torpedo.visible = False
                    explosion.x = torpedo.x - 50*(window.width/1280)
                    explosion.y = torpedo.y - 50*(window.height/720)
                    explosion.visible = True
                    playsound(load_sound('Game Data/Sound Effects/explosion.wav'))
                    pyglet.clock.schedule_once(cancel_explosion, 1.3333)
                    cl.send(str(['TO MY PARTNER', 'EXPLOSION', torpedoPosition, 'torpedo']).encode(FORMAT))
                    torpedoMoveSoFar = 0
                    utility_being_used = False

            elif bomber.visible:
                if bomberMoveSoFar < 6:
                    bomber.rotation = 0
                    bomber.Position[1] -= 1
                    bomberMoveSoFar +=1
                    bomber.y += (30*(window.height/720))
                else:
                    bomber.visible = False
                    explosion.x = bomber.x - 50 * (window.width / 1280)
                    explosion.y = bomber.y - 50 * (window.height / 720)
                    explosion.visible = True
                    playsound(load_sound('Game Data/Sound Effects/explosion.wav'))
                    pyglet.clock.schedule_once(cancel_explosion, 1.3333)
                    cl.send(str(['TO MY PARTNER', 'EXPLOSION', bomber.Position, 'bomber']).encode(FORMAT))
                    bomberMoveSoFar = 0
                    utility_being_used = False

            elif drone.visible:
                if drone_switch.on == 'water':
                    if drone_move_so_far < drone.max_move_so_far:
                        drone.rotation = 0
                        drone.Position[1] -= 1
                        for island in islands:
                            if island == drone.Position:
                                drone.Position[1] += 1
                                return
                        drone_move_so_far += 1
                        drone.y += (30 * (window.height / 720))
                    else:
                        drone.visible = False
                        costume(explosion, load_gif('Game Data/Gifs/scanner.gif'))
                        explosion.x = drone.x - (25 * (window.width / 1280))
                        explosion.y = drone.y - (25 * (window.height / 720))
                        explosion.visible = True
                        playsound(load_sound('Game Data/Sound Effects/3 ping sonar for drone.wav'))
                        pyglet.clock.schedule_once(cancel_explosion, 3)
                        cl.send(str(['TO MY PARTNER', 'Drone Scan', drone.Position]).encode(FORMAT))
                        drone_move_so_far = 0
                        utility_being_used = False
                if drone_switch.on == 'air':
                    if drone_move_so_far < drone.max_air_drone_move:
                        drone.rotation = 0
                        drone.Position[1] -= 1
                        drone_move_so_far += 1
                        drone.y += (30 * (window.height / 720))
                    else:
                        drone.visible = False
                        costume(explosion, load_gif('Game Data/Gifs/scanner.gif'))
                        explosion.x = drone.x - (25 * (window.width / 1280))
                        explosion.y = drone.y - (25 * (window.height / 720))
                        explosion.visible = True
                        playsound(load_sound('Game Data/Sound Effects/3 ping sonar for drone.wav'))
                        pyglet.clock.schedule_once(cancel_explosion, 3)
                        cl.send(str(['TO MY PARTNER', 'Drone Scan', drone.Position]).encode(FORMAT))
                        drone_move_so_far = 0
                        utility_being_used = False

            elif silenceTarget.visible:
                if silenceTargetMoveSoFar < silenceTarget.max_move_so_far:
                    silenceTarget.Position[1] -= 1
                    if silenceTarget.Position[1] < 1:
                        silenceTarget.Position[1] += 1
                        return
                    for island in islands:
                        if island == silenceTarget.Position:
                            silenceTarget.Position[1] += 1
                            return
                    for coord in coordsITraveledSo:
                        if coord == silenceTarget.Position:
                            silenceTarget.Position[1] += 1
                            return
                    silenceTargetMoveSoFar += 1
                    silenceTarget.y += (30 * (window.height / 720))
                else:
                    silenceTarget.visible = False
                    silenceTargetMoveSoFar = 0
                    utility_being_used = False
                    costume(CommitButton, CommitButtonPic2)
                    my_turn = False
                    playsound(load_sound('Game Data/Sound Effects/button press.wav'))
                    cl.send(str(['TO MY PARTNER', 'My Turn Done', 'used silence']).encode(FORMAT))
                    for glow in ListOfGlows:
                        glow.visible = False
                    chargeCommand = ''
                    directionCommand = ''
                    commands = ''
                    Submarine.x = silenceTarget.x
                    Submarine.y = silenceTarget.y
                    position = silenceTarget.Position.copy()
                    costume(WhooseTurn, notYourTurnPic)
                    pyglet.clock.schedule_once(put_back_up, 1)
                    CommandsLabel.text = ''
                    deepDiveOn = False
                    enemySubmarine.visible = False
                    if sheilds > 0:
                        sheilds -= 1
                        if sheilds == 0:
                            costume(Submarine, center(load_image('Game Data/Captain Board/Captian Submarine.png')))

            else:
                uppressed = True

silenceTargetMoveSoFar = 0
drone_move_so_far = 0
TimeLeftUntilPlayBegins = 0
bomberMoveSoFar = 0
sheilds = 0
deepDiveOn = False
placingMine = False
utility_being_used = False
torpedoPosition = []
torpedoMoveSoFar = 0
leftpressed = False
rightpressed = False
uppressed = False
downpressed = False
mineSweeperOn = False
def put_back_up(dt):
    costume(CommitButton, CommitButtonPic1)

@window.event
def on_mouse_press(x, y, but, mod):
    global KnobUp, I_made_this_game, commands, directionCommand, chargeCommand,  my_turn, position, switch_on_charge, torpedoPosition, utility_being_used, placingMine, deepDiveOn, sheilds, TimeLeftUntilPlayBegins, enginnerCommand, ListOfUsedEnginneringStuff, lives, mineSweeperOn
    print(x, y)
    if Scene == 'stats':
        if math.dist((x, y), (1224*(window.width/1280), 638*(window.height/720))) < Range:
            costume(back_to_title_screen_button, load_image('Game Data/Buttons/return to title screen button (down).png'))
            playsound(load_sound('Game Data/Sound Effects/button press.wav'))
            pyglet.clock.schedule_once(make_welcome_screen, 1)
    if Scene == 'Welcome':
        if math.dist((x, y), (28*(window.width/1280), 670*(window.height/720))) < Range:#Login switch pressed
            if login_switch.on:
                login_switch.on = False
                playsound(load_sound('Game Data/Sound Effects/Switch Sound.wav'))
                costume(login_switch, load_image('Game Data/Buttons/Periscope button (up).png'))
            else:
                login_switch.on = True
                playsound(load_sound('Game Data/Sound Effects/Switch Sound.wav'))
                costume(login_switch, load_image('Game Data/Buttons/Periscope button (down).png'))
        if math.dist((x, y), (639*(window.width/1280), (71*(window.height/720)))) < Range:
            if perscope.y < perscope.up:
                return
            costume(stats_button, load_image('Game Data/Buttons/Stats button (down).png'))
            playsound(load_sound('Game Data/Sound Effects/button press.wav'))
            pyglet.clock.schedule_once(make_stats_board, 1)
            cl.send(str(['Give Me Stats']).encode(FORMAT))
        if math.dist((x, y), (1064*(window.width/1280), 108*(window.width/1280))) < Range:
            if perscope.y < perscope.up:
                return
            costume(RedButton, RedButtonPic2)
            playsound(load_sound('Game Data/Sound Effects/button press.wav'))
            if KnobUp:
                pyglet.clock.schedule_once(make_map_board, 1)
            else:
                pyglet.clock.schedule_once(make_join_board, 1)
                cl.send(str(['Give Me Rooms']).encode(FORMAT))
        if math.dist((x, y), (190*(window.width/1280), 98*(window.width/1280))) < Range:
            if KnobUp:
                costume(Knob, KnobPic2)
                KnobUp = False
            else:
                costume(Knob, KnobPic1)
                KnobUp = True
            playsound(load_sound('Game Data/Sound Effects/knob turning sound.wav'))

    if Scene == 'maps':
        if math.dist((170*(window.width/1280), 655*(window.height/720)), (x, y)) < Range:#return to main menu button pressed
            costume(back_to_title_screen_button_for_joining_and_making_a_game, load_image('Game Data/Buttons/return to title screen (down) from map selection screen.png'))
            playsound(load_sound('Game Data/Sound Effects/button press.wav'))
            pyglet.clock.schedule_once(make_welcome_screen, 1)

        if math.dist((43*(window.width/1280), 46*(window.height/720)), (x, y)) < 10*(window.height/720):#tell what weapon hit you dot pressed
            if tell_what_hit_me_dot.on:
                costume(tell_what_hit_me_dot, load_image('Game Data/Buttons/yellow light off (weapons).png'))
                tell_what_hit_me_dot.on = False
                costume(Setting_options[Setting_options.index(Settings_weapons_option)], load_image('Game Data/Settings Tab/weapons detection indicator light (off).png'))

            else:
                costume(tell_what_hit_me_dot, load_image('Game Data/Buttons/yellow light on (weapons).png'))
                tell_what_hit_me_dot.on = True
                costume(Setting_options[Setting_options.index(Settings_weapons_option)],
                        load_image('Game Data/Settings Tab/weapons detection indicator light (on).png'))

        elif math.dist((121*(window.width/1280), 47*(window.height/720)), (x, y)) < 10*(window.height/720):#tell when mines deployed dot pressed
            if ShowMineWhenPlayed_dot.on:
                costume(ShowMineWhenPlayed_dot, load_image('Game Data/Buttons/yellow light off (mines).png'))
                ShowMineWhenPlayed_dot.on = False
                costume(Setting_options[Setting_options.index(Settings_mine_option)],
                        load_image('Game Data/Settings Tab/mine detection indicator light (off).png'))

            else:
                costume(ShowMineWhenPlayed_dot, load_image('Game Data/Buttons/yellow light on (mines).png'))
                ShowMineWhenPlayed_dot.on = True
                costume(Setting_options[Setting_options.index(Settings_mine_option)],
                        load_image('Game Data/Settings Tab/mine detection indicator light (on).png'))

        elif math.dist((199*(window.width/1280), 49*(window.height/720)), (x, y)) < 10*(window.height/720):#tell when you are found dot pressed
            if tell_if_drone_found_me_dot.on:
                costume(tell_if_drone_found_me_dot, load_image('Game Data/Buttons/yellow light off (location).png'))
                tell_if_drone_found_me_dot.on = False
                costume(Setting_options[Setting_options.index(Settings_location_option)],
                        load_image('Game Data/Settings Tab/location detection indicator light (off).png'))

            else:
                costume(tell_if_drone_found_me_dot, load_image('Game Data/Buttons/yellow light on (location).png'))
                tell_if_drone_found_me_dot.on = True
                costume(Setting_options[Setting_options.index(Settings_location_option)],
                        load_image('Game Data/Settings Tab/location detection indicator light (on).png'))

        if math.dist((69*(window.width/1280), 371*(window.height/720)), (x, y)) < 30*(window.height/720):
            if Sonar_switch.on == 'Shields':
                playsound(load_sound('Game Data/Sound Effects/Switch Sound.wav'))
                Sonar_switch.on = 'Utilitys'
                costume(Sonar_switch, load_image('Game Data/Buttons/sonar switch (to utility).png'))
                costume(Setting_options[Setting_options.index(Settings_sonar_option)],
                        load_image('Game Data/Settings Tab/sonar option (utility).png'))



            elif Sonar_switch.on == 'Utilitys':
                playsound(load_sound('Game Data/Sound Effects/Switch Sound.wav'))
                Sonar_switch.on = 'Shields'
                costume(Sonar_switch, load_image('Game Data/Buttons/sonar switch (to shield).png'))
                costume(Setting_options[Setting_options.index(Settings_sonar_option)],
                        load_image('Game Data/Settings Tab/sonar option (shield).png'))

        if math.dist((203*(window.width/1280), 371*(window.height/720)), (x, y)) < 30*(window.height/720):
            if enginneringSwitch.on:
                playsound(load_sound('Game Data/Sound Effects/Switch Sound.wav'))
                enginneringSwitch.on = False
                costume(enginneringSwitch, load_image('Game Data/Buttons/engineering toggle down.png'))
                costume(Setting_options[Setting_options.index(Settings_engineer_option)],
                        load_image('Game Data/Settings Tab/engineering option (off).png'))

            elif not enginneringSwitch.on:
                playsound(load_sound('Game Data/Sound Effects/Switch Sound.wav'))
                enginneringSwitch.on = True
                costume(enginneringSwitch, load_image('Game Data/Buttons/engineering toggle up.png'))
                costume(Setting_options[Setting_options.index(Settings_engineer_option)],
                        load_image('Game Data/Settings Tab/engineering option (on).png'))

        for text in ListOfMaxNumbers:
            if math.dist((x, y), (text.minus[0]*(window.width/1280), text.minus[1]*(window.height/720))) < 10*(window.height/720):
                number = int(text.text)
                number -= 1
                if number < 1:
                    return
                else:
                    text.text = str(number)
        for text in ListOfMaxNumbers:
            if math.dist((x, y), (text.plus[0]*(window.width/1280), text.plus[1]*(window.height/720))) < 10*(window.height/720):
                number = int(text.text)
                number += 1
                if number > 8:
                    return
                else:
                    text.text = str(number)
        for dot in ListOfFullChargeDots:
            if math.dist((dot.click[0]*(window.width/1280), (dot.click[1]*(window.height/720))), (x, y)) < 10*(window.height/720):
                if dot.on:
                    dot.on = False
                    costume(dot, load_image('Game Data/Buttons/start with full charge (off).png'))
                else:
                    dot.on = True
                    costume(dot, load_image('Game Data/Buttons/start with full charge (on).png'))
        if math.dist((x, y), (987 * (window.width / 1280), 69 * (window.width / 1280))) < Range:
            new_list = []
            New_list = []
            for dot in ListOfFullChargeDots:
                new_list.append(dot.on)
            for number in ListOfMaxNumbers:
                New_list.append(int(number.text))
            costume(CommitButtonMap, CommitButtonPic2)
            pyglet.clock.schedule_once(make_loading_board, 1)
            playsound(load_sound('Game Data/Sound Effects/button press.wav'))
            cl.send(str(['New Game', ChoiceText.text, f'{my_name_Label.text}\'s Game', new_list, New_list, enginneringSwitch.on, tell_what_hit_me_dot.on, ShowMineWhenPlayed_dot.on, tell_if_drone_found_me_dot.on, Sonar_switch.on]).encode(FORMAT))
            costume(PlayingBoard, load_image(f'Game Data/game boards/Real Maps/{ShowMapPics[ShowMapIndex].title}.png'))
            I_made_this_game = True

    if Scene == 'join':
        if math.dist((170*(window.width/1280), 655*(window.height/720)), (x, y)) < Range:#return to main menu button pressed
            costume(back_to_title_screen_button_for_joining_and_making_a_game, load_image('Game Data/Buttons/return to title screen (down) from map selection screen.png'))
            playsound(load_sound('Game Data/Sound Effects/button press.wav'))
            pyglet.clock.schedule_once(make_welcome_screen, 1)


        if math.dist((x, y), (987 * (window.width / 1280), 69 * (window.width / 1280))) < Range:
            costume(CommitButtonMap, CommitButtonPic2)
            playsound(load_sound('Game Data/Sound Effects/button press.wav'))
            cl.send(str(['JOINING GAME', ChoiceText.text]).encode(FORMAT))
            for index in range(len(rooms)):
                if rooms[index][1] == ChoiceText.text:
                    costume(PlayingBoard, load_image(f'Game Data/game boards/Real Maps/{rooms[index][0]}.png'))
                    pyglet.clock.schedule_once(make_game_board, 1)

    if Scene == 'playing' or Scene == 'Select':
        if math.dist((7*(window.width/1280), 380*(window.height/720)), (x, y)) < 40*(window.height/720):
            if not Settings_panel.over:
                Settings_panel.over = True
        if math.dist((458*(window.width/1280), 380*(window.height/720)), (x, y)) < 40*(window.height/720):
            if Settings_panel.over:
                Settings_panel.over = False

    if Scene == 'playing' and my_turn:
        if mineSweeperOn:
            for mine in ListOfEnemyMines:
                if math.dist((x, y), (mine.x, mine.y)) < 22 * (window.height / 720):
                    ListOfEnemyMines.remove(mine)
                    costume(explosion, load_gif('Game Data/Gifs/mine sweeper.gif'))
                    explosion.x = mine.x - 50 * (window.width / 1280)
                    explosion.y = mine.y - 50 * (window.height / 720)
                    explosion.visible = True
                    pyglet.clock.schedule_once(cancel_explosion, 1.3333)
                    cl.send(str(['TO MY PARTNER', 'Mine Disabled', mine.Position, 'mine']).encode(FORMAT))
            mineSweeperOn = False

        if usingEnginnering:
            for overlay in ListOfEnginnerOverlays:
                if math.dist((x, y), (overlay.x, overlay.y)) < 20*(window.height/720):# enginner button pressed
                    enginnerglow.x = overlay.x-40*(window.width/1280)
                    enginnerglow.y = overlay.y-40*(window.height/720)
                    enginnerglow.visible = True
                    enginnerCommand = overlay.id

        if math.dist((x, y), (834*(window.width/1280), 680*(window.height/720))) < (30*(window.height/720)) and not utility_being_used:#Surface Button Pressed
            test_list = ListOfUsedEnginneringStuff.copy()
            for distinct1 in test_list:
                    ListOfUsedEnginneringStuff.remove(distinct1)
                    ListOfEnginnerOverlays.append(distinct1)
                    distinct1.visible = False
                    costume(distinct1, center(load_image('Game Data/Buttons/enginener circle.png')))
            TimeLeftUntilPlayBegins = 2#ends up being 2
            costume(SurfaceButton, SurfaceAboveWaterPic)
            playsound(load_sound('Game Data/Sound Effects/button press.wav'))
            cl.send(str(['TO MY PARTNER', 'My Turn Done', 'surfaced']).encode(FORMAT))
            for glow in ListOfGlows:
                glow.visible = False
            chargeCommand = ''
            directionCommand = ''
            costume(WhooseTurn, notYourTurnPic)
            yourTrail.clear()
            my_turn = False
            coordsITraveledSo.clear()
            commands = ''
            CommandsLabel.text = ''
            deepDiveOn = False
            if sheilds > 0:
                sheilds -= 1
                if sheilds == 0:
                    costume(Submarine, center(load_image('Game Data/Captain Board/Captian Submarine.png')))

        if not utility_being_used:
            for mine in ListOfMines:
                if math.dist((x, y), (mine.x, mine.y)) < 22*(window.height/720):
                    if mine.disabled:
                        ListOfMines.remove(mine)
                        costume(explosion, load_gif('Game Data/Gifs/mine sweeper.gif'))
                        explosion.x = mine.x - 50 * (window.width / 1280)
                        explosion.y = mine.y - 50 * (window.height / 720)
                        explosion.visible = True
                        pyglet.clock.schedule_once(cancel_explosion, 1.3333)
                        return
                    ListOfMines.remove(mine)
                    explosion.x = mine.x - 50 * (window.width / 1280)
                    explosion.y = mine.y - 50 * (window.height / 720)
                    explosion.visible = True
                    playsound(load_sound('Game Data/Sound Effects/explosion.wav'))
                    pyglet.clock.schedule_once(cancel_explosion, 1.3333)
                    cl.send(str(['TO MY PARTNER', 'EXPLOSION', mine.Position, 'mine']).encode(FORMAT))


        if math.dist((1017 * (window.width / 1280), 174 * (window.height / 720)), (x, y)) < 30 * (window.height / 720):  # mine switch pressed
            if mine_switch.on == 'sweep':
                costume(mine_switch, load_image('Game Data/Buttons/Mine Switch (mine).png'))
                playsound(load_sound('Game Data/Sound Effects/Switch Sound.wav'))
                mine_switch.on = 'plant'
            else:
                costume(mine_switch, load_image('Game Data/Buttons/Mine Switch (sweep).png'))
                playsound(load_sound('Game Data/Sound Effects/Switch Sound.wav'))
                mine_switch.on = 'sweep'


        if math.dist((1142*(window.width/1280), 290*(window.height/720)), (x, y)) < 30*(window.height/720):#drone switch pressed
            if drone_switch.on == 'air':
                costume(drone_switch, load_image('Game Data/Buttons/drone toggle (sea).png'))
                drone_switch.on = 'water'
                costume(drone, center(load_image('Game Data/Captain Board/drone.png')))
            else:
                costume(drone_switch, load_image('Game Data/Buttons/drone toggle (air).png'))
                drone_switch.on = 'air'
                costume(drone, center(load_image('Game Data/Captain Board/airDrone.png')))

        if math.dist((x, y), (897*(window.width/1280), (159*(window.height/720)))) < 30*(window.height/720):#switch pressed
            if switch_on_charge:
                switch_on_charge = False
                costume(First_mate_switch, First_mate_switch_usePic)
            else:
                switch_on_charge = True
                costume(First_mate_switch, First_mate_switch_chargePic)
            playsound(load_sound('Game Data/Sound Effects/Switch Sound.wav'))

        if math.dist((x, y), (834*(window.width/1280), 249*(window.height/720))) < 40*(window.height/720):#Commit button pressed
            if utility_being_used:
                playsound(load_sound('Game Data/Sound Effects/Finishing using utility.wav'))
                return

            if not (directionCommand != '' and chargeCommand != ''):
                if usingEnginnering:
                    playsound(load_sound('Game Data/Sound Effects/Move a direction, charge utility and select engineering option.wav'))
                else:
                    playsound(load_sound('Game Data/Sound Effects/You must charge and choose direction first.wav'))
                return
            prepositoin = position.copy()
            if directionCommand == 'n':
                position = [position[0], position[1]-1]
                sprite = correctSprite(pyglet.sprite.Sprite(ylinePic, x=Submarine.x, y=Submarine.y + (15 * (window.height / 720))))
                Dir = Submarine.scale_x
            if directionCommand == 's':
                position = [position[0], position[1]+1]
                sprite = correctSprite(pyglet.sprite.Sprite(ylinePic, x=Submarine.x, y=Submarine.y - (15 * (window.height / 720))))
                Dir = Submarine.scale_x
            if directionCommand == 'e':
                position = [position[0]+1, position[1]]
                sprite = correctSprite(pyglet.sprite.Sprite(xlinePic, x=Submarine.x + (23 * (window.width / 1280)), y=Submarine.y))
                Dir = -abs(Submarine.scale_x)
            if directionCommand == 'w':
                position = [position[0]-1, position[1]]
                sprite = correctSprite(pyglet.sprite.Sprite(xlinePic, x=Submarine.x - (23 * (window.width / 1280)), y=Submarine.y))
                Dir = abs(Submarine.scale_x)
            if position[0] < 1:
                playsound(load_sound('Game Data/Sound Effects/Sorry you can\'t move there.wav'))
                position = prepositoin.copy()
                return
            if position[0] > 15:
                playsound(load_sound('Game Data/Sound Effects/Sorry you can\'t move there.wav'))
                position = prepositoin.copy()
                return
            if position[1] > 15:
                playsound(load_sound('Game Data/Sound Effects/Sorry you can\'t move there.wav'))
                position = prepositoin.copy()
                return
            if position[0] < 1:
                playsound(load_sound('Game Data/Sound Effects/Sorry you can\'t move there.wav'))
                position = prepositoin.copy()
                return
            if position in coordsITraveledSo and not deepDiveOn:
                playsound(load_sound('Game Data/Sound Effects/Sorry you can\'t move there.wav'))
                position = prepositoin.copy()
                return
            for island in islands:
                if island == position:
                    position = prepositoin.copy()
                    playsound(load_sound('Game Data/Sound Effects/Sorry you can\'t move there.wav'))
                    return
            if position[0] < 1 or position[0] > 15:
                playsound(load_sound('Game Data/Sound Effects/Sorry you can\'t move there.wav'))
                position = prepositoin.copy()
                return
            if position[1] < 1 or position[1] > 15:
                playsound(load_sound('Game Data/Sound Effects/Sorry you can\'t move there.wav'))
                position = prepositoin.copy()
                return

            if usingEnginnering:

                if enginnerCommand == '':
                    playsound(load_sound('Game Data/Sound Effects/Move a direction, charge utility and select engineering option.wav'))
                    position = prepositoin.copy()
                    return
                for overlay in ListOfEnginnerOverlays:
                    if overlay.id == enginnerCommand:
                        if overlay.direction != directionCommand and directionCommand != '':
                            playsound(load_sound('Game Data/Sound Effects/The direction you choose must match.wav'))
                            position = prepositoin.copy()
                            return
                        ListOfEnginnerOverlays.remove(overlay)
                        ListOfUsedEnginneringStuff.append(overlay)
                        costume(overlay, center(load_image('Game Data/Misc/engineering board cross out.png')))
                        overlay.visible = True



                westcount = 0
                copyList = ListOfUsedEnginneringStuff.copy()
                for overlay in copyList:  # check for full pipes
                    if overlay.direction == 'w':
                        westcount += 1
                if westcount == 6:  # clear yellow pipe
                    for distinct1 in copyList:
                        if distinct1.kind == 'w':
                            ListOfUsedEnginneringStuff.remove(distinct1)
                            ListOfEnginnerOverlays.append(distinct1)
                            distinct1.visible = False
                            costume(distinct1, center(load_image('Game Data/Buttons/enginener circle.png')))
                    lives -= 1
                    cl.send(str(['TO MY PARTNER', 'My Lives', lives]).encode(FORMAT))
                    try:
                        costume(DamageMeter, eval(f"DamageMeterPic{lives}"))
                    except NameError:
                        cl.send(str(['TO MY PARTNER', 'You Win']).encode(FORMAT))
                        costume(GameOver, load_gif('Game Data/Gifs/you lose.gif'))
                        GameOver.visible = True

                northcount = 0
                copyList = ListOfUsedEnginneringStuff.copy()
                for overlay in copyList:  # check for full pipes
                    if overlay.direction == 'n':
                        northcount += 1
                if northcount == 6:  # clear yellow pipe
                    for distinct1 in copyList:
                        if distinct1.direction == 'n':
                            ListOfUsedEnginneringStuff.remove(distinct1)
                            ListOfEnginnerOverlays.append(distinct1)
                            distinct1.visible = False
                            costume(distinct1, center(load_image('Game Data/Buttons/enginener circle.png')))
                    lives -= 1
                    cl.send(str(['TO MY PARTNER', 'My Lives', lives]).encode(FORMAT))
                    try:
                        costume(DamageMeter, eval(f"DamageMeterPic{lives}"))
                    except NameError:
                        cl.send(str(['TO MY PARTNER', 'You Win']).encode(FORMAT))
                        costume(GameOver, load_gif('Game Data/Gifs/you lose.gif'))
                        GameOver.visible = True

                eastcount = 0
                copyList = ListOfUsedEnginneringStuff.copy()
                for overlay in copyList:  # check for full pipes
                    if overlay.direction == 'e':
                        eastcount += 1
                if eastcount == 6:  # clear yellow pipe
                    for distinct1 in copyList:
                        if distinct1.direction == 'e':
                            ListOfUsedEnginneringStuff.remove(distinct1)
                            ListOfEnginnerOverlays.append(distinct1)
                            distinct1.visible = False
                            costume(distinct1, center(load_image('Game Data/Buttons/enginener circle.png')))
                    lives -= 1
                    cl.send(str(['TO MY PARTNER', 'My Lives', lives]).encode(FORMAT))
                    try:
                        costume(DamageMeter, eval(f"DamageMeterPic{lives}"))
                    except NameError:
                        cl.send(str(['TO MY PARTNER', 'You Win']).encode(FORMAT))
                        costume(GameOver, load_gif('Game Data/Gifs/you lose.gif'))
                        GameOver.visible = True

                southcount = 0
                copyList = ListOfUsedEnginneringStuff.copy()
                for overlay in copyList:  # check for full pipes
                    if overlay.direction == 's':
                        southcount += 1
                if southcount == 6:  # clear yellow pipe
                    for distinct1 in copyList:
                        if distinct1.direction == 's':
                            ListOfUsedEnginneringStuff.remove(distinct1)
                            ListOfEnginnerOverlays.append(distinct1)
                            distinct1.visible = False
                            costume(distinct1, center(load_image('Game Data/Buttons/enginener circle.png')))
                    lives -= 1
                    cl.send(str(['TO MY PARTNER', 'My Lives', lives]).encode(FORMAT))
                    try:
                        costume(DamageMeter, eval(f"DamageMeterPic{lives}"))
                    except NameError:
                        cl.send(str(['TO MY PARTNER', 'You Win']).encode(FORMAT))
                        costume(GameOver, load_gif('Game Data/Gifs/you lose.gif'))
                        GameOver.visible = True


                radioactivecount = 0
                copyList = ListOfUsedEnginneringStuff.copy()
                for overlay in copyList:  # check for full pipes
                    if overlay.kind == 'r':
                        radioactivecount += 1
                if radioactivecount == 6:  # clear yellow pipe
                    for distinct1 in copyList:
                        if distinct1.kind == 'r':
                            ListOfUsedEnginneringStuff.remove(distinct1)
                            ListOfEnginnerOverlays.append(distinct1)
                            distinct1.visible = False
                            costume(distinct1, center(load_image('Game Data/Buttons/enginener circle.png')))
                    lives -= 1
                    cl.send(str(['TO MY PARTNER', 'My Lives', lives]).encode(FORMAT))
                    try:
                        costume(DamageMeter, eval(f"DamageMeterPic{lives}"))
                    except NameError:
                        cl.send(str(['TO MY PARTNER', 'You Win']).encode(FORMAT))
                        costume(GameOver, load_gif('Game Data/Gifs/you lose.gif'))
                        GameOver.visible = True

                yellowcount = 0
                orangecount = 0
                graycount = 0
                copyList = ListOfUsedEnginneringStuff.copy()
                for overlay in ListOfUsedEnginneringStuff:#check for full pipes
                    if overlay.pipe == 'y':
                        yellowcount += 1
                    elif overlay.pipe == 'o':
                        orangecount += 1
                    elif overlay.pipe == 'g':
                        graycount += 1
                if yellowcount == 4:#clear yellow pipe
                    for distinct1 in copyList:
                        if distinct1.pipe == 'y':
                            playsound(load_sound('Game Data/Sound Effects/Pipe cleared.wav'))
                            ListOfUsedEnginneringStuff.remove(distinct1)
                            ListOfEnginnerOverlays.append(distinct1)
                            distinct1.visible = False
                            costume(distinct1, center(load_image('Game Data/Buttons/enginener circle.png')))
                if graycount == 4:#clear gray pipe
                    for distinct2 in copyList:
                        if distinct2.pipe == 'g':
                            playsound(load_sound('Game Data/Sound Effects/Pipe cleared.wav'))
                            ListOfUsedEnginneringStuff.remove(distinct2)
                            ListOfEnginnerOverlays.append(distinct2)
                            distinct2.visible = False
                            costume(distinct2, center(load_image('Game Data/Buttons/enginener circle.png')))
                if orangecount == 4:#clear orange pipe
                    for distinct3 in copyList:
                        if distinct3.pipe == 'o':
                            playsound(load_sound('Game Data/Sound Effects/Pipe cleared.wav'))
                            ListOfUsedEnginneringStuff.remove(distinct3)
                            ListOfEnginnerOverlays.append(distinct3)
                            distinct3.visible = False
                            costume(distinct3, center(load_image('Game Data/Buttons/enginener circle.png')))

            Submarine.x = (84 * (window.width / 1280) + (47 * (window.width / 1280) * position[0])) - 47 * (window.width / 1280)
            Submarine.y = (651 * (window.height / 720) - (30 * (window.height / 720) * position[1])) + 30 * (window.height / 720)
            Submarine.scale_x = Dir
            yourTrail.append(sprite)
            coordsITraveledSo.append(prepositoin)
            for overlay in ListOfPowerUpsOverlay:
                if overlay.name == chargeCommand:
                    overlay.charge += 1
                    try:
                        costume(ListOfPowerUps[ListOfPowerUpsOverlay.index(overlay)], eval(f"Pic{overlay.max}_piece_{overlay.charge}_glow"))
                    except NameError:
                        playsound(load_sound('Game Data/Sound Effects/This utility is fully charged.wav'))
                        overlay.charge -= 1
                        position = prepositoin.copy()
                        Submarine.x = (84 * (window.width / 1280) + (47 * (window.width / 1280) * position[0])) - 47 * (window.width / 1280)
                        Submarine.y = (651 * (window.height / 720) - (30 * (window.height / 720) * position[1])) + 30 * (window.height / 720)
                        yourTrail.pop()
                        return



            costume(CommitButton, CommitButtonPic2)
            my_turn = False
            playsound(load_sound('Game Data/Sound Effects/button press.wav'))
            cl.send(str(['TO MY PARTNER', 'My Turn Done', directionCommand]).encode(FORMAT))
            chargeCommand = ''
            directionCommand = ''
            costume(WhooseTurn, notYourTurnPic)
            pyglet.clock.schedule_once(put_back_up, 1)
            commands = ''
            CommandsLabel.text = ''
            deepDiveOn = False
            enemySubmarine.visible = False
            enginnerglow.visible = False
            enginnerCommand = ''
            for glow in ListOfGlows:
                glow.visible = False
            for base in bases:
                if base == position:
                    lives = 4
                    lose_lives('I Can Put whatever I want in here as long as I put Something in.')
                    cl.send(str(['TO MY PARTNER', 'My Lives', lives]).encode(FORMAT))
                    basesSprites.pop(bases.index(base))
                    bases.remove(base)
                    playsound(load_sound('Game Data/Sound Effects/Hospital base.wav'))

            if sheilds > 0:
                sheilds -= 1
                if sheilds == 0:
                    costume(Submarine, center(load_image('Game Data/Captain Board/Captian Submarine.png')))

        if math.dist((x, y), (830*(window.width/1280), 627*(window.height/720))) < 40*(window.height/720):
            playsound(load_sound('Game Data/Sound Effects/Sonar ping 2.wav'))
            chargeCommand = ''
            directionCommand = ''
            commands = ''
            CommandsLabel.text = ''
        if chargeCommand == '':
            for overlay in ListOfPowerUpsOverlay:
                if (math.dist((x, y), (overlay.x, overlay.y)) < 40 * (window.height / 720)):
                    if switch_on_charge:
                        Commands = list(commands)
                        Commands.append(f"-{overlay.name}")
                        commands = ''.join(Commands)
                        chargeCommand = overlay.name
                    else:# they are trying to use a first mate thing
                        if overlay.charge == overlay.max:
                            if overlay.name == 't':
                                if usingEnginnering:
                                    copyList = ListOfUsedEnginneringStuff.copy()
                                    for OVERLAY in copyList:
                                        if OVERLAY.kind == 'w':
                                            playsound(load_sound(
                                                'Game Data/Sound Effects/You cannot use this utility until you clear engineering board.wav'))
                                            return
                                utility_being_used = True
                                playsound(load_sound('Game Data/Sound Effects/torpedo sound.wav'))
                                torpedo.visible = True
                                torpedoPosition = position.copy()
                                torpedo.x = Submarine.x
                                torpedo.y = Submarine.y
                                ListOfPowerUpsOverlay[0].charge = 0
                                costume(Torpedo_Charge, eval(f"Pic{overlay.max}_piece_0_glow"))
                            if overlay.name == 'm':
                                if usingEnginnering:
                                    copyList = ListOfUsedEnginneringStuff.copy()
                                    for OVERLAY in copyList:
                                        if OVERLAY.kind == 'w':
                                            playsound(load_sound(
                                                'Game Data/Sound Effects/You cannot use this utility until you clear engineering board.wav'))
                                            return
                                utility_being_used = True
                                ListOfPowerUpsOverlay[1].charge = 0
                                costume(Mine_Charge, eval(f"Pic{overlay.max}_piece_0_glow"))
                                if mine_switch.on == 'sweep':
                                    print('hohohoh')
                                    mineSweeperOn = True
                                    if len(ListOfEnemyMines) == 0:
                                        utility_being_used = False
                                        return
                                    utility_being_used = False
                                    return
                                new_mine = correctSprite(pyglet.sprite.Sprite(minePic))
                                playsound(load_sound('Game Data/Sound Effects/button press.wav'))
                                new_mine.x = Submarine.x
                                new_mine.y = Submarine.y
                                new_mine.Position = position.copy()
                                new_mine.disabled = False
                                placingMine = True
                                ListOfMines.append(new_mine)
                            if overlay.name == 'dd':
                                if usingEnginnering:
                                    copyList = ListOfUsedEnginneringStuff.copy()
                                    for OVERLAY in copyList:
                                        if OVERLAY.kind == 'u':
                                            playsound(load_sound(
                                                'Game Data/Sound Effects/You cannot use this utility until you clear engineering board.wav'))
                                            return
                                ListOfPowerUpsOverlay[8].charge = 0
                                costume(DeepDive_Charge, eval(f"Pic{overlay.max}_piece_0_glow"))
                                deepDiveOn = True
                                playsound(load_sound('Game Data/Sound Effects/Deep dive.wav'))
                            if overlay.name == 'sh':
                                if usingEnginnering:
                                    copyList = ListOfUsedEnginneringStuff.copy()
                                    for OVERLAY in copyList:
                                        if OVERLAY.kind == 'u':
                                            playsound(load_sound(
                                                'Game Data/Sound Effects/You cannot use this utility until you clear engineering board.wav'))
                                            return
                                sheilds = 4#It ends up being the same result as 3
                                ListOfPowerUpsOverlay[7].charge = 0
                                costume(Shield_Charge, eval(f"Pic{overlay.max}_piece_0_glow"))
                                costume(Submarine, center(load_image('Game Data/Captain Board/Shield Submarine.png')))
                                playsound(load_sound('Game Data/Sound Effects/Shield sound effect.wav'))
                            if overlay.name == 'a':
                                if usingEnginnering:
                                    copyList = ListOfUsedEnginneringStuff.copy()
                                    for OVERLAY in copyList:
                                        if OVERLAY.kind == 'w':
                                            playsound(load_sound('Game Data/Sound Effects/You cannot use this utility until you clear engineering board.wav'))
                                            return
                                utility_being_used = True
                                bomber.visible = True
                                bomber.Position = position.copy()
                                bomber.position = Submarine.position
                                ListOfPowerUpsOverlay[2].charge = 0
                                costume(AirStrike_Charge, eval(f"Pic{overlay.max}_piece_0_glow"))
                                playsound(load_sound('Game Data/Sound Effects/Airplane sound.wav'))
                            if overlay.name == 'r':
                                if usingEnginnering:
                                    copyList = ListOfUsedEnginneringStuff.copy()
                                    for OVERLAY in copyList:
                                        if OVERLAY.kind == 's':
                                            playsound(load_sound(
                                                'Game Data/Sound Effects/You cannot use this utility until you clear engineering board.wav'))
                                            return
                                ListOfPowerUpsOverlay[5].charge = 0
                                costume(Recon_Charge, eval(f"Pic{overlay.max}_piece_0_glow"))
                                cl.send(str(['TO MY PARTNER', 'Give Me Mines']).encode(FORMAT))
                                playsound(load_sound('Game Data/Sound Effects/Recon sound effect.wav'))
                            if overlay.name == 'd':
                                if usingEnginnering:
                                    copyList = ListOfUsedEnginneringStuff.copy()
                                    for OVERLAY in copyList:
                                        if OVERLAY.kind == 's':
                                            playsound(load_sound(
                                                'Game Data/Sound Effects/You cannot use this utility until you clear engineering board.wav'))
                                            return
                                utility_being_used = True
                                drone.visible = True
                                drone.Position = position.copy()
                                drone.position = Submarine.position
                                ListOfPowerUpsOverlay[3].charge = 0
                                costume(Drone_Charge, eval(f"Pic{overlay.max}_piece_0_glow"))
                                playsound(load_sound('Game Data/Sound Effects/torpedo sound.wav'))
                            if overlay.name == 'si':
                                if usingEnginnering:
                                    copyList = ListOfUsedEnginneringStuff.copy()
                                    for OVERLAY in copyList:
                                        if OVERLAY.kind == 'u':
                                            playsound(load_sound(
                                                'Game Data/Sound Effects/You cannot use this utility until you clear engineering board.wav'))
                                            return
                                utility_being_used = True
                                ListOfPowerUpsOverlay[6].charge = 0
                                costume(Silence_Charge, eval(f"Pic{overlay.max}_piece_0_glow"))
                                silenceTarget.Position = position.copy()
                                silenceTarget.position = Submarine.position
                                silenceTarget.visible = True
                            if overlay.name == 'so':
                                if usingEnginnering:
                                    copyList = ListOfUsedEnginneringStuff.copy()
                                    for OVERLAY in copyList:
                                        if OVERLAY.kind == 's':
                                            playsound(load_sound(
                                                'Game Data/Sound Effects/You cannot use this utility until you clear engineering board.wav'))
                                            return
                                if not SonarIsSetOnSheilds:
                                    ListOfPowerUpsOverlay[4].charge = 0
                                    costume(Sonar_Charge, eval(f"Pic{overlay.max}_piece_0_glow"))
                                    cl.send(str(['TO MY PARTNER', 'Sonar Played']).encode(FORMAT))
                                else:
                                    ListOfPowerUpsOverlay[4].charge = 0
                                    costume(Sonar_Charge, eval(f"Pic{overlay.max}_piece_0_glow"))
                                    cl.send(str(['TO MY PARTNER', 'Tell me your sheild']).encode(FORMAT))



        if directionCommand not in ['n', 's', 'e', 'w']:
            if math.dist((x, y), (121 * (window.width / 1280), 197 * (window.height / 720))) < 28 * (window.height / 720):
                Commands = list(commands)
                Commands.append('-W')
                commands = ''.join(Commands)
                directionCommand = 'w'

            if math.dist((x, y), (345*(window.width/1280), 196*(window.height/720))) < 28*(window.height/720):
                Commands = list(commands)
                Commands.append('-N')
                commands = ''.join(Commands)
                directionCommand = 'n'

            if math.dist((x, y), (562*(window.width/1280), 196*(window.height/720))) < 28*(window.height/720):
                Commands = list(commands)
                Commands.append('-S')
                commands = ''.join(Commands)
                directionCommand = 's'

            if math.dist((x, y), (773*(window.width/1280), 197*(window.height/720))) < 28*(window.height/720):
                Commands = list(commands)
                Commands.append('-E')
                commands = ''.join(Commands)
                directionCommand = 'e'

        CommandsLabel.text = commands
switch_on_charge = True

@window.event
def on_mouse_motion(x, y, dx, dy):
    if Scene == 'playing' and my_turn:
        if math.dist((x, y), (121*(window.width/1280), 197*(window.height/720))) < 28*(window.height/720):
            westglow.visible = True
        else:
            westglow.visible = False
        if math.dist((x, y), (345*(window.width/1280), 196*(window.height/720))) < 28*(window.height/720):
            northglow.visible = True
        else:
            northglow.visible = False
        if math.dist((x, y), (562*(window.width/1280), 196*(window.height / 720))) < 28*(window.height / 720):
            southglow.visible = True
        else:
            southglow.visible = False
        if math.dist((x, y), (773*(window.width/1280), 197*(window.height/720))) < 28*(window.height/720):
            eastglow.visible = True
        else:
            eastglow.visible = False
        for overlay in ListOfPowerUpsOverlay:
            if math.dist((x, y), (overlay.x, overlay.y)) < 40*(window.height/720):
                overlay.visible = True
            else:
                overlay.visible = False
        if usingEnginnering:
            for overlay in ListOfEnginnerOverlays:
                if math.dist((x, y), (overlay.x, overlay.y)) < 20*(window.height/720):
                    overlay.visible = True
                else:
                    overlay.visible = False

my_turn = False
I_made_this_game = False

def ask_for_position(dt):#sourcery skip
    global Scene, islands, my_turn
    enemyRedDot.visible = True
    playsound(load_sound('Game Data/Sound Effects/welcome select your position.wav'))
    Scene = 'Select'
    CommandsLabel.visible = True
    costume(GifBox, load_gif('Game Data/Gifs/Type Position.gif'))
    GifBox.visible = True
    GifBox.y = -1*(window.width/1280)
    GifBox.x = 2*(window.height/720)
    GifBox.scale_x *= 1.06
    GifBox.scale_y *= 1.07
    Input_text.visible = True
    if I_made_this_game:
        my_turn = False
        file = open(f'Game Data/game boards/Real Maps/{ShowMapPics[ShowMapIndex].title}.txt')
        first_list = file.read().split('/')
        file.close()

        with suppress(FileNotFoundError):
            basefile = open(f'Game Data/game boards/Real Maps/{ShowMapPics[ShowMapIndex].title}.base')
            data = basefile.read().split('/')
            for info in data:
                x, y = info.split(',')
                X = int(x)
                Y = int(y)
                bases.append([int(x), int(y)])
                baseSprite = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Captain Board/repair base.png'))))
                baseSprite.x = (84 * (window.width / 1280) + (47 * (window.width / 1280) * X)) - 47 * (window.width / 1280)
                baseSprite.y = (651 * (window.height / 720) - (30 * (window.height / 720) * Y)) + 30 * (window.height / 720)
                baseSprite.Position = (X, Y)
                basesSprites.append(baseSprite)

            basefile.close()

        for text in first_list:
            x, y = text.split(',')
            islands.append([int(x), int(y)])
    else:
        my_turn = True
        for index in range(len(rooms)):
            if rooms[index][1] == ChoiceText.text:
                file = open(f'Game Data/game boards/Real Maps/{rooms[index][0]}.txt')
                first_list = file.read().split('/')
                file.close()
                with suppress(FileNotFoundError):
                    basefile = open(f'Game Data/game boards/Real Maps/{rooms[index][0]}.base')
                    data = basefile.read().split('/')
                    for info in data:
                        x, y = info.split(',')
                        X = int(x)
                        Y = int(y)
                        bases.append([int(x), int(y)])
                        baseSprite = correctSprite(
                            pyglet.sprite.Sprite(center(load_image('Game Data/Captain Board/repair base.png'))))
                        baseSprite.x = (84 * (window.width / 1280) + (47 * (window.width / 1280) * X)) - 47 * (window.width / 1280)
                        baseSprite.y = (651 * (window.height / 720) - (30 * (window.height / 720) * Y)) + 30 * (window.height / 720)
                        baseSprite.Position = (X, Y)
                        basesSprites.append(baseSprite)
                    basefile.close()
                for text in first_list:
                    x, y = text.split(',')
                    islands.append([int(x), int(y)])

def this_inot_that_special(dt):
    global enemydirection, navagatorStartLineHere
    costume(SurfaceButton, SurfaceUnderWaterPic)
    costume(WhooseTurn, yourTurnPic)
    if enemydirection == 'n':
        sprite = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Navagator Stuff/navYline.png')), x=navagatorStartLineHere[0], y=navagatorStartLineHere[1] + (11 * (window.height / 720))))
        navagatorStartLineHere = [navagatorStartLineHere[0], navagatorStartLineHere[1]+(22*(window.height/720))]
        enemyTrail.append(sprite)
    if enemydirection == 's':
        sprite = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Navagator Stuff/navYline.png')), x=navagatorStartLineHere[0], y=navagatorStartLineHere[1] - (11 * (window.height / 720))))
        navagatorStartLineHere = [navagatorStartLineHere[0], navagatorStartLineHere[1] - (22 * (window.height / 720))]
        enemyTrail.append(sprite)
    if enemydirection == 'w':
        sprite = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Navagator Stuff/navXline.png')), x=navagatorStartLineHere[0] - (11 * (window.width / 1280)), y=navagatorStartLineHere[1]))
        navagatorStartLineHere = [navagatorStartLineHere[0] - (22 * (window.height / 720)), navagatorStartLineHere[1]]
        enemyTrail.append(sprite)
    if enemydirection == 'e':
        sprite = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Navagator Stuff/navXline.png')), x=navagatorStartLineHere[0] + (11 * (window.width / 1280)), y=navagatorStartLineHere[1]))
        navagatorStartLineHere = [navagatorStartLineHere[0] + (22 * (window.height / 720)), navagatorStartLineHere[1]]
        enemyTrail.append(sprite)
    if enemydirection == 'surfaced':
        pop_up(load_image('Game Data/Pop ups/enemy surfaced.png'))
    if enemydirection == 'used silence':
        enemyTrail.clear()
    enemyRedDot.x = navagatorStartLineHere[0]
    enemyRedDot.y = navagatorStartLineHere[1]

navagatorStartLineHere = [1089*(window.width/1280), 524*(window.height/720)]
enemydirection = 'n'

def you_win(dt):
    costume(GameOver, load_gif('Game Data/Gifs/you win.gif'))
    if I_made_this_game:
        cl.send(str({'winner': my_name_Label.text, 'creator': my_name_Label.text, 'joiner': litte_enemy_name_Label.text, 'date': f'{datetime.date.today().month}~{datetime.date.today().day}~{datetime.date.today().year}', 'board': ShowMapPics[ShowMapIndex].title, 'engineering': enginneringSwitch.on}).encode(FORMAT))
    else:
        for index in range(len(rooms)):
            if rooms[index][1] == ChoiceText.text:
                cl.send(str({'winner': my_name_Label.text, 'creator': litte_enemy_name_Label.text,
                             'joiner': my_name_Label.text,
                             'date': f'{datetime.date.today().month}~{datetime.date.today().day}~{datetime.date.today().year}',
                             'board': rooms[index][0], 'engineering': rooms[index][4]}).encode(FORMAT))
    GameOver.visible = True

def lose_lives(dt):
    try:
        costume(DamageMeter, eval(f"DamageMeterPic{lives}"))
    except NameError:
        cl.send(str(['TO MY PARTNER', 'You Win']).encode(FORMAT))
        costume(GameOver, load_gif('Game Data/Gifs/you lose.gif'))
        GameOver.visible = True

def make_mines_for_recon(dt):
    for position in ListOfEnemyMinePositions:
        mine = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Captain Board/Enemy mine.png'))))
        mine.Position = position
        mine.x = (84 * (window.width / 1280) + (47 * (window.width / 1280) * position[0])) - 47 * (window.width / 1280)
        mine.y = (651 * (window.height / 720) - (30 * (window.height / 720) * position[1])) + 30 * (window.height / 720)
        ListOfEnemyMines.append(mine)

def socketUpdate():
    global rooms, Scene, my_turn, enemydirection, lives, TimeLeftUntilPlayBegins, directionCommand, ListOfEnemyMines, ListOfEnemyMinePositions, games
    while True:
        try:
            Message = eval(cl.recv(29999).decode(FORMAT))
        except TypeError:
            print('ERROR\n'*12)
            print(f"this is your message you received: {Message}")
        if Message[0] == 'Your Rooms':
            rooms = Message[1].copy()
        if Message[0] == 'Game Started':
            GifBox.visible = False
            Scene = 'playing'
            def function(dt):
                cl.send(str(['TO MY PARTNER', 'My Name', my_name_Label.text]).encode(FORMAT))
            pyglet.clock.schedule_once(function, 1)
        if Message[0] == 'Your Stats':
            Games = Message[1].split('-')
            games.clear()
            for Game in Games:
                games.append(eval(Game))

        if Message[0] == 'FROM YOUR PARTNER':
            if Message[1] == 'Mine Disabled':
                for mine in ListOfMines:
                    if mine.Position == Message[2]:
                        mine.disabled = True
            if Message[1] == 'My Sheild':
                if Message[2]:
                    pop_up(load_image('Game Data/Pop ups/enemy shield is on.png'))
                else:
                    pop_up(load_image('Game Data/Pop ups/enemy shield is off.png'))
            if Message[1] == 'Tell me your sheild':
                if sheilds == 0:
                    cl.send(str(['TO MY PARTNER', 'My Sheild', False]).encode(FORMAT))
                else:
                    cl.send(str(['TO MY PARTNER', 'My Sheild', True]).encode(FORMAT))
            if Message[1] == 'My Name':
                def function(dt):litte_enemy_name_Label.text = Message[2]
                pyglet.clock.schedule_once(function, 1.0/100)
                litte_enemy_name_Label.visible = True
                if not I_made_this_game:
                    cl.send(str(['TO MY PARTNER', 'My Name', my_name_Label.text]).encode(FORMAT))
            if Message[1] == 'Found Ya' and tell_if_drone_found_me:
                pop_up(load_image('Game Data/Pop ups/location detected.png'))
            if Message[1] == 'Played Mine':
                pop_up(load_image('Game Data/Pop ups/enemy mine deployed.png'))
            if Message[1] == 'My Utilitys':
                enemysUtilitys = Message[2].copy()
                for utility in enemysUtilitys:
                    ListOfGlows[utility].visible = True
            if Message[1] == 'Sonar Played':
                msg = []
                for overlay in ListOfPowerUpsOverlay:
                    if overlay.charge == overlay.max:
                        msg.append(ListOfPowerUpsOverlay.index(overlay))
                cl.send(str(['TO MY PARTNER', 'My Utilitys', msg]).encode(FORMAT))
            if Message[1] == 'My Position':
                SubmarinePosition = Message[2]
                if (drone.Position == SubmarinePosition) or (drone.Position[0] == SubmarinePosition[0] and abs(drone.Position[1]-SubmarinePosition[1]) == 1) or (drone.Position[1] == SubmarinePosition[1] and abs(drone.Position[0]-SubmarinePosition[0]) == 1) or (abs(drone.Position[0]-SubmarinePosition[0]) == 1 and abs(drone.Position[1]-SubmarinePosition[1]) == 1):
                    cl.send(str(['TO MY PARTNER', 'Found Ya']).encode(FORMAT))
                    enemySubmarine.x = (84 * (window.width / 1280) + (47 * (window.width / 1280) * SubmarinePosition[0])) - 47 * (window.width / 1280)
                    enemySubmarine.y = (651 * (window.height / 720) - (30 * (window.height / 720) * SubmarinePosition[1])) + 30 * (window.height / 720)
                    enemySubmarine.visible = True
            if Message[1] == 'Drone Scan':
                cl.send(str(['TO MY PARTNER', 'My Position', position]).encode(FORMAT))
            if Message[1] == 'Your Mines You asked for':
                ListOfEnemyMinePositions = Message[2].copy()
                pyglet.clock.schedule_once(make_mines_for_recon, 1 / 100)
            if Message[1] == 'Give Me Mines':
                MinePositions = []
                for mine in ListOfMines:
                    MinePositions.append(mine.Position)
                cl.send(str(['TO MY PARTNER', 'Your Mines You asked for', MinePositions]).encode(FORMAT))
            if Message[1] == 'You Win':
                pyglet.clock.schedule_once(you_win, 1/100)
            if Message[1] == 'EXPLOSION':
                explosionPosition = Message[2]
                if Message[3] == 'mine':
                    for mine in ListOfEnemyMines:
                        if mine.Position == Message[2]:
                            ListOfEnemyMines.remove(mine)
                if tell_what_hit_me:
                    if Message[3] == 'mine':
                        pop_up(load_image('Game Data/Pop ups/mine attack.png'))
                    if Message[3] == 'bomber':
                        pop_up(load_image('Game Data/Pop ups/airstrike.png'))
                    if Message[3] == 'torpedo':
                        pop_up(load_image('Game Data/Pop ups/torpedo attack.png'))

                if not my_turn:
                    cl.send(str(['TO MY PARTNER', 'EXPLOSION', explosionPosition, Message[3]]).encode(FORMAT))
                    explosion.x = (84 * (window.width / 1280) + (47 * (window.width / 1280) * explosionPosition[0])) - 47 * (window.width / 1280)-(50*(window.width/1280))
                    explosion.y = (651 * (window.height / 720) - (30 * (window.height / 720) * explosionPosition[1])) + 30 * (window.height / 720)-(50*(window.height/720))
                    explosion.visible = True
                    playsound(load_sound('Game Data/Sound Effects/explosion.wav'))
                    pyglet.clock.schedule_once(cancel_explosion, 1.333)
                if sheilds == 0:
                    if explosionPosition == position:
                        lives -= 2
                        pyglet.clock.schedule_once(lose_lives, 1/100)
                    else:
                        if explosionPosition[0] == position[0]:
                            if abs(explosionPosition[1]-position[1]) == 1:
                                lives -= 1
                                pyglet.clock.schedule_once(lose_lives, 1 / 100)
                        elif explosionPosition[1] == position[1]:
                            if abs(explosionPosition[0]-position[0]) == 1:
                                lives -= 1
                                pyglet.clock.schedule_once(lose_lives, 1 / 100)
                        elif (abs(explosionPosition[0] - position[0]) == 1) and (abs(explosionPosition[1] - position[1]) == 1):
                            lives -= 1
                            pyglet.clock.schedule_once(lose_lives, 1 / 100)
                cl.send(str(['TO MY PARTNER', 'My Lives', lives]).encode(FORMAT))
            if Message[1] == 'My Lives':
                enemyLives = Message[2]
                def function(dt):
                    with suppress(FileNotFoundError):
                        costume(enemyDamageMeter, load_image(f"Game Data/Damage meters/Opponent Damage meter {enemyLives}.png"))
                pyglet.clock.schedule_once(function, 1/100)

            if Message[1] == 'My Turn Done':
                if TimeLeftUntilPlayBegins < 1:
                    enemydirection = Message[2]
                    playsound(load_sound('Game Data/Sound Effects/Sonar ping 3.wav'))
                    my_turn = True
                    pyglet.clock.schedule_once(this_inot_that_special, 1 / 100)
                else:
                    enemydirection = Message[2]
                    TimeLeftUntilPlayBegins -= 1
                    cl.send(str(['TO MY PARTNER', 'My Turn Done', directionCommand]).encode(FORMAT))
                    for glow in ListOfGlows:
                        glow.visible = False
                    chargeCommand = ''
                    directionCommand = ''
                    commands = ''
                    CommandsLabel.text = ''
                    deepDiveOn = False
                    pyglet.clock.schedule_once(fuction_for_surfaced_for_socket_update_as_threading_can_not_meddle_with_pyglet_stuff, 1/100)


def fuction_for_surfaced_for_socket_update_as_threading_can_not_meddle_with_pyglet_stuff(dt):
    global sheilds, navagatorStartLineHere
    costume(SurfaceButton, SurfaceAboveWaterPic)
    costume(WhooseTurn, notYourTurnPic)
    if enemydirection == 'n':
        sprite = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Navagator Stuff/navYline.png')), x=navagatorStartLineHere[0], y=navagatorStartLineHere[1] + (11 * (window.height / 720))))
        navagatorStartLineHere = [navagatorStartLineHere[0], navagatorStartLineHere[1]+(22*(window.height/720))]
        enemyTrail.append(sprite)
    if enemydirection == 's':
        sprite = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Navagator Stuff/navYline.png')), x=navagatorStartLineHere[0], y=navagatorStartLineHere[1] - (11 * (window.height / 720))))
        navagatorStartLineHere = [navagatorStartLineHere[0], navagatorStartLineHere[1] - (22 * (window.height / 720))]
        enemyTrail.append(sprite)
    if enemydirection == 'w':
        sprite = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Navagator Stuff/navXline.png')), x=navagatorStartLineHere[0] - (11 * (window.width / 1280)), y=navagatorStartLineHere[1]))
        navagatorStartLineHere = [navagatorStartLineHere[0] - (22 * (window.height / 720)), navagatorStartLineHere[1]]
        enemyTrail.append(sprite)
    if enemydirection == 'e':
        sprite = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Navagator Stuff/navXline.png')), x=navagatorStartLineHere[0] + (11 * (window.width / 1280)), y=navagatorStartLineHere[1]))
        navagatorStartLineHere = [navagatorStartLineHere[0] + (22 * (window.height / 720)), navagatorStartLineHere[1]]
        enemyTrail.append(sprite)
    if enemydirection == 'used silence':
        enemyTrail.clear()
    enemyRedDot.x = navagatorStartLineHere[0]
    enemyRedDot.y = navagatorStartLineHere[1]
    if sheilds > 0:
        sheilds -= 1
        if sheilds == 0:
            costume(Submarine, center(load_image('Game Data/Captain Board/Captian Submarine.png')))

def update(dt):
    global navagatorStartLineHere
    if Settings_panel.over and Settings_panel.x < -420 * (window.width / 1280):
        Settings_panel.x += 10 * (window.width / 1280)
        for option in Setting_options:
            option.x += 10 * (window.width / 1280)
    if not Settings_panel.over and Settings_panel.x > -870*(window.width/1280):
        Settings_panel.x -= 10 * (window.width / 1280)
        for option in Setting_options:
            option.x -= 10 * (window.width / 1280)
    speed = 1*(window.height/720)
    if uppressed:
        for line in enemyTrail:
            line.y += speed
        navagatorStartLineHere = [navagatorStartLineHere[0], navagatorStartLineHere[1] + speed]
    if downpressed:
        for line in enemyTrail:
            line.y -= speed
        navagatorStartLineHere = [navagatorStartLineHere[0], navagatorStartLineHere[1] - speed]
    if leftpressed:
        for line in enemyTrail:
            line.x -= speed
        navagatorStartLineHere = [navagatorStartLineHere[0] - speed, navagatorStartLineHere[1]]
    if rightpressed:
        for line in enemyTrail:
            line.x += speed
        navagatorStartLineHere = [navagatorStartLineHere[0] + speed , navagatorStartLineHere[1]]
    enemyRedDot.x = navagatorStartLineHere[0]
    enemyRedDot.y = navagatorStartLineHere[1]

def the_first_pyglet_updater(dt):
        global backgroundPlayer
        if login_switch.on:
            if perscope.y > 0:
                perscope.y -= perscope.speed
            else:
                if my_name_Label.opacity < 255:
                    my_name_Label.opacity += 5
        else:
            if my_name_Label.opacity > 0:
                my_name_Label.opacity -= 5
                return
            if perscope.y < perscope.up:
                perscope.y += perscope.speed
        if Scene != 'playing' and backgroundPlayer.playing == False:
            backgroundPlayer.queue(backgroundSound)
            backgroundPlayer.play()
        if Scene == 'playing' and backgroundPlayer.playing:
            backgroundPlayer.pause()
            playsound(load_sound('Game Data/Sound Effects/big splash.wav'))
            pyglet.clock.schedule_once(ask_for_position, 3)
            pyglet.clock.unschedule(the_first_pyglet_updater)
            pyglet.clock.schedule_interval(update, 1.0 / 60)


T(target=socketUpdate).start()
pyglet.clock.schedule_interval(the_first_pyglet_updater, 1.0 / 60)
torpedo_overlay = correctSprite(pyglet.sprite.Sprite(center(load_image('Game Data/Buttons/Frist Mate Circle.png')), x=90, y=90))
pyglet.app.run()