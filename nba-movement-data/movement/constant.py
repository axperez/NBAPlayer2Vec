import os
# change this data_dir for personal path
if os.environ['HOME'] == '/home/ax':
    data_dir = '/home/ax/Projects/thesis/NBAPlayer2Vec/nba-movement-data'
else:
    raise Exception("Unspecified data_dir, unknown environment")