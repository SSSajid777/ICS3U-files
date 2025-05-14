from student import Student
 
#Create a student object


student1= Student("Emma", "Sun", 15, "10th")

#Add some classes for our student

student1.add_class("Physics")
student1.add_class("English")
student1.add_class("Computer Science")

#Add some marks for the student

student1.add_final_grade("Physics", 97.5)
student1.add_final_grade("English", 0.01)
student1.add_final_grade("Computer Science", 100.1)


#Make sure it all works
print("Student Name: " +student1.fname+" "+student1.lname)
print("Age: "+str(student1.age))
print("Grade: "+student1.grade)
print("Classes:")
print(student1.classes)

student1.add_avg_final_grade(average)
