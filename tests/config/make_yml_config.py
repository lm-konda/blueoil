'''
Auto config yaml generator (for unit test)

usage:
  python make_yml_config.py

how to modify:
  add comment or array for each setting
  and
  display them.
'''

header_line = "# supported task types are 'classification', 'object_detection' and 'semantic_segmentation'.\n"

output_files = [
    'caltech101_classification',
    'caltech101_classification_has_validation',
    'delta_mark_classification',
    'delta_mark_classification_has_validation',
    'delta_mark_object_detection',
    'delta_mark_object_detection_has_validation',
    'openimagesv4_object_detection',
    'openimagesv4_object_detection_has_validation',
]

task_types = [
    'task_type: classification\n\n',
    'task_type: classification\n\n',
    'task_type: classification\n\n',
    'task_type: classification\n\n',
    'task_type: object_detection\n\n',
    'task_type: object_detection\n\n',
    'task_type: object_detection\n\n',
    'task_type: object_detection\n\n',
]

network_names = [
    'network_name: LmnetV1Quantize\n\n',
    'network_name: LmnetV1Quantize\n\n',
    'network_name: LmnetV1Quantize\n\n',
    'network_name: LmnetV1Quantize\n\n',
    'network_name: LMFYoloQuantize\n\n',
    'network_name: LMFYoloQuantize\n\n',
    'network_name: LMFYoloQuantize\n\n',
    'network_name: LMFYoloQuantize\n\n',
]

dataset_formats = [
    '  format: Caltech101\n',
    '  format: Caltech101\n',
    '  format: DeLTA-Mark for Classification\n',
    '  format: DeLTA-Mark for Classification\n',
    '  format: DeLTA-Mark for Object Detection\n',
    '  format: DeLTA-Mark for Object Detection\n',
    '  format: OpenImagesV4\n',
    '  format: OpenImagesV4\n',
]

dataset_train_paths = [
    '  train_path: ./lmnet/tests/fixtures/datasets/dummy_classification\n',
    '  train_path: ./lmnet/tests/fixtures/datasets/dummy_classification\n',
    '  train_path: ./lmnet/tests/fixtures/datasets/custom_delta_mark_classification/for_train\n',
    '  train_path: ./lmnet/tests/fixtures/datasets/custom_delta_mark_classification/for_train\n',
    '  train_path: ./lmnet/tests/fixtures/datasets/custom_delta_mark_object_detection/for_train\n',
    '  train_path: ./lmnet/tests/fixtures/datasets/custom_delta_mark_object_detection/for_train\n',
    '  train_path: ./lmnet/tests/fixtures/datasets/custom_open_images_v4_bounding_boxes/for_train\n',
    '  train_path: ./lmnet/tests/fixtures/datasets/custom_open_images_v4_bounding_boxes/for_train\n',
]

dataset_test_paths = [
    '  test_path: \n',
    '  test_path: ./lmnet/tests/fixtures/datasets/dummy_classification\n',
    '  test_path: \n',
    '  test_path: ./lmnet/tests/fixtures/datasets/custom_delta_mark_classification/for_validation\n',
    '  test_path: \n',
    '  test_path: ./lmnet/tests/fixtures/datasets/custom_delta_mark_object_detection/for_validation\n',
    '  test_path: \n',
    '  test_path: ./lmnet/tests/fixtures/datasets/custom_open_images_v4_bounding_boxes/for_validation\n',
]

trainer_batch_sizes = [
    '  batch_size: 1\n',
    '  batch_size: 1\n',
    '  batch_size: 1\n',
    '  batch_size: 1\n',
    '  batch_size: 1\n',
    '  batch_size: 1\n',
    '  batch_size: 1\n',
    '  batch_size: 1\n',
]

trainer_epochs = [
    '  epochs: 1\n',
    '  epochs: 1\n',
    '  epochs: 1\n',
    '  epochs: 1\n',
    '  epochs: 1\n',
    '  epochs: 1\n',
    '  epochs: 1\n',
    '  epochs: 1\n',
]

trainer_optimizer_comment = "# supported 'optimizer' is 'Momentum', 'SGD', 'Adam' currently.\n"

trainer_optimizers = [
    '  optimizer: MomentumOptimizer\n',
    '  optimizer: MomentumOptimizer\n',
    '  optimizer: MomentumOptimizer\n',
    '  optimizer: MomentumOptimizer\n',
    '  optimizer: MomentumOptimizer\n',
    '  optimizer: MomentumOptimizer\n',
    '  optimizer: MomentumOptimizer\n',
    '  optimizer: MomentumOptimizer\n',
]

trainer_lr_setting_comment = "# supported 'learning_rate_setting' is 'tune1', 'tune2', 'tune3', 'fixed'.\n\
#   'tune1' is 2 times decay, learning rate reduce to 1/10 on epoch/2 and epoch-1.\n\
#   'tune2' is 3 times decay, learning rate reduce to 1/10 on epoch/3 and epoch*2/3 and epoch-1.\n\
#   'tune3' is warmup and 3 times decay, warmup learning rate 1/1000 in 1 epoch, then train same as 'tune2'.\n\
#   'fixed' is constant learning rate.\n"

trainer_lr_settings = [
    '  learning_rate_setting: tune1\n',
    '  learning_rate_setting: tune1\n',
    '  learning_rate_setting: tune1\n',
    '  learning_rate_setting: tune1\n',
    '  learning_rate_setting: tune1\n',
    '  learning_rate_setting: tune1\n',
    '  learning_rate_setting: tune1\n',
    '  learning_rate_setting: tune1\n',
]

trainer_initial_lrs = [
    '  initial_learning_rate: 0.001\n',
    '  initial_learning_rate: 0.001\n',
    '  initial_learning_rate: 0.001\n',
    '  initial_learning_rate: 0.001\n',
    '  initial_learning_rate: 0.001\n',
    '  initial_learning_rate: 0.001\n',
    '  initial_learning_rate: 0.001\n',
    '  initial_learning_rate: 0.001\n',
]

common_image_size_heights = [
    '    - 128  # height\n',
    '    - 128  # height\n',
    '    - 128  # height\n',
    '    - 128  # height\n',
    '    - 128  # height\n',
    '    - 128  # height\n',
    '    - 128  # height\n',
    '    - 128  # height\n',
]

common_image_size_widths = [
    '    - 128  # width\n',
    '    - 128  # width\n',
    '    - 128  # width\n',
    '    - 128  # width\n',
    '    - 128  # width\n',
    '    - 128  # width\n',
    '    - 128  # width\n',
    '    - 128  # width\n',
]

common_is_pretrain_model_comment = '  # set pretrain model name. currently, this feature is not supported, always ignored.\n'

common_is_pretrain_model = [
    '  pretrain_model: false\n',
    '  pretrain_model: false\n',
    '  pretrain_model: false\n',
    '  pretrain_model: false\n',
    '  pretrain_model: false\n',
    '  pretrain_model: false\n',
    '  pretrain_model: false\n',
    '  pretrain_model: false\n',
]

common_enable_prefetch_comment = '  # enable dataset prefetch, set false if weired problem happens\n'

common_enable_prefetch = [
    '  dataset_prefetch: true',
    '  dataset_prefetch: true',
    '  dataset_prefetch: true',
    '  dataset_prefetch: true',
    '  dataset_prefetch: true',
    '  dataset_prefetch: true',
    '  dataset_prefetch: true',
    '  dataset_prefetch: true',
]

def learning_settings_to_yaml(index):
    name = output_files[index]
    config_file = name + ".yml"

    fp = open(config_file, 'w')

    # header
    fp.write(header_line)

    # task type
    fp.write(str(task_types[index]))

    # network name
    fp.write(str(network_names[index]))

    # dataset
    fp.write("dataset:\n")
    # dataset format
    fp.write(str(dataset_formats[index]))
    # dataset train path
    fp.write(str(dataset_train_paths[index]))
    # dataset test path
    fp.write(str(dataset_test_paths[index]))
    fp.write('\n')

    # trainer
    fp.write("trainer:\n")
    # trainer batch size
    fp.write(str(trainer_batch_sizes[index]))
    # trainer epochs
    fp.write(str(trainer_epochs[index]))
    # trainer optimizer comment
    #fp.write(str(trainer_optimizer_comment))
    # trainer optimizer 
    #fp.write(str(trainer_optimizers[index]))
    # trainer lr setting comment
    #fp.write(str(trainer_lr_setting_comment))
    # trainer lr setting
    #fp.write(str(trainer_lr_settings[index]))
    # trainer initial lr
    #fp.write(str(trainer_initial_lrs[index]))
    fp.write('\n')

    # common
    fp.write("common:\n")
    # common image size
    fp.write("  image_size:\n")
    # common image size height
    fp.write(str(common_image_size_heights[index]))
    # common image size width
    fp.write(str(common_image_size_widths[index]))
    fp.write('\n')
    # common is pretrain_model comment
    fp.write(str(common_is_pretrain_model_comment))
    # common is pretrain_model
    fp.write(str(common_is_pretrain_model[index]))
    fp.write('\n')
    # common enable prefetch comment
    fp.write(str(common_enable_prefetch_comment))
    # common enable prefetch
    fp.write(str(common_enable_prefetch[index]))

def main():
    for index in range(0, len(output_files)):
        learning_settings_to_yaml(index)
    
if __name__ == '__main__':
    main()