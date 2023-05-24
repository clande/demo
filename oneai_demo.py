import asyncio
import os
import oneai

oneai.api_key = os.getenv("ONEAI_KEY")


async def insert_collection():
    collection_insert = oneai.Pipeline(steps=[
        oneai.skills.SplitByTopic(),  # split the content to smaller chunks
        oneai.skills.CollectionInsert(  # insert the chunks into the collection
            input_skill=oneai.skills.SplitByTopic(),  # use output of SplitByTopic Skill
            collection='blah5',  # collection ID
        ),
    ])
    with open('file_store/1_min_sample.mp3.txt', 'r') as file_input:
        output = await collection_insert.run_async(file_input)
        print(f"Insert completed = {output}")

asyncio.run(insert_collection())
