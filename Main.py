import math
import json


class Solver():
    """This is the main class that the program uses in order to compute the different calculations.
    Each method of this solver class corresponds to a different geometric calculation and as a result
    takes in different parameters. Each method, returns the corresponding calculated value."""

    def area_of_square(l):
        """
        This method calculates the area of a square given a side length
        :param l:length of one side
        :ptype: float
        :rtype: float
        """
        assert type(l)==float
        return l**2
    
    def area_of_rectangle(l,w):
        """
        This method calculates the area of a rectangle given a length and a width.
        :param l:length ; w:width
        :ptype: float,float
        :rtype: float
        """
        assert type(l)==float
        assert type(w)==float
        return l*w
    
    def area_of_circle(r):
        """
        This method calculates the area of a circle given a radius size
        :param r:radius of the circle
        :ptype: float
        :rtype: float
        """
        assert type(r)==float
        a=r**2
        return math.pi*a
    
    def area_of_triangle(b,h):
        """
        This method calculates the area of a triangle given a base and height
        :param b:length of the base ; h:height of triangle
        :ptype: float,float
        :rtype: float
        """
        assert type(b)==float
        assert type(h)==float
        return 0.5*b*h
    
    def volume_of_cube(l):
        """
        This method calculates the volume of a cube given the length of one side
        :param l:length of one side
        :ptype: float
        :rtype: float
        """
        assert type(l)==float
        return l**3

    def volume_of_rectangular_prism(l,w,h):
        """
        This method calculates the volume of a rectangular prism given its length, width, and height.
        :param l:length ; w:width ; h:height
        :ptype: float,float, float
        :rtype: float
        """
        assert type(l)==float
        assert type(w)==float
        assert type(h)==float
        return l*w*h
    
    def volume_of_sphere(r):
        """
        This method calculates the volume of a sphere given a radius size
        :param r:radius of the sphere
        :ptype: float
        :rtype: float
        """
        assert type(r)==float
        w=r**3
        q=4/3
        return q*math.pi*w
    
    def pythagorean_sides(a, b, c):
        """
        This method calculates the length of the third side of a right triangle given the lengths of the 
        two other sides using the Pythagorean Theorem. 
        :param a,b,c: two of these variables are the lengths of two sides of the right triangle
        and the third is a string "?" which signifies the side that needs to be calculated
        :ptype: float or string
        :rtype: float
        """
        if c=="?":
            w=a**2+b**2
            return math.sqrt(w)
        elif a=="?":
            w=c**2-b**2
            return math.sqrt(w)
        elif b=="?":
            w=c**2-a**2
            return math.sqrt(w)
        
    def find_third_triangle(ang1, ang2):
        """
        This method calculates the third angle in a triangle given the values of the remaining two angles
        :param ang1: value of one of the anlges ; ang2: value of the second angle
        :ptype: float, float
        :rtype: float
        """
        assert type(ang1)==float
        assert type(ang2)==float
        w=ang1+ang2
        return 180-w
    

    def find_comp_angles(list1, list2):
        """
        This method returns a dictionary with every key/value pair being a set of complementary angles where
        the key corresponds to an angle in list1 and the value for that key corresponds to an angle in list2
        :param list1: user inputted list of angles ; list2: user inputted list of angles
        :ptype: list, list
        :rtype: dictionary
        """
        assert type(list1)==list 
        assert type(list2)==list
        comp={}
        for x in list1:
            for y in list2:
                if x+y==90:
                    comp[x]=y
        return comp
    

    def find_sup_angles(list1, list2):
        """
        This method returns a dictionary with every key/value pair being a set of supplementary angles where
        the key corresponds to an angle in list1 and the value for that key corresponds to an angle in list2
        :param list1: user inputted list of angles ; list2: user inputted list of angles
        :ptype: list, list
        :rtype: dictionary
        """
        assert type(list1)==list 
        assert type(list2)==list
        sup={}
        for x in list1:
            for y in list2:
                if x+y==180:
                    sup[x]=y
        return sup


"""
This is the main function that gets called when the code is first run. It sets a local variabel 'running'
to true which ensures the program can run until it is manually terminated through the terminal. Upon starting,
this function displays a range of options for the user to choose from. Once an option is chosen, the corresponding
conditional block is triggered. After taking in the parameters as inputs, the conditional blocks call on the 
methods of the Solver class to make the calculations which are then displayed into the terminal. 
"""
def main():
    running=True
    while running:
        print()
        print("How can I help you?")
        print("-------------------")
        print("1. Area of a Square")
        print("2. Area of a Rectangle")
        print("3. Area of a Circle")
        print("4. Area of a Triangle")
        print("5. Volume of a Cube")
        print("6. Volume of a Rectangular Prism")
        print("7. Volume of a Sphere")
        print("8. Pythagorean Theorem for Sides")
        print("9. Find the Third Angle of a Triangle")
        print("10. Given 2 lists of angles, which are complementary and supplementary")
        print("X. Exit")

        choice=input("Your choice?  ")
        if choice=="X":
            print("Have a good day!")
            running=False
        elif choice=="1":
            length=input("What is the length of one side?  ")
            l=float(length)
            ans=Solver.area_of_square(l)
            print(f"The area of a square with length {length} is {ans}")
        elif choice=="2":
            length=input("What is the length?  ")
            width=input("What is the width?  ")
            l=float(length)
            w=float(width)
            ans=Solver.area_of_rectangle(l,w)
            print(f"The area of a rectangle with length {length} and width {width} is {ans}")
        elif choice=="3":
            radius=input("What is the radius?  ")
            r=float(radius)
            ans=Solver.area_of_circle(r)
            print(f"The area of a circle with radius {radius} is {ans}")
        elif choice=="4":
            base=input("What is the base?  ")
            height=input("What is the height?  ")
            b=float(base)
            h=float(height)
            ans=Solver.area_of_triangle(b,h)
            print(f"The area of a triangle with base {base} and height {height} is {ans}")
        elif choice=="5":
            length=input("What is the length of one side?  ")
            l=float(length)
            ans=Solver.volume_of_cube(l)
            print(f"The volume of a cube with length {length} is {ans}")
        elif choice=="6":
            length=input("What is the length?  ")
            width=input("What is the width?  ")
            height=input("What is the height?  ")
            l=float(length)
            w=float(width)
            h=float(height)
            ans=Solver.volume_of_rectangular_prism(l,w,h)
            print(f"The volume of a rectangular prism with length {length}, width {width}, and height {height} is {ans}")
        elif choice=="7":
            radius=input("What is the radius?  ")
            r=float(radius)
            ans=Solver.volume_of_sphere(r)
            print(f"The volume of a sphere with radius {r} is {ans}")
        elif choice=="8":
            print("Type '?' for the side you want to find")
            a=input("What is the vertical side (a)?  ")
            b=input("What is the horizontal side (b)?  ")
            c=input("What is the hypotenuse (c)?  ")
            if c=="?":
                a=float(a)
                b=float(b)
                g="hypotenuse"
            elif a=="?":
                b=float(b)
                c=float(c)
                g="vertical"
            elif b=="?":
                a=float(a)
                c=float(c)
                g="horizontal"
            ans=Solver.pythagorean_sides(a, b, c)
            print(f"The length of the {g} side is {ans}")
        elif choice=="9":
            ang1=input("What is angle 1?  ")
            ang2=input("What is angle 2?  ")
            ang1=float(ang1)
            ang2=float(ang2)
            ans=Solver.find_third_triangle(ang1, ang2)
            print(f"The third angle of the triangle is {ans}")
        elif choice=="10":
            list1=input("What is the first list of angles?  ")
            list2=input("What is the second list of angles?  ")
            list1=json.loads(list1)
            list2=json.loads(list2)
            ans1=Solver.find_comp_angles(list1, list2)
            ans2=Solver.find_sup_angles(list1, list2)
            print(f"The the sets of complementary angles are {ans1} and the sets of supplementary angles are {ans2}")

if __name__== "__main__":
    main()
