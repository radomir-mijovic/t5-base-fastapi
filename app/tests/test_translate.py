import pytest
from fastapi.testclient import TestClient

from app.main import app, settings

client = TestClient(app)


def test_should_translate_text_if_no_errors():
    response = client.post(
        f"{settings.TRANSLATE_PREFIX}/translate",
        json={
            "source_language": "English",
            "destination_language": "German",
            "input_text": "How are you?",
        },
    )
    assert response.status_code == 200
    assert response.json() == {"translated_text": "Wie sind Sie?"}


@pytest.mark.parametrize("wrong_language", ["Spanish", "Serbian", "Italian"])
def test_should_return_error_if_source_language_language_is_not_supported(
    wrong_language,
) -> None:
    response = client.post(
        f"{settings.TRANSLATE_PREFIX}/translate",
        json={
            "source_language": wrong_language,
            "destination_language": "German",
            "input_text": "How are you?",
        },
    )

    assert response.status_code == 422
    assert (
        response.json()["detail"][0]["msg"]
        == "value is not a valid enumeration member; permitted:"
        " 'English', 'French', 'German', 'Romanian'"
    )


@pytest.mark.parametrize("wrong_language", ["Spanish", "Serbian", "Italian"])
def test_should_return_error_if_destination_language_language_is_not_supported(
    wrong_language,
) -> None:
    response = client.post(
        f"{settings.TRANSLATE_PREFIX}/translate",
        json={
            "source_language": "English",
            "destination_language": wrong_language,
            "input_text": "How are you?",
        },
    )

    assert response.status_code == 422
    assert (
        response.json()["detail"][0]["msg"]
        == "value is not a valid enumeration member; permitted:"
           " 'English', 'French', 'German', 'Romanian'"
    )
