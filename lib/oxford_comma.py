def oxford_comma(items):

    if len(items) == 1:
        return ''.join(items)
    elif len(items) == 2:
        return ' and '.join(items)
    else:
        commas = ', '.join(items[:-1])
        return  f"{commas}, and {items[-1]}"
        
        
    
