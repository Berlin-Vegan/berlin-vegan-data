from django.conf import settings
from django.core.mail import send_mail


def mail_new_submit(open_submits:  int) -> None:
    subject = 'Es gibt eine neue Einreichung'
    message = f'Momentan gib es {open_submits} offene Einreichungen. https://data.berlin-vegan.de/gastro-submit-list/'
    from_email = settings.EMAIL_FROM
    recipient_list = [settings.EMAIL_GASTROS]

    try:
        send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)
    except:
        pass


