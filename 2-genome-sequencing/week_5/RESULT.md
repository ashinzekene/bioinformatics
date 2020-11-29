- **Based on the above definition of N50, define N75.**
N75 is the maximal contig length in which all the contigs of at least that length make up three fourth (75%) of the length of the contigs. Take for example the following contigs [10,20,20,40,50,60,60,70]. The total contig length is 330, The contigs 40,50,60,60,70 make up 190, which is greater than 75% of the total contig length

- **Compute N50 and N75 for the nine contigs with the following lengths:**
[20, 20, 30, 30, 60, 60, 80, 100, 200].  

N50 comprises (100, 200) contigs. Answer 100
N75 comprises (60, 60, 80, 100, 200) contigs. Answer 60

**Say that we know that the genome length is 1000. What is NG50?**
NG50 would comprise (60, 60, 80, 100, 200). Answer 60

**If the contig in our dataset of length 100 had a misassembly breakpoint in the middle of it, what would be the value of NGA50?**
The new contigs with the misassembly would be [20, 20, 30, 30, 50, 50, 60, 60, 80, 200]
NGA50 would comprise (60, 80, 200) - Answer 60
