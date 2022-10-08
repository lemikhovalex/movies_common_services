import asyncio
from http import HTTPStatus

from elasticsearch import AsyncElasticsearch

import config.constants as constants
from config.config import CONFIG


async def fill_es_indeies() -> None:
    """
    Создаёт файл и удаляет его, даже если сам тест упал в ошибку
    """
    url = f"http://{CONFIG.es_host}:{CONFIG.es_port}"
    es = AsyncElasticsearch(url)
    indecies = ["genres", "persons", "movies"]
    es = es.options(ignore_status=HTTPStatus.BAD_REQUEST)
    await asyncio.gather(
        *[
            es.indices.create(
                index=idx,
                settings=constants.settings,
                mappings=getattr(constants, f"mappings_{idx}"),
            )
            for idx in indecies
        ]
    )
    await es.close()

if __name__ == "__main__":
    asyncio.run(fill_es_indeies())
    print('index created')
