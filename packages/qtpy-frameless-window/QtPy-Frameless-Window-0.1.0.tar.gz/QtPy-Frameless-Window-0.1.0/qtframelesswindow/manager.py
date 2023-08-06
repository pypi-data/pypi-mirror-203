from enum import Enum
from qtpy.QtCore import QFile
from qtpy.QtGui import QIcon
from qtpy.QtWidgets import QWidget,QAbstractButton
from .resource import resource

class Theme(Enum):
    DARK="dark"
    LIGHT="light"
    
style_mapdict={
    "--R":255,
    "--G":255,
    "--B":255,
}
    
class ResourceManager(Enum):
    
    def path(self,theme:Theme):
        raise NotImplementedError
    
    def get(self,theme:Theme):
        raise NotImplementedError
    
    def set(self,obj:QWidget,theme:Theme=Theme.LIGHT):
        raise NotImplementedError
    
class StyleManager(ResourceManager):
    BUTTON="button"
    BUTTON_CLOSE="button_close"
    
    
    def path(self,theme:Theme):
        return f":/qtframelesswindow/qss/{self.value}.qss"
    
    def get(self, theme: Theme):
        f=QFile(self.path(theme))
        f.open(QFile.OpenModeFlag.ReadOnly)
        content=str(f.readAll(),encoding="utf-8")
        f.close()
        for k,v in style_mapdict.items():
            content=content.replace(k,str(v))
        return content
    
    def set(self,obj:QWidget,theme:Theme=Theme.LIGHT):
        obj.setStyleSheet(self.get(theme))
        
    
class IconManager(ResourceManager):
    CLOSE="close"
    MAXIMIZE="maximize"
    MINIMIZE="minimize"
    NORMALIZE="normalize"
    
    def path(self,theme:Theme):
        dir_name="black" if theme==Theme.LIGHT else "white"
        return f":/qtframelesswindow/images/{dir_name}/{self.value}.svg"
    
    def get(self, theme: Theme):
        return QIcon(self.path(theme))
    
    def set(self, obj: QWidget, theme: Theme=Theme.LIGHT):
        if isinstance(obj,QAbstractButton):
            obj.setIcon(self.get(theme))