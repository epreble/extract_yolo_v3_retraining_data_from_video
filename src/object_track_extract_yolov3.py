# Modified version of https://www.learnopencv.com/object-tracking-using-opencv-cpp-python/
# Install cv2 in python3 via pip install opencv-contrib-python
# the "contrib" part expands the install to include all the object tracking packages

import cv2
import sys

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
print(major_ver, minor_ver, subminor_ver)


def process_args(args):
    mode = 'undefined'
    video_path = 'undefined'
    output_path = 'undefined'

    try:
        mode = args[1]
        print()
        print('mode:', mode)
    except:
        print()
        print('Error')
        print('mode argument missing. <test> or <capture> required as arg0')
        sys.exit()

    if mode == 'test':
        try:
            video_path = args[2]
            print('video_path:', video_path)
        except:
            print()
            print('Error')
            print('video path must be supplied as argument')
            sys.exit()
    elif mode == 'capture':
        try:
            video_path = args[2]
            output_path = args[3]
            print('video_path:', video_path)
            print('output_path:', output_path)
        except:
            print()
            print('Error')
            print('video path and output path must be supplied as arguments')
            sys.exit()

    return mode, video_path, output_path


def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    # print('h:', h)
    # print('w:', w)
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter), r


if __name__ == '__main__':

    # python object_track_extract_yolov3.py test <video_path>
    # python object_track_extract_yolov3.py capture <video_path> <output_path>

    mode, video_path, output_path = process_args(sys.argv)

    print()
    # sys.exit()
    # Set up tracker. Choose type from list.

    tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN']
    tracker_type = tracker_types[1]

    # if int(minor_ver) < 3:
    #     tracker = cv2.Tracker_create(tracker_type)
    # else:
    if tracker_type == 'BOOSTING':
        tracker = cv2.TrackerBoosting_create()
    if tracker_type == 'MIL':
        tracker = cv2.TrackerMIL_create()
    if tracker_type == 'KCF':
        tracker = cv2.TrackerKCF_create()
    if tracker_type == 'TLD':
        tracker = cv2.TrackerTLD_create()
    if tracker_type == 'MEDIANFLOW':
        tracker = cv2.TrackerMedianFlow_create()
    if tracker_type == 'GOTURN':
        tracker = cv2.TrackerGOTURN_create()
    if tracker_type == 'MOSSE':
        tracker = cv2.TrackerMOSSE_create()
    if tracker_type == "CSRT":
        tracker = cv2.TrackerCSRT_create()

    # Read video
    video = cv2.VideoCapture(video_path)

    # Exit if video not opened.
    if not video.isOpened():
        print("Could not open video")
        sys.exit()

    # Read first frame.
    ok, frame = video.read()
    if not ok:
        print('Cannot read video file')
        sys.exit()

    # Define an initial bounding box
    # bbox = (287, 23, 86, 320)
    # bbox = (1393, 1485, 1443, 1535)

    # Uncomment the line below to select a different bounding box
    # (h, w) = frame.shape[:2]
    resize, ratio = ResizeWithAspectRatio(frame, width=500)
    # print('ratio', ratio)
    bbox = cv2.selectROI(resize, False)

    # Initialize tracker with first frame and bounding box
    ok = tracker.init(resize, bbox)

    while True:
        # Read a new frame
        ok, frame = video.read()
        if not ok:
            break
        resize, ratio = ResizeWithAspectRatio(frame, width=500)  # Resize by width OR

        # Start timer
        timer = cv2.getTickCount()

        # Update tracker
        ok, bbox = tracker.update(resize)

        # print(bbox)
        # sys.exit()

        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

        # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(resize, p1, p2, (255, 0, 0), 2, 1)
            # if mode == 'capture':
            #     cv2.imwrite(os.path.join(output_path, '%d.jpg') % count, resize)

        else:
            # Tracking failure
            cv2.putText(resize, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
        # sys.exit()

        # print(frame)

        # Display tracker type on frame
        cv2.putText(resize, tracker_type + " Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

        # Display FPS on frame
        cv2.putText(resize, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

        # Display result
        cv2.imshow("Tracking", resize)

        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27: break