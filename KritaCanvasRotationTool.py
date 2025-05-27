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
        self.timer_ccw = QTimer()
        self.timer_ccw.setInterval(1)
        self.timer_cw = QTimer()
        self.timer_cw.setInterval(1)
        self.angle_total = 0
        self.timer_cw.timeout.connect(lambda: self.__rotate(self.timer_cw, self.DIR_CW))
        self.timer_ccw.timeout.connect(lambda: self.__rotate(self.timer_ccw, self.DIR_CCW))

    def setup(self):
        pass

    def createActions(self, window):
        # 创建新的菜单
        action = window.createAction("canvasRotationMenu", "Krita Canva Rotation Tool", "tools/scripts")
        menu = QMenu(window.qwindow())
        action.setMenu(menu)

        # 设置旋转属性
        action_set = window.createAction("setRotationSetting", "rotation setting", "")
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
            step, rotate_anim = dialog.get_values()
            self.config.step = step
            self.config.rotate_anim = rotate_anim
            self.config.save_config_to_disk()

    # 微旋转
    def micro_rotation_add(self):
        self.rotate_canvas(self.config.step)

    def micro_rotation_sub(self):
        self.rotate_canvas(-self.config.step)

    # 粗旋转
    DIR_CW = True
    DIR_CCW = False
    def coarse_rotation_sub(self):
        step = self.config.get_coarse_step()
        if not self.config.rotate_anim:
            if self.timer_cw.isActive(): self.timer_cw.stop()
            self.rotate_canvas(-step)
            return
        self.timer_ccw.start()

    def coarse_rotation_add(self):
        step = self.config.get_coarse_step()
        if not self.config.rotate_anim:
            if self.timer_cw.isActive(): self.timer_cw.stop()
            self.rotate_canvas(step)
            return
        self.timer_cw.start()

    def __rotate(self, timer, dir=DIR_CW):
        smoothMOD = self.config.get_smoothMOD_step()
        if timer.isActive():
            if self.angle_total >= self.config.get_smooth_step():
                timer.stop()
                self.angle_total = 0
        if smoothMOD != 0 :
            self.rotate_canvas(smoothMOD)
        if dir == self.DIR_CW :
            self.rotate_canvas(self.config.smooth)
        else:
            self.rotate_canvas(-self.config.smooth)
        self.angle_total += self.config.smooth



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
