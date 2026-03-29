import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import networkx as nx

# Setup dashboard layout
fig = plt.figure(constrained_layout=True, figsize=(18,12))
gs = GridSpec(3, 2, figure=fig)

# 1. Pie Chart: Key Challenges
ax1 = fig.add_subplot(gs[0,0])
ax1.pie(project_data["Key Challenges"].values(), labels=project_data["Key Challenges"].keys(), autopct='%1.1f%%', startangle=140)
ax1.set_title("Key Challenges Distribution")

# 2. Bar Chart: AI Workflow Steps
ax2 = fig.add_subplot(gs[0,1])
ax2.bar(project_data["AI Solution & Workflow"].keys(), project_data["AI Solution & Workflow"].values(), color='skyblue')
ax2.set_title("AI Solution & Workflow Steps Count")
ax2.set_ylabel("Number of Actions")

# 3. Line Graph: MW Submission vs PMax
ax3 = fig.add_subplot(gs[1,0])
mw_requested = [165, 155]
mw_labels = ["Requested", "Corrected"]
ax3.plot(mw_labels, mw_requested, marker='o', color='red')
ax3.set_title("MW Submission vs PMax Limit")
ax3.set_ylabel("MW")

# 4. Network Graph: AI Workflow Schematic
ax4 = fig.add_subplot(gs[1,1])
G = nx.DiGraph()
workflow_nodes = ["Constraint Analysis", "Safe-to-Submit Calculation", "Automated Output", "Audit Logging"]
G.add_edges_from([("Constraint Analysis","Safe-to-Submit Calculation"), ("Safe-to-Submit Calculation","Automated Output"), ("Automated Output","Audit Logging")])
nx.draw(G, with_labels=True, node_color='lightgreen', node_size=2000, arrowsize=20, font_size=10, ax=ax4)
ax4.set_title("AI Workflow Schematic")

# 5. Horizontal Bar Chart: Tools & Technologies Usage
ax5 = fig.add_subplot(gs[2,:])
tools = project_data["Tools & Technologies"]
usage_score = [5,4,3,4,2,1]  # illustrative usage score
ax5.barh(tools, usage_score, color='orange')
ax5.set_title("Tools & Technologies Usage")
ax5.set_xlabel("Usage Score")

# Save dashboard
dashboard_path = "/mnt/data/CAISO_Project_Dashboard.png"
plt.savefig(dashboard_path)
dashboard_path
