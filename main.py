import pygame
from Map import Map
pygame.init()
pygame.display.init()
display_size = (1000, 800)


display_surface = pygame.display.set_mode(display_size)

run = True

map = Map()
tile_map = map.generate_map()

print("Map: ", map)
print("Map Width:", len(tile_map[0]))
print("Map Height:", len(tile_map))
background_img = pygame.image.load("Images/background_3.png")
background_img = pygame.transform.scale(background_img,(1000,768))

new_tile_map = map.customize_map(tile_map)
# map.create_map_dictionary(new_tile_map)

while(run):
    mouse_pos = pygame.mouse.get_pos()
    # print(mouse_pos)
    display_surface.blit(background_img, (0,0))
    blck_list = map.draw_map(new_tile_map, display_surface)
    print("blck_lsit: ", blck_list)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:

                print("Mouse Pos:", mouse_pos)
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()

pygame.quit()

