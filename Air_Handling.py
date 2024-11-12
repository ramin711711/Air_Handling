try:
    print(1/0)
except:
    print("Something went wrong")
 


 

v = [1,2,3,5,3,5,0,'Hello']   
for _ in v:
    try:
        print(f"{10/_:.1f}")
    except:
        print("Error occured")

    


v = [1,2,3,5,3,5,0,'Hello']   
for _ in v:
    try:
        print(f"{10/_:.1f}")
    except:
        pass
    




v = [1,2,3,5,3,5,0,'Hello']   
for _ in v:
    try:
        print(f"{10/_:.1f}")
    except:
        continue
print("Hello")





try:
    a = 10/0
    print(a)
except ZeroDivisionError as V:
    print(f"Error: {str(V)}")
except ValueError as E:
    print(str(E))
else:
    print(f"Final answer is: {a}")
finally:
   print("The execution has ended")