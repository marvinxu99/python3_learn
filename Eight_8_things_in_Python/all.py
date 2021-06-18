
# def valid_rgb(rgb):
#     '''Receives (r, g, b)  tuple, 
#        Checks if each rgb int is within (0, 255) inclusive'''    
#     for val in rgb:
#         if not 0 <= val <= 255:
#             return False
#     return True

# def valid_rgb(rgb):
#     '''Receives (r, g, b)  tuple, 
#        Checks if each rgb int is within (0, 255) inclusive'''    
#     valid = [
#         0 <= val <= 255 for val in rgb 
#     ]
#     return all(valid)

def valid_rgb(rgb):
    '''Receives (r, g, b)  tuple, 
       Checks if each rgb int is within (0, 255) inclusive'''    
    return all([
        0 <= val <= 255 for val in rgb 
    ])

'''
    all(
        condtion(item)
        for item in iterable
    )
'''

if __name__ == "__main__":
    assert valid_rgb((25, 5, 225)) == True
    assert valid_rgb((255, 255, 255)) == True
    assert valid_rgb((290, 100, 200)) == False
    assert valid_rgb((250, 300, 200)) == False
    assert valid_rgb((250, 100, 400)) == False
    print('Passed all tests ...')


