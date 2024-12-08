import requests


class WikiCategoryCounter:
    """A class for counting the number of entries in the Wikipedia category, grouped by the first letters."""

    def __init__(self, category_page: str, all_letters: bool = False):

        self.category_name = category_page
        # The category may contain category_members not only in the current language,
        # use parameter all_letters to exclude category_members with names in a foreign language from the count
        self.all_letters = all_letters
        if not all_letters:
            #  all_letters=False, generate dict with letters of Russian alphabet
            self.letter_counter: dict = {chr(num): 0 for num in range(ord('А'), ord('Я') + 1)}
            # Adding Russian letter Ё to the alphabet
            self.letter_counter["Ё"] = 0
        else:
            self.letter_counter: dict = {}

    @staticmethod
    def _query(params: dict):
        """GET query to wikipedia API with params"""

        base_url = "https://ru.wikipedia.org/w/api.php"
        params["format"] = "json"
        params["action"] = 'query'
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Error fetching data from Wikipedia API: {e}")

    def update_letter_counter(self, letter):
        """update letter counter"""
        if self.all_letters or letter in self.letter_counter:
            self.letter_counter[letter] = self.letter_counter.get(letter, 0) + 1

    def count_category_members(self):
        """count the number of entries in the Wikipedia category, grouped by the first letters."""
        params = {"list": 'categorymembers',
                  'cmtitle': self.category_name,
                  'cmlimit': 'max'}

        result = self._query(params)
        while True:
            for member in result["query"]["categorymembers"]:
                letter = member['title'][0].upper()
                self.update_letter_counter(letter)

            if "continue" in result:
                params["cmcontinue"] = result["continue"]["cmcontinue"]
                result = self._query(params)
            else:
                break

        return self.letter_counter
