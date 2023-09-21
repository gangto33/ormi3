class OperList:
    def __init__(self, *args):
        self.__operlist = list(args)


    def __str__(self):
        return f'<{str(self.__operlist)[1:-1]}>'


    def __repr__(self):
        return f'<{str(self.__operlist)[1:-1]}>'


    def __len__(self):
        return self.__operlist.__len__()
    

    def __add__(self, other):
        if len(self.__operlist) != len(other.__operlist):
            raise
        for i in range(len(self.__operlist)):
            self.__operlist[i] += other.__operlist[i]
        return f'<{str(self.__operlist)[1:-1]}>'
    

    def __sub__(self, other):
        if len(self.__operlist) != len(other.__operlist):
            raise
        for i in range(len(self.__operlist)):
            self.__operlist[i] -= other.__operlist[i]
        return f'<{str(self.__operlist)[1:-1]}>'


    def __mul__(self, other):
        if not isinstance(other, int):
            raise
        for i in range(len(self.__operlist)):
            self.__operlist[i] *= other
        return f'<{str(self.__operlist)[1:-1]}>'


    def append(self, data):
        self.__operlist.append(data)
    

    def remove(self, data):
        self.__operlist.remove(data)

l = OperList(1, 2, 3, 4)
l
l.append(5)
print(l + l) # 출력: <2, 4, 6, 8, 10>
print(l + l)



#############################################

f = open('student.csv', 'w')
s = '''학년,반,번,이름,국어,영어,수학,사회
3,3,1,licat,90,80,30,40
3,3,2,mura,80,70,60,30
3,3,3,binky,30,80,70,30
'''
f.write(s)
f.close()

f = open('student.csv', 'r')
lines = f.readlines()
new_s = f"{lines[0][:-1]},평균\n"

for line in lines:
    line = line[:-1]
    try:
        line += f",{sum(map(int, line.split(',')[4:])) / 4}\n"
        new_s += line
    except:
        continue

f.close()
print(new_s)

f = open('student.csv', 'w')
f.write(new_s)
f.close()