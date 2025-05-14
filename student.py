class Student():   #This is my student class for ICS3U1
    def __init__(self, fname, lname, age, grade):
        """
        Initialize a student object with first name, last name, age,, grade and 
        then add an empty dictionary for classes

        """
        self.fname=fname
        self.lname=lname
        self.age=age
        self.grade=grade
        self.classes={}

    def add_class(self, class_name):
        """
        Add a class to the classes dictionary. The key is the name and the initial value is None.
        We can add it later.

        """
        self.classes[class_name]=None


    def add_final_grade(self, class_name, final_grade):
        #Adds a final value to the classes dictionary
        if class_name in self.classes:
         self.classes[class_name]= final_grade   
        else:
           print("Class does not exist.")

    


    