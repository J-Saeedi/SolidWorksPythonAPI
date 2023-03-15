# warmup with selection
# get section properties

#import libraries
import win32com.client
import pythoncom

# python has not Nothing :|
Nothing = win32com.client.VARIANT(pythoncom.VT_DISPATCH, None)

# create instance
sw = win32com.client.Dispatch("SldWorks.Application")

# define model
Model = sw.ActiveDoc

# select the component
Model.Extension.SelectByID2("section", "FACE", 0, 0, 0, False, 0, Nothing, 0)

# get section properties
result = Model.Extension.GetSectionProperties2
print(f'Ix is:{result[13]*1e12} mm^4 \nIy is:{result[14]*1e12} mm^4')

# here is the list of all properties https://help.solidworks.com/2016/english/api/sldworksapi/solidworks.interop.sldworks~solidworks.interop.sldworks.imodeldocextension~getsectionproperties2.html
