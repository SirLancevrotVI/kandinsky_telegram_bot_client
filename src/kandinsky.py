import replicate


def generate_img(text_prompt: str, negative: str = None, seed: str = None):
    arguments = {"prompt": text_prompt}

    if negative:
        arguments["negative_prompt"] = negative

    if seed:
        if seed.isdigit():
            arguments["seed"] = int(seed)

    output = replicate.run(
        "ai-forever/kandinsky-2.2:ea1addaab376f4dc227f5368bbd8eff901820fd1cc14ed8cad63b29249e9d463",
        input=arguments,
    )
    print(output)

    return output


if __name__ == "__main__":
    generate_img("a black sheep with white god ray and black background")
