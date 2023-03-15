# lesson 2
# changing dimension from assembly

# import libraries
import win32com.client

# create instance for solidworks
sw = win32com.client.Dispatch("SldWorks.Application")

# Define Assembly as active document
AssemblyDoc = sw.ActiveDoc

# Define both dimensions
# dim = AssemblyDoc.Parameter("parameter_name@Sketch_name@Part_name.Part")

# Setting new value for dimensions
# dim.SystemValue = 000


# Rebuild the document
AssemblyDoc.EditRebuild3()



print("Job successfully done.")
