import graphics as g
win=g.GraphWin(width=100,height=100)
xes=map(lambda x: x,range(101))
pts=map(lambda x: g.Point(x,x**2/100),xes)
pol=g.Polygon(*pts)
pol.draw(win)
win.getMouse()
win.close()