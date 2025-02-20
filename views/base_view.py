from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.navigationdrawer import MDNavigationLayout
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.navigationdrawer import (
    MDNavigationLayout,
    MDNavigationDrawer,
    MDNavigationDrawerMenu,
    MDNavigationDrawerHeader,
    MDNavigationDrawerLabel,
    MDNavigationDrawerDivider,
    MDNavigationDrawerItem,
)
from datetime import datetime

class BaseView(MDApp):
    root_screen = None
    navigation_layout = None
    navigation_drawer = None
    screen_manager = None
    top_app_bar = None
    main_content = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.theme_cls.theme_style = "Light"

        self.root_screen = MDScreen()
        self.navigation_layout = MDNavigationLayout()
        self.screen_manager = MDScreenManager()
        self.navigation_drawer = self.render_navigation_drawer()
        self.main_content = MDScreen()

    def render_navigation_drawer(self):
        navigation_drawer = MDNavigationDrawer(
            MDNavigationDrawerMenu(
                MDNavigationDrawerHeader(
                    title="Menu",
                    # title_color="#4a4939",
                    # text="Header text",
                    spacing="4dp",
                    padding=("12dp", 0, 0, "56dp"),
                ),
                
                MDNavigationDrawerDivider(),
                
                # MDNavigationDrawerItem(
                #     icon = "cog-outline",
                #     text = "Page 1",
                #     on_release = lambda x: self.page_navigation("aaa"),
                # ),
                
                # MDNavigationDrawerItem(
                #     icon = "cog-outline",
                #     text = "Page 2",
                #     on_release = lambda x: self.page_navigation("bbb"),
                # ),
                
                MDNavigationDrawerDivider(),
                
                MDNavigationDrawerLabel(
                    text="System",
                ),
                
                MDNavigationDrawerItem(
                    icon = "cog-outline",
                    text = "System Parameter",
                ),
                
                MDNavigationDrawerDivider(),
            ),
            id="main_navigation_drawer",
            radius=(0, 16, 16, 0),
        )

        return navigation_drawer
    
    def page_navigation(self, page_name):
        self.screen_manager.current = page_name
        self.navigation_drawer.set_state("close")

    def render_top_app_bar(self):
        top_app_bar = MDTopAppBar(
            title = "M Widget",
            elevation=4,
            pos_hint={"top": 1},
            # md_bg_color="#e7e4c0",
            # specific_text_color="#4a4939",
            left_action_items=[
                ['menu', lambda x: self.navigation_drawer.set_state("open")]
            ],
        )

        self.main_content.add_widget(top_app_bar)

    def render_main_content(self):
        self.main_content.add_widget(MDLabel(text="Hello, World!", halign="center"))
    
    def build(self):
        self.render_top_app_bar()
        self.render_main_content()

        self.screen_manager.add_widget(self.main_content)

        self.navigation_layout.add_widget(self.screen_manager)
        self.navigation_layout.add_widget(self.navigation_drawer)

        self.root_screen.add_widget(self.navigation_layout)

        return self.root_screen

if __name__ == "__main__":
    layout = BaseView()
    layout.run()