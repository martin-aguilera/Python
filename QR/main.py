from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
import io
import qrcode

# Designate Our .kv design file
Builder.load_file("update_label.kv")


class MyLayout(Widget):
    def press(self):
        # Create variables for our widget
        name = self.ids.name_input.text

        # Update the label
        qr_Load = qrcode.QRCode()
        qr_Load.add_data(name)
        ioStr = io.StringIO()
        qr_Load.print_ascii(out=ioStr)
        ioStr.seek(0)
        a = ioStr.read()
        print(a)
        self.ids.name_label.text = f"[font=consolaz.ttf]{a}[/font]"

        # Clear input box
        self.ids.name_input.text = ""


class QRApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    QRApp().run()
