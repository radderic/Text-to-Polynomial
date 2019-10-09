from pprint import pprint
from sympy import Matrix

def genMatrix(s):
    power = len(s)
    m = []
    x = 0
    for c in s:
        row = [ord(c)]
        for p in range(0, power):
            row.insert(0, x**p)
        print(ord(c), c, row)
        m.append(row)
        x += 1
    return m

print("Enter word to get polynomial: ")
words = input()
m = genMatrix(words)
print("\nMatrix to evaluate: \n")
mat = Matrix(m)
pprint(mat)
rref = mat.rref()
print("\nRow Reduced Matrix: \n")
pprint(rref)

word_len = len(words)
print("\n----------------------------------------------------------------")
print("\nEquation for \"{w}\" where the range of x integers from 0 to {l}: \n".format(w=words, l=word_len))
print("----------------------------------------------------------------")
g_term = ""
c_term = ""
p_term = ""
j_term = ""
for i in range(0, word_len):
    g_term += "(" + str(rref[0][word_len+(i*(word_len+1))]) + ".0)*(x^" + str(word_len-i-1) + ")"
    c_term += "(" + str(rref[0][word_len+(i*(word_len+1))]) + ".0)*pow(x," + str(word_len-i-1) + ")"
    p_term += "(" + str(rref[0][word_len+(i*(word_len+1))]) + ".0)*(x**" + str(word_len-i-1) + ")"
    j_term += "(" + str(rref[0][word_len+(i*(word_len+1))]) + ".0)*Math.pow(x," + str(word_len-i-1) + ")"
    if(i != word_len-1):
        g_term += " + "
        c_term += " + "
        p_term += " + "
        j_term += " + "

print("\nGeneral:", g_term.replace("/", ".0/"))
print("\nPython:", p_term.replace("/", ".0/"))
print("\nC/C++:", c_term.replace("/", ".0/"))
print("\nJava:", j_term.replace("/", ".0/"))

