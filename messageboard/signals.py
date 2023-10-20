from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
import logging

log = logging.getLogger('django')

@receiver(user_logged_in)
def user_logged_in_cb(sender, user, **kwargs):
    log.info(f"{user} logged in.")

@receiver(user_login_failed)
def user_login_failed_cb(sender, user=None, **kwargs):
    log.error(f"{user or 'unknown user'} failed to login.")

@receiver(user_logged_out)
def user_logged_out_cb(sender, user, **kwargs):
    log.info(f"{user} logged out.")