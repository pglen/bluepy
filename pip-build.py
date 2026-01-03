rm -fr dist/*
python3 -m build
auditwheel repair dist/bluepyenc-1.1.0-cp310-cp310-linux_x86_64.whl -w dist
rm dist/bluepyenc-1.1.0-cp310-cp310-linux_x86_64.whl
