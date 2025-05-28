from .SerializationToolConfig import SerializationToolConfig, RotationSettingDialog
from krita import Krita, Extension
from PyQt5.QtWidgets import QInputDialog, QMenu, QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer

class RotateCanvasTool(Extension):
    def __init__(self, parent):
        super().__init__(parent)
        self.config = SerializationToolConfig()
        self.config.read_config_value()
        self.angle_total = 0

    def setup(self):
        pass

    def createActions(self, window):
        # 创建新的菜单
        action = window.createAction("canvasRotationMenu", "Krita Canva Rotation Tool", "tools/scripts")
        menu = QMenu(window.qwindow())
        action.setMenu(menu)

        # 设置旋转属性
        action_set = window.createAction("setRotationSetting", "Rotation Setting", "")
        action_set.triggered.connect(self.set_rotation_setting)
        menu.addAction(action_set)

        # 粗旋转
        action_set_step_add = window.createAction("CoarseRotationADD", "Coarse Rotate Canvas +", "")
        action_set_step_add.triggered.connect(self.coarse_rotation_add)
        menu.addAction(action_set_step_add)

        action_set_step_sub = window.createAction("CoarseRotationSUB", "Coarse Rotate Canvas -", "")
        action_set_step_sub.triggered.connect(self.coarse_rotation_sub)
        menu.addAction(action_set_step_sub)

        # 微旋转
        action_cw = window.createAction("MicroRotationADD", "Micro Rotate Canvas +" ,"")
        action_cw.triggered.connect(self.micro_rotation_add)
        menu.addAction(action_cw)

        # 逆时针旋转
        action_ccw = window.createAction("MicroRotationSUB", "Micro Rotate Canvas -", "")
        action_ccw.triggered.connect(self.micro_rotation_sub)
        menu.addAction(action_ccw)

    # 设置旋转属性
    def set_rotation_setting(self):
        dialog = RotationSettingDialog(self.config)
        if dialog.exec_() == QDialog.Accepted:
            step, coarse_step = dialog.get_values()
            self.config.step = step
            self.config.coarse_step = coarse_step
            self.config.save_config_to_disk()

    # 微旋转
    def micro_rotation_add(self):
        self.rotate_canvas(self.config.step)

    def micro_rotation_sub(self):
        self.rotate_canvas(-self.config.step)

    # 粗旋转
    def coarse_rotation_add(self):
        step = self.computer_coarse_step()
        self.rotate_canvas(step)

    def coarse_rotation_sub(self):
        step = self.computer_coarse_step()
        self.rotate_canvas(-step)

    def computer_coarse_step(self)->float:
        app = Krita.instance()
        win = app.activeWindow()
        current_angle:float = 0
        if win is None:
            return 0
        view = win.activeView()
        if view is None:
            return 0
        canvas = view.canvas()
        current_angle = abs(canvas.rotation())
        step_mod:float = current_angle%self.config.coarse_step
        step:float = 0
        if step_mod > 0.0:
            step = self.config.coarse_step - step_mod
        if step_mod == 0.0:
            step = self.config.coarse_step
        return step


    def rotate_canvas(self, angle_delta:float):
        app = Krita.instance()
        win = app.activeWindow()
        if win is not None:
            view = win.activeView()
            if view is not None:
                canvas = view.canvas()
                current_angle = canvas.rotation()
                canvas.setRotation(current_angle + angle_delta)

Krita.instance().addExtension(RotateCanvasTool(Krita.instance()))
