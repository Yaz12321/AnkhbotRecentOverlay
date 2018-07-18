#---------------------------------------
#	Import Libraries
#---------------------------------------
import clr, sys, json, os, codecs, time
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")
from ast import literal_eval
#---------------------------------------
#	[Required]	Script Information
#---------------------------------------
ScriptName = "FileSwitch"
Website = ""
Creator = "Yaz12321"
Version = "1.0"
Description = "Read Twitch files, and copy them into a text file one at a time"

settingsFile = os.path.join(os.path.dirname(__file__), "settings.json")

#---------------------------------------
#   Version Information
#---------------------------------------

# Version:

# > 1.0< 
    # Official Release

class Settings:
    # Tries to load settings from file if given 
    # The 'default' variable names need to match UI_Config
    def __init__(self, settingsFile = None):
        if settingsFile is not None and os.path.isfile(settingsFile):
            with codecs.open(settingsFile, encoding='utf-8-sig',mode='r') as f:
                self.__dict__ = json.load(f, encoding='utf-8-sig') 
        else: #set variables if no settings file
            self.OnlyLive = False
            self.selectedfiles = "(42,40,39)"
            self.Delay = 10
            selectedfilestitle = "(\"Recent Subscriber\",\"Recent Follower\",\"Recent Donation\")"

            
    # Reload settings on save through UI
    def ReloadSettings(self, data):
        self.__dict__ = json.loads(data, encoding='utf-8-sig')
        return

    # Save settings to files (json and js)
    def SaveSettings(self, settingsFile):
        with codecs.open(settingsFile,  encoding='utf-8-sig',mode='w+') as f:
            json.dump(self.__dict__, f, encoding='utf-8-sig')
        with codecs.open(settingsFile.replace("json", "js"), encoding='utf-8-sig',mode='w+') as f:
            f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8-sig')))
        return


#---------------------------------------
# Initialize Data on Load
#---------------------------------------
def Init():
    # Globals
    global MySettings

    # Load in saved settings
    MySettings = Settings(settingsFile)

    global t
    t = time.time()
    global n
    n = 0

    # End of Init
    return

#---------------------------------------
# Reload Settings on Save
#---------------------------------------
def ReloadSettings(jsonData):
    # Globals
    global MySettings

    # Reload saved settings
    MySettings.ReloadSettings(jsonData)

    # End of ReloadSettings
    return

global files
files = ('30day_cheer_amount.txt','30day_donation_amount.txt','30day_top_cheerer.txt','30day_top_cheerers.txt','30day_top_cheers.txt','30day_top_donations.txt','30day_top_donator.txt','30day_top_donators.txt','all_time_top_cheerer.txt','all_time_top_cheerers.txt','all_time_top_cheers.txt','all_time_top_donations.txt','all_time_top_donator.txt','all_time_top_donators.txt','AmountOfFollowers.txt','AmountOfGameWispSub.txt','AmountOfHosts.txt','AmountOfRaids.txt','AmountOfSubs.txt','CurrentlyPlaying.txt','CurrentSong.txt','Deaths.txt','donation_goal.txt','ExtraLife.txt','ExtraLife_Donators.txt','ExtraLife_Recent_Donator.txt','ExtraLife_Team.txt','Followers.txt','GameWispSubs.txt','Hosts.txt','monthly_cheer_amount.txt','monthly_donation_amount.txt','monthly_top_cheerer.txt','monthly_top_cheerers.txt','monthly_top_cheers.txt','monthly_top_donations.txt','monthly_top_donator.txt','monthly_top_donators.txt','most_recent_cheerer.txt','most_recent_donator.txt','most_recent_follower.txt','most_recent_resubscriber.txt','most_recent_subscriber.txt','RecentFollower.txt','RecentRaider.txt','RecentSub.txt','RequestedBy.txt','session_cheerers.txt','session_cheer_amount.txt','session_donation_amount.txt','session_donators.txt','session_followers.txt','session_follower_count.txt','session_most_recent_cheerer.txt','session_most_recent_donator.txt','session_most_recent_follower.txt','session_most_recent_resubscriber.txt','session_most_recent_subscriber.txt','session_subscribers.txt','session_subscriber_count.txt','session_top_cheerer.txt','session_top_cheerers.txt','session_top_cheers.txt','session_top_donations.txt','session_top_donator.txt','session_top_donators.txt','SpotifySong.txt','Subs.txt','total_cheer_amount.txt','total_donation_amount.txt','total_follower_count.txt','total_subscriber_count.txt','total_subscriber_score.txt','weekly_cheer_amount.txt','weekly_donation_amount.txt','weekly_top_cheerer.txt','weekly_top_cheerers.txt','weekly_top_cheers.txt','weekly_top_donations.txt','weekly_top_donator.txt','weekly_top_donators.txt')


global path
path = path = os.path.dirname(os.path.abspath(__file__))


def Execute(data):

    return

def switch():
    selected = literal_eval(MySettings.selectedfiles)
    selectedtitle = literal_eval(MySettings.selectedfilestitle)
    twitchfile = files[selected[n]]
    twitchf = open("Services/Twitch/Files/{}".format(twitchfile),"r+")
    filetext = twitchf.read()
    twitchf.close()
    f = open("{}/Overlayfile.txt".format(path),"w+")
    overlay = selectedtitle[n] + ": " + filetext
    f.write(overlay)
    f.close()

    if n == len(selected)-1:
        global n
        n = 0
    else:
        global n
        n = n + 1

    return time.time()
    
def Tick():
    if MySettings.OnlyLive:

        #set run permission
        startCheck = Parent.IsLive()
        
    else: #set run permission
        startCheck = True
        
    if startCheck and time.time() > t + MySettings.Delay:
        
        global t
        t = switch()
    return

def UpdateSettings():
    with open(m_ConfigFile) as ConfigFile:
        MySettings.__dict__ = json.load(ConfigFile)
    return
