def stalin_sort(array: list):
    if not len(array):
        return []
    pivot = array[0]
    sorted_array = []
    for element in array:
        print(f'I am {element}')
        try:
            if pivot <= element:
                sorted_array.append(element)
                pivot = element
            else:
                print(f'{element} 🔫 Not in order!')
        except Exception as e:
            print(f'{element} 🔫 Not sortable!')
    return sorted_array


if __name__ == '__main__':
    import random
    randomlist = []
    for i in range(0, 10):
        n = random.randint(1, 30)
        randomlist.append(n)
    print(stalin_sort(randomlist))
