from django.db import models



class InfoFile(models.Model):
    class Meta:
        db_table = "info_file"

    file_id = models.AutoField(primary_key=True)
    link_data = models.CharField(max_length=500) # link view on web browser
    local_folder = models.CharField(max_length=500) # folder save file
    email_create = models.CharField(max_length=45) # email updatefile
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_id