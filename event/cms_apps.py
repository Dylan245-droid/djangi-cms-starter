from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register  # register the application
class EventsApphook(CMSApp):
    app_name = "event"
    name = "Event Application"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["event.urls"]