# SsDL
An *extremely simple* tool to download maps from popular beat saber leaderboard website [scoresaber](https://scoresaber.com).

## Requirements:
- Python (>= 3.8)
- Modded Beat Saber
- Beat Saber Mod Assistant
- OneClick install enabled from BSMA settings

## Usage
Go to the scoresaber website and look for the map's hash, located under the game mode 
![image](https://user-images.githubusercontent.com/47455213/175826605-649ed539-df85-4c22-bb5a-a93367113b21.png)

Copy the hash and paste it in when the script asks you to do so, wait a couple seconds and the map should be installed

## Adding to powershell dotfile
Personally  i highly reccomend using this script with windows terminal and with powershell, since it allows you to add it to your user configuration and recall it whenever you want just by typing in an alias, just like this
![image](https://user-images.githubusercontent.com/47455213/175826775-7aaec35e-a9ff-429a-b23b-8884b9939012.png)

to do this, just add 
```
function ssdl ($command) {
  python3 "*path to ssdl*"
}
```

to your CurrentUserCurrentHost file, found under C:\Users\user\Documents\PowerShell\Microsoft.PowerShell_profile.ps1
