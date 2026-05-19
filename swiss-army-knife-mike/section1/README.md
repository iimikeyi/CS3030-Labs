## Section 1 ##
The sentinel Script checks whether the CS3030-Labs directory exists on your system and reports success or an error message. 

## How to Run it ## 
sentinel 

~/bin is in your $PATH first 

## 3 Most Useful Commands ##
- chmod - Changes file permissiosn 
- pip freeze - lists all install packages 
- alias - creates a shortcut for long commands

## Setting up the Environment ##
1. Clone this repo
2. Navigate to `section1/`
3. Run `python -m venv .venv`
4. Activate: `source .venv/bin/activate`
5. Install dependencies: `pip install -r task6/requirements.txt`

## Adding Sentienl to you PATH ##
1. Copy `task8/sentinel` into `~/bin/`
2. Add `export PATH="$PATH:$HOME/bin"` to your `~/.bashrc`
3. Run `source ~/.bashrc`
4. Type `sentinel` from anywhere!
