import colorgram as clg
import turtle as t
import random

t.colormode(255)
# colorsExt = clg.extract("image.jpg", 20)
# rgb_colors = []
#
# for color in colorsExt:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71),
         (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229),
         (14, 205, 222), (63, 21, 10), (224, 19, 111)]


brush = t.Turtle()
brush.speed("fastest")
brush.penup()
brush.hideturtle()
brush.setheading(218)
brush.forward(450)
brush.setheading(0)

number_of_dots = 181

for dot_count in range(1, number_of_dots):
    brush.dot(20, random.choice(color))
    brush.forward(50)
    if dot_count % 15 == 0:
        brush.setheading(90)
        brush.forward(50)
        brush.setheading(180)
        brush.forward(750)
        brush.setheading(0)

screen = t.Screen()
screen.exitonclick()