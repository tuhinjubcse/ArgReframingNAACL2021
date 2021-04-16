# ArgReframingNAACL2021


pip install torch==1.3.1

In the fairseq/connotations folder you can put the train.source , train.target , val.source , val.target files
The data and model is available on request as we understand that our data can be misused for generations and manipulation

Please email tuhin.chakr@cs.columbia.edu / smara@cs.columbia.edu and fill the form
https://docs.google.com/forms/d/e/1FAIpQLSdM3qRWHV4lgpIkRkZ74YwS2haD6qUTrzujsasJpaBbH9EnQA/viewform?usp=sf_link


Change the encoder.json path to correct path in fairseq/fairseq/data/encoder/gpt2_bpe_utils.py line 131

run sh preprocess1.sh
run sh preprocess2.sh
run sh trainbart.sh


pip install allennlp==1.0.0

After model is finetuned use python finalent.py to generate
Test data and model output for ENTRUST is in fairseq/testdata/ folder
