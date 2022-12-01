if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Akshay962/AkshayChand2004 /AkshayChand2004
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /AkshayChand2004
fi
cd /AkshayChand2004
pip3 install -U -r requirements.txt
echo "Starting Bot....💥"
python3 bot.py
