from math import inf
def divide(first, second):
    try:
        result = first/second
        return result
    except Exception as e:
        if isinstance(e, ZeroDivisionError):
            result = inf
            return result


