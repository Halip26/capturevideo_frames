import os
import shutil
import sys
import cv2


# Deklarasi kelas FrameCapture
class FrameCapture:

    # menginisialisasi jalur file
    # dan membuat direktori untuk frame yang ditangkap
    def __init__(self, file_path):
        self.directory = "captured_frames"
        self.file_path = file_path

        # Jika direktori sudah ada,
        # maka akan dihapus dan direplace dengan direktori baru.
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
        os.mkdir(self.directory)

    # Fungsi untuk menangkap semua frame dari file video
    def capture_frames(self):
        cv2_object = cv2.VideoCapture(self.file_path)

        frame_number = 0
        frame_found = 1

        # Mengulang selama masih terdapat frame yang dapat ditangkap
        while frame_found:
            frame_found, image = cv2_object.read()
            capture = f"{self.directory}/frame{frame_number}.jpg"
            cv2.imwrite(capture, image)

            frame_number += 1


if __name__ == "__main__":
    file_path = sys.argv[1]
    fc = FrameCapture(file_path)
    fc.capture_frames()
