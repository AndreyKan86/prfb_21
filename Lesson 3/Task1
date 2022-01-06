import math

def find_time(time):
    time = time.split(",")
    hour = time[1][0:2]
    minut = time[1][2:4]
    seconds = time[1][4:6]
    milis = time[1][6:]
    return str(hour + ":" + minut + ":" + seconds + milis)

def convert(data):
    deg1 = math.trunc(data[0] / 100)
    coord1 = deg1 + (data[0] - 100 * deg1) / 60
    deg2 = math.trunc(data[1] / 100)
    coord2 = deg2 + (data[1] - 100 * deg2) / 60
    coord = coord1, coord2
    return coord

def dist(a, b):
    phi1 = math.radians(a[0])
    lam1 = math.radians(a[1])
    phi2 = math.radians(b[0])
    lam2 = math.radians(b[1])
    dphi = phi2 - phi1
    dlam = lam2 - lam1
    delta = 2 * math.asin(math.sqrt(math.pow(math.sin(dphi / 2), 2) + math.cos(phi1) * math.cos(phi2) * math.pow(math.sin(dlam / 2), 2)))
    distance = 6372795 * delta
    return distance

def find_coord(coord):
    if len(coord) != 80: 
        return 1
    else:
        coord = coord.split(",")
        return float(coord[2]), float(coord[4])

def main ():
    f = open ('nmea.log')
    a = (60.051584, 30.300509)
    line =''
    t = True 
    for i in f:
        if find_coord(i) != 1:
            l = dist(convert(find_coord(i)), a)
            if l < 25 and t is True:
                print ('Время вхождения в заданную область', find_time(i))
                t = False
            if l > 25 and t is False:
                print ('Время выхода из заданной области',   find_time(i))
                t = True
               
    return (line)

    
if __name__ == '__main__':

    print(main())
   
