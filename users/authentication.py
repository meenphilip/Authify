from django.contrib.auth.models import User


class EmailAuthBackend:
    """
    Authenticate using an e-mail address.
    """

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    # get user with their id
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except:
            return None
