import ultralytics,os
workspace = os.path.dirname(os.path.dirname(os.path.abspath(ultralytics.__file__)))
os.chdir(workspace)
print("set workspace:", workspace)




from ultralytics.data.utils import load_dataset_cache_file

cache_path="/root/ultra_louis_work/datasets/flickr/annotations/final_flickr_separateGT_train_segm.cache"
cache_path="/root/ultra_louis_work/datasets/flickr/annotations/final_flickr_separateGT_train_segm.engine.cache"


def check_cache_func(cache_path):
    cache_data=load_dataset_cache_file(cache_path)
    # print("cache_data:", cache_data)
    print("cache_data keys:", cache_data.keys())
 

    labels=cache_data.get('labels', None)
    if labels is not None:
        print("labels len:", len(labels))

    print("First 5 labels:")
    for i in range(5):
        print("-"*100)
        print(f"Label {i}:")
        for key, val in cache_data['labels'][i].items():
            print(f"  {key}: {val}")

        # check the maxminum value of cls is smaller than the length of texts
        cls_list=cache_data['labels'][i]['cls']
        texts=cache_data['labels'][i]['texts']
        if max(cls_list)>=len(texts):
            print(f"Error: In label {i}, max cls value {max(cls_list)} >= number of texts {len(texts)}")
        if min(cls_list)<0:
            print(f"Error: In label {i}, min cls value {min(cls_list)} < 0")



cache_path=check_cache_func(cache_path)