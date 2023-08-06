from fonticon_fa6 import FA6B, FA6R, FA6S
from qtpy.QtWidgets import QPushButton
from superqt.fonticon import icon


def test_FA6S(qtbot):
    btn = QPushButton()
    qtbot.addWidget(btn)
    btn.setIcon(icon(FA6S.spinner))
    btn.show()


def test_FA6B(qtbot):
    btn = QPushButton()
    qtbot.addWidget(btn)
    btn.setIcon(icon(FA6B.accusoft))
    btn.show()


def test_FA6R(qtbot):
    btn = QPushButton()
    qtbot.addWidget(btn)
    btn.setIcon(icon(FA6R.address_book))
    btn.show()
