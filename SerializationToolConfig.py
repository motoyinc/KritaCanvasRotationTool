import configparser
import os
from krita import Krita, Extension


class SerializationToolConfig:
    def __init__(self):
        self.__config_path = os.path.join(os.path.dirname(__file__), 'KritaCanvasRotationToolSettings.ini')
        self.__config = configparser.ConfigParser()

        # 配置
        self.step:float = 1.0
        self.coarse_step: int = 5


    def read_config_value(self):
        self.__config.read(self.__config_path)

        if 'CanvasRotation' in self.__config:
            section = self.__config['CanvasRotation']
            # 读取 step
            try:
                self.step = float(section.get('step', 1.0))
            except ValueError:
                self.step = 1.0

            # 读取 coarse_step
            try:
                self.coarse_step = int(section.get('coarse_step', 5))
            except ValueError:
                self.coarse_step = 5
        else:
            self.step = 1.0
            self.coarse_step = 5
        self.save_config_to_disk()

    def save_config_to_disk(self):
        self.__config.read(self.__config_path)
        if 'CanvasRotation' not in self.__config:
            self.__config['CanvasRotation'] = {}

        self.__config['CanvasRotation']['step'] = str(self.step)
        self.__config['CanvasRotation']['coarse_step'] = str(self.coarse_step)

        with open(self.__config_path, 'w') as configfile:
            self.__config.write(configfile)



from PyQt5.QtWidgets import QDialog, QVBoxLayout, QDialogButtonBox, QLabel, QDoubleSpinBox, QCheckBox, QSlider, QHBoxLayout, QComboBox
from PyQt5.QtCore import Qt

class RotationSettingDialog(QDialog):
    def __init__(self, config: SerializationToolConfig):
        super().__init__()
        self.setWindowTitle("Set Rotation Settings")
        self.config = config

        layout = QVBoxLayout()

        # ---- 微调旋转滑动条 ----
        layout.addWidget(QLabel("Set Micro Rotation Step:"))

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(1)     # 0.1°
        self.slider.setMaximum(50)    # 5.0°
        self.slider.setSingleStep(1)
        self.slider.setValue(int(config.step * 10))

        self.label = QLabel(f"{config.step:.1f}°")
        self.slider.valueChanged.connect(self._update_label)

        hlayout1 = QHBoxLayout()
        hlayout1.addWidget(self.slider)
        hlayout1.addWidget(self.label)
        layout.addLayout(hlayout1)

        # ---- 粗调旋转 ComboBox ----
        layout.addWidget(QLabel("Set Coarse Rotation Step:"))

        self.coarse_step_values = [1, 2, 5, 15, 20, 25, 30, 35, 40, 45]
        self.combo = QComboBox()
        for v in self.coarse_step_values:
            self.combo.addItem(f"{v}°")

        if config.coarse_step in self.coarse_step_values:
            index = self.coarse_step_values.index(config.coarse_step)
            self.combo.setCurrentIndex(index)

        layout.addWidget(self.combo)

        # ---- 确认 / 取消 按钮 ----
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.setLayout(layout)

    def _update_label(self, value):
        self.label.setText(f"{value / 10:.1f}°")

    def get_values(self):
        step_value = self.slider.value() / 10.0
        coarse_step_value = self.coarse_step_values[self.combo.currentIndex()]
        return step_value, coarse_step_value
