import textwrap
import re

template = "assets/make_me_a_video_game_template.txt"
test_template = "assets/dark_and_stormy_night_template.txt"

def main():
    welcome()

def welcome(response = str()):
    print(textwrap.dedent("""
        *********************** Welcome to madlibs_cli.py! ***********************
        *  One player (the cli) acts as the “reader” and asks the other player   *
        *  (that's you), who hasn't seen the story, to fill in the blanks with   *
        *  adjectives, nouns, exclamations, colors, adjectives, and more. These  *
        *  words are inserted into the blanks and then the story is read aloud   *
        *  to hilarious results. There are no winners or losers, only laughter.  *
        **************************************************************************
        """))
    read_template()

def read_template(source = test_template):
#def read_template(source = template):
    # tf, tc = template file, template contents
    # try to open madlibs file source, read contents, and send contents to parse_template()
    try:
        with open(source, "r") as tf:
            tc = tf.read()
            parse_template(tc)
            return tc
    # if madlibs file source is not found return error message
    except FileNotFoundError:
        return "The template file was not found."

def parse_template(string):
    # set regex pattern to match madlibs blanks; regex/findall solution assisted by ChatGPT
    pattern = r'\{([^}]*)\}'
    # set parts = a tuple containing the madlibs blanks from the string
    parts = tuple(re.findall(pattern, string))
    # set stripped = source string with the madlibs blanks removed replacing the regex matches with empty {}
    stripped = re.sub(pattern, "{}", string)
    # send stripped and parts to the merge()
    merge(stripped, fill_in_the_blank(parts))
    return stripped, parts

def fill_in_the_blank(prompts):
    answers = []
    for _ in prompts:
        print(f" Please enter a {_}:")
        answers.append(input("> "))
    return answers

def merge(story, responses):
    for _ in responses:
        story = re.sub(r'{}', _, story, 1)
    print(story)
    write_file(story)
    return story

def write_file(output):
    pass

main()