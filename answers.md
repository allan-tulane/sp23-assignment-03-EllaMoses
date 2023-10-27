# CMPS 2200 Assignment 3
## Answers

**Name:** Ella Moses


Place all written answers from `assignment-03.md` here for easier grading.


- **b.**

The recurrence for Work is W(n) = W(n-1) + 1. This is balanced with n levels and constant work at each level so W(n) = O(n).
The recurrence for Span is S(n) = S(n-1) + 1. This is balanced with n levels so S(n) = O(n)

- **d.**

The work for mapping is O(n) and the span for mapping is O(1) since they are all done in parallel
The work for scan is O(n) and the span for scan is O(logn) since we are assuming it is the most efficient version
The work for reduce is  O(n) and the span for reduce is O(logn)

so W(n) = O(n) and S(n) = O(lg n)


- **f.**

The recurrence for Work is W(n) = 2W(n/2) + 1. This is leaf dominated with n leaves on the lowest level so W(n) = O(n)

The recurrence for Span is S(n) = S(n/2) + 1. This is balanced with logn levels so S(n) = O(logn)
