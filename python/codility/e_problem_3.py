# Created by Jello on 2017. 6. 14.

path_data = []
max_cnt = 0


def search_node(N):
    path_data.append(N.x)
    if N.l == None and N.r == None:
        global max_cnt
        max_cnt = max(len(set(path_data)), max_cnt)
    else:
        if N.l != None:
            search_node(N.l)
        if N.r != None:
            search_node(N.r)


def solution(T):
    search_node(T)
    return max_cnt
