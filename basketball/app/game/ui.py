git clone https://github.com/Wils96/Basketball_Cog.git
cd Basketball_Cog
git checkout -b delete-file-branch
git rm basketball/app/game/ui.py
git commit -m "Delete basketball/app/game/ui.py"
git push origin delete-file-branch
