def ASCIIRectangle(width, height, offset=0,bchar='#',filled=False, msg=None):
    # top
    print(' '*offset + bchar*width) 
    # edges/insides
    if isinstance(msg, str):
        printoptions(width, height, offset, bchar, filled, msg=msg)
    elif isinstance(msg, dict):
        printoptions(width, height, offset, bchar, filled, msg=msg['m'], vpos=msg['v'], hpos=msg['h'])
    else:
        printoptions(width, height, offset, bchar, filled)
    # bottom
    print(' '*offset + bchar*width)

def printoptions(width, height, offset, bchar, filled, msg='', vpos='center', hpos='center'):
    assert vpos in ['top', 'center', 'bottom']
    assert hpos in ['top', 'center', 'bottom']

    if width <= len(msg):
        raise Exception("message too long to display inside box")

    padleft = ((width - len(msg)) // 2) - 1 if hpos == 'center' else 0 if hpos == 'top' else (width - len(msg) - 2)
    padright = width - len(msg) - padleft - 2
    padchar = ' ' if not filled else bchar
    for i in range(height-2):
        print(' '*offset + bchar,end='')
        # top
        if vpos == 'top' and i == 0:
            print(padchar*padleft + msg + padchar*padright, end='') 
        # center
        elif vpos == 'center' and i == (height // 2) - 1:
            print(padchar*padleft + msg + padchar*padright,end='') 
        # bottom
        elif vpos == 'bottom' and i == height-2-1:
            print(padchar*padleft + msg + padchar*padright, end='') 
        else:
            print(padchar*(width-2), end='')
        print(bchar)
