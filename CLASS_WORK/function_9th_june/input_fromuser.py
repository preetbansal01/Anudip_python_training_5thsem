 # wapp which provide menu to the user to select the 2D figure (circle , rectangle and square) 
 # after selecting the figure user is again asked to provide input of corresponding data for the figure 
 # after input of corresponding data again provide a menu to select the operation (area , perimeter ) nad 
 # as per the data provided by user dislay the result of operation .
 # the stars is repeted again and again unitil user select the option to exit from that figure 
import geometry

while True:
    menu = input("Enter the shape (circle/square/rectangle/exit): ")

    if menu == "circle":
        radius = float(input("Enter radius: "))
        op = input("Enter operation (area/perimeter): ")
        if op == "area":
            print("Area =", geometry.circle_area(radius))
        elif op == "perimeter":
            print("Perimeter =", geometry.circle_perimeter(radius))

    elif menu == "square":
        side = float(input("Enter side: "))
        op = input("Enter operation (area/perimeter): ")
        if op == "area":
            print("Area =", geometry.square_area(side))
        elif op == "perimeter":
            print("Perimeter =", geometry.square_perimeter(side))

    elif menu == "rectangle":
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))
        op = input("Enter operation (area/perimeter): ")
        if op == "area":
            print("Area =", geometry.rectangle_area(length, breadth))
        elif op == "perimeter":
            print("Perimeter =", geometry.rectangle_perimeter(length, breadth))

    elif menu == "exit":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")






