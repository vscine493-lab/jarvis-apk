from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

from android.permissions import request_permissions, Permission
from jnius import autoclass


class JarvisApp(App):

    def build(self):
        request_permissions([
            Permission.RECORD_AUDIO,
        ])

        self.status = Label(
            text="JARVIS ONLINE\n\nMicrofone autorizado.\n\nDiga: JARVIS",
            halign="center",
            valign="middle"
        )

        Clock.schedule_once(self.preparar, 1)

        return self.status

    def preparar(self, *args):
        self.status.text = (
            "JARVIS ONLINE\n\n"
            "Sistema preparado.\n\n"
            "Aguardando palavra de ativação..."
        )

    def abrir_site(self, url):
        PythonActivity = autoclass(
            "org.kivy.android.PythonActivity"
        )
        Intent = autoclass(
            "android.content.Intent"
        )
        Uri = autoclass(
            "android.net.Uri"
        )

        intent = Intent(
            Intent.ACTION_VIEW,
            Uri.parse(url)
        )

        PythonActivity.mActivity.startActivity(intent)


    def on_pause(self):
        return True


    def on_resume(self):
        self.status.text = (
            "JARVIS ONLINE\n\n"
            "Aguardando JARVIS..."
        )


JarvisApp().run()
