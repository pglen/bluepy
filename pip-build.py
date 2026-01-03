rm -fr dist/*
python3 -m build
auditwheel repair dist/bluepyenc-*-cp310-cp310-linux_x86_64.whl -w dist
rm dist/bluepyenc-*-cp310-cp310-linux_x86_64.whl
