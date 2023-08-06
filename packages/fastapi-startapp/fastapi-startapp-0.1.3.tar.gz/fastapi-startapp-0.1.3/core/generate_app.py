# -*-coding:utf-8-*-
import os


class GenerateAppManger(object):
    """
    生成app对应的数据
    """
    def __init__(self, app_name: str):
        self.app_name = app_name
        self.root_dir = f'{self.app_name}/'

    def execute(self):
        pass

    def run(self):
        # 创建app文件夹
        self.create_app_root_file_dir()
        # 创建app文件夹下的文件夹
        res = [self.create_file_dir(file_dir_name) for file_dir_name in self.app_file_dir_name_list()]
        return None


    def app_file_name_mappings(self) -> list:
        """
        app文件夹下的文件名称
        :return:
        """
        return ['models', 'middlewares', 'cores']

    def app_file_dir_name_list(self) -> list:
        """
        app文件夹下的文件夹名称
        :return: list
        """
        return [
            'databases',
            'controllers',
            'cores',
        ]

    def create_file(self, file_path: str, file_content) -> None:
        """
        创建文件
        :param file_path: 文件路径
        :param file_content: 文件内容
        :return: None
        """

        with open(file_path, 'w') as f:
            f.write(file_content.strip())
        return None

    def _create_init_file(self, file_path: str) -> None:
        """
        创建文件目录下的初始化文件
        :param file_path: 文件路径
        :return: None
        """
        file_content = str()
        self.create_file(file_path, file_content)
        return None

    def create_file_dir(self, file_name: str) -> None:
        """
        创建文件目录
        :param file_name:
        :return:
        """
        file_path = self.root_dir + '{file_name}'.format(file_name=file_name)
        os.makedirs(file_path)
        init_file_path = file_path + '/__init__.py'
        self._create_init_file(init_file_path)
        return None

    def create_app_root_file_dir(self) -> None:
        """
        创建app文件夹
        :return: None
        """
        self.create_file_dir(self.app_name)
        return None
