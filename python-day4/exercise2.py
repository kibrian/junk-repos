PI=3.142
radious=float(input('Enter radious: '))

def area(radious):
    area=PI*radious*radious
    return area

def cir(radious):
    cir=2*PI*radious
    return cir

print('area is {} cir is {}'.format(area(radious),cir(radious)))