import pygame.image


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


    def draw_player(self,display):
        frog = pygame.image.load(self.img_path).convert()
        frog = pygame.transform.scale(frog,(48,48))
        frog.set_colorkey((168, 168, 168))

        display.blit(frog, (self.player_x, self.player_y))


