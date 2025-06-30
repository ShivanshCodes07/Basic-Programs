class Student():
    def __init__(self,name ,marks):
        self.name = name
        self.marks = marks
    def avg(self):
        sum = 0
        for i in self.marks:
            sum+=i
            
        return sum/3

    
s1 = Student("shivansh" , [90,90,90])
print("hi" ,s1.name ,"your average marks is " ,s1.avg())