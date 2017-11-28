from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.http import Http404, request, HttpResponseRedirect

from ChatBot.models import User


class DeleteUser(DeleteView):
    model = User
    template_name = "delete_user.html"
    success_url = reverse_lazy('login')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == request.user:
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        else:
            raise Http404
            # or return HttpResponse('404_url')
