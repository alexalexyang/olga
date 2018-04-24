from modeltranslation.translator import translator, TranslationOptions
from oscar.apps.catalogue.models import Product


class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


translator.register(Product, ProductTranslationOptions)



# from modeltranslation.translator import translator, TranslationOptions
# from oscar.apps.catalogue.abstract_models import AbstractProduct
#
# class ProductTranslationOptions(TranslationOptions):
#     fields = ('title', 'description',)
#
# translator.register(AbstractProduct, ProductTranslationOptions)