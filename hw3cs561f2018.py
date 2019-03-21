# -*- coding: UTF-8 -*-
import numpy as np
#fo = open("output2.txt", "w")
#1 to move left, 2 to move north, 3 to move right, 4 to move south
#A = [2,4,3,1]
A = [1,3,4,2]
#the order of action is tie breaking
r = 0.9

class car(object):
    def __init__(self, start, s):
        self.start = start
        self.end = [-1,-1]
        self.map_r = []
        self.buf_d = np.zeros((s,s), dtype=int)
        self.map_d = np.zeros((s,s), dtype=int)
        self.S = []
        self.U = []
        self.u = []
        return
    
    def update_end(self, loc, s):
        self.end = loc
        for i in range(s):
            for j in range(s):
                if(i != loc[0] or j != loc[1]):
                    self.S.append([i, j])
        return
    
    def update_map_r(self, map_in, s):
        self.map_r = map_in
        self.U = clone(s, map_in)
        self.u = clone(s, self.U)            
        return
    
    def update_map_d(self, s):
        get_direction(s, self.S, self.map_r, self.U, self.u, self.map_d, self.buf_d, A, r)
        return
    
    def output_car(self):
        print "start: ", self.start," end: ", self.end
        print "S: "
        print self.S   
        print "map_reward: "
        for i in range(s):
            for j in range(s):
                print ("{:04d}".format(self.map_r[j][i])),
            print(" ")         
        '''fo.write("map_direction and utility: \n "),
        for i in range(s):
            fo.write("(%08d)" %i),
        fo.write("\n")
        for i in range(s):
            fo.write(str(i)),
            for j in range(s):
                fo.write("(%07.2f" %self.U[j][i]),
                if (self.map_d[j][i] == 1):
                    fo.write("←"),
                elif (self.map_d[j][i] == 2):
                    fo.write("↑"),
                elif (self.map_d[j][i] == 3):
                    fo.write("→"),
                elif (self.map_d[j][i] == 4):
                    fo.write("↓"),
                else:
                    fo.write("0"),
                fo.write(")"),    
            fo.write("\n")'''
        print "map_direction and utility: \n ",
        for i in range(s):
            print ("(%010d)" %i),
        print ""
        for i in range(s):
            print i,
            for j in range(s):
                print ("(%07.2f" %self.U[j][i]),
                if (self.map_d[j][i] == 1):
                    print "←",
                elif (self.map_d[j][i] == 2):
                    print "↑",
                elif (self.map_d[j][i] == 3):
                    print "→",
                elif (self.map_d[j][i] == 4):
                    print "↓",
                else:
                    print "0",
                print ")",    
            print(" ")
        return

def get_direction(s, S, R, U, u, D, d, A, r):
    stop = False
    #i = 0
    while stop == False:
    #for a in range(50):    
        #print "\ni : ", i 
        #i += 1
        for st in range(len(S)):
            pos = S[st]
            x = pos[0]
            y = pos[1]
            #print pos
            buf_max = -1e9
            for a in range(len(A)):
                buf = 0          
                if(A[a] == 2):#move north
                    if (x == 0):#left
                        buf = buf + 0.1*U[x][y]
                    else:
                        buf = buf + 0.1*U[x-1][y]
                    if (y == 0):#north
                        buf = buf + 0.7*U[x][y]
                    else:
                        buf = buf + 0.7*U[x][y-1]
                    if (x == s-1):#right
                        buf = buf + 0.1*U[x][y]
                    else:
                        buf = buf + 0.1*U[x+1][y]
                    if (y == s-1):#south
                        buf = buf + 0.1*U[x][y]
                    else:
                        buf = buf + 0.1*U[x][y+1]
                elif(A[a] == 4):#move south
                    if (x == 0):#left
                        buf = buf + 0.1*U[x][y]
                    else:
                        buf = buf + 0.1*U[x-1][y]
                    if (y == 0):#north
                        buf = buf + 0.1*U[x][y]
                    else:
                        buf = buf + 0.1*U[x][y-1]
                    if (x == s-1):#right
                        buf = buf + 0.1*U[x][y]
                    else:
                        buf = buf + 0.1*U[x+1][y]
                    if (y == s-1):#south
                        buf = buf + 0.7*U[x][y]
                    else:
                        buf = buf + 0.7*U[x][y+1]        
                elif(A[a] == 3):#move right
                    if (x == 0):#left
                        buf = buf + 0.1*U[x][y]
                    else:
                        buf = buf + 0.1*U[x-1][y]
                    if (y == 0):#north
                        buf = buf + 0.1*U[x][y]
                    else:
                        buf = buf + 0.1*U[x][y-1]
                    if (x == s-1):#right
                        buf = buf + 0.7*U[x][y]
                    else:
                        buf = buf + 0.7*U[x+1][y]
                    if (y == s-1):#south
                        buf = buf + 0.1*U[x][y]
                    else:
                        buf = buf + 0.1*U[x][y+1]
                elif(A[a] == 1):#move left
                    if (x == 0):#left
                        buf = buf + 0.7*U[x][y]
                    else:
                        buf = buf + 0.7*U[x-1][y]
                    if (y == 0):#north
                        buf = buf + 0.1*U[x][y]
                    else:
                        buf = buf + 0.1*U[x][y-1]
                    if (x == s-1):#right
                        buf = buf + 0.1*U[x][y]
                    else:
                        buf = buf + 0.1*U[x+1][y]
                    if (y == s-1):#south
                        buf = buf + 0.1*U[x][y]
                    else:
                        buf = buf + 0.1*U[x][y+1]
                #print "action: ", A[a]
                #print "value: ", buf
                if(buf > buf_max):
                    buf_max = buf
                    d[x][y] = A[a]
            #print "buf_max: ", buf_max
            u[x][y] = R[x][y] + r*buf_max
        flag_1 = True
        flag_2 = True
        for st in range(len(S)):
            pos = S[st]
            x = pos[0]
            y = pos[1]
            if(u[x][y] - U[x][y] > 0.1):
                flag_1 = False
            U[x][y] = u[x][y]
            if(D[x][y] != d[x][y]):
                flag_2 = False
            D[x][y] = d[x][y]
            #print "x, y: ", x, y," U[st]: ", U[x][y]," D[st]: ", D[x][y]
        if flag_1 == True and flag_2 == True:
            stop = True
            #print i
    return            
    
def input_function():
    with open("input.txt") as fi:
        s = int(fi.readline())
        n = int(fi.readline())
        o = int(fi.readline())
        obstacles = []
        for i in range(o):
            line = fi.readline().split(",")
            x = int(line[0])
            y = int(line[1])
            obstacles.append([x,y])
        cars = []
        for i in range(n):
            line = fi.readline().split(",")
            x = int(line[0])
            y = int(line[1])
            new = car([x,y], s)
            cars.append(new)
        for i in range(n):
            line = fi.readline().split(",")
            x = int(line[0])
            y = int(line[1])
            cars[i].update_end([x,y], s)
    return s, n, o, obstacles, cars
    
def check_in(s, n, o, obstacles, cars):
    print "s: ", s
    print "n: ", n
    print "o: ", o
    print "obstacles: ", obstacles
    print "cars: "
    for i in range(len(cars)):
        print "i = ", i
        cars[i].output_car()
    return  

def check_map(s, map_in):
    print "map with obstacles: "
    for i in range(s):
        for j in range(s):
            print ("{:04d}".format(map_in[j][i])),
        print(" ")
    return

def make_map(s, obstacles):
    map_ob = []
    for i in range(s):
        map_row = []
        for j in range(s):
            map_row.append(-1)
        map_ob.append(map_row)
    for i in range(len(obstacles)):
        x = obstacles[i][0]
        y = obstacles[i][1]
        map_ob[x][y] = map_ob[x][y] - 100
    return map_ob    

def map_cars(s, map_ob, cars):
    for i in range(len(cars)):
        tem = clone(s, map_ob)
        tem[cars[i].end[0]][cars[i].end[1]] = tem[cars[i].end[0]][cars[i].end[1]] + 100
        cars[i].update_map_r(tem, s)
        cars[i].update_map_d(s)
    return
    
def clone(s, map_in):
    out = []
    for i in range(s):
        new = []
        for j in range(s):
            new.append(map_in[i][j])
        out.append(new)
    return out
 
def simulate(s, car):
    #car.output_car()
    out = 0
    for i in range(10):
        np.random.seed(i)
        swerve = np.random.random_sample(1000000)
        k = 0
        buff_x = car.start[0]
        buff_y = car.start[1]
        pos = [buff_x, buff_y]
        #print "car.start: ", car.start
        #print "pos: ", pos
        while (pos != car.end):
            x = pos[0]
            y = pos[1]
            #print "before\npos: ", pos
            #print "out: ", out
            #print "k: ",k," swerve[k]: ", swerve[k]
            if(swerve[k] > 0.7):
                if(swerve[k] > 0.8):
                    if(swerve [k] > 0.9):#go on opposite direction on the direction map
                        #print "turn_left(turn_left(move))"
                        if(car.map_d[x][y] == 1):#left on direction map => go right
                            if(x < s-1):#boundary check
                                pos[0] = pos[0] + 1
                        elif(car.map_d[x][y] == 2):#north on direction map => go south
                            if(y < s-1):#boundary check
                                pos[1] = pos[1] + 1
                        elif(car.map_d[x][y] == 3):#right on direction map => go left
                            if(x > 0):#boundary check
                                pos[0] = pos[0] - 1
                        elif(car.map_d[x][y] == 4):#south on direction map => go north
                            if(y > 0):#boundary check
                                pos[1] = pos[1] - 1
                    else:#go on right direction on the direction map
                        #print "turn_right(move)"
                        if(car.map_d[x][y] == 1):#left on direction map => go north
                            if(y > 0):#boundary check
                                pos[1] = pos[1] - 1
                        elif(car.map_d[x][y] == 2):#north on direction map => go right
                            if(x < s-1):#boundary check
                                pos[0] = pos[0] + 1
                        elif(car.map_d[x][y] == 3):#right on direction map => go south
                            if(y < s-1):#boundary check
                                pos[1] = pos[1] + 1
                        elif(car.map_d[x][y] == 4):#south on direction map => go left
                            if(x > 0):#boundary check
                                pos[0] = pos[0] - 1
                else:#go on left direction on the direction map 
                        #print "turn_left(move)"
                        if(car.map_d[x][y] == 1):#left on direction map => go south
                            if(y < s-1):#boundary check
                                pos[1] = pos[1] + 1
                        elif(car.map_d[x][y] == 2):#north on direction map => go left
                            if(x > 0):#boundary check
                                pos[0] = pos[0] - 1
                        elif(car.map_d[x][y] == 3):#right on direction map => go north
                            if(y > 0):#boundary check
                                pos[1] = pos[1] - 1
                        elif(car.map_d[x][y] == 4):#south on direction map => go right
                            if(x < s-1):#boundary check
                                pos[0] = pos[0] + 1
            else:#go on same direction on the direction map
                #print "move"
                if(car.map_d[x][y] == 1):#left
                    if(x > 0):#boundary check
                        pos[0] = pos[0] - 1
                elif(car.map_d[x][y] == 2):#north
                    if(y > 0):#boundary check
                        pos[1] = pos[1] - 1
                elif(car.map_d[x][y] == 3):#right
                    if(x < s-1):#boundary check
                        pos[0] = pos[0] + 1
                elif(car.map_d[x][y] == 4):#south
                    if(y < s-1):#boundary check
                        pos[1] = pos[1] + 1
            out = out + car.map_r[x][y]
            k += 1 
            #print "after\npos: ", pos
            #print "x: ",x," y: ",y
            #print "out: ", out
            #print "k: ", k
        out = out + 100
        #out = out + car.map_r[car.end[0]][car.end[1]]
        #print "i: ",i
        #print "out: ", out
    #print "out: ", out
    return int(np.floor(out/10))

def simulate_all(s, cars):
    out = []
    for i in range(len(cars)):
        tem = simulate(s, cars[i])
        out.append(tem)
    return out
    
s, n, o, ob, cars = input_function()
map_ob = make_map(s, ob)
map_cars(s, map_ob, cars)
#check_map(s, map_ob)
#check_in(s, n, o, ob, cars)
ans = simulate_all(s, cars)
#print "ans: ", ans
'''
with open("My_policy0.txt", "w") as fo:
    for k in range(len(cars)):
        for i in range(s):
            for j in range(s):
                if (cars[k].map_d[j][i] == 1):
                    fo.write("←"),
                elif (cars[k].map_d[j][i] == 2):
                    fo.write("↑"),
                elif (cars[k].map_d[j][i] == 3):
                    fo.write("→"),
                elif (cars[k].map_d[j][i] == 4):
                    fo.write("↓"),
                else:
                    fo.write("0"),
            fo.write("\n")
        fo.write("\n")'''       
with open("output.txt", "w") as fo:
    for i in range(len(ans)):
        fo.write(str(ans[i]) + "\n")
