# Problem 64:
#     Odd Period Square Roots
#
# Description:
#     All square roots are periodic when written as continued fractions and can be written in the form:
#         sqrt(N) = a_0 + 1 / (a_1 + 1 / (a_2 + 1 / (a_3 + ...)))
#
#     For example, let us consider sqrt(23):
#         sqrt(23) = 4 + sqrt(23) - 4
#                  = 4 + 1 / (1 / (sqrt(23) - 4))
#                  = 4 + 1 / (1 + (sqrt(23) - 3) / 7)
#
#     If we continue we would get the following expansion:
#         sqrt(23) = 4 + 1 / (1 + 1 / (3 + 1 / (1 + 1 / (8 + ...))))
#
#     The process can be summarised as follows:
#         a_0 = 4, 1 / (sqrt(23) - 4) =     (sqrt(23) + 4) / 7  = 1 + (sqrt(23) - 3) / 7
#         a_1 = 1, 7 / (sqrt(23) - 3) = 7 * (sqrt(23) + 3) / 14 = 3 + (sqrt(23) - 3) / 2
#         a_2 = 3, 2 / (sqrt(23) - 3) = 2 * (sqrt(23) + 3) / 14 = 1 + (sqrt(23) - 4) / 7
#         a_3 = 1, 7 / (sqrt(23) - 4) = 7 * (sqrt(23) + 4) / 7  = 8 +  sqrt(23) - 4
#         a_4 = 8, 1 / (sqrt(23) - 4) =     (sqrt(23) + 4) / 7  = 1 + (sqrt(23) - 3) / 7
#         a_5 = 1, 7 / (sqrt(23) - 3) = 7 * (sqrt(23) + 3) / 14 = 3 + (sqrt(23) - 3) / 2
#         a_6 = 3, 2 / (sqrt(23) - 3) = 2 * (sqrt(23) + 3) / 14 = 1 + (sqrt(23) - 4) / 7
#         a_7 = 1, 7 / (sqrt(23) - 4) = 7 * (sqrt(23) + 4) / 7  = 8 +  sqrt(23) - 4
#
#     It can be seen that the sequence is repeating.
#     For conciseness, we use the notation sqrt(23) = [4;(1,3,1,8)],
#       to indicate that the block (1,3,1,8) repeats indefinitely.
#
#     The first ten continued fraction representations of (irrational) square roots are:
#         sqrt(2)  = [ 1 ; (2) ],          period = 1
#         sqrt(3)  = [ 1 ; (1,2) ],        period = 2
#         sqrt(5)  = [ 2 ; (4) ],          period = 1
#         sqrt(6)  = [ 2 ; (2,4) ],        period = 2
#         sqrt(7)  = [ 2 ; (1,1,1,4) ],    period = 4
#         sqrt(8)  = [ 2 ; (1,4) ],        period = 2
#         sqrt(10) = [ 3 ; (6) ],          period = 1
#         sqrt(11) = [ 3 ; (3,6) ],        period = 2
#         sqrt(12) = [ 3 ; (2,6) ],        period = 2
#         sqrt(13) = [ 3 ; (1,1,1,1,6) ],  period = 5
#
#     Exactly four continued fractions, for N ≤ 13, have an odd period.
#     How many continued fractions for N ≤ 10,000 have an odd period?

from math import floor, sqrt


def is_square(n: int) -> bool:
    """
    Returns True iff `n` is a perfect square.

    Args:
        n (int): Natural number

    Returns:
        (bool): True iff `n` is a perfect square

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(n) == int and n > 0
    s = sqrt(n)
    return int(s) == s


def continued_fraction_period(n: int) -> int:
    """
    Given a non-square number `n`,
      returns the period of the continued-fraction representation of sqrt(n),
      that is, the length of the indefinitely repeating portion of the representation.

    Args:
        n (int): Natural number (assumed non-square)

    Returns:
        (int): Period of continued-fraction representation of sqrt(n)

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(n) == int and n > 0

    # Idea:
    #     Want to find the continued-fraction representation of sqrt(n),
    #       given as a_0, a_1, ...
    #     We can expand this and rephrase this as a set of three sequences: r_i, q_i, and a_i, where
    #         (sqrt(n) - r_i) / q_i = a_i + 1 / (...)
    #
    #     Given N, r_i and q_i, we can determine a_i simply as:
    #         a_i = floor((sqrt(N) - r_i) / q_i)
    #
    #     Knowing N, r_i, q_i, and a_i, we can determine the next values in the sequence.
    #     Drop the `i` subscripts, for readability.
    #     Let b = a{i+1} as well.
    #     The remaining summand can be manipulated into a more desirable form:
    #         a + 1 / (b + ...) = (sqrt(n) - r) / q
    #      => 1 / (b + ...) = (sqrt(n) - r) / q - a
    #      => 1 / (b + ...) = (sqrt(n) - r - a*q) / q
    #      => b + ... = q / (sqrt(n) - r - a*q)
    #                 = q / (sqrt(n) - (r+a*q))
    #                 = q / (sqrt(n) - (r+a*q)) * [(sqrt(n) + (r+a*q))/(sqrt(n) + (r+a*q))]
    #                 = q * (sqrt(n) + (r+a*q)) / (n-(r+a*q)^2)
    #                 = (sqrt(n) + (r+a*q)) / ((n-(r+a*q)^2)/q)
    #                 = (sqrt(n) - (-1*(r+a*q))) / ((n-(r+a*q)^2)/q)
    #
    #     Thus we have let the next values in the sequences be:
    #         r{i+1} = -1 * (r + a*q)
    #         q{i+1} = (n - (r+a*q)^2) / q
    #
    #     When some pair (r_i, q_i) has already been encountered,
    #       the continued fraction has started to repeat,
    #       so we can determine the period based on when that pair was previously seen.

    i, r, q = 0, 0, 1
    pairs = {(r, q): i}
    while True:
        i += 1
        a = floor((sqrt(n)-r)/q)
        r, q = -1*(r + a*q), (n-(r+a*q)**2)//q
        p = (r, q)
        if p in pairs:
            return i - pairs[p]
        else:
            pairs[p] = i


def main(n: int) -> int:
    """
    Returns the number of continued-fraction representations
      of irrational square roots (≤ `n`)
      which have an odd period.

    Args:
        n (int): Natural number

    Returns:
        (int): Number of odd-period irrational square roots (≤ `n`)

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(n) == int and n > 0

    # See `continued_fraction_period` for explanation

    return sum(map(lambda x: (not is_square(x) and continued_fraction_period(x) % 2 == 1), range(2, n+1)))


if __name__ == '__main__':
    maximum_radicand = int(input('Enter a natural number: '))
    odd_period_count = main(maximum_radicand)
    print('Number of square roots of N ≤ {} having an odd-period continued fraction:'.format(maximum_radicand))
    print('  {}'.format(odd_period_count))
