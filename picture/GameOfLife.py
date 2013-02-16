from newPicture import Picture

def p(a) :
    y=0
    for row in a :
        x=0
        for i in row :
            if i == 0:
                grid[x][y].changeFillColor((0,0,0))
            else :
                grid[x][y].changeFillColor((255,0,0))
            x=x+1
        y=y+1
    animate.display()

## update b given a using game of life rules
def update(a,b) :
    h = len(a)
    w = len(a[0])
    for row in range(h) :
        for col in range(w) :
            live = 0
            for r in range(-1,2) :
                for c in range(-1,2) :
                    live = live + a[(row+r)%h][(col+c)%w]
            live = live - a[row][col]
            if live < 2 or live > 3 :
                b[row][col] = 0
            elif live == 2 :
                b[row][col] = a[row][col]
            elif live == 3 :
                b[row][col] = 1
            else :
                print("Live count is wrong")
                

## initialize 2d array of zeroes of given size
def init2d(w,h) :
    a = []
    for i in range(h) :
        a.append([0]*w)
    return a

## main
def main(w,h) :
    global animate
    animate = Picture((w*10, h*10))
    animate.setFillColor((0, 0, 0))
    
    global grid
    grid = [[animate.drawRectFill(x*10, y*10, 10, 10) for y in range(h)]for x in range(w)]
        
    a = init2d(w,h)
    b = init2d(w,h)
    
    # Glider pattern
    a[1][1] = 1
    a[2][2] = 1
    a[3][0] = 1
    a[3][1] = 1
    a[3][2] = 1
    
    u = ""
    while u == "" :   
        p(a)
        u = input("Press enter to continue, any other key to exit ")
        update(a,b)
        a,b = b,a
        
main(80,50)
