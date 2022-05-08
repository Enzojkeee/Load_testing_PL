import argparse


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('n')
    parser.add_argument('m')
    return parser.parse_args()



def count_and_print_steps(n,m):
    list_for_index = m * ([int(i) for i in range(1, n + 1)])
    two_List = [' ']
    three_List = []
    cnt = 0
    while two_List[-1] != 1:
        two_List = []
        for j in range(cnt, m + cnt):
            two_List.append(list_for_index[j])
            cnt += 1
        three_List.append(two_List)
        cnt -= 1
        print(three_List)
    for k in range(len(three_List)):
        print(three_List[k][0], end="")

if __name__ == "__main__":
    nm = arg_parser()
    count_and_print_steps(int(nm.n), int(nm.m))
