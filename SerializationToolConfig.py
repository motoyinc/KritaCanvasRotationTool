import configparser
import os

class SerializationToolConfig:
    def __init__(self):
        self.__config_path = os.path.join(os.path.dirname(__file__), 'KritaCanvasRotationToolSettings.ini')
        self.__config = configparser.ConfigParser()

        ## 配置bi
        self.step = 1.0
        self.rotate_anim = False
        # self.smooth = 0.5

    def read_config_value(self):
        self.__config.read(self.__config_path)

        if 'CanvasRotation' in self.__config and 'step' in self.__config['CanvasRotation']:
            try:
                step_value = float(self.__config['CanvasRotation']['step'])
                self.step = step_value
            except ValueError:
                self.step = 1.0
        else:
            self.step = 1.0

    def save_config_to_disk(self):
        if not os.path.exists(self.__config_path):
            self.__config['CanvasRotation'] = {'step': str(self.step)}
        else:
            self.__config.read(self.__config_path)
            if 'CanvasRotation' not in self.__config:
                self.__config['CanvasRotation'] = {}
    
        self.__config['CanvasRotation']['step'] = str(self.step)
        with open(self.__config_path, 'w') as configfile:
            self.__config.write(configfile)
