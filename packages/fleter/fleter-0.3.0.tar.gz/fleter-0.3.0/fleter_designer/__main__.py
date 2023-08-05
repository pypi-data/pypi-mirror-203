from flet import *
from flet.flet import *
from flet_core import *
from flet_core.theme import *
from flet_core.icons import *
from flet_core.colors import *
from fleter import *

if __name__ == '__main__':
    def main(page: Page):
        page_hearderbar = HeaderBar(page)
        page_hearderbar.show()

        page_appbar = AppBar(
            leading=Icon(flet),
            leading_width=40,
            center_title=False,
            title= Text("AppBar Example"),
            bgcolor=BLUE_500,
            actions=[
                PopupMenuButton(
                    items=[
                        SwitchThemePopupMenuItem(page=page)
                    ]
                ),
                Divider(),
            ],
        )

        print(f"Platform :: {page.platform}")

        page.appbar = page_appbar

        page.update()


    app(target=main, view=WEB_BROWSER)
