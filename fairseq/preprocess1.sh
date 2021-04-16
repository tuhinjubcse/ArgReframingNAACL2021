for SPLIT in train val test
do
  for LANG in source target
  do
    python -m examples.roberta.multiprocessing_bpe_encoder \
    --encoder-json encoder.json \
    --vocab-bpe vocab.bpe \
    --inputs "connotations/$SPLIT.$LANG" \
    --outputs "connotations/$SPLIT.bpe.$LANG" \
    --workers 60 \
    --keep-empty;
  done
done
