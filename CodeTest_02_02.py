def solution(board, moves):
    answer=0
    ssum=[]
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1]!=0:
                ssum.append(board[j][moves[i]-1])
                board[j][moves[i]-1]=0
                break
        if len(ssum) > 1 and ssum[len(ssum)-1]==ssum[len(ssum)-2]:
            del ssum[len(ssum)-1]
            del ssum[len(ssum)-1]
            answer+=1
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

result = solution(board, moves)
print(result)