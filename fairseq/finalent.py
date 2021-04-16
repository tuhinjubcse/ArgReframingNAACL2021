import torch
from fairseq.models.bart import BARTModel
import os
import time
import numpy as np

from allennlp.predictors.predictor import Predictor
import allennlp_models.pair_classification

predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/mnli_roberta-2020.06.09.tar.gz", "textual_entailment")
os.environ['CUDA_VISIBLE_DEVICES']="1"


datadir = 'connotations'
cpdir = 'checkpoint-'+datadir+'/'
bart = BARTModel.from_pretrained(cpdir,checkpoint_file='checkpoint_best.pt',data_name_or_path=datadir)
filename = 'test'

bart.cuda()
bart.eval()
np.random.seed(4)
torch.manual_seed(4)

count = 1
bsz = 1 
maxb = 256
minb = 7
print("done")
t = 0.7
elem = []
count = 1
f = open(filename+'.hypo','a')
for line in open(filename+'.source'):
    if count>0:
        sline = line.strip()
        maxprob = -1
        final = ''
        for val in [5,10,15,20,25,30,35,40,45,50]:
            with torch.no_grad():
                hypotheses_batch = bart.sample([sline], sampling=True, sampling_topk=val  ,temperature=t ,lenpen=2.0, max_len_b=maxb, min_len=minb, no_repeat_ngram_size=3)
                for hypothesis in hypotheses_batch:
                    hypothesis = hypothesis.replace('\n','')
            x = predictor.predict(hypothesis=sline.replace(' <A0>',''),premise=hypothesis) #.replace('trust <V> ',''),premise=hypothesis)
            if x['probs'][0]>maxprob:
                maxprob = x['probs'][0]
                finale = hypothesis
        f.write(finale+'\n')
    count = count+1
