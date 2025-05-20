from .SerializationToolConfig import SerializationToolConfig
from krita import Krita, Extension
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QMenu

class RotateCanvasTool(Extension):
    def __init__(self, parent):
        super().__init__(parent)
        self.config = SerializationToolConfig()
        self.config.read_config_value()

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
            self.config.save_config_value(step)

    def rotate_canvas_clockwise(self):
        """将当前画布顺时针旋转1度"""
        self.rotate_canvas(self.step)

    def rotate_canvas_counterclockwise(self):
        """将当前画布逆时针旋转1度"""
        self.rotate_canvas(-self.step)

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
