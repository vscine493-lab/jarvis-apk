from jnius import autoclass

PythonActivity = autoclass("org.kivy.android.PythonActivity")
Intent = autoclass("android.content.Intent")

RecognizerIntent = autoclass(
    "android.speech.RecognizerIntent"
)

def iniciar_reconhecimento():
    intent = Intent(
        RecognizerIntent.ACTION_RECOGNIZE_SPEECH
    )

    intent.putExtra(
        RecognizerIntent.EXTRA_LANGUAGE_MODEL,
        RecognizerIntent.LANGUAGE_MODEL_FREE_FORM
    )

    intent.putExtra(
        RecognizerIntent.EXTRA_LANGUAGE,
        "pt-BR"
    )

    intent.putExtra(
        RecognizerIntent.EXTRA_PROMPT,
        "Diga seu comando"
    )

    PythonActivity.mActivity.startActivityForResult(
        intent,
        1001
    )
