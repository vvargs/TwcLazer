# CLIHELPER.py
# EF1500
# Misc things for the CLI

BANNER = """
  _______           _                        
 |__   __|         | |                       
    | |_      _____| |     __ _ _______ _ __ 
    | \ \ /\ / / __| |    / _` |_  / _ \ '__|
    | |\ V  V / (__| |___| (_| |/ /  __/ |   
    |_| \_/\_/ \___|______\__,_/___\___|_|   
    
    Record Twitcast streams!
    
    Developed By EF1500 | Holoarchivists
    https://github.com/ef1500 | https://github.com/HoloArchivists

"""

OPTIONS = """
Required Arguments
  -u, --username              Channel to download the stream from
  
Optional arguments
  -ff, --fileformat FORMAT    filename format for the stream
  -p, --path PATH             Path to download the stream to
  -q, --quality [low, best, worst]

Flags
  -nW, --noWarn               Don't display lagspike warning when downloading high bitrate streams
  -nR, --noRetry              Don't try to reconnect if the websocket connection drops
  -pC, --printChat            Print the chat to the terminal
  -wC, --withChat             Export the stream's chat to a file
  
Misc (Use if --withChat is true. Completely Optional.)
  -cF, --chatFormat           Override The chat's default formatting
  -gF, --giftFormat           Override The gift's default formatting
  """

HIGH_QUAL_WARNING = f"""
Downloading at the highest possible source may cause visible lagspikes in the video file. Please ensure that your connection can accomodate high-bitrate streaming. To disable this warning, use the --nowarn argument (-nW) or select a lower bitrate source.
You've Been Warned!
"""

FILENAME_FORMATTING_INFO = """
Filename Formatting Options

By Default, the output file is formatted like so:
-ff "%%Un-[%%Dy-%%Dm-%%Dd]-%%Id-%%Tn"
<username>-[<year>_<month>_<day>]-<id>-<tn>

However, you may override this if you so choose. The following is a list of formatting options you may use:

  %Id - Movie ID        %Tn - Timename
  %Tt - Title           %Hs - Hashtag (If Any)
  %Tl - Telop           %Cn - Category Name
  %Ci - Category ID     %Pm - Pin Message (If any)
  %Dy - Year            %Dm - Month
  %Dd - Day             %Un - Username
"""

CHAT_FORMATTING_INFO = f"""
Chat Formatting Options

By default, the twitcast chat is recorded in the output file like so:

  Comments:
  <author_screenName>: <message> | <createdAt>

  Gifts:
  <item_name> | <message> | <sender_screenName>

However, you may override this if you so choose. the following is a list of percent arguments to format the chat however you wish:

  Comments:
  %Ag - Author Grade          %Ai - Author ID
  %An - Author Name           %Ap - Author Profile Image
  %As - Author Screen Name    %Ca - Created At
  %Ei - Event ID              %Mg - Message
  %Nc - Comment Number        %Et - Event Type
  
  Gifts:
  %Ca - Created At            %Ei - Event ID
  %Id - Item Detail Image     %Ie - Item Effect Command
  %Ii - Item Image            %In - Item Name
  %Is - ItemSowsSenderInfo    %Mg - Message
  %Sg - Sender Grade          %Si - Sender ID
  %Sn - Sender Name           %Sp - Sender Profile Image
  %Ss - Sender Screen Name    %Et - Event Type
"""

