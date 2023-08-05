# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: Copyright 2023 David Seaward and contributors

from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Welcome


class HelloScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Welcome()


class HelloApp(App):
    SCREENS = {
        "hello": HelloScreen,
    }

    def on_mount(self) -> None:
        self.push_screen("hello")

    def on_button_pressed(self) -> None:
        self.exit()


def invoke():
    app = HelloApp()
    app.run()


if __name__ == "__main__":
    invoke()
