# -*- coding: utf-8 -*-
# *******************************************************
#   ____                     _               _
#  / ___|___  _ __ ___   ___| |_   _ __ ___ | |
# | |   / _ \| '_ ` _ \ / _ \ __| | '_ ` _ \| |
# | |__| (_) | | | | | |  __/ |_ _| | | | | | |
#  \____\___/|_| |_| |_|\___|\__(_)_| |_| |_|_|
#
#  Sign up for free at http://www.comet.ml
#  Copyright (C) 2015-2021 Comet ML INC
#  This file can not be copied and/or distributed without the express
#  permission of Comet ML Inc.
# *******************************************************

import io
import json
from typing import Any, Dict

from . import completion, session_registry


def completion_create(experiment, original, return_value, *args, **kwargs):
    if not experiment.auto_metric_logging:
        return

    prompt, model = kwargs["prompt"], kwargs["model"]

    session_step = session_registry.accumulate_and_get(experiment.id, "step", 1)
    _log_token_metrics(experiment, return_value, session_step)

    prompt_call = completion.prompt_call(model, prompt, return_value)
    session_prompt_calls = session_registry.accumulate_and_get(
        experiment.id, "prompt_calls", [prompt_call]
    )
    experiment.log_asset(
        io.StringIO(json.dumps(session_prompt_calls)),
        file_name="openai-prompts.json",
        overwrite=True,
    )

    choices = [choice["text"] for choice in return_value["choices"]]
    prompts_choices = completion.prompt_choice_generator(prompt, choices)
    for prompt, choice in prompts_choices:
        experiment.log_text(prompt, metadata={"choice": choice}, step=session_step)


def _log_token_metrics(experiment, response: Dict[str, Any], step: int) -> None:
    usage = response["usage"]

    for token_key in ["prompt_tokens", "completion_tokens", "total_tokens"]:
        used_amount = session_registry.accumulate_and_get(
            experiment.id, token_key, usage[token_key]
        )
        experiment.log_metric("openai_{}".format(token_key), used_amount, step=step)
