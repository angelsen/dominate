from . import tags


class BootstrapComponent(tags.html_tag):
    def __init__(self, *args, **kwargs):
        bs_class = type(self).__name__.replace("_", "-").lower()
        user_classes = kwargs.pop("_class", "") + " " + kwargs.pop("cls", "")
        all_classes = " ".join(filter(None, [bs_class, user_classes.strip()]))

        super().__init__(*args, **kwargs, _class=all_classes)


class navbar(BootstrapComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            tagname="nav",
        )


class navbar_brand(BootstrapComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            tagname="a",
            href="#",
        )


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


class navbar_toggler(btn):
    def __init__(self, *args, **kwargs):
        # kwargs["type"] = "button"
        super().__init__(*args, **kwargs, type="submit")


class navbar_collapse(BootstrapComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            tagname="div",
        )


class navbar_nav(BootstrapComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            tagname="ul",
        )


class nav_item(BootstrapComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            tagname="li",
        )


class nav_link(BootstrapComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            tagname="a",
            aria_current="page",
            href="#",
        )


class dropdown_menu(BootstrapComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            tagname="ul",
        )


class dropdown_item(BootstrapComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            tagname="a",
            href="#",
        )


class row(BootstrapComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            tagname="div",
        )


class col(BootstrapComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            tagname="div",
        )


class container(BootstrapComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            tagname="div",
        )


class btn_group(BootstrapComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            tagname="div",
        )


class collapse(BootstrapComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            tagname="div",
        )


class form_control(BootstrapComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            tagname="input",
        )


class card(BootstrapComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            tagname="div",
        )


class card_body(BootstrapComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            tagname="div",
        )


class bold(BootstrapComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            tagname="div",
        )
