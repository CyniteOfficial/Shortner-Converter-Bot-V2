echo "Cloning Repo...."
git clone https://github.com/hintpirox/conq.git /conq
cd /conq
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
