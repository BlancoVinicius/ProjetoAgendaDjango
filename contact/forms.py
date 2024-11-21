from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact

class ContatcForm(forms.ModelForm):
    ### criando um campo no proprio form
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'classe-a classe-b',
                "placeholder": "Escreva aquiiii"
            }
        ),
        label="Primeiro Nome",
        help_text="Insira seu nome!"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ### alterando o wiggt first_name
        # self.fields['first_name'].widget.attrs.update({
        #     'class':'classe-a classe-b',
        #     "placeholder": "Veio do init escreva aqui"
        # })
    
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone',)

        ### criando um novo widget na classe meta
        # widgets = {
        #     'first_name' : forms.TextInput(
        #         attrs={
        #             'class':'classe-a classe-b',
        #             "placeholder": "Escreva aqui"
        #         }
        #     )
        # }
    
    def clean(self):
                
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem Erro',
                code='invalid'
            )
        )

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem Erro2',
                code='invalid'
            )
        )
        return super().clean()