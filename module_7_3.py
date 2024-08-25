class WordsFinder:
    def __init__(self, *file_name):
        self.file_names = ()
        for name in file_name:
            self.file_names = name

    def get_all_words(self):
        all_words = {}
        for name in [self.file_names]:
            with open(name, 'r', encoding='utf-8') as f:
                s = f.read()
                for ch in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    s = s.replace(ch, '')
                    s = s.replace('\n', ' ')
        all_words[name] = s.split(' ')
        return all_words  # all_words[name]

    def find(self, word):
        all_words = self.get_all_words()
        find_word = {}
        for name, words in self.get_all_words().items():
            for w in words:
                if w.upper() == word.upper():
                    find_word[name] = words.index(w) + 1
        return find_word

    def count(self, word):
        all_words = self.get_all_words()
        count_word = {}
        counter = 0
        for name, words in self.get_all_words().items():
            for w in words:
                if w.upper() == word.upper():
                    counter += 1
            count_word[name] = counter
        return count_word

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
