import pygame
import os

pygame.init()
pygame.display.set_caption('Blur Algorithm')
screen = pygame.display.set_mode((567, 320))
done = False
clock = pygame.time.Clock()

def get_image(path,size):
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    image = pygame.image.load(canonicalized_path)
    image = pygame.transform.scale(image, size)
    return image

def get_trans_surf(size):
    surf = pygame.Surface(size)
    surf.fill((0,0,0))
    surf.set_colorkey((0,0,0))
    return surf



surf = get_trans_surf((256,256))
surf.blit(get_image('cat_eye.png',(256,256)), (0,0))

def get_clr(x,y):
    try:
        return surf.get_at((x,y))
    except:
        return None

blur_img = get_trans_surf((256,256))

x = 0
y = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((40,40,40))
    
    if not y > 256:
        clrs = [
                get_clr(x-2,y-2),get_clr(x-1,y-2),get_clr(x,y-2),get_clr(x+1,y-2),get_clr(x+2,y-2),
                get_clr(x-2,y-1),get_clr(x-1,y-2),get_clr(x,y-2),get_clr(x+1,y-2),get_clr(x+2,y-2),
                get_clr(x-2,y),get_clr(x-1,y),get_clr(x,y),get_clr(x+1,y),get_clr(x+2,y),
                get_clr(x-2,y+1),get_clr(x-1,y+1),get_clr(x,y+1),get_clr(x+1,y+1),get_clr(x+2,y+1),
                get_clr(x-2,y+2),get_clr(x-1,y+2),get_clr(x,y+2),get_clr(x+1,y+2),get_clr(x+2,y+2),
        ]
        r = [[],0]
        g = [[],0]
        b = [[],0]
        o = [[],0]
        for clr in clrs:
            if not clr == None:
                r[0].append(clr[0])
                r[1] += clr[0]
                g[0].append(clr[1])
                g[1] += clr[1] 
                b[0].append(clr[2])
                b[1] += clr[2]
                o[0].append(clr[3])
                o[1] += clr[3]
        r = r[1]/len(r[0])
        g = g[1]/len(g[0])
        b = b[1]/len(b[0])
        o = o[1]/len(o[0])
        s = get_trans_surf((1,1))
        s.fill((r,g,b))
        s.set_alpha(o)
        blur_img.blit(s, (x,y))
    
    blank_surf = pygame.Surface((522,264))
    blank_surf.fill((255,255,255))
    screen.blit(blank_surf, (28,28))



    screen.blit(blur_img, (290,32))
    screen.blit(get_image('cat_eye.png', (256,256)), (32,32))





    pointer = pygame.Surface((20,20))
    pointer.fill((130, 130, 130))
    pointer.set_alpha(120)
    screen.blit(pointer ,((290+x)-10,(32+y)-10))


    dot = pygame.Surface((6,6))
    dot.fill((255,0,0))
    screen.blit(dot, (290+x-3,32+y-3))


    if not y > 256:
        if x == 256:
            x = -1
            y += 1
        x += 1

    pygame.display.flip()
    clock.tick(1000)