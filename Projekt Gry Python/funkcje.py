import math
from dane import *
class funkcje:
    def music(self):
        mixer.music.load('soundtrack.wav')
        mixer.music.set_volume(0.5)
        mixer.music.play(-1)
    def number_enemy_add(self,number_enemy,level_val):
        if level_val == 2:
            number_enemy = 8
        if level_val == 3:
            number_enemy = 9
        if level_val == 4:
            number_enemy = 10
        if level_val == 5:
            number_enemy = 11
        if level_val == 6:
            number_enemy = 13
        if level_val == 7:
            number_enemy = 15
        if level_val == 8:
            number_enemy = 17
        if level_val == 9:
            number_enemy = 19
        return number_enemy

    def level(self,level_val):
        if score_val > 10:
            level_val = 2
        if score_val > 30:
            level_val = 3
        if score_val > 40:
            level_val = 4
        if score_val > 50:
            level_val = 5
        return level_val

    def score_display(self,x, y):
        score = font.render("score  " + str(score_val), True, (0, 0, 200))
        screen.blit(score, (x, y))

    def level_display(self):
        level_in_game0 = font.render("level  " + str(level_val), True, (250, 250, 250))
        screen.blit(level_in_game0, (700, 0))

    def game_over_str(self):
        over_text = over_font.render("U GOT HIT BY AN ENEMY :(", True, (255, 255, 255))
        screen.blit(over_text, (100, 100))
        score_end = over_font.render('Your score was : ' + str(score_val), True, (255, 0, 0))
        screen.blit(score_end, (100, 250))
        level_end = over_font.render('You have reached level : ' + str(level_val), True, (0, 0, 255))
        screen.blit(level_end, (100, 340))

    def player(self,x, y):
        screen.blit(playerImage, (x, y))

    def enemy(self,x, y, k):
        screen.blit(enemyImage[k], (x, y))

    def bullet(self,x, y):
        global bullet_state
        bullet_state = "fire"
        screen.blit(bulletImage, (x + 16, y + 16))

    # dystans pomiedzy wrogiem a naszym pociskiem

    def collision(self,enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
        if distance < 36:
            return True
        else:
            return False

    def game_over(self,enemyX, enemyY, playerX, playerY):
        distance_game_over = math.sqrt(math.pow(playerX - enemyX, 2) + math.pow(playerY - enemyY, 2))
        if distance_game_over < 36:
            return True
        else:

            return False
