# One Button PDF Publishing

#import libraries
import win32com.client
import os

# create instance for solidworks application
sw = win32com.client.Dispatch("SldWorks.Application")
Model = sw.ActiveDoc
print("Good, Now you Access to the SolidWork")

# get path of current directory
current_path = os.getcwd()
print("your path is: ", current_path)

# save model as PDF format
saving_path = os.path.join(current_path , "test.PDF")
Model.SaveAs3(saving_path, 0,0)
print("saving your model as PDF format was succesfully done.")
