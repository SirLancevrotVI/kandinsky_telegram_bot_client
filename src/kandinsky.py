import replicate


def generate_img(
    text_prompt: str,
    negative: str = None,
    seed: str = None,
    num_inference_steps: str = None,
    num_inference_steps_prior: str = None,
    width: str = None,
    height: str = None,
):
    arguments = {"prompt": text_prompt}

    if negative:
        arguments["negative_prompt"] = negative

    if seed:
        if seed.isdigit():
            arguments["seed"] = int(seed)

    if num_inference_steps:
        if num_inference_steps.isdigit():
            arguments["num_inference_steps"] = int(num_inference_steps)

    if num_inference_steps_prior:
        if num_inference_steps_prior.isdigit():
            arguments["num_inference_steps_prior"] = int(num_inference_steps_prior)

    if width:
        if width.isdigit():
            arguments["width"] = int(width)

    if height:
        if height.isdigit():
            arguments["height"] = int(height)

    # balance num_inference_steps (0 <= x <= 500) max-min
    if "num_inference_steps" in arguments:
        arguments["num_inference_steps"] = max(
            0, min(arguments["num_inference_steps"], 500)
        )

    # balance num_inference_steps_prior (0 <= x <= 500) max-min
    if "num_inference_steps_prior" in arguments:
        arguments["num_inference_steps_prior"] = max(
            0, min(arguments["num_inference_steps_prior"], 500)
        )

    # w & h must be in (384, 512, 576, 640, 704, 768, 960, 1024, 1152, 1280, 1536, 1792, 2048)
    # if not, set to nearest
    if "width" in arguments:
        arguments["width"] = min(
            [384, 512, 576, 640, 704, 768, 960, 1024, 1152, 1280, 1536, 1792, 2048],
            key=lambda x: abs(x - arguments["width"]),
        )

    if "height" in arguments:
        arguments["height"] = min(
            [384, 512, 576, 640, 704, 768, 960, 1024, 1152, 1280, 1536, 1792, 2048],
            key=lambda x: abs(x - arguments["height"]),
        )

    output = replicate.run(
        "ai-forever/kandinsky-2.2:ea1addaab376f4dc227f5368bbd8eff901820fd1cc14ed8cad63b29249e9d463",
        input=arguments,
    )
    print(output)

    return output


if __name__ == "__main__":
    generate_img("a black sheep with white god ray and black background")
