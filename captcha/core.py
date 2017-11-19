import numpy as np
import cv2
import string
import os
from captcha import constant


class Captcha:
    def __init__(self, width, high, letter=None,
                 folder='captcha', debug=False):
        if letter is None:
            letter = string.ascii_uppercase + string.digits
        stop_letter = {'I', 'O', 'Q'}
        self.letter = [i for i in letter if i not in stop_letter]
        self.width, self.high = width, high
        self.debug = debug
        self.folder = folder
        if not self.debug and folder:
            if not os.path.exists(self.folder):
                os.makedirs(self.folder)

    def _tilt_img(self, img, top_left, bottom_right):
        # TODO
        pass

    def _shake_img(self, img, outer_top_left, outer_bottom_right,
                   inner_top_left, inner_bottom_right):
        (x1, y1), (x2, y2) = outer_top_left, outer_bottom_right
        (i1, j1), (i2, j2) = inner_top_left, inner_bottom_right
        delta_x = np.random.randint(x1-i1, x2-i2)
        delta_y = np.random.randint(y1-j1, y2-j2)
        area = img[y1:y2, x1:x2, :]
        area_high, area_width, _ = area.shape
        tmp_area = area.copy()
        tmp_area.fill(255)

        for index_y in range(area_high):
            for index_x in range(area_width):
                new_x, new_y = index_x + delta_x, index_y + delta_y
                if new_x < area_width and new_y < area_high:
                    tmp_area[new_y, new_x, :] = area[index_y, index_x, :]

        for index_y in range(area_high):
            for index_x in range(area_width):
                area[index_y, index_x, :] = tmp_area[index_y, index_x, :]

    def _distort_img(self, img):
        # TODO
        pass

    def _draw_basic(self, img, text):
        font_face = getattr(cv2,  np.random.choice(constant.FONTS))
        font_color = tuple(int(np.random.choice(range(0, 156)))
                           for _ in range(3))
        font_scale = 1
        font_thickness = 2
        (width, high), _ = cv2.getTextSize(
            text, font_face, font_scale, font_thickness)
        bottom_left_coordinate = (
            (self.width-width)//2,
            self.high - (self.high-high)//2
        )
        cv2.putText(img, text, bottom_left_coordinate, font_face, font_scale,
                    font_color, font_thickness)

        # TODO shake and tilt
        top_left = ((self.width-width)//2, (self.high-high)//2)
        bottom_right = ((self.width-width)//2 + width,
                        self.high - (self.high-high)//2)
        self._shake_img(img, (0, 0), (self.width, self.high),
                        top_left, bottom_right)

    def _draw_line(self, img):
        left_x = np.random.randint(0, self.width//4)
        left_y = np.random.randint(self.high)
        right_x = np.random.randint(self.width*3//4, self.width)
        right_y = np.random.randint(self.high)
        start, end = (left_x, left_y), (right_x, right_y)
        line_color = tuple(int(np.random.choice(range(0, 156)))
                           for _ in range(3))
        line_thickness = np.random.randint(1, 3)
        cv2.line(img, start, end, line_color, line_thickness)

    def _put_noise(self, img):
        for i in range(800):
            x = np.random.randint(self.width)
            y = np.random.randint(self.high)
            dot_color = tuple(int(np.random.choice(range(0, 156)))
                              for _ in range(3))
            img[y, x, :] = dot_color

    def save_img(self, text):
        img = np.zeros((self.high, self.width, 3), np.uint8)
        img.fill(255)
        self._draw_basic(img, text)
        self._draw_line(img)
        self._put_noise(img)
        self._distort_img(img)

        if self.debug:
            cv2.imshow("img", img)
            cv2.waitKey(0)
        if not self.debug:
            cv2.imwrite('{}/{}.jpg'.format(self.folder, text), img)

    def batch_create_img(self, number=5):
        exits = set()
        while(len(exits)) <= number:
            word = ''.join(np.random.choice(self.letter, 5))
            if word not in exits:
                exits.add(word)
                self.save_img(word)


if __name__ == '__main__':
    c = Captcha(150, 40, debug=True)
    c.batch_create_img(10)
