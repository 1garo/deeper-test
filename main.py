# Very important here - the lower the interger, the higher the priority
# 1 higher
# 100 lower
import json
import itertools
from operator import itemgetter
from collections import OrderedDict, defaultdict

with open('source_file_2.json', 'r') as myfile:
    data=myfile.read()

obj = json.loads(data)
ord_obj = OrderedDict()
ord_obj  = obj
ordered_object = sorted(ord_obj, key=lambda x: x["priority"])
res_managers = {} 
res_watchers = {}
for i in ordered_object:
    res_managers.update({
        i["name"]: i["managers"]
    })
    res_watchers.update({
        i["name"]: i["watchers"]
    })

res_m = defaultdict(list)
res_w = defaultdict(list)
for key, val in sorted(res_managers.items()):
    res_m[val[0]].append(key)
for key, val in sorted(res_watchers.items()):
    res_w[val[0]].append(key)

with open("managers.json", "w") as fout: 
    json.dump(res_m, fout, indent=4)

with open("watchers.json", "w") as fout: 
    json.dump(res_w, fout, indent=4)
