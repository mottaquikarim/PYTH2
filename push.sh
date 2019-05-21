#!/bin/sh

setup_git() {
  echo "IN setup_git"
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
  echo "DONE setup_git"
}

commit_to_git() {
  echo "IN commit_to_git"
  echo "----------------"

  git remote add origin2 https://$GH_TOKEN@github.com/mottaquikarim/PYTH2.git
  git checkout -f $TRAVIS_BRANCH 

  echo "CALL PY"
  pwd
  python scripts/convert_to_nb.py
  python scripts/build_summary.py
  git status
  echo "DONE PY"

  git add .
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER [ci skip]"
  echo "----------------"
  echo "DONE commit_to_git"
}

push_to_git() {
  echo "IN push_to_git"
  echo ${GH_TOKEN}
  echo https://$GH_TOKEN@github.com/mottaquikarim/PYTH2.git
  git push --quiet --set-upstream origin2 $TRAVIS_BRANCH
  echo "DONE push_to_git"
}

setup_git || true
commit_to_git || true
push_to_git || true
EXIT_CODE=$?

exit ${EXIT_CODE}
