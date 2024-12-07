grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
medium_gr =  (sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4]))
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_stud_list = sorted(students)
class_journal = {sorted_stud_list[0]: medium_gr[0], sorted_stud_list[1]: medium_gr[1], sorted_stud_list[2]: medium_gr[2], sorted_stud_list[3]: medium_gr[3], sorted_stud_list[4]: medium_gr[4]}
print(class_journal)