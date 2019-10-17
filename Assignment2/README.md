# Finding spatially close reads falling under the same genomic location
## Using insert sort and linked lists
### Python 3

#### Results obtained for the test sets: 
loci indicates chromosome arms while value counts of pairs of reads (seq i and seq j ) that satisfy the following two conditions:

* seq i and seq j reside on the same chromosome arm
* d(seq i , seq j ) ≤ k, where d(p, q) for two points p, q in 2D space is defined as

nodes of the linked list are represented by [] and links between them with ->

##### input1, k = 1.5
time python main.py input1.txt 1.5

[loci: 2q, value: 1] -> [loci: 5p, value: 0] -> [loci: 5q, value: 0] -> [loci: 8q, value: 0] -> [loci: 11p, value: 1] -> 

real	0m0.067s
user	0m0.060s
sys	0m0.004s

##### input2, k = 1.5
time python main.py input2.txt 1.5

[loci: 1p, value: 2] -> [loci: 1q, value: 2] -> [loci: 2p, value: 3] -> [loci: 2q, value: 3] -> [loci: 3p, value: 0] -> [loci: 3q, value: 4] -> [loci: 4p, value: 1] -> [loci: 4q, value: 0] -> [loci: 5p, value: 3] -> [loci: 5q, value: 0] -> [loci: 6p, value: 0] -> [loci: 6q, value: 3] -> [loci: 7p, value: 1] -> [loci: 7q, value: 3] -> [loci: 8p, value: 3] -> [loci: 8q, value: 4] -> [loci: 9p, value: 1] -> [loci: 9q, value: 0] -> [loci: 10p, value: 1] -> [loci: 10q, value: 0] -> [loci: 11p, value: 1] -> [loci: 11q, value: 5] -> [loci: 12p, value: 2] -> [loci: 12q, value: 2] -> [loci: 13p, value: 0] -> [loci: 13q, value: 0] -> [loci: 14p, value: 0] -> [loci: 14q, value: 0] -> [loci: 15p, value: 3] -> [loci: 15q, value: 0] -> [loci: 16p, value: 0] -> [loci: 16q, value: 1] -> [loci: 17p, value: 4] -> [loci: 17q, value: 2] -> [loci: 18p, value: 2] -> [loci: 18q, value: 2] -> [loci: 19p, value: 1] -> [loci: 19q, value: 3] -> [loci: 20p, value: 3] -> [loci: 20q, value: 1] -> [loci: 21p, value: 1] -> [loci: 21q, value: 0] -> [loci: 22p, value: 4] -> [loci: 22q, value: 3] -> 

real	0m1.417s
user	0m1.400s
sys	0m0.016s

##### input3, k = 1.5

time python main.py input3.txt 1.5

[loci: 1p, value: 13] -> [loci: 1q, value: 21] -> [loci: 2p, value: 22] -> [loci: 2q, value: 23] -> [loci: 3p, value: 12] -> [loci: 3q, value: 23] -> [loci: 4p, value: 20] -> [loci: 4q, value: 15] -> [loci: 5p, value: 20] -> [loci: 5q, value: 23] -> [loci: 6p, value: 27] -> [loci: 6q, value: 25] -> [loci: 7p, value: 13] -> [loci: 7q, value: 20] -> [loci: 8p, value: 25] -> [loci: 8q, value: 11] -> [loci: 9p, value: 8] -> [loci: 9q, value: 17] -> [loci: 10p, value: 21] -> [loci: 10q, value: 20] -> [loci: 11p, value: 18] -> [loci: 11q, value: 18] -> [loci: 12p, value: 8] -> [loci: 12q, value: 28] -> [loci: 13p, value: 25] -> [loci: 13q, value: 17] -> [loci: 14p, value: 23] -> [loci: 14q, value: 14] -> [loci: 15p, value: 25] -> [loci: 15q, value: 19] -> [loci: 16p, value: 14] -> [loci: 16q, value: 16] -> [loci: 17p, value: 37] -> [loci: 17q, value: 21] -> [loci: 18p, value: 21] -> [loci: 18q, value: 24] -> [loci: 19p, value: 8] -> [loci: 19q, value: 16] -> [loci: 20p, value: 16] -> [loci: 20q, value: 22] -> [loci: 21p, value: 15] -> [loci: 21q, value: 15] -> [loci: 22p, value: 14] -> [loci: 22q, value: 19] -> 

real	2m24.159s
user	2m24.096s
sys	0m0.012s


## "Cheating vertion"

Cheating vertion stores chromosome arm as tuple(int(#chrom), arm) so sorting the first linked list is easier. It reduces a lot computation time but as implemented means information loss. However a subclass of lnk_list could be created to store both loci and the new tuple.

##### input3, k = 1.5

time python main_cheating.py input3.txt 1.5

[loci: 1p, value: 13] -> [loci: 1q, value: 21] -> [loci: 2p, value: 22] -> [loci: 2q, value: 23] -> [loci: 3p, value: 12] -> [loci: 3q, value: 23] -> [loci: 4p, value: 20] -> [loci: 4q, value: 15] -> [loci: 5p, value: 20] -> [loci: 5q, value: 23] -> [loci: 6p, value: 27] -> [loci: 6q, value: 25] -> [loci: 7p, value: 13] -> [loci: 7q, value: 20] -> [loci: 8p, value: 25] -> [loci: 8q, value: 11] -> [loci: 9p, value: 8] -> [loci: 9q, value: 17] -> [loci: 10p, value: 21] -> [loci: 10q, value: 20] -> [loci: 11p, value: 18] -> [loci: 11q, value: 18] -> [loci: 12p, value: 8] -> [loci: 12q, value: 28] -> [loci: 13p, value: 25] -> [loci: 13q, value: 17] -> [loci: 14p, value: 23] -> [loci: 14q, value: 14] -> [loci: 15p, value: 25] -> [loci: 15q, value: 19] -> [loci: 16p, value: 14] -> [loci: 16q, value: 16] -> [loci: 17p, value: 37] -> [loci: 17q, value: 21] -> [loci: 18p, value: 21] -> [loci: 18q, value: 24] -> [loci: 19p, value: 8] -> [loci: 19q, value: 16] -> [loci: 20p, value: 16] -> [loci: 20q, value: 22] -> [loci: 21p, value: 15] -> [loci: 21q, value: 15] -> [loci: 22p, value: 14] -> [loci: 22q, value: 19] -> 

real	0m14.044s
user	0m14.020s
sys	0m0.016s

##### input4, k = 1.5

time python main_cheating.py input4.txt 1.5
[loci: 1p, value: 1605] -> [loci: 1q, value: 1775] -> [loci: 2p, value: 1775] -> [loci: 2q, value: 1715] -> [loci: 3p, value: 1853] -> [loci: 3q, value: 1988] -> [loci: 4p, value: 1815] -> [loci: 4q, value: 1812] -> [loci: 5p, value: 1929] -> [loci: 5q, value: 1696] -> [loci: 6p, value: 1821] -> [loci: 6q, value: 1863] -> [loci: 7p, value: 1678] -> [loci: 7q, value: 1686] -> [loci: 8p, value: 1678] -> [loci: 8q, value: 1774] -> [loci: 9p, value: 1740] -> [loci: 9q, value: 1856] -> [loci: 10p, value: 1798] -> [loci: 10q, value: 1845] -> [loci: 11p, value: 1817] -> [loci: 11q, value: 1866] -> [loci: 12p, value: 2022] -> [loci: 12q, value: 1625] -> [loci: 13p, value: 1747] -> [loci: 13q, value: 1844] -> [loci: 14p, value: 1862] -> [loci: 14q, value: 1803] -> [loci: 15p, value: 1755] -> [loci: 15q, value: 1788] -> [loci: 16p, value: 1828] -> [loci: 16q, value: 1814] -> [loci: 17p, value: 1855] -> [loci: 17q, value: 1785] -> [loci: 18p, value: 1796] -> [loci: 18q, value: 1807] -> [loci: 19p, value: 1683] -> [loci: 19q, value: 1855] -> [loci: 20p, value: 1745] -> [loci: 20q, value: 1810] -> [loci: 21p, value: 1747] -> [loci: 21q, value: 1854] -> [loci: 22p, value: 1901] -> [loci: 22q, value: 1898] -> 

real	39m48.481s
user	32m50.316s
sys	0m0.048s

