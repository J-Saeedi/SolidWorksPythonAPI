# warm up with Controlling Options
# increase deciaml place by 1


# import libraries
import win32com.client

# create instance
sw = win32com.client.Dispatch("SldWorks.Application")

# define model
model = sw.ActiveDoc

#result = model.GetType
#print(result)

# define model types
model_types = {1:'part', 2:'assembly', 3:'drawing'}


# warm up with selection manager

# define selection manager
selectionManager = model.SelectionManager

selected_counts = selectionManager.GetSelectedObjectCount2(-1)
print(selected_counts, "items selected")

if selected_counts > 0:
    # if user was selected some items
    for index in range(1,selected_counts+1):
        this_component = selectionManager.GetSelectedObjectsComponent3(index, -1)
        this_model = this_component.GetModelDoc2
        this_model_name = this_model.GetTitle
        this_model_type = this_model.GetType
        print(f'{this_model_name} is a {model_types[this_model_type]}')
        this_model.SetMaterialPropertyName2("", "", "201 Annealed Stainless Steel (SS)")
