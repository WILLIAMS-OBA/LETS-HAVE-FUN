def checking_temprature(temperature, character):
    c = 0
    threshold = 50
    if character == "c":
        f = (temperature * 9/5) + 32
        print(f)
    elif character == "f":
        c = (temperature - 32) * 5/9
        print(c)
        
    else: 
        print('invalid character')
   
    if c >= 50 or f >= 150:
        print('Heat Alert')
    else:
        print("Cold advisory")

checking_temprature(50,"c")
