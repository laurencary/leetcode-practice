from typing import List

# valid sudoku
def isValidSudoku(board: List[List[str]]) -> bool:
    #rows
    for row in range(0,9):
        nums = list(range(1,10))
        for col in range(0,9):
            if board[row][col] != ".":
                if int(board[row][col]) != nums[int(board[row][col]) - 1]:
                    return False
                nums[int(board[row][col]) - 1] = "."

    for col in range(0,9):
        nums = list(range(1,10))
        for row in range(0,9):
            if board[row][col] != ".":
                if int(board[row][col]) != nums[int(board[row][col]) - 1]:
                    return False
                nums[int(board[row][col]) - 1] = "."


    for grid_row in [0,3,6]:
        for grid_col in [0,3,6]:
            nums = list(range(1,10))
            for row_adj in range(0,3):
                for col_adj in range(0,3):
                    row = grid_row + row_adj
                    col = grid_col + col_adj
                    if board[row][col] != ".":
                        if int(board[row][col]) != nums[int(board[row][col]) - 1]:
                            return False
                        nums[int(board[row][col]) - 1] = "."

    return True
board = [
    ["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]
]

# print(isValidSudoku(board))


# group anagrams
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    if len(strs) == 1: return [strs]
    
    result = {}

    for str in strs:
        key = ''.join(sorted(str))
        if key in result:
            result[key].append(str)
        else:
            result[key] = [str]

    return list(result.values())

# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

def longestConsecutive(nums: List[int]) -> int:

    seq = set(nums)
    max_length = 0
    
    for num in seq:
        if num - 1 not in seq:
            count = 1
            next = num + 1
            while next in seq:
                count += 1
                next += 1
            
            max_length = max(max_length, count)
    
    return max_length


print(longestConsecutive([100,3,2,200,4,1,345,7,5,500]))