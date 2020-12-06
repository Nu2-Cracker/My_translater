

def part_of_speech(sententce: str) -> str:
    """
    説明文[品詞]を取得する
    :param sententce: row sentence
    :return: sententce: part of speech
    """
    import re

    def search_pattern(pattern: str) -> str:
        compiled = re.compile(pattern)
        result = compiled.match(sententce)
        sentence = result.group(0).replace("としての", "")
        return sentence

    try:
        pattern = r"(\S+\s\S+)としての"
        sentence = search_pattern(pattern)
        return sentence
    except AttributeError:
        pattern = r"(\S+)としての"
        sentence = search_pattern(pattern)
        return sentence

