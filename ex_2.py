lenght = float(input("Input the lenght of the room: "))
width = float(input("Input the width of the room: "))

square = lenght*width
cost = float(input("The room is "+str(square) + " m2." +
             " Now input the cost of tile EUR/m2: "))
total_cost = square*cost
print("The total cost is "+str(total_cost)+" EUR")
