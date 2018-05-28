from modeltranslation.translator import translator, TranslationOptions
from oscar.apps.customer.models import CommunicationEventType


class ProductTranslationOptions(TranslationOptions):
    fields = ('email_subject_template',
              'email_body_template',
              'email_body_html_template',)


translator.register(CommunicationEventType, ProductTranslationOptions)