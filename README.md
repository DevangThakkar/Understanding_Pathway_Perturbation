# Understanding Pathway Perturbation

The aim of this assignment is to understand and implement algorithms to:

* create a regulatory network from gene expression data,
* calculate a score and thus, the rankings for individual pathways for each sample.

Selected iterature on inference of regulatory networks includes [[1]](https://doi.org/10.1038/ng1532)(ARACNE-Mutual information), [[2]](https://doi.org/10.1093/bioinformatics/btw216)(ARACNE-Mutual information), [[3]](https://www.ncbi.nlm.nih.gov/pubmed/10902190)(Mutual information), [[4]](https://doi.org/10.1038/ng.3593)(VIPER), [[5]](https://doi.org/10.1038/msb.2010.31)(MARINa), [[6]](https://doi.org/10.1038/ng.3168)(HotNet2) and [[7]](https://doi.org/10.1093/bioinformatics/btt471)(TieDIE). Some review papers on network inference: [[8]](https://doi.org/10.1016/j.biosystems.2008.12.004), [[9]](https://www.nature.com/articles/nmeth.2016), and [[10]](10.3389/fcell.2014.00038) 

ARACNE-AP [atry to execute a run of ARACNe-AP on Breast Cancer TFs. The data has been downloaded from the link:
https://tcga.xenahubs.net/download/TCGA.BRCA.sampleMap/HiSeqV2 with the list of TFs downloaded from
https://github.com/ucscXena/TF_modules/blob/master/MasterR/Taylor_ARACNe_Interactome_Human.TFs 

A primary run of ARACNe-AP was conducted on unfiltered data and was stopped after ~40 hours of execution. A filtering protocol was put in place in order to remove genes with zero expression in a lot of samples. Further runs on a 4 CPU machine with 30G of memory lead to execution of a bootstrap taking ~50 minutes to complete.

ARACNe-AP commands:
- `nohup time java -Xmx25G -jar Aracne.jar -e HiSeqV2.txt  -o outputFolder --tfs TF.txt --pvalue 1E-8 --seed 1 --calculateThreshold --threads 4 &`
- ```
  for i in {1..10}
  do
  java -Xmx25G -jar Aracne.jar -e HiSeqV2_Filtered_10.txt  -o outputFolder --tfs TF.txt --pvalue 1E-8 --seed $i --threads 4
  done
  ```
- `nohup time java -Xmx25G -jar Aracne.jar -o outputFolder --consolidate &`


A summary of number of identifiers which have zero expression:
--------------------------------------------------------------

- Number of identifiers with at least one zero expression instance: 7873
- Number of identifiers with at least 10 per cent zero expression instance: 4501 (Chosen)
- Number of identifiers with at least 25 per cent zero expression instance: 3704
- Number of identifiers with at least 50 per cent zero expression instance: 2857
- Number of identifiers with at least 75 per cent zero expression instance 2056
- Number of identifiers with at least 90 per cent zero expression instance 1452
