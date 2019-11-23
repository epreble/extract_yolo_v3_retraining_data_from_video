# extract_yolo_v3_retraining_data_from_video
### Decompose video into individual frames with bounding box output formatted for Yolo v3 retraining.
TODO: ### DOI

Use object tracking software (OpenCV2) to generate yolov3 suitable training images from videos for new object types

- Obtain videos of the objects of interest
- `test` each video
    - Run `python object_track_extract_yolov3.py test <video_path>`
    - The first video frame is loaded
    - Draw a bounding box around the object of interest
    - Press the spacebar and verify that the bounding box properly follows the object without errors
        - If errors occur, change the `tracker_types` in the script to another type and try again
- `capture` data from each video
    - Run `python object_track_extract_yolov3.py capture <video_path> <output_path>`
    - Follow the same process as above.
    - With the 'capture' argument, data will be output to the `<output path>`

### Environment Requirements
- Python 3.7
- OpenCV
    - Install cv2 in python3 via pip install opencv-contrib-python
    - The "contrib" installation expands the install to include all the object tracking packages

### References
Object Tracking Video code modified from Satya Mallick's article on LearnOpenCV here:
https://www.learnopencv.com/object-tracking-using-opencv-cpp-python/
