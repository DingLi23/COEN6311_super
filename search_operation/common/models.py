from django.db import models

class Record(models.Model):
    
    id = models.BigAutoField(
        "universal id", 
        primary_key=True,
    )

    create_time = models.DateTimeField(
        "universal create time", 
        auto_now_add=True
    )
    # updateTime = models.DateTimeField("universal update time", db_column='update_time')

    class Meta:
        # https://docs.djangoproject.com/en/3.2/topics/db/models/#abstract-base-classes
        abstract = True