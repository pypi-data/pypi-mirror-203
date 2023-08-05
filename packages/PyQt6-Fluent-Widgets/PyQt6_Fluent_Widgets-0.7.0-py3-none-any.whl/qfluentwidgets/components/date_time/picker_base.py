# coding:utf-8
from typing import Iterable, List

from PyQt6.QtCore import Qt, pyqtSignal, QSize, QRectF, QPoint, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QColor, QPainter, QCursor, QRegion
from PyQt6.QtWidgets import (QApplication, QWidget, QFrame, QVBoxLayout, QHBoxLayout,
                             QGraphicsDropShadowEffect, QSizePolicy, QPushButton, QListWidgetItem)

from ..widgets.cycle_list_widget import CycleListWidget
from ..widgets.button import TransparentToolButton
from ...common.icon import FluentIcon
from ...common.style_sheet import FluentStyleSheet, themeColor, isDarkTheme


class SeparatorWidget(QWidget):
    """ Separator widget """

    def __init__(self, orient: Qt.Orientation, parent=None):
        super().__init__(parent=parent)
        if orient == Qt.Orientation.Horizontal:
            self.setFixedHeight(1)
        else:
            self.setFixedWidth(1)

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        FluentStyleSheet.TIME_PICKER.apply(self)


class ItemMaskWidget(QWidget):
    """ Item mask widget """

    def __init__(self, listWidgets: List[CycleListWidget], parent=None):
        super().__init__(parent=parent)
        self.listWidgets = listWidgets
        self.setFixedHeight(37)
        FluentStyleSheet.TIME_PICKER.apply(self)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.RenderHint.Antialiasing |
                               QPainter.RenderHint.TextAntialiasing)

        # draw background
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(themeColor())
        painter.drawRoundedRect(self.rect().adjusted(4, 0, -3, 0), 5, 5)

        # draw text
        painter.setPen(Qt.GlobalColor.black if isDarkTheme() else Qt.GlobalColor.white)
        painter.setFont(self.font())
        w, h = 0, self.height()
        for i, p in enumerate(self.listWidgets):
            painter.save()

            # draw first item's text
            x = p.itemSize.width()//2 + 4 + self.x()
            item1 = p.itemAt(QPoint(x, self.y() + 6))
            if not item1:
                painter.restore()
                continue

            iw = item1.sizeHint().width()
            y = p.visualItemRect(item1).y()
            painter.translate(w, y - self.y() + 7)
            self._drawText(item1, painter, 0)

            # draw second item's text
            item2 = p.itemAt(self.pos() + QPoint(x, h - 6))
            self._drawText(item2, painter, h)

            painter.restore()
            w += (iw + 8)  # margin: 0 4px;

    def _drawText(self, item: QListWidgetItem, painter: QPainter, y: int):
        align = item.textAlignment()
        w, h = item.sizeHint().width(), item.sizeHint().height()
        if align & Qt.AlignmentFlag.AlignLeft:
            rect = QRectF(15, y, w, h)      # padding-left: 11px
        elif align & Qt.AlignmentFlag.AlignRight:
            rect = QRectF(4, y, w-15, h)    # padding-right: 11px
        elif align & Qt.AlignmentFlag.AlignCenter:
            rect = QRectF(4, y, w, h)

        painter.drawText(rect, align, item.text())


class PickerColumn:
    """ Picker column """

    def __init__(self, name: str, items: list, width: int, align=Qt.AlignmentFlag.AlignLeft):
        self.name = name
        self.items = items
        self.width = width
        self.align = align
        self._value = None   # type: str
        self.isVisible = True

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = str(v)


class PickerBase(QPushButton):
    """ Picker base class """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.columns = []   # type: List[PickerColumn]
        self.columnMap = {}
        self.buttons = []   # type: List[QPushButton]

        self.hBoxLayout = QHBoxLayout(self)

        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.setSizeConstraint(QHBoxLayout.SizeConstraint.SetFixedSize)

        FluentStyleSheet.TIME_PICKER.apply(self)
        self.clicked.connect(self._showPanel)

    def addColumn(self, name: str, items: Iterable, width: int, align=Qt.AlignmentFlag.AlignCenter):
        """ add column

        Parameters
        ----------
        name: str
            the name of column

        items: Iterable
            the items of column

        width: int
            the width of column

        align: Qt.AlignmentFlag
            the text alignment of button
        """
        if name in self.columnMap:
            return

        # create column
        column = PickerColumn(name, list(items), width, align)
        self.columns.append(column)
        self.columnMap[name] = column

        # create button
        button = QPushButton(name, self)
        button.setFixedSize(width, 30)
        button.setObjectName('pickerButton')
        button.setProperty('hasBorder', False)
        button.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        self.hBoxLayout.addWidget(button, 0, Qt.AlignmentFlag.AlignLeft)
        self.buttons.append(button)

        self._setButtonAlignment(button, align)

        # update the style of buttons
        for btn in self.buttons[:-1]:
            btn.setProperty('hasBorder', True)
            btn.setStyle(QApplication.style())

    def _setButtonAlignment(self, button: QPushButton, align=Qt.AlignmentFlag.AlignCenter):
        """ set the text alignment of button """
        if align == Qt.AlignmentFlag.AlignLeft:
            button.setProperty('align', 'left')
        elif align == Qt.AlignmentFlag.AlignRight:
            button.setProperty('align', 'right')
        else:
            button.setProperty('align', 'center')

    def setColumnAlignment(self, index: int, align=Qt.AlignmentFlag.AlignCenter):
        """ set the text alignment of specified column """
        if not 0 <= index < len(self.columns):
            return

        self.columns[index].align = align
        self._setButtonAlignment(self.buttons[index], align)

    def setColumnVisible(self, index: int, isVisible: bool):
        """ set the text alignment of specified column """
        if not 0 <= index < len(self.columns):
            return

        self.columns[index].isVisible = isVisible
        self.buttons[index].setVisible(isVisible)

    def value(self):
        return [c.value for c in self.columns if c.isVisible]

    def setColumnValue(self, index: int, value):
        if not 0 <= index < len(self.columns):
            return

        value = str(value)
        self.columns[index].value = value
        self.buttons[index].setText(value)
        self._setButtonProperty('hasValue', True)

    def setColumn(self, index: int, name: str, items: Iterable, width: int, align=Qt.AlignmentFlag.AlignCenter):
        """ set column

        Parameters
        ----------
        index: int
            the index of column

        name: str
            the name of column

        items: Iterable
            the items of column

        width: int
            the width of column

        align: Qt.AlignmentFlag
            the text alignment of button
        """
        if not 0 <= index < len(self.columns):
            return

        column = self.columns[index]
        self.columnMap.pop(column.name)

        column = PickerColumn(name, items, width, align)
        self.columns[index] = column
        self.columnMap[name] = column

        self.buttons[index].setText(name)
        self.buttons[index].setFixedWidth(width)
        self._setButtonAlignment(self.buttons[index], align)

    def clearColumns(self):
        """ clear columns """
        self.columns.clear()
        self.columnMap.clear()
        while self.buttons:
            btn = self.buttons.pop()
            btn.deleteLater()

    def enterEvent(self, e):
        self._setButtonProperty('enter', True)

    def leaveEvent(self, e):
        self._setButtonProperty('enter', False)

    def mousePressEvent(self, e):
        self._setButtonProperty('pressed', True)
        super().mousePressEvent(e)

    def mouseReleaseEvent(self, e):
        self._setButtonProperty('pressed', False)
        super().mouseReleaseEvent(e)

    def _setButtonProperty(self, name, value):
        """ send event to picker buttons """
        for button in self.buttons:
            button.setProperty(name, value)
            button.setStyle(QApplication.style())

    def _showPanel(self):
        """ show panel """
        panel = PickerPanel(self)
        for column in self.columns:
            if column.isVisible:
                panel.addColumn(column.items, column.width, column.align)

        panel.setValue(self.value())

        panel.confirmed.connect(self._onConfirmed)
        panel.columnValueChanged.connect(
            lambda i, v: self._onColumnValueChanged(panel, i, v))

        panel.exec(self.mapToGlobal(QPoint(0, -37*4)))

    def _onConfirmed(self, value: list):
        for i, v in enumerate(value):
            self.setColumnValue(i, v)

    def _onColumnValueChanged(self, panel, index: int, value: str):
        """ column value changed slot """
        pass


class PickerPanel(QWidget):
    """ picker panel """

    confirmed = pyqtSignal(list)
    columnValueChanged = pyqtSignal(int, str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.itemHeight = 37
        self.listWidgets = []   # type: List[CycleListWidget]

        self.view = QFrame(self)
        self.itemMaskWidget = ItemMaskWidget(self.listWidgets, self)
        self.hSeparatorWidget = SeparatorWidget(Qt.Orientation.Horizontal, self.view)
        self.yesButton = TransparentToolButton(FluentIcon.ACCEPT, self.view)
        self.cancelButton = TransparentToolButton(FluentIcon.CLOSE, self.view)

        self.hBoxLayout = QHBoxLayout(self)
        self.listLayout = QHBoxLayout()
        self.buttonLayout = QHBoxLayout()
        self.vBoxLayout = QVBoxLayout(self.view)

        self.__initWidget()

    def __initWidget(self):
        self.setWindowFlags(Qt.WindowType.Popup | Qt.WindowType.FramelessWindowHint |
                            Qt.WindowType.NoDropShadowWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setShadowEffect()
        self.yesButton.setIconSize(QSize(16, 16))
        self.cancelButton.setIconSize(QSize(13, 13))
        self.yesButton.setFixedHeight(33)
        self.cancelButton.setFixedHeight(33)

        self.hBoxLayout.setContentsMargins(12, 8, 12, 20)
        self.hBoxLayout.addWidget(self.view, 1, Qt.AlignmentFlag.AlignCenter)
        self.hBoxLayout.setSizeConstraint(QHBoxLayout.SizeConstraint.SetMinimumSize)

        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.addLayout(self.listLayout, 1)
        self.vBoxLayout.addWidget(self.hSeparatorWidget)
        self.vBoxLayout.addLayout(self.buttonLayout, 1)
        self.vBoxLayout.setSizeConstraint(QVBoxLayout.SizeConstraint.SetMinimumSize)

        self.buttonLayout.setSpacing(6)
        self.buttonLayout.setContentsMargins(3, 3, 3, 3)
        self.buttonLayout.addWidget(self.yesButton)
        self.buttonLayout.addWidget(self.cancelButton)
        self.yesButton.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.cancelButton.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.yesButton.clicked.connect(self._fadeOut)
        self.yesButton.clicked.connect(
            lambda: self.confirmed.emit(self.value()))
        self.cancelButton.clicked.connect(self._fadeOut)

        self.view.setObjectName('view')
        FluentStyleSheet.TIME_PICKER.apply(self)

    def setShadowEffect(self, blurRadius=30, offset=(0, 8), color=QColor(0, 0, 0, 30)):
        """ add shadow to dialog """
        self.shadowEffect = QGraphicsDropShadowEffect(self.view)
        self.shadowEffect.setBlurRadius(blurRadius)
        self.shadowEffect.setOffset(*offset)
        self.shadowEffect.setColor(color)
        self.view.setGraphicsEffect(None)
        self.view.setGraphicsEffect(self.shadowEffect)

    def addColumn(self, items: Iterable, width: int, align=Qt.AlignmentFlag.AlignCenter):
        """ add one column to view

        Parameters
        ----------
        items: Iterable[Any]
            the items to be added

        width: int
            the width of item

        align: Qt.AlignmentFlag
            the text alignment of item
        """
        if self.listWidgets:
            self.listLayout.addWidget(SeparatorWidget(Qt.Orientation.Vertical))

        w = CycleListWidget(items, QSize(width, self.itemHeight), align, self)
        w.vScrollBar.valueChanged.connect(self.itemMaskWidget.update)

        N = len(self.listWidgets)
        w.currentItemChanged.connect(
            lambda i, n=N: self.columnValueChanged.emit(n, i.text()))

        self.listWidgets.append(w)
        self.listLayout.addWidget(w)

    def resizeEvent(self, e):
        self.itemMaskWidget.resize(self.view.width()-3, self.itemHeight)
        m = self.hBoxLayout.contentsMargins()
        self.itemMaskWidget.move(m.left()+2, m.top() + 148)

    def value(self):
        """ return the value of columns """
        return [i.currentItem().text() for i in self.listWidgets]

    def setValue(self, value: list):
        """ set the value of columns """
        if len(value) != len(self.listWidgets):
            return

        for v, w in zip(value, self.listWidgets):
            w.setSelectedItem(v)

    def columnValue(self, index: int) -> str:
        """ return the value of specified column """
        if not 0 <= index < len(self.listWidgets):
            return

        return self.listWidgets[index].currentItem().text()

    def setColumnValue(self, index: int, value: str):
        """ set the value of specified column """
        if not 0 <= index < len(self.listWidgets):
            return

        self.listWidgets[index].setSelectedItem(value)

    def column(self, index: int):
        """ return the list widget of specified column """
        return self.listWidgets[index]

    def exec(self, pos, ani=True):
        """ show panel

        Parameters
        ----------
        pos: QPoint
            pop-up position

        ani: bool
            Whether to show pop-up animation
        """
        if self.isVisible():
            return

        # show before running animation, or the height calculation will be wrong
        self.show()

        rect = QApplication.screenAt(QCursor.pos()).availableGeometry()
        w, h = self.width() + 5, self.height()
        pos.setX(
            min(pos.x() - self.layout().contentsMargins().left(), rect.right() - w))
        pos.setY(max(rect.top(), min(pos.y() - 4, rect.bottom() - h + 5)))
        self.move(pos)

        if not ani:
            return

        self.isExpanded = False
        self.ani = QPropertyAnimation(self.view, b'windowOpacity', self)
        self.ani.valueChanged.connect(self._onAniValueChanged)
        self.ani.setStartValue(0)
        self.ani.setEndValue(1)
        self.ani.setDuration(150)
        self.ani.setEasingCurve(QEasingCurve.Type.OutQuad)
        self.ani.start()

    def _onAniValueChanged(self, opacity):
        m = self.layout().contentsMargins()
        w = self.view.width() + m.left() + m.right() + 120
        h = self.view.height() + m.top() + m.bottom() + 12
        if not self.isExpanded:
            y = int(h / 2 * (1 - opacity))
            self.setMask(QRegion(0, y, w, h-y*2))
        else:
            y = int(h / 3 * (1 - opacity))
            self.setMask(QRegion(0, y, w, h-y*2))

    def _fadeOut(self):
        self.isExpanded = True
        self.ani = QPropertyAnimation(self, b'windowOpacity', self)
        self.ani.valueChanged.connect(self._onAniValueChanged)
        self.ani.finished.connect(self.deleteLater)
        self.ani.setStartValue(1)
        self.ani.setEndValue(0)
        self.ani.setDuration(150)
        self.ani.setEasingCurve(QEasingCurve.Type.OutQuad)
        self.ani.start()
