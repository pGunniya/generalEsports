import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches
import numpy as np
from matplotlib.patches import Ellipse


df = pd.read_excel(r"C:\Users\Pranav\Documents\Valorant\esport_Ages.xlsx")
img = plt.imread(r"C:\Users\Pranav\Documents\Valorant\areas.png")


age_val = df['age_valorant']
age_csgo = df['age_csgo']
rank_val = df['world_ranking_valorant']
rank_csgo = df['world_ranking_csgo']


# here we're looking at wether there's a correlation between rank and age

# plt.scatter(age_csgo, rank_csgo)
# for i in range(df.shape[0]):
#     plt.text(x = df.age_csgo[i] + .1, y = df.world_ranking_csgo[i] + .1, s = df.team_name_csgo[i], fontsize = 'small')

# plt.title("How does rank and age correlate? CSGO")
# plt.arrow(28, 0, -7.5, 0, width = 0.05, head_width = .5, head_length = .15)
# plt.arrow(20, 28, 0, -22, width = 0.03, head_width = .15, head_length = .5)
# plt.xlabel("Age")
# plt.ylabel("Rank")
# plt.imshow(img, extent = [19,30,-1,32])
# ellipse = matplotlib.patches.Ellipse(xy = (21.9,5.3), width = 2.1, height = 1.9, fill = False, edgecolor = 'b', lw = .5)
# plt.gca().add_patch(ellipse)
# plt.text(x = 21, y = 5, s = "Young & Successful", fontsize = 'x-large')

# ellipse = matplotlib.patches.Ellipse(xy = (28.5,5.3), width = 1.9, height = 1.9, fill = False, edgecolor = 'b', lw = .5)
# plt.gca().add_patch(ellipse)
# plt.text(x = 28, y = 5, s = "Old is GOLD", fontsize = 'x-large')

# ellipse = matplotlib.patches.Ellipse(xy = (28.5,25.3), width = 1.9, height = 1.9, fill = False, edgecolor = 'b', lw = .5)
# plt.gca().add_patch(ellipse)
# plt.text(x = 28, y = 25, s = "Old but bad", fontsize = 'x-large')

# ellipse = matplotlib.patches.Ellipse(xy = (21.75,25.3), width = 2.1, height = 1.9, fill = False, edgecolor = 'b', lw = .5)
# plt.gca().add_patch(ellipse)
# plt.text(x = 21, y = 25, s = "Emerging Talent", fontsize = 'x-large')

# plt.gca().set_aspect('auto')
# plt.show()


# plt.scatter(age_val, rank_val)
# for i in range(df.shape[0]):
#     plt.text(x = df.age_valorant[i]+ .1, y = df.world_ranking_valorant[i]+ .1, s = df.team_name_valorant[i])

# plt.title("How does rank and age correlate? Valorant")
# plt.arrow(26, 0, -5, 0, width = 0.05, head_width = .5, head_length = .15)
# plt.arrow(20, 12, 0, -10, width = 0.03, head_width = .15, head_length = .5)
# plt.xlabel("Age")
# plt.ylabel("Rank")
# plt.imshow(img, extent = [19,26,-1,13])

# ellipse = matplotlib.patches.Ellipse(xy = (21.15,1.2), width = 1.8, height = 1.1, fill = False, edgecolor = 'b', lw = .5)
# plt.gca().add_patch(ellipse)
# plt.text(x = 20.5, y = 1, s = "Young & Successful", fontsize = 'x-large')

# ellipse = matplotlib.patches.Ellipse(xy = (24.85,1.2), width = 1.4, height = 1.1, fill = False, edgecolor = 'b', lw = .5)
# plt.gca().add_patch(ellipse)
# plt.text(x = 24.5, y = 1, s = "Old is GOLD", fontsize = 'x-large')

# ellipse = matplotlib.patches.Ellipse(xy = (24.85,10.2), width = 1.4, height = 1.1, fill = False, edgecolor = 'b', lw = .5)
# plt.gca().add_patch(ellipse)
# plt.text(x = 24.5, y = 10, s = "Old but bad", fontsize = 'x-large')

# ellipse = matplotlib.patches.Ellipse(xy = (21,10.2), width = 1.7, height = 1.1, fill = False, edgecolor = 'b', lw = .5)
# plt.gca().add_patch(ellipse)
# plt.text(x = 20.5, y = 10, s = "Emerging Talent", fontsize = 'x-large')

# plt.gca().set_aspect('auto')
# plt.show()



# Here we are comparing ages between valorant and csgo

# fig1, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, figsize = (9,4), sharex = True)
# ax1.set_title("Csgo Ages")
# ax1.hist(x = age_csgo, bins = 12)

# ax2.set_title("Valorant Ages")
# ax2.hist(x = age_val, bins = 12)

#plt.show()


fig2, (ax1, ax2) = plt.subplots(1,2)
ax1.set_title("Csgo Ages")
ax1.boxplot(age_csgo)

ax2.set_title("Valorant Ages")
ax2.boxplot(age_val)

plt.show()

