import os
import sys
from dominate.util import raw, text
from . import document as dominate_document
from . import util
from . import tags
from .tags import html_tag
from .dom_tag import dom_tag, attr, get_current
from .dom1core import dom1core


class document(dominate_document):
    def __init__(self, title="Dominate", doctype="<!DOCTYPE html>", *args, **kwargs):
        super(document, self).__init__(title, doctype, **kwargs)
        self.pretext = util.container()

    def _render(self, sb, *args, **kwargs):
        if self.pretext:
            sb.append(self.pretext.render())
        return super(document, self)._render(sb, *args, **kwargs)


def build(base_html, module_path=sys.argv[0]):
    HTML_FILE = os.path.splitext(module_path)[0] + ".html"
    with open(HTML_FILE, "w") as file:
        file.write(base_html.render())


class controlTag(dom_tag, dom1core):
    str_run = False

    def __init__(self, *args, **kwargs):
        if args and isinstance(args[0], str):
            self.arg = args[0]
            args = args[1:]

        super().__init__(*args, **kwargs)

    def _render(self, sb, indent_level, indent_str, pretty, xhtml):
        pretty = pretty and self.is_pretty

        name = getattr(self, "tagname", type(self).__name__)

        # open tag
        sb.append(r"{% ")
        sb.append(name)
        if self.arg:
            sb.append(f" {self.arg}")
        sb.append(r" %}")

        if self.is_single:
            return sb

        inline = self._render_children(sb, indent_level + 1, indent_str, pretty, xhtml)
        if pretty and not inline:
            sb.append("\n")
            sb.append(indent_str * indent_level)

        # close tag
        sb.append(r"{% ")
        sb.append(f"end{name}")
        sb.append(r" %}")

        self._rendered = True
        return sb


def static(arg):
    s = "{%% static '%s' %%}" % arg
    return s


def url(arg):
    s = "{%% url %s %%}" % arg
    return s


# {% url 'some-url-name' v1 v2 %}


class extends(controlTag):
    is_single = True
    pass


class include(controlTag):
    is_single = True
    pass


class load(controlTag):
    is_single = True
    pass


class forloop(controlTag):
    tagname = "for"


class block(controlTag):
    pass


def v(s):
    v = "{{ %s }}" % s
    return v


class variableTag(dom_tag, dom1core):
    str_run = False

    def __init__(self, *args, **kwargs):
        if args and isinstance(args[0], str):
            self.arg = args[0]
            args = args[1:]

        super().__init__(*args, **kwargs)

    def _render(self, sb, indent_level, indent_str, pretty, xhtml):
        pretty = pretty and self.is_pretty

        name = getattr(self, "tagname", type(self).__name__)

        # open tag
        sb.append(r"{{ ")
        if self.arg:
            sb.append(f"{self.arg}|")
        sb.append(name)
        sb.append(r" }}")

        return sb


class safe(variableTag):
    pass
