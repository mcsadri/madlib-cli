import pytest
from madlib_cli.madlib import welcome, read_template, parse_template, merge

# def test_welcome_run():
#     welcome_actual = welcome("RUN")
#     welcome_expected = "run"
#     assert welcome_actual == welcome_expected
#
# def test_welcome_quit():
#     welcome_actual = welcome("QuiT")
#     welcome_expected = "quit"
#     assert welcome_actual == welcome_expected
#
# def test_welcome_invalid_input():
#     welcome_actual = welcome("play")
#     welcome_expected = "Please type RUN or QUIT."
#     assert welcome_actual == welcome_expected

@pytest.mark.skip("pending")
def test_read_template_returns_stripped_string():
    actual = read_template("assets/dark_and_stormy_night_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected

@pytest.mark.skip("pending")
def test_read_template_returns_stripped_string2():
    actual = read_template("assets/make_me_a_video_game_template.txt")
    expected = """Make Me A Video Game!\n\nI the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb} {A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!\n\nWhat are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name}'s Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find."""
    assert actual == expected

@pytest.mark.skip("pending")
def test_read_template_returns_stripped_string_error():
    actual = read_template("assets/make_me_a_vide0_game_template.txt")
    expected = "The template file was not found."
    assert actual == expected


#@pytest.mark.skip("pending")
def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


@pytest.mark.skip("pending")
def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected


@pytest.mark.skip("pending")
def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)