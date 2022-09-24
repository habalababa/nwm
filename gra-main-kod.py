import pygame
import os
pygame.font.init()
pygame.mixer.init()
width, height = 900, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("graaaa")
hpfont = pygame.font.SysFont("comicsans", 20)
winfont = pygame.font.SysFont("comicsans", 100)
bckgrnd = (0, 153, 0)
brd = (255, 255, 255)
yellowcl = (255, 255, 0)
redcl = (255, 0, 0)
fps = 60
shiplng, shiphgt = 55, 40
spd = 5
bullspd = 10
bulllng, bullhgt = 10, 10
maxbull = 5
redhit = pygame.USEREVENT + 1
bluehit = pygame.USEREVENT + 2
bullethitsnd = pygame.mixer.Sound(os.path.join("gra", "gethitc.mp3"))
bulletshotsnd = pygame.mixer.Sound(os.path.join("gra", "shotc.mp3"))
winsnd = pygame.mixer.Sound(os.path.join("gra", "winningc.mp3"))

bullredjpg = pygame.image.load(os.path.join("gra", "bulred.png"))
bullred = pygame.transform.scale(bullredjpg, (bulllng, bullhgt))

bullbluejpg = pygame.image.load(os.path.join("gra", "bulblue.png"))
bullblue = pygame.transform.scale(bullbluejpg, (bulllng, bullhgt))

border = pygame.Rect(width//2 - 2.5, 0, 5, height)

redshipjpg = pygame.image.load(os.path.join("gra", "statek.png"))
redship = pygame.transform.rotate(pygame.transform.scale(redshipjpg, (shiplng, shiphgt)), 0)

blueshipjpg = pygame.image.load(os.path.join("gra", "statekgit.png"))
blueship = pygame.transform.rotate(pygame.transform.scale(blueshipjpg, (shiplng, shiphgt)), 180)

space = pygame.transform.scale(pygame.image.load(os.path.join("gra", "kosmos.png")), (width, height))

redbullets = []
bluebullets = []

def upd(red, blue, redbullets, bluebullets, redhp, bluehp):
    win.blit(space, (0,0))
    pygame.draw.rect(win, brd, border)
    redhptxt = hpfont.render("health: " + str(bluehp), 1, redcl)
    bluehptxt = hpfont.render("health: " + str(redhp), 1, redcl)
    win.blit(redhptxt, (10, 10))
    win.blit(bluehptxt, (width - bluehptxt.get_width() - 10, 10))
    win.blit(blueship, (blue.x, blue.y))
    win.blit(redship, (red.x, red.y))
    for bullet in bluebullets:
        pygame.draw.rect(win, redcl, bullet)
    for bullet in redbullets:
        pygame.draw.rect(win, yellowcl, bullet)
    pygame.display.update()
def redmoves(keysk, red):
    if keysk[pygame.K_a] and red.x - 8 + spd > 0:
        red.x -= spd
    if keysk[pygame.K_d] and red.x + spd + shiplng < border.x:
        red.x += spd
    if keysk[pygame.K_w] and red.y - 9 + spd > 0:
        red.y -= spd
    if keysk[pygame.K_s] and red.y - 1 + spd + shiphgt < height:
        red.y += spd
def bluemoves(keysk, blue):
    if keysk[pygame.K_LEFT] and blue.x - 13 + spd > border.x:
        blue.x -= spd
    if keysk[pygame.K_RIGHT] and blue.x + spd + shiplng - 5 < width:
        blue.x += spd
    if keysk[pygame.K_UP] and blue.y - 8 + spd > 0:
        blue.y -= spd
    if keysk[pygame.K_DOWN] and blue.y + shiphgt - 5 + spd < height:
        blue.y += spd
def handlebullets(bluebullets, redbullets, red, blue):
    for bullet in bluebullets:
        bullet.x += bullspd
        if blue.colliderect(bullet):
            pygame.event.post(pygame.event.Event(redhit))
            bluebullets.remove(bullet)
        elif bullet.x > width:
            bluebullets.remove(bullet)
    for bullet in redbullets:
        bullet.x -= bullspd
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(bluehit))
            redbullets.remove(bullet)
        elif bullet.x < 0:
            redbullets.remove(bullet)
def winneris(text):
    istxt = winfont.render(text, 1, brd)
    win.blit(istxt, (width//2 - istxt.get_width()//2, height//2 - istxt.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    red = pygame.Rect(50, 250, shiplng, shiphgt)
    blue = pygame.Rect(800, 250, shiplng, shiphgt)
    run = True
    clock = pygame.time.Clock()
    redhp = 10
    bluehp = 10
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(redbullets) < maxbull and redhp > 0 and bluehp > 0:
                    bullet = pygame.Rect(red.x + shiplng, red.y + shiphgt//2 - 2, 10, 5)
                    redbullets.append(bullet)
                    bulletshotsnd.play()
                if event.key == pygame.K_RCTRL and len(bluebullets) < maxbull and redhp > 0 and bluehp > 0:
                    bullet = pygame.Rect(blue.x, blue.y + shiphgt//2 - 2, 10, 5)
                    bluebullets.append(bullet)
                    bulletshotsnd.play()
            if event.type == redhit:
                redhp -= 1
                bullethitsnd.play()

            if event.type == bluehit:
                bluehp -= 1
                bullethitsnd.play()
        wintxt = ""
        if redhp == 0:
            wintxt = "red wins"
            winsnd.play()
        if bluehp == 0:
            wintxt = "blue wins"
            winsnd.play()
        if wintxt != "":
            winneris(wintxt)
            break


        keysk = pygame.key.get_pressed()
        redmoves(keysk, red)
        bluemoves(keysk, blue)
        handlebullets(redbullets, bluebullets, red, blue)
        upd(red, blue, redbullets, bluebullets, redhp, bluehp)

    main()
if __name__ == "__main__":
    main()