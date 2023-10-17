import os
from os.path import join, dirname

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

REPLICATE_API = os.environ.get("REPLICATE_API_TOKEN")
TELEGRAM_BOT_API = os.environ.get("TELEGRAM_BOT_API_TOKEN")

ARGUMENT_REGEXP = "{arg_field}\s+([^\\s]+(\s+[^\\s]+)*)"

COMMAND_ARGUMENTS = {
    "negative": r"(-n|—n|--neg|--negative|—neg|—negative)",
    "seed": r"(-s|--seed|—seed|—s)",
    "num_inference_steps": r"(-i|--num_steps|—num_steps|—i)",
    "num_inference_steps_prior": r"(-p|--num_prior|—num_prior|—p)",
    "width": r"(-w|—w|--width|—width)",
    "height": r"(-h|—h|--height|—height)",
}
