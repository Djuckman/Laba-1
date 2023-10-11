numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
nums = [num for num in numbers if num != None]
av = sum(nums) / (len(nums) + 1)
print("Измененный список:", [num if num != None else av for num in numbers])