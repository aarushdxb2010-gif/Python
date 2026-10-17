class multipleFunctions():
    
    def Subfields():
        print("Sub-fields in AI are:")
        lists = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        for temp in lists:
            print(temp)
            
    def OddEven():
        num = int(input("Enter a number: "))
        if (num % 2 == 0):
            print(f"{num} is Even number")
            return "Even number"
        else:
            print(f"{num} is odd Number")
            return "odd Number"

    def Elegible():
        gender = input("Your Gender:")
        age = int(input("Your Age:"))
        if gender.lower() == 'male' and age >= 21:
            print("ELIGIBLE")
        elif gender.lower() == 'female' and age >= 18:
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def percentage():
        s1 = int(input("Subject1= "))
        s2 = int(input("Subject2= "))
        s3 = int(input("Subject3= "))
        s4 = int(input("Subject4= "))
        s5 = int(input("Subject5= "))
        total = s1 + s2 + s3 + s4 + s5
        percent = total / 5
        print(f"Total : {total}")
        print(f"Percentage : {percent}")
        return percent

    def triangle():
        height = int(input("Height: "))
        breadth = int(input("Breadth: "))
        print(f"Area formula: (Height*Breadth)/2")
        print(f"Area of Triangle: {(height * breadth) / 2}")
        
        h1 = int(input("Height1: "))
        h2 = int(input("Height2: "))
        b1 = int(input("Breadth: "))
        print(f"Perimeter formula: Height1+Height2+Breadth")
        print(f"Perimeter of Triangle: {h1 + h2 + b1}")

    def BMI():
        bmi = int(input("Enter the BMI Index: "))
        if bmi < 18.5:
            print("Underweight")
            return "Underweight"
        elif bmi <= 24.9:
            print("Normal")
            return "Normal"
        elif bmi <= 29.9:
            print("Overweight")
            return "Overweight"
        else:
            print("Very Overweight")
            return "Very Overweight"