from rest_framework.serializers import ModelSerializer

from .models import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        exclude = ()
        model = Note


class NoteListSerializer(NoteSerializer):
    class Meta:
        exclude = ('text',)
        model = Note


class NoteDetailSerializer(NoteSerializer):
    ...
