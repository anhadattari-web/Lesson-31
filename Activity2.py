import pygame
pygame.init()
scrn_w, scrn_h=400, 500
display_surface=pygame.display.set_mode(scrn_w,scrn_h)
pygame.display.set_caption('adding imageand background image')
background_image=pygame.transform.scale(pygame.image.load('background.png').convert(),(scrn_w,scrn_h))
penguin_image=pygame.transform.scale(pygame.image.load('penguin.png').convert_alpha(),(200,300))
penguin_rect=penguin_image.get_rect(center=(scrn_w//2, scrn_h//2 - 30))
text=pygame.font.Font(None, 36).render('Hello World', True, pygame.Color('Black'))
text_rect=text.get_rect(center=(scrn_w//2, scrn_h//2+110))
def game_loop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get:
            if event.type==pygame.QUIT:
                running=False
        display_surface.blit(background_image,(0,0))
        display_surface.blit(penguin_image,penguin_rect)
        display_surface.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__=='__main__':
    game_loop


