#vignesh reddy kandi
def triangle(side1,side2,side3):
    if(side1==side2 and side2==side3 and side1==side3):
        return "Equilateral Triangle"
    elif(side1==side2 or side2==side3 or side1==side3):
        return "Isoceles Triangle"   
    elif(side1!=side2 and side2!=side3 and side1!=side3):
        return "Scalene Triangle"
