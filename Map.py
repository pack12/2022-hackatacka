import pygame
class Map:

    def generate_map(self):
        tile_map = []
        row = []
        #Originally 1, 125
        for i in range(1, 8):

            for j in range(1, 49):

                row.append(0)
            tile_map.append(row)
            row = []

        return tile_map
    def customize_map(self, tile_map):
        for i in range(len(tile_map[0])):
            # print(i)
            tile_map[0][i] = 2
        for i in range(len(tile_map[1])):
            tile_map[1][i] = 2
        for i in range(len(tile_map[2])):
            tile_map[2][i] = 2
        for i in range(len(tile_map[3])):
            tile_map[3][i] = 2
        for i in range(len(tile_map[4])):
            tile_map[4][i] = 2
        for i in range(len(tile_map[5])):
            tile_map[5][i] = 2
        for i in range(len(tile_map[6])):
            tile_map[6][i] = 1
        tile_map[6][0] = 2
        tile_map[6][1] = 2
        tile_map[6][2] = 2
        tile_map[6][3] = 2
        tile_map[6][4] = 2
        tile_map[6][5] = 2

        for i in range(27, 48):
            tile_map[6][i] = 2
            tile_map[6][i] = 0



        return tile_map


    def create_map_dictionary(self, list_types, blck_rect_list):
        tiles = {}
        blck_nmbr = 0
        block_str = "block_"
        block_str = block_str + str(blck_nmbr)

        #Assign correct Center values and rect values
        incrementor = 0
        # print("BEFORE the dark days!", blck_rect_list[incrementor])
        blck_nmbr = 0
        block_str = "block_"
        block_str = block_str + str(blck_nmbr)
        while(incrementor != 336):

            tiles[block_str] = {'isPlayerOn':False,'center':(blck_rect_list[incrementor].center[0], blck_rect_list[incrementor].center[1]), 'rect':blck_rect_list[incrementor],
                                'type':list_types[incrementor]}
            # tiles[block_str] = blck_rect_list[incrementor]
            incrementor+=1
            blck_nmbr+=1
            block_str = "block_" + str(blck_nmbr)
        # print(tiles)



        return tiles

    def get_blck_list(self, blck_list):
        return blck_list
    def create_blck_rect(self, tile_map, display):
        dirt_block = pygame.image.load("Images/dirt_block.png")
        dirt_block = pygame.transform.scale(dirt_block, (48, 48))

        grass_block = pygame.image.load("Images/grass_block.png")
        grass_block = pygame.transform.scale(grass_block, (48, 48))
        # print(tile_map)
        block_rect_list = []
        x, y = 0, 0
        for i in tile_map:
            for j in i:

                if j == 0:
                    block = display.blit(dirt_block, (x, y))
                    block_rect_list.append(block)
                    # self.create_map_dictionary(tile_map, block)
                if j == 1:
                    block = display.blit(grass_block, (x, y))
                    block_rect_list.append(block)
                    # self.create_map_dictionary(tile_map, block)

                if j == 2:
                    block = pygame.Rect(x, y, 48, 48)
                    block_rect_list.append(block)
                    # self.create_map_dictionary(tile_map, block)

                x += 48
                if x == 1008:
                    x = 0
                    y += 48
        return block_rect_list

    def draw_map(self, tile_dictionary, display):
        dirt_block = pygame.image.load("Images/dirt_block.png")
        dirt_block = pygame.transform.scale(dirt_block, (48, 48))

        grass_block = pygame.image.load("Images/grass_block.png")
        grass_block = pygame.transform.scale(grass_block, (48, 48))
        for i in tile_dictionary:
            # print("DICK:", i)
            # print(tile_dictionary[i])

            if(tile_dictionary[i]['type']) == 0:
                display.blit(dirt_block, (tile_dictionary[i]['rect'].x, tile_dictionary[i]['rect'].y))
            if (tile_dictionary[i]['type']) == 1:
                display.blit(grass_block, (tile_dictionary[i]['rect'].x, tile_dictionary[i]['rect'].y))
            if (tile_dictionary[i]['type']) == 2:
                # display.blit(dirt_block, (tile_dictionary[i]['rect'].x, tile_dictionary[i]['rect'].y))
                pass

            # display.blit()


        # print(block_rect_list)
        # return block_rect_list





