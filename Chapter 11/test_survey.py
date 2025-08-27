import pytest
from survey import AnonymousSurvey  # Import the AnonymousSurvey class to be tested

# ---------- FIXTURE ----------
@pytest.fixture
def language_survey():
    """
    Create an AnonymousSurvey instance with a fixed question.
    This fixture will be available to any test function that includes
    'language_survey' as a parameter.
    """
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey


# ---------- TESTS USING FIXTURE ----------
def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses  # Check if the response is in the list


def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses


# ---------- TESTS WITHOUT FIXTURE ----------
# These tests create their own AnonymousSurvey instance directly

def test_store_single_response_no_fixture():
    """Test storing one response without using the fixture."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses


def test_store_three_responses_no_fixture():
    """Test storing three responses without using the fixture."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses


# ---------- HOW TO RUN TESTS ----------
# In the terminal, run:
# python -m pytest test_survey.py
# Pytest will automatically find and run all functions starting with "test_"
