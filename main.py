import threading
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock

API_URL = "https://script.google.com/macros/s/AKfycbxfR2GAm1rP6t8A4_jenG3fT7HsqQn6wfVZ2eG8o8a6_gyVa8YhrrLs418f7BzItUV3/exec"

class TopMarkeetApp(App):
    def build(self):
        self.title = "Top Markeet Auto Lister"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        layout.add_widget(Label(text="Top Markeet - Markaz Lister", font_size='22sp', size_hint_y=None, height=50))

        self.query_input = TextInput(hint_text="Markaz Product Name, Link, or Code", multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.query_input)

        self.profit_input = TextInput(text="300", hint_text="Profit (Default 300)", input_filter='int', multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.profit_input)

        self.submit_btn = Button(text="List on Store.link", size_hint_y=None, height=55, background_color=(0.1, 0.6, 0.2, 1))
        self.submit_btn.bind(on_press=self.send_data)
        layout.add_widget(self.submit_btn)

        self.status_label = Label(text="Ready", font_size='16sp')
        layout.add_widget(self.status_label)

        return layout

    def send_data(self, instance):
        product = self.query_input.text.strip()
        profit = self.profit_input.text.strip() or "300"

        if not product:
            self.status_label.text = "Please enter product name, link or code!"
            return

        self.status_label.text = "Sending to Store.link..."
        self.submit_btn.disabled = True
        threading.Thread(target=self.post_request, args=(product, profit), daemon=True).start()

    def post_request(self, product, profit):
        try:
            payload = {"product": product, "profit": int(profit)}
            response = requests.post(API_URL, json=payload, timeout=15)
            if response.status_code == 200:
                Clock.schedule_once(lambda dt: self.update_ui("Success! Listed on Top Markeet."))
            else:
                Clock.schedule_once(lambda dt: self.update_ui(f"Error: {response.status_code}"))
        except Exception as e:
            Clock.schedule_once(lambda dt: self.update_ui("Connection Failed!"))

    def update_ui(self, message):
        self.status_label.text = message
        self.submit_btn.disabled = False

if __name__ == '__main__':
    TopMarkeetApp().run()
