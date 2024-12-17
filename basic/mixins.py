from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

class BaseMixin:
    """
    A base mixin to handle common functionality for views.
    Can be used to check authentication, provide common context, and more.
    """

    def check_user_authenticated(self, request):
        """
        Check if the user is authenticated. Returns a response or raises an error.
        """
        if not request.user.is_authenticated:
            return JsonResponse({"error": "Authentication required"}, status=401)
        return None

    def get_context_data(self, *args, **kwargs):
        account_no = self.request.user.account_no if self.request.user.is_authenticated else 1
        context={
            "balance_url": "http://localhost:8080/balance/",
            "exchange_url": "http://localhost:5000/buy",
            "account_no": account_no,
            "site_name": "My Django Site",
        }
        
        return context

    def json_response(self, data, status=200):
        """
        Return a JsonResponse with the given data.
        """
        return JsonResponse(data, status=status)

