from .utils import commit_hash, tag_name


def commit(request):
    id = commit_hash()
    id_short = commit_hash(short=True)
    tag = tag_name()

    git = dict(
        id=id,
        id_short=id_short,
        tag=tag,
        url=f'https://github.com/Berlin-Vegan/berlin-vegan-data/commits/master'
    )

    return dict(git=git)
