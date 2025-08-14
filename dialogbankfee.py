# TODO: ************* ERROR ***********

import math

from PySide6.QtWidgets import QDialog, QToolTip
from PySide6.QtGui import QGuiApplication, QRegularExpressionValidator, QCursor
from PySide6.QtCore import QRegularExpression

from UI.ui_dialogbankfee import Ui_DialogBankFee
from num2fawords import words

import DB.bankfee


class DialogBankFee(QDialog):
    # TODO: * بعدا کارمزدها را از پایگاه داده بخوانم

    C2C_FEES = {
        10_000_000: 6000,
        20_000_000: 8400,
        30_000_000: 10800,
        40_000_000: 13200,
        50_000_000: 15600,
        60_000_000: 18000,
        70_000_000: 20400,
        80_000_000: 22800,
        90_000_000: 25200,
        100_000_000: 27600,
        110_000_000: 30000,
        120_000_000: 32400,
        130_000_000: 34800,
        140_000_000: 37200,
        150_000_000: 39600
        }
    PAYA_SAGHF = 25_000  # حداکثر کارمزد پایا

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogBankFee()
        self.ui.setupUi(self)

        # self.sizeHint()
        # ...
        self.clipboard = QGuiApplication.clipboard()
        # ...
        regex = QRegularExpression(r'^\d+$')  # فقط عدد صحیح مثبت بدون حد بالا
        validator = QRegularExpressionValidator(regex)
        self.ui.ledValue.setValidator(validator)
        # ...
        self.connect_signals_to_slots()

    def connect_signals_to_slots(self):
        self.ui.btnCopyCardi.clicked.connect(self.btnCopyCardi_clicked)
        self.ui.btnCopyPaya.clicked.connect(self.btnCopyPaya_clicked)
        self.ui.btnCopySatna.clicked.connect(self.btnCopySatna_clicked)
        # ...
        self.ui.btnBankFeeSettings.clicked.connect(self.btnBankFeeSettings_clicked)
        self.ui.btnOk.clicked.connect(self.btnOk_clicked)
        self.ui.btnCancel.clicked.connect(self.btnCancel_clicked)
        # ...
        self.ui.ledValue.textChanged.connect(self.calculate_fees)  # هنگام تغییر عدد، محاسبه شود

    def btnBankFeeSettings_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageSettings)

    def btnCancel_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageCalculation)

    def btnOk_clicked(self):
        # self.ui.stackedWidget.setCurrentWidget(self.ui.pageCalculation)
        pass

    def btnCopyCardi_clicked(self):
        text = self.ui.ledCardi.text()
        self.copy_text_to_clipboard(text)

    def btnCopyPaya_clicked(self):
        text = self.ui.ledPaya.text()
        self.copy_text_to_clipboard(text)

    def btnCopySatna_clicked(self):
        text = self.ui.ledSatna.text()
        self.copy_text_to_clipboard(text)

    def copy_text_to_clipboard(self, text):
        # هم None هم رشته خالی رو چک می‌کنه
        if not text:
            return
        self.clipboard.setText(text)
        QToolTip.showText(QCursor.pos(), "کپی شد!")

    def calculate_fees(self):
        text = self.ui.ledValue.text()
        if not text:
            self.ui.ledCardi.clear()
            self.ui.ledPaya.clear()
            self.ui.ledSatna.clear()
            self.ui.lblLedValueNum2String.clear()
            self.ui.lblLedValueNum2String.adjustSize()

            return

        try:
            amount = int(text)
            self.ui.lblLedValueNum2String.setText(words(amount) + " ریال")
            self.ui.lblLedValueNum2String.adjustSize()
            self.adjustSize()
        except ValueError:
            self.ui.lblLedValueNum2String.clear()
            self.ui.lblLedValueNum2String.adjustSize()
            return

        self.ui.ledCardi.setText(str(self.calculate_cardi(amount)))
        self.ui.ledPaya.setText(str(self.calculate_paya(amount)))
        self.ui.ledSatna.setText(str(self.calculate_satna(amount)))

    def calculate_cardi(self, value: int) -> int:
        # for limit, fee in self.C2C_FEES.items():
        #     if value <= limit:
        #         return fee
        # return 0

        cfg = self.CARDI_CONFIG

        if value > cfg["max_amount"]:
            return 0  # فراتر از سقف مجاز

        if value <= cfg["base_limit"]:
            return cfg["base_fee"]

        extra = value - cfg["base_limit"]
        steps = math.ceil(extra / cfg["step_unit"])
        fee = cfg["base_fee"] + steps * cfg["step_fee"]
        return min(fee, cfg["max_fee"])

    def calculate_paya(self, value: int) -> int:
        # if value <= 0:
        #     return 0
        # elif value <= 20_000_000:
        #     return 2000
        # elif value <= 500_000_000:
        #     fee = int(value * 0.0001)
        #     return min(fee, self.PAYA_SAGHF)
        # return 0

        if value <= 0 or value > 1_000_000_000:
            return 0  # خارج از محدوده مجاز پایا

        fee = int(value * 0.0001)
        return min(max(fee, 300), 7500)

    def calculate_satna(self, value: int) -> int:
        # if value < 500_000_000:
        #     return 0
        # elif value <= 1_250_000_000:
        #     return int(value * 0.0002)
        # elif value <= 10_000_000_000:
        #     return 250_000
        # return 0

        if value < 500_000_000 or value > 1_250_000_000:
            return 0  # خارج از محدوده مجاز ساتنا

        fee = int(value * 0.0002)
        return min(fee, 350_000)
