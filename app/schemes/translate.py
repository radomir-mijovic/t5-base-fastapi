from enum import Enum

from pydantic import BaseModel


class SupportedLanguages(str, Enum):
    english = "English"
    french = "French"
    german = "German"
    romanian = "Romanian"


class TranslationSchema(BaseModel):
    source_language: SupportedLanguages
    destination_language: SupportedLanguages = SupportedLanguages.german
    input_text: str = "Enter text for translation"
