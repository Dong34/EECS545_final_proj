# The new config inherits a base config to highlight the necessary modification
_base_ = '/home/yierdong/eecs545_proj_new/food-recognition-benchmark-starter-kit/Swin-Transformer-Object-Detection/configs/swin/mask_rcnn_swin_tiny_patch4_window7_mstrain_480-800_adamw_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=50),
        mask_head=dict(num_classes=50)))

# Modify dataset related settings
dataset_type = 'COCODataset'
# classes = ('water','jam')
classes = ('water', 'salad-leaf-salad-green', 'bread-white', 'tomato-raw', 'butter', 'carrot-raw', 'bread-wholemeal', 'coffee-with-caffeine', 'rice', 'egg', 'mixed-vegetables', 'apple', 'jam', 'cucumber', 'wine-red', 'banana', 'cheese', 'potatoes-steamed', 'bell-pepper-red-raw', 'hard-cheese', 'espresso-with-caffeine', 'tea', 'bread-whole-wheat', 'mixed-salad-chopped-without-sauce', 'avocado', 'white-coffee-with-caffeine', 'tomato-sauce', 'wine-white', 'broccoli', 'strawberries', 'pasta-spaghetti', 'honey', 'zucchini', 'parmesan', 'chicken', 'chips-french-fries', 'braided-white-loaf', 'dark-chocolate', 'mayonnaise', 'pizza-margherita-baked', 'blueberries', 'onion', 'salami', 'leaf-spinach', 'soft-cheese', 'salmon', 'water-mineral', 'gruyere', 'glucose-drink-50g', 'yaourt-yahourt-yogourt-ou-yoghourt-natural')
data = dict(
    train=dict(
        img_prefix='/home/yierdong/eecs545_proj_new/food-recognition-benchmark-starter-kit/data/train/images',
        classes=classes,
        ann_file='/home/yierdong/eecs545_proj_new/food-recognition-benchmark-starter-kit/data/train/new_top50cat_train_filter_no_blur.json'),
    val=dict(
        img_prefix='/home/yierdong/eecs545_proj_new/food-recognition-benchmark-starter-kit/data/val/images',
        classes=classes,
        ann_file='/home/yierdong/eecs545_proj_new/food-recognition-benchmark-starter-kit/data/val/new_top50cat_val_filter_no_blur.json'),
    test=dict(
        img_prefix='/home/yierdong/eecs545_proj_new/food-recognition-benchmark-starter-kit/data/val/images',
        classes=classes,
        ann_file='/home/yierdong/eecs545_proj_new/food-recognition-benchmark-starter-kit/data/val/new_top50cat_val_filter_no_blur.json'))

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'checkpoints/mask_rcnn_swin_tiny_patch4_window7_1x.pth'