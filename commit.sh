rm -rf requirements.txt
python -m pip freeze > requirements.txt
git add .
git commit -m "test"
git push
