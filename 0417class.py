'''
class student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"

민수 = student("민수", 85)
지영 = student("지영", 92)

print(민수.get_grade())
print(지영.get_grade())
'''

'''
class student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __str__(self):
        return'이름 :{}, 점수 : {}'.format(self.name,self.score)

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"

민수 = student("민수", 85)
지영 = student("지영", 92)

print(민수)
print(민수.name)
'''

class student:
    def __init__(self, name, score):
        self.__name = name #'__'를 붙여 캡슐화
        self.__score = score
    
    def __str__(self):
        return'이름 :{}, 점수 : {}'.format(self.__name,self.__score)

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"

민수 = student("민수", 85)
지영 = student("지영", 92)

'''
민수.name = name
민수.score = score
'''
print(민수)
print(민수.__name) #실제로는 있는데 밖에서는 안 보이게 암호화했다
