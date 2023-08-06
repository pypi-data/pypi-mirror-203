<div align="center">
<h2>
    Diffusion WebUI: Stable Diffusion + ControlNet + Inpaint
</h2>
<h4>
    <img width="700" alt="teaser" src="data/logo.png">
</h4>
</div>

### Installation
```bash
git clone https://github.com/kadirnar/dress_diff
cd dress_diff
pip install -r requirements.txt
pip install -e.
```

### Web Demo Usage
```python
from dress_diff import app

app()
```

### Text2Image API Usage
```python
from dress_diff import StableDiffusionText2ImageGenerator, get_scheduler_list, scheduler_list

generate = StableDiffusionText2ImageGenerator().generate_image(
    model_path="dress_diff",
    prompt="dress",
    negative_prompt="bad,ugly",
    num_images_per_prompt=1,
    scheduler=scheduler_list[0],
    guidance_scale=7.5,
    num_inference_steps=50,
    height=512,
    width=512,
    seed_generator=0 # 0 for random seed
)
```
