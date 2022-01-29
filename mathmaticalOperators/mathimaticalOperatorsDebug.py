'''
Created on Jan 28, 2022

@author: ITAUser
'''
def calculations(list):
    print("The sum is:")
    sum = list[0] + list[1] + list[2] + list[3] + list[4]
    print(sum)
    
    print("The average is:")
    average = sum / 5
    print(average) 
    
    print("The range is:")
    diff = list[4] - list[0]
    print(diff)



list = [24, 35, 46, 67, 78]
calculations(list)