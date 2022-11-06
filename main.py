import pygame
from Map import Map
from Frog import Frog
pygame.init()
pygame.display.init()
display_size = (1000, 768)


display_surface = pygame.display.set_mode(display_size)

run = True

map = Map()
tile_map = map.generate_map()

print("Map: ", map)
print("Map Width:", len(tile_map[0]))
print("Map Height:", len(tile_map))
background_img = pygame.image.load("Images/jungle_background.png")
background_img = pygame.transform.scale(background_img,(1000,768))

new_tile_map = map.customize_map(tile_map)
print("newtileMap:",new_tile_map)
list_types = []
for i in range(len(new_tile_map)):
    for j in range(len(new_tile_map[i])):
        list_types.append(new_tile_map[i][j])
# print("LIST TYPES: ", list_types)
# print("LIST LENGTH", len(list_types))
blck_list = map.create_blck_rect(new_tile_map, display_surface)
tile_dictionary = map.create_map_dictionary(list_types, blck_list)
print(tile_dictionary)
# print("DICT LENGTH", len(tile_dictionary))
# print("blck_lsit: ", blck_list)


frog = Frog(96, 500, 0, 0, "idle")
print(frog.img_path)

while(run):
    mouse_pos = pygame.mouse.get_pos()
    # print(mouse_pos)
    display_surface.blit(background_img, (0,0))
    map.draw_map(tile_dictionary, display_surface)
    frog.check_player_blck_collision(tile_dictionary)
    frog.update_position()
    frog.draw_player(display_surface)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:

                print("Mouse Pos:", mouse_pos)
            if event.key == pygame.K_RIGHT:

                print("running")
                frog.state = "running"
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()

pygame.quit()

