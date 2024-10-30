# TODO Напишите функцию find_common_participants
def find_common_participants(first_str, second_str, separator=","):
    first_list = first_str.split(separator)
    second_list = second_str.split(separator)

    common_participants = []

    for first_part in first_list:
        for second_part in second_list:
            if first_part == second_part:
                common_participants.append(first_part)
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_list = find_common_participants(participants_first_group, participants_second_group)
print(common_list)
