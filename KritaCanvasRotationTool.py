from .SerializationToolConfig import SerializationToolConfig
from krita import Krita, Extension
from PyQt5.QtWidgets import QInputDialog, QMenu
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
        self.smooth = 0.1
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

        # 设置旋转步进
        action_set = window.createAction("rotateCanvasSetStep", "Set Rotation Step", "")
        action_set.triggered.connect(self.set_rotation_step)
        menu.addAction(action_set)

        action_set_step_add = window.createAction("ConfigStepADD", "Config Step +", "")
        action_set_step_add.triggered.connect(self.config_step_add)
        menu.addAction(action_set_step_add)

        action_set_step_sub = window.createAction("ConfigStepSUB", "Config Step -", "")
        action_set_step_sub.triggered.connect(self.config_step_sub)
        menu.addAction(action_set_step_sub)

        action_set_step_reset = window.createAction("ConfigStepReset", "Config Step Reset", "")
        action_set_step_reset.triggered.connect(self.config_step_reset)
        menu.addAction(action_set_step_reset)

        # 顺时针旋转
        action_cw = window.createAction("canvasRotateCW", "Rotate Canvas Clockwise" ,"")
        action_cw.triggered.connect(self.rotate_canvas_clockwise)
        menu.addAction(action_cw)

        # 逆时针旋转
        action_ccw = window.createAction("canvasRotateCCW", "Rotate Canvas CounterClockwise", "")
        action_ccw.triggered.connect(self.rotate_canvas_counterclockwise)
        menu.addAction(action_ccw)

    def set_rotation_step(self):
        """设置旋转步进"""
        step, ok = QInputDialog.getDouble(None, "Set Rotation Step", "Enter rotation step (degrees):", self.config.step, 0.1, 45.0, 2)
        if ok:
            self.config.step = step
            self.config.save_config_to_disk()

    def config_step_sub(self):
        self.adjust_step(increase=False)

    def config_step_add(self):
        self.adjust_step(increase=True)

    def config_step_reset(self):
        self.config.step = 1.0
        self.config.save_config_to_disk()
        self.display_config_step()

    def adjust_step(self, increase=True):
        """调整旋转步进值"""
        step = self.config.step

        if increase:
            if step < 1.0:
                step += 0.05
            elif step < 45.0:
                step += 1.0
            else:
                step = 45.0  # 最大值限制
        else:
            if step > 1.0:
                step -= 1.0
            elif step > 0.05:
                step -= 0.05
            else:
                step = 0.01  # 最小值限制

        # 确保步进值在允许的范围内
        step = max(0.01, min(step, 45.0))
        self.config.step = step
        self.config.save_config_to_disk()
        self.display_config_step()

    def display_config_step(self):
        view = Krita.instance().activeWindow().activeView()
        if view:
            view.showFloatingMessage(f"Step: {self.config.step:.2f}°",QIcon(),2000,0)

    DIR_CW = True
    DIR_CCW = False
    def rotate_canvas_clockwise(self):
        if not self.config.rotate_anim:
            if self.timer_cw.isActive(): self.timer_cw.stop()
            self.rotate_canvas(self.config.step)
            return
        self.timer_cw.start()

    def rotate_canvas_counterclockwise(self):
        if not self.config.rotate_anim:
            if self.timer_cw.isActive(): self.timer_cw.stop()
            self.rotate_canvas(-self.config.step)
            return
        self.timer_ccw.start()

    def __rotate(self, timer, dir=DIR_CW):
        if dir == self.DIR_CW :
            self.rotate_canvas(self.smooth)
        else:
            self.rotate_canvas(-self.smooth)
        self.angle_total += self.smooth
        if timer.isActive():
            if self.angle_total >= self.config.step:
                timer.stop()
                self.angle_total = 0


    def rotate_canvas(self, angle_delta):
        app = Krita.instance()
        win = app.activeWindow()
        if win is not None:
            view = win.activeView()
            if view is not None:
                canvas = view.canvas()
                current_angle = canvas.rotation()
                canvas.setRotation(current_angle + angle_delta)

Krita.instance().addExtension(RotateCanvasTool(Krita.instance()))
