# warmup with selection

#import libraries
import win32com.client
import pythoncom

# python has not Nothing :|
Nothing = win32com.client.VARIANT(pythoncom.VT_DISPATCH, None)


# create instance
sw = win32com.client.Dispatch("SldWorks.Application")

# define model
Model = sw.ActiveDoc
selection_manager = Model.SelectionManager


# select the component
Model.Extension.SelectByID2("example", "FACE", 0, 0, 0, False, 0, Nothing, 0)

# hide component
#Model.HideComponent2

face = selection_manager.GetSelectedObject5
result = Model.Extension.GetSectionProperties2
print(f'Ix is:{result[13]} \nIy is:{result[14]}')
