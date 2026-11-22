#fitting_functions -saved: This PC - OS - Users - lucyl - documents - scripts

def linear(x, m, b): #outputs the line eqn
    return m*x + b

def slope_units(x_units, y_units):
    return y_units.strip("s") + "/" + x_units.strip("s")
    
def print_equation(m, b, y_units, x_units):
    print("y = ", m, slope_units(x_units, y_units), "+", b, y_units)
    
    
