- The two tasks of the IR HW4 are placed in two different directories:
HW4_Task1 and HW4_Task2

TASK 1: (HW4_Task1 directory)

The following files and folders provide inputs to HW4_Task1\src\HW4_Task1\HW4.java:
1) The directory 'Tokenization_Outputs' which contains output of HW3 Task1
2) The file 'Queries.txt' which contains a list of queries to be searched for.

Steps to run Task1:
1) Open Eclipse
2) click on File, select 'Open Projects from File System...'
3) Select 'HW4_Task1' directory and press 'Finish'
4) Right click on 'HW4_Task1\src\HW4_Task1\HW4.java' from the Package Explorer,
   and select 'Run As' -> 'Java Application' to compile and run 'HW4.java'

The outputs include:
1) 'Indexes' directory which contains index files on indexing the files in 'Tokenization_Outputs'
2) 'Scores.txt' which contains top 100 ranked documents found, according to the scoring algorithm used by Lucene
   for each of the queries in 'Queries.txt'.

 TASK 2: (HW4_Task2 directory)

The following files provide inputs to HW4_Task2\task2.py:
1) 'Document_IDs.txt' which contains a list of 1000 DocIDs
2) 'Global_statistics.txt' which contains information like Average Document Length
   and each document's length
3) 'Queries.txt' which contains a list of queries to be searched for
4) 'Unigrams.txt' which is the output of HW3 Task 2, containing all the unigrams
   along with the docIDs which contain them along with the corresponding term frequency

Steps to run Task2:
1) Open comand prompt
2) Navigate to where you have placed 'HW4_Task2\task2.py'
3) Enter the command:
   > python task2.py
   And press Enter

The output file is:
1) 'Scores.txt' which contains top 100 ranked documents found, by using Okapi BM25 algorithm
   for each of the queries in 'Queries.txt'


Contents apart from 'HW4_Task1' and 'HW4_Task2' directories in HW4:
1) 'Extensive Comparison.txt' containing comparision between top 5 search results for each
   of the 9 queries in 'Queries.txt'
2) 'Implementation Report' containing short description of how both the tasks have been implemented
3) 'README.txt' containing steps to run each of the two tasks

PS - The 18 tables each containing at MOST 100 docIDs ranked by score are placed in two files:
1) HW4_Task1\Scores.txt - 9 tables
2) HW4_Task2\Scores.txt - 9 tables