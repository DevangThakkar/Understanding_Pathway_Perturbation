# Understanding Pathway Perturbation
*Self-undertaken project*

The aim of this assignment is to understand and implement algorithms to:

* create a regulatory network from gene expression data,
* calculate a score and thus, the rankings for individual pathways for each sample.

Selected iterature on inference of regulatory networks includes [[1]](https://doi.org/10.1038/ng1532)(ARACNE-Mutual information), [[2]](https://doi.org/10.1093/bioinformatics/btw216)(ARACNE-Mutual information), [[3]](https://www.ncbi.nlm.nih.gov/pubmed/10902190)(Mutual information), [[4]](https://doi.org/10.1038/ng.3593)(VIPER), [[5]](https://doi.org/10.1038/msb.2010.31)(MARINa), [[6]](https://doi.org/10.1038/ng.3168)(HotNet2) and [[7]](https://doi.org/10.1093/bioinformatics/btt471)(TieDIE). Some review papers on network inference: [[8]](https://doi.org/10.1016/j.biosystems.2008.12.004), [[9]](https://www.nature.com/articles/nmeth.2016), and [[10]](10.3389/fcell.2014.00038) 

ARACNE-AP [2](https://doi.org/10.1093/bioinformatics/btw216) was executed on a gene expression dataset for Breast Cancer transcription factors. The data has been downloaded from the link: https://tcga.xenahubs.net/download/TCGA.BRCA.sampleMap/HiSeqV2.gz with the list of TFs downloaded from https://github.com/ucscXena/TF_modules/blob/master/MasterR/Taylor_ARACNe_Interactome_Human.TFs

### Execution Notes:
A primary run of ARACNe-AP was conducted on unfiltered data and was stopped after ~40 hours of execution on a single CPU machine. [A filtering protocol](../master/check_zeros.py) was put in place in order to remove genes with zero expression in at least *xx* per cent of the samples (where *xx* is one of 10, 25, 50, 75, 90). Further runs on a 4 CPU GCE machine (30G memory) lead to execution of individual bootstraps taking ~50 minutes to complete.

Python script to generate filtered file (Input: HiSeqV2.txt, Output: HiSeqV2_Filtered_*xx*.txt)
- `python check_zeros.py`

ARACNe-AP commands: (increasing java heap size to 25G with multi-threading over 4 threads)
- `nohup time java -Xmx25G -jar Aracne.jar -e HiSeqV2_Filtered_10.txt  -o outputFolder --tfs TF.txt --pvalue 1E-8 --seed 1 --calculateThreshold --threads 4 &`
- ```
  for i in {1..10}
  do
  java -Xmx25G -jar Aracne.jar -e HiSeqV2_Filtered_10.txt  -o outputFolder --tfs TF.txt --pvalue 1E-8 --seed $i --threads 4
  done
  ```
- `nohup time java -Xmx25G -jar Aracne.jar -o outputFolder --consolidate &`


### A summary of number of identifiers which have zero expression:

- Number of identifiers with at least one zero expression instance: 7873
- Number of identifiers with at least 10 per cent zero expression instance: 4501 (Chosen)
- Number of identifiers with at least 25 per cent zero expression instance: 3704
- Number of identifiers with at least 50 per cent zero expression instance: 2857
- Number of identifiers with at least 75 per cent zero expression instance 2056
- Number of identifiers with at least 90 per cent zero expression instance 1452

Output: On consolidating the bootstraps, we get a [network](../master/output/network.txt) in the form of edges with high MI values and p values below a calculated threshold [(0.02792)](../master/output/miThreshold_p1E-8_samples1218.txt). For example, we can identfy all the downstream 
## Calculating scores for a pathway for individual samples

Having inferred the network from the gene expression data, the task now is to calculate a sample-specific score for an individual pathway. The pathway considered is the [FOXM1 pathway](../master/FOXM1.network), an important regulator often overexpressed in cancer [[11]](https://doi.org/10.1158/0008-5472.CAN-11-0640). The FOXM1 pathway has been visualized using the UCSC Xena [Visualization Browser](https://xenabrowser.net/heatmap/) and can be found [here](../master/FOXM1_viz.png).

Literature in this area includes: [[12]](https://doi.org/10.1371/journal.pcbi.1000792)(DIRAC), [[13]](https://doi.org/10.1101/gr.150904)(NetProphet), [[14]](https://doi.org/10.1073/pnas.1219651110)(Pathifier) and [[15]](https://doi.org/10.1186/s12859-017-1711-z)(GRAPE).

We use GRAPE [[15]](https://doi.org/10.1186/s12859-017-1711-z) rank create a score for the pathways, available [here](../master/pathway_scores.txt). We see from the [visualization](../master/FOXM1_viz.png) of the FOXM1 pathway that most genes in the FOXM1 pathway are overregulated at the same time as FOXM1. Since the samples have been sorted by decresaing regulation of FOXM1, the pathway scores obtained must also follow a negative trend, which is seen from a [graph](../master/FOXM1_Pathway_scores_plot.pdf) of the pathway scores.
