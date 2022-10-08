# ---------------------------------------- #
#           Algorithmic Project            #
#  Algorithmic - 8INF870 - Imène Benkalai  #
#        Claire SABA - SABC14529902        #
# ---------------------------------------- #

from Stable import *

# ----- Generate 10 random graphs ----- #
graph1 = extract_graph_from_file("graph_4")  # For this one, I used the graph from the example.
graph2 = extract_graph_from_file("graph_10")
graph3 = extract_graph_from_file("graph_20")
graph4 = extract_graph_from_file("graph_30")
graph5 = extract_graph_from_file("graph_40")
graph6 = extract_graph_from_file("graph_50")
graph7 = extract_graph_from_file("graph_60")
graph8 = extract_graph_from_file("graph_70")
graph9 = extract_graph_from_file("graph_80")
graph10 = extract_graph_from_file("graph_90")
graph11 = extract_graph_from_file("graph_100")


# ----- Use the exact method on the 10 random graphs ----- #
print("-"*10+" Exact Method "+"-"*10)

print("Graph 1")
begin = time.time()
res = exact_method(graph1, begin)
duration = time.time() - begin
print(f"Method took {duration} seconds to find a solution of size {len(res)}:\n{res}\n")

print("Graph 2")
begin = time.time()
res = exact_method(graph2, begin)
duration = time.time() - begin
print(f"Method took {duration} seconds to find a solution of size {len(res)}:\n{res}\n")

print("Graph 3")
begin = time.time()
res = exact_method(graph3, begin)
duration = time.time() - begin
print(f"Method took {duration} seconds to find a solution of size {len(res)}:\n{res}\n")

print("Graph 4")
begin = time.time()
res = exact_method(graph4, begin)
duration = time.time() - begin
print(f"Method took {duration} seconds to find a solution of size {len(res)}:\n{res}\n")

print("Graph 5")
begin = time.time()
res = exact_method(graph5, begin)
duration = time.time() - begin
print(f"Method took {duration} seconds to find a solution of size {len(res)}:\n{res}\n")

print("Graph 6")
begin = time.time()
res = exact_method(graph6, begin)
duration = time.time() - begin
print(f"Method took {duration} seconds to find a solution of size {len(res)}:\n{res}\n")

print("Graph 7")
begin = time.time()
res = exact_method(graph7, begin)
duration = time.time() - begin
print(f"Method took {duration} seconds to find a solution of size {len(res)}:\n{res}\n")

print("Graph 8")
begin = time.time()
res = exact_method(graph8, begin)
duration = time.time() - begin
print(f"Method took {duration} seconds to find a solution of size {len(res)}:\n{res}\n")

print("Graph 9")
begin = time.time()
res = exact_method(graph9, begin)
duration = time.time() - begin
print(f"Method took {duration} seconds to find a solution of size {len(res)}:\n{res}\n")

print("Graph 10")
begin = time.time()
res = exact_method(graph10, begin)
duration = time.time() - begin
print(f"Method took {duration} seconds to find a solution of size {len(res)}:\n{res}\n")

print("Graph 11")
begin = time.time()
res = exact_method(graph11, begin)
duration = time.time() - begin
print(f"Method took {duration} seconds to find a solution of size {len(res)}:\n{res}\n")


# ----- Use the approximate method on the 10 random graphs ----- #
print("-"*10+" Approximate Method "+"-"*10)

print("Graph 1")
begin = time.time()
res = approximate_method(graph1, begin)
duration = time.time() - begin
print(f"Method took {duration} seconds to find a solution of size {len(res)}:\n{res}\n")

print("Graph 2")
begin = time.time()
res = approximate_method(graph2, begin)
duration = time.time() - begin
print(f"Method took {duration} seconds to find a solution of size {len(res)}:\n{res}\n")

print("Graph 3")
begin = time.time()
res = approximate_method(graph3, begin)
duration = time.time() - begin
print(f"Method took {duration} seconds to find a solution of size {len(res)}:\n{res}\n")

print("Graph 4")
begin = time.time()
res = approximate_method(graph4, begin)
duration = time.time() - begin
print(f"Method took {duration} seconds to find a solution of size {len(res)}:\n{res}\n")

print("Graph 5")
begin = time.time()
res = approximate_method(graph5, begin)
duration = time.time() - begin
print(f"Method took {duration} seconds to find a solution of size {len(res)}:\n{res}\n")

print("Graph 6")
begin = time.time()
res = approximate_method(graph6, begin)
duration = time.time() - begin
print(f"Method took {duration} seconds to find a solution of size {len(res)}:\n{res}\n")

print("Graph 7")
begin = time.time()
res = approximate_method(graph7, begin)
duration = time.time() - begin
print(f"Method took {duration} seconds to find a solution of size {len(res)}:\n{res}\n")

print("Graph 8")
begin = time.time()
res = approximate_method(graph8, begin)
duration = time.time() - begin
print(f"Method took {duration} seconds to find a solution of size {len(res)}:\n{res}\n")

print("Graph 9")
begin = time.time()
res = approximate_method(graph9, begin)
duration = time.time() - begin
print(f"Method took {duration} seconds to find a solution of size {len(res)}:\n{res}\n")

print("Graph 10")
begin = time.time()
res = approximate_method(graph10, begin)
duration = time.time() - begin
print(f"Method took {duration} seconds to find a solution of size {len(res)}:\n{res}\n")

print("Graph 11")
begin = time.time()
res = approximate_method(graph11, begin)
duration = time.time() - begin
print(f"Method took {duration} seconds to find a solution of size {len(res)}:\n{res}\n")

