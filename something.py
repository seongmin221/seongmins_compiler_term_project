import time

SLRTable = {
  0 : {'vtype' : 's5', 'class': 's6', '$': 'r4', 'CODE': 1, 'VDECL' : 2, 'FDECL' : 3, 'CDECL': 4},
  1 : {'$': 'acc'},
  2 : {'vtype': 's5', 'class': 's6', '$': 'r4', 'CODE': 7, 'VDECL': 2, 'FDECL': 3, 'CDECL': 4},
  3 : {'vtype': 's5', 'class': 's6', '$': 'r4', 'CODE': 8, 'VDECL': 2, 'FDECL': 3, 'CDECL': 4},
  4 : {'vtype': 's5', 'class': 's6', '$': 'r4', 'CODE': 9, 'VDECL': 2, 'FDECL': 3, 'CDECL': 4},
  5 : {'id': 's10', 'ASSIGN': 11},
  6 : {'id': 's12'},
  7 : {'$': 'r1'},
  8 : {'$': 'r2'},
  9 : {'$': 'r3'},
  10 : {'semi': 's13', 'assign': 's15', 'lparen': 's14'},
  11 : {'semi': 's16'},
  12 : {'lbrace': 's17'},
  13 : {'vtype': 'r5', 'id': 'r5', 'rbrace': 'r5', 'if': 'r5', 'while': 'r5', 'return': 'r5', 'class': 'r5', '$': 'r5'},
  14 : {'vtype': 's19', 'rparen': 'r21', 'ARG': 18},
  15 : {'id': 's28', 'literal': 's22', 'character': 's23', 'boolstr': 's24', 'lparen': 's27', 'num': 's29', 'RHS': 20, 'EXPR': 21, 'T': 25, 'F': 26},
  16 : {'vtype': 'r6', 'id': 'r6', 'rbrace': 'r6', 'if': 'r6', 'while': 'r6', 'return': 'r6', 'class': 'r6', '$': 'r6'},
  17 : {'vtype': 's5', 'rbrace': 'r38', 'VDECL': 31, 'FDECL': 32, 'ODECL': 30},
  18 : {'rparen': 's33'},
  19 : {'id': 's34'},
  20 : {'semi': 'r7'},
  21 : {'semi': 'r8', 'addsub': 's35'},
  22 : {'semi': 'r9'},
  23 : {'semi': 'r10'},
  24 : {'semi': 'r11'},
  25 : {'semi': 'r13', 'addsub': 'r13', 'multdiv': 's36', 'rparen': 'r13'},
  26 : {'semi': 'r15', 'addsub': 'r15', 'multdiv': 'r15', 'rparen': 'r15'},
  27 : {'id': 's28', 'lparen': 's27', 'num': 's29', 'RHS': 37, 'T': 25, 'F': 26},
  28 : {'semi': 'r17', 'addsub': 'r17', 'multdiv': 'r17', 'rparen': 'r17'},
  29 : {'semi': 'r18', 'addsub': 'r18', 'multdiv': 'r18', 'rparen': 'r18'},
  30 : {'rbrace': 's38'},
  31 : {'vtype': 's5', 'rbrace': 'r38', 'VDECL': 31, 'FDECL': 32, 'ODECL': 39},
  32 : {'vtype': 's5', 'rbrace': 'r38', 'VDECL': 31, 'FDECL': 32, 'ODECL': 40},
  33 : {'lbrace': 's41'},
  34 : {'rparen': 'r23', 'comma': 's43', 'MOREARGS': 42},
  35 : {'id': 's28', 'lparen': 's27', 'num': 's29', 'T': 44, 'F': 26},
  36 : {'id': 's28', 'lparen': 's27', 'num': 's29', 'F': 45},
  37 : {'addsub': 's35', 'rparen': 's46'},
  38 : {'vtype': 'r35', 'class': 'r35', '$': 'r35'},
  39 : {'rbrace': 'r36'},
  40 : {'rbrace': 'r37'},
  41 : {'vtype': 's53', 'id': 's54', 'rbrace': 'r25', 'if': 's51', 'while': 's52', 'return': 'r25', 'VDECL': 49, 'ASSIGN': 50, 'BLOCK': 47, 'STMT': 48},
  42 : {'rparen': 'r29'},
  43 : {'vtype': 's55'},
  44 : {'semi': 'r12', 'addsub': 'r12', 'multdiv': 's36', 'rparen': 'r12'},
  45 : {'semi': 'r14', 'addsub': 'r14', 'multdiv': 'r14', 'rparen': 'r14'},
  46 : {'semi': 'r16', 'addsub': 'r16', 'multdiv': 'r16', 'rparen': 'r16'},
  47 : {'return': 's57', 'RETURN': 56},
  48 : {'vtype': 's53', 'id': 's54', 'rbrace': 'r25', 'if': 's51', 'while': 's52', 'return': 'r25', 'VDECL': 49, 'ASSIGN': 50, 'BLOCK': 58, 'STMT': 48},
  49 : {'vtype': 'r26', 'id': 'r26', 'rbrace': 'r26', 'if': 'r26', 'while': 'r26', 'return': 'r26'},
  50 : {'semi': 's59'},
  51 : {'lparen': 's60'},
  52 : {'lparen': 's61'},
  53 : {'id': 's62', 'ASSIGN': 11},
  54 : {'assign': 's15'},
  55 : {'id': 's63'},
  56 : {'rbrace': 's64'},
  57 : {'id': 's28', 'literal': 's22', 'character': 's23', 'boolstr': 's24', 'lparen': 's27', 'num': 's29', 'RHS': 65, 'EXPR': 21, 'T': 25, 'F': 26},
  58 : {'rbrace': 'r24', 'return': 'r24'},
  59 : {'vtype': 'r27', 'id': 'r27', 'rbrace': 'r27', 'if': 'r27', 'while': 'r27', 'return': 'r27'},
  60 : {'boolstr': 's67', 'COND': 66},
  61 : {'boolstr': 's67', 'COND': 68},
  62 : {'semi': 's13', 'assign': 's15'},
  63 : {'rparen': 'r23', 'comma': 's43', 'MOREARGS': 69},
  64 : {'vtype': 'r19', 'rbrace': 'r19', 'class': 'r19', '$': 'r19'},
  65 : {'semi': 's70'},
  66 : {'rparen': 's71'},
  67 : {'rparen': 'r31', 'comp': 's72'},
  68 : {'rparen': 's73'},
  69 : {'rparen': 'r22'},
  70 : {'rbrace': 'r34'},
  71 : {'lbrace': 's74'},
  72 : {'boolstr': 's67', 'COND': 75},
  73 : {'lbrace': 's76'},
  74 : {'vtype': 's53', 'id': 's54', 'rbrace': 'r25', 'if': 's51', 'while': 's52', 'return': 'r25', 'VDECL': 49, 'ASSIGN': 50, 'BLOCK': 77, 'STMT': 48},
  75 : {'rparen': 'r30'},
  76 : {'vtype': 's53', 'id': 's54', 'rbrace': 'r25', 'if': 's51', 'while': 's52', 'return': 'r25', 'VDECL': 49, 'ASSIGN': 50, 'BLOCK': 78, 'STMT': 48},
  77 : {'rbrace': 's79'},
  78 : {'rbrace': 's80'},
  79 : {'vtype': 'r33', 'id': 'r33', 'rbrace': 'r33', 'if': 'r33', 'while': 'r33', 'else': 's82', 'return': 'r33', 'ELSE': 81},
  80 : {'vtype': 'r29', 'id': 'r29', 'rbrace': 'r29', 'if': 'r29', 'while': 'r29', 'return': 'r29'},
  81 : {'vtype': 'r28', 'id': 'r28', 'rbrace': 'r28', 'if': 'r28', 'while': 'r28', 'return': 'r28'},
  82 : {'lbrace': 's83'},
  83 : {'vtype': 's53', 'id': 's54', 'rbrace': 'r25', 'if': 's51', 'while': '52', 'return': 'r25', 'VDECL': 49, 'ASSIGN': 50, 'BLOCK': 84, 'STMT': 48},
  84 : {'rbrace': 's85'},
  85 : {'vtype': 'r32', 'id': 'r32', 'rbrace': 'r32', 'if': 'r32', 'while': 'r32', 'return': 'r32'}
}

CFG = {
    0: {'from': 'START', 'to': 'CODE'},
    1: {'from': 'CODE', 'to': 'VDECL CODE'},
    2: {'from': 'CODE', 'to': 'FDECL CODE'},
    3: {'from': 'CODE', 'to': 'CDECL CODE'},
    4: {'from': 'CODE', 'to': ''},
    5: {'from': 'VDECL', 'to': 'vtype id semi'},
    6: {'from': 'VDECL', 'to': 'vtype ASSIGN semi'},
    7: {'from': 'ASSIGN', 'to': 'id assign RHS'},
    8: {'from': 'RHS', 'to': 'EXPR'},
    9: {'from': 'RHS', 'to': 'literal'}, 
    10: {'from': 'RHS', 'to': 'character'}, 
    11: {'from': 'RHS', 'to': 'boolstr'},
    12: {'from': 'EXPR', 'to': 'EXPR addsub T'},
    13: {'from': 'EXPR', 'to': 'T'},
    14: {'from': 'T', 'to': 'T multdiv F'},
    15: {'from': 'T', 'to': 'F'},
    16: {'from': 'F', 'to': 'lparen EXPR rparen'},
    17: {'from': 'F', 'to': 'id'},
    18: {'from': 'F', 'to': 'num'},
    19: {'from': 'FDECL', 'to': 'vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace'},
    20: {'from': 'ARG', 'to': 'vtype id MOREARGS'},
    21: {'from': 'ARG', 'to': ''},
    22: {'from': 'MOREARGS', 'to': 'comma vtype id MOREARGS'},
    23: {'from': 'MOREARGS', 'to': ''},
    24: {'from': 'BLOCK', 'to': 'STMT BLOCK'},
    25: {'from': 'BLOCK', 'to': ''},
    26: {'from': 'STMT', 'to': 'VDECL'},
    27: {'from': 'STMT', 'to': 'ASSIGN semi'},
    28: {'from': 'STMT', 'to': 'if lparen COND rparen lbrace BLOCK rbrace ELSE'},
    29: {'from': 'STMT', 'to': 'while lparen COND rparen lbrace BLOCK rbrace'},
    30: {'from': 'COND', 'to': 'boolstr comp COND'},
    31: {'from': 'COND', 'to': 'boolstr'},
    32: {'from': 'ELSE', 'to': 'else lbrace BLOCK rbrace'},
    33: {'from': 'ELSE', 'to': ''},
    34: {'from': 'RETURN', 'to': 'return RHS semi'},
    35: {'from': 'CDECL', 'to': 'class id lbrace ODECL rbrace'},
    36: {'from': 'ODECL', 'to': 'VDECL ODECL'},
    37: {'from': 'ODECL', 'to': 'FDECL ODECL'},
    38: {'from': 'ODECL', 'to': ''},
}

# while index < inputCnt:
#   try:
#     print("State :", stack[0])
#     print("Stack :", stack)
#     print("Next Input Symbol :", inputSequence[index])
#     print("Decision :", SLRTable[stack[0]][inputSequence[index]], "\n")
    
#     if SLRTable[stack[0]][inputSequence[index]].__contains__("s"):
#       nextState = int(SLRTable[stack[0]][inputSequence[index]].strip("s"))
#       # 다음 state를 stack 의 top에 push
#       stack.append(nextState)
#       index += 1

#     elif SLRTable[stack[0]][inputSequence[index]].__contains__("r"):
#       stack.pop()
      

#     else:
#       print("else")
#       index += 1

#   except Exception as e:
#     print("error with parsing", e)
#     break



inputString = "vtype id lparen rparen lbrace vtype id semi return literal semi rbrace $"

inputSequence = inputString.split(' ')

# initialization
index = 0
stateStack = [0]


while not inputSequence.__contains__("CODE"):

    print("Stack :", stateStack)
    print("Index :", index)
    print(inputSequence)
    print("Next Input Symbol :", inputSequence[index])
    print("Decision :", SLRTable[stateStack[-1]][inputSequence[index]], "\n")
    
    try:
        # 현재 stack 의 top 을 테이블에서 찾는 과정
        decision = SLRTable[stateStack[-1]][inputSequence[index]]
        # 만약 table 에서 찾은 값이 s<number> 라면, "goto <number>" & "shift"
        if decision.__contains__("s"):
            # goto <number>
            nextState = int(decision.strip("s"))
            stateStack.append(nextState)
            # shift
            index += 1

        # 만약 table 에서 찾은 값이 r<number> 라면, "pop stack" & "reduce by CFG<number>" 
        elif decision.__contains__("r"):
            # find CFG<number>
            cfgNum = int(decision.strip("r"))   # r 뒤에 숫자 가져오기
            cfg = CFG[cfgNum]                   # 그에 해당하는 CFG 가져오기

            print("--- remove with :", cfg, "\n")

            # for A -> ɑ pop |ɑ| contents from stack
            popCnt = len(cfg["to"].split(" "))  # |ɑ| 의 크기 구하기
            # 만약 ɑ 가 ε 이라면 ?

            if cfg["to"] != "":
                for i in range(0, popCnt):
                    stateStack.pop()
                    inputSequence.pop(index-1)
                    index -= 1

            # from A -> ?? , reduce with A
            push = CFG[cfgNum]['from']
            inputSequence.insert(index, push)
            
            # if cfg["to"] == "":
            #     index += 1
            # print(SLRTable[stateStack[-1]][inputSequence[index]])

            # GOTO
            stateStack.append(SLRTable[stateStack[-1]][inputSequence[index]])
            index += 1

    except Exception as e:
       print("error with parsing", e)
       break

if inputSequence.__contains__("CODE"):
    print("success")