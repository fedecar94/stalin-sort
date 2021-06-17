def stalin_sort(array: list):
    if not len(array):
        return []
    pivot = array[0]
    new_array = []
    for element in array:
        print(f'I am {element}')
        try:
            if pivot <= element:
                new_array.append(element)
                pivot = element
            else:
                print(f'{element} 🔫 Not in order!')
        except Exception as e:
            print(f'{element} 🔫 Not sortable!', e)

    return new_array


if __name__ == '__main__':
    import random

    randomlist = [random.randint(1, 30) for x in range(0, 10)]

    print(randomlist)
    sorted_array = stalin_sort(randomlist)
    print(sorted_array)
