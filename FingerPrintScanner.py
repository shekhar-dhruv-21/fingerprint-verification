from calendar import c
import cv2
import numpy as np
import os

test_original = cv2.imread("./database/2_2.tif") #main file
cv2.imshow("Original", cv2.resize(test_original, None, fx=1, fy=1))
cv2.waitKey(0)
cv2.destroyAllWindows()
result =0.0
for file in [file for file in os.listdir("./database")]:
    
    fingerprint_database_image = cv2.imread("./database/1_2.tif") #test file
    
    sift = cv2.xfeatures2d.SIFT_create()
    
    keypoints_1, descriptors_1 = sift.detectAndCompute(test_original, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_database_image, None)

    matches = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10), 
                dict()).knnMatch(descriptors_1, descriptors_2, k=2)
    match_points = []
    # 1
    for i in range(len(matches)):
      p,q = matches[i]

      if p.distance < 0.1*q.distance:
         match_points.append(p)
    
    # 2
    keypoints = 0
    if len(keypoints_1) <= len(keypoints_2):
      keypoints = len(keypoints_1) 
    else:
      keypoints = len(keypoints_2)
  
    # 3
    if (len(match_points) / keypoints)>0.95:
        print("% match: ", len(match_points) / keypoints * 100)
        print("Figerprint ID: " + str(file))         
        result = cv2.drawMatches(test_original, keypoints_1, fingerprint_database_image, 
                                keypoints_2, match_points, None) 
        result = cv2.resize(result, None, fx=2.5, fy=2.5)
        # cv2.imshow("result", result)
       
        cv2.waitKey(0)
        cv2.destroyAllWindows() 
        print("Finger Print matched!!")     
        break
    

if(match_points == []):
  print("Finger Print Not Matched!! ")
