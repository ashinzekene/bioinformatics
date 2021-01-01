# How do we compare biological sequences

The LCS algorithm we developed previously makes it possible to introduce absord indels to sequence comparisons. With these we make alignments that are far too absord to resemeble that which exist in biological systems.

Apart from rewarding matches as we did previously, we need a way of penalizing insertion and deletions (indels) as well as mismatches.

### Scoring matrices
We would still award +1 to __matches__, but also we would penalize __mismatches__ by a positive constant __μ__ (the __mismatch penalty__) and indels by some positive constant __σ__ (the __indel penalty__)


In this example, we set the parameters, μ = 1 and σ = 2, hence the score assigned is __-4__.

![Scoring matrices](./assets/alignment_scoring_example.png)


Biologists have refined this further to allow for the fact that some mutations are more probable than others hence leading to mismatches and different indel penalties. With this, we would use a (k+1) x (k+1) __scoring matrix__ holding the scores of aligning k number of different symbols.

An example scoring matrix for DNA might look like 

![DNA scoring matrix](./assets/alignment_scoring_matrix.png)

   
An example of such scoring matrix is __PAM Scoring Matrices__ (Percentage Allowed Mutation scoring matrices for amino acids)

### Global Alignment
__Global Alignment Problem:__ Find a highest-scoring alignment of two strings as defined by a scoring matrix.  
__Input:__ Two strings and a scoring matrix Score.  
__Output:__ An alignment of the strings whose alignment score (as defined by Score) is maximized over all alignments of the strings.  