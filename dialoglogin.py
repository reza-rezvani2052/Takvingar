import re

from dialogdraggable import DialogDraggable
from UI.ui_dialoglogin import Ui_DialogLogin

from definitions import Direction, user_info
from DB.database import (add_user_to_db, get_pass_hint, get_all_username,
                         update_settings, check_password)

from PySide6.QtCore import Qt, QPoint, QEasingCurve, QPropertyAnimation
from PySide6.QtWidgets import QMessageBox, QStackedWidget, QWidget, QCompleter
from PySide6.QtGui import QKeyEvent, QCloseEvent


class DialogLogin(DialogDraggable):
    def __init__(self, show_login_page=True, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogLogin()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.SplashScreen | Qt.WindowStaysOnTopHint)

        self.list_usernames = get_all_username()
        completer = QCompleter(self.list_usernames)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)  # مطابقت جزئی، نه فقط ابتدای رشته
        self.ui.ledUsername.setCompleter(completer)

        self._is_user_registered_successfully = False

        # ...
        if show_login_page:
            self.ui.stackedWidgetMain.setCurrentWidget(self.ui.pageLogin)
            print(self.list_usernames)  # TODO: ***  QCompleter...
        else:
            self.ui.stackedWidgetMain.setCurrentWidget(self.ui.pageRegistration)
        # ...

        self.connect_signals_to_slots()

    # ------------------------------------------------------------------------

    def connect_signals_to_slots(self):
        self.ui.btnClose.clicked.connect(self.btnClose_clicked)
        self.ui.btnLogIn.clicked.connect(self.btnLogIn_clicked)
        self.ui.btnPasswordHint.clicked.connect(self.btnPasswordHint_clicked)

        self.ui.btnRegister.clicked.connect(self.btnRegister_clicked)
        self.ui.btnGoToLoginPage.clicked.connect(self.btnGoToLoginPage_clicked)
        self.ui.btnCancelRegistrationPage.clicked.connect(self.btnClose_clicked)

    def btnClose_clicked(self):
        self.close()

    def btnLogIn_clicked(self):
        username = self.ui.ledUsername.text().strip()
        password = self.ui.ledPassword.text()
        ret = check_password(username, password)
        if not ret:
            QMessageBox.warning(self, "ورود ناموفق",
                                "نام کاربری یا کلمه عبور نادرست است")
        else:
            self.animateAndAccept()

    def btnPasswordHint_clicked(self):
        username = self.ui.ledUsername.text().strip()
        if not username:
            QMessageBox.warning(self, "ورود نام کاربری", "لطفاً نام کاربری را وارد کنید.")
            self.ui.ledUsername.setFocus()
            return

        ret = get_pass_hint(username).strip()
        if not ret:
            ret = "چیزی یافت نشد"

        QMessageBox.information(self, "راهنمای کلمه عبور", ret)

    # ------------------------------------------------------------------------

    def btnGoToLoginPage_clicked(self):
        if self.ui.stackedWidgetMain.currentWidget() != self.ui.pageLogin:
            self.animateStackedWidgetPages(self.ui.stackedWidgetMain, self.ui.pageLogin)

    def btnRegister_clicked(self):
        if not self.validate_registration():  # پیام های خطای احتمالی در همان تابع نمایش داده میشود
            return
        # ...
        username = self.ui.ledUsernameRegistrationPage.text().strip()
        password = self.ui.ledPasswordRegistrationPage.text()
        reminder = self.ui.ledPasswordHint.text().strip()

        success, message = self.register_user(username, password, reminder)
        if success:
            self._is_user_registered_successfully = True
            self.ui.stackedWidgetMain.setCurrentWidget(self.ui.pageLogin)
            self.ui.ledUsername.setText(username)
            self.ui.ledPassword.setFocus()
        else:
            QMessageBox.warning(self, "خطا", "ثبت کاربر با خطا مواجه شده است." + "\n" + message)

    def validate_registration(self):
        username = self.ui.ledUsernameRegistrationPage.text().strip()
        password = self.ui.ledPasswordRegistrationPage.text()
        password_again = self.ui.ledPasswordAgainRegistrationPage.text()
        reminder = self.ui.ledPasswordHint.text().strip()

        # بررسی تکمیل بودن فیلدها
        if not username:
            QMessageBox.warning(self, "خطا", "لطفاً نام کاربری را وارد کنید.")
            self.ui.ledUsernameRegistrationPage.setFocus()
            return False

        if not password:
            QMessageBox.warning(self, "خطا", "لطفاً کلمه عبور را وارد کنید.")
            self.ui.ledPasswordRegistrationPage.setFocus()
            return False

        if not password_again:
            QMessageBox.warning(self, "خطا", "لطفاً تکرار کلمه عبور را وارد کنید.")
            self.ui.ledPasswordAgainRegistrationPage.setFocus()
            return False

        if not reminder:
            QMessageBox.warning(self, "خطا", "لطفاً یادآوری کلمه عبور را وارد کنید.")
            self.ui.ledPasswordHint.setFocus()
            return False

        # بررسی معتبر بودن نام کاربری (حداقل 4 حرف شامل حروف انگلیسی، عدد، زیرخط)
        if not re.fullmatch(r"[A-Za-z0-9_]{4,}", username):
            QMessageBox.warning(self, "خطا", "نام کاربری باید حداقل ۴ حرف و شامل حروف، عدد یا زیرخط (_) باشد.")
            self.ui.ledUsernameRegistrationPage.setFocus()
            return False

        # بررسی تطابق کلمه عبور و تکرار آن
        if password != password_again:
            QMessageBox.warning(self, "خطا", "کلمه عبور و تکرار آن یکسان نیستند.")
            self.ui.ledPasswordAgainRegistrationPage.setFocus()
            return False

        # بررسی اینکه هیچ بخش معنادار (۴ کاراکتر یا بیشتر) از رمز داخل یادآوری نباشد
        for i in range(len(password) - 3):
            substring = password[i:i + 4].lower()
            if substring in reminder.lower():
                QMessageBox.warning(self, "خطا", "عبارت یادآوری نباید شامل بخش‌هایی از کلمه عبور باشد.")
                self.ui.ledPasswordHint.setFocus()
                return False

        # اگر همه چیز درست بود
        return True

    @staticmethod
    def register_user(username, password, pass_hint, access_level=None) -> tuple[bool, str]:
        return add_user_to_db(username, password, pass_hint, access_level)

    # ------------------------------------------------------------------------

    def keyPressEvent(self, e: QKeyEvent):
        if e.key() == Qt.Key_Escape:
            self.btnClose_clicked()
        else:
            super().keyPressEvent(e)

    # ------------------------------------------------------------------------

    def closeEvent(self, event: QCloseEvent):
        # _ = event  # به جای Q_UNUSED(event)
        # ...
        self.write_settings()
        super().closeEvent(event)

    def write_settings(self):
        new_settings = {
            "HasLoginFormShownBefore": True,
            "IsUserRegisteredSuccessfully":
                len(self.list_usernames) > 0 or self._is_user_registered_successfully
        }

        # تغییر و ذخیره تنظیمات
        if not update_settings(new_settings):
            print("Failed to update settings.")

        # ...
        # TODO:
        # if self._is_user_registered_successfully:
        #     user_info.username = "xxxx"
        #
        #     new_user_info = {"Username": user_info.username}
        #     update_userinfooooooooooooooooooooooooooo(new_user_info)
        # ...

    # ------------------------------------------------------------------------

    def animateAndAccept(self):
        self.anim = QPropertyAnimation(self, b"windowOpacity")  # ذخیره به عنوان attribute
        self.anim.setStartValue(1.0)
        self.anim.setEndValue(0.0)
        self.anim.setDuration(800)

        # اتصال مستقیم بدون Qt.QueuedConnection
        self.anim.finished.connect(self._on_animation_finished)

        self.anim.start()

    def _on_animation_finished(self):
        self.accept()
        self.anim.deleteLater()  # حذف انیمیشن با استفاده از reference مستقیم
        self.anim = None  # جلوگیری از circular reference

    def animateStackedWidgetPages(self, stacked_widget: QStackedWidget, page: QWidget,
                                  direction: Direction = Direction.LeftToRight) -> None:
        # 1. ابتدا صفحه را مخفی کرده و موقعیت اولیه را تنظیم کنید
        page.show()  # اطمینان از visibility
        page.raise_()  # اطمینان از قرارگیری در بالای stacked widget

        # 2. موقعیت پایانی را از geometry واقعی ویجت بگیرید
        pos_end = page.pos()

        # 3. تنظیم موقعیت اولیه بر اساس جهت
        pos_start = QPoint(pos_end)

        if direction == Direction.TopToBottom:
            pos_start.setY(pos_end.y() - 35)  # حرکت از بالا
        elif direction == Direction.BottomToTop:
            pos_start.setY(pos_end.y() + 35)  # حرکت از پایین
        elif direction == Direction.RightToLeft:
            pos_start.setX(pos_end.x() + 50)  # حرکت از راست
        elif direction == Direction.LeftToRight:
            pos_start.setX(pos_end.x() - 15)  # حرکت از چپ

        # 4. اعمال موقعیت اولیه قبل از شروع انیمیشن
        page.move(pos_start)
        stacked_widget.setCurrentWidget(page)

        # 5. ایجاد و تنظیم انیمیشن
        animation = QPropertyAnimation(page, b"pos")
        animation.setDuration(700)  # مدت زمان بهینه‌تر
        animation.setStartValue(pos_start)
        animation.setEndValue(pos_end)
        animation.setEasingCurve(QEasingCurve.OutQuint)  # منحنی نرم‌تر

        # 6. مدیریت حذف خودکار انیمیشن
        animation.finished.connect(lambda: (
            animation.deleteLater(),
            # print("Animation completed and deleted")  # برای دیباگ
        ))

        animation.start()

    # ------------------------------------------------------------------------
