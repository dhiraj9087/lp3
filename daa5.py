def is_safe(row,col,board):
    duprow,dupcol=row,col
    while row>=0 and col>=0:
        if board[row][col]=='Q':
            return False
        row-=1
        col-=1
    row=duprow
    col=dupcol
    while col>=0:
        if board[row][col]=='Q':
            return False
        col-=1
    row,col=duprow,dupcol
    while row<n and col>=0:
        if board[row][col]=='Q':
            return False
        row+=1
        col-=1
    return True
def solve(col,board,ans):
    if col==len(board):
        ans.append([''.join(row) for row in board])
        return
    for row in range(n):
        if is_safe(row,col,board)==True:
            board[row][col]='Q'
            solve(col+1,board,ans)
            board[row][col]='.'
n=int(input())
board=[['.' for i in range(n)] for j in range(n)]
ans=[]
solve(0,board,ans)
for i in ans:
    print(i)
# print(ans)