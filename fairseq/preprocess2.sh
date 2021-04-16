fairseq-preprocess \
  --source-lang "source" \
  --target-lang "target" \
  --trainpref "connotations/train.bpe" \
  --validpref "connotations/val.bpe" \
  --destdir "connotations/" \
  --workers 60 \
  --srcdict dict.txt \
  --tgtdict dict.txt;
