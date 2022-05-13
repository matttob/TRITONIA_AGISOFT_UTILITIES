import Metashape
import sys
import inspect
import numpy as np  
import matplotlib.pyplot as plt

# Define target removed points percentage 
target_percentage = 0.499
# define number of recunc error iteration steps
number_of_err_steps = 10


# loop through all of the available chunks in the model
for chunk in Metashape.app.document.chunks:
    # save text by defining filter syntax
    f = Metashape.PointCloud.Filter()
    # intitialise Reconstruction Uncertainty filter
    f.init(chunk, Metashape.PointCloud.Filter.ReconstructionUncertainty)
    # create numpy array of values of Reconstruction Uncertainty using the min and max value provided by the filter
    re_cunc_iter = np.arange(f.min_value, f.max_value,((f.max_value-f.min_value)/number_of_err_steps))
    
    #initialise list for storing values of the percentage of points selected for each value of Reconstruction Uncertainty
    percent_selecteds =[]
    

    # loop through all values of Reconstruction Uncertainty and store the number of points selected in each case
    for i in re_cunc_iter:
        # select points 
        f.selectPoints(i)
        # compute the number of points selected
        nselected = len([p for p in chunk.point_cloud.points if p.selected])
        # compute percentage of points selected from total number of points in chunk
        percent_selected = nselected / len(chunk.point_cloud.points)
        # create list of percentage selected values
        percent_selecteds.append(percent_selected)
    
    # change list to numpy array
    percent_selecteds = np.array(percent_selecteds)
    # apply same selection criteria to re_cunc_iter array to ensure correct indexing
    re_cunc_iter_less_than_half = re_cunc_iter[percent_selecteds<target_percentage]
    # select only values of percent selected that are less than our target percentage
    percent_selecteds_less_than_half = percent_selecteds[percent_selecteds<target_percentage]
    
    # find absolute difference between percentage of points selected and target percentage
    percent_selected_diff_to_target = abs(percent_selecteds_less_than_half - target_percentage) 
    
    # find index of smallest : closest value to target
    rep_cunc_half_points_selected_ind = np.argmin(percent_selected_diff_to_target)

    # remove points using the re_cunc_iter value with the index defined above
    f.removePoints(re_cunc_iter_less_than_half[rep_cunc_half_points_selected_ind])

    # print(percent_selecteds_less_than_half[rep_cunc_half_points_selected_ind])
    print("Percentage of total points removed based on Reprojection Error = " + str((percent_selecteds_less_than_half[rep_cunc_half_points_selected_ind])*100) + "%")