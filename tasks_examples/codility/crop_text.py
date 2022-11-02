"""
Codility crop the text by limit task.
"""


def solution(message, K):
    # if length of the message is less or equal to limit k
    if len(message) <= K:
        return message
    # if length of message exceeds limit
    else:
        # Cut message by K + 1 -> split by ' ' -> take all except last value of the list
        return ' '.join(message[:K + 1].split(' ')[0:-1])


if __name__ == "__main__":
    test1 = solution("Codibility We test coders", 14)
    test2 = solution("The quick brown fox jumps over the lazy dog", 39)
    test3 = solution("Why not", 100)
    print(test1)
    print(test2)
    print(test3)
