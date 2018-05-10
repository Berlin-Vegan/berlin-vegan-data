from bvdata.data.models import GastroSubmit
from .utils import commit_hash


def commit(request):
    id = commit_hash()
    id_short = commit_hash(short=True)

    git = dict(
        id=id,
        id_short=id_short,
        url=f'https://github.com/Berlin-Vegan/berlin-vegan-data/commits/master'
    )

    return dict(git=git)


def submit_count(request):
    return dict(submit_count=GastroSubmit.objects.all().count())