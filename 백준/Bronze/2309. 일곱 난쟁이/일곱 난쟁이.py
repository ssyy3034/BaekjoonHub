dwarf_list = []
for i in range(9):
    dwarf_list.append(int(input()))
total_height = sum(dwarf_list)
fakeDwarf1, fakeDwarf2 = 0,0
for i in range(9):
    for j in range(i+1, 9):
        if total_height - (dwarf_list[i]+ dwarf_list[j]) == 100:
            fakeDwarf1 = dwarf_list[i]
            fakeDwarf2 = dwarf_list[j]
            break
        if fakeDwarf1:
            break
dwarf_list.remove(fakeDwarf1)
dwarf_list.remove(fakeDwarf2)
dwarf_list.sort()
for height in dwarf_list:
    print(height)
