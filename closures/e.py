formatters = {}
colors = ['red', 'green', 'blue']

for color in colors:
    def in_color(s):
        return ('<spam style="color:' + color + '">' + s + '</span')

    formatters[color] = in_color
