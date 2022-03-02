import cv2
import numpy as np

class InRangeImage:
    def __init__(self, image, title='image') -> None:
        self.image = image
        self.filted = image.copy()
        self.control_map = {
            'low_r':0,
            'low_g':0,
            'low_b':0,
            'height_r':255,
            'height_g':255,
            'height_b':255,
        }
        self.title = title
        cv2.namedWindow(self.title)
        cv2.createTrackbar(f"Low R {self.control_map['low_r']}", self.title , 0, 255, self.on_low_r_trackbar)
        cv2.createTrackbar(f"Low G {self.control_map['low_g']}", self.title , 0, 255, self.on_low_g_trackbar)
        cv2.createTrackbar(f"Low B {self.control_map['low_b']}", self.title , 0, 255, self.on_low_b_trackbar)
        cv2.createTrackbar(f"Height R {self.control_map['height_r']}", self.title , 0, 255, self.on_height_r_trackbar)
        cv2.createTrackbar(f"Height G {self.control_map['height_g']}", self.title , 0, 255, self.on_height_g_trackbar)
        cv2.createTrackbar(f"Height B {self.control_map['height_b']}", self.title , 0, 255, self.on_height_b_trackbar)
        self.on_low_r_trackbar(0)
        self.on_low_g_trackbar(0)
        self.on_low_b_trackbar(0)
        self.on_height_r_trackbar(255)
        self.on_height_g_trackbar(255)
        self.on_height_b_trackbar(255)
        cv2.setTrackbarPos(f"Height R {self.control_map['height_r']}", self.title, 255)
        cv2.setTrackbarPos(f"Height G {self.control_map['height_g']}", self.title, 255)
        cv2.setTrackbarPos(f"Height B {self.control_map['height_b']}", self.title, 255)

    @staticmethod
    def filted_from_config(image, config):
        lower = np.array([config['low_b'],config['low_g'],config['low_r']])
        upper = np.array([config['height_b'],config['height_g'],config['height_r']])
        rangeImage = cv2.inRange(image.copy(),lower,upper)
        img_mask = (rangeImage//255).astype(bool)
        filted = image.copy()
        filted[img_mask] = 255
        return filted

    def show_inrange(self):
        lower = np.array([self.control_map['low_b'],self.control_map['low_g'],self.control_map['low_r']])
        upper = np.array([self.control_map['height_b'],self.control_map['height_g'],self.control_map['height_r']])
        rangeImage = cv2.inRange(self.image.copy(),lower,upper)
        rangeBGR = cv2.cvtColor(rangeImage, cv2.COLOR_GRAY2BGR)
        img_mask = (rangeImage//255).astype(bool)
        self.filted = self.image.copy()
        self.filted[img_mask] = 255
        cv2.imshow(self.title, np.concatenate([self.filted,rangeBGR],1))

    def on_low_r_trackbar(self, value):
        self.control_map['low_r'] = value
        self.show_inrange()
        
    def on_low_g_trackbar(self, value):
        self.control_map['low_g'] = value
        self.show_inrange()

    def on_low_b_trackbar(self, value):
        self.control_map['low_b'] = value
        self.show_inrange()

    def on_height_r_trackbar(self, value):
        self.control_map['height_r'] = value
        self.show_inrange()

    def on_height_g_trackbar(self, value):
        self.control_map['height_g'] = value
        self.show_inrange()

    def on_height_b_trackbar(self, value):
        self.control_map['height_b'] = value
        self.show_inrange()
        
if __name__ == "__main__":
    img = cv2.imread('/Users/liyue/Desktop/QC/QRCode/土地謄本/0_origin.jpg')
    irimg = InRangeImage(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()