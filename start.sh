echo "Cloning Repo...."
git clone https://github.com/NaaLink/NaaLink-Converter-Bot-V2.git /NaaLink-Converter-Bot-V2
cd /NaaLink-Converter-Bot-V2
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
