from krita import Krita, Extension
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QMenu
import configparser
import os

class RotateCanvasTool(Extension):
    def __init__(self, parent):
        super().__init__(parent)
        self.step = 1.0

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

    def update_config_value(self):
        config_path = os.path.join(os.path.dirname(__file__), 'KritaCanvasRotationToolSettings.ini')
        config = configparser.ConfigParser()

        if not os.path.exists(config_path):
            config['CanvasRotation'] = {'step': str(self.step)}
        else:
            config.read(config_path)
            if 'CanvasRotation' not in config:
                config['CanvasRotation'] = {}

        config['CanvasRotation']['step'] = str(self.step)
        with open(config_path, 'w') as configfile:
            config.write(configfile)

    def read_config_value(self):
        config_path = os.path.join(os.path.dirname(__file__), 'KritaCanvasRotationToolSettings.ini')
        config = configparser.ConfigParser()
        config.read(config_path)

        if 'CanvasRotation' in config and 'step' in config['CanvasRotation']:
            try:
                # 将读取的字符串转换为浮点数
                step_value = float(config['CanvasRotation']['step'])
                return step_value
            except ValueError:
                # 如果转换失败，返回默认值
                return 1.0
        else:
            return 1.0

    def set_rotation_step(self):
        """设置旋转步进"""
        self.step = self.read_config_value()
        step, ok = QInputDialog.getDouble(None, "Set Rotation Step", "Enter rotation step (degrees):", self.step, 0.1, 45.0, 2)
        if ok:
            self.step = step
            self.update_config_value()

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
                canvas.setRotation(current_angle + angle_delta)  # 设置新角度为当前角度减1度

Krita.instance().addExtension(RotateCanvasTool(Krita.instance()))
