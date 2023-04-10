import colorgram

colors = colorgram.extract('hirst_painting.jpg', 20)
rgb_values = []

for x in range(len(colors)):
    rgb_color = colors[x].rgb
    rgb_tuple = (rgb_color.r, rgb_color.g, rgb_color.b)
    rgb_values.append(rgb_tuple)
print(rgb_values)
