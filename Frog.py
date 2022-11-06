import pygame.image
import time

class Frog:
    def __init__(self, x, y, h_velocity, v_velocity, state):
        self.player_x = x
        self.player_y = y
        self.h_velocity = h_velocity
        self.v_velocity = v_velocity


        if(state) == "idle":
            self.img_path = "Images/frog_idle2.png"
        elif state == "run":
            self.img_path = "Images/Ninja Frog/Run (32x32).png"
        elif state == "falling":
            self.img_path = "Images/frog_fall.png"
            self.player_y+=v_velocity



    def draw_player(self,display):
        if self.state == "falling":
            self.img_path = "Images/frog_fall.png"
        elif self.state == "idle":
            self.img_path = "Images/frog_idle2.png"
        elif self.state == "run":
            self.img_path = "Images/Ninja Frog/Run (32x32).png"
        # print(self.img_path)
        frog = pygame.image.load(self.img_path).convert()
        frog = pygame.transform.scale(frog,(48,48))
        frog.set_colorkey((168, 168, 168))

        display.blit(frog, (self.player_x, self.player_y))
    def check_player_blck_collision(self,block_dict):
        for i in block_dict:

            if block_dict[i]['rect'].x == self.player_x  and block_dict[i]['rect'].y -40 == self.player_y and block_dict[i]['type'] == 1:
                self.state = "idle"
                time.sleep(0.5)
                # self.v_velocity = 0
                # self.h_velocity = 0
                # print("collision")
            # elif block_dict[i]['center'][0] == self.player_x  and block_dict[i]['center'][1] + 10 == self.player_y and block_dict[i]['type'] == 0:
            #     self.state = "idle"
            #     print("collisoin")


            elif block_dict[i]['rect'].y < self.player_y and block_dict[i]['type'] ==2:
                self.state = "falling"


    def move_frog(self):
        self.player_x+=1


    def update_position(self):
        print(self.state)
        if self.state == "falling":
            # self.v_velocity+=0.15
            self.player_y += 1
        elif self.state == "idle":

            self.v_velocity = 0
            self.h_velocity = 0








