def somma(values):
    """
    Args:
        values to sum
    Return:
        sum of values
    """
    count = 0
    for value in values:
        count+=value
    return count


def media(lista):
    """
    Args:
        values for the average
    Return:
        average
    """
    sum = somma(lista)
    if len(lista)==0:
        return 0
    else:
        return sum/len(lista)
