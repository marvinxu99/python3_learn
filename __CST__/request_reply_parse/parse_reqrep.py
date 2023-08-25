# Pyhtonic way of file handling
'''
Path is a class that represents concrete paths to physical files in your computer. 
Calling .open() on a Path object that points to a physical file opens it just like 
open() would do. So, Path.open() works similarly to open(), but the file path is 
automatically provided by the Path object you call the method on.

Since pathlib provides an elegant, straightforward, and Pythonic way to manipulate 
file system paths, you should consider using Path.open() in your with statements 
as a best practice in Python.

'''
import pathlib
import logging

file_input = pathlib.Path("requestreply.txt")
file_output = pathlib.Path("output.txt")

step_ids = set()

request_tbl = {
    
    
}

# Parse the requestreply.txt
try:
    with file_input.open(mode="r") as f_inp:      
        for line in f_inp:
            if "<stepid>" in line:
                step_id = line.replace("<stepid>", "").replace("</stepid>", "")
                step_ids.add(step_id)

except OSError as error:
        logging.error("Reading file %s failed due to: %s", file_input, error)


# Write results into output.txt
try:
    with file_output.open(mode="w") as f_out:
        out_list = list(set(step_ids))
        if len(out_list) > 0:
            for stepid in out_list:
                f_out.write(stepid)
        else:
            f_out.write("No stepid found in the file.")
            
except OSError as error:
        logging.error("Writing to file %s failed due to: %s", file_output, error)

