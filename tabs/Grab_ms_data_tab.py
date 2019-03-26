from PyQt5.QtWidgets import *
from global_vars import global_vars
from metaspace import sm_annotation_utils as smau


class GrabMSDataTab():
    def __init__(self, ext_obj):
        ext_obj.tab_gms_lineEditMSLogin.textChanged[str].connect(lambda: self.set_MS_Login(ext_obj))
        ext_obj.tab_gms_lineEditMSPass.textChanged[str].connect(lambda: self.set_MS_password(ext_obj))
        ext_obj.tab_gms_msLoginStatus.setText('Hola. You are NOT authorized!')
        ext_obj.tab_gms_btnMSLogin.clicked.connect(lambda: self.loginMS(ext_obj))

    '''Callbacks'''
    @staticmethod
    def set_MS_Login(ext_obj):
        global_vars.set_MS_login(ext_obj.tab_gms_lineEditMSLogin.text())

    @staticmethod
    def set_MS_password(ext_obj):
        global_vars.set_MS_password(ext_obj.tab_gms_lineEditMSPass.text())

    @staticmethod
    def loginMS(ext_obj):
        sm = smau.SMInstance()
        sm.login(email=global_vars.tab_gms_MSLogin,
                 password=global_vars.tab_gms_MSPass)
        if sm.login_status() == 200:
            ext_obj.tab_gms_msLoginStatus.setText('Super. Now you are authorized!')


    '''Getters'''
    @staticmethod
    def get_MSLogin():
        return global_vars.tab_gms_MSLogin

    @staticmethod
    def get_MSPass():
        return global_vars.tab_gms_MSPass