import ultralytics,os
workspace = os.path.dirname(os.path.dirname(os.path.abspath(ultralytics.__file__)))
os.chdir(workspace)
print("set workspace:", workspace)




from ultralytics.data.utils import load_dataset_cache_file




def check_cache_func(cache_path):
    cache_data=load_dataset_cache_file(cache_path)
    # print("cache_data:", cache_data)s
    print("cache_path:", cache_path)
    print("cache_data keys:", cache_data.keys())
 

    labels=cache_data.get('labels', None)
    if labels is not None:
        print("labels len:", len(labels))

    # count how many boxes 
    total_boxes=0
    if labels is not None:
        for label in labels:
            boxes=label.get('cls', None)
            if boxes is not None:
                total_boxes+=len(boxes)
    print("total boxes in all labels:", total_boxes)



    # file 
    num=0
    if num <1: return 

    print(f"First {num} labels:")
    for i in range(num):
        print("-"*100)
        print(f"Label {i}:")



        # for key, val in cache_data['labels'][i].items():
        #     print(f"  {key}: {val}")
        # check the maxminum value of cls is smaller than the length of texts
        cls_list=cache_data['labels'][i]['cls']
        im_file=cache_data['labels'][i]['im_file']
        print(" im_file:", im_file)
        # print("  cls_list:", cls_list)
        print(" number of boxes:", len(cls_list))
        # texts=cache_data['labels'][i]['texts']
        # if max(cls_list)>=len(texts):
        #     print(f"Error: In label {i}, max cls value {max(cls_list)} >= number of texts {len(texts)}")
        # if min(cls_list)<0:
        #     print(f"Error: In label {i}, min cls value {min(cls_list)} < 0")


# cache_path="../datasets/flickr/annotations/final_flickr_separateGT_train_segm.cache"

# check_cache_func(cache_path)

# cache_path="../datasets/flickr/annotations/final_flickr_separateGT_train_segm.engine.cache"
# check_cache_func(cache_path)



# cache_path="../datasets/mixed_grounding/annotations/final_mixed_train_no_coco_segm.cache"
# check_cache_func(cache_path)

# cache_path="../datasets/mixed_grounding/annotations/final_mixed_train_no_coco_segm.engine.cache"
# check_cache_func(cache_path)




cache_path="../datasets/Objects365v1/labels/train.cache"
check_cache_func(cache_path)

cache_path="../datasets/Objects365v1/annotations/objects365_train_segm.engine.cache"
check_cache_func(cache_path)
