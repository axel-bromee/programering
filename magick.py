import random
ja=["ja","mycket troligt"]
otydlig=["kanske","testa igen"]
nej=["nej","verkligen inte"]
ha=[random.choice(ja),random.choice(nej),random.choice(otydlig)]

print(random.choice(ha))