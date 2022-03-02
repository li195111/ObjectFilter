import json
import os
import sys

import cv2
import imutils
import numpy as np

from inrange_ui import QtCore, QtGui, QtWidgets, Ui_ObjcetFilter


class ObjectFilter:
    def __init__(self) -> None:
        self.app = QtWidgets.QApplication(sys.argv)
        # create window
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ObjcetFilter()
        self.ui.setupUi(self.window)
        self.config_path = ''
        self.control_maps = {}
        self.control_names = []
        self.control_values = []
        self.image = None
        self.resized_image = None
        self.filted_image = None
        self.setupDefaults()

    def get_config(self):
        return {'low_r':self.ui.SliderLR.value(),
                'low_g':self.ui.SliderLG.value(),
                'low_b':self.ui.SliderLB.value(),
                'height_r':self.ui.SliderHR.value(),
                'height_g':self.ui.SliderHG.value(),
                'height_b':self.ui.SliderHB.value()}
    
    def set_config(self, config_name=None):
        if config_name is None:
            config_name = self.current_config_name
        self.ui.ConfigNameInput.setText(config_name)
        config_value = self.control_maps[config_name]
        self.ui.SliderLR.setValue(config_value['low_r'])
        self.ui.SliderLG.setValue(config_value['low_g'])
        self.ui.SliderLB.setValue(config_value['low_b'])
        self.ui.SliderHR.setValue(config_value['height_r'])
        self.ui.SliderHG.setValue(config_value['height_g'])
        self.ui.SliderHB.setValue(config_value['height_b'])
        self.ui.spinBoxLR.setValue(config_value['low_r'])
        self.ui.spinBoxLG.setValue(config_value['low_g'])
        self.ui.spinBoxLB.setValue(config_value['low_b'])
        self.ui.spinBoxHR.setValue(config_value['height_r'])
        self.ui.spinBoxHG.setValue(config_value['height_g'])
        self.ui.spinBoxHB.setValue(config_value['height_b'])
        self.show_inrange()
        
    def enableEditors(self):
        self.ui.NewConfigBtn.setEnabled(True)
        self.ui.ConfigNameInput.setEnabled(True)
        self.ui.RenameConfigBtn.setEnabled(True)
        self.ui.SliderLR.setEnabled(True)
        self.ui.SliderLG.setEnabled(True)
        self.ui.SliderLB.setEnabled(True)
        self.ui.spinBoxLR.setEnabled(True)
        self.ui.spinBoxLG.setEnabled(True)
        self.ui.spinBoxLB.setEnabled(True)
        self.ui.SliderHR.setEnabled(True)
        self.ui.SliderHG.setEnabled(True)
        self.ui.SliderHB.setEnabled(True)
        self.ui.spinBoxHR.setEnabled(True)
        self.ui.spinBoxHG.setEnabled(True)
        self.ui.spinBoxHB.setEnabled(True)
        self.ui.SaveConfigBtn.setEnabled(True)
        self.ui.DeleteConfigBtn.setEnabled(True)
        self.ui.ConfigListView.setEnabled(True)
        
    def disenableEditors(self):
        self.ui.NewConfigBtn.setEnabled(False)
        self.ui.ConfigNameInput.setEnabled(False)
        self.ui.RenameConfigBtn.setEnabled(False)
        self.ui.SliderLR.setEnabled(False)
        self.ui.SliderLG.setEnabled(False)
        self.ui.SliderLB.setEnabled(False)
        self.ui.spinBoxLR.setEnabled(False)
        self.ui.spinBoxLG.setEnabled(False)
        self.ui.spinBoxLB.setEnabled(False)
        self.ui.SliderHR.setEnabled(False)
        self.ui.SliderHG.setEnabled(False)
        self.ui.SliderHB.setEnabled(False)
        self.ui.spinBoxHR.setEnabled(False)
        self.ui.spinBoxHG.setEnabled(False)
        self.ui.spinBoxHB.setEnabled(False)
        self.ui.SaveConfigBtn.setEnabled(False)
        self.ui.DeleteConfigBtn.setEnabled(False)
        self.ui.ConfigListView.setEnabled(False)
        
    def setupDefaults(self):
        self.ui.SliderLR.valueChanged.connect(self.updateLRValue)
        self.ui.SliderLG.valueChanged.connect(self.updateLGValue)
        self.ui.SliderLB.valueChanged.connect(self.updateLBValue)
        self.ui.SliderHR.valueChanged.connect(self.updateHRValue)
        self.ui.SliderHG.valueChanged.connect(self.updateHGValue)
        self.ui.SliderHB.valueChanged.connect(self.updateHBValue)
        
        self.ui.spinBoxLR.valueChanged.connect(self.updateLRValue)
        self.ui.spinBoxLG.valueChanged.connect(self.updateLGValue)
        self.ui.spinBoxLB.valueChanged.connect(self.updateLBValue)
        self.ui.spinBoxHR.valueChanged.connect(self.updateHRValue)
        self.ui.spinBoxHG.valueChanged.connect(self.updateHGValue)
        self.ui.spinBoxHB.valueChanged.connect(self.updateHBValue)
        
        self.ui.LoadFileBtn.clicked.connect(self.loadFile)
        self.ui.RenameConfigBtn.clicked.connect(self.rename_config)
        self.ui.NewConfigBtn.clicked.connect(self.new_config)
        self.ui.SaveConfigBtn.clicked.connect(self.save_config)
        self.ui.DeleteConfigBtn.clicked.connect(self.delete_config)
        self.ui.ConfigListView.clicked.connect(self.selected_config)
        self.ui.ConfigNameInput.setText('new_config_1')
        self.ui.FilePathInput.setText('/Users/liyue/Desktop/QC/QRCode/土地謄本/0_origin.jpg')
        
    def show_inrange(self):
        config = self.get_config()
        lower = np.array([config['low_b'],config['low_g'],config['low_r']])
        upper = np.array([config['height_b'],config['height_g'],config['height_r']])
        rangeImage = cv2.inRange(self.image.copy(),lower,upper)
        rangeBGR = cv2.cvtColor(rangeImage, cv2.COLOR_GRAY2BGR)
        img_mask = (rangeImage//255).astype(bool)
        self.filted_image = self.image.copy()
        self.filted_image[img_mask] = 255
        display = np.concatenate([self.image,self.filted_image,rangeBGR],1)
        self.updateImageArea(self.resize_display(display))
        
    def updateLRValue(self, value):
        self.ui.spinBoxLR.setValue(value)
        self.ui.SliderLR.setValue(value)
        self.show_inrange()

    def updateLGValue(self, value):
        self.ui.spinBoxLG.setValue(value)
        self.ui.SliderLG.setValue(value)
        self.show_inrange()

    def updateLBValue(self, value):
        self.ui.spinBoxLB.setValue(value)
        self.ui.SliderLB.setValue(value)
        self.show_inrange()

    def updateHRValue(self, value):
        self.ui.spinBoxHR.setValue(value)
        self.ui.SliderHR.setValue(value)
        self.show_inrange()

    def updateHGValue(self, value):
        self.ui.spinBoxHG.setValue(value)
        self.ui.SliderHG.setValue(value)
        self.show_inrange()

    def updateHBValue(self, value):
        self.ui.spinBoxHB.setValue(value)
        self.ui.SliderHB.setValue(value)        
        self.show_inrange()

    def updateListView(self):
        self.control_names = list(self.control_maps.keys())
        self.control_values = list(self.control_maps.values())
        slm = QtCore.QStringListModel()
        slm.setStringList(self.control_names)
        self.ui.ConfigListView.setModel(slm)
    
    def updateImageArea(self, image=None):
        if image is None:
            image = self.resized_image
        self.ui.ImageArea.setPixmap(QtGui.QPixmap.fromImage(self.cv2qimage(image)))
        
    def resize_display(self, image):
        area = self.ui.ImageArea.geometry()
        width = area.width()
        height = area.height()
        area_aspect_ratio = width / height
        img_height, img_width = image.shape[:2]
        img_aspect_ratio = img_width / img_height
        inter = cv2.INTER_LANCZOS4
        if area_aspect_ratio > 1:
            if img_aspect_ratio > 1:
                resized_image = imutils.resize(image, width=width, inter=inter)
            else:
                resized_image = imutils.resize(image, height=height, inter=inter)
        else:
            if img_aspect_ratio > 1:
                resized_image = imutils.resize(image, width=width, inter=inter)
            else:
                resized_image = imutils.resize(image, height=height, inter=inter)
        return resized_image
        
    def loadFile(self):
        file_path = self.ui.FilePathInput.text()
        self.image = cv2.imread(file_path)
        if not self.image is None:
            self.resized_image = self.resize_display(self.image)
            self.updateImageArea()
            self.enableEditors()
            
            # Config
            img_dir = os.path.dirname(file_path)
            self.config_path = os.path.join(img_dir,f'config.json')
            if not os.path.exists(self.config_path):
                self.new_config()
                self.control_maps[self.ui.ConfigNameInput.text()] = self.get_config()
                # New Config
                with open(self.config_path, 'w') as fp:
                    json.dump(self.control_maps,fp)
            else:
                # Read Config
                with open(self.config_path, 'r') as fp:
                    self.control_maps = json.load(fp)
                self.updateListView()
                if len(self.control_names) > 0:
                    self.current_config_name = self.control_names[0]
                    self.set_config()
        else:
            self.disenableEditors()

    def init_config(self, config_name):
        self.control_maps[config_name] = {'low_r':0,
                                          'low_g':0,
                                          'low_b':0,
                                          'height_r':255,
                                          'height_g':255,
                                          'height_b':255}

    def new_config(self):
        idx = len(self.control_names)+1
        config_name = f'new_config_{idx}'
        while config_name in self.control_maps:
            idx += 1
            config_name = f'new_config_{idx}'
        self.current_config_name = config_name
        self.init_config(self.current_config_name)
        self.updateListView()
        self.set_config()

    def save_config(self):
        if self.config_path:
            config_name = self.ui.ConfigNameInput.text()
            self.control_maps[config_name] = self.get_config()
            with open(self.config_path, 'w') as fp:
                json.dump(self.control_maps, fp)
        self.updateListView()

    def rename_config(self):
        config_name = self.ui.ConfigNameInput.text()
        config = self.control_maps[self.current_config_name]
        if self.current_config_name in self.control_maps:
            self.control_maps.pop(self.current_config_name)
        self.control_maps[config_name] = config
        self.current_config_name = config_name
        self.updateListView()
        self.set_config()

    def delete_config(self):
        config_name = self.ui.ConfigNameInput.text()
        if config_name in self.control_maps:
            self.control_maps.pop(config_name)
        self.updateListView()
        if len(self.control_names) > 0:
            self.current_config_name = self.control_names[0]
            self.set_config()
        
    def selected_config(self, qModelIndex:QtCore.QModelIndex):
        self.current_config_name = self.control_names[qModelIndex.row()]
        self.set_config()

    def cv2qimage(self, cv_img):
        height, width = cv_img.shape[:2]
        bytesPerLine = 3 * width
        return QtGui.QImage(cv_img.data, width, height, bytesPerLine, QtGui.QImage.Format.Format_BGR888)

    def start(self):
        self.window.show()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    objfilter = ObjectFilter()
    objfilter.start()
