def calculate_bmi(height,weight):
    print("Height = "+ str(height))
    print("Weight = "+str(weight))

    bmi = weight/(height*height)
    print("BMI is equal to : " + str(bmi))

    if bmi<18.5:
        print("Under Weight")
    elif bmi<25:
        print("Normal Weight")
    else:
        [print("Over Weight")]


calculate_bmi(weight=57 ,height = 1.73)











'''alternatibe way to use wihtout identifying string

def calculate_bmi(height,weight):
    print("Height = ",height)
    print("Weight = ",weight)

calculate_bmi(weight=57 ,height = 1.73)'''