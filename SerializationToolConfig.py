import configparser
import os
from krita import Krita, Extension


class SerializationToolConfig:
    def __init__(self):
        self.__config_path = os.path.join(os.path.dirname(__file__), 'KritaCanvasRotationToolSettings.ini')
        self.__config = configparser.ConfigParser()

        # 配置
        self.step:float = 1.0
        self.coarse_step: float = 15.0
        self.computer_coarse_step: float = 0
        self.smooth_step: float = 0
        self.smoothMOD_step: float = 0
        self.rotate_anim:bool = False
        self.smooth = 0.1

    def read_config_value(self):
        self.__config.read(self.__config_path)

        if 'CanvasRotation' in self.__config:
            section = self.__config['CanvasRotation']
            # 读取 step
            try:
                self.step = float(section.get('step', 1.0))
            except ValueError:
                self.step = 1.0

            # 读取 rotate_anim
            try:
                self.rotate_anim = section.getboolean('rotate_anim', fallback=False)
            except ValueError:
                self.rotate_anim = False
        else:
            self.step = 1.0
            self.rotate_anim = False

    def save_config_to_disk(self):
        self.__config.read(self.__config_path)
        if 'CanvasRotation' not in self.__config:
            self.__config['CanvasRotation'] = {}

        self.__config['CanvasRotation']['step'] = str(self.step)
        self.__config['CanvasRotation']['rotate_anim'] = str(self.rotate_anim)

        with open(self.__config_path, 'w') as configfile:
            self.__config.write(configfile)

    def get_coarse_step(self)->float:
        step = self.__computer_coarse_step()
        self.smoothMOD_step = step % self.smooth
        self.smooth_step = step - (step % self.smooth)

    def get_smoothMOD_step(self):
        step = self.smoothMOD_step
        self.smoothMOD_step = 0
        return step

    def get_smooth_step(self):
        return self.smooth_step

    def __computer_coarse_step(self)->float:
        app = Krita.instance()
        win = app.activeWindow()
        current_angle = 0
        if win is not None:
            view = win.activeView()
            if view is not None:
                canvas = view.canvas()
                current_angle = canvas.rotation()
        angle = current_angle % self.coarse_step
        if angle > 0.0:
            angle = self.coarse_step - angle
        if angle == 0.0:
            angle = self.coarse_step

        self.computer_coarse_step = angle
        return angle


from PyQt5.QtWidgets import QDialog, QVBoxLayout, QDialogButtonBox, QLabel, QDoubleSpinBox, QCheckBox, QSlider, QHBoxLayout
from PyQt5.QtCore import Qt

class RotationSettingDialog(QDialog):
    def __init__(self, config: SerializationToolConfig):
        super().__init__()
        self.setWindowTitle("Set Rotation Setting")

        # 步进值范围：0.1 ~ 5.0
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(50)
        self.slider.setSingleStep(1)
        self.slider.setValue(int(config.step * 10))

        # 动态显示值的标签
        self.label = QLabel(f"{config.step:.1f}°")

        self.slider.valueChanged.connect(self._update_label)
        # 复选框
        self.smooth_checkbox = QCheckBox("Enable Coarse Rotation Animation")
        self.smooth_checkbox.setChecked(config.rotate_anim)

        # 按钮区域
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Set Micro Rotation Step:"))
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.slider)
        hlayout.addWidget(self.label)
        layout.addLayout(hlayout)

        layout.addWidget(self.smooth_checkbox)
        layout.addWidget(buttons)
        self.setLayout(layout)

    def get_values(self):
        step_value = self.slider.value() / 10.0
        return step_value, self.smooth_checkbox.isChecked()

    def _update_label(self, value):
        self.label.setText(f"{value / 10:.1f}°")

