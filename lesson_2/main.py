# lesson 2
# changing dimension from assembly

# import libraries
import win32com.client

# create instance for solidworks
sw = win32com.client.Dispatch("SldWorks.Application")

# Define Assembly as active document
AssemblyDoc = sw.ActiveDoc

# Define both dimensions
dim1 = AssemblyDoc.Parameter("data@Sketch4@Part1.Part")
dim2 = AssemblyDoc.Parameter("data@Sketch1@Part2.Part")

# Setting new value for dimensions
new_value = 0.140
dim1.SystemValue = new_value
dim2.SystemValue = new_value

# Rebuild the document
AssemblyDoc.EditRebuild3()



print("Job successfully done.")
