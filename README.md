# Capture Video Frames

This Python script captures frames from a video file and saves them as individual images in a newly created directory. It also includes a progress line that calculates the percentage of completed frames and prints it out.

## Installation

To run this script, the following modules need to be installed:

- OpenCV (cv2)
- datetime
- os
- shutil
- sys

## Usage

To use this script, run it using Python in the command line with the video file path as the argument.

``` Python
python frame_capture.py path/to/video/file
```

The script will then create a new directory with the captured frames in the same directory as the script. The directory's name includes the current date and time information.

## Example

```Python
python frame_capture.py videos/sample_video.mp4
```

_This will create a new directory with the captured frames in the same directory as frame_capture.py. The directory will have a name similar to captured_frames-2021-08-18_20-18-05._

## Notes

If the directory already exists, it will be deleted and replaced with a new directory.
To stop the script, press CTRL+C.
