# Word-As-Image
A runnable version of project "Word-As-Image"

## What to do about the Word-As-Image code
1. change the losses.py, you could copy the file in the code directory or just change the "np.bool" in line 164 of file Word-As-Image/code/losses.py to "np.bool_"
2. change the line 23 in Word-As-Image/code/config/base.yaml if you are unable to connect to the huggingface_hub, I recommend to use the download_model.sh to download the model especially who can not directly visit huggingface
## What to do in the word environment
1. change `from huggingface_hub import HfFolder, cached_download, hf_hub_download, model_info` into `from huggingface_hub import HfFolder, hf_hub_download, model_info`, and `resolved_module_file = cached_download(` into `resolved_module_file = hf_hub_download(` accordingly in the file $CONDA_PREFIX/lib/python3.8/site-packages/diffusers/dynamic_modules_utils.py
2. 
