import ast

@staticmethod
def get_value_from_config(config, section, config_key):
    value = config.get(section, config_key)
    try:
        # Try to parse as an integer
        return int(value)
    except ValueError:
        pass
    try:
        # Try to parse as a list
        return ast.literal_eval(value)
    except (ValueError, SyntaxError):
        pass

    # cant parse, return the original string value
    return value



def custom_title_case(input_sentance):
    SKIP_WORDS = ["of", "the", "and", "or"]
    words = input_sentance.split()
    title_cased_words = []
    for i, word in enumerate(words):
        if i == 0 or word.lower() not in SKIP_WORDS:
            title_cased_words.append(word.capitalize())
        else:
            title_cased_words.append(word.lower())
    return " ".join(title_cased_words)
