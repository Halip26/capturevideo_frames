import os
import shutil
import sys
import cv2
from datetime import datetime


# Deklarasi kelas FrameCapture
class FrameCapture:

    # menginisialisasi jalur file
    # dan membuat direktori untuk frame yang ditangkap
    def __init__(self, video_path):
        self.directory = 'captured_frames-%s' % datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.video = cv2.VideoCapture(video_path)
        # Jika direktori sudah ada,
        # maka akan dihapus dan direplace dengan direktori baru.
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
        os.mkdir(self.directory)

    # Fungsi untuk menangkap semua frame dari file video
    def capture_frames(self):

        count = 0
        total_frames = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))

        # Mengulang selama masih terdapat frame yang dapat ditangkap
        while True:
            success, image = self.video.read()
            if not success:
                break
            capture = f"{self.directory}/frame%d.jpg" % count
            cv2.imwrite(capture, image)
            count += 1

            # Calculate the percentage completed and print a progress line
            percent_complete = count / total_frames * 100
            print(
                f"Captured {count} frames ({percent_complete:.1f}%)", end="\r")


if __name__ == "__main__":
    file_path = sys.argv[1]
    fc = FrameCapture(file_path)
    fc.capture_frames()
