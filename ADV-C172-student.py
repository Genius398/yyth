 class Doctor():
    def __init__(self):
        print("This is a modified doctor class")
        
    def BMI(weight, height):
        bmi = weight/(height*height)
        print("Your BMI is " + str(bmi))
        
    def heart_rate(heart_rates):
        if(heart_rate>60 and heart_rate<100):
            print("Normal heart rate")
            
        elif(heart_rate>60):
            print("Low heart rate")
            
        elif(heart_rate<100):
            print("High heart rate")
            
 class Patient(Doctor):
     def __init__(self, name, weight, height, heart_rates):
         self.paitent_name=name
         self.paitent_weight=weight
         self.paitent_height=height
         self.paitent_heart_rate = heart_rates
         
     def heathCheck(self):
         print("\n Patient Name: ", self.paitent_name)
         Doctor.BMI(self.patient_weight, self.patient_height)
         Doctor.heart_rate(self.patient_heart_rates)
         
         
         


     
            
            
 patient1=Patient("Michael", 30, 0.9144, 80)
 patient1.heathCheck       
 
 patient2=Patient("Jessica", 40, 1, 120)
 patient2.heathCheck       