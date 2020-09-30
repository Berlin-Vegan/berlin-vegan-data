from django.conf import settings
from django.core.mail import send_mail


def mail_new_submit(open_submits: int) -> None:
    subject = "Es gibt eine neue Einreichung"
    message = f"There are currently {open_submits} open submissions. https://data.berlin-vegan.de/gastros/submissions/"
    from_email = settings.EMAIL_FROM
    recipient_list = [settings.EMAIL_GASTROS]

    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=True,
    )
