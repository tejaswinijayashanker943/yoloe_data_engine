import ultralytics,os
workspace = os.path.dirname(os.path.dirname(os.path.abspath(ultralytics.__file__)))
os.chdir(workspace)
print("set workspace:", workspace)






# check how many files under the json_dir

def count_json_files(json_dir):
    import os
    count=0
    for filename in os.listdir(json_dir):
        if filename.endswith(".json"):
            count+=1
    return count




json_dir="../buffer/objv1_engine_buffer/1detection_data"
predict_json_dir="../buffer/objv1_engine_buffer/2model_predict"
num_files=count_json_files(json_dir)
print(f"Number of json files in {json_dir}: {num_files}")


num_predict_files=count_json_files(predict_json_dir)
print(f"Number of json files in {predict_json_dir}: {num_predict_files}")


#  


# json_dir="../buffer/mixed_engine_buffer/1grounding_data_merged"
# predict_json_dir="../buffer/mixed_engine_buffer/2model_predict"

# def get_json_pairs(json_dir, predict_json_dir):
#     import os
#     json_files=set()
#     predict_json_files=set()
#     for filename in os.listdir(json_dir):
#         if filename.endswith(".json"):
#             json_files.add(filename)
#     for filename in os.listdir(predict_json_dir):
#         if filename.endswith(".json"):
#             predict_json_files.add(filename)
#     common_files=json_files.intersection(predict_json_files)
#     only_in_json=json_files - predict_json_files
#     only_in_predict=predict_json_files - json_files
#     return common_files, only_in_json, only_in_predict

# print("Checking json files between:")
# print(" json_dir:", json_dir)
# print(" predict_json_dir:", predict_json_dir)
# common_files, only_in_json, only_in_predict=get_json_pairs(json_dir, predict_json_dir)
# print(f"Number of common json files: {len(common_files)}")
# print(f"Number of json files only in {json_dir}: {len(only_in_json)}")
# print(f"Number of json files only in {predict_json_dir}: {len(only_in_predict)}")