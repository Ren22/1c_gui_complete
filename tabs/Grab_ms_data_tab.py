from global_vars.global_vars import global_vars
from metaspace import sm_annotation_utils as smau
from PyQt5.QtWidgets import QMessageBox


class GrabMSDataTab():
    def __init__(self, ext_obj):
        global_vars.tab_gms_database = [item.text() for item in ext_obj.tab_gms_lineEditMSDb.selectedItems()]

        ext_obj.tab_gms_lineEditMSLogin.textChanged[str].connect(lambda: self.set_MS_Login(ext_obj))
        ext_obj.tab_gms_lineEditMSPass.textChanged[str].connect(lambda: self.set_MS_password(ext_obj))
        ext_obj.tab_gms_lineEditMSDs.textChanged[str].connect(lambda: self.set_msDsName(ext_obj))
        ext_obj.tab_gms_lineEditMSDb.itemSelectionChanged.connect(lambda: self.set_Db(ext_obj))
        ext_obj.tab_gms_msLoginStatus.setText('Hola. You are NOT authorized!')
        ext_obj.tab_gms_btnMSLogin.clicked.connect(lambda: self.loginMS(ext_obj))
        ext_obj.tab_gms_cbFdr.currentTextChanged.connect(lambda: self.provide_fdr(ext_obj))

    '''Callbacks'''
    @staticmethod
    def provide_fdr(ext_obj):
        mapFdr = {'10%': 0.1, '20%': 0.2, '50%': 0.5}
        global_vars.tab_gms_fdr = mapFdr[ext_obj.tab_gms_cbFdr.currentText()]

    @staticmethod
    def set_Db(ext_obj):
        global_vars.tab_gms_database = [item.text() for item in ext_obj.tab_gms_lineEditMSDb.selectedItems()]

    @staticmethod
    def set_msDsName(ext_obj):
        global_vars.tab_gms_msDSName = ext_obj.tab_gms_lineEditMSDs.text()

    @staticmethod
    def set_MS_Login(ext_obj):
        global_vars.tab_gms_MSLogin = ext_obj.tab_gms_lineEditMSLogin.text()

    @staticmethod
    def set_MS_password(ext_obj):
        global_vars.tab_gms_MSPass = ext_obj.tab_gms_lineEditMSPass.text()

    @staticmethod
    def loginMS(ext_obj):
        sm = smau.SMInstance()
        if sm.login(email=global_vars.tab_gms_MSLogin,
                    password=global_vars.tab_gms_MSPass):
            ext_obj.tab_gms_msLoginStatus.setText('Super. Now you are authorized!')
        else:
            QMessageBox.critical(ext_obj, "Error", "Login or password is incorrect. Make sure you are not using"
                                                   " google account credentials to login. If that is the case, "
                                                   "please set up password for your account on metaspace profile "
                                                   "page instead.")
            Exception('Settings file was not found or does not exist')
            return

    '''Getters'''
    @staticmethod
    def get_MSLogin():
        return global_vars.tab_gms_MSLogin

    @staticmethod
    def get_MSPass():
        return global_vars.tab_gms_MSPass