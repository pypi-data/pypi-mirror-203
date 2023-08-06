# Test Player
This is a test player.
This description is the same `README.md` file.


## Steps
1. Create `app.py` file
2. Install dependencies
3. Create `LICENSE` file
4. Create `README.md` file
5. Create `setup.py` file

## Dependencies

```
pip install setuptools wheel twine
```

## License
1. Go to https://choosealicense.com/ and click on 'GNU GPLv3'
2. Copy License
3. Create `LICENSE` file (no extension) and paste license content.

## Package release
```
# sdist = source distribution | bdist = build distribution
> python3 setup.py sdist bdist_wheel

# Check dist for invalid markup
> twine check dist/*

# Upload dist
> twine upload dist/*
```
