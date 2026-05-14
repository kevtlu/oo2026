import tkinter as tk
import math

class RegularPolygon:
    def __init__(self, cx, cy, radius, sides):
        self.cx = cx
        self.cy = cy
        self.radius = radius
        self.sides = sides

    def get_corner(self):
        points = []

        for i in range(self.sides):
            angle = 2 * math.pi * i / self.sides - math.pi / 2

            x = self.cx + self.radius * math.cos(angle)
            y = self.cy + self.radius * math.sin(angle)

            points.append((x, y))

        return points

    def get_area(self):
        return (self.sides * self.radius ** 2 *
                math.sin(2 * math.pi / self.sides)) / 2

    def draw(self, canvas):
        vertices = self.get_corner()

        coords = []
        for x, y in vertices:
            coords.extend([x, y])

        canvas.create_polygon(
            coords,
            outline="black",
            fill="lightgreen",
            width=2
        )

root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

info_label = tk.Label(root, text="")
info_label.pack()

def update_polygon(value):
    sides = int(value)

    canvas.delete("all")

    polygon = RegularPolygon(250, 250, 120, sides)

    polygon.draw(canvas)

    area = polygon.get_area()

    info_label.config(
        text=f"Nurkade arv: {sides}    Pindala: {area:.2f}"
    )

slider = tk.Scale(
    root,
    from_=3,
    to=20,
    orient=tk.HORIZONTAL,
    label="Nurkade arv",
    command=update_polygon
)

slider.pack()

slider.set(5)

root.mainloop()