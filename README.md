# Project Euler - Problem 64 - Odd Period Square Roots
All square roots are periodic when written as continued fractions and can be written in the form:

$\qquad\sqrt{N} = a_0 + \frac{1}{a_1 + \frac{1}{a_2 + \frac{1}{a_3 + \dots}}}$

For example, let us consider $\sqrt{23}$:

$\qquad\sqrt{23} = 4 + \sqrt{23} - 4 = 4 + \frac{1}{\frac{1}{\sqrt{23}-4}} = 4 + \frac{1}{1+\frac{\sqrt{23}-3}{7}}$

If we continue we would get the following expansion:

$\qquad\sqrt{23} = 4 + \frac{1}{1 + \frac{1}{3 + \frac{1}{1 + \frac{1}{8+\dots}}}}$


The process can be summarised as follows:

$\qquad a_0 = 4, \frac{1}{\sqrt{23}-4} = \frac{\sqrt{23}+4}{7} = 1 + \frac{\sqrt{23}-3}{7}$

$\qquad a_1 = 1, \frac{7}{\sqrt{23}-3} = \frac{7(\sqrt{23}+3)}{14} = 3 + \frac{\sqrt{23}-3}{2}$

$\qquad a_2 = 3, \frac{2}{\sqrt{23}-3} = \frac{2(\sqrt{23}+3)}{14} = 1 + \frac{\sqrt{23}-4}{7}$
 
$\qquad a_3 = 1, \frac{7}{\sqrt{23}-4} = \frac{7(\sqrt{23}+4)}{7} = 8 + \sqrt{23} - 4$

$\qquad a_4 = 8, \frac{1}{\sqrt{23}-4} = \frac {\sqrt{23}+4}{7} = 1 + \frac{\sqrt{23}-3}{7}$

$\qquad a_5 = 1, \frac{7}{\sqrt{23}-3} = \frac{7 (\sqrt{23}+3)}{14} = 3 + \frac{\sqrt{23}-3}{2}$

$\qquad a_6 = 3, \frac{2}{\sqrt{23}-3} = \frac{2(\sqrt{23}+3)}{14} = 1 + \frac{\sqrt{23}-4}{7}$

$\qquad a_7 = 1, \frac{7}{\sqrt{23}-4} = \frac{7(\sqrt{23}+4)}{7} = 8 + \sqrt{23} - 4$

It can be seen that the sequence is repeating.
For conciseness, we use the notation $\sqrt{23} = [4;(1,3,1,8)]$, to indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:

$\qquad\sqrt{2} = [1;(2)]$, period = $1$

$\qquad\sqrt{3} = [1;(1,2)]$, period = $2$

$\qquad\sqrt{5} = [2;(4)]$, period = $1$

$\qquad\sqrt{6} = [2;(2,4)]$, period = $2$

$\qquad\sqrt{7} = [2;(1,1,1,4)]$, period = $4$

$\qquad\sqrt{8} = [2;(1,4)]$, period = $2$

$\qquad\sqrt{10} = [3;(6)]$, period = $1$

$\qquad\sqrt{11} = [3;(3,6)]$, period = $2$

$\qquad\sqrt{12} = [3;(2,6)]$, period = $2$

$\qquad\sqrt{13} = [3;(1,1,1,1,6)]$, period = $5$

Exactly four continued fractions, for $N \leq 13$, have an odd period.

How many continued fractions for $N \leq 10,000$ have an odd period?
