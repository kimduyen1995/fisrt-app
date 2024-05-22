from decouple import config

from my_app.configs.app_settings import *

APP_ENV = config("APP_ENV")

FOLDER_PATH = "/opt/demo"
UPLOAD_DIRECTORY = FOLDER_PATH + "/upload"

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DATETIME_FORMAT3 = '%Y%m%d_%H%M%S'
DATETIME_FORMAT5 = '%Y%m%d%H%M%S'
DATETIME_FORMAT_EXPORT = '%d/%m/%Y %H:%M:%S'




UPLOAD_DIRECTORY_PUBLIC = "https://localhost/view-file?path="
DOWNLOAD_DIRECTORY_PUBLIC = "https://localhost/download-file?path="





