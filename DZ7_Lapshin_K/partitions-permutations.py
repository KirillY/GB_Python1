# tried to generate spaces between digits in card with partitions method - too complex
# instead I used line.insert(random.randint(0, len(line), ' ')

def spaces_between_digits():
    '''
    generate partitions of number n - amount of spaces between digits in card
    limited because spaces INSIDE digits and OUTSIDE are different
    :return:
    '''

    def partitionfunc(n, k, l=1):
        '''
        solution is complex for me - generator and recursion
        https://stackoverflow.com/questions/18503096/python-integer-partitioning-with-given-k-partitions
        partition of a positive integer n is a way of writing n as a sum of positive integers:
        eg. 3 = 1+1+1 = 1+2
        by implementing partitions we distribute 16 (default) spaces into 5 available spots between digits
        :param n: integer to partition
        :param k: length of partitions
        :param l: min partition element size
        :return: generator of tuples - partitions of n, length k, min elt size l
        '''
        if k < 1:
            raise StopIteration
        if k == 1:
            if n >= l:
                yield (n,)
            raise StopIteration
        for i in range(l, n + 1):
            for result in partitionfunc(n - i, k - 1, i):
                yield (i,) + result

    ###  selecting partitions with proper inter-digit spaces from cell_spaces_list ###
    partition_list = list()
    cell_spaces_list = [1 + x for x in range(0, 15, 3)]  # considers only spaces INSIDE 5 digits 1--2---3-----4-5
    for partition in partitionfunc(16, 4):
        # print(partition)
        if all(elt in cell_spaces_list for elt in partition):
            partition_list.append(partition)
    print(partition_list)
    ### get all possible non-equal permutations ###
    for partition in partition_list:  # using permutations to get all possible combinations of spaces
        perm = set(itertools.permutations(partition))
        # print(perm)

from datetime import datetime, timedelta
time_str = '2017-03-30 14:57:07.439890+00:00'
date_time = datetime.datetime.strptime(''.join(time_str.rsplit(':', 1)), '%Y-%m-%d %H:%M:%S.%f%z')
interval = 7884000
threshold_date = datetime.utcnow() - timedelta(seconds=interval)