#encoding:shift-jis
from __future__ import division, print_function
__metaclass__ = type 

import os.path
from contextlib import contextmanager
from win32com.shell import shell

from sffairmaker.qutil import *
from sffairmaker import const

def appdata_dir():
    CSIDL_APPDATA = 0x1A
    appdata= shell.SHGetSpecialFolderPath(0, CSIDL_APPDATA, 1)
    return appdata

class _Settings(QSettings):
    def __init__(self):
        from os.path import join, expandvars 
        
        s = QSettings(join(os.getcwdu(), "inidir.ini"), QSettings.IniFormat)
        iniPath = join(expandvars(unicode(s.value("iniDir", const.IniDir).toString())), const.IniName)
        QSettings.__init__(self, iniPath, QSettings.IniFormat)
    
    def externalSprEditingCommand(self):
        v = self.value("ExternalSprEditingCommand")
        if v.isValid():
            return unicode(v.toString())
        else:
            return const.DefaultExternalSprEditingCommand
    
    def setExternalSprEditingCommand(self, command):
        self.setValue(
            "ExternalSprEditingCommand", 
            QString(command)
        )
    
    def externalAirEditingCommand(self):
        v = self.value("ExternalAirEditingCommand")
        if v.isValid():
            return unicode(v.toString())
        else:
            return const.DefaultExternalAirEditingCommand
    
    def setExternalAirEditingCommand(self, command):
        self.setValue(
            "ExternalAirEditingCommand", 
            QString(command)
        )
    
    def backupToRecycle(self):
        v = self.value("BackupToRecycle")
        if v.isValid():
            return bool(v.toBool())
        else:
            return True
    
    def setBackupToRecycle(self, v):
        return self.setValue("BackupToRecycle", v)

class Settings(_Settings):
    _instance = None
    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

Settings = Settings.instance


def main():
    app = QApplication([])
    assert Settings() == Settings()
    
    

if "__main__" == __name__:
    main()