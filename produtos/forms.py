from django.forms import ModelForm
from .models import Produto

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'quantidade', 'tipo', 'preco', 'observacao']