class student():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def concat(self):
        full_name=self.fname+" "+self.lname
        return full_name
Student=student("Astuti","Ranjan")
full_name= Student.concat() 
print(full_name)

if __name__=="__main__":
    Student=student("Nishant","Ranjan")
    full_name= Student.concat()
    print(full_name)
    Student=student("Nishant","Ranjan")
    full_name= Student.concat()
    print(full_name)


