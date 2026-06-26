"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return "un" + word
    """Take the given word and add the 'un' prefix.

    Parameters:
        word (str): The root word.

    Returns:
        str: Root word prepended with 'un'.
    """

    pass


def make_word_groups(vocab_words):
    seperator = ' :: ' + vocab_words[0]
    return seperator.join(vocab_words)
    """Transform a list containing a prefix and words.

    Parameters:
        vocab_words (list[str]): Vocabulary words with prefix at first index.

    Returns:
        str: Prefix followed by vocabulary words with prefix applied.

    This function takes a `vocab_words` list of strings and returns a string
    with the prefix and the words with prefix applied, separated by ' :: '.

    Examples:
        >>> list('en', 'close', 'joy', 'lighten')
        'en :: enclose :: enjoy :: enlighten'.

    """

    pass


def remove_suffix_ness(word):
    base_word = word[:-4]
    if base_word[-1] == 'i':
        return base_word[:-1] + 'y'
    else:
        return base_word
    """Remove the suffix from the word while keeping spelling in mind.

    Parameters:
        word (str): Word to remove suffix from.

    Returns:
        str: Word with suffix removed & spelling adjusted.

    Examples:
        >>> remove_suffix_ness('heaviness')
        'heavy'

        >>> remove_suffix_ness('sadness')
        'sad'

    """

    pass


def adjective_to_verb(sentence, index):
    spec_word = sentence.split()[index]
    if spec_word[-1] == '.':
        return spec_word [:-1] + 'en'
    else:
        return spec_word + 'en'
    
    """Change the adjective within the sentence to a verb.

    Parameters:
        sentence (str): The word used in a sentence as an adjective.
        index (int): Index of the adjective to remove and transform.

    Returns:
        str: The extracted adjective in verb form.

    Examples:
        >>> adjective_to_verb('It got dark as the sun set.', 2)
        'darken'

        >>> adjective_to_verb('The ink stains her fingers black.', -1)
        'blacken'

    """

    pass
