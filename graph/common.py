__author__ = 'bcm'
from pygame import Color


class Colors():
    #color declarations
    monokai_bg = Color(34, 34, 34)
    monokai_orange = Color(255, 151, 60)
    monokai_purple = Color(145, 84, 188)
    monokai_white = Color(235, 249, 243)
    monokai_green = Color(152, 224, 35)
    monokai_blue = Color(71, 192, 230)
    color_red = Color(255, 0, 0)
    color_green = Color(0, 255, 0)
    color_blue = Color(0, 0, 255)
    color_white = Color(255, 255, 255)
    color_black = Color(0, 0, 0)

    #color assignments
    background_color = monokai_bg
    vertex_color = monokai_purple
    vertex_boarder_color = monokai_blue
    word_color = monokai_white
    edge_color = monokai_blue
    selected_color = monokai_orange
    debug_color = monokai_green