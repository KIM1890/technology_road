from django.views.generic import TemplateView


class StorePageView(TemplateView):
    template_name = "pages/store.html"


class IpadPageView(TemplateView):
    template_name = "pages/ipad.html"


class IphonePageView(TemplateView):
    template_name = "pages/iphone.html"


class WatchPageView(TemplateView):
    template_name = "pages/watch.html"


class TVPageView(TemplateView):
    template_name = "pages/tv.html"


class SupportPageView(TemplateView):
    template_name = "pages/support.html"


class CartPageView(TemplateView):
    template_name = "pages/cart.html"


class ComingSoonView(TemplateView):
    template_name = "pages/coming_soon.html"
