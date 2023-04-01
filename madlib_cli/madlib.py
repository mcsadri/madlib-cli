import textwrap
import re

def main():
    template = welcome()
    ml_file = read_template(template)
    if ml_file != "The template file was not found.":
        ml_stripped, ml_parts = parse_template(ml_file)
        ml_responses = fill_in_the_blank(ml_parts)
        ml_assembled = merge(ml_stripped, ml_responses)
        write_file(template, ml_assembled)
    else:
        print("end")

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
    reply = str()
    print("Pick a madlib. 1 (for test) or 2 (for full):")
    while reply != 1 and reply != 2:
        reply = input("> ")
        if reply == "1":
            return "assets/dark_and_stormy_night_template.txt"
        elif reply == "2":
            return "assets/make_me_a_video_game_template.txt"

def read_template(source):
    # tf, tc = template file, template contents
    # try to open madlibs file source, read contents, and send contents to parse_template()
    with open(source, "r") as tf:
        tc = tf.read()
        return tc

def parse_template(string):
    # set regex pattern to match madlibs blanks; regex/findall solution assisted by ChatGPT
    pattern = r'\{([^}]*)\}'
    # set parts = a tuple containing the madlibs blanks from the string
    parts = tuple(re.findall(pattern, string))
    # set stripped = source string with the madlibs blanks removed replacing the regex matches with empty {}
    stripped = re.sub(pattern, "{}", string)
    # send stripped and parts to the merge()
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
    return story

def write_file(loc, finished):
    file_name = loc.replace("template", "output")
    with open(file_name, "w") as output:
        output.write(finished)

main()