from modeltranslation.translator import translator, TranslationOptions
from oscar.apps.catalogue.models import Product


class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


translator.register(Product, ProductTranslationOptions)