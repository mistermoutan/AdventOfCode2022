with open("input.txt") as f:
    lines = f.readlines()
    current_elf_calories = 0
    all_elf_calories = []
    for line in lines:
        if line != "\n":
            current_elf_calories += int(line)
        else:
            all_elf_calories.append(current_elf_calories)
            current_elf_calories = 0
    all_elf_calories.sort() 
    print(sum(all_elf_calories[-3:]))
        
