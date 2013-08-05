def truncate(s, size=80, tail='...'):
    s_size = len(s)
    
    if s_size <= size:
        return s

    tail_size = len(tail)
    if tail_size > size:
        return tail[:size]
        
    pos_max = size - len(tail)
    return s[:pos_max] + tail
