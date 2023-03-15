# warm up with Controlling Options

# import libraries
import win32com.client


# create instance
sw = win32com.client.Dispatch("SldWorks.Application")

# define model
Model = sw.ActiveDoc

# getting user prefernece value of Background color
#result = sw.GetUserPreferenceIntegerValue(305)
# 3
#result = sw.SetUserPreferenceIntegerValue(305,1)


# disable input dimension value checkbox (usful for running macro)
#result = sw.SetUserPreferenceToggle(10, False)
result = sw.GetUserPreferenceToggle(10)
print(result)
