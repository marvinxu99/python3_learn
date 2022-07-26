import tkinter as tk
from tkinter import ttk

def get_element_details(style):
    print('element: %s' % style)
    print('option: %s' % str(s.element_options(style)))
    layout = s.layout(style)
    for elem, elem_dict in layout:
        get_sub_element_details(elem, elem_dict)
    print(layout)

def get_sub_element_details(elem, _dict, depth=1):
    print('%selement: %s' % (''.join(['\t' for i in range(depth)]), elem))
    for key in _dict:
        if key != 'children':
            print('%s%s: %s' % (''.join(['\t' for i in range(depth+1)]), key, _dict[key]))
    print('%soption: %s' % (''.join(['\t' for i in range(depth+1)]), s.element_options(elem)))
    if 'children' in _dict:
        for child, child_dict in _dict['children']:
            get_sub_element_details(child, child_dict, depth+1)

root = tk.Tk()
widget = ttk.Button(root, text='test')
widget.grid(sticky='nesw')

w2 = ttk.Separator(root, orient='horizontal')
w2.grid(sticky='nesw')

style = widget.winfo_class()

style2 = w2.winfo_class()

s = ttk.Style()

print(s.theme_use())
print('normal theme')
get_element_details(style)

# print('\nclam theme')
# s.theme_use('clam')
# get_element_details(style)

print('Tseparator...')
get_element_details(style2)