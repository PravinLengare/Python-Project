import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):

    """
    Scrape information from LinkedIn profile.
    If mock is True, returns mock data from a GitHub Gist.
    If False, fetches data from an external API using a real LinkedIn URL.
    """
    if mock:
        # Use mock data from a GitHub Gist
        mock_url = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/faa5b7b8d5aebfe8f6a17b4312adb25710e35d6f/eden-marco.json"
        response = requests.get(mock_url, timeout=10)
        return response.json()
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"  # Replace with actual endpoint if different
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(api_endpoint, params=params, timeout=20)

    data = response.json().get("person")
    return data

if __name__ == "__main__":
    profile_data = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/eden-marco/",
        mock=False  # Set to False when using actual API
    )
    print(profile_data)
