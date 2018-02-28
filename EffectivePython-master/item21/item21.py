def safe_division(number, divisor, *, ignore_overflow=True,
                  ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


def foo(*args, **kwargs):
    ignore_overflow = kwargs.pop('ignore_overflow', False)
    ignore_zero_div = kwargs.pop('ignore_zero_div', False)
    if kwargs:
        raise TypeError('Unexpected **kwargs: %r' % kwargs)




if __name__ == '__main__':
    safe_division(10, 0, ignore_zero_division=True)
    foo(2, 3, ok='yes', ignore_overflow=False)