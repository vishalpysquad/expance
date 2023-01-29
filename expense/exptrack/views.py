from django.views.generic import CreateView, DeleteView, ListView

from .forms import ExpDesignForm
from .models import ExpanseTracking


class ExpanseCreate(CreateView):
    form_class = ExpDesignForm
    template_name = "expense/expanse_create.html"
    success_url = "createexp"

    def form_valid(self, form):
        expanse = form.save()
        credit = ExpanseTracking.objects.filter(
            user=self.request.user.id, status="Credit"
        ).values_list("price", flat=True)
        debit = ExpanseTracking.objects.filter(
            user=self.request.user.id, status="Debit"
        ).values_list("price", flat=True)
        balance = sum(credit) - sum(debit)
        expanse.balance += balance
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = super().get_context_data(**kwargs)
        if context:
            context["data"] = ExpanseTracking.objects.all()
            context["balance"] = context["data"][len(context["data"]) - 1].balance
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super().get_context_data(**context)


class ExpanseList(ListView):
    model = ExpanseTracking
    template_name = "expense/expanse_create.html"


class ExpanseDelete(DeleteView):

    model = ExpanseTracking
    success_url = "/createexp"

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
