from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import EventPluginModel
from django.utils.translation import gettext as _


@plugin_pool.register_plugin  # register the plugin
class EventPluginPublisher(CMSPluginBase):
    model = EventPluginModel  # model where plugin data are saved
    module = _("Events")
    name = _("Event Plugin")  # name of the plugin in the interface
    render_template = "event/event_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context