# https://blog.jonasneubert.com/2019/01/23/barcode-generation-python/

# https://www.ghostscript.com/

# (1) pip install treepoem
#     it will install treepoem 3.3.1 and Pillow 7.0.0

# (2) Install ghostscript    - 32bit


# Another solution is to edit the C:\Users\Windows.UserName\AppData\Local\Programs\Python\Python37\Lib\site-packages\treepoem__init__.py

# the script is looking for gs.exe, change to gswin32.exe as shown below.

# Then add the GhostScriptInstallDir\bin in the PATH in windows.

# def _get_ghostscript_binary():
#     binary = "gswin32c" # changed from 'gs' to 'gswin32c'

#     if sys.platform.startswith("win"):
#         binary = EpsImagePlugin.gs_windows_binary
#         if not binary:
#             raise TreepoemError(
#                 "Cannot determine path to ghostscript, is it installed?"
#             )

#     return binary

#

import treepoem

image = treepoem.generate_barcode(
    barcode_type='qrcode',
    data='barcode payload'
    )

image.convert('1').save('barcode.png')

