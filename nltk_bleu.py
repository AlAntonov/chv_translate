from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import argparse

def argparser():
    Argparser = argparse.ArgumentParser()
    Argparser.add_argument('--reference', type=str)
    Argparser.add_argument('--candidate', type=str)

    args = Argparser.parse_args()
    return args

args = argparser()

reference = open(args.reference, 'r', encoding='utf-8').readlines()
candidate = open(args.candidate, 'r', encoding='utf-8').readlines()

if len(reference) != len(candidate):
    raise ValueError('The number of sentences in both files do not match.')

score = 0.
counter = 0

first_sent = len(reference)
#first_sent = 100
cc = SmoothingFunction()

for i in range(first_sent):
    i_score = sentence_bleu([reference[i].strip().split()], candidate[i].strip().split(), smoothing_function=cc.method2)
    #if i_score > 0.95:
    #print("%d - %f: %s\n%s" % (i, i_score, reference[i], candidate[i]))
    #counter = counter + 1
    score += i_score

score /= first_sent
print("Good count is %d" % counter)
print("The bleu score is: "+str(score))