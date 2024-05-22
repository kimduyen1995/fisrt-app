from django.conf import settings as project_settings
from my_app.configs import app_settings
from rest_framework.viewsets import ViewSet
from rest_framework import status
from django.db.models.query import QuerySet

from my_app.my_core.helpers.response import *
from my_app.my_http.models.info_file import *
from my_app.my_core.helpers.utils import *

class InfoFileView(ViewSet):
    def api_get_info_file(self, request):
        qr = InfoFile.objects.all()
        data = qr.values()

        return response_data(data=data, status=1, message="Success")

    def api_insert_file(self, request):
        data_input = request.data
        user_email = data_input.get("user_email")
        dict_upload = self.upload_file(request, user_email)
        ok = dict_upload.get("ok", False)
        print(ok)
        if ok:
            data = dict_upload.get("link_public", [])
            msg = "Success"
            status_api = 1
        else:
            msg = "Failed "
            status_api = STATUS_CODE_ERROR_LOGIC
        return response_data(data=data, status=status_api, message=msg)


    def upload_file(self, request, user_email,  fname=""):
        ok = False
        list_link_public = []
        list_file_name = []
        err = ""
        try:
            data_input = request.data
            number_file_init = data_input.get("numberFile", 0)
            str_datetime = get_current_datetime().strftime(DATETIME_FORMAT3)
            number_file = int(number_file_init)
            # print(request.FILES)
            print(number_file)
            for file_obj in request.FILES.getlist('file'):
                # cnt = i_file + 1
                # key_file = 'file_{}'.format(cnt)
                # file_obj = request.FILES[key_file]
                # print(file_obj.content_type)
                link_folder = UPLOAD_DIRECTORY
                # link_public = UPLOAD_DIRECTORY_PUBLIC +  "upload/" + folder_name



                file_name_init = convert_no_accent_vietnamese(file_obj.name)

                final_file = file_name_init.split(".")[-1]

                # if file_obj.content_type == "image/heic":
                #
                #     file_name_init = file_name_init.replace(".heic", ".webp")

                # link_public = link_public + "/" + str_datetime + "_" + file_name_init

                if not os.path.exists(link_folder):
                    os.makedirs(link_folder)

                abs_dir = os.path.abspath(link_folder)
                random_number = random.randint(0, 100)

                filename = str_datetime + "_{}_".format(str(random_number)) + file_name_init

                filepath = os.path.join(abs_dir, filename)
                print(filepath)

                save_file(file_obj, filepath)


                str_uuid = str(uuid.uuid4().node).zfill(16)
                link_public = UPLOAD_DIRECTORY_PUBLIC + str_uuid
                if file_obj.content_type not in ['image/heic', 'image/png', 'image/jpeg', 'application/pdf']:
                    link_public = DOWNLOAD_DIRECTORY_PUBLIC + str_uuid

                list_link_public.append(link_public)
                list_file_name.append(file_name_init)

                # import thong tin file vao database
                self.save_data_db(user_email,  filepath, link_public,  fname)

            ok = True
        except Exception as e:
            print("upload_file: {} >> Error: {}".format(fname, e))



        dict_output = {
            "ok": ok,
            "link_public": list_link_public,
            "file_name": list_file_name,
            "error": err
        }
        return dict_output

    def save_data_db(self, user_email,  link_folder, link_public,  fname=""):
        ok = False
        try:
            InfoFile.objects.create(link_data=link_public, local_folder=link_folder, email_create =user_email)
            # str_uuid = str(uuid.uuid4().node).zfill(16)
            # time_now = get_current_datetime()
            # storage_uuid = InfoFile()
            # storage_uuid.link_data = link_public
            # storage_uuid.local_folder = link_folder
            # storage_uuid.email_create = user_email

            # storage_uuid.save()
            ok = True
        except Exception as e:
            print("save_data_db:{} >> Error/Loi :{}".format(fname, e))
        return ok

