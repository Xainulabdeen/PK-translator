# views.py
from django.shortcuts import render, HttpResponse
from translate import Translator

# Available languages with their corresponding language codes
LANGUAGES = {
    "English": "en",
    "Urdu": "ur",
    "Sindhi": "sd",
    "Pashto": "ps",
    "Arabic": "ar",
}

def home(request):
    if request.method == "POST":
        text = request.POST["translate"]
        language = request.POST["language"]

        # Check if the language is supported
        lang_code = LANGUAGES.get(language)
        if lang_code:
            try:
                translator = Translator(to_lang=lang_code)
                translation = translator.translate(text)
                return HttpResponse(translation)
            except Exception as e:
                return HttpResponse(f"Error during translation: {e}")
        else:
            return HttpResponse("Selected language is not supported for translation.")

    return render(request, "main/index.html", {"languages": LANGUAGES.keys()})
