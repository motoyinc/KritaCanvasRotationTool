from krita import Krita, Extension

class RotateCanvasTool(Extension):
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action_cw = window.createAction(
            "canvasRotateCW",
            "Rotate Canvas Clockwise",
            "tools/scripts"
        )
        action_cw.triggered.connect(self.rotate_canvas_clockwise)
        action_ccw = window.createAction(
            "canvasRotateCCW",
            "Rotate Canvas CounterClockwise",
            "tools/scripts"
        )
        action_ccw.triggered.connect(self.rotate_canvas_counterclockwise)

    def rotate_canvas_clockwise(self):
        """将当前画布顺时针旋转1度"""
        self.rotate_canvas(1)

    def rotate_canvas_counterclockwise(self):
        """将当前画布逆时针旋转1度"""
        self.rotate_canvas(-1)

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
