# warm up with Controlling Options
# increase deciaml place by 1


# import libraries
import win32com.client

# create instance
sw = win32com.client.Dispatch("SldWorks.Application")

# define model
model = sw.ActiveDoc

status = model.GetUserPreferenceIntegerValue(24)
print(status)
status = model.SetUserPreferenceIntegerValue(24, status+1)
print(status)
