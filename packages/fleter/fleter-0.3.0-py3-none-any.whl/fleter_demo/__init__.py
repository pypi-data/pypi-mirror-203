import flet
import fleter
import flet_core

def run():
    def main(page: flet.Page):
        headerbar = fleter.HeaderBar(page, has_close=True, has_minimize=True, has_maximize=True)
        headerbar.controls.insert(1, fleter.SwitchThemeButton(page))
        headerbar.controls.insert(
            2,
            flet.PopupMenuButton(
                items=(
                    fleter.PopupColorItem(flet_core.colors.BLUE_500, "Blue")
                )
            )
        )

        combobox = fleter.ComboBox(
            options=[
                "normal",
                ("disabled", True),
                ("active", False),
            ]
        )

        notebook = fleter.NoteBook()
        notebook.add_control_with_can_close(
            "ComboBox",
            combobox,
            close_tip=True,
        )

        page.add(
            headerbar,
            notebook,
        )
        page.update()

        print(page.controls)

    flet.app(target=main)

if __name__ == '__main__':
    run()
