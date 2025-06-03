from enum import Enum
from dataclasses import dataclass


# ======================= اطلاعات کاربر ============================
@dataclass
class UserInfo:
    username: str = ""
    access_level: int = None  # 1=Full access, 0=Read only


user_info = UserInfo()


# ==================== اطلاعات شرکت (ثابت) ========================
@dataclass(frozen=True)
class CompanyInformation:
    organization_name: str = "Hosfa"
    organization_domain: str = "https://takvingar.ir/"


company_info = CompanyInformation()


# ====================== اطلاعات برنامه (ثابت) =======================
@dataclass(frozen=True)
class AppInformation:
    application_name_en: str = "Takvingar"
    application_name_fa: str = "تکوینگر"
    support_mail: str = "reza.rezvani2052@gmail.com"


app_info = AppInformation()


# ======================= تنظیمات برنامه ==========================
@dataclass
class AppSettings:
    run_at_windows_startup: bool = False
    show_on_top: bool = False
    show_on_tray_on_exit: bool = False
    save_path: str = ""
    db_data_path: str = ""
    # ...
    num_of_app_exec: int = 0


app_settings = AppSettings()


# ====== کلید های تنظیمات برنامه در پایگاه داده (ثابت) =====
# هر تغییری در جدول مربوطه در پایگاه داده باید در این اعمال شود و بالعکس
@dataclass(frozen=True)
class SettingsKeys:
    has_login_form_shown_before: str = "HasLoginFormShownBefore"
    is_user_registered_successfully: str = "IsUserRegisteredSuccessfully"
    run_app_at_windows_startup: str = "RunAppAtWindowsStartup"
    show_on_top: str = "ShowOnTop"
    show_on_system_tray_on_exit: str = "ShowOnSystemTrayOnExit"
    save_path: str = "SavePath"
    db_data_path: str = "DbDataPath"
    num_of_app_exec: str = "NumOfAppExec"


settings_keys = SettingsKeys()


# ================== کدهای خروج برنامه =====================
class AppExitCode(Enum):
    OK_EXIT_CODE = 0
    LOGIN_CANCELED_BY_USER = 1
    APP_RESTARTED_BY_USER = 100
    MULTIPLE_INSTANCE_ERR = -1
    DB_FILE_NOT_FOUND = -2


# ====================== جهت‌ها ============================
class Direction(Enum):
    TopToBottom = 0
    BottomToTop = 1
    LeftToRight = 2
    RightToLeft = 3

# =================== تاریخ شمسی و میلادی =====================
# @dataclass
# class JalaliGregorianDate:
#     year: int
#     month: int
#     day: int
