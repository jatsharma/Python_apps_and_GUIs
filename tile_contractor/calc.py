# A tile contractor charges for his work in terms of tiles fitted per square feet,
# example if he charges 20$/square feet means for 100sqft the charges would be $2000
# You want to build a simple calculator for him so that he can quote a final amount to his customer.
#
# Level 1:
# The calculator should have the following features:
# 1. Should accept inputs as the length and breadth of the room to be tiled.
# 2. Should give an option to offer discount in terms of percentage.
# 3. Should give output as total area covered, total discount in terms of $, the total amount customer has to pay.
#
# Level 2:
# 1. Try accepting length values in different units, build a separate function to convert unit from meter to feet.
# 2. Try to make the above calculator in the form of a GUI using Tkinter.
# 3. Try to optimize the code. i.e. Try to use less variables and less redundancies.


# rate per sqft
rate = 20


def calculator(length, breadth):
    area = float(length) * float(breadth)
    print(f"Total area is {area} square feet")
    total_cost = float(area) * float(rate)
    disc = str(input("Do you want to offer discount? Y for yes N for no"))
    if disc == 'y':
        perc = float(input("Please enter discount %"))
        discount = total_cost * (perc / 100)
        print(f"Total discount is ${discount}")
        final_cost = total_cost - discount
        print(f"Final cost of work is ${final_cost}")
    else:
        print(f"Final cost of work is ${total_cost}")


try:
    l = float(input("Please enter length in feet"))
    b = float(input("Please enter breadth in feet"))

    calculator(l, b)
except Exception:
    print("Please enter correct value")
