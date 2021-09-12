import pickle
import glob
import os
import shutil


#with open ('retrieval-SfM-120k.pkl', 'rb') as f:
with open ('sfmnd0.25-b6bfcb44.pkl', 'rb') as f:
  train = pickle.load(f)

#origin_filepath = "unsize"
test_filepath = "./sfmnd_ver0.0.0"
origin_filepath = "ims.tar/ims/*/*/*/*"
l = []
in_val = train["train"]
idx_cluster_q = in_val["qidxs"]
idx_cluster_p = in_val["pidxs"]
idx_cids = in_val["cids"]
if os.path.exists(test_filepath):
    pass
else:
    os.mkdir(test_filepath)

print("making list")
for p in glob.glob(origin_filepath):
    l.append(p)

print("making complete")
num_category = len(l)
num_cluster = max(idx_cluster_p)


for i in range(num_category):
    #test_filename = test_filepath + "/" + str(idx_cluster[i])
    test_filename = test_filepath + "/" + str(i)
    if os.path.exists(test_filename):
        pass
    else:
        os.mkdir(test_filename)
    print(str(i) + "category")
    l_in = [s for s in l if idx_cids[idx_cluster_p[i]] in s]
    shutil.copy(l_in[0], test_filename)
    l_in = [s for s in l if idx_cids[idx_cluster_q[i]] in s]
    shutil.copy(l_in[0], test_filename)
