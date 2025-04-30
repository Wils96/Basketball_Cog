# 1. Clone or update
git clone https://github.com/<you>/<repo>.git
cd repo
git pull

# 2. Remove the file
git rm path/to/the/file.ext

# 3. Commit the deletion
git commit -m "Remove file.ext"

# 4. Push back up
git push origin main
# (or the branch you’re working on)
