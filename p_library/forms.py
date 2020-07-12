from django import forms
from p_library.models import Author, Book, Friend


class AuthorForm(forms.ModelForm):

    full_name = forms.CharField(label='Имя', widget=forms.TextInput)

    class Meta:
        model = Author
        fields = '__all__'


class BookForm(forms.ModelForm):

    title = forms.CharField(label='Название', widget=forms.TextInput)

    class Meta:
        model = Book
        fields = '__all__'
        
class Maker(forms.ModelForm):

    make_name = forms.CharField(label='Издатель', widget=forms.TextInput)

    
        

class AuthorAdminForm(forms.ModelForm):

    full_name = forms.CharField(widget=forms.TextInput, label='Имя')


class FriendAdminForm(forms.ModelForm):

    name = forms.CharField(label='Имя друга', widget=forms.TextInput)


class FriendForm(forms.ModelForm):

    friend_name = forms.CharField(label='Имя друга', widget=forms.TextInput)
    books = forms.ModelMultipleChoiceField(
        label='Книги',
        queryset=Book.objects,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Friend
        fields = '__all__'


class FriendEditForm(forms.ModelForm):

    name = forms.CharField(label='Имя друга', widget=forms.TextInput)

    class Meta:
        model = Friend
        fields = ('friend_name',)

