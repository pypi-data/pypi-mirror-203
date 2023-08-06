# -*- coding: utf-8 -*-
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


def build_temp_file_from_file(file: File) -> NamedTemporaryFile:
    temp_file = NamedTemporaryFile()
    for chunk in file.chunks(1024 * 1024):
        temp_file.write(chunk)
    temp_file.flush()
    return temp_file


class PillowImage:

    def __init__(self, filename: str = None, file: File = None):
        from PIL import Image

        if filename is None:
            self._temp_file = build_temp_file_from_file(file)
            filename = self._temp_file.name

        self.image: Image.Image = Image.open(filename)
        self.image.verify()
        self._filename = filename
        self._image_module = Image

    def get_content_type(self):
        return self._image_module.MIME.get(self.image.format)


# class CV2Video:
#
#     def __init__(self, filename: str = None, file: File = None):
#         import cv2
#
#         if filename is None:
#             self._temp_file = build_temp_file_from_file(file)
#             filename = self._temp_file.name
#
#         self.video = cv2.VideoCapture(filename)
#         self._filename = filename
#         self._cv2 = cv2
#
#     def get_width(self) -> int:
#         return int(self.video.get(self._cv2.CAP_PROP_FRAME_WIDTH))
#
#     def get_height(self) -> int:
#         return int(self.video.get(self._cv2.CAP_PROP_FRAME_HEIGHT))
#
#     def get_fps(self) -> int:
#         return int(self.video.get(self._cv2.CAP_PROP_FPS))
#
#     def get_frame_count(self) -> int:
#         return int(self.video.get(self._cv2.CAP_PROP_FRAME_COUNT))
#
#     def get_duration(self) -> int:
#         fps = self.get_fps()
#         frame_count = self.get_frame_count()
#         return math.ceil(frame_count / fps)
