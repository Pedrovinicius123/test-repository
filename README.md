# test-repository

## Epilogue

An idea I've got

I'm higly suspecting that there is no algorithm that solves a 3-SAT (and forward) problem efficiently, most of the problems have a high time complexity in worst case.
But i have to prove that for **all** problems we have are contained in the worst case. There's a graph that determine it.

![P_neq_NP](https://github.com/user-attachments/assets/14a41604-99a4-4e7b-bfca-8f27e9c8ee61)

 According to [this source](https://www-sciencedirect-com.translate.goog/topics/computer-science/combinatorial-problem): "Combinatorial problems arise in many areas of computer science and other disciplines in which computational methods are applied, such as artificial intelligence, operations research, bioinformatics and electronic commerce. Prominent examples are tasks such as finding shortest or cheapest round trips in graphs, finding models of propositional formulae or determining the 3D-structure of proteins. Other well-known combinatorial problems are encountered in planning, scheduling, time-tabling, resource allocation, code design, hardware design and genome sequencing. These problems typically involve finding groupings, orderings or assignments of a discrete, finite set of objects that satisfy certain conditions or constraints."

 That may be disapointing, but I think that is the right answer: $P \neq NP$. More studies must be done to ensure that. Although, it is very sad for me that this is maybe true...
 
To prove that, we must ensure that there is non-combinatory or heuristic algorithm that can solve, in optimal polinomial time, a SAT problem. This make the graph even more important, because it shows the function $\theta(i) = \frac{\theta!}{i! \cdot (\theta - i)!}$, that is in function of $i$ related to $\theta$ (nothing more, nothing less than $C_{\theta, i}$ in function of $i$, where $i \leq \theta$). In worst case, it leads to huge number of combinations, and for check each of then, we have a high computational complexity. So let's get into it.

## The proof (?)

The algorithm I developed along this research may not be the best to solve an SAT problem, but it sufficient to ensure that there is no combinatory algorithm to solve the problem related to SAT. There is the proof: given an algorithm that takes the intersection of the clauses and gather the non-empty intersections, distribushing then through a series of combinations formed by the own intersections, we can notice something different: in worst cases, the problem suffers a explosive grow on this computational cost. Even if we take every combination rapidly, it would take several time to solve, given the astounding number of iterations necessary to solve it (in worst case). "Is there any way to find the correct combination without needing to iterate between all of then?" **And that is exactly the question, in a informal way, that the P vs NP problem asks**.  
