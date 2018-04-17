from oscar.apps.dashboard.catalogue.forms import ProductForm as baseProductForm
from modeltranslation.forms import *


class ProductForm(baseProductForm):
    # model = Product
    class Meta(baseProductForm.Meta):
        fields = [
            'title',
            'title_en',
            'title_de',
            'title_fr',
            'title_ja',
            'upc',
            'description',
            'description_en',
            'description_de',
            'description_fr',
            'description_ja',
            'is_discountable',
            'structure']
