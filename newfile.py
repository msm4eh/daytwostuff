# %%
#terminal display path: @msm4eh ➜ /workspaces/daytwostuff (main)

# %% 
# you should not include the virtual environment in the repo because it is a very large file and can instead be easily recreated using the requirements.txt file

#new terminal display path: (venv) @msm4eh ➜ /workspaces/daytwostuff (main)

# %% 
import pandas as pd
data = pd.read_csv("best_selling_albums.csv")

# From the extension menu, I noticed that it says it is enabled on 'Codespaces: special xylophone' and it says I can disable or unistall it, implying it is currently in an active status. I also noticed that it was published 2 years ago but updated a month ago.

# Three useful elements of the extension are: 
# 1. it can remove or fill missing data values
# 2. it can automatically generate visualizations with the dataset
# 3. it generates and shows the code it is using to clean/wrangle your data

#%% the requirements.txt is useful to easily reproduce the virtual environment with all the correct packages and versions needed to recreate the project.
