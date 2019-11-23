# extract_yolo_v3_retraining_data_from_video
### Decompose video into individual frames with bounding box output formatted for Yolo v3 retraining.
TODO: ### DOI

Use object tracking software (OpenCV2) to generate yolov3 suitable training images from videos for new object types

- Obtain videos of the objects of interest
- `test` each video
    - Run `python Object_Tracker_for_Video.py test <video_path>`
    - The first video frame is loaded
    - Draw a bounding box around the object of interest
    - Press the spacebar and verify that the bounding box properly follows the object without errors
        - If errors occur, change the `tracker_types` in the script to another type and try again
- `capture` data from each video
    - Run `python object_tracker_for_video.py capture <video_path> <output_path>`
    - Follow the same process as above.
    - With the 'capture' argument, data will be output to the `<output path>`


TODO: OpenCV License Ref:
TODO: Tracking Video code modified from: 
