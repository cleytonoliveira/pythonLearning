width = int(input('Type the width of your wall: '))
height = int(input('Type the height of your wall: '))
area = width * height
paintSpend = area / 2
print('The width of {}, height of {} the area is {} and will be necessary {} litre to paint your wall.'.format(width, height, area, paintSpend))
