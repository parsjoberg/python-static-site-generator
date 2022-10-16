from imp import source_from_cache
import typer
from ssg.site import Site


def main(source="content", dest="dist"):
    config = {
        "source": source,
        "dest": dest
    }
    site = Site(**config).build()


typer.run(main)
