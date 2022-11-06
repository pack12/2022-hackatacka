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
print(frog.state)
running = False
direction = None
jump = False
stop = False
stop_count = 0

tile_dictionary['block_98']['type'] = 1
while(run):
    mouse_pos = pygame.mouse.get_pos()
    # print(mouse_pos)
    display_surface.blit(background_img, (0,0))
    map.draw_map(tile_dictionary, display_surface)
    frog.check_player_blck_collision(tile_dictionary)
    print("running:", running, "direction: ", direction)
    frog.update_position(jump,running, direction, stop)
    frog.draw_player(display_surface)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:

                print("Mouse Pos:", mouse_pos)
            if event.key == pygame.K_RIGHT:

                running = True
                direction = "right"
            elif event.key == pygame.K_LEFT:
                running = True
                direction = "left"
            elif event.key == pygame.K_SPACE:
                jump = True
                running = False
            elif event.key == pygame.K_s:
                stop_count+=1
                if stop_count %2 == 0:
                    stop = False
                elif stop_count %2 != 0:

                    stop = True
                    running = False
                    jump = False

        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()

pygame.quit()

