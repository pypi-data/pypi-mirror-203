import argparse

import requests
import tabulate

from rich import print as rprint
from rich.console import Console
from rich.markdown import Markdown

DOCKERHUB_API = "https://hub.docker.com/api/content/v1"
DOCKERHUB_REGISTRY_API = "https://registry.hub.docker.com/v2"

def pprint(data):
    header = data[0].keys()
    rows =  [x.values() for x in data]
    print(tabulate.tabulate(rows, header))

def search(args):
    url_official = f"{DOCKERHUB_API}/products/search?page_size={args.number}&q={args.query}"
    url = f"{DOCKERHUB_API}/products/search?page_size={args.number}&source=community&q={args.query}"
    res_official = requests.get(url_official)
    res = requests.get(url)
    images_official = []
    images = []
    if res.json()["count"] > 0:
        images = [{"name": entry["name"], "desc": entry["short_description"], "official": "", "url": f"https://hub.docker.com/{'_' if entry['source'] == 'library' else entry['source']}/{entry['name']}"} for entry in res.json()["summaries"]]
    if res_official.json()["count"] > 0:
        images_official = [{"name": entry["name"], "desc": entry["short_description"],  "Official": "Yes", "url": f"https://hub.docker.com/{'_' if entry['source'] == 'library' else entry['source']}/{entry['name']}"} for entry in res_official.json()["summaries"]]
    all_images = images_official + images
    if not args.url:
        all_images = [{i:image[i] for i in image if i != "url"} for image in all_images]
    pprint(all_images)

def tags(args):
    image = args.query.split("/")
    if len(image) == 1:
        a = "library"
        b = image[0]
    else:
        a = image[0]
        b = image[1]
    url = f"{DOCKERHUB_REGISTRY_API}/repositories/{a}/{b}/tags?page_size={args.number}"
    res = requests.get(url).json()
    tags = [{"tag": entry["name"], "digest": entry["digest"] if "digest" in entry else entry["images"][0]["digest"]} for entry in res["results"]]
    res = {}
    for tag in tags:
        res.setdefault(tag['digest'], []).append(tag["tag"])
    res2 = [{"tags": ", ".join(res[k])} for k in res]
    pprint(res2)

def readme(args):
    image = args.query.split("/")
    if len(image) == 1:
        a = "library"
        b = image[0]
    else:
        a = image[0]
        b = image[1]
    url = f"{DOCKERHUB_REGISTRY_API}/repositories/{a}/{b}"
    res = requests.get(url).json()
    rprint(res["full_description"])
    console = Console()
    md = Markdown(res["full_description"])
    if args.no_pager:
        rprint(md)
    else:
        with console.pager():
            console.print(md)

def main():
    parser = argparse.ArgumentParser()
    parsers = parser.add_subparsers()
    search_parser = parsers.add_parser("search")
    search_parser.add_argument("query")
    search_parser.add_argument("--number", "-n", default="25")
    search_parser.add_argument("--url", "-u", action="store_true")
    search_parser.set_defaults(func=search)

    tags_parser = parsers.add_parser("tags")
    tags_parser.add_argument("query")
    tags_parser.add_argument("--number", "-n", default="25")
    tags_parser.set_defaults(func=tags)

    readme_parser = parsers.add_parser("readme")
    readme_parser.add_argument("query")
    readme_parser.add_argument("--no-pager", action="store_true")
    readme_parser.set_defaults(func=readme)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
        sys.exit(1)



if __name__ == "__main__":
    main()
