# Word-As-Image
A runnable version of project "Word-As-Image"

## What to do about the Word-As-Image code
1. change the losses.py, you could copy the file in the code directory or just change the "np.bool" in line 164 of file Word-As-Image/code/losses.py to "np.bool_"
2. change the line 23 in Word-As-Image/code/config/base.yaml to the path of model_index.json which you have already downloaded locally if you are unable to connect to the huggingface_hub, I recommend to use the download_model.sh to download the model especially who can not directly visit huggingface
## What to do in the word environment
### Create the word environment and install dependencies
```
conda create --name word python=3.8.15
conda activate word
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 --extra-index-url https://download.pytorch.org/whl/cu113
conda install -y numpy scikit-image
conda install -y -c anaconda cmake=3.12.2 # this is mainly different part from the origin setup steps given by repo Word-As-Image
conda install -y -c conda-forge ffmpeg
pip install svgwrite svgpathtools cssutils numba torch-tools scikit-fmm easydict visdom freetype-py shapely
pip install opencv-python==4.5.4.60  
pip install kornia==0.6.8
pip install wandb
pip install shapely
pip install diffusers==0.8
pip install transformers scipy ftfy accelerate
git clone https://github.com/BachiLi/diffvg.git
cd diffvg/
git submodule update --init --recursive
DIFFVG_CUDA=1 python setup.py install # Add DIFFVG_CUDA=1, or it will bring error that diffvg does not compile with GPU
```
### change specific files
1. change `from huggingface_hub import HfFolder, cached_download, hf_hub_download, model_info` into `from huggingface_hub import HfFolder, hf_hub_download, model_info`, and `resolved_module_file = cached_download(` into `resolved_module_file = hf_hub_download(` accordingly in the file $CONDA_PREFIX/lib/python3.8/site-packages/diffusers/dynamic_modules_utils.py
2. 
