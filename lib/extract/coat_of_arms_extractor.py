import os
import re
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

from lib.config.municipality_information_system_loader import (
    MunicipalityInformationSystem,
)


def extract_coat_of_arms(
    results_path,
    municipality_information_systems: list[MunicipalityInformationSystem],
    clean=False,
    quiet=False,
):
    results_path = os.path.join(results_path, "germany-municipalities-coat-of-arms")

    # Make results path
    os.makedirs(os.path.join(results_path), exist_ok=True)

    session = requests.Session()
    # Define a descriptive User-Agent as required by Wikimedia Foundation policy
    session.headers.update(
        {
            "User-Agent": "Open Data Product/1.0 (opendataproduct@gmail.com) Python-Requests"
        }
    )

    retries = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        raise_on_status=True,
    )
    session.mount("https://", HTTPAdapter(max_retries=retries))

    search_url = "https://de.wikipedia.org/w/api.php"

    for municipality_information_system in municipality_information_systems:
        sanitized_name = (
            municipality_information_system.municipality_name.split(",")[0]
            .replace("/", " ")
            .replace("(", "")
            .replace(")", "")
        )
        sanitized_file_name = (
            municipality_information_system.municipality_name.split(",")[0]
            .lower()
            .replace("/", " ")
            .replace("(", "")
            .replace(")", "")
            .replace(" ", "-")
            .replace("_", "-")
            .replace("ä", "ae")
            .replace("ö", "oe")
            .replace("ü", "ue")
            .replace("ß", "ss")
        )
        file_path = os.path.join(
            results_path,
            f"{municipality_information_system.ars}-{sanitized_file_name}.png",
        )

        if not clean and os.path.exists(file_path):
            not quiet and print(f"✓ Already exists {os.path.basename(file_path)}")
            continue

        search_params = {
            "action": "query",
            "list": "search",
            "srsearch": sanitized_name,
            "format": "json",
        }

        try:
            res = session.get(search_url, params=search_params)
            res.raise_for_status()
            search_res = res.json()
            search_results = search_res.get("query", {}).get("search", [])

            if not search_results:
                not quiet and print(f"✗ No Wikipedia pages found for {sanitized_name}")
                continue

            # Iterate through search results to verify the ARS inside the page content
            target_title = None
            for result in search_results:
                title = result["title"]

                # Fetch the raw wikitext content of the candidate page to confirm the ARS
                content_params = {
                    "action": "query",
                    "prop": "revisions",
                    "titles": title,
                    "rvprop": "content",
                    "format": "json",
                    "formatversion": "2",
                }

                res = session.get(search_url, params=content_params)
                res.raise_for_status()
                content_res = res.json()
                page_data = content_res.get("query", {}).get("pages", [{}])[0]
                wikitext = page_data.get("revisions", [{}])[0].get("content", "")

                # Clean the wikitext to find the AGS (8 digits) or ARS (12 digits).
                # German Wikipedia infoboxes typically list the 8-digit Gemeindeschlüssel (AGS),
                # often formatted with spaces (e.g. "09 1 84 112").
                wikitext_clean = wikitext.replace(" ", "").replace("\xa0", "")
                if (
                    municipality_information_system.ags in wikitext_clean
                    or municipality_information_system.ars in wikitext_clean
                ):
                    target_title = title
                    break

            if not target_title:
                print(
                    f"✗ Could not verify page for {sanitized_name} with AGS {municipality_information_system.ags} / ARS {municipality_information_system.ars}"
                )
                continue

            # Use pageimages API tool to extract the primary image (the coat of arms)
            image_params = {
                "action": "query",
                "prop": "pageimages",
                "titles": target_title,
                "piprop": "original",
                "format": "json",
                "formatversion": "2",
            }

            res = session.get(search_url, params=image_params)
            res.raise_for_status()
            image_res = res.json()
            page_image_info = image_res.get("query", {}).get("pages", [{}])[0]

            # Extract the original source URL of the image
            url = page_image_info.get("original", {}).get("source")

            if not url:
                print(f"✗ No image found for {target_title}")
                continue

            if "upload.wikimedia.org" in url and url.endswith(".svg"):
                # Match the structure of a standard Wikipedia upload URL
                match = re.search(
                    r"https://upload\.wikimedia\.org/wikipedia/commons/(.*?)/(.*?)/(.*\.svg)",
                    url,
                )
                if match:
                    a, b, filename = match.groups()
                    url = f"https://upload.wikimedia.org/wikipedia/commons/thumb/{a}/{b}/{filename}/960px-{filename}.png"

            try:
                with session.get(url, stream=True) as response:
                    response.raise_for_status()

                    with open(file_path, "wb") as file:
                        for chunk in response.iter_content(chunk_size=8192):
                            if chunk:
                                file.write(chunk)

                print(f"✓ Extracted {os.path.basename(file_path)}")

            except Exception as e:
                print(f"✗ Failed to download image from {url}. Error: {e}")
                continue

        except Exception as e:
            print(f"✗ An error occurred while crawling: {e}")
            # continue
            raise e
