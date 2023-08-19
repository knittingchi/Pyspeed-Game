import keyboard
import time
import random

class CarGame:
    def __init__(self):
        self.player_position = 1
        self.obstacle_position = random.randint(1, 3)
        self.score = 0

    def display_road(self):
        road = "|" + " " * self.player_position + "🚗" + " " * (3 - self.player_position) + "|"
        obstacle = "|" + " " * self.obstacle_position + "🚧" + " " * (3 - self.obstacle_position) + "|"
        print(road)
        print(obstacle)
        print("-" * 7)

    def move_car(self, direction):
        if direction == "left" and self.player_position > 0:
            self.player_position -= 1
        elif direction == "right" and self.player_position < 2:
            self.player_position += 1

    def play(self):
        print("Welcome to the Car Game!")
        print("Use left and right arrow keys to control the car.")
        time.sleep(2)

        while True:
            self.obstacle_position = random.randint(0, 2)
            self.display_road()

            if self.obstacle_position == self.player_position:
                print("Game Over!")
                print("Your score:", self.score)
                break

            time.sleep(0.5)
            self.score += 1

            if keyboard.is_pressed("left"):
                self.move_car("left")
            elif keyboard.is_pressed("right"):
                self.move_car("right")

if __name__ == "__main__":
    game = CarGame()
    game.play()
