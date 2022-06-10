import kivy
from kivy.app import App
from gerencVentana import AdministrarVentanas

kivy.require('1.11.1')

__version__ = "1.11.1"


class exemploCrud(App):
    def build(self):
        self.root = AdministrarVentanas()
        return self.root


if __name__ == '__main__':
    exemploCrud().run()
