from oscar.apps.dashboard.catalogue.forms import ProductForm as baseProductForm
from modeltranslation.forms import *


class ProductForm(baseProductForm):
    # model = Product
    class Meta(baseProductForm.Meta):
        fields = [
            'title',
            'title_de',
            'title_ru',
            'title_zh_hans',
            'upc',
            'description',
            'description_de',
            'description_ru',
            'description_zh_hans',
            'is_discountable',
            'structure']
