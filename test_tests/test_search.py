import pytest
from test_pages.searchbar import SearchBar

@pytest.mark.usefixtures("login")  # Automatically perform login before this test
class TestQKartSearchBar:

    def test_search_item(self):
        # Initialize SearchBar object
        search_bar = SearchBar(self.driver)

        # Search for 'shoes'
        search_bar.search_item("shoes")
