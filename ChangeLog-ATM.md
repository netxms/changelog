# 4.2

-   Improved transaction emulation tool

# 4.1

-   Implemented configurable display modes for cash details tab
-   Implemented configurable time range for cash history in cash details tab
-   Implemented "network" downtime tracking
-   Fixed nxdbmgr crash during check
-   Implemented video search result export to PDF
-   Use node name as terminal ID in video surveillance module if custom attribute is not set
-   Fixed bug in license counting in video surveillance module
-   Do not attempt to schedule video surveillance module file download from ATM if it's disconnected
-   Improved logging in video surveillance subagent
-   Improved poller messages when ATM component table cannot be read

# 4.0

-   Fixed minor shutdown bugs in vendor subagents
-   Added caching of CDM and CIM physical cash unit positions
-   Improved logging in XFS subagent
-   Implemented comm log parsing for GRG ATMs
-   Added simple command line tool for DDC message decoding
-   Added SIU diagnostic to xfsdiag
-   XFS NCR profile can read service names from registry

# 3.10

-   Improved logging in video capture subagent
-   Implemented option to keep last known ATM state
-   Added metrics for cheque depositor status poll
-   Added support for biometric devices in XFS (device class `BIO`)
-   Fixed bug in transaction journal writing on NCR ATMs
-   Added zero counters bug detection in XFS subagent

# 3.9

-   Improved NCR journal parsing
-   Fixed server crash when executing journal sync reset on unconnected ATM
-   ATM journal search UI cleanup and minor fixes
-   Added limit on number of matches for EJ search
-   Implemented regex and simple journal search modes
-   Use background writer for ATM cash history table and improve performance
-   Fixed deadlock on server shutdown
-   Fixed ATM state being reset to UNKNOWN when XFS subagent is not available
-   Fixed memory leak in server module
-   Fixed component problem generation for cash units
-   Improved metrics for camera status
-   Severity for component problems based on device status codes can be redefined in server configuration
-   Added support for archived journal files synchronization
-   Video surveillance subagent will load even if all cameras are not working
-   Added cash-in related events for video surveillance module

# 3.8

-   Correct detection of `SUSPEND` state on Wincor ATMs
-   Fifth cassette is disabled by default in NCR XFS profile
-   Improved XFS service detection on NCR ATMs
-   Improved diagnostic
-   Fixed default communication log location on GRG Banking ATMs
-   Added support for hardware error decoding on GRG Banking ATMs
-   Added support for GRG Banking ATMs
-   XFS subagent caches physical cash unit positions to counteract buggy XFS implementations that may return empty value for physical cash unit position from time to time
-   Added configurable number of polls during which cash unit position should be in MISSING state before generating component problem
-   Fixed resource leak
-   Fixed bug in installer that prevented external XFS subagent registration for autostart
-   Improved support for ATMs with two cash dispensers
-   Added atm component retention time
-   Added journal sync option to load main journal file location form agent config file
-   Fixed journal tag selection when journal with non default tag disappears
-   Added clear journal date command
-   Fixed minor shutdown bugs in vendor subagents
-   Updated transaction codes to one character
-   Improved journal parsing on NCR ATMs
-   Improved EJ parser for NCR ATMs
-   Fixed incorrect txn type for deposit
-   Fixed SQL error when updating card number in video capture event log
-   Include event_id into ordering when search for video capture events
-   Added "Save as" action to media view
-   Fixed bug with IST node change

# 3.7

-   Added support for new Diebold Nixdorf ATMs
-   Improved Wincor XFS profile

# 3.6

-   Added XFS profile `DIEBOLD-NIXDORF`

# 3.5

-   cdmType and direction attributes of cash units exposed to NXSL

# 3.2

-   Fixed issues with operator initiated agent restart
-   Added XFS subagent configuration option FixCurrentCount that enables calculated current counter for cash units (based on initial and dispensed counters)
-   Fixed bugs in Diebold message trace parser
-   Fixed bug in Wincor hardware inventory parser
-   Agent local database problems logged with higher severity level
-   Write EmPower bridge diagnostic output to agent log
-   Fixed bug in EmPower bridge automatic restart
-   Fixed agent deadlock on startup on Diebold ATMs
-   Windows XP support dropped
-   DDC message decoder for Diebold ATMs
-   Option to turn on combined journal (message decode + EDC) on Diebold ATMs
-   Switched to pcre (from libtre) as regular expression matching engine
-   Added "rescan" option in log parser definitions
-   Log parsers can be configured to add extra parameters to generated events
-   Additional SSL trace output can be enabled in agent configuration file
-   Added support for reading WMI query result as list or table
-   User-defined additional journals for synchronization with server
-   Automatic rotation of decoded message trace file in Diebold subagents
-   Added hook scripts `Hook::AcceptCassetteForPoll` and `Hook::AcceptCashUnitForPoll`
-   Currency and denomination propagated to PCUs from owning LCUs in model

# 3.1

-   Added message trace file parser in Diebold subagent
-   Added custom parser thread for message trace file, changed default file location and initial decoding for solicited status messages
-   Diebold and Empower subagents report additional journal files if message decoder turned on
-   Implemented multi journal support and journal tags
-   Implemented `JournalSync.Tags` list
-   General improvements in journal sync
-   Fixed default Diebold message trace file name

# 3.0

-   Fixed sensor state parsing on Diebold
-   Fixed possible server crash if IST node property in ATM is incorrectly set
-   Fixed lock issues in journal sync subagent
-   XFSDiag updated for correct handling of IPM device class
-   Fixed invalid thread access in NXVS client
-   Improved Wincor journal parsing
-   Check for potential NULL pointer in physical cash unit position name
-   Fixed bug in Wincor journal parsing
-   Added logging of unknown terminal status codes in IBA subagent
-   Additional status codes for IBA kiosks
-   Fixed incorrect access to pcre capture groups
-   Fixed perspective layouts
-   Custom code names can be set in agent config for IBA kiosks

# 2.1.9-6

-   Updated device status codes for IBA kiosks

# 2.1.9-5

-   Updated device status codes for IBA kiosks

# 2.1.9-4

-   Fixed Windows XP compatibility issues

# 2.1.9-2

-   Additional status codes for IBA kiosks

# 2.1.9-1

-   Added support for Diebold Agilis on 64-bit systems
-   Improved Wincor journal parsing
-   Fixed agent crash caused by incorrect data provided by XFS dispenser service

# 2.1.9

-   Improved screenshot performance
-   Fixed bug in journal synchronization

# 2.1.8-3

-   Fixed bug in sensor state parsing on Diebold ATMs

# 2.1.8-1

-   Fixed bug related to second dispenser support

# 2.1.8

-   Implemented agent parameters for hardware inventory collection

# 2.1.7-2

-   Fixed agent crash when accessing XFS

# 2.1.7-1

-   Fixed bug in file manager subagent

# 2.1.7

-   Added support for second card reader, dispenser, and cash acceptor
-   Improved device autodetection on NCR ATMs

# 2.1.6

-   Fixed log parser bug
-   Fixed agent crash under certain conditions
-   Fixed bug in File.Size parameter handling
-   Installer restarts session agents and external sub-agents during upgrade

# 2.1.4-2

-   Added XFS subagent table `XFS.CashIn.CashUnits`
-   Improved NCR M-status mapping

# 2.1.3-52

-   Correct handling of broken pre-allocated EJ files on NCR ATMs

# 2.1.3-50

-   Improved XFS device autodetection on Diebold ATMs
-   Correctly detect "out of suspend mode" condition on NCR ATMs

# 2.1.3-48

-   Journal synchronization uses same exclusion schedule as vendor sub-agent

# 2.1.3-47

-   Fixed bug in socket error reporting

# 2.1.3-46

-   Faster initialization of journal synchronization subagent

# 2.1.3-45

-   Additional diagnostic output on Wincor ATMs

# 2.1.3-44

-   Fixed bug in EJ rotation detection
-   Agent installer set correct permissions on log directory

# 2.1.3-41

-   Fixed agent crash on shutdown or restart
-   Fixed incorrect handling of long lines in external lists and tables
-   Fixed incorrect handling of long parameters

# 2.1.3-35

-   Added support for agent actions defined by external subagents
-   EJ location for Hyosung ATM can be set in agent’s configuration file

# 2.1.3-32

-   Added parameter XFS.CashIn.DevicePosition
-   Added parameter XFS.Dispenser.DevicePosition
-   Fixed bug in agent upgrade procedure

# 2.1.3-27

-   Fixed bug in EJ synchronization
-   Fixed agent crash if local database cannot be open

# 2.1.3-23

-   Added support for unique agent identifiers

# 2.1.3-15

-   Fixed agent crash if EJ synchronization sub-agent loaded before vendor sub-agent

# 2.1.3-14

-   VSS mode is off by default in Diebold sub-agent
-   Improved XFS device detection on Diebold

# 2.1.3-13

-   Fixed bug in ATM state detection for Diebold Agilis Empower
-   Added actions for journal and receipt printer device reset

# 2.1.3-12

-   Fixed slow change detection by Diebold EJ monitor

# 2.1.3-10

-   Implemented application state monitoring for Diebold Agilis versions prior 2.4
-   Improved Diebold EJ monitoring
-   Diebold MSD codes `AL01:3F:**:**` handled locally by agent without sending hardware error events to server

# 2.1.3-3

-   Exclusion time ranges for EJ monitoring implemented in all vendor sub-agents
-   Agent retries bound tunnel handshake before fallback to unbound mode

# 2.1.3-1

-   Improved automatic device profile selection
-   File owner information provided by file manager sub-agent

# 2.1.3

-   Fixed bug in Diebold EJ synchronization

# 2.1.2-129

-   Diebold sub-agent save last known ATM application state across restarts

# 2.1.2-127

-   Fixed bug in Agilis EmPower subagent
-   Fixed bug in physical cash unit positions override

# 2.1.2-124

-   Agilis EmPower subagent
-   Detected physical cash unit positions override from configuration file
-   Fixed bug in tunnel definition parsing
-   Fixed memory leak in agent

# 2.1.2-115

-   Added zero filled blocks detection within journal files
-   Fixed agent crash on NCR

# 2.1.2-111

-   Updated dispenser service names for automatic detection on NCR
-   Fixed "Unknown event 212 received" errors on Wincor
-   Fixed excessive XFS session creation if persistent sessions are off
-   Fixed agent crash on Wincor

# 2.1.2-108

-   Added option to enable Microsoft Volume Shadow Copy for reading NCR EJ file

# 2.1.2-95

-   Configurable exclusion intervals for NCR electronic journal monitoring

# 2.1.2-79

-   Configurable polling interval for IrisGuard sub-agent
-   Minor bug fixes in JMX sub-agent

# 2.1.2-59

-   Added option to read log files using Microsoft Volume Shadow Copy to avoid interferences with other applications accessing same log files

# 2.1.1-100

-   Added wrapper for Diebold EJ archiver that temporary suspends EJ monitoring by PM agent to allow EJ rotation

# 2.1.1-86

-   Fixed UDBD log parsing issues on some Diebold Agilis versions
-   Added configuration option for interval between tunnel keepalive packets
-   Fully qualified domain name sent as part of agent information during tunnel setup
-   All binaries are digitally signed

# 2.1.1-5

-   Additional debug information logged

# 2.1-94

-   Improved XFS service automatic selection on Diebold
-   Additional debug information logged on agent startup

# 2.1-89

-   Suspend UDBD log monitoring on Diebold when log zipper error detected
-   XFS trace level can be configured
-   Correctly handle "suspend mode" message on NCR

# 2.1-79

-   Improved XFS service automatic selection

# 2.1-74

-   Automatic device profile selection
-   Automatic XFS service selection

# 2.1-72

-   Improved ATM state detection on Diebold ATMs
-   Use NDC unsolicited status messages to get sensor states on NCR
-   Fixed agent crash when reading table XFS.LogicalServices

# 2.1-RC1-103

-   Fixed agent crash on startup

# 2.1-RC1-95

-   Fixed electronic journal synchronization issues on Diebold
-   Fixed hardware error detection bug on Diebold

# 2.1-RC1-53

-   Default session idle timeout increased to avoid issues with file tracking

# 2.1-RC1-42

-   Added Hyosung vendor subagent
-   Added Hyosung XFS device profiles

# 2.1-RC1-37

-   Improved agent tunnel support
-   Fixed network interface name resolution bug on Windows
-   Fixed log monitoring subagent crash

# 2.1-M3-124

-   Separate template file for empty location list case in nearest ATM location subagent

# 2.1-M3-87

-   Implemented external tables in agent
-   Improved channel closure detection in agent tunnels
-   Fixed agent restart issue
-   Agent generates full crash dumps by default
-   Added configuration option for overriding cash units currency and denomination reported by XFS layer

# 2.1-M3-46

-   Added configuration option FixRejectCount
-   XFS subagent generates events for item presented and items taken
-   xfsdiag always skip service DBD_EPPCH
-   Added unsolicited dispense detection
-   Fixed card reader event handler
-   Cheque depositor included into XFS inventory table
-   Additional XFS parameters for dispenser (intermediate stacker state and transport status)
-   Alternate journal file location for Diebold Agilis EmPower
-   Additional parameters in XFS subagent for cash-in devices
-   IrisGuard monitoring subagent added
-   Nearest ATM location subagent added
-   Fixed agent crash on Windows if agent tunnels are used
-   Changed agent tunnel binding, implemented tunnel unbind
-   Fixed agent crash after tunnel disconnect
-   Fixed potential race condition during agent tunnel closure

# 2.1-M3

-   Added configuration option for IPM service in XFS subagent
-   Improved Wincor inventory
-   Connection from agent to server implemented using tunnel
-   Host names used in agent tunnel definition resolved at each connect

# 2.1-M2

-   Added option to extracts current NCR cash counters from EJ
-   Fixed NCR log parser
-   Added banknote jam detection in IBA kiosk subagent
-   Added XFS subagent parameter InitProcess
-   DIEBOLD profile use WaitForAmiInit.exe to determine correct start time for XFS
-   Fix for detecting journal printer in Wincor inventory
-   Added table `XFS.LogicalServices`
-   XFS persistent sessions option is turred on by default
-   Added support for depositor devices in XFS subagent
-   UDBD log parser uses link to current file name
-   Changed parsing rules for Diebold for application state tracking
-   Added `ATM.Vendor`, `ATM.ModelName`, `ATM.State` parameters for Diebold and Wincor subagents
-   Added support for journal files pre-filled with zeroes
-   Improved Diebold log parsers
-   Updated NCR journal parser
-   Added support for XFS IPM device class
-   Fixed IBA kiosk status detection
-   Wincor NP06 journal printer support added
-   Default pinpad device in Diebiold profile changed to DBD_EPP7
-   Added support for monitoring preallocated log files
-   Agent registry upgrade fixed
-   Fixed file forced close on Windows upgrade run
-   Command executor class implemented for Windows
-   Fixed command line length limit in Process.CountEx on Windows
-   Alias support in config class
-   Agent core configuration section can be changed with -G command line option
-   Implicit external subagent registration using `EXT:*` sections in configuration file
-   Agent external section can generate wit -Z command line option
-   Fixed modification time for uploaded files.
-   Agent do not attempt to configure external subagent listeners when in external subagent loader mode
-   Implemented message compression in NXCP. Compression is used on agent connections by default.
-   Added DEFLATE stream compression method
-   Java API can receive compressed files from agents using LZ4

# 2.1-M1

-   Added action to reset retained cards counter on card reader
-   Added subagent for IBA kiosk monitoring
-   Ignore door states on NCR ATMs
-   Fixed session agent work on Windows XP with disabled terminal services
-   Fixed bug in agent local database structure check
-   `System.Memory.*.*Perc` changed to return float fixes
-   Agent version changed to return build tag as version
-   Default number of agent sessions changed to 1024 if proxy is enabled
-   Added progress bar to download actions
-   Fixed directory download in webui
-   Added show file size option for directories
-   File manager uses multiple messages to send folder listings to avoid timeouts on slow links
-   Added System.CPU.Interrupts and System.CPU.ContextSwitches agent parameters for Windows, Linux and FreeBSD subagents
-   Fixed bug in reading encrypted agent secret from config
-   Interrupt and context switch parameters correctly implemented on Windows
-   Added read-only root folder support to filemgr subagent

# 2.1-M0

-   Fixed errors with partial journal file sync
-   Fixed bug with not comming journal file date to agent
-   Added `XFS.CardReader.ChipProtocols`, `XFS.CardReader.ReadTracks`, `XFS.CardReader.Type`, `XFS.CardReader.WriteTracks`, `XFS.Dispenser.CashUnitPositions` parameters
-   Added common function to send transaction events
-   NCR subagent send events for video subagent
-   Fixes in NCR journal parser
-   Fixed DIEBOLD profile in XFS subagent
-   Fixed memory leaks in core agent session
-   Added new policy type for log parser policies
-   Changed default logwatch reading folder
-   Fixed possible NULL pointer in agent offline data collection
-   Registry configuration moved into agent database.
-   Added option to define while node connection if server id should be sent while connection.
-   Fixed data reconciliation problems when server is not master server
-   Increased timeout on bulk data send
-   Added repeat count to matcher for log parser
-   Added parameters and events in case if agent failed to open log or database
-   Add logging for long running queries
-   Added functionality to send \<\<ERROR\>\> status for cashed dci values
-   Added configuration for agent data reconciliation block size, timeout and data collectors pool
-   Fixed agent crash when executing action with output
-   Added agent parameters `System.CPU.CurrentUsage` and `System.CPU.CurrentUsage(*)`
-   Removed 4GB log size limit in log rotation configuration
-   Added K/M/G/T suffixes support when setting log size in config
-   Fixed incorrect interface list report on Windows before NT 6.0
-   Additional agent metrics for self-monitoring (SNMP proxy, external parameters and syslog proxy stats)
-   New agent metrics `Agent.Proxy.ActiveSessions`, `Agent.Proxy.ConnectionRequests`, `Agent.Proxy.IsEnabled`

# 2.0.3

-   Added XFS.SIU.HardwareReset parameter
-   Added XFS.Inventory parameter
-   Added agent local database usage option to subagents.
-   Added new agent parameter handler return code: `RC_NO_SUCH_INSTANCE`

# 2.0.2

-   Implemented external XFS subagent start command
-   XFS device profiles added
-   XFS diagnostic tool added
-   Transaction detection for video surveillance based on XFS message hook
-   Journal synchronization subagent added
