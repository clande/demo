import asyncio
import os
import oneai
from oneai import Input, Output

oneai.api_key = os.getenv("ONEAI_KEY")


async def split(filepath):
    pipeline = oneai.Pipeline(
        steps=[
            oneai.skills.SplitByTopic(),
        ]
    )

    with open(filepath, 'r') as file_input:
        output = await pipeline.run_batch_async([file_input], on_output=handle_success, on_error=handle_error)
        print(f'OUTPUT = {output}')


def handle_success(input, output_map: [Input, Output]) -> None:
    print(f'success: spans = ')
    for span in output_map.segments.output_spans:
        print(span)


def handle_error(input, output_map: [Input, Exception]) -> None:
    print(f'failure: {output_map}')


asyncio.run(split('file_store/Auburn.txt'))
# asyncio.run(split('file_store/1_min_sample.mp3.txt'))
