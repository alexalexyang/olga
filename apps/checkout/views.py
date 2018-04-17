from oscar.apps.checkout.views import PaymentDetailsView as BasePaymentDetailsView


class PaymentDetailsView(BasePaymentDetailsView):

    preview = True