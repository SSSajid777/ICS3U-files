from student import Student
 
#Create a student object


student1= Student("Emma", "Sun", 15, "10th")

#Add some classes for our student

student1.add_class("Physics")
student1.add_class("English")
student1.add_class("Computer Science")


#Make sure it all works
print("Student Name: " +student1.fname+" "+student1.lname)
print("Age:"+str(student1.age))
print("Grade: "+student1.grade)
print("Classes:")
print(student1.classes)

