def truncate(s, size=80, tail='...'):
    """
    >>> truncate('abc'*20, 10, '...')
    'abcabca...'

    >>> truncate ('abc'*20, 2, '...')
    '..'

    >>> truncate('abc'*20, 0, '...')
    ''

    >>> truncate('abc'*20, 60, '...')
    'abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc'

    >>> truncate('abc'*20, 70, '...')
    'abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc'
    
    """
    s_size = len(s)
    
    if s_size <= size:
        return s

    tail_size = len(tail)
    if tail_size > size:
        return tail[:size]
        
    pos_max = size - tail_size
    return s[:pos_max] + tail
