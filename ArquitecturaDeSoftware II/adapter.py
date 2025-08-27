import matplotlib.pyplot as plt
import networkx as nx

# Crear el grafo
G = nx.DiGraph()

# Nodos
G.add_node("A", label="Proveedor A\n(API XML)", color="lightblue")
G.add_node("AD", label="Adapter\n(XML → JSON)", color="lightgreen")
G.add_node("B", label="Empresa B\n(Consume JSON)", color="lightyellow")

# Conexiones
G.add_edge("A", "AD", label="XML")
G.add_edge("AD", "B", label="JSON")

# Posiciones de los nodos (alineados horizontalmente)
pos = {"A": (0, 0), "AD": (1, 0), "B": (2, 0)}

# Dibujar nodos
colors = [G.nodes[n]["color"] for n in G.nodes()]
labels = {n: G.nodes[n]["label"] for n in G.nodes()}
nx.draw(G, pos, with_labels=True, labels=labels, node_color=colors, node_size=5000, font_size=10, font_weight="bold", edgecolors="black")

# Dibujar etiquetas de aristas
edge_labels = nx.get_edge_attributes(G, "label")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

# Guardar como PNG
plt.savefig("adapter_pattern.png", format="png", dpi=300, bbox_inches="tight")
plt.show()

print("✅ Imagen guardada como adapter_pattern.png")
