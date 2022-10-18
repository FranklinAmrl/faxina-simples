from user.forms.user_registration_form import UserRegistrationForm

from django.views.generic.edit import FormView


class UserRegistrationFormView(FormView):
    template_name = "user_registration.html"
    form_class = UserRegistrationForm
    success_url = "/"

    def form_valid(self, form):
        return super().form_valid(form)
