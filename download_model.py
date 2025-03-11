from huggingface_hub import snapshot_download
from tqdm.auto import tqdm
model_id = "runwayml/stable-diffusion-v1-5"
model_dir = "/path/to/your/model_dir" # like "/data/huggingface/models/runwayml/stable-diffusion-v1-5"

auth_token = "your_token" # get this token from huggingface and paste here
allow_patterns = ['feature_extractor/*', 'safety_checker/*', 'scheduler/*', 'text_encoder/*', 'tokenizer/*', 'unet/*', 'vae/*', 'diffusion_pytorch_model.bin', 'scheduler_config.json', 'config.json', 'model.onnx', 'model_index.json']
ignore_patterns = "*.msgpack"
user_agent = "diffusers/0.8.0; python/3.7.12; torch/1.12.1+cu113; pipeline_class/StableDiffusionPipeline"
snapshot_download(
    repo_id=model_id,
    cache_dir=model_dir,
    resume_download=True,
    token=auth_token,
    allow_patterns=allow_patterns,
    ignore_patterns=ignore_patterns,
    user_agent=user_agent
)