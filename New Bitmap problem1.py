#define values
cleaning_rate=60
cavity_filling=200
x_ray=100
disc1=0.05
disc2=0.1
tax_rate=0.15

#take inputs 
name=input(" name of the patient is:")
cleaning= input(" cleaning process done ? (y/n)")
cavity=input("cavity filling finished ? (y/n)")
xray=input(" X ray done ?(y/n)")


#defining the function
def calculate(name, cleaning, cavity, xray):
    print("name of the patient is :",name) 
    total=0
    
    if(cleaning=="y"):
        total=total+cleaning_rate
        print("the cleaning finished")
    else:
        print("cleaning not done")
    
    if(cavity=="y"):
        total=total+cavity_filling
        print("the cavity filling processed")
    else:
        print("cavity feeling was not processed ")
        
    if(xray=="y"):
        total=total+x_ray
        print("x ray has been  performed")
    else:
        print(" x ray has been notperformed ")
        
    # print("patients name :",name)    
    
    #tax calcualtion
    tax=total*tax_rate
    total=total+tax
    print("total taxes : ",tax)
    
    #to get discount 
  
    if(total>200):
        total=total-disc1
        print("discount was 5 percent")
    elif(total>300):
        total=total-disc2
        print("discount was 10 percent")
        
    print(" now you can see your total bill :",total)
        
    # taking the inputs 
    # name=input("name of patient :")
    # cleaning= input("cleaning done ?")
    # cavity=input(" cavity filling done?")
    # xray=input("was X ray  done?")
    
calculate(name,cleaning,cavity,xray)