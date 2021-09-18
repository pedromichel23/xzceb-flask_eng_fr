"""This module is ued for translate text from english to french and from french to english"""
import os
from os.path import join, dirname
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.environ['apikey']
URL = os.environ['url']

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)

def english_to_french(english_text):
    """This function translate english text to french text"""
    # Code here
    if isinstance(english_text, str) and not english_text == "none":
        french_text = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        return french_text['translations'][0]['translation']
    return "Type a text in English"


def french_to_english(french_text):
    """This function translate french text to english text"""
    # Code here
    if isinstance(french_text, str) and not french_text == "none":
        english_text = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        return english_text['translations'][0]['translation']
    return "Type a text in French"
