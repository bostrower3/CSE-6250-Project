# CSE-6250-Project
Project for CSE-6250
- bostrower3
- npatel484

Dependencies:

- Python==3.7
- pytorch==1.0
- gensim==3.8.3
- matplotlib==3.3.2
- nltk==3.5
- numpy==1.20.3
- pandas==1.1.5
- scikit_learn==1.0.1
- scipy==1.7.3
- spacy==2.3.2
- tensorflow==1.13.1
- tflearn==0.5.0
- tqdm==4.49.0

Preprocessing:

Before you run the preprocessing script, you will need to obtain access to the MIMIC-III dataset. You may apply for that using this [link](https://physionet.org/content/mimiciii/1.4/).

Once you have been granted permissions to the dataset, download D_ICD_DIAGNOSES.csv and D_ICD_PROCEDURES.csv from the MIMIC-III dataset, decompress them, and add them to caml-mimic/mimicdata.

Update MODEL_DIR and DATA_DIR variables in caml-mimic/constants.py. 

Execute CSE-6250-Project/caml-mimic/notebooks/dataproc_mimic_III.ipynb in it's entirity. 

To train the HLAN model, see the procedure [here](https://github.com/bostrower3/CSE-6250-Project/tree/main/Explainable-Automated-Medical-Coding%20-%20Copy#how-to-train-on-new-data): 

Original Authors:
- Hang Dong 
- Víctor Suárez-Paniagua 
- William Whiteley 
- Honghan Wu

Preprocessing author:
- James Mullenbach


