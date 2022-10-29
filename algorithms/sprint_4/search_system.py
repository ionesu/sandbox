"""
https://contest.yandex.ru/contest/24414/run-report/73252017/
I have a problem here with a memory in the last test 27 :(

You can use hash tables from the standard libraries for this problem.

Timofey writes his search engine.

There are n documents, each of which is a text of words. Based on these documents, it is required to build a search index.
 Requests will be submitted to the system. A query is a set of words.
 Upon request, you need to display the 5 most relevant documents.

The relevance of the document is evaluated as follows: for each unique word from the query, the number of its
occurrences in the document is taken, the resulting numbers for all words from the query are summed up.
The total amount is the relevance of the document. The larger the amount, the more the document fits the request.

Documents are sorted in descending order of relevance. If the relevances of the documents are the same, then by
increasing their serial numbers in the database (that is, in the input data).

Think about cases where queries consist of words that appear in a small number of documents.
What if the same word appears many times in the same document?

Input Format
The first line contains a natural number n — the number of documents in the database (1 ≤ n ≤ 104).

Next n lines contain documents, one per line. Each document consists of several words, the words are separated from
each other by one space and consist of small Latin letters. The length of one text does not exceed 1000 characters.
The text is not empty.

The next line contains the number of requests — a natural number m (1 ≤ m ≤ 104). The next m lines contain queries,
one per line. Each query consists of one or more words. The request is never empty. Words are separated from each other
by one space and consist of small Latin letters. The number of characters in the request does not exceed 100.

Output Format
For each query print on one line the numbers of the five most relevant documents. If there are less than five documents,
print as many as there are. Documents with relevance 0 do not need to be issued.

Input Example:
3
i love coffee
coffee with milk and sugar
free tea for everyone
3
i like black coffee without milk
everyone loves new year
mary likes black coffee without milk

Operations complexity:
filenames_words_index - О(n^2)
search_system - О(mlogm) - where is 'm' - quantity of queries

Spatial complexity: O(n)
"""
from collections import Counter, defaultdict
from typing import List, Tuple, Set


LIMIT = 5


def filenames_words_index(docs: List[List[str]]) -> defaultdict:
    result = defaultdict(dict)

    for doc_index, doc_words in enumerate(docs, start=1):
        for word, count in Counter(doc_words).items():
            result[word][doc_index] = count

    return result


def search_system(docs: List[List[str]], number_of_queries: int, ques: List[Set[str]]):
    filenames_words = filenames_words_index(docs)

    result = [defaultdict(int) for _ in range(number_of_queries)]

    for index in range(number_of_queries):
        for word in ques[index]:
            for doc, count in filenames_words.get(word, {}).items():
                result[index][doc] += count

    return [sorted(i.items()) for i in result]


def read_input() -> Tuple[List[List[str]], int, List[Set[str]]]:
    n = int(input())
    documents = [input().split() for _ in range(n)]

    m = int(input())
    queries = [set(input().split()) for _ in range(m)]

    return documents, m, queries


def print_final_result(r):
    for i in r:
        print(*[doc[0] for doc in sorted(i, key=lambda item: item[1], reverse=True)][:LIMIT])


if __name__ == '__main__':
    documents, m, queries = read_input()
    result = search_system(documents, m, queries)
    print_final_result(result)
