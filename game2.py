import pygame

# from the math module (built into python), get the fabs method
from math import fabs, hypot

from random import randint
# import randint
pygame.init()

screen_size = (640,480)
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Bird Chase")
background_image = pygame.image.load('sky1.png')
bird_image2 = pygame.image.load('bird2.png')
bird_image = pygame.image.load('bird.png')
bee_image = pygame.image.load('bee.png')
fly_image = pygame.image.load('fly.png')
butterfly_image = pygame.image.load('butterfly.png')
pygame.mixer.music.load('song.mp3')
bird_image = bird_image2
bird = {
    "x":randint(25,440),
    "y":randint(25,600),
    "speed":5,
    "wins":0,
    "power":0
}
# font = pygame.font.FONT(none,25)
# wins_text = font.render("Wins: %d" % (hero['wins']), True, (0,0,0)
bee = {
    'x':randint(25,440),
    'y':randint(25,600),
    'speed':1,
    'dx':1,
    'dy':1
}
fly = {
    'x':randint(25, 440),
    'y':randint(25,600),
    'speed':2,
    'dx':1,
    'dy':1
}
butterfly = {
    'x':randint(25,440),
    'y':randint(25,600),
    'speed':2,
    'dx':1,
    'dy':1
}
keys = {
    "up":273,
    "down":274,
    "right":275,
    "left":276
}

keys_down = {
    "up":False,
    "down":False,
    "left":False,
    "right":False
}
def bird_on_screen():
    if bird['x'] <= 20:
        bird['x'] = 20;
    elif bird['x'] > 640:
        bird['x'] = 640;
    if bird['y'] < 0:
        bird['y'] = 0;
    elif bird['y'] > 480:
        bird['y'] = 480
def bee_on_screen():
    if bee['x'] <= 20:
        bee['x'] = 20;
    elif bird['x'] > 620:
        bee['x'] = 620;
    if bee['y'] < 20:
        bee['y'] = 20;
    elif bee['y'] > 440:
        bee['y'] = 440
def fly_on_screen():
    if fly['x'] <= 20:
        fly['x'] = 20;
    elif fly['x'] > 620:
        fly['x'] = 620;
    if fly['y'] < 20:
        fly['y'] = 20;
    elif fly['y'] > 440:
        fly['y'] = 440

def butterfly_on_screen():
    if butterfly['x'] <= 40:
        butterfly['x'] = 40;
    elif butterfly['x'] > 620:
        butterfly['x'] = 620;
    if butterfly['y'] < 40:
        butterfly['y'] = 40;
    elif butterfly['y'] > 620:
        butterfly['y'] = 620



bird_alive = True
game_on = True
bee_movementX = True;
bee_movementY = True;
butterfly_movementX = False;
butterfly_movementY = False;
fly_power_up = True;
fly_returns_to_map = True
butterfly_power_up = True;
butterfly_returns_to_map = True;
tick = 0
pygame.mixer.music.play(-1)
while game_on:
    
    bird_on_screen();
    fly_on_screen();
    bee_on_screen();
    butterfly_on_screen();
    tick += 1
   



    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            # user clicked red x in corner
            game_on = False
        elif event.type == pygame.KEYDOWN:
            if event.key == keys['up']:
                keys_down['up'] = True
            elif event.key == keys['down']:
                keys_down['down'] = True
            elif event.key == keys['left']:
                keys_down['left'] = True
            elif event.key == keys['right']:
                keys_down['right'] = True
                    # blit takes 2 arguments what and where
        elif event.type == pygame.KEYUP:
            if event.key == keys['up']:
                keys_down['up'] = False
            elif event.key == keys['down']:
                keys_down['down'] = False
            elif event.key == keys['left']:
                keys_down['left'] = False
            elif event.key == keys['right']:
                keys_down['right'] = False




    if bird_alive:
        if keys_down['up']:
            bird['y'] -= bird['speed']
        # bee['y'] += bee['speed']
        # fly['y']  -= bird['y']
        # butterfly['y'] += butterfly['speed']
        elif keys_down['down']:
            bird['y'] += bird['speed']
        # bee['x'] = bird['x']
        # fly['y'] += fly['speed']
        # butterfly['y'] -= butterfly['speed']
        elif keys_down['left']:
            bird['x'] -= bird['speed']
        # bee['x'] += bee['speed']
        # fly['x'] -= fly['speed']
        # butterfly['x'] += butterfly['speed']
        elif keys_down['right']:
            bird['x'] += bird['speed']
        # bee['x'] -= bee['speed']
        # fly['x'] += fly['speed']
        # butterfly['x'] -= butterfly['speed']
    
    dx = bee['x'] - bird['x']
    dy = bee['y'] - bird['y']
    dist = hypot(dx,dy)
        # print dist
    dx = dx / dist
    dy = dy / dist
        # print dx, dy
    bee['x'] -= dx * bee['speed']
    bee['y'] -= dy * bee['speed']

    if tick % 20 == 0:
        # change directions!
        butterfly['dx'] = randint(-1,1)
        butterfly['dy'] = randint(-1,1)

    butterfly['x'] += butterfly['dx'] * butterfly['speed']
    butterfly['y'] += butterfly['dy'] * butterfly['speed']


    # dx = butterfly['x'] - bird['x']
    # dy = butterfly['y'] - bird['y']
    # dist = hypot(dx,dy)
    #     # print dist
    # dx = dx / dist
    # dy = dy / dist
    #     # print dx, dy
    # butterfly['x'] -= dx * butterfly['speed']
    # butterfly['y'] -= dy * butterfly['speed']


    distance_bee = fabs(bird['x']-bee['x']) + fabs(bird['y']-bee['y'])
    distance_fly = fabs(bird['x']-fly['x']) + fabs(bird['y']-fly['y'])
    distance_butterfly = fabs(bird['x']-butterfly['x']) + fabs(bird['y']-butterfly['y'])
    distance_betweenHM = fabs(bird["x"] - fly["x"]) + fabs(bird["y"] - fly["y"]);
    distance_betweenHB = fabs(bird["x"] - butterfly["x"]) + fabs(bird["y"] - butterfly["y"]);
    if distance_fly< 32:
        # print "Collision"
        bird["power"] += 1
        if bird["power"] == 3:
            
            bird_image = pygame.transform.scale(bird_image, (72, 72))
        if bird["power"] == 6:
            bird_image = pygame.transform.scale(bird_image, (96, 96))
        if bird["power"] == 9:
            bird_image = pygame.transform.scale(bird_image, (128, 128))
    if distance_bee< 32:
        # print "Collision"
        bird["power"] = 0
        bird_image = pygame.transform.scale(bird_image, (32, 32))

    if distance_butterfly < 32:
        bird["power"] += 1
        if bird["power"] == 3:
            
            bird_image = pygame.transform.scale(bird_image, (72, 72))
        if bird["power"] == 6:
            bird_image = pygame.transform.scale(bird_image, (96, 96))
        if bird["power"] == 9:
            bird_image = pygame.transform.scale(bird_image, (128, 128))
    # if distance_butterfly < 64:
    #     print "Collision"
    # else:
    #     print "not touching"
    pygame_screen.blit(background_image,[0,0])
    pygame_screen.blit(bird_image, [bird['x'],bird['y']])
    pygame_screen.blit(bee_image, [bee['x'],bee['y']])
    pygame_screen.blit(fly_image, [fly['x'],fly['y']])
    pygame_screen.blit(butterfly_image, [butterfly['x'],butterfly['y']])
# -------------------------------
    if(fly_power_up == True):
    	pygame_screen.blit(fly_image, [fly["x"], fly["y"]]);
        if(distance_betweenHM<32):
    			pygame_screen.blit(fly_image, [-10, -10]);
    			bird["speed"] += 5;
    			# bee["speed"] -=1;
    			fly_power_up = False;
    			fly_returns_to_map = False;
    if(fly_returns_to_map == False):
    	fly["x"] = randint(10, 400);
    	fly["y"] = randint(10, 600);
    	pygame_screen.blit(fly_image, [fly["x"], fly["y"]]);
    	fly_returns_to_map = True;
    	fly_power_up = True;
    # if(butterfly_power_up == True):
    #     pygame_screen.blit(butterfly_image, [butterfly["x"], butterfly["y"]]);
    #     if(distance_betweenHB<32):
    #             pygame_screen.blit(butterfly_image, [-10, -10]);
    #             bird["speed"] += 5;
    #             # bee["speed"] -=1;
    #             butterfly_power_up = False;
    #             butterfly_returns_to_map = False;
    # if(butterfly_returns_to_map == False):
    #     butterfly["x"] = randint(10, 400);
    #     butterfly["y"] = randint(10, 600);
    #     pygame_screen.blit(butterfly_image, [butterfly["x"], butterfly["y"]]);
    #     butterfly_returns_to_map = True;
    #     butterfly_power_up = True;

    font = pygame.font.Font(None, 25)
    wins_text = font.render("Power: %d" % (bird['power']), True, (0,0,0))
    pygame_screen.blit(wins_text,[40,40])
# --------------------------------


    pygame.display.flip()
