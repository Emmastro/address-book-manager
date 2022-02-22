from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q

from .models import Contact
from .forms import ContactForm


# @method_decorator(login_required, name='dispatch')
class ContactsList(ListView):
    """
    """

    model = Contact
    template_name = "contacts.html"
    context_object_name = "contacts"
    paginate_by = 20
    order_by = "first_name"

    def get_queryset(self):
        search_key = self.request.GET.get("search_key")

        if search_key:
            contact_list = self.model.objects.filter(
                Q(first_name__icontains=search_key) |
                Q(last_name__icontains=search_key) | 
                Q(phone_number__icontains=search_key) |
                Q(email__icontains=search_key)
            )
        else:
            contact_list = super().get_queryset().order_by(self.order_by)

        return contact_list


# @method_decorator(login_required, name='dispatch')
class ContactsDetail(DetailView):
    """
    """

    model = Contact
    template_name = "contacts.html"
    context_object_name = "contacts"
    paginate_by = 20
    order_by = "first_name"


# @method_decorator(login_required, name='dispatch')
class AddContactView(CreateView):
    """
    """
    template_name = 'new-contact.html'
    form_class = ContactForm
    success_url = '/'
    def form_valid(self, form):
        """
        """
        # TODO: add form validation
        form.save()
        print(form)
        return super(AddContactView, self).form_valid(form)