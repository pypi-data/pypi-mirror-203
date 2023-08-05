try:
    import flet

    from typing import Any, Optional, Union

    from flet import ButtonStyle
    from flet import Control, OptionalNumber
    from flet import Ref
except:
    pass


def close(page: flet.Page):
    page.window_close()
    page.close_in_app_web_view()


def maximize(page: flet.Page):
    if page.window_maximized:
        page.window_maximized = False
    elif not page.window_maximized:
        page.window_maximized = True
    page.update()


def minimize(page: flet.Page):
    page.window_minimized = True
    page.update()


def theme_auto(page: flet.Page):
    page.theme_mode = "system"
    page.update()


def theme_light(page: flet.Page):
    page.theme_mode = "light"
    page.update()


def theme_dark(page: flet.Page):
    page.theme_mode = "dark"
    page.update()


def theme_color(page: flet.Page, color):
    page.theme = page.dark_theme = flet.Theme().use_material3
    page.update()


CLOSE_ID = close

MAXIMIZE_ID = maximize

MINIMIZE_ID = minimize

THEME_AUTO = theme_auto

THEME_LIGHT = theme_light

THEME_DARK = theme_dark


class SwitchThemeButton(flet.IconButton):
    __name__ = "fleter.SwichThemeButton"

    def __init__(self,
                 page: flet.Page,

                 on_click=None,

                 light_icon=flet.icons.BRIGHTNESS_7,
                 dark_icon=flet.icons.BRIGHTNESS_5,
                 system_icon=flet.icons.BRIGHTNESS_AUTO,
                 has_system: bool = True,
                 ):
        super(SwitchThemeButton, self).__init__(
            on_click=on_click,
        )

        self._page = page
        if has_system:
            THEME_AUTO(self._page)
        else:
            THEME_LIGHT(self._page)
        self._light_icon = light_icon
        self._dark_icon = dark_icon
        self._system_icon = system_icon
        self._has_system = has_system

        if self._page.theme_mode == "light":
            self.icon = light_icon
        elif self._page.theme_mode == "dark":
            self.icon = dark_icon
        elif self._page.theme_mode == "system":
            self.icon = system_icon

        if on_click is None:
            self.on_click = lambda _: self.swich_theme()

    @property
    def light_icon(self):
        return self._light_icon

    @light_icon.setter
    def light_icon(self, icon):
        self._light_icon = icon

    @property
    def dark_icon(self):
        return self._dark_icon

    @dark_icon.setter
    def dark_icon(self, icon):
        self._dark_icon = icon

    @property
    def system_icon(self):
        return self._system_icon

    @system_icon.setter
    def system_icon(self, icon):
        self._system_icon = icon

    @property
    def has_system(self):
        return self._has_system

    @has_system.setter
    def has_system(self, has: bool):
        self._has_system = has

    def swich_theme(self):
        if self._has_system:
            if self._page.theme_mode == "light":
                self.icon = self._dark_icon
                THEME_DARK(self._page)

            elif self._page.theme_mode == "dark":
                self.icon = self._system_icon
                THEME_AUTO(self._page)

            elif self._page.theme_mode == "system":
                self.icon = self._light_icon
                THEME_LIGHT(self._page)
        else:
            if self._page.theme_mode == "light":
                self.icon = self._dark_icon
                THEME_DARK(self._page)

            elif self._page.theme_mode == "dark":
                self.icon = self._light_icon
                THEME_LIGHT(self._page)

        self._page.update()


class SwitchThemePopupMenuItem(flet.PopupMenuItem):
    __name__ = "fleter.SwichThemePopupMenuItem"

    def __init__(self,
                 page: flet.Page,

                 *args,

                 text: str = "Toggle Dark Theme",

                 light_icon=flet.icons.BRIGHTNESS_7,
                 dark_icon=flet.icons.BRIGHTNESS_5,

                 **kwargs
                 ):
        self._light_icon = light_icon
        self._dark_icon = dark_icon

        page.theme_mode = "light"

        super().__init__(*args, text=text, checked=False, on_click=lambda evt: self.swich_theme(), **kwargs)

        self._page = page

    def swich_theme(self):
        if self._page.theme_mode == "light":
            self.icon = self._dark_icon
            self.checked = True
            THEME_DARK(self._page)

        elif self._page.theme_mode == "dark":
            self.icon = self._light_icon
            self.checked = False
            THEME_LIGHT(self._page)


class CloseButton(flet.IconButton):
    __name__ = "fleter.CloseButton"

    def __init__(self,
                 page: flet.Page,
                 icon=flet.icons.CLOSE_ROUNDED,
                 on_click=None,
                 ):
        super(CloseButton, self).__init__(icon=icon)

        self._page = page

        if on_click is None:
            self.on_click = lambda _: self.close()

    def close(self):
        CLOSE_ID(self._page)


class MaximizeButton(flet.IconButton):
    __name__ = "fleter.MaximizeButton"

    def __init__(self,
                 page: flet.Page,
                 icon=flet.icons.ZOOM_OUT_MAP_ROUNDED,
                 icon_max=flet.icons.ZOOM_IN_MAP_ROUNDED,
                 on_click=None,
                 ):
        super(MaximizeButton, self).__init__(icon=icon, icon_size=20)

        self._page = page

        self._icon = icon
        self._icon_max = icon_max

        if on_click is None:
            self.on_click = lambda _: self.maximize()

    def maximize(self):
        if self._page.window_maximized:
            self.icon = self._icon
        elif not self._page.window_maximized:
            self.icon = self._icon_max
        MAXIMIZE_ID(self._page)
        self._page.update()


class MinimizeButton(flet.IconButton):
    __name__ = "fleter.MinimizeButton"

    def __init__(self,
                 page: flet.Page,
                 icon=flet.icons.MINIMIZE_ROUNDED,
                 on_click=None,
                 ):
        super(MinimizeButton, self).__init__(icon=icon)

        self._page = page

        if on_click is None:
            self.on_click = lambda _: self.minimize()

    def minimize(self):
        self._page.window_minimized = True
        MINIMIZE_ID(self._page)
        self._page.update()

