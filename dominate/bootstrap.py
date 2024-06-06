from . import tags
from . import util
import uuid


class BootstrapComponent(tags.html_tag):
    cls = None

    def __init__(self, *args, **kwargs):
        if self.cls:
            bs_class = self.cls
        else:
            bs_class = type(self).__name__.replace("_", "-").lower()
        all_classes = self._all_classes(bs_class, kwargs)

        super().__init__(*args, **kwargs, _class=all_classes)

    def _all_classes(self, bs_class, kwargs):
        user_classes = kwargs.pop("_class", "") + " " + kwargs.pop("cls", "")
        all_classes = " ".join(filter(None, [bs_class, user_classes.strip()]))

        return all_classes

    def _btn_classes(self, bs_class, kwargs):
        user_classes = kwargs.pop("_class", "") + " " + kwargs.pop("btn_cls", "")
        btn_classes = " ".join(filter(None, [bs_class, user_classes.strip()]))

        return btn_classes


class navbar_brand(BootstrapComponent):
    tagname = "a"


class btn(BootstrapComponent):
    def __init__(self, *args, **kwargs):
        id = kwargs.pop("id", "")
        super().__init__(
            *args,
            **kwargs,
            tagname="button",
            data_bs_toggle="collapse",
            data_bs_target=f"#{id}",
            aria_controls=f"{id}",
            aria_expanded="false",
            aria_label="Toggle navigation",
        )


class navbar_collapse(BootstrapComponent):
    tagname = "div"


class nav_item(BootstrapComponent):
    tagname = "li"


class row(BootstrapComponent):
    tagname = "div"


class col(BootstrapComponent):
    tagname = "div"


class container(BootstrapComponent):
    tagname = "div"


class btn_group(BootstrapComponent):
    tagname = "div"


class collapse(BootstrapComponent):
    tagname = "div"


class form_control(BootstrapComponent):
    tagname = "input"


class card(BootstrapComponent):
    tagname = "div"


class card_body(BootstrapComponent):
    tagname = "div"


class bold(BootstrapComponent):
    tagname = "div"


class BootstrapComponentWithId(BootstrapComponent):
    def __init__(self, *args, **kwargs):
        id = kwargs.get("id", None)
        if id is None:
            kwargs["id"] = str(uuid.uuid4())
        super().__init__(*args, **kwargs)


class accordion(BootstrapComponentWithId):
    tagname = "div"


class accordion_header(BootstrapComponent):
    tagname = "h2"


class accordion_button(BootstrapComponent):
    tagname = "button"

    def __init__(self, *args, **kwargs):
        accordion_id = kwargs.pop("data_bs_target", None)
        if accordion_id is not None:
            kwargs["data_bs_target"] = "#" + accordion_id
            kwargs["aria_controls"] = accordion_id

        kwargs.setdefault("aria_expanded", "false")
        kwargs.setdefault("data_bs_toggle", "collapse")
        kwargs.setdefault("cls", "collapsed")

        super().__init__(*args, **kwargs)


class accordion_collapse(BootstrapComponentWithId):
    tagname = "div"

    def __init__(self, *args, **kwargs):
        accordion_parent_id = kwargs.pop("data_bs_parent", None)
        if accordion_parent_id is not None:
            kwargs["data_bs_parent"] = "#" + accordion_parent_id
        super().__init__(*args, **kwargs, _class="collapse")


class accordion_body(BootstrapComponent):
    tagname = "div"


class accordion_item(BootstrapComponent):
    tagname = "div"

    def __init__(self, header, body, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        id_ = str(uuid.uuid4())

        with accordion_header() as hdr:
            with accordion_button(data_bs_target=id_) as btn:
                btn.add(header)
            hdr.add(btn)

        with accordion_collapse(id=id_, data_bs_parent=parent.id) as clp:
            with accordion_body() as bd:
                bd.add(body)
            clp.add(bd)

        self.add(hdr, clp)


class dropdown_menu(BootstrapComponent):
    tagname = "ul"

    def add(self, *args):
        for item in args:
            li = tags.li(args)
            super(dropdown_menu, self).add(li)


class dropdown_item(BootstrapComponent):
    tagname = "a"


class dropdown(BootstrapComponent):
    tagname = "div"
    cls = "dropdown"

    def __init__(self, *args, **kwargs):
        self.tagname = kwargs.pop("tagname", self.tagname)
        super().__init__(*args, **kwargs)
        self.menu = dropdown_menu()

        super(dropdown, self).add(self.toggle)
        super(dropdown, self).add(self.menu)

    def add(self, *args):
        self.menu.add(*args)


class dropdown_button(dropdown):
    def __init__(self, title, *args, **kwargs):
        bs_class = "btn dropdown-toggle"
        btn_classes = self._btn_classes(bs_class, kwargs)

        self.toggle = tags.button(
            title,
            cls=btn_classes,
            data_bs_toggle="dropdown",
            aria_expanded="false",
            type="button",
        )
        super().__init__(*args, **kwargs)


class dropdown_link(dropdown):
    def __init__(self, link_title, href="#", *args, **kwargs):
        bs_class = "btn dropdown-toggle"
        btn_classes = self._btn_classes(bs_class, kwargs)

        self.toggle = tags.a(
            link_title,
            href=href,
            cls=btn_classes,
            role="button",
            data_bs_toggle="dropdown",
            aria_expanded="false",
        )
        super().__init__(*args, **kwargs)


class navbar_nav(BootstrapComponent):
    tagname = "ul"


class container_fluid(BootstrapComponent):
    tagname = "div"


class navbar(BootstrapComponent):
    tagname = "nav"
    cls = "navbar"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.container = super(navbar, self).add(container_fluid())
        self.container = super(navbar, self).add(container_fluid())

        with self.container:
            self.brand = util.container()
            tags.button(
                tags.span(
                    cls="navbar-toggler-icon",
                ),
                cls="navbar-toggler",
                type="button",
                data_bs_toggle="collapse",
                data_bs_target="#navbarNavDropdown",
            )
            self.navbar = tags.div(
                cls="collapse navbar-collapse",
                id="navbarNavDropdown",
            )

    def add(self, *args):
        return self.navbar.add(*args)


class tabs(tags.html_tag):
    tagname = "div"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.nav_tabs = self.add(
            tags.ul(
                cls="nav nav-tabs",
                role="tablist",
            )
        )
        self.tab_content = self.add(
            tags.div(
                cls="tab-content",
            ),
        )


class tabpanel(BootstrapComponent):
    tagname = "div"
    cls = "tab-pane fade"

    def __init__(self, title, parent, *args, active=False, **kwargs):
        self.id = str(uuid.uuid4())
        self.cls += " show active" if active else ""
        super().__init__(
            *args,
            role="tabpanel",
            id=f"{self.id}-pane",
            **kwargs,
        )

        with parent.nav_tabs:
            with tags.li(
                _class="nav-item",
                role="presentation",
            ):
                tags.button(
                    title,
                    _class="nav-link" + (" active" if active else ""),
                    id=f"{self.id}-tab",
                    data_bs_toggle="tab",
                    data_bs_target=f"#{self.id}-pane",
                    role="tab",
                    aria_controls=self.id,
                )

        parent.tab_content.add(self)
        # if active:
        #    self.add_class("show active")
