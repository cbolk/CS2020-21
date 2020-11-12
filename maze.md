A Maze
A classical _maze_, or labyrinth, is a unique path (eventually particularly intricated), with no two alternative valid routes, from start to finish. 

A maze of words is a concatenation of words fulfilling a set of rules, such that from the starting word it is possible to get to the finishing word, passing through all words, once and only once.

The words can be connected if, given one word, it is possible to obtain the next one:
1. if they are the anagram of each other (for example: ``scar`` and ``cars`` -- same characters in a different order)
2. by changing one character in a different one (for example: ``core`` and ``care``)
3. by adding a character (for example: ``sore`` and ``store``)
4. by removing a character (for example: ``found`` and ``fund``)

Write a program that receives in input the name of the file containing the sequence of words constituting the initial problem, and the name of the file containing a sequence of words _expected_ to be the solution. The program *verifies* that the content of the second file is a solution: if it is, it outputs "True", "False" otherwise.

To be a correct solution:
+ the sequence must have all words, and each word must appear only once;
+ between two subsequent words, one of the four above rules must hold.

big, bind, bing, blind, dead, deal, deed, dig, dog, goad, god, gold, good, lead, load

deed, dead, deal, lead, load, goad, gold, good, god, dog, dig, big, bing, bind, blind
