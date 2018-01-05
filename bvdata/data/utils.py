import os, subprocess, shlex

from django.utils.crypto import get_random_string


def get_random_string_32():
    return get_random_string(length=32, allowed_chars='abcdefghijklmnopqrstuvwxyz0123456789')


# source https://gist.github.com/pjhjohn/193c76c22fa167c0841116fb53c0d1eb
# param 'short' for shortening hash (slice for commit hash, abbreviation for tag name)
# param 'tag and not commit' for returning tag name only
# param 'commit and not tag' for returning commit hash only
def gitget(short=False, tag=False, commit=False):
    if tag and commit : tag, commit = False, False
    # Cosntants
    devnull = open(os.devnull, 'w')
    cmd_git_tag_exact = [shlex.split('git describe --tags --exact-match --abbrev=0'),
                         shlex.split('git describe --tags --exact-match --abbrev=1')]
    cmd_git_tag = [shlex.split('git describe --tags --abbrev=1'), shlex.split('git describe --tags --abbrev=0')]
    cmd_git_commit = shlex.split('git rev-parse HEAD')

    # Git Tag Name
    tag_name = None
    try:
        if tag:
            tag_name = subprocess.check_output(cmd_git_tag[short], stderr=devnull)
        success = subprocess.check_call(cmd_git_tag_exact[short], stdout=devnull, stderr=devnull) == 0
        if success:
            tag_name = subprocess.check_output(cmd_git_tag_exact[short], stderr=devnull)
    except subprocess.CalledProcessError:
        pass

    # Git Commit Hash
    commit_hash = subprocess.check_output(cmd_git_commit, stderr=devnull)
    if short:
        commit_hash = commit_hash[:7]

    if tag_name is not None:
        tag_name = tag_name.strip()
    if commit_hash is not None:
        commit_hash = commit_hash.strip()

    if tag:
        return tag_name.decode("utf-8")
    if commit:
        return commit_hash.decode("utf-8")
    return [tag_name, commit_hash][tag_name is None]


# Only Commit Hash
def commit_hash(short=False):
    return gitget(short=short, commit=True)


# Only Tag Name
def tag_name(short=False):
    return gitget(short=short, tag=True)


# Tag Name if exactly matches, Commit Hash otherwise
def mixed(short=False):
    return gitget(short=short)
