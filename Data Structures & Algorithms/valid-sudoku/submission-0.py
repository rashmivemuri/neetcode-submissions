class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flag=True
        db={}
        for i in range(len(board)):
            dr=set()
            dc=set()
            
            if flag==False:
                break
            for j in range(len(board)):
                
                
                if board[i][j] != '.' and board[i][j] not in dr:
                    dr.add(board[i][j])
                elif board[i][j] != '.' and board[i][j] in dr:
                    flag=False
                if  board[j][i] != '.' and board[j][i] not in dc:
                    dc.add(board[j][i])
                elif board[j][i] != '.' and board[j][i] in dc:
                    flag=False

                
                    
                if board[i][j] != '.':
                    if (i//3*3+j//3) not in db:
                        db[(i//3*3+j//3)] = set()
                        db[ (i//3*3+j//3)].add(board[i][j])
                    elif board[i][j] in db.get((i//3*3+j//3),set()):
                        flag=False
                    else:
                        db[(i//3*3+j//3)].add(board[i][j])
               


        return flag

        