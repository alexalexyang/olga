from oscar.apps.dashboard.communications.forms import CommunicationEventTypeForm as baseCommunicationEventTypeForm
# from modeltranslation.forms import *


class CommunicationEventTypeForm(baseCommunicationEventTypeForm):
    class Meta(baseCommunicationEventTypeForm.Meta):
        fields = [
            'email_subject_template',
            'email_subject_template_ru',
            'email_body_template',
            'email_body_template_ru',
            'email_body_html_template',
            'email_body_html_template_ru',
        ]
