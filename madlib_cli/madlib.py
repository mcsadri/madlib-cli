import textwrap

template = "assets/make_me_a_video_game_template.txt"
test_template = "assets/dark_and_stormy_night_template.txt"

def main():
    welcome()

def welcome(response = str()):
    print(textwrap.dedent("""
        ********************** Welcome to madlibs_cli.py! **********************
        * One player (the cli) acts as the “reader” and asks the other player  *
        * (that's you), who hasn't seen the story, to fill in the blanks with  *
        * adjectives, nouns, exclamations, colors, adjectives, and more. These *
        * words are inserted into the blanks and then the story is read aloud  *
        * to hilarious results. There are no winners or losers, only laughter. *
        *                                                                      *
        * When you're ready, please type RUN at the prompt. You can also QUIT. *
        ************************************************************************
        """))
    while response != "run" and response != "quit":
        if response:
            print("\nPlease type RUN or QUIT.")
            return "Please type RUN or QUIT."
        response = input ("> ")
        response = response.lower()
        # if response:
        #     print("\nPlease type RUN or QUIT.")
        #     return "Please type RUN or QUIT."
    return response

def read_template(source = template):
    # tf, tc = template file, template contents
    try:
        with open(source, "r") as tf:
            tc = tf.read()
            return tc
    except FileNotFoundError:
        return "The template file was not found."





def parse_template():
    pass

def merge():
    pass


#main()