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
          pip install allennlp_models

After model is finetuned use python finalent.py to generate


                Test data and model output for ENTRUST and various systems is in fairseq/testdata/ folder
                Input partisanfinal.source fallaciesfinal.source 
                Output for ENTRUST partisanfinal.hypo fallaciesfinal.hypo 
                Gold is fallaciesgoldhuman and partisangoldhuman


If you use any data or code please cite us 

                @article{chakrabarty2021entrust,
                  title={ENTRUST: Argument Reframing with Language Models and Entailment},
                  author={Chakrabarty, Tuhin and Hidey, Christopher and Muresan, Smaranda},
                  journal={arXiv preprint arXiv:2103.06758},
                  year={2021}
                }
