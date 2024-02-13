
git clone --depth 1 https://github.com/installturbotax/installturbotax.github.io.git .
git fetch origin --force --prune --prune-tags --depth 50 refs/heads/main:refs/remotes/origin/main
git checkout --force origin/main
git clean -d -f -f
cat .readthedocs.yaml
asdf global python 3.12.0
python -mvirtualenv $READTHEDOCS_VIRTUALENV_PATH
python -m pip install --upgrade --no-cache-dir pip setuptools
python -m pip install --upgrade --no-cache-dir sphinx readthedocs-sphinx-ext
cat docs/conf.py
