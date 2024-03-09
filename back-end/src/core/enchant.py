import enchant


class EnchantClient:
    def __init__(self):
        self.client = enchant.Dict("en_US")

    def check_word(self, word: str) -> bool:
        return self.client.check(word)
