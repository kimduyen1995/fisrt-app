from Cryptodome.Cipher import AES
import time
import string
import random
import base64
from Crypto.Util.Padding import pad
from ..helpers.global_variable import *
import os
from datetime import datetime, timedelta, date
import uuid
import re






def get_current_datetime():
    return datetime.utcnow() + timedelta(hours=7)







def convert_no_accent_vietnamese(text, fname=""):
    """
    Convert from 'Tieng Viet co dau' thanh 'Tieng Viet khong dau'
    text: input string to be converted
    Return: string converted
    """


    new_text = ""
    try:
        patterns = {
            '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
            '[đ]': 'd',
            '[èéẻẽẹêềếểễệ]': 'e',
            '[ìíỉĩị]': 'i',
            '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
            '[ùúủũụưừứửữự]': 'u',
            '[ỳýỷỹỵ]': 'y',
            '[ ]': "_"
        }
        output_init = text.strip()
        output = output_init.lower()
        for regex, replace in patterns.items():
            output = re.sub(regex, replace, output)
            # deal with upper case
            output = re.sub(regex.upper(), replace.lower(), output)
            new_text = output
    except Exception as e:
        print(e)
        # logger.info("convert_no_accent_vietnamese >> {} Error/Loi : {}".format(fname, e))
    return new_text


def convert_date_import_Db(dd_mm_yyy, fname=""):
    result = None
    try:
        if dd_mm_yyy is not None and len(dd_mm_yyy) > 0:
            result = datetime.strptime(str(dd_mm_yyy), "%d/%m/%Y").strftime('%Y-%m-%d')
    except Exception as e:
        print("--------------------")
        print("convert_date_import_Db: {} >> {} ".format(fname, e))
    return result


def get_str_datetime_now_import_db():
    time_now = get_current_datetime()
    str_time_now = time_now.strftime(DATETIME_FORMAT)
    return str_time_now


def save_file_txt(folder, name_file, content, fname= ""):
    # ex : input namefile = test, link_forder = ../../data/export_kbyt, content = test
    # ouput ../data/export_kbyt/test.txt
    filename = name_file + '.' + 'txt'
    file_directory = ""

    txt_output = ""
    try:
        if folder != "":
            link_folder = UPLOAD_DIRECTORY + "/" + folder
            abs_dir = os.path.abspath(link_folder)
            file_directory = os.path.join(abs_dir, filename)
            if not os.path.exists(link_folder):
                os.makedirs(link_folder)
            with open(file_directory, "w") as fp:
                fp.write(content)
                fp.close()
                return file_directory
        return txt_output
    except Exception as ex:
        print("{}--------------".format(fname))
        print(ex)

        # logger_db.info("Error on {} when save file: {}".format(fname, file_directory, ex))
        return txt_output




def read_file_txt_convert_str(link_file, fname= ""):
    # ex : link_file = ../../data/a/b.txt
    # ouput: str nội dung file
    content = ""
    try:
        if link_file != "":
            f = open(link_file, 'r', encoding="utf8")
            content = f.read()
    except Exception as ex:
        print("read_file_txt_convert_str")
        print("Error on {} when read file: {}, >> {}".format(fname, link_file, ex))
    return content

def save_file(file_input, full_path):
    with open(full_path, 'wb+') as f:
        for chunk in file_input.chunks():
            f.write(chunk)

