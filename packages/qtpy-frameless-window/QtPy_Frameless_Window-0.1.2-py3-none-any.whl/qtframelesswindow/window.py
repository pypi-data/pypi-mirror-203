from qtpy.QtCore import Qt, QCoreApplication, QEvent, QPropertyAnimation, QRect
from qtpy.QtGui import QPaintEvent, QPainter, QColor
from qtpy.QtWidgets import QWidget, QVBoxLayout, QMainWindow, QDialog
from .buttons import TitleBar
import math



BORDER = 5


class FramelessWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__background="white"
        self.__radius=5
        self.__setupUi()
        self.__set_frameless()
        self.__set_animation_toggle()

    def __setupUi(self):
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(*([BORDER] * 4))
        self.layout().setSpacing(0)
        self.client_window = QWidget(self)
        self.layout().addWidget(self.client_window)
        self.titlebar = TitleBar(self)
        self.main_window = QWidget(self)
        self.client_window.setLayout(QVBoxLayout())
        self.client_window.layout().setSpacing(0)
        self.client_window.layout().setContentsMargins(0, 0, 0, 0)
        self.client_window.layout().addWidget(self.titlebar)
        self.client_window.layout().addWidget(self.main_window)
        self.resize(400,400)

    def __set_frameless(self):
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        # style sheet
        self.client_window.setObjectName("__window")
        self.set_border_radius(BORDER)
        # resize
        QCoreApplication.instance().installEventFilter(self)

    def set_border_radius(self, radius: int):
        self.__radius=radius
        self.update_stylesheet()
        
    def set_theme(self,theme:str="light",bg_color:str=None):
        if theme=="light":
            self.__background="white" if bg_color is None else bg_color
        else:
            self.__background="#383838" if bg_color is None else bg_color
        self.update_stylesheet()
        self.titlebar.title.set_theme(theme)
        self.titlebar.buttons.set_theme(theme)
        
    def update_stylesheet(self):
        self.setStyleSheet(
            "#__window{background-color:"+str(self.__background)+";border-radius:" + str(self.__radius) + "px;}"
        )

    def eventFilter(self, obj, event):
        # resize, refer to https://github.com/zhiyiYo/PyQt-Frameless-Window
        et = event.type()
        if et != QEvent.MouseButtonPress and et != QEvent.MouseMove:
            return False
        if self.isMaximized():
            return False
        edges = Qt.Edge(0)
        pos = event.globalPos() - self.pos()
        if pos.x() < BORDER:
            edges |= Qt.LeftEdge
        if pos.x() >= self.width() - BORDER:
            edges |= Qt.RightEdge
        if pos.y() < BORDER:
            edges |= Qt.TopEdge
        if pos.y() >= self.height() - BORDER:
            edges |= Qt.BottomEdge
        # change cursor
        if et == QEvent.MouseMove and self.windowState() == Qt.WindowNoState:
            if edges in (Qt.LeftEdge | Qt.TopEdge, Qt.RightEdge | Qt.BottomEdge):
                self.setCursor(Qt.SizeFDiagCursor)
            elif edges in (Qt.RightEdge | Qt.TopEdge, Qt.LeftEdge | Qt.BottomEdge):
                self.setCursor(Qt.SizeBDiagCursor)
            elif edges in (Qt.TopEdge, Qt.BottomEdge):
                self.setCursor(Qt.SizeVerCursor)
            elif edges in (Qt.LeftEdge, Qt.RightEdge):
                self.setCursor(Qt.SizeHorCursor)
            else:
                self.setCursor(Qt.ArrowCursor)
        elif et == QEvent.MouseButtonPress and edges:
            self.window().windowHandle().startSystemResize(edges)
        return False

    def paintEvent(self, event: QPaintEvent) -> None:
        # set shadow , refer to https://blog.csdn.net/goforwardtostep/article/details/99549750
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        shadow = QColor(50, 50, 50, 30)
        for i in range(BORDER):
            shadow.setAlpha(120 - math.sqrt(i) * 40)
            painter.setPen(shadow)
            painter.drawRoundedRect(
                BORDER - i,
                BORDER - i,
                self.width() - (BORDER - i) * 2,
                self.height() - (BORDER - i) * 2,
                4,
                4,
            )

    def __set_animation_toggle(self):
        self.__record:QRect=None
        self.__animation_toggle = QPropertyAnimation(self, b"geometry")
        self.__animation_toggle.setDuration(100)
        
    def show(self) -> None:
        super().show()
        self.__record=self.geometry()
        
    def resize(self,*args,**kwds):
        super().resize(*args,**kwds)

    def showMaximized(self) -> None:
        self.titlebar.show()
        self.layout().setContentsMargins(*([0] * 4))
        self.set_border_radius(0)
        if not self.isVisible():
            self.setGeometry(self.get_screen())
            return
        if self.geometry().height()!=self.get_screen().height() or \
            self.geometry().width()!=self.get_screen().width():
            self.__record=self.geometry()
        self.__animation_toggle.setStartValue(self.geometry())
        self.__animation_toggle.setEndValue(self.get_screen())
        self.__animation_toggle.start()

    def showNormal(self) -> None:
        self.titlebar.show()
        self.layout().setContentsMargins(*([BORDER] * 4))
        self.set_border_radius(BORDER)
        if not self.isVisible():
            super().showNormal()
            self.__record=self.geometry()
        self.__animation_toggle.setStartValue(self.geometry())
        self.__animation_toggle.setEndValue(self.__record)
        self.__animation_toggle.start()
        
    def showFullScreen(self) -> None:
        self.titlebar.hide()
        self.showMaximized()

    def isMaximized(self) -> bool:
        return self.geometry() == self.get_screen()

    def get_screen(self):
        rect = self.screen().availableGeometry()
        rect.setHeight(rect.height() - 2)
        return rect

    def setWindowIcon(self, icon) -> None:
        self.titlebar.icon.setIcon(icon)
        return super().setWindowIcon(icon)

    def setWindowTitle(self, arg__1: str) -> None:
        self.titlebar.title.setText(arg__1)
        return super().setWindowTitle(arg__1)
    
    def setTitlebar(self,titlebar:QWidget):
        self.titlebar.deleteLater()
        self.client_window.layout().replaceWidget(self.titlebar,titlebar)
        self.titlebar=titlebar
    
class FramelessMainWindow(FramelessWindow):
    def __init__(self) -> None:
        super().__init__()
        self.main_window=QMainWindow()
        
class FramelessDialog(FramelessWindow):
    def __init__(self) -> None:
        super().__init__()
        self.main_window=QDialog()
        self.titlebar.buttons.minBtn.hide()
        self.titlebar.buttons.toggleBtn.hide()
        self.titlebar.buttons.setFixedWidth(45)