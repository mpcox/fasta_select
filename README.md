# fasta_select

This Python program extracts specified sequences from a fasta file.


INSTALLATION

*fasta_select* requires the *biopython* package. This can be installed with

```
pip install biopython
```


USAGE

Program usage is as follows:

```
fasta_select [-h] [-r lower upper] [-s text_file | -e text_file] FASTA_input_file
```
```
Optional flags:
-h                print help information
-r lower upper    give lower and upper bounds of sequences to extract (base pairs)
-s|selected       name of file listing headers of sequences to extract OR
-e|excluded       name of file listing headers of sequences *not* to extract                       
```


EXAMPLE

```
fasta_select contigs.fasta -s selected_sequences.txt > selected_contigs.fasta
```
