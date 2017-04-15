# Xena_assignment

The aim of this assignment is to try to execute a run of ARACNe-AP on Breast Cancer TFs. The data has been downloaded from the link:
https://tcga.xenahubs.net/download/TCGA.BRCA.sampleMap/HiSeqV2 with the list of TFs downloaded from
https://github.com/ucscXena/TF_modules/blob/master/MasterR/Taylor_ARACNe_Interactome_Human.TFs 

A primary run of ARACNe-AP was conducted on unfiltered data and was stopped after ~40 hours of execution. A filtering protocol was put in place in order to remove genes with zero expression in a lot of samples. A second run is currently underway with processing taking place on the filtered data.

ARACNe-AP commands:
- nohup time java -Xmx5G -jar Aracne.jar -e HiSeqV2.txt  -o outputFolder --tfs TF.txt --pvalue 1E-8 --seed 2 --calculateThreshold &
- nohup time java -Xmx5G -jar Aracne.jar -e HiSeqV2.txt  -o outputFolder --tfs TF.txt --pvalue 1E-8 --seed 2 &