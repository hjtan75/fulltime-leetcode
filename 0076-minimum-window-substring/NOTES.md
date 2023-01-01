* The solution called for O(n + m) with sliding window as the solution
* The naive method would be try every possible substring, then check whether all character is included. This take O(n^3)
​
### First approarch
* Two pointer method as the slilding window O(n)
* A dictionary will keep track of the number of character existed O(m)
* Total time complexity: O(nm)
​
​