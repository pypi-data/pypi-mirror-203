# -*-coding:utf-8-*-
# 校验app名称是否存在， 存在抛出异常

class AppNameValidator(object):
    def __init__(self, app_name: str):
        self.app_name = app_name

    def validate(self) -> Exception or None:
        pass


