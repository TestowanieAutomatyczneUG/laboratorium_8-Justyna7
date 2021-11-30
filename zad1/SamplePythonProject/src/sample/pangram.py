def is_pangram(word):
    if isinstance(word, str):
        a = "qwertyuiopasdfghjklzxcvbnm"
        w = set(word.lower())
        for i in a:
            if i not in w:
                return False
        return True
    else:
        raise Exception("Typ musi miec warosc String")