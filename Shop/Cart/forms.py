from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 10)]

class CartAddProductForm(forms.Form):
    #TypedChoiceField с coerce=int для преобразования ввода в целое число
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label='')    #количество между 1-20. 
    #update : позволяет указать, следует ли добавлять сумму к любому существующему значению в корзине для 
    # данного продукта (False) или если существующее значение должно быть обновлено с заданным значением (True).
    # HiddenInput, поскольку не требуется показывать это поле пользователю.
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)