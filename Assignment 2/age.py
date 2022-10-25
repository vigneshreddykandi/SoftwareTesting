
def Ageverification(age):
    if(age <= 18):
        return "You are a child"
    elif(age > 18 and age <= 70):
        return "You are an adult"    
    elif(age > 70):
        return "You are a pensioner"
    
    