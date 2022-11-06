import pygame.image
import time

class Frog:
    def __init__(self, x, y, h_velocity, v_velocity, state):
        self.player_x = x
        self.player_y = y
        self.h_velocity = h_velocity
        self.v_velocity = v_velocity
        self.state = "free"
        self.state2 = None


        if(state) == "idle":
            self.img_path = "Images/frog_idle2.png"
        elif state == "run":
            self.img_path = "Images/Ninja Frog/Run (32x32).png"
        elif state == "falling":
            self.img_path = "Images/frog_fall.png"
            # self.player_y+=v_velocity




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

            if block_dict[i]['rect'].y -40 == self.player_y and block_dict[i]['type'] == 1:
                self.state = "idle"
                # print("player_x", self.player_x)
                # print(i,block_dict[i])




            elif block_dict[i]['rect'].y < self.player_y and block_dict[i]['type'] ==2:
                self.state = "falling"

    # def check_falling(self, block_dict):
    #     for i in block_dict:
    #         if block_dict[i]['rect'].x == self.player_x and block_dict[i]['rect'].y == self.player_y:
    #             print(block_dict[i])
    #             # self.state = "falling"






    def update_position(self, jump,running, direction,stop):
        print(self.state)
        if(stop != True):

            if self.state == "falling":
                # self.v_velocity+=0.15
                self.player_y += 1
            elif self.state == "idle" and running == True and direction == "right":
                print("yoo")
                self.h_velocity +=0.01
                self.player_x +=self.h_velocity
            elif self.state == "idle" and running == True and direction == "left":

                self.h_velocity -= 0.01
                self.player_x -= self.h_velocity
            elif self.state == "idle" and jump == True:
                print("Jumping for joy!")
                self.v_velocity+=5
                self.player_y-=self.v_velocity
            elif self.state == "idle":

                self.v_velocity = 0
                self.h_velocity = 0












