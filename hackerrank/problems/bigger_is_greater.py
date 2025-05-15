"""
http://hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=false
"""

import heapq


def bigger_is_greater(w):
    """
    Finds the smallest lexicographically greater string by rearranging characters of w.

    Args:
        w: The input word (string).

    Returns:
        The smallest lexicographically greater string, or "no answer" if none exists.
        Uses a max heap (simulated with heapq min-heap) for sorting the suffix.
    """
    import ipdb; ipdb.set_trace()
    chars = list(w)
    n = len(chars)

    # 1. Find the largest index i such that chars[i] < chars[i+1]
    # (Scan from right-to-left)
    pivot_index = -1
    for i in range(n - 2, -1, -1):
        if chars[i] < chars[i+1]:
            pivot_index = i
            break

    # 2. If no such index exists, the sequence is already sorted in descending order
    if pivot_index == -1:
        return "no answer"

    pivot_char = chars[pivot_index]

    # 3. Find the smallest character in the suffix chars[pivot_index+1:]
    #    that is strictly greater than pivot_char. Find its rightmost index.
    suffix_chars = chars[pivot_index + 1:]
    smallest_greater_char = None
    swap_suffix_index = -1 # Index relative to the start of the suffix

    for k in range(len(suffix_chars)):
        current_char = suffix_chars[k]
        if current_char > pivot_char:
            # If this is the first greater char found, or
            # if it's smaller than the current best, update.
            # If it's equal to the current best, update (to get rightmost).
            if smallest_greater_char is None or current_char <= smallest_greater_char:
                smallest_greater_char = current_char
                swap_suffix_index = k

    # The actual index in the original list 'chars'
    swap_index = pivot_index + 1 + swap_suffix_index

    # 4. Swap the pivot character with the found character
    chars[pivot_index], chars[swap_index] = chars[swap_index], chars[pivot_index]

    # 5. Sort the suffix starting from pivot_index + 1 in ascending order.
    #    We will use a max-heap (simulated with heapq min-heap) as requested.
    #    Put elements into heap negated, extract, then reverse.

    suffix_to_sort = chars[pivot_index + 1:]

    # Use a min-heap storing (-ord(char), char) to simulate a max-heap based on ord(char)
    max_heap = []
    for char in suffix_to_sort:
        heapq.heappush(max_heap, (-ord(char), char))

    sorted_suffix_desc = []
    while max_heap:
        _, char = heapq.heappop(max_heap) # Extract max character
        sorted_suffix_desc.append(char)

    # Reverse the descending list to get the ascending order needed for the smallest result
    sorted_suffix_asc = sorted_suffix_desc[::-1]

    # 6. Combine the prefix, the new pivot, and the sorted suffix
    result_chars = chars[:pivot_index + 1] + sorted_suffix_asc

    return "".join(result_chars)


if __name__ == "__main__":
    # Example Usage (from problem description)
    print(bigger_is_greater("ab"))      # Output: ba
    print(bigger_is_greater("bb"))      # Output: no answer
    print(bigger_is_greater("hefg"))    # Output: hegf
    print(bigger_is_greater("dhck"))    # Output: dhkc
    print(bigger_is_greater("dkhc"))    # Output: hcdk
    print(bigger_is_greater("lmno"))    # Output: lmon
    print(bigger_is_greater("dcba"))    # Output: no answer
    print(bigger_is_greater("dcbb"))    # Output: no answer
    print(bigger_is_greater("abdc"))    # Output: acbd
    print(bigger_is_greater("abcd"))    # Output: abdc
    print(bigger_is_greater("fedcbabcd")) # Output: fedcbabdc
