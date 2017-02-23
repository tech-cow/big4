
## SORTING ALGORITHMS

往往不同编程语言中会有一个内置的sort包，但因为特殊需要可以选择性的编写不同的逻辑。
在选择使用特定的Algorithm的时候，需要考虑以下几点
* How much data is to be sorted?
* Does the data fit in memory?
* Is the data already mostly sorted?
* How much additional memory does the algorithm require?
* Is relative order preserved?


### Merge Sort

* 英语定义：Merge sort is another divide-and-conquer algorithm that works by splitting a data set into two or more subsets, sorting the subsets, and then merging them together into the final sorted set.

* 个人理解：把Array对半分解，直到每个Array里面只有一个数，然后在开始对这些subset进行排序，排序完了进行合并，直到合并完成

* 优点：O(nLogn)，在大型的数据中，运行时间最短
* 缺点：需要更多的Space，因为需要不停的增加新的list
