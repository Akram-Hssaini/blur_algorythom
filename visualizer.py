import pygame
import os
import time

blur_value = int(input('Blur Value (default 5): '))

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

eye = get_trans_surf((256,256))
eye.blit(get_image('cat_eye.png',(256,256)), (0,0))
blured_img = get_trans_surf((256,256))
blank_surf = pygame.Surface((522,264))
blank_surf.fill((255,255,255))

def get_clr(x,y):
    try:
        return eye.get_at((x,y))
    except:
        return None

def get_color_avg_of_range(x,y,rang):
    rgbos = [[[],0],[[],0],[[],0],[[],0]]
    x_ind = -(int(rang/2)+1)
    y_ind = -(int(rang/2)+1)
    for i in range(rang):
        y_ind += 1
        for i2 in range(rang):
            x_ind += 1
            clr = get_clr(x+x_ind,y+y_ind)
            if not clr == None:
                rgbos[0][0].append(clr[0])
                rgbos[0][1] += clr[0]
                rgbos[1][0].append(clr[1])
                rgbos[1][1] += clr[1]
                rgbos[2][0].append(clr[2])
                rgbos[2][1] += clr[2]
                rgbos[3][0].append(clr[3])
                rgbos[3][1] += clr[3]
        x_ind = -(int(rang/2)+1)
    avg_clr = (0,0,0,0)
    if not len(rgbos[0][0]) == 0 and not len(rgbos[1][0]) == 0 and not len(rgbos[2][0]) == 0 and not len(rgbos[3][0]) == 0:
        avg_clr = (rgbos[0][1]/len(rgbos[0][0]),rgbos[1][1]/len(rgbos[1][0]),rgbos[2][1]/len(rgbos[2][0]),rgbos[3][1]/len(rgbos[3][0]))
    return avg_clr

last = time.time()

for y in range(256):
    for x in range(256):
        r,g,b,o = get_color_avg_of_range(x,y, blur_value)
        s = get_trans_surf((1,1))
        s.fill((r,g,b))
        s.set_alpha(o)
        blured_img.blit(s, (x,y))

print(f'loading time: {round(time.time()-last, 4)}s')
screen = pygame.display.set_mode((567, 320))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((40,40,40))
    screen.blit(blank_surf, (28,28))
    screen.blit(blured_img, (290,32))
    screen.blit(get_image('cat_eye.png', (256,256)), (32,32))

    pygame.display.flip()
    clock.tick(1000)