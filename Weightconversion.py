import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def convert_weight(weight, from_unit, to_unit):
    units = {
        "kg": 1000,
        "hg": 100,
        "dag": 10,
        "g": 1,
        "dg": 0.1,
        "cg": 0.01,
        "mg": 0.001
    }
    return weight * units[from_unit] / units[to_unit]

def main():
    print("Weight Conversion Program")
    print("-------------------------")
    print("Available units: kg, hg, dag, g, dg, cg, mg")
    from_unit = input("Enter the source unit: ")
    to_unit = input("Enter the target unit: ")
    weight = float(input("Enter the weight: "))

    converted_weight = convert_weight(weight, from_unit, to_unit)
    print("Converted weight: {:.2f} {}".format(converted_weight, to_unit))
    time.sleep(1)

    choice = input('convert again? (y/n)')

    if choice == 'y':
      print('---------------------------------')
      main() 
    elif choice == 'n':
      print('---------------------------------')
      print('exiting...')
      time.sleep(3)
      subprocess.Popen(['python3', './main.py'])
    else:
      print('invalid option, exiting...')
      time.sleep(3)











clear_screen()
main()


