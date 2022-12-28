from django.core.mail import send_mail


from django.conf import settings


def send_email(request):
    print(f"EMAIL_HOST = {settings.EMAIL_HOST_USER}")
    send_mail(
        'Subject here',
        'Here is the message.',
        settings.EMAIL_HOST_USER,
        ['ifeanyi.okala.247238@unn.edu.ng'],
        fail_silently=False,
    )


