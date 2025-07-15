GAME_WIDTH = 700
GAME_height=700
speed = 40
body_parts = 3
snake_color = "#00ff00"
food_color = "#ff0000"
background_color = "#000000"


class_snake:
    pass

class_food:
    pass

def next_turn():
    pass

def change_direction():
    pass

def check_collisions():
    pass

def game_over():
    pass

window = Tk()
window.title("snake game")

score = 0
direction = 'down'

label = label (window, text="Score:{}".format(score),font=('algerian',40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, )

window.mainloop()
