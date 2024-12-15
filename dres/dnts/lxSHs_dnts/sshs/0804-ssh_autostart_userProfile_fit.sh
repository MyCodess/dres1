


--############################## prof-autostart-agent : FIT : ############
## -------- sshAgent
SSH_AGENT=`which ssh-agent`
SSH_ADD=`which ssh-add`
SSH=`which ssh`

function check_ssh_agent
{
        AGENT_PID=`pgrep -u $LOGNAME ssh-agent | tail -1`

        if [ -z "$AGENT_PID" ]
        then
                echo "starting ssh-agent ...\n"
                find /tmp -user $LOGNAME -name ssh-\* 2> /dev/null
                eval $($SSH_AGENT)
                $SSH_ADD
                $SSH_ADD -l
        else
                if [ $AGENT_PID ]
                then
                        echo "restoring environment for ssh ..."

                        ((AGENT_PID-=1))
                        SOCKET_FILE="`find /tmp -user $LOGNAME -name agent.$AGENT_PID 2> /dev/null`"

                        eval `echo export SSH_AGENT_PID=$AGENT_PID`
                        eval `echo export SSH_AUTH_SOCK=$SOCKET_FILE`

                        $SSH_ADD -l > /dev/null 2>&1
                        if [ $? -eq 1 ]
                        then
                                $SSH_ADD
                        fi
                fi
        fi
}

# main
check_ssh_agent
## ----------- END-sshAgent
--##########################################################################
