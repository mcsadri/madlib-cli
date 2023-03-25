def main():
    pass

def read_template(self):
    # self parameter via https://stackoverflow.com/a/43839602
    # tf, tc = template file, template content
    try:
        with open("assets/dark_and_stormy_night_template.txt", "r") as tf:
            tc = tf.read()
            return tc
    except FileNotFoundError:
        return "The template file was not found."



def parse_template():
    pass

def merge():
    pass


main()