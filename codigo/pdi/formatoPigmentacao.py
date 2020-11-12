# Acesso as funcoes por lista

# link: https://www.daniweb.com/programming/software-development/threads/321181/python-bresenham-circle-arc-algorithm
# {'tipo': 'circulo', 'raio': x, 'centroX': x, 'centroY': y}
def circulo(radius, cx, cy,):
    "Bresenham complete circle algorithm in Python"
    # init vars
    switch = 3 - (2 * radius)
    points = set()
    x = 0
    y = radius
    # first quarter/octant starts clockwise at 12 o'clock
    while x <= y:
        # first quarter first octant
        points.add((cx+x,-y+cy))
        # first quarter 2nd octant
        points.add((cx+y,-x+cy))
        # second quarter 3rd octant
        points.add((cx+y,x+cy))
        # second quarter 4.octant
        points.add((cx+x,y+cy))
        # third quarter 5.octant
        points.add((-x+cx,y+cy))        
        # third quarter 6.octant
        points.add((-y+cx,x+cy))
        # fourth quarter 7.octant
        points.add((-y+cx,-x+cy))
        # fourth quarter 8.octant
        points.add((-x+cx,-y+cy))
        if switch < 0:
            switch = switch + (4 * x) + 6
        else:
            switch = switch + (4 * (x - y)) + 10
            y = y - 1
        x = x + 1
    return points

# pontos 1 - 4
def formatoQuadratico(cx, cy):
    pontos = set()
    #pontos.add((cx, cy))
    pontos.add((cx, cy-1))
    pontos.add((cx+1,cy))
    pontos.add((cx+1,cy-1))
    #pontos.add(cx-1, cy-1)
    return pontos

'''
def validacaoCoordenada(dimensaoX, dimensaoY, pontoX, pontoY):
    if( (dimensaoX > pontoX) or dimensaoX < 0)
        return 
'''