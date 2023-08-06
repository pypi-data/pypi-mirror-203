import gradio as gr
import torch
from controlnet_aux import HEDdetector
from diffusers import ControlNetModel, StableDiffusionControlNetPipeline
from PIL import Image

from diffusion_webui.utils.model_list import (
    controlnet_hed_model_list,
    stable_model_list,
)
from diffusion_webui.utils.scheduler_list import (
    SCHEDULER_LIST,
    get_scheduler_list,
)


class StableDiffusionControlNetHEDGenerator:
    def __init__(self):
        self.pipe = None

    def load_model(self, stable_model_path, controlnet_model_path, scheduler):
        if self.pipe is None:
            controlnet = ControlNetModel.from_pretrained(
                controlnet_model_path, torch_dtype=torch.float16
            )

            self.pipe = StableDiffusionControlNetPipeline.from_pretrained(
                pretrained_model_name_or_path=stable_model_path,
                controlnet=controlnet,
                safety_checker=None,
                torch_dtype=torch.float16,
            )

        self.pipe = get_scheduler_list(pipe=self.pipe, scheduler=scheduler)
        self.pipe.to("cuda")
        self.pipe.enable_xformers_memory_efficient_attention()

        return self.pipe

    def controlnet_hed(self, image_path: str):
        hed = HEDdetector.from_pretrained("lllyasviel/ControlNet")
        image = Image.open(image_path)
        image = hed(image)

        return image

    def generate_image(
        self,
        image_path: str,
        stable_model_path: str,
        controlnet_hed_model_path: str,
        prompt: str,
        negative_prompt: str,
        num_images_per_prompt: int,
        guidance_scale: int,
        num_inference_step: int,
        sheduler: str,
        seed_generator: int,
    ):

        image = self.controlnet_hed(image_path=image_path)

        pipe = self.load_model(
            stable_model_path=stable_model_path,
            controlnet_model_path=controlnet_hed_model_path,
            scheduler=sheduler,
        )

        if seed_generator == 0:
            random_seed = torch.randint(0, 1000000, (1,))
            generator = torch.manual_seed(random_seed)
        else:
            generator = torch.manual_seed(seed_generator)

        output = pipe(
            prompt=prompt,
            image=image,
            negative_prompt=negative_prompt,
            num_images_per_prompt=num_images_per_prompt,
            num_inference_steps=num_inference_step,
            guidance_scale=guidance_scale,
            generator=generator,
        ).images

        return output

    def app():
        with gr.Blocks():
            with gr.Row():
                with gr.Column():
                    controlnet_hed_image_file = gr.Image(
                        type="filepath", label="Image"
                    )
                    controlnet_hed_prompt = gr.Textbox(
                        lines=1,
                        show_label=False,
                        placeholder="Prompt",
                    )

                    controlnet_hed_negative_prompt = gr.Textbox(
                        lines=1,
                        show_label=False,
                        placeholder="Negative Prompt",
                    )

                    with gr.Row():
                        with gr.Column():
                            controlnet_hed_stable_model_id = gr.Dropdown(
                                choices=stable_model_list,
                                value=stable_model_list[0],
                                label="Stable Model Id",
                            )
                            controlnet_hed_guidance_scale = gr.Slider(
                                minimum=0.1,
                                maximum=15,
                                step=0.1,
                                value=7.5,
                                label="Guidance Scale",
                            )
                            controlnet_hed_num_inference_step = gr.Slider(
                                minimum=1,
                                maximum=100,
                                step=1,
                                value=50,
                                label="Num Inference Step",
                            )

                            controlnet_hed_num_images_per_prompt = gr.Slider(
                                minimum=1,
                                maximum=10,
                                step=1,
                                value=1,
                                label="Number Of Images",
                            )

                        with gr.Row():
                            with gr.Column():
                                controlnet_hed_model_id = gr.Dropdown(
                                    choices=controlnet_hed_model_list,
                                    value=controlnet_hed_model_list[0],
                                    label="ControlNet Model Id",
                                )
                                controlnet_hed_scheduler = gr.Dropdown(
                                    choices=SCHEDULER_LIST,
                                    value=SCHEDULER_LIST[0],
                                    label="Scheduler",
                                )

                                controlnet_hed_seed_generator = gr.Number(
                                    minimum=0,
                                    maximum=1000000,
                                    step=1,
                                    value=0,
                                    label="Seed Generator",
                                )

                    controlnet_hed_predict = gr.Button(value="Generator")

                with gr.Column():
                    output_image = gr.Gallery(
                        label="Generated images",
                        show_label=False,
                        elem_id="gallery",
                    ).style(grid=(1, 2))

            controlnet_hed_predict.click(
                fn=StableDiffusionControlNetHEDGenerator().generate_image,
                inputs=[
                    controlnet_hed_image_file,
                    controlnet_hed_stable_model_id,
                    controlnet_hed_model_id,
                    controlnet_hed_prompt,
                    controlnet_hed_negative_prompt,
                    controlnet_hed_num_images_per_prompt,
                    controlnet_hed_guidance_scale,
                    controlnet_hed_num_inference_step,
                    controlnet_hed_scheduler,
                    controlnet_hed_seed_generator,
                ],
                outputs=[output_image],
            )
