echo "Cloning Repo...."
git clone https://github.com/Mdisksiteconverorbot/Mdisk-Site-Convertor-Bot.git /Mdisk-Site-Convertor-Bot
cd /Mdisk-Site-Converto-Bot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
