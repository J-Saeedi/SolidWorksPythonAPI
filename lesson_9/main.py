# warm up with custom properies
# import libraries
import win32com.client

# create instance for solidworks app
sw = win32com.client.Dispatch("SldWorks.Application")

# define model
model = sw.ActiveDoc

propMgr = model.Extension.CustomPropertyManager("")

result = propMgr.Get("custom revision")
print(result)
