def bubble(seq):
    length = len(seq)
    if length <= 1:
        return seq
    else:
        need_sort = True
        n = length
        while need_sort:
            need_sort = False
            for idx in range(1, n):
                left = seq[idx - 1]
                right = seq[idx]
                if left > right:
                    seq[idx - 1], seq[idx] = right, left
                    need_sort = True
            n = n - 1
        return seq


def select(seq):
    length = len(seq)
    if length <= 1:
        return seq
    else:
        for left_idx, left_elem in enumerate(seq):
            min_elem = left_elem
            exchange_pos = left_idx
            for current_idx, current_elem in enumerate(seq[left_idx+1:], left_idx+1):
                if current_elem < min_elem:
                    min_elem = current_elem
                    exchange_pos = current_idx
            if exchange_pos != left_idx:
                seq[left_idx] = min_elem
                seq[exchange_pos] = left_elem
        return seq


def insert(seq):
    length = len(seq)
    if length <= 1:
        return seq
    else:
        for left_boundry, processing_elem in enumerate(seq[1:], 1):
            current_pos = left_boundry
            insert_pos = left_boundry
            while current_pos:
                prev_pos = current_pos - 1
                prev_elem = seq[prev_pos]
                if prev_elem > processing_elem:
                    seq[current_pos] = prev_elem
                    insert_pos = prev_pos
                else:
                    break
                current_pos = current_pos - 1
            if insert_pos != left_boundry:
                seq[insert_pos] = processing_elem
        return seq


def merge(seq):
    length = len(seq)
    if length <= 1:
        return seq
    else:
        def merge_sort(left, right):
            left = merge(left)
            right = merge(right)
            result = []
            while (left and right):
                if left[0] < right[0]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            if left:
                result.extend(left)
            if right:
                result.extend(right)
            return result

        start = 0
        end = length - 1
        sep = (start + end) / 2
        left = seq[start:sep + 1]
        right = seq[sep + 1:]
        return merge_sort(left, right)


def quick(seq):
    length = len(seq)
    if length <= 1:
        return seq
    else:
        left = []
        right = []
        pivot = seq[0]
        for elem in seq[1:]:
            if elem < pivot:
                left.append(elem)
            else:
                right.append(elem)
        return quick(left) + [pivot] + quick(right)


def test():
    test_case_list = (
                (1, 1, 1, 1),
                (),
                (0,),
                (1, 2, 3, 4, 5),
                (5, 4, 3, 2, 1),
                (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 4, 3, 2, 7, 8, 9, 1, 2, 4, 7),
                (21, 23, 34, 45, 76, 98, 34, 12, 23, 1, 2, 34, 10),
            )
    func_list = (bubble, select, insert, merge, quick)
    for func in func_list:
        print "Testing %s..." % func.func_name
        for test_case in test_case_list:
            print "\t", test_case
            print "\tSorted:", func(list(test_case))
        print "=====END====="


if __name__ == "__main__":
    test()


