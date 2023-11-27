
from sources.commons import montferret_query
from os import makedirs
from httpx import get
from re import search


async def get_legal_laws_urls(host: str, params: dict | None = None) -> dict:
    
    with open("sources/scripts/legal_laws.fql", "r") as f:
        query = f.read()
        print(f"{query}")

        res = await montferret_query(
            query=query,
            host=host,
            params=params,
        )


        print(res)

        return res


async def download_laws_to_disk(urls: list[str], folder_path: str):
    makedirs(folder_path, exist_ok=True)

    for url in urls:
        print(url)

        response = get(url)
        # total = int(response.headers["Content-Length"])
        content_disposition = response.headers["Content-Disposition"]
        regex = r"filename=(.*)"

        m = search(regex, content_disposition)

        if m is None:
            print("No match")
            continue

        filename = m.group(1)

        with open(f"{folder_path}/{filename}", "wb") as file:
            for chunk in response.iter_bytes():
                file.write(chunk)

            # with tqdm(total=total, unit_scale=True, unit_divisor=1024, unit="B") as progress:
            #     num_bytes_downloaded = response.num_bytes_downloaded
            #     for chunk in response.iter_bytes():
            #         download_file.write(chunk)
            #         progress.update(
            #             response.num_bytes_downloaded - num_bytes_downloaded)
            #         num_bytes_downloaded = response.num_bytes_downloaded
