fire_cells = input().split("#")
amount_of_water = int(input())
total_fire = 0
print("Cells:")
for check in range(len(fire_cells)):
    my_list = fire_cells[check].split(" = ")
    type_of_fire = my_list[0]
    cell = my_list[1]
    cell = int(cell)
    valid_cell = False
    if amount_of_water >= total_fire + cell:
        if type_of_fire == "Low" and 1 <= cell <= 50:
            total_fire += cell
            valid_cell = True
        elif type_of_fire == "Medium" and 51 <= cell <= 80:
            total_fire += cell
            valid_cell = True
        elif type_of_fire == "High" and 81 <= cell <= 125:
            total_fire += cell
            valid_cell = True
        if valid_cell:
            print(f" - {cell}")

effort = float(total_fire * 0.25)
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
