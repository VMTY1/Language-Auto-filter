if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Akshay962/new2v /new2v
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /new2v
fi
cd /new2v
pip3 install -U -r requirements.txt
echo "Starting Bot....💥"
python3 bot.py
