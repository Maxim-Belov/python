# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(unsort_list):

    def min_num(li):

        min_elem = float('inf')
        for elem in li:
            if elem < min_elem:
                min_elem = elem
        return min_elem
    work_list = [x for x in unsort_list]
    sorted_list = []
    while len(work_list):
        for elem in work_list:
            if elem == min_num(work_list):
                sorted_list.append(elem)
                work_list.remove(elem)
    print('Список %s преобразован:\n%s' % (unsort_list, sorted_list))
    return sorted_list


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])