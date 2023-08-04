class Fighter():
    def __init__(self, model, missile):
        self.model = model
        self.missile = missile
    
    def attack(self):
        print(self.model+" 출동")
    def fire(self):
        print(self.missile+" 발사")

fighter1 = Fighter('F22', '미사일')
fighter2 = Fighter('F16', '전자포')

fighter2.attack()
fighter1.fire()


student1 = 0
student2 = 0

def plus1(num):
    global student1
    student1 += num
    return student1

def plus2(num):
    global student2
    student2 += num
    return student2

print(plus1(3)) # 3
print(plus2(4)) # 4
print(plus1(5)) # 8
print(plus2(5)) # 9


class Oper:
    def __init__(self):
        self.res = 0
    
    def plus(self, num):
        self.res += num
        return self.res

student1 = Oper()
student2 = Oper()

print(student1.plus(3)) # 3
print(student2.plus(4)) # 4
print(student1.plus(5)) # 8
print(student2.plus(5)) # 9

#https://rebro.kr/133