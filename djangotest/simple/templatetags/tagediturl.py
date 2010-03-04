from django import template

register = template.Library()

@register.tag
def edit_url(parser, token):
    try:
        tag_name, args = token.split_contents()
    except:
        raise template.TemplateSyntaxError, "%r syntax error" % token.contents.split()
    if not (args[0] == args[-1] and args[0] in ("'",'"')):
        raise template.TemplateSyntaxError, "%r syntax error" % tag_name
    return AdminUrlTagClass(args[1:-1])

class AdminUrlTagClass(template.Node):
    def __init__(self, args):
        self.args = template.Variable(args)
        
    def render(self, context):
        instance = self.args.resolve(context)
        return "/admin/%s/%s/%s/" % (instance._meta.app_label,
                                        instance._meta.module_name,
                                        instance.id)
            