import os
import sys
py_file_location = "/content/via-line-detect/src"
if os.path.abspath(py_file_location) not in sys.path:
    sys.path.append(os.path.abspath(py_file_location))
#############################################################################################################
##
##  Parameters
##
#############################################################################################################
import numpy as np
import cv2

class Parameters():
    # thay đổi số lượng epoch ở đây
    n_epoch = 30

    l_rate = 0.0001
    weight_decay=1e-5
    save_path = "savefile/"
    # train from scratch.
    model_path = "savefile/"
    batch_size = 16
    x_size = 512
    y_size = 256
    resize_ratio = 8
    grid_x = x_size//resize_ratio  #64
    grid_y = y_size//resize_ratio  #32
    feature_size = 4
    regression_size = 110
    mode = 2
    threshold_point = 0.75 #0.35 #0.5 #0.57 #0.64 #0.35
    threshold_instance = 0.1

    #loss function parameter
    K1 = 1.0                     #  ####################################
    K2 = 2.0
    constant_offset = 0.2
    constant_exist = 1.0 #2.0#1.0    #8
    constant_nonexist = 1.0#3.0
    constant_angle = 1.0
    constant_similarity = 1.0
    constant_attention = 0.1
    constant_alpha = 0.5 #in SGPN paper, they increase this factor by 2 every 5 epochs
    constant_beta = 0.5
    constant_l = 1.0
    constant_lane_loss = 1.0  #10  ######################################
    constant_instance_loss = 1.0

    #data loader parameter
    flip_ratio=0.6
    translation_ratio=0.6
    rotate_ratio=0.6
    noise_ratio=0.6
    intensity_ratio=0.6
    shadow_ratio=0.6
    scaling_ratio=0.2
    flip_indices=[(0,34),(1,35),(2,36),(3,37),(4,38),(5,39),(6,40),(7,41),(8,42),(9,43),(10,44),(11,45),(12,46),(13,47),(14,48),(15,49),(16,50),(17,51)
                    ,(18,52),(19,53),(20,54),(21,55),(22,56),(23,57),(24,58),(25,59),(26,60),(27,61),(28,62),(29,63),(30,64),(31,65)
                    ,(32,66),(33,67),(68,68),(69,69),(70,72),(71,73)]
    
    train_root_url="../dataset/train/"
    train_labels_root="../dataset/train/"

    test_root_url="../dataset/train/"
    test_labels_root="../dataset/train/"
    
    # test parameter
    color = [(0,0,0), (255,0,0), (0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255),(255,255,255),(100,255,0),(100,0,255),(255,100,0),(0,100,255),(255,0,100),(0,255,100)]
    grid_location = np.zeros((grid_y, grid_x, 2))
    for y in range(grid_y):
        for x in range(grid_x):
            grid_location[y][x][0] = x
            grid_location[y][x][1] = y
    num_iter = 30
    threshold_RANSAC = 0.1
    ratio_inliers = 0.1

    # expand

    point_in_lane = 0
    source_points = np.float32([
    [0, y_size],
    [0, (5/9)*y_size],
    [x_size, (5/9)*y_size],
    [x_size, y_size]
    ])
    
    destination_points = np.float32([
    [0 * x_size, y_size],
    [0 * x_size, 0],
    [x_size - (0 * x), 0],
    [x_size - (0 * x), y_size]
    ])
    
    perspective_transform = cv2.getPerspectiveTransform(source_points, destination_points)
    inverse_perspective_transform = cv2.getPerspectiveTransform( destination_points, source_points)