def quick_sort(elements):
    """Sort an integer array using selection Algorthim.
    
    >>> selection_sort([10, 2, 1, 2, 4, 5, 7, 9])
    [1, 2, 2, 4, 5, 7, 9, 10]
    """
    if len(elements) < 2:
        return elements

    pivot = elements[-1]
    smaller, equal, larger = list(), list(), list()
    
    for element in elements:
        
        if element < pivot:
            smaller.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            larger.append(element)
    
    return quick_sort(smaller) + equal + quick_sort(larger)