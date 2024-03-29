from asyncio import run
from sources.elperuano import get_legal_laws_urls, download_laws_to_disk
from dotenv import load_dotenv
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
from llama_index.indices.base import BaseGPTIndex
from pathlib import Path

DEFAULT_DATA_FOLDER = ".elperuano"
DEFAULT_MONTFERRET_WORKER_URL = "https://montferret-worker-production.up.railway.app"
DEFAULT_LAWS_FOLDER = f"{DEFAULT_DATA_FOLDER}/laws"
DEFAULT_SAVED_VERSION_FILEPATH = f"{DEFAULT_DATA_FOLDER}/saved_version.json"


async def download_laws(
        day_from: int,
        month_from: int,
        year_from: int,
        day_to: int,
        month_to: int,
        year_to: int
):
    params = {
        "day_from": day_from,
        "month_from": month_from - 1,
        "year_from": year_from,
        "day_to": day_to,
        "month_to": month_to - 1,
        "year_to": year_to
    }
    urls = await get_legal_laws_urls(DEFAULT_MONTFERRET_WORKER_URL, params= params)
    await download_laws_to_disk(urls, folder_path=DEFAULT_LAWS_FOLDER)


async def load_laws_as_index(saved_version_filepath: str) -> BaseGPTIndex:
    if not Path(saved_version_filepath).exists():
        documents = SimpleDirectoryReader(DEFAULT_LAWS_FOLDER).load_data()
        index = GPTSimpleVectorIndex.from_documents(documents)
        index.save_to_disk(saved_version_filepath)

        return index

    index = GPTSimpleVectorIndex.load_from_disk(saved_version_filepath)

    return index


async def main():
    load_dotenv()

    await download_laws(1,11,2023,30,11,2023)
    # laws_index = await load_laws_as_index(DEFAULT_SAVED_VERSION_FILEPATH)
    # res = laws_index.query(
    #     "Resume los cambios más importantes en el sistema de justicia penal",
    #     mode="summarize",
    # )

    # print(res)

run(main())
