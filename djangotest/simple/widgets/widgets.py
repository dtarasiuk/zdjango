from django.utils.safestring import mark_safe
from django.forms.extras.widgets import SelectDateWidget


class ZSelectDateWidget(SelectDateWidget):

    def render(self, name, value, attrs=None):
        return mark_safe(u'<input id="id_%s" name="%s" value="%s" class="datepicker"/>'% \
            (self.attrs['name'], self.attrs['name'], value))

    class Media:
        css = {
            'all': ('css/main.css', \
            'http://jquery-ui.googlecode.com/svn/tags/latest/themes/base/jquery-ui.css')
        }
        js = ('http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js', \
        'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8/jquery-ui.min.js', \
        'js/enabledatapickers.js')
