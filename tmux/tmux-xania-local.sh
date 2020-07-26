#!/bin/sh  
# based on http://ryan.himmelwright.net/post/scripting-tmux-workspaces/  

# set environmental variables
XANIA_HOME=$(find ~ -type d -name xania 2>/dev/null) 
SESSION="Xania" 
SESSIONEXISTS=$(tmux list-sessions | grep $SESSION)

# Only create tmux session if it doesn't already exist
if [ "$SESSIONEXISTS" = "" ] 
then     

	# Start New Session with our name     
	tmux new-session -d -s $SESSION      

	# Name first Pane and start bash     
	tmux rename-window -t 0 'Dev'     
	tmux send-keys -t 'Dev' 'cd $XANIA_HOME' C-m 'clear' C-m 'vim xania' C-m     

	# Create and setup pane for build bin     
	tmux new-window -t $SESSION:1 -n 'Build'     
	tmux send-keys -t 'Build' 'cd $XANIA_HOME && cd xania/install/bin' C-m 
	tmux send-keys -t 'Build' './doorman' C-m
	tmux split-window -h -t 'Build'	
	tmux send-keys -t 'Build' 'cd $XANIA_HOME && cd xania/area && ../install/bin/xania' C-m 
	tmux send-keys './xania' C-m	

	# setup Writing window     
	tmux new-window -t $SESSION:2 -n 'Play'     
	tmux send-keys -t 'Play' 'cd $XANIA_HOME && clear' C-m

	# Setup an additional shell     
	tmux new-window -t $SESSION:2 -n 'Shell'     
	tmux send-keys -t 'Shell' C-m 'cd $XANIA_HOME && clear' C-m 
fi

# Attach Session on the Main window 
tmux attach-session -t $SESSION:0

