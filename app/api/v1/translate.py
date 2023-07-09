from fastapi import APIRouter
from transformers import T5ForConditionalGeneration, T5Tokenizer

from app.schemes.translate import TranslationSchema

router = APIRouter()


tokenizer = T5Tokenizer.from_pretrained(
    "t5-base", truncation=True, model_max_length=100
)
model = T5ForConditionalGeneration.from_pretrained("t5-base", return_dict=True)


def text_translate(source_language, destination_language, input_text) -> str:
    """Function to translate user text

    Args:
        source_language: (str) Language to translate from
        destination_language: (str) Language to translate to
        input_text: (str) Text to be translated

    Returns translated text, if fails returns error info
    """
    try:
        input_ids = tokenizer(
            f"translate {source_language} to {destination_language}: {input_text}",
            return_tensors="pt",
        ).input_ids
        output = model.generate(input_ids)

        return tokenizer.decode(output[0], skip_special_tokens=True)

    except:
        return "Something went wrong"


@router.post("/translate")
async def translate(translation: TranslationSchema):
    translated_text = text_translate(
        source_language=translation.source_language,
        destination_language=translation.destination_language,
        input_text=translation.input_text,
    )

    return {"translated_text": translated_text}
