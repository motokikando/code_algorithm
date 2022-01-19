n = input()
def opt_cnt(n:str) -> str:
    op_cnt = len(n) -1
    for i in range(op_cnt**2):
        op = ["-"]*op_cnt
        # print(op)
        for j in range(op_cnt):
            if ((i >> j) & 1):
                op[op_cnt -1 -j] = "+"
                # print(op)
        fomula = ""
        for p_n, p_o in zip(n, op + [""]):
            fomula += (p_n + p_o)
            # print(fomula)
        if eval(fomula) == 7:
            return fomula + "=7"

print(opt_cnt(n))

# n = "2221"
# op_cnt = len(n) - 1  # すき間の個数
# for i in range(2 ** op_cnt):
#     op = ["-"] * op_cnt  # あらかじめ ["-", "-", "-"] というリストを作っておく
#     for j in range(op_cnt):
#         if ((i >> j) & 1):
#             op[op_cnt - 1 - j] = "+"  # フラグが立っていた箇所を "+" で上書き

#     formula = ""
#     for p_n, p_o in zip(n, op + [""]):  # 少々モヤッとする
#         formula += (p_n + p_o)
#     if eval(formula) == 7:
#         print(formula + "=7")
#         break

