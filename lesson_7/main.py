# warm up with Controlling Options
# increase deciaml place by 1


# import libraries
import win32com.client

# create instance
sw = win32com.client.Dispatch("SldWorks.Application")

# define model
model = sw.ActiveDoc

result = model.SetMaterialPropertyName2("", "", "201 Annealed Stainless Steel (SS)")
print(result)
