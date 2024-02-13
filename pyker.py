class Canvas:
    def __init__(self, width, height, color=0xFFFFFF):
        self.pixels = [color] * (width * height)
        self.width = width
        self.height = height

    def fill(self, color):
        for i in range(self.width*self.height):
            self.pixels[i] = color

    def rect(self, x0, y0, w, h, color):
        for dy in range(h):
            y = y0 + dy
            if y not in range(self.height): continue
            for dx in range(w):
                x = x0 + dx
                if x not in range(self.width): continue
                self.pixels[y*self.width + x] = color

    def circle(self, cx, cy, r, color):
        if r == 0: return

        x1 = cx - r
        x2 = cx + r
        if x1 > x2: (x1, x2) = (x2, x1)

        y1 = cy - r
        y2 = cy + r
        if y1 > y2: (y1, y2) = (y2, y1)

        for y in range(y1, y2 + 1):
            if y not in range(self.height): continue
            for x in range(x1, x2 + 1):
                if x not in range(self.width): continue
                dx = x - cx
                dy = y - cy
                if dx*dx + dy*dy <= r*r:
                    self.pixels[y*self.width + x] = color
