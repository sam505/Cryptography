def decode(text):
    dictionary = {}
    for letter in text:
        if letter.isalpha():
            try:
                dictionary[letter] += 1
            except KeyError:
                dictionary[letter] = 1
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    print(sorted_dict)
    return sorted_dict


def main():
    encoded_text = open("in.txt").read()
    result = decode(encoded_text)
    # tr ’hqwslyrbfgkaznptivuox’ ’THEASUDIPNORYGLCFMVWB’ < in.txt > out.txt

if __name__ == "__main__":
    main()
