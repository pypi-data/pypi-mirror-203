from qtpy.QtGui import QPaintEvent,QMouseEvent,QColor,QFont
from qtpy.QtWidgets import QPushButton,QWidget,QHBoxLayout,QLabel,QSizePolicy
from .manager import StyleManager,IconManager,style_mapdict
from typing import List

BTN_H=30
BTN_W=45

class WindowButton(QPushButton):
    def __init__(self,parent,theme:str="light"):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Policy.Preferred,QSizePolicy.Policy.Preferred)
        self.style_manager=StyleManager.BUTTON
        self.set_theme(theme)
        
    def set_theme(self,theme:str="light"):
        self.theme=theme
        self.style_manager.set(self,theme)
        
class MinimizeButton(WindowButton):
    def __init__(self, parent, theme:str="light"):
        self.icon_manager=IconManager.MINIMIZE
        super().__init__(parent, theme)
        self.clicked.connect(self.window().showMinimized)
        
    def set_theme(self, theme:str="light"):
        self.icon_manager.set(self,theme)
        return super().set_theme(theme)
    
class CloseButton(WindowButton):
    def __init__(self, parent, theme:str="light"):
        self.icon_manager=IconManager.CLOSE
        super().__init__(parent, theme)
        self.style_manager=StyleManager.BUTTON_CLOSE
        self.style_manager.set(self,theme)
        self.clicked.connect(self.window().close)
    def set_theme(self, theme:str="light"):
        self.icon_manager.set(self,theme)
        return super().set_theme(theme)
    
class ToggleButton(WindowButton):
    def __init__(self, parent, theme:str="light"):
        super().__init__(parent, theme)
        self.icon_manager={
            "max":IconManager.MAXIMIZE,
            "normal":IconManager.NORMALIZE
        }
        self.clicked.connect(self.__toggle)
        
    def __toggle(self):
        if self.window().isMaximized():
            self.window().showNormal()
        else:
            self.window().showMaximized()
    
    def paintEvent(self, arg__1: QPaintEvent) -> None:
        self.icon_manager["normal" if self.window().isMaximized() else "max"].set(self,self.theme)
        return super().paintEvent(arg__1)
    
class WindowIcon(WindowButton):
    def __init__(self, parent, theme:str="light"):
        super().__init__(parent, theme)
        self.icon_manager=IconManager.CLOSE
        self.icon_manager.set(self)
           
    def mouseMoveEvent(self, arg__1: QMouseEvent) -> None:
        self.window().windowHandle().startSystemMove()
        return super().mouseMoveEvent(arg__1)
    
    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        if self.window().isMaximized():
            self.window().showNormal()
        else:
            self.window().showMaximized()
        return super().mouseDoubleClickEvent(event)
    
class WindowButtons(QWidget):
    def __init__(self, parent=None,theme:str="light") -> None:
        super().__init__(parent)
        self.setupUi()
        self.setFixedWidth(BTN_W*3)
        
    def setupUi(self):
        self.setLayout(QHBoxLayout())
        self.layout().setContentsMargins(0,0,0,0)
        self.layout().setSpacing(0)
        self.minBtn=MinimizeButton(self)
        self.toggleBtn=ToggleButton(self)
        self.closeBtn=CloseButton(self)
        self.layout().addWidget(self.minBtn)
        self.layout().addWidget(self.toggleBtn)
        self.layout().addWidget(self.closeBtn)
        
    def set_theme(self,theme:str="light"):
        self.minBtn.set_theme(theme)
        self.toggleBtn.set_theme(theme)
        self.closeBtn.set_theme(theme)
        
    def set_color(self,color:QColor):
        style_mapdict["--R"]=color.red()
        style_mapdict["--G"]=color.blue()
        style_mapdict["--B"]=color.green()
        btns:List=[self.minBtn,self.toggleBtn,self.closeBtn]
        for btn in btns:            
            btn.style_manager.set(btn,btn.theme)
            
class WindowIcon(QPushButton):
    def __init__(self,parent):
        super().__init__(parent)
        self.setFixedSize(BTN_H,BTN_H)
        self.setStyleSheet("border:none;background:transparent;")
        
    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        if self.window().isMaximized():
            self.window().showNormal()
        else:
            self.window().showMaximized()
        return super().mouseDoubleClickEvent(event)
    
    def mouseMoveEvent(self, arg__1: QMouseEvent) -> None:
        self.window().windowHandle().startSystemMove()
        return super().mouseMoveEvent(arg__1)
    
class WindowTitle(QLabel):
    def __init__(self,parent):
        super().__init__(parent)
        self.setFont(QFont("Segoe UI",10))
        # self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setSizePolicy(QSizePolicy.Policy.Ignored,QSizePolicy.Policy.Fixed)
        
    def set_theme(self,theme:str="light"):
        if theme=="light":
            self.setStyleSheet("color:black;")
        else:
            self.setStyleSheet("color:white")
        
    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        if self.window().isMaximized():
            self.window().showNormal()
        else:
            self.window().showMaximized()
        return super().mouseDoubleClickEvent(event)
    
    def mouseMoveEvent(self, arg__1: QMouseEvent) -> None:
        self.window().windowHandle().startSystemMove()
        return super().mouseMoveEvent(arg__1)

class TitleBar(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.__layout=QHBoxLayout()
        self.__layout.setContentsMargins(0,0,0,0)
        self.__layout.setSpacing(0)
        self.buttons=WindowButtons(self)
        self.icon=WindowIcon(self)
        self.title=WindowTitle(self)
        self.__layout.addWidget(self.icon)
        self.__layout.addWidget(self.title)
        self.__layout.addWidget(self.buttons)
        self.setLayout(self.__layout)
        self.setFixedHeight(BTN_H)
        