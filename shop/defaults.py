from mezzanine.conf import register_setting
from django.utils.translation import ugettext_lazy as _

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    append=True,
    default=("SOCIAL_LINK_FACEBOOK",
             "SOCIAL_LINK_TWITTER",
             "SOCIAL_LINK_INSTAGRAM",
             "SOCIAL_LINK_NEWSLETTER",),
)


register_setting(
    name="SOCIAL_LINK_FACEBOOK",
    label=_("Facebook link"),
    description=_("If present a Facebook icon will be in the footer."),
    editable=True,
    default="",
)

register_setting(
    name="SOCIAL_LINK_TWITTER",
    label=_("Twitter link"),
    description=_("If present a Twitter icon will be in the footer."),
    editable=True,
    default="",
)

register_setting(
    name="SOCIAL_LINK_INSTAGRAM",
    label=_("Instagram link"),
    description=_("If present an Instagram icon will be in the footer."),
    editable=True,
    default="",
)

register_setting(
    name="SOCIAL_LINK_NEWSLETTER",
    label=_("Newsletter link"),
    description=_("If present a newsletter icon will be in the footer."),
    editable=True,
    default="",
)