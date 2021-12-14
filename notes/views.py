from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from .models import Note
from .permissions import IsOwnerUser
from .serializers import NoteDetailSerializer


@method_decorator(csrf_exempt, name='dispatch')
class MyLoginView(LoginView):
    template_name = 'login_form.html'
    redirect_authenticated_user = True


class MyLogoutView(LoginRequiredMixin,
                   LogoutView):
    ...


class NoteViewSet(ModelViewSet):

    queryset = Note.objects.all()
    serializer_class = NoteDetailSerializer
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly, ]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(author=request.user.id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data.update({'author': request.user.id})
        request.POST._mutable = False
        return super(NoteViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        input_data = request.data.copy()
        input_data['updated_at'] = datetime.now()

        instance = self.get_object()
        check_done = input_data.get('done')
        if (isinstance(check_done, bool) and check_done) and instance.done is not True:
            input_data['closed_at'] = datetime.now()

        serializer = self.get_serializer(instance, data=input_data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
