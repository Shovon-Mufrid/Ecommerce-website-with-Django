from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from App_UserLog.models import UserLog

@receiver(post_save)
def log_object_creation_update(sender, instance, created, **kwargs):
    if sender.__name__ != "UserLog":
        # temp=
        import inspect
        request=""
        for frame_record in inspect.stack():
            if frame_record[3]=='get_response':
                request = frame_record[0].f_locals['request']
                break
        else:
            request = None

        if created:
            action = f'Created {sender.__name__} {instance}'
        else:
            action = f'Updated {sender.__name__} {instance}'
    
        content_type = ContentType.objects.get_for_model(sender)

        UserLog.objects.create(
            user=request.user,
            action=action,
            content_type=content_type,
            object_id=instance.pk,
        )  


@receiver(post_delete)
def log_object_deletion(sender, instance, **kwargs):
    if sender.__name__ != "UserLog":
        import inspect
        request=""
        for frame_record in inspect.stack():
            if frame_record[3]=='get_response':
                request = frame_record[0].f_locals['request']
                break
        else:
            request = None
        content_type = ContentType.objects.get_for_model(sender)
        UserLog.objects.create(
            user=request.user,
            action=f'Deleted {sender.__name__} {instance}',
            content_type=content_type,
            object_id=instance.pk,
        )
