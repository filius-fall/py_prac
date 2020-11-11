# this code runs at specific intervals of time


names = ["Picard", "Riker", "Troi", "Crusher", "Worf", "Data", "La Forge"]
def interval_function(names_list,modulus=3):
    for index,value in enumerate(names_list,1):
        print(f"{value:-^15}",end="")
        if index%modulus==0:
            print()
    print()
interval_function(names)