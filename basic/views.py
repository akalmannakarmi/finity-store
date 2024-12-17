from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .mixins import BaseMixin
from .forms import CustomUserCreationForm
from store.models import Listing

class IndexView(BaseMixin,TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		mixin_context = super(BaseMixin, self).get_context_data(**kwargs)
		list_view_context = super(IndexView, self).get_context_data(**kwargs)
		context = {**mixin_context, **list_view_context}
		context["featured"] = Listing.objects.all()[:3]
		context["newest"] = Listing.objects.all()[:3]
		context["ending"] = Listing.objects.all()[:3]
		return context

class RegisterView(CreateView):
	form_class = CustomUserCreationForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')
