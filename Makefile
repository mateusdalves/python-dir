VERSION_FILE=VERSION

patch: build-patch
minor: build-minor
major: build-major

build-patch:
	bumpversion patch

build-minor:
	bumpversion minor

build-major:
	bumpversion major