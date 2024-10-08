"""Demonstrate simple fixtures."""
# NEXT SESSION DETERMINE AMOUNTS OF THE RANKINGS VIA PRINTING THE RETURN VALUES OF THE FUNCTION 
# AND THAN MOVE ON TO THE OTHER PARTS OF THE EXERCISE. 

import pytest

# CODE PROVIDED BY BRIAN THAT I COMMENTED OUT BECAUSE THE BOOK SAID I NEEDED TO MAKE A FILE OF THE SAME NAME AND WRITE MY OWN FUNCTIONS. 

@pytest.fixture()
def some_data():
    """Return answer to ultimate question."""
    return 42
def test_some_data(some_data):
    """Use fixture return value in a test."""
    assert some_data == 42




@pytest.fixture()
def some_other_data():
    """Raise an exception from fixture."""
    x = 43
    assert x == 42
    return x


def test_other_data(some_other_data):
    """Try to use failing fixture."""
    assert some_other_data == 42



@pytest.fixture()
def a_tuple():
    """Return something more interesting."""
    return (1, "foo", None, {"bar": 23})


def test_a_tuple(a_tuple):
    """Demo the a_tuple fixture."""
    assert a_tuple[3]["bar"] == 32

# strikeouts27 Tests 
# I want this fixture to be able to convert data into a dictionary.
@pytest.fixture()
def setup_dictionary_converter():
    # I want to create dictionaries that will be used in the test.
    texas_rangers_starting_lineup_dictionary = {}
    texas_rangers_reserves_lineup_dictionary = {}
    texas_rangers_starting_lineup_rankings_dictionary = {}
    texas_rangers_reserves_lineup_rankings_dictionary = {}
    yield texas_rangers_starting_lineup_dictionary, texas_rangers_reserves_lineup_dictionary, texas_rangers_starting_lineup_rankings_dictionary, texas_rangers_reserves_lineup_rankings_dictionary

    # after the test is done, I want to clean up the dictionaries.
    texas_rangers_starting_lineup_dictionary = {}
    texas_rangers_reserves_lineup_dictionary = {}
    texas_rangers_starting_lineup_rankings_dictionary = {}
    texas_rangers_reserves_lineup_rankings_dictionary = {}

def test_dictionary_converter(setup_dictionary_converter):


    # here is the data that will be used in the test.
    texas_rangers_starting_lineup = (
            ("Rafael Palmero", "first_base"),
            ("Mark Mclemore", "second_base"),
            ("Corey_Seager", "shortstop"),
            ("Adrian Beltre", "third_base"),
            ("Nolan_Ryan", "pitcher"),
            ("Ivan_Rodriguez", "catcher"),
            ("Rusty_Greer", "center_field"),
            ("Juan Gonzalez", "left_field"),
            ("Adolis_Garcia", "right_field"),
                )   

# here is the other data that will be used in the test.  
    texas_rangers_reserves_lineup = (
            ("Will Clark", "first_base"),  
            ("Michael Young", "second_base"), 
            ("Elvis Andrus", "shortstop"), 
            ("Hank Blalock", "third_base"), 
            ("Kenny Rogers", "pitcher"), 
            ("Jonah Heim", "catcher"),  
            ("Josh Hamilton" "center_field"), 
            ("David Murphy", "left_field"),  
            ("Nelson Cruz", "right_field"), 
    )

    # here is the data that will be used in the test.
    texas_rangers_starting_lineup_rankings = (
            ("Rafael Palmero", "85"),
            ("Mark Mclemore", "80"),  
            ("Corey_Seager", "100"),
            ("Adrian Beltre", "90"),
            ("Nolan_Ryan", "95"),
            ("Ivan_Rodriguez", "95"), 
            ("Rusty_Greer", "90"),  
            ("Juan Gonzalez", "97"), 
            ("Adolis_Garcia", "90"), 
        )
    # here is the other data that will be used in the test.
    texas_rangers_reserves_lineup_rankings = (
            ("Will_Clark", "80"), 
            ("Michael Young", "90"),  
            ("Elvis Andrus", "85"),  
            ("Hank Blalock", "80"),  
            ("Kenny Rogers", "85"),  
            ("Jonah Heim", "85"),  
            ("Josh Hamilton", "95"),  
            ("David Murphy", "80"),  
            ("Nelson Cruz", "80"), 
        )

    # I want to convert the data into a dictionary.
    texas_rangers_starting_lineup = {player:position for player, position in texas_rangers_starting_lineup}
    assert isinstance(texas_rangers_starting_lineup, dict)


def test_total_roster_rankings(setup_dictionary_converter):
        # here is the data that will be used in the test.
    texas_rangers_starting_lineup_rankings = (
            ("Rafael Palmero", 85),
            ("Mark Mclemore", 80),  
            ("Corey_Seager", 100),
            ("Adrian Beltre", 90),
            ("Nolan_Ryan", 95),
            ("Ivan_Rodriguez", 95), 
            ("Rusty_Greer", 90),  
            ("Juan Gonzalez", 97), 
            ("Adolis_Garcia", 90), 
        )
    
    texas_rangers_starting_lineup_total_team_rankings = {player: ranking for player, ranking in texas_rangers_starting_lineup_rankings}
    texas_rangers_starting_lineup_total_team_rankings_dictionary = {player: ranking for player, ranking in texas_rangers_starting_lineup_rankings}

    texas_rangers_starters_score= 0
    for ranking in texas_rangers_starting_lineup_total_team_rankings.values():
        texas_rangers_starters_score += ranking
    print(f" The total rank for the texas rangers starters is {texas_rangers_starters_score}")

    # here is the other data that will be used in the test.
    texas_rangers_reserves_lineup_rankings = (
            ("Will_Clark", 80), 
            ("Michael Young", 90),  
            ("Elvis Andrus", 90),  
            ("Hank Blalock", 80),  
            ("Kenny Rogers", 85),  
            ("Jonah Heim", 85),  
            ("Josh Hamilton", 95),  
            ("David Murphy", 80),  
            ("Nelson Cruz", 80), 
        )
    
    texas_rangers_reserves_lineup_total_team_rankings_dictionary = {player: ranking for player, ranking in texas_rangers_reserves_lineup_rankings}
    texas_rangers_reserves_score= 0
    for ranking in texas_rangers_reserves_lineup_total_team_rankings_dictionary.values():
        texas_rangers_reserves_score += ranking
    print(f" The total rank for the texas rangers reserves is {texas_rangers_reserves_score}")


    assert texas_rangers_starters_score > texas_rangers_reserves_score
    

    
if __name__ == "__main__":
    result = test_dictionary_converter(setup_dictionary_converter)
    pytest.main()

# Fixtures are often one of the trickier parts of pytest for people to get used to.
# Going through the following exercises will
# • help solidify your understanding of how fixtures work,
# • allow you to use different fixture scopes, and
# • internalize the run sequence with the visual output of --setup-show.
# 1. Create a test file called test_fixtures.py.
# 2. Write a few data fixtures—functions with the @pytest.fixture() decorator—that
# return some data (perhaps a list, dictionary, or tuple).
# 3. For each fixture, write at least one test function that uses it.
# 4. Write two tests that use the same fixture.
# 5. Run pytest --setup-show test_fixtures.py. Are all the fixtures run before every test?
# 6. Add scope='module' to the fixture from Exercise 4.
# 7. Re-run pytest --setup-show test_fixtures.py. What changed?
# 8. For the fixture from Exercise 6, change return <data> to yield <data>.
# 9. Add print statements before and after the yield.
# 10. Run pytest -s -v test_fixtures.py. Does the output make sense?
# 11. Run pytest --fixtures. Can you see your fixtures listed?
# 12. Add a docstring to one of your fixtures, if you didn’t include them already.
# Re-run pytest --fixtures to see the description show up.
    



