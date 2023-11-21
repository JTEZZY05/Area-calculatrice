# Function for calculating area of a rectangle
def area_rectangle(l,w):
    area_rec = l*w
    return area_rec

# Function for calculating area of a square
def area_square(s):
    area_squa = s**2
    return area_squa

# Function for calculating area of a triangle
def area_triangle(b,h):
    area_tri = (b*h)/2
    return area_tri

runnit_back = True # controls the while loop.
while runnit_back == True: # Only runs when runnit_back is true, so if flag returns false at any point, code stops.

    area_find = input("What area would you like to find? (square, triangle, rectangle): ")
    if area_find == "square":
        side = float(input("What is the side of your square? "))
        print("The area of your square is", area_square(side))

        cont = input("Would you like to continue? (yes/no) ")
        if cont == "yes":
            print("Ok, let's continue.")
        else:
            print("Understandable, have a nice day.")
            runnit_back = False

    elif area_find == "triangle":
        base = float(input("What is the base of your triangle? "))
        height = float(input("What is the height of your triangle? "))
        print("The area of your triangle is", area_triangle(base,height))

        cont = input("Would you like to continue? (yes/no) ")
        if cont == "yes":
            print("Ok, let's continue.")
        else:
            print("Understandable, have a nice day.")
            runnit_back = False

    elif area_find == "rectangle":
        length = float(input("What is the length of your rectangle? "))
        width = float(input("What is the width of your rectangle? "))
        print("The area of your rectangle is", area_rectangle(length,width))

        cont = input("Would you like to continue? (yes/no) ")
        if cont == "yes":
            print("Ok, let's continue.")
        else:
            print("Understandable, have a nice day.")
            runnit_back = False

    else:
        print("What da hell boi. That ain't one of the options I gave you")
        runnit_back = False
