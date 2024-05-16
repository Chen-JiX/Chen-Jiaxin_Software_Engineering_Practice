# coding = utf-8
from read_frame import read_frame


def test_score(test):
    score = 0
    ans = read_frame('answer/Answer.png')
    test = read_frame(test)
    for i in range(len(ans)):
        if (ans[i] == test[i]).all():
            score += 10
    return score


def test_score_with_wrong(test):
    score = 0
    wrong = [0 for i in range(10)]
    ans = read_frame('answer/Answer.png')
    test = read_frame(test)
    for i in range(len(ans)):
        if (ans[i] == test[i]).all():
            score += 10
        else:
            wrong[i] += 1
    return score, wrong



