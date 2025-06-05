# 5.3.0

## Fixed issues

-   NX-2710 (Traffic graphs for interface on overview)
-   NX-2774 (Allow to specify column for instance-name for instance discovery from a table)

# 5.2.3

-   Default timeout for service checks via netsvc subagent set to 1 second
-   Fixed alarm severity text for Grafana API
-   Forced plain text web service requests are cached separately

## Fixed issues

-   NX-2766 (Template macros are not expanded in instance data filed in DCIs Instance discovery)
-   NX-2768 (Changes to VNC properties not logged to audit log)
-   NX-2770 (Object query result view pinning does not work)
-   NX-2777 (No favicon in new Web UI)
-   NX-2781 (Send all parameters of default email notification channel to reporting server)
-   \#140 (SQL errors after converting database to TimescaleDB)

# 5.2.2

-   Fixed insert into table "notification\_log" for TimescaleDB
-   Improved client performance, by disabling alarm refresh if tab is not active
-   Fixed missing DCI on network map links when new DCI's are added on alreay opened map
-   Added job progress indication within views
-   Fixed NXSL get web service document functions 
-   Added Grafana Infinity plugin web API endpoints

## Fixed issues

-   NX-2733 (Do not show zone column in discovery targets if zoning is off)
-   NX-2742 (Add NXSL node object method for enabling/disabling SM-CLP polling)
-   NX-2751 (Delete scheduled tasks on node deletion)
-   NX-2752 (Add ICMP response time jitter internal DCI for ICMP response statistic collection)
-   NX-2754 (Separate error code for situation when TCP proxy is not enabled in agent config)
-   NX-2755 (NXSL Interface utilization values returned as int, without decimal point)
-   NX-2764 (Add PostgreSQL 17 support in monitoring subagent (pgi\_stat\_checkpointer))
-   NX-2765 (Increase command length in package manager)

# 5.2.1

-   NXSL function PostEvent accepts any event source object
-   Added option to set in maintenance all objects under Wireless Domain
-   InfluxDB and Clickhouse drivers can be configured to use custom attributes of DCI's template
-   Fixed bug in driver for Cambium CnPilot devices
-   Fixed database connection leak during package deployment

## Fixed issues

-   NX-2600 (Threshold for missing table instances never deactivated)
-   NX-2723 (Add Web API endpoint for object maintenance)
-   NX-2729 (Display hints for hook scripts in script library)
-   NX-2734 (When exporting event processing policy rule, automatically add referenced actions)
-   NX-2735 (Cannot delete user from object access control list)
-   NX-2740 (Modbus DCI becomes unsupported when proxy is unreachable)

# 5.2.0

-   User-defined tags on data collection items
-   Network maps can be shown in object's context in a same way as dashboards
-   Improved package deployment
-   NXSL math functions Min, Max, Average, MeanAbsoluteDeviation, and StandardDeviation accepts variadic arguments
-   New NXSL function Math::Sum
-   New NXSL array method indexOf
-   Simplified loops over numeric ranges in NXSL using class "Range"
-   Unicode escape sequences in NXSL string literals
-   Script entry point can be given for script DCI
-   Dot can be used as script entry point separator instead of slash
-   Fan-out diver for ClickHouse
-   Fixed direction and arrow size for Network Map links
-   Reworked Network Map link label location calculation for multi link connection
-   Configurable values for RADIUS authentication request attributes Service-Type and NAS-Identifier
-   SM-CLP protocol support reworked and switched to SSH as a transport
-   Updated set of standard templates
-   Fixed incorrect data and occasional server crashes in network discovery filter script

## Fixed issues

-   NX-74 (New node options - "expected capabilities")
-   NX-1301 (Automatic traffic DCI linking to interface)
-   NX-2654 (Add agent running config object tool via db migration script)
-   NX-1302 ("Traffic" overlay for maps)
-   NX-2568 (Add case-insensitive versions of threshold operations "like" and "not like")
-   NX-2624 (Review SMCLP data source and switch it to SSH)
-   NX-2662 (Show map in tab on object)
-   NX-2667 (Context dashboard should be able to pick DCIs from child objects by specific DCI tag)
-   NX-2668 (Change all server configuration variables related to polling intervals to be modifiable without server restart)
-   NX-2680 (Add NXSL function Math::Sum)
-   NX-2681 (Add array method "indexOf")
-   NX-2686 (Put DCI to ERROR state if it's transformation script has compilation error)
-   NX-2689 (Add event ID (if available) to notification log)
-   NX-2694 (Add "front side only" property to rack objects)
-   NX-2695 (Fit rack image into the view both vertically and horizontally)
-   NX-2703 (Support Unicode escape sequences in NXSL string literals)
-   NX-2707 (Add method "createSensor" to container object classes in NXSL)
-   NX-2716 (Agent metric that reports server's access level to that agent)
-   NX-2721 (Add $ipAddress variable of class InetAddress in Hook::AcceptNewNode script)
-   NX-2725 (NetXMS does not fallback to secondary proxy nodes)
-   NX-2728 (Update interface configuration when a node with an agent is rebooted)
-   NX-2732 (Server attempts TCP ping for nodes behind proxy)

# 5.1.5

-   VNC detection during configuration poll can be disabled
-   System access rights included into user ACL report
-   Fixed bugs in NXSL script conversion to V5 format
-   Fixed file handle leak in SSH subagent
-   Fixed bug in configuration export

## Fixed issues

-   NX-2712 (Scripted thresholds triggers activation event repeatedly)
-   NX-2714 (Status of interface not propagated to circuit)
-   NX-2726 (Web API call causes server crash)

# 5.1.4

-   Agent uses Windows Installer API instead of launching msiexec.exe for installing .msi and .msp packages
-   New Windows agent metric System.IsRestartPending
-   Improved server performance when launching multiple external actions
-   MIB Explorer added to "Tools" perspective
-   Fixed incorrect parsing of 32 bit agent installer names when adding package to package manager
-   Changed IPv4 address parser - now it only accepts canonical form (4 decimal numbers separated by dots)
-   Correct handling of network mask /31 on peer-to-peer interfaces
-   Node sub objects like Interface will not be shown on Infrastructure perspective if they do not have parent shown in the same tree
-   Added dBm and rpm DCI units to no multipliers list
-   Fixed tab priority for multiple built in views
-   Fixed problem when newly added DCI were not shown on Network Map (links, DCI containers)
-   Fixed broken autobind during node configuration poll

## Fixed issues

-   NX-2645 (Remember perspective splitter position)
-   NX-2684 (Remove hardcoded license id from the nxlicmgr)
-   NX-2690 (Migration from Timescale to regular Postgres fails on win\_event\_log table)
-   NX-2696 (View options in Data Collection does not show actual state of Use Multipliers checkbox)
-   NX-2699 (Show value of os.name in nxmc's About dialog)
-   NX-2701 (Automatic DB unlock fails because GetLocalIpAddr() may return different address)
-   NX-2705 (NXSL split string with trim option)
-   NX-2711 (scheduled\_tasks column is out of range for type integer)

# 5.1.3

-   Fixed critical bug in SNMP trap receiver
-   Server checks for other possible SNMP credentials during configuration poll if node marked as SNMP unreachable
-   Image attributes in Markdown viewer
-   Fixed bug in counter reset detection

## Fixed issues

-   NX-2685 (nxshell asks for password while using properties file)

# 5.1.2

-   Server performance and memory usage optimization when polling multiple SNMP devices
-   Limit routing table scans during SNMP device configuration poll
-   Optimized memory usage in InfluxDB driver
-   Server startup time improved
-   Added server configuration option "Client.MinVersion"
-   Improved Markdown viewer
-   InfluxDB driver options for validation and correction of DCI values being sent

## Fixed issues

-   NX-2635 (Predefined graphs perspective not working in web UI)
-   NX-2640 (Add more detailed stats on pollers to debug console)
-   NX-2647 (On node deletion interfaces under circuit objects are not deleted)
-   NX-2649 (Issues with "move to another container" context menu on interfaces)
-   NX-2650 (Add new hotkey in "execute server script" for "clear output+run script")
-   NX-2653 (Can not pin Data Collection tab which is in edit mode)
-   NX-2657 (IllegalStateException in nxmc log)
-   NX-2660 (Add method to read little-endian 4 byte float value from ByteStream)
-   NX-2661 (Issues with loading image of DCI image element of map)
-   NX-2669 (Add internal table with node's interfaces)
-   NX-2672 (Kiosk mode issues)
-   NX-2673 (Table DCI column querying not working, if metric has no leading dot)
-   NX-2675 (Add NXSL methods to handle markdown comments correctly)
-   NX-2676 (Issues with comment tab creation and modification on object)

# 5.1.1

-   Improved server performance
-   Improved wireless controller bridge for HFCL
-   MS SQL database driver no longer requires SQL Server Native Client (can use SQL Server ODBC driver v13, v17, or v18 instead)
-   Added driver for Huawei LAN switches
-   Updated driver for Dell switches
-   Updated driver for Qtech switches
-   Added internal metrics Server.ObjectCount.AccessPoints and Server.ObjectCount.Interfaces
-   New NXSL functions Math::Average, Math::MeanAbsoluteDeviation, and Math::StandardDeviation
-   nxdbmgr can do in-place conversion from standard PostgreSQL schema to TimescaleDB
-   Fixed server crash on receiving SNMP trap
-   Fixed bug in database initialization script
-   Fixed task scheduler performance issues
-   Removed "Delete" button form object upper bar

## Fixed issues

-   NX-2587 (No line numbering in DCI instance discovery filter script)
-   NX-2629 (Can not clone an object tool)
-   NX-2630 (Not all the Markdowns are functioning)
-   NX-2631 (In-place migration from standard PostgreSQL to TimescaleDB)
-   NX-2632 (Inconsistency in asset management schema enum field definition)
-   NX-2633 (Text not fully displayed in button)
-   NX-2637 (Circuit class functionality)
-   NX-2639 (Incorrect log message for Mattermost driver)
-   NX-2642 (Add alarm\_state\_changes and certificate\_action\_log tables to nxdbmgr -Z all)

# 5.1.0

-   New automatic map type "hybrid topology"
-   New object class "Circuit"
-   Only read access is needed for dashboard context object for scripting dashboard elements
-   Reading of FDB moved to network device drivers to allow better handling of devices not following standards
-   Peer information on interfaces can be set and cleared manually
-   Added down since nxsl parameter to access point
-   Vlans view merged in to the Ports view
-   Added option to show physical links on L2 ad-hoc map
-   L2 predefined map will not cache results, only ad-hock map results are cached
-   More accurate ad-hoc IP topology maps
-   Unreachable node will be tested for all protocols in each configuration poll
-   Use inetCidrRouteTable, ipCidrRouteTable, and ipForwardTable in addition to ipRouteTable to get routing information via SNMP
-   EtherNet/IP added as DCI data source
-   Improved web UI login pages
-   Separate "Comments" view for objects
-   Templates perspective can be configured to show nodes under assigned templates
-   New attributes in NXSL class "InetAddress" ("isSubnetBase", "isSubnetBroadcast", "subnet")
-   New NXSL function "CalculateDowntime"
-   New method "calculateDowntime" in NXSL class "NetObj"
-   Other UI usability improvements
-   Fixed session agent compatibility issues on Windows 11
-   Optional DCI event "all thresholds deactivated"
-   DCI data type after transformation can be configured separately from input data type
-   New scheduled task handler Agent.ExecuteCommand
-   Improved network map multi link spacing
-   New action System.TerminateUserSession in Windows agent
-   Fixed network map object label scaling on zoom in/out

## Fixed issues

-   NX-253 (Configurable label for Y axis on line charts)
-   NX-834 (DCI Table scroll position in dashboard is reset during refresh)
-   NX-968 (Remove Peer from unmanaged interface)
-   NX-1118 (Add "hide link labels" option for network map dashboard elements)
-   NX-1200 (New object group - Circuits)
-   NX-1288 (Fix selection colors in syslog monitor)
-   NX-1414 (Support for ipCidrRouteTable)
-   NX-1465 (When MIB browser opened, unfold tree and select longest match of device's SNMP object ID)
-   NX-1617 (Show comments window only if comment present)
-   NX-1958 (Support custom font for Label in Dashboard)
-   NX-1973 (Add ability to manually specify a peer for an interface)
-   NX-2034 (Use RENAME COLUMN on SQLite newer than 3.25.0)
-   NX-2353 (Add hotkey to start search in "Search IP address" view)
-   NX-2371 (Separate data types for raw and transformed DCI values)
-   NX-2439 (Implement agent table System.InstalledProducts for ArchLinux)
-   NX-2458 (Add option to nest context dashboard in dashboard)
-   NX-2461 (Smart algorithm for processing counter32/64 roll-over)
-   NX-2488 (Use caching when using web service requests in NXSL)
-   NX-2512 (Not able to import columns for table DCI with origin=script)
-   NX-2517 (Linux agent can crash if some CPUs are disabled)
-   NX-2528 (Markdown Support in Object Comment Sections)
-   NX-2531 (Ability to disable server actions in EPP)
-   NX-2533 (NXSL global variable that contains object tool input field values)
-   NX-2535 (Replace drop down with radio buttons in EPP rule Downtime Control)
-   NX-2538 (Add ability to use IPv4 style netmask in network discovery target properties)
-   NX-2540 (Add $map object for use in map filter script)
-   NX-2541 (All EPP actions should be executed asynchronously)
-   NX-2542 (Add syslog metadata to generated events)
-   NX-2544 (New agent metrics for counting online and offline CPUs)
-   NX-2545 (Exporting a template with big file in a policy causes nxmc to close)
-   NX-2552 (Exception in desktop UI)
-   NX-2562 (Add pollingScheduleType attribute to DCI object)
-   NX-2566 (List of packages is not read correctly on linux systems where alien is installed)
-   NX-2574 (nxevent and nxaevent utilities do not support named event parameters)
-   NX-2580 (Configurable default time range for ad-hoc line charts)
-   NX-2584 (Change network map edit mode to network map lock mode)
-   NX-2586 (Export all to CSV not working in data collection configuration view)
-   NX-2593 (Add option to use properties file for NXShell)
-   NX-2596 (Unable to create zone via Web API)
-   NX-2597 (Log PATH and LD\_LIBRARY\_PATH values on agent startup)
-   NX-2598 (Generate event when all thresholds of a DCI are rearmed)
-   NX-2602 (Audit log not available in context menu for some objects)
-   NX-2606 (no id ranges possible in Configuration-\>Windows event log parser)
-   NX-2613 (Show gray "Any" in "source objects" list, if it's empty)
-   NX-2617 (Show info in EPP rule that "Accept correlated events" is checked)
-   NX-2618 (Server crash when file upload task configuration is invalid)
-   NX-2619 (SQL insert into nodes failed)
-   NX-2620 (System.ProcessList truncates the full process name or path)
-   NX-2621 (Add "Line chart" item in context menu of map link)

# 5.0.8

-   Fixed error in web console on package deployment
-   Implemented refresh for Event Processing Policy view
-   Fixed Arp Cache view refresh when data is not available
-   Implemented find mac in Web APIs
-   NXSL function "trace" handles objects and arrays in a same way as "print"
-   New methods "print" and "trace" in NXSL class "Table"
-   Added workaround for incorrect LLDP information returned by Alpha Bridge switches
-   Fixed bug in network map link styling script processing

## Fixed issues

-   NX-1311 (Table DCIs ignoring table configuration)
-   NX-2567 (ExternalMetricProvider does not work on Windows)
-   NX-2570 (Use monotonic clock instead of system time for calculating agent uptime)
-   NX-2572 (Problem creating PostgreSQL database during installation on Windows)

# 5.0.7

-   Server configuration option to enable agent tunnel binding using only tunnel's source IP address
-   Fixed incorrect Windows Remote Desktop session color depth reported by agent
-   Fixed buffer overflow for IPv6 IP addresses print in log
-   Fixed top level object display issues in "Infrastructure" perspective

## Fixed issues

-   NX-387 (Tool to read current (loaded) agent config)
-   NX-937 (Copy DCI value from object overview)
-   NX-2206 ("Package Deployment Monitor" should be resorted when status of any deployment changes)
-   NX-2549 (Exception in AlarmNotifier)
-   NX-2551 (Desktop UI show same warning in alarm viewer multiple times)
-   NX-2553 (New agent action - show running configuration)
-   NX-2557 (Exception in WebUI)
-   NX-2559 (Line colors and time frame not saved when double-clicking graphs in Performance tab)
-   NX-2561 (Object query hangs on script errors)

# 5.0.6

-   Added notification channel driver for Mattermost
-   Topic support in notification channel driver for Telegram
-   Fixed incorrect client IP address reported by Windows agent in table System.ActiveUserSessions
-   Fixed bug in output of nxget -U
-   Fixed web UI crash when opening dashboard in kiosk mode

## Fixed issues

-   NX-2550 (Errors in desktop client log (Widget is disposed))

# 5.0.5

-   L2 network map seeds with no SNMP or L2 data will not prevent network map from update
-   Server performance improvements
-   Server actions of types "agent command" and "SSH command" executed asynchronously (partial fix for NX-2541)
-   Fixed server crash during LDAP synchronization
-   Subnets bound to containers correctly displayed in infrastructure perspective
-   Predefined maps with default size and background image resized automatically to be no less than image size

# 5.0.4

-   New SNMP DCI option "Interpret raw value as IPv6 address"
-   Added driver for GE MDS Orbit devices
-   Added driver for EtherWan switches
-   Added driver for Siemens RuggedCom switches
-   Mikrotik driver reports RSSI for wireless clients
-   RSSI is displayed in "Wireless Stations" view
-   Added "move object" item to object context menu
-   Optional context selector for dashboards in dashboard perspective
-   Seed node propery page removed for custom network maps
-   Fixed server crash when accessing alarm category list from NXSL
-   Fixed drawing issues of line charts with logarithmic scale
-   Fixed incorrect line numbers in NXSL error messages
-   Fixed bug in "Go to object" action in UI
-   Fixed bug in D-Link driver
-   Fixed interface utilization information sychronization 
-   Fixed network map color source selection
-   Fixed historical line chart pop-out on web
-   Fixed save of network map object position
-   Fixed tables display glitch on Windows
-   Fixed data type of configuration variable "Objects.NetworkMaps.UpdateInterval"

## Fixed issues

-   NX-2489 (Read list of performance counters only when needed)
-   NX-2536 (SNMP DCI "interpret raw value as MAC address" does not support EUI-64)
-   NX-2537 (Double links on maps)

# 5.0.3

-   Notification channel driver "Shell" escapes single quote character during exec-type command line expansion
-   Priority inclusion rules in UI element filter
-   Macro expansion in API call executeLibraryScript works for all object classes
-   Improved handling of large number of simultaneous ICMP ping requests
-   Fixed bug in database upgrade procedure
-   Fixed deadlock in web UI

## Fixed issues

-   NX-2521 (ICMP.PacketLoss internal DCI collects 0 after server restart)
-   NX-2529 (Option to enable/disable Version Number on Web interface)

# 5.0.2

-   Fixed bug in database upgrade procedure
-   Fixed "pin to pinboard" in UI

# 5.0.1

-   Fixed bug in database upgrade procedure
-   Added CSV export in alarm viewer and agent tunnel manager

# 5.0.0

-   Improved network maps
-   Added network map link styling script
-   Delegate access option that allows read access to network maps without full read access to objects on a map
-   Reworked monitoring of wireless access points and controllers
-   Major overhaul of sensor objects
-   Many NXSL function deprecated in favor of object methods
-   Improved NXSL classes and functions for date/time handling
-   Add option to check alarm details from alarm log view
-   Log parser rules can define metrics that are populated from match data
-   Special NXSL return codes for data collection and transformation scripts (DataCollection::ERROR, DataCollection::NOT\_SUPPORTED, DataCollection::NO\_SUCH\_INSTANCE)
-   New NXSL function FindAccessPointByMACAddress
-   New NXSL function GetMappingTableKeys
-   "Stop" function in script executor view
-   Desktop client can reconnect automatically after short connectivity loss
-   New agent metric File.Hash.SHA256
-   New agent list and table Net.IP.Neighbors
-   Index property displayed in MIB browser
-   Root object can be set for object query
-   Improved SNMP trap processing performance
-   New log parser file option "removeEscapeSequences"
-   Added peer certificate verification in ticketing system connectors
-   Housekeeper scripts (NXSL and SQL)
-   Improved REST API
-   Introduces new object class "Collector"
-   Downtime log controlled by EPP

## Fixed issues

-   NX-480 (Returning "Unsupported" from a script DCI)
-   NX-797 (Automatic reconnect of management console)
-   NX-1790 (Drag-n-dropped object are positioned to wrong place when map is scrolled down or right)
-   NX-1870 (Representation of float DCI that gets string data as input)
-   NX-1935 (Introduce hook script on map regeneration with ability to set link names)
-   NX-2006 (Remove example event templates (code 4000-4011) from database)
-   NX-2038 (Optimize network discovery - separate information gathering and decision making)
-   NX-2076 (Raw value should be always displayed as string)
-   NX-2292 (Automatic maps should not include nodes that are connected through a node that was excluded by filter script)
-   NX-2323 (Make parameters in all events named)
-   NX-2343 (Several changes in NXSL syntax in v 5.0)
-   NX-2375 (Use "varchar(max)" instead of "text" on Microsoft SQL Server)
-   NX-2403 (Add support for AES-192 and AES-256 in SNMPv3)
-   NX-2444 (On demand background external metrics)
-   NX-2455 (Ability to check TLS.Certificate.\* for protocols with STARTTLS command)
-   NX-2481 (Add ability to manually poll network map generation)
-   NX-2507 (Add ability to cancel timers from NXSL)
-   NX-2520 (Remove "Channel name" selector from "Send notification" dialog)
-   NX-2523 (New agent metric Process.MemoryUsage (percentage of memory used by process))
-   NX-2524 (Option to disable threshold without deleting it)
-   NX-2525 (Add the ability to specify multiplier values in threshold)
-   NX-2526 (When editing a template with a DCI without instance to use instance - DCI becomes unsupported)

# 4.5.7

-   Fixed incorrect LLDP topology information reading on some devices
-   Fixed background color issue in user agent's notification popup
-   Fixed memory leak in FreeBSD subagent
-   Fixed server clock widget in UI for time zones with non-whole hour difference from UTC

# 4.5.6

-   Fixed bug in background task scheduler
-   Fixed bug in reporting access control
-   Fixed minor memory leak in server
-   Fixed event storm detection event generation
-   Fixed incorrect notification popup size calculation in user agent
-   Fixed bug in NXSL function CreateUserAgentNotification
-   Improved housekeeper throttling logic
-   User-defined scripts for housekeeper
-   Object context menu available in alarm view
-   Call for DCI status change added to web API

# 4.5.5

-   Fixed scheduled file upload
-   Fixed policy apply on object selection change
-   Fixed custom attribute conflict propagation and conflict removal
-   Fixed agent crash on empty output from external table provider
-   Fixed bug in pin/popup agent file view
-   Updated OPC UA subagent dependencies
-   New agent metrics System.CurrentTime.ISO8601.Local, System.CurrentTime.ISO8601.UTC, and System.TimeZoneOffset
-   Bundled zlib updated to latest version
-   Print exception trace replaced by error logging
-   Disable walk action on root object in mib browser
-   Business service polls can be disabled or will not be executed if object is unmanaged
-   Added peer certificate verification for notification channels 

## Fixed issues

-   NX-2511 (In repeating events, you can specify no more than 5 characters, sometimes more is needed)
-   NX-2516 (CURLAUTH\_NEGOTIATE in not available in libCURL 7.29.0)

# 4.5.4

-   Improved Juniper driver
-   Improved integration with ticketing system Redmine
-   Fixed build errors on Solaris 11.4 with Solaris Studio 12.6
-   Fixed memory leak in web UI (server side)
-   Fixed some server performance issues

## Fixed issues

-   NX-2492 (Custom attribute inheritance conflict not detected)
-   NX-2515 (Inherited object custom attributes not deleted from children)

# 4.5.3

-   Fixed server crash during passive network discovery
-   Fixed bug in dashboard chart data source editor
-   Fixed bug in TCP proxy session setup

## Fixed issues

-   NX-2509 (productVersion does not display value correctly with Ethernet-IP)

# 4.5.2

-   Fixed server crash on client session disconnect
-   Fixed updated issues in new web UI
-   Cosmetic fixes in UI

## Fixed issues

-   NX-2490 (Server tries to read from tdata\_xxxx table when TimescaleDB is used as backend)
-   NX-2502 (nxagentd uses UDP port 4700 to exchange hearthbeat messages and listens on address 0.0.0.0)

# 4.5.1

-   Driver for Edgecore enterprise switches
-   Driver for HPE Aruba Networking switches and wireless controllers
-   Chart height in performance view automatically adjusted to accomodate large legend
-   New NXSL class "MacAddress"
-   Attribute "state" of NXSL class "AccessPoint" renamed to "apState" (to avoid conflict with attribute "state" from parent class)
-   Context object views can be hidden
-   Configurable timeout for client session first packet
-   Improved VLAN handling by generic driver
-   Updated Eltex driver
-   Fix missing object synchronization for ad-hock maps (drill down)
-   Fixed server crash when interface list cannot be read from SNMP device and option to ignore interfaces in NOT PRESENT state is on
-   Fixed bug in EPP rule copying
-   Fixed line numbering bug in desktop UI script editor

## Fixed issues

-   NX-2491 (Add alarm category attribute to NXSL alarm class)
-   NX-2493 (Activation / Deactivation event not shown in threshold editor)

# 4.5.0

-   XPath can be used for querying XML-based web services
-   New NXSL operation "?." (safe dereference)
-   New method "join" in NXSL arrays
-   Server-side custom attributes (not visible by clients)
-   Additional argument in NXSL method createSNMPTransport to control if it should fail when node is marked as unreachable via SNMP
-   Updated drivers for Eltex and TP-Link switches
-   Added agent metric Agent.LocalDatabase.FileSize
-   Fixed internal metrics PollTime.\*

## Fixed issues

-   NX-1409 (Implement separate access right for editing object comments)
-   NX-2275 (Option for ignoring interfaces in NOT PRESENT state)
-   NX-2412 (Separate access right for editing agent configuration file)
-   NX-2440 (Wildcard imports in NXSL)
-   NX-2485 (XPath support in web service queries)
-   NX-2487 (Any changes to object from UI or via Java API wipe out responsible users list)

# 4.4.5

-   Improved SNMP proxy performance under heavy load
-   Added limit on number of nested NXSL VMs (to prevent accidential infinite loop of script execution)
-   Fixed server crash on polling TP-Link switches
-   Fixed bug in dashboard element "status indicator"
-   Fixed bug in status map view
-   Fixed bug in database manager check function
-   Fixed "Failed to register resource" error in web UI
-   Fixed database import/migration to TimescaleDB
-   Java components switched to logback 1.3.13 (fixes CVE-2023-6378)

## Fixed issues

-   NX-2465 (List of saved queries in Tools-\>Find Object is not updated when query list is altered in Configuration)
-   NX-2479 (Misleading error messages when loading properties for root objects)

# 4.4.4

-   New methods in NXSL class "InetAddress": contains, equals, inRange, sameSubnet
-   Constructor for NXSL class "InetAddress" accepts mask length as second argument
-   Fixed incorrect ICMP polling if ICMP proxy set on node level
-   Improved topology discovery on TP-Link devices
-   Improved driver for DLink devices
-   Added driver for TP-Link devices
-   Added driver for Eltex devices
-   Added driver for Q-tech devices
-   nxencpasswd can read password from terminal
-   GUI clients built with patched version of simple-xml (fixes CVE-2017-1000190)
-   Fixed deadlock after login in legacy web UI

## Fixed issues

-   NX-2431 (Implement agent list Net.IP.RoutingTable for AIX)
-   NX-2478 (Named function parameters does not work for entry points)

# 4.4.3

-   Package deployment can be scheduled
-   Server-side macro expansion in package deployment command
-   Use compact JSON format when saving events to database
-   Improved event processing performance
-   Improved NXSL function "random"
-   New event processing macros %d (DCI description), %D (DCI comments), %L (object alias), and %C (object comments)
-   Added driver for FortiGate devices
-   Fixed server crash during execution of delayed EPP action
-   Fixed server crash when processing interfaces with 8 byte MAC address
-   Fixed session disconnect handling in new management client application
-   Fixed bug in physical disk information reading on Windows
-   Fixed bug in SSH key store
-   Improved debug logging
-   Minor fixes and improvements in new management client application

## Fixed issues

-   NX-1063 (Interface icon is incorrect)
-   NX-2224 (Command history in nxadm)
-   NX-2446 (Increase timeout for agent tunnel binding)
-   NX-2463 (Add metric to measure execution time of background queries in dbquery subagent)
-   NX-2467 (Allow to execute same action multiple times in one EPP rule)
-   NX-2468 (NetworkService.Status SMTP call to curl\_easy\_perform failed (56: Command failed: 502))
-   NX-2469 (Empty "Parameters" line should be interpreted as no arguments in Execute Script)
-   NX-2471 (Add agent list and table to list physical disks)
-   NX-2475 (netsvc: ServiceCheck.SMTP() uses VRFY command, which is disabled on most servers)

# 4.4.2

-   Server checks interface speed during status poll and generates event if it changes
-   Improved Cambium device driver
-   Added driver for Hirschmann switches
-   Implemented implicit import for constants in NXSL
-   NXSL implicit import does not add non-referenced functions and constants from imported module
-   Context action "Change expected interface state" implemented in new GUI client
-   Context action "Clone network map" implemented in new GUI client
-   Masked credentials in "Network Credentials" view
-   Fixed bugs in TCP proxy session closure handling (server and agent side)
-   Fixed bug in parsing XML content returned by web service
-   Fixed template apply/remove in new GUI client
-   Fixed server crash when network map uses physical link with non existing rack
-   Fixed audit log writing on object move

## Fixed issues

-   NX-2410 (Notification driver is locked during retry waiting period)
-   NX-2432 (Query interface speed when status poll detects that interface goes up)
-   NX-2441 (Auto-focus on Two-Factor input on WebUI)
-   NX-2442 (Maintenance predefined time)
-   NX-2449 (Unexpected SYS\_DUPLICATE\_IP\_ADDRESS generation)
-   NX-2450 (microhttpd presence is not detected correctly)
-   NX-2451 (GetDCIValue() should return same data type as set in DCI properties)
-   NX-2452 (Agent on Windows returns only one software inventory record when multiple versions of same software are installed)

# 4.4.1

-   Improved support for LLDP-V2-MIB
-   Server can use both LLDP-MIB and LLDP-V2-MIB if supported by device
-   Server saves SNMPv3 context engine ID alongside authoritative engine ID to avoid unnecessary engine ID discovery
-   NXSL function GetDCIValues can be used to retrieve raw DCI values
-   Added method "enableWinPerfCountersCache" to NXSL class "Node"
-   Custom timeouts for external metric providers in agent
-   Fixed incorrect display of line chart series with "Invert values" option
-   Fixed database upgrade procedure (zone UIN update)
-   Fixed memory leak in subagent "netsvc"
-   Fixed bug in NXSL function FormatMetricPrefix
-   Added workaround for "unexpected eof" OpenSSL error reported by web service calls to some servers
-   Minor fixes in asset management
-   Minor fixes and improvements in new management client application

## Fixed issues

-   NX-2407 (Add the ability to duplicate server action in action manager)
-   NX-2414 (nxdbmgr should ignore data for deleted DCIs if there's record in dci\_delete\_list for that DCI)
-   NX-2415 (Legend text color is ignored in the nxmc console)
-   NX-2419 (When log file monitoring with wildcards is used, data right after file creation might be skipped)
-   NX-2428 (Cannot import configuration if threshold activation or deactivation event tags are missing or empty)
-   NX-2434 (Add option to set user, password as a parameters for IMAP and SMTP)
-   NX-2435 (0 is not shown on Y scale in graphs)

# 4.4.0

-   "Trusted devices" in two-factor authentication
-   Scrollable dashboards
-   Native Modbus TCP support
-   Arguments can be passed to script called via script macro
-   Indirect function calls in NXSL
-   Interface table in agents
-   Linux agent can report interface aliases
-   Improved dashboard elements "Pie Chart" and "Gauge"
-   New macro {node-name} in DCI performance view configuration
-   Added Query table columns for SNMP Table DCI
-   Spanning Tree port state for interfaces collected at status poll
-   System event for STP port state change
-   Improved configuration import

## Fixed issues

-   NX-457 (Support for multiple tile providers)
-   NX-696 (Condition status reset to UNKNOWN on change)
-   NX-875 (More info on per-node basis on polls for that node)
-   NX-935 (Scrollbar in Dashboards)
-   NX-1014 (Correct names of "Remove" menu items to "Remove from node" or "Remove from template")
-   NX-1232 (Tool for simplified SNMP tables configuration)
-   NX-1598 (Rename column "submap\_id" in table "object\_properties")
-   NX-1613 (Object state icon not shown in Template -> Remove)
-   NX-2067 (Add a hotkey to save policies. Ctrl+S)
-   NX-2244 (Have ability in the UI to jump to specific DCI from check)
-   NX-2294 (Add server setting to prefer IPv4 address when resolving node hostname)
-   NX-2295 (Use System.ActiveUserSessions agent list to display "User sessions" in management client)
-   NX-2317 (Add parameters to threshold activation events with additional information on triggered threshold)
-   NX-2357 (Create events for invalid object identifiers in EPP rules)
-   NX-2364 (Add option to request 2FA authorization less frequently)
-   NX-2370 (Use libedit for shell-style tools)
-   NX-2372 (Show DCI comments in Data Collection / Last Values view)
-   NX-2373 (Make DCI comments available in alarms generated from threshold violation events)
-   NX-2384 (Store and display event message in active threshold)
-   NX-2391 (Not possible to set correct zone for cluster)
-   NX-2392 (ARP table view for nodes)
-   NX-2397 (Cluster that is in another zone still belongs to the zone with Zone UIN=0)
-   NX-2420 (Add explicit option for log parser to follow symlinks)
-   NX-2422 (Keep separate session for each node in MIB explorer in new Management Client)
-   NX-2424 (Add information about user login failure (2FA issue, etc) to audit log)

# 4.3.7

-   Fixed bug in reading topology information from LLDPv2 MIB
-   Small fixes and improvements in new management client application

## Fixed issues

-   NX-2253 (Actual repeat count should be passed to event in log file monitoring when reset repeat count is true)
-   NX-2418 (Log file monitoring does not work properly with symlinks)
-   NX-2421 (Invalid time format in log parser configuration can cause agent crash)

# 4.3.6

-   Correctly handle FDB record type "secure"
-   Improved driver for Cambium devices
-   Fixed bug in handling /32 addresses during network discovery
-   Fixed bug in flood notification processing in Telegram driver
-   Fixed server crash caused by timeout during file transfer to agent
-   Fixed bug in SNMP codepage handling
-   Fixed bar gauge dashboard element drawing issue
-   Small fixes and improvements in new management client application

# 4.3.5

-   Fixed bug in X.509 certificate subject and issuer decoding
-   Agent tunnel listener will not start if server certificate is not loaded
-   Fixed WEB service configuration import with multiple headers 
-   Fixed login issues in new web UI
-   Small fixes and improvements in new management client application

## Fixed issues

-   NX-2272 (Session is not closed if user cancel 2FA auth initialization)
-   NX-2276 (Warn user when adding too wide mask to active discovery)
-   NX-2388 (Modify default templates - filesystem with type "ahafs" should be excluded from discovery)
-   NX-2404 (Integer division by zero in NXSL crashes server)
-   NX-2406 (Entering maintenance mode on cluster does not trigger maintenance mode on nodes within cluster)

# 4.3.4

-   Fixed bug in ICMP ping implementation introduced in 4.3.3
-   Added agent configuration option for setting file mode creation mask (umask)
-   Bundled SQLite updated to version 3.41.2
-   Multiple fixes and improvements in new management client application

## Fixed issues

-   NX-2137 (File delivery policy times out of big files when saved)
-   NX-2386 (Object Category custom node icon covers object browser status icon)
-   NX-2395 (Output of PATCH Web Service call is ignored)
-   NX-2396 (Web Service Definition timeout not displayed correctly)

# 4.3.3

-   Improved database migration procedure when TimescaleDB is target (GitHub issue 83)
-   Fixed bug in handling "verify-peer" option for network service metrics
-   Fixed server crash when doing RADIUS authentication using MS-CHAP
-   Fixed columns for 'Find switch port' search result
-   Added additional information to debug message about event with incorrect source id
-   Added ZoneUIN for Cluster's overview page
-   Small fixes and adjustments to new management client
-   Close DCI config view message not shown on DCI copy
-   Dashboard element "Table Value" works in context dashboards

## Fixed issues

-   NX-2387 (SQL errors when saving OSPF neighbor list)

# 4.3.2

-   Fixed stacked line charts in new UI
-   Fixed timeout inconsistencies in netsvc subagent
-   Added web API calls for managing alarm comments
-   More functionality migrated to new management client

## Fixed issues

-   NX-677 (Dashboard editor: accelerators are duplicated in Line chart -> Data sources)
-   NX-2377 (Copy-paste of rules not working in EPP editor)
-   NX-2348 (Show active threshold event name in Last Values)
-   NX-2376 (Agent restart is not working correctly on RedHat based Linux OS)
-   NX-2379 (REST API to force poll DCI)
-   NX-2383 (Ignore systemd synthetic records when resolving node IP address to hostname)

# 4.3.1

-   Fixed database schema upgrade on Microsoft SQL Server
-   Fixed issues with network service checks using netsvc subagent as a replacement for portcheck subagent
-   Fixed bug in external table provider command execution
-   Fixed server crash during execution of object tool of type "server command"
-   Dashboard element "Availability Chart" is working again
-   Mikrotik driver correctly handles server settings for using ifXTable and interface aliases
-   Fixed VLAN configuration reading bug in Juniper driver
-   Multiple fixes and improvements in new management client application
-   Cosmetic fixes in Windows agent installer

## Fixed issues

-   NX-808 (NXSL error message should include module name)
-   NX-2222 (Interface alias duplicated in UI if Objects.Interfaces.UseAliases set to "concatenate name with alias")
-   NX-2345 (Copy to Clipboard and Save as image... buttons no longer exist in WebUI in line chart window)
-   NX-2374 (Template auto unbind grace period handled incorrectly)

# 4.3.0

-   New format strings in NXSL (Python f-string style)
-   Intoduced two dots option to concatinate string in NXSL
-   NXSL keywords replaced: "sub" changed to "function" and "use" changed to "import"
-   Inline action scripts in EPP
-   Set and delete custom attributes in EPP rule
-   Column display names in object queries can be set using column metadata
-   New agent metrics File.Type and File.Content
-   New dashboard element "File Monitor"
-   Functionality of PortCheck and ECS subagents merged into NETSVC subagent
-   In dbquery subagent configuration database connections can be configured as separate sections
-   Database driver options can be configured in dbquery subagent
-   SMTP driver supports authentication
-   Correctly read LLDP information from devices that support only LLDP-V2 MIB
-   Fixed object query result sorting on hidden columns
-   Server configuration parameter DBDrvParam is deprecated and replaced with DBDriverOptions

## Fixed issues

-   NX-538 (ESXi not detected as LLDP)
-   NX-1291 (Different font size on different dashboard gauge entries)
-   NX-1915 (Ability to copy shared secret from Network Configuration)
-   NX-2075 (EPP rule to have both IF and IF NOT conditions for objects)
-   NX-2180 (Clusters cannot change zones)
-   NX-2192 (Merge PortCheck and ECS subagents functionality into NETSVC subagent)
-   NX-2270 (After adding device overview to pinboard it is not displayed properly on the pinboard)
-   NX-2289 (Filtering on Container object Thresholds tab)
-   NX-2301 (Show interfaces in object tree when searching for node)
-   NX-2303 (Add OAuth 2.0 Bearer Access Token in libcurl build on Windows)
-   NX-2305 (Add wrapper to get information from smartctl)
-   NX-2311 (Add macros to display DCI values with multipliers and measurement units)
-   NX-2312 (Named capture groups in log parser)
-   NX-2320 (Configuration import ends with timeout for large configuration files)
-   NX-2324 (Telegram notifications should stay in queue if there is no connection to the Internet)
-   NX-2327 (SMTP driver with authentication support)
-   NX-2328 (Improved algorithm for managing thread pool size)
-   NX-2329 (Time based filter in EPP rules)
-   NX-2330 (Add option to set/delete custom attributes from EPP rule)
-   NX-2331 (Display DCI and policy count for templates in object details)
-   NX-2332 (Add new EPP action that allows to specify NXSL script inline)
-   MX-2335 (MQTT DCIs on objects of Sensor class)
-   NX-2336 (F-strings in NXSL)
-   NX-2337 (Side areas in new UI)
-   NX-2339 (New syntax for calling external processes)
-   NX-2350 (Use Container for Seed Node)
-   NX-2352 (File manager's chmod does not work with environment variables)
-   NX-2360 (Network equipment may get discovered by a broadcast address)
-   NX-2367 (netxms-dbdrv-mariadb uses character set utf8mb3 instead of utf8mb4 as connection encoding)
-   NX-2368 (NetXMS Agent Windows Service recovery to restart on failure)

# 4.2.461

-   Improved dashboard element "status indicator"
-   Improved SMSEagle notification channel driver
-   Fixed random zero values returned by Linux agent for file system space metrics
-   Fixed copy MAC in FDB table
-   Fixed server certificate monitoring template

## Fixed issues

-   NX-2056 (Create DCI status indicator dashboard element)
-   NX-2326 (Add parameter in log parser events that contains file name)
-   NX-2346 (Unexpected SNMPv3 authentication failures)
-   NX-2349 (NXSL `$node->executeAgentCommand()` crashing server)

# 4.2.433

-   Driver for Juniper Networks devices retrieves product information from vendor MIB
-   Empty source/tag is processed as match any source/tag for Windows Event Log and syslog parser
-   Configurable maximum message size for client connections
-   "Follow location" option for web services
-   Fixed server crash after DB connection loss
-   Fixed server deadlock within topology poll
-   Fixed web application property reading from JNDI and properties file

## Fixed issues

-   NX-2278 (Support for hexadecimal encoding of OCTET STRING in nxsnmpset)
-   NX-2298 (Alphabetize Source Objects in Event Processing Policy)
-   NX-2315 (Chained import in NXSL is not working)
-   NX-2321 (History for a Table DCI value shown as empty)
-   NX-2333 (Data collection error thresholds show up as "`error(1) < 0`")

# 4.2.395

-   Context dashboards
-   Out of the box access to OSPF information on routers
-   Automatic OSPF topology maps
-   TCP port forwarding for object tools of type "local command" and "URL"
-   "Spread" operation for arrays in NXSL
-   New methods executeAgentCommand and executeAgentCommandWithOutput in NXSL class "Node"
-   Simplified data collection configuration for MQTT sources
-   Notification channel driver for MQTT
-   Automatic binding on configuration poll works again (but can be switched off in configuration)
-   Added driver for Teltonika modems
-   Improved database write performance on TimescaleDB and PostgreSQL
-   Reduced memory consumption by server's background database writer
-   Improved UI for two-factor authentication
-   Improved D-Link driver
-   Agent saves backup copy of it's ID on file system
-   Reworked general data collection object property page
-   Added internal monitoring metrics for server certificate expiration date
-   Built-in TFTP support
-   Fixed network map issues with link duplicates on auto populated maps
-   Fixed network map clone
-   NXSL function JsonParse correctly handles JSON documents with array as top level element
-   Custom error message can be provided in NXSL statement `abort`
-   Operator `new` in NXSL can be omitted
-   NXSL VM automatically loads `stdlib` module if it's available in the script library
-   Improved DCI format strings (usage of unit names and multipliers can be controlled)
-   Agent manager view updates automatically on tunnel open or close
-   Added Organizationally Unique Identifier lookup

## Fixed issues

-   NX-648 (DCI units and binary prefix)
-   NX-702 (DCI option - "Store only if value changes")
-   NX-708 (Add map option to make all labels non-transparent)
-   NX-826 (Show chart title in dashboard elements editor)
-   NX-1279 (WebUI does not support ServerName/ServerColor options)
-   NX-1474 (Execute server script - replace error message box with alternative way)
-   NX-1527 (Option to hide DCIs from templates or created by instance discovery)
-   NX-1560 (List of custom agent ports to be used during network discovery and configuration polls)
-   NX-1632 (NetXMS agent service is disabled after installing netxms-agent deb package on Debian 9)
-   NX-1809 (Center Map Background Image)
-   NX-2044 (Object Tool to run against container)
-   NX-2078 (Add the ability to specify an alias when creating an object)
-   NX-2103 (Add ability to push values to Push DCIs from log file parser)
-   NX-2140 (Export result of the package deployment to CSV)
-   NX-2234 (With a drop-down menu with a choice of DCI metrics, swap the display of Description and Name (Parameter))
-   NX-2237 (Add the ability to set height for passive elements in rack and use custom picture)
-   NX-2251 (Add 'conflict' marker to inherited custom attributes)
-   NX-2259 (Configurable server's SNMPv3 engine ID)
-   NX-2261 (Access to MikroTik metrics via network driver metrics)
-   NX-2266 (Add agent metric similar to `System.IO.Devices` but including sub-devices)
-   NX-2273 (2FA method can't be removed in user editor)
-   NX-2274 (2FA - unable to add failed method in user editor - it's silently ignored)
-   NX-2281 (Action message should be multiline field)
-   NX-2288 (External parameter redirect issue on Ubuntu 22.04 LTS)
-   NX-2302 (NXSL function PollerTrace is not working in template auto-apply poll)
-   NX-2304 (Improved script execution options for nxadm)
-   NX-2306 (Node configuration poll don't update information about interfaces type)
-   NX-2308 (LDAP user sync login error should be logged at lower level)
-   NX-2309 (No scrolling or resize for ports part in VLAN view)

# 4.1.420

-   Optimized alarm resolve/terminate using regular expressions
-   Improved topology detection on Juniper switches
-   Fixed communication protocol compatibility issues in C++ client library and command line client tools
-   Fixed business service default retention time for historical data

## Fixed issues

-   NX-627 (Gauge rendered incorrectly)
-   NX-846 (Ability to copy to clipboard in Routing Table and FDB views)
-   NX-1077 (Option to copy MAC address to clipboard in FDB view)
-   NX-2283 (Show version in debug console)

# 4.1.404

-   Fixed full screen dashboard display on startup in desktop client
-   Improved database consistency checks for business services
-   Added Oracle driver option to disable OCI statement caching
-   Fixed slow appearance of discovered nodes
-   Fixed bugs in database schema upgrade from pre-4.0 versions
-   Fixed bug in map options property page
-   Fixed incorrect string encoding during SNMP SET operation
-   Fixed sqlite upgrade issues

## Fixed issues

-   NX-755 (Network discovery may not stop immediately)

# 4.1.377

-   Agent configuration option to disable local database
-   Linux subagent can read software inventory from OpenWrt package manager
-   Added driver for HPE iLO
-   Fixed incorrect return code of NXSL function `SNMPSet` and method `set` in SNMP transport
-   Original DCI string value returned by transformation script is preserved
-   Fixed bug in downtime calculation for hierarchical business services

## Fixed issues

-   NX-2262 (`syncUserDatabase()` does not wait for `CMD_USER_DB_EOF`)

# 4.1.333

-   Added support for package type "zip"
-   Fixed incorrect label colors on dashboards after migration from 4.0
-   Minimum number of bytes required for MAC address search reduced to two
-   Reading of ipAddrTable and/or ipAddressTable during configuration poll can be disabled via custom attributes
-   Fixed server crash caused by incorrect value of configuration parameter `ICMP.PingSize`
-   Multiple fixes and improvements in new UI

## Fixed issues

-   NX-2089 (Bundle prunmgr.exe with web-ui installer)
-   NX-2250 (Show VLAN information on interface overview page)
-   NX-2258 (No context menu on area of interactive dashboard graphs)

# 4.1.283

-   Maintenance journals for objects
-   SSH connectivity checked as part of status and configuration polls
-   Runtime errors in filtering scripts interpreted as "ignore" if applicable and otherwise as "block"
-   Authentication option (on by default) for local server console (accessible via nxadm)
-   Added driver for Ubiquiti EdgeSwitch switches
-   Octal numeric constants removed from NXSL
-   New string method `equals` in NXSL
-   Jira connector supports Jira Cloud
-   Internal metrics for monitoring notification channels
-   Improved titles in dashboard elements
-   Ignore IP addresses found during network discovery on interfaces marked as excluded from topology
-   New server configuration variables:
    -   `AgentTunnels.Certificates.ReissueInterval`
    -   `AgentTunnels.Certificates.ValidityPeriod`
-   Fixed DCI creation from NXSL
-   Added $dci variable to DCI script
-   Added option to configure column data type for external table

## Fixed issues

-   NX-1115 (JIRA configuration parameters re-read only on restart)
-   NX-1183 (Add option to choose automatic colors for instances in performance tabs)
-   NX-1734 (Add column "Peer Interface" to interface list view)
-   NX-1785 (Automatic color assignment for items on performance tab graph)
-   NX-1802 (Binary data support in NXSL SNMP functions)
-   NX-2021 (Title is not displayed for some Dashboard elements)
-   NX-2154 (Node search by partial MAC address)
-   NX-2163 (Show user name on process tab)
-   NX-2165 ("Show file" in file manager displays incorrect progress bar message)
-   NX-2196 (Keep SNMP alias separately in interface object)
-   NX-2215 (Extract XMPP related code into a notification channel driver)
-   NX-2216 (Telegram notification channel should throttle message sending and retry sending after timeout)
-   NX-2220 (Add timer key column to Scheduled Tasks)
-   NX-2223 (Notification log view should have multi-line preview panel)
-   NX-2225 (Maintenance journal)
-   NX-2226 (Agent policy move to TemplateGroup)
-   NX-2229 (Add scrollbar and ability to resize to script editor in Object Query)
-   NX-2230 (Business service enhancements)
-   NX-2231 (Use TCP/UDP for active network discovery)
-   NX-2233 (Add new agent metric similar to `Service.Check()` that would follow redirects)
-   NX-2239 (Node SSH polling)
-   NX-2240 (Changes to DCI comments in template are not synchronized with DCIs created from that template)
-   NX-2242 (On Windows, if agent action calls .cmd file and that file produces output, execution fails)
-   NX-2252 (`TLS.Certificate.*` 500 internal error to some domains when nginx enabled ssl\_reject\_handshake on)
-   NX-2254 (LDAP synchronization error events generated for any LDAP user login error)
-   NX-2255 (SQL issues with server\_action\_execution\_log)
-   NX-2256 (Have two separate certificates on server - for TLS connection and to issue agent certificates)
-   NX-2257 (`PostgreSQL.Version` returns 0.0 if database is not connected)

# 4.0.2227

-   NXSL hook script for user login
-   SSH subagent metric `SSH.Command` returns collection error instead of "unsupported metric" if host name cannot be resolved

## Fixed issues

-   NX-2227 (Typo in message for event `SYS_DUPLICATE_MAC_ADDRESS`)
-   NX-2235 (Object Query CSV export does not prompt to overwrite .csv file)
-   NX-2236 (Option of copying of data from an Object Query in Dashboard view)

# 4.0.2195

-   Fixed bugs in IP topology map builder
-   Added action to open object details form Business Service checks
-   Alarms for unknown nodes are not included in summary e-mails
-   Fixed bug with threshold recreation on any DCI change

## Fixed issues

-   NX-2214 (Agent does not report network interface speed)

# 4.0.2157

-   New parameter `Oracle.Cursors.MaxPerSession` in Oracle subagent
-   Fixed json file parsing for Web Services

## Fixed issues

-   NX-2212 (Agent segmentation fault when accessing table `Hardware.NetworkAdapters`)
-   NX-2213 (Set event parameter from NXSL by index)

# 4.0.2151

## Fixed issues

-   NX-2210 (Network Service HTTP polling ports above 32767 generates incorrect Host header in HTTP request)
-   NX-2211 (Agent crash while processing request for `System.ThreadCount`)

# 4.0.2148

-   New attribute "lastCollectionTime" in NXSL class "DCI"
-   Notification channel driver for Twilio
-   Fixed server crash on receiving SNMP trap if configuration parameter `SNMP.Traps.LogAll` is set to true
-   Fixed bug in automatic object binding
-   Fixed bug in NXSL function FormatMetricPrefix
-   Fixed bug in business service state calculation
-   Fixed incorrect handling of manually set Y axis range on bar charts

## Fixed issues

-   NX-2153 (Add REST API endpoint for persistent storage)
-   NX-2198 (Alternative data source for agent parameters `Hardware.System.*` on Linux)
-   NX-2209 (cpuid.h is not supported on ARM macOS)

# 4.0.2088

-   Two-factor authentication for users
-   SMTP implemented as a notification channel and e-mail actions replaced by notification actions
-   Added `DefaultNotificationChannel.SMTP.Html` and `DefaultNotificationChannel.SMTP.Text` server
    configuration parameters for default SMTP channel names used by internal functions
-   Removed lock for user management view
-   Strings `true` and `false` interpreted as boolean values when accessing custom attributes from NXSL
-   Database manager can create database and database user before database schema initialization
-   OPC UA subagent moved to core product
-   Added option to manually create subnet
-   Separately configurable timeouts for agent's external parameters and external command execution
-   Zoning is enabled by default
-   Value of any type can be used as boolean in NXSL
-   NXSL operator `in` works for strings and hash maps
-   Single-quoted strings in NXSL (without escape characters)
-   Multiline string constants in NXSL
-   Operators `print` and `println` in NXSL converted to functions
-   New methods `contains` and `remove` for NXSL hash maps
-   Improved string manipulation functions in NXSL
-   Integer division operator in NXSL
-   Multi-OID SNMP requests in NXSL
-   Macros can be used in object comments
-   New threshold type "absolute deviation"
-   Added option for L2 network maps to create links using physical links
-   Configurable HTTP request method and request data in web service definitions
-   Polling intervals can be overridden on object level via custom attributes
-   Implemented DCI search on container
-   Improved Web API
-   Improved SSH subagent
-   Inherited object access rights visible in object properties in UI
-   Correlated events can be processed in event processing policy
-   Escalation level for responsible users
-   Structured alarm filter in UI
-   Log parser debug output only controlled by debug level for tag `logwatch.parser` (parser option `trace` is deprectated)
-   Added support for multi-select fields in report execution forms
-   Improved package deployment via agents
-   New event template option "hide from event monitor"
-   Reporting server uses XLSX format instead of XLS
-   Fixed small issues in object custom attribute inheritance

## Fixed issues

-   NX-1 (New threshold type: absolute deviation)
-   NX-251 (Service check for POP3S and SMTPS)
-   NX-436 (Add an option to secure syslog server)
-   NX-841 (Bar Chart legend always shown in two columns, event if space if available for more elements in each line)
-   NX-843 (Transposed bar chart use data sources from bottom to top instead of standard top to bottom)
-   NX-1354 (Object ACL editor should not allow empty list of users without "inherit access rights" checkbox)
-   NX-1382 (NXSL `$dci->instance` has `instance-name` value)
-   NX-1452 (User filter for `Process.Count` parameter)
-   NX-1468 (Status from network map objects is not propagated to map groups)
-   NX-1487 (Grace period for automatic template removal)
-   NX-1611 (Macro expansion in object comments)
-   NX-1660 (Generate event on ICMP status poll failure)
-   NX-1673 (DCI Performance tab - `{instance-name}` doesn't work)
-   NX-1698 (SNMP query for printer status string is unreadable)
-   NX-1766 (File transfer implementation issues)
-   NX-1776 (Forbid deletion of events that are used in thresholds or policies)
-   NX-1822 (DCI should stay disabled, if it stops getting discovered by instance discovery and gets discovered again)
-   NX-1829 (Misleading error message, when trying to rename protected image in image library)
-   NX-1838 (Files in file delivery policy should be exported as part of configuration export)
-   NX-1859 (Implement two-factor authentication in NetXMS server)
-   NX-1923 (Enforce unique event names)
-   NX-1972 (Add extended version of `System.Processes` table having info on CPU and memory consumption per process)
-   NX-2013 (Add ability to send audit log to syslog in UTF-8)
-   NX-2025 (Add macro expansion in timer delay and snooze time fields in EPP action properties)
-   NX-2032 (Create new REST API endpoint to set custom attribute on object)
-   NX-2062 (Add option to specify community string in CreateSNMPTransport)
-   NX-2066 (Add more parameters to events created on server within Windows Event Log synchronization)
-   NX-2068 (Rename column `check_responce` in table `network_services` to `check_response`)
-   NX-2069 (Collect hardware information about HDD/SSD and network cards on Linux)
-   NX-2095 (Add option to access node hardware inventory information from NXSL)
-   NX-2098 (New action type "Execute command on remote node via ssh")
-   NX-2100 (Add "support level" or "escalation" value to Responsible persons)
-   NX-2111 (Add ability to configure web service proxy in node properties)
-   NX-2161 (Move execution of object queries from "Configuration" menu)
-   NX-2167 (Add context to `SYS_SCRIPT_ERROR` event)
-   NX-2173 (File integrity monitoring)
-   NX-2174 (Periodically check telegram API if it's operable)
-   NX-2178 (Configurable encoding for SNMP)
-   NX-2179 (Configurable encoding for syslog)
-   NX-2184 (Notification channels SMTPS support)
-   NX-2185 (Certificate pinning for agent tunnels)
-   NX-2189 (Typo when interfaces are removed during polling)
-   NX-2190 (Add NXSL function that will convert numeric value to human-readable form with multipliers)
-   NX-2191 (Ignore node unreachable state when performing manual configuration poll)
-   NX-2194 (Add option to access node software inventory information from NXSL)
-   NX-2195 (DB Checker inefficiencies with IsDciExists)
-   NX-2198 (Alternative data source for agent parameters `Hardware.System.*` on Linux)
-   NX-2199 (Agent parameters to get certificate information from file)
-   NX-2200 (Remove length limit on command in NXSL method `Node::executeSSHCommand`)
-   NX-2204 (Agent not recognizing Windows 11)
-   NX-2205 (Generate event if LDAP sync failed)
-   NX-2207 (Implement `System.OS` metrics for Linux, AIX, FreeBSD and Solaris)
-   NX-2208 (Zone UIN being reused)

# 3.9.420

-   New agent command line option `-Q` (query values of configuration entry)
-   Windows service start mode can be changed from UI
-   Improved web API for accessing collected DCI data
-   Improved file transfer on slow links
-   Fixed bug in network topology discovery

## Fixed issues

-   NX-290 (SSL Certificate expiration check)
-   NX-781 (Convert to template item work incorrectly on cluster nodes)
-   NX-1032 (Threshold violations are not shown for table DCIs)
-   NX-1551 (Multiple execution completion dialogs after executing object tool on container)
-   NX-1587 (Fix MySQL error: The `INFORMATION_SCHEMA.GLOBAL_STATUS` feature is disabled;
    see the documentation for [show\_compatibility\_56](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_show_compatibility_56))
-   NX-2122 (Table DCI last values are not loaded on server start)
-   NX-2152 (Map should zoom in relation to mouse cursor, not center of map view)
-   NX-2175 (Add hint to SNMP Trap Transformation Script editor)
-   NX-2182 (Changing `Objects.Nodes.ResolveNames` actually requires server restart, but should work without server restart)
-   NX-2183 (Daily Email Summary doesn't seem to resolve users properly in "Ack/Resolved by" column)

# 3.9.361

-   Custom port number can be specified in MySQL and MariaDB database drivers
-   MySQL subagent can be switched to use MariaDB driver
-   Fixed bug in housekeeper (expired DCI data may not be deleted)
-   Object filtering in object tree by exact IP address
-   State filter in /objects endpoint in web API

## Fixed issues

-   NX-30 (Show thresholds on graph is broken)
-   NX-127 (Implement `System.CPU.Usage.IoWait` in Solaris subagent)
-   NX-1448 (It is not possible to specify semicolon as external table separator)
-   NX-1450 (External parameters that returns process exit code)
-   NX-2157 (Macros are not expanded when uploading file via file delivery policy)
-   NX-2166 ("Hide value on last values" does not work)
-   NX-2168 (Divide by zero on core start)
-   NX-2170 (Macros in shell notification channel are not resolved)

# 3.9.334

-   Fixed bar gauge color selection by active DCI threshold
-   Bundled SQLite updated to version 3.36.0
-   Windows crash dump handler writes compressed dump files
-   Improved Juniper driver
-   NXSL methods `enableConfigurationPolling` and `enableStatusPolling` moved from class `Node` to class `DataCollectionTarget`
-   New method `enableDataCollection` in NXSL class `DataCollectionTarget`
-   New agent parameters `System.CurrentDate` and `System.TimeZone`
-   Fixed bug in cluster resource selection for table DCI
-   Fixed possible server deadlock when zone proxies are in use

## Fixed issues

-   NX-2107 (SQL error on server startup)
-   NX-2128 (Disabled DCIs with instance discovery generate instance DCIs)
-   NX-2131 (Migration from psql-timescale to psql is broken)
-   NX-2132 (nxdbmgr check should not delete orphaned idata/tdata records on Timescale database)
-   NX-2143 (MIB Explorer "Create Data Collection item..." reports error on Retention time 0 or blank, but is added as "default")
-   NX-2144 (Graph Title in Web GUI is truncated, seemingly due to an ampersand)
-   NX-2145 (Update HP iLO Template to include support for HP iLOs on G10 servers)
-   NX-2148 (MIB compiler throws syntax error if statements in TEXTUAL-CONVENTION definition are in non-standard order)
-   NX-2149 (Custom Attribute Inheritance - detached inherited custom attribute not deletable)
-   NX-2150 (nxshell session.modifyObject produces Variable not found exception with setSnmpAuthName)

# 3.9.298

-   Improved file delivery policy editor
-   Fixed bug in centralized agent upgrade on Windows
-   New endpoint /events in web API for sending events
-   Filtering by primary host name in web API endpoint /objects
-   Fixed session agent crash on 32 bit Windows systems

## Fixed issues

-   NX-2129 (File delivery policy on Windows Agent causing .part0 to be added to the filename)
-   NX-2130 (If file in file delivery policy is updated new version is appended to the old one instead of replacing it)
-   NX-2133 (Set subagent column as instance on table `Agent.SubAgents`)
-   NX-2134 (Agent crashes if invalid owner or group set in file delivery policy)

# 3.9.280

-   Service manager view for nodes
-   External audit logging via LEEF protocol
-   Improved process table in Windows agent
-   Windows service manager in GUI
-   Process manager in GUI
-   Optimized working with ICMP
-   Object alias shown in geo map tooltips
-   Geo map tooltips work in web UI
-   Added option to hide other objects in object's geo location view
-   Object names can be shown on geo maps
-   Fixed issues with Chassis/Rack placement properties page save
-   Fixed bug in standard deviation calculation in ping subagent
-   Fixed incorrect limit on dashboard element span in UI property page
-   Fixed file transfer issue when upgrading agents from Package Manager

## Fixed issues

-   NX-2050 (Show Node alias on Status Map widget)
-   NX-2115 (Allow adding image in chassis properties without selecting a rack)
-   NX-2118 (Changes in ICMP statistic collection period are not applied until server restart)
-   NX-2119 (Agent table "`ICMP.Targets`" should have "Standard deviation" column)
-   NX-2121 (Status map view should show node aliases)
-   NX-2124 (Log parser hangs on lines longer than 4095 characters)
-   NX-2125 (Server incorrectly reads IP network mask from VMWare ESXi and vCenter)

# 3.9.235

-   Fixed bug in NXSL function `trim`

## Fixed issues

-   NX-2108 (3.9.229 Cannot start process (No such file or directory))

# 3.9.229

-   Dashboards can be saved as images in desktop UI
-   Database manager checks for access point objects without valid parent node
-   Server does not report duplicate MAC addresses if interfaces are from same node
-   New agent actions: `Process.Terminate`, `Service.Start`, `Service.Stop`
-   Web API session inactivity timeout can be configured
-   Fixed server deadlock related to multi-zone configuration
-   Fixed bugs in external command execution
-   Fixed small issues in influxdb driver
-   Fixed deleted form network map object list load from database on startup
-   Fixed rack placement object property page save
-   Fixed bug in SQLite driver (incorrect reading of fields with null value)

## Fixed issues

-   NX-1625 (`Icmp.MovingAvgPingTime(*)` need a way to specify sample size)
-   NX-2092 (Keep last known topology information when node goes down)
-   NX-2093 (Add new parameter to ping subagent that will calculate jitter as moving average on response time deltas)
-   NX-2101 ("Compile script" button should not be present in script preview in EPP rule list)

# 3.9.178

-   Server installer on Windows has database initialization task unchecked when upgrading from pre-3.9 version

# 3.9.176

-   Added option to push DCI data using Web API
-   Fixed bug in file transfer to agent on Windows
-   Fixed agent crash if file template is used in logwatch subagent
-   Fixed object tools in alarm browser
-   Server configuration tree logged on startup

## Fixed issues

-   NX-2094 (Error ORA-01476 in Oracle subagent)
-   NX-2097 (Server and agent cannot load configuration if it is a symbolic link)

# 3.9.156

-   Predefined object queries
-   LDAP synchronization filter
-   User's email and phone number synchronized with LDAP
-   Bind9 subagent rewritten in C++ and uses HTTP API
-   New NXSL function replace
-   Added `Geolocation.History.RetentionTime` server configuration parameter and geolocation history clearing by housekeeper
-   Added percentage value to pie chart
-   Added drill down object for tube and pie charts
-   Network map link color can be defined by script
-   Added method to get all tooltip data of the network map in one request
-   New NXSL functions to make web service custom requests (GET, POST, PUT, PATCH, DELETE)
-   JQ used for json parsing in web service requests
-   NXSL function `assert()` accepts second argument - diagnostic message
-   If agent configuration contains errors agent starts anyway and reports configuration load failure
-   Agent configuration tree logged on startup
-   Fixed broken "Responsible Users" object property page
-   Object management endpoints in web API
-   Source build configuration script do not throw error if libjq, libcurl, libssh, libmosquitto, or OpenLDAP are not available unless they are explicitly required
-   Cambium ePMP driver can read geo coordinates from device
-   Improved InfluxDB driver

## Fixed issues

-   NX-408 (Alarm log columns Ack by/Resolved by/Terminated by contain "admin" if not set)
-   NX-1548 (Allow monitoring of dynamic number of logs via Logwatch)
-   NX-1899 (Add description filter to Summary Table column definition)
-   NX-1903 (REST API AdHoc Summary Table - add ability to filter dci on description instead of just dciName)
-   NX-1964 (Windows installer unable to create user on MySQL 8)
-   NX-1995 (Create object endpoint for REST API)
-   NX-2030 (Use last known coordinates when re-adding node to network map)
-   NX-2046 (Get remote file fingerprint using file manager)
-   NX-2059 (Predefined object queries)
-   NX-2061 (Add changing file owner and changing file permissions functionality to file delivery policy)
-   NX-2063 (Detect conversion from group to super group in Telegram notification channel)
-   NX-2070 (Add notification log and server action execution log)
-   NX-2073 (Generate event when duplicate MAC address is detected on the network)
-   NX-2074 (DCI Table Last Value Column Widths are very large)
-   NX-2082 (File upload should support resume and consistency checks)
-   NX-2083 (Alarm list scrolls when alarms being added or removed)
-   NX-2086 (Notification channel driver for Google Chat)
-   NX-2087 (Incorrect values reported by `WindowsFirewall.State`)
-   NX-2088 (PostgreSQL driver reporting internal error "pResult is NULL in DrvExecute")

# 3.8.405

-   Fixed potential data loss in InfluxDB driver
-   Fixed invalid memory access in NXSL VM when using expression variables
-   Fixed interface counters access by agent on FreeBSD 13
-   Fixed bug in CAS server access
-   Fixed bug in report definition processing
-   Fixed server deadlock during proxy load rebalancing
-   Read system description before interface list during configuration poll
-   Separate debug tag for SMTP sender

# 3.8.382

-   New method `enable8021xStatusPolling` in NXSL class `Node`
-   Linux agent reports correct MTU for interfaces
-   Data view created for report execution only if explicitly requested in report properties
-   Fixed database upgrade issue on Microsoft SQL Server

## Fixed issues

-   NX-2048 (More information in `System.Services` table)
-   NX-2052 (nxdbmgr cannot drop orphaned TDATA tables created by older server versions)

# 3.8.366

-   Improved handling of partial or incorrect information in LLDP MIB (fixes topology building issues with MikroTik devices)
-   Fixed bug in discovering agent only nodes in remote zones
-   Fixed interface object synchronization for physical links widget
-   Fixed log name save for "Windows event log parser"
-   Removed repeat count options from "Windows event log parser" and "Syslog parser"
-   Added severity filter in Windows Event Log synchronization subagent
-   Added event and alarm on agent tunnel connection problems

## Fixed issues

-   NX-658 (Write poller statistics to debug log)
-   NX-673 (Performance Tab - missing "Stacked" and "Translucent")
-   NX-1510 (Special handling for user initiated agent restart to avoid node down or agent unreachable events)
-   NX-1589 (Error in database initialization on MS SQL 2017)
-   NX-1682 (`SYS_SCRIPT_ERROR` event is not happening when instance discovery filter script or transformation script has no closing bracket)
-   NX-1705 (DNS Lookup on Status Poll Change)
-   NX-1783 (When upgrading, agent installer asks for server IP, but does not update it in nxagentd.conf)
-   NX-1952 (Update IP address on interface to address resolved by DNS for nodes without agent)
-   NX-2040 (Periodically check if files used in file delivery policies are available on the server)
-   NX-2041 (Filter by Object ID (in Object Browser's filter) should match exact ID, not substring)
-   NX-2042 (Display EPP rule that created alarm in alarm log and alarm browser)
-   NX-2051 (Allow storing `SYS_DB_QUERY_FAILED` events to event log)
-   NX-2055 (Execution of some commands as agent actions may fail on Windows)
-   NX-2057 (Add filtering by alarm status (acknowledged, resolved) in Alarm Viewer dashboard element)

# 3.8.314

-   Database manager can detect and delete orphaned data tables
-   Event processing macro `%A` (alarm message) also works in rules following one that triggered alarm as well as when alarm is resolved or terminated by the rule
-   Fixed agent crash on log parser rule with inverted match
-   MIB compiler accepts object identifiers that starts with uppercase letter
-   Implemented hash map to string conversion in NXSL
-   Fixed save of node state
-   Web API included into Web UI installer on Windows
-   Fixed deployment issues with Web UI installer on Windows

## Fixed issues

-   NX-227 (Create "nxdownload" utility)
-   NX-553 (CPU and Memory DCI support in Darwin)
-   NX-1006 (Node with all status poll sources disabled creates a down alarm)
-   NX-1057 (Ability to execute set of SQL commands on server start)
-   NX-1473 (System Description for Agents that are also running SNMP should be Agent's description, not SNMP's)
-   NX-1851 (nxdbmgr not checking for situation when DCI present in `items`, but not in `object_properties`)
-   NX-1882 (Add option for negative mask in `File.Count`, `File.FolderCount`, and `File.Size`)
-   NX-1947 (Server repeats `SYS_IF_DOWN` after `SYS_NODE_UP` even if interface was already down before `SYS_NODE_DOWN`)
-   NX-1976 (Add interface names to automatically generated IP topology maps)
-   NX-2043 (Delete "last agent contact" timestamp when isAgent capability switches off)

# 3.8.267

-   Fixed server crash during scheduled task processing

## Fixed issues

-   NX-2009 (Add notification channel driver "Shell command")
-   NX-2035 (Instance discovery using `ICMP.Targets` list crashes server)
-   NX-2037 (Save IP address of client connecting via WebAPI to audit log)

# 3.8.262

-   Fixed server crash when accessing NXSL class metadata
-   Fixed agent crash when parsing log files
-   Fixed file handle leak in log parser subagent
-   DCI Editor filter now search by description, parameter, and DCI ID
-   Long polling can be disabled in Telegram driver
-   Fixed Log Parser Policy save with empty agent action field

## Fixed issues

-   NX-1770 (Add ability to filter by DCI name in DCI list)
-   NX-2033 (Incorrect interface name displayed in MAC address table for MikroTik routers)
-   NX-2036 (Filter in DCI editor should search both description and parameter)

# 3.8.250

-   Added notification channel driver for SNMP traps
-   Event processing macro `%K` (alarm key) also works in rules following one that triggered alarm
-   Improved Data Collection Editor and Policy Editor usability
-   DCI instance used for custom attribute lookup when expanding `%{}` macro
-   Fixed sorting for "Object query" dashboard element
-   Fixed memory leak in server related to "Object query" dashboard element

## Fixed issues

-   NX-2022 (Rack with custom height is incorrectly displayed)
-   NX-2028 (Use instance name for custom attribute search when expanding `%{}` macro)
-   NX-2029 (Line Chart General Time Period keeps reverting to "Back from now" when trying to use "Fixed time frame" option)
-   NX-2031 (HTTP proxy parameter configured in nxmc properties has no effect)

# 3.8.226

-   Lower memory footprint of NXSL scripts
-   Correct handling of agent policies by external subagents
-   Added attribute `tunnel` to NXSL class `Node`
-   Server runs configuration poll on node after agent upgrade
-   File manager subagent does not register same root multiple times
-   Fixed refresh issues in Object Details view
-   Fixed visualization issues in switch port view
-   Fixed incorrect root object filtering in dashboard elements "Event Monitor", "SNMP Trap Monitor", and "Syslog Monitor"

## Fixed issues

-   NX-2014 (Create NXSL property on node object that gives reference to each type of proxy)
-   NX-2024 (Add "Max Wait Time" to `Server.EventProcessors` Internal Parameter Table)

# 3.8.193

-   Fixed Timescale DB 2.x compatibility issues
-   New methods isDirectChild, isDirectParent, isChild, isParent in NXSL class "NetObj"
-   New NXSL function GetCurrentTimeMs
-   Fixed possible server crash when agent tunnel is closing
-   Always use UTF-8 instead of current system character encoding for exported CSV files
-   Fixed process handle leak in Windows agent when external parameter providers are used
-   Westerstrand SNMP device driver can read device geolocation
-   NXSL function PollerTrace works in autobind filter scripts and instance discovery filter scripts
-   Improved diagnostic output for manually started polls
-   Improved network map tooltip data update

# 3.8.166

-   Improved driver for H3C (now HPE) switches
-   Fixed intermittent problems with SNMP communications via proxy agents
-   Fixed multiple file download in file manager in web UI
-   Fixed excessive server memory consumption when transferring file from client to agent over slow link
-   Fixed occasional high CPU usage by server process
-   Deleted unused `job_history` table
-   Fixed graph refresh
-   Fixed object synchronization issue in web UI
-   Fixed memory leak in server
-   Fixed incorrect sorting by "Source" column in user management view
-   Fixed intermittent client disconnects
-   Fixed interface synchronization for network map element on dasbhboad

## Fixed issues

-   NX-804 (Validate scripts in all windows)
-   NX-1989 (Compile NXSL in dci instance discovery filter and container autobind filter)
-   NX-1990 (Add filter in Script Library)
-   NX-1996 (Retriggered event when node comes out of maintenance is missing value for currentValue (%4) parameter)
-   NX-2005 (Add ability to have formatting in Telegram notifications)
-   NX-2011 (NXSL inList function returns int32 instead of boolean)

# 3.8.120

-   Improved reporting server
-   Support for key based SSH authentication
-   Web service proxy function in core agent now disabled by default
-   Only HTTP and HTTPS are allowed in web service URLs
-   Context configuration removed from global log parsers configuration views in UI
-   New NXSL functions PollerTrace and SendNotification
-   New method setNamedParameter in NXSL class Event
-   Fixed bug in subnet mask correction
-   Added `Topology.RoutingTable` internal DCI table
-   Fixed bug on node creation

## Fixed issues

-   NX-1437 (Show tunnel connection time in tunnel manager)
-   NX-1775 (Add deactivation event to list of thresholds in DCI properties)
-   NX-1988 (Show full user name in user selector dialogs)
-   NX-1991 (Incorrect handling of HTTP and communication errors when collecting data from web services)
-   NX-1992 (Properly parse : in web monitoring parameter name)
-   NX-1994 (Handle multiple agents connecting back to same node)
-   NX-1999 (Make routing table available as internal table)
-   NX-2000 (Snooze timer in EPP to avoid repeating actions)
-   NX-2001 (Add ability to put trace messages from hook scripts to text output of status/conf/etc poll)
-   NX-2004 (`/objects/<container_id>` REST API endpoint against container object returning error 46 - multiple JSON fields named flags)

# 3.7.145

-   Fixed bug in interface and subnet creation hook scripts handling

# 3.7.144

-   Target for event processing policy remote action can be given as node object ID
-   New agent metrics:
    -   `Agent.TCPProxy.IsEnabled`
    -   `Agent.TCPProxy.ConnectionRequests`
-   Fixed bug in agent action execution from event processing policy
-   Fixed incorrect boolean values handling in NXSL
-   Fixed bug in "Find switch port" tool
-   Fixed server crash when connection to agent is slow or unstable

# 3.7.130

-   Per node SSH port configuration
-   New user properties "email" and "phone number"
-   Fixed broken reporting server connector

## Fixed issues

-   NX-1081 (Some devices are not detected correctly by CATALYST-GENERIC driver)
-   NX-1663 (NXSL function `GetDCIValue` should read value from database if cache is not populated yet)
-   NX-1965 (Inconsistencies in address range add/edit dialog)

# 3.7.116

-   New methods `appendAll` and `insertAll` in NXSL arrays
-   DCI transformation test can be run from template data collection configuration
-   Fixed bug in remote agent configuration update
-   Fixed bug in object selection dialog in UI
-   Fixed server hang on shutdown if initiated from remote GUI session

## Fixed issues

-   NX-1875 (Error message is not cleared in list of notification channels)

# 3.7.95

-   UI framework updated to Eclipse 4.17 / RAP 3.14
-   Improved clipboard support in web UI
-   Improved access control logic for enter/leave/schedule maintenance
-   Improved generic Cisco driver
-   Improved support for Cisco Nexus switches
-   Added command line tool `nxaevent` for sending events to server via local agent
-   New agent parameter `Agent.IsRestartPending`
-   Default DCI instance retention time changed to 7 days
-   Container auto bind and template auto apply for sensors, mobile devices, and access points is configurable and off by default
-   Explicit boolean data type in NXSL
-   NXSL regular expression matching operator returns boolean `false` instead of `null` value if there is no match
-   New method `setIfXTableUsageMode` in NXSL class `Node`
-   New methods enableAgentStatusPolling, enableICMPStatusPolling, and enableSNMPStatusPolling in NXSL class "Interface"
-   SQL query trace in server can be enabled independently from global debug level and changed at runtime
-   Fixed unrecoverable "objects out of sync" state on client
-   Fixed issues with file following

## Fixed issues

-   NX-770 (Instance discovery poll a node when an instance DCI is added)
-   NX-790 (Ability to disable 802.1x checking)
-   NX-1058 (Repeat event in DCI threshold may not be generated if repeat interval is the same as polling interval)
-   NX-1173 (Add bulk DCI update functionality)
-   NX-1469 (Show warning to user on attempt to force poll node in unmanaged state)
-   NX-1602 (Option to disable ICMP poll for individual child Interface objects)
-   NX-1623 (DCI > "Clear collected data" should refresh Last Values)
-   NX-1654 (NXMC slow when container or template with many nodes is expanded)
-   NX-1948 (Create nxaevent utility similar to nxapush)
-   NX-1956 (Allow applying templates to Access Points)
-   NX-1975 (Per DCI multiplier settings)
-   NX-1983 (Add automatic bind rules for clusters)
-   NX-1984 (File delivery policy incorrectly handles Russian letters)
-   NX-1985 (File name is cleaned on save in GUI log parser policy editor)

# 3.6.300

-   Fixed bug in object tool filter configuration
-   Fixed bug in map image save
-   Fixed handling of tunnel options in Windows agent installer unattended mode

## Fixed issues

-   NX-1520 (Object Details - Overview tab in desktop client is unusable when using dark gtk3 theme)
-   NX-1881 (Unable to open web browser from object tools for nodes have IPv6 address returned from DNS)
-   NX-1906 ("Save Resources" keeps on showing when closing the console)
-   NX-1943 (Dashboard element in 2nd column does not spans correctly)
-   NX-1944 (Add macro that will return all tags of event in concatenated form)
-   NX-1969 (Create default interface if node replies via SNMP, but provides empty interface list)
-   NX-1978 (Cleanup configuration and status poll textual output)
-   NX-1980 (Object Tools input field display name to wrap or input dialog to resize)
-   NX-1981 (Unable to create new DCI when filter is not empty in Data Collection Configuration)
-   NX-1982 (Export Configuration Tool - Unable to remove items from "Actions" and "Event Processing Rules")

# 3.6.273

-   New NXSL function `PostEventEx`
-   Origin timestamp can be set when event is being sent via Java API
-   Fixed server memory leak and high CPU usage when using "server command" type object tools

# 3.6.269

-   Fixed memory leak in server

# 3.6.264

-   Fixed bug in agent connection setup via proxy

# 3.6.262

-   Fixed bug causing random client and agent timeouts
-   Fixed bug in database upgrade procedure
-   Fixed bug in nxdbmgr reset-system-account

## Fixed issues

-   NX-1977 (NXSL `GetDCIValues()` does not work on TimeScaleDB)

# 3.6.252

-   Object categories
-   Support for externally provisioned agent certificates
-   New instance discovery method "internal table"
-   Added option to validate server certificate on agent
-   Fixed column sorting in Web Service Definition view
-   Support for IPv6 in NXSL functions AddrInSubnet and AddrInRange
-   New NXSL function GetServerQueueNames
-   New NXSL functions for object search: FindObjectByGUID, FindNodeByAgentId, FindNodeByIPAddress, FindNodeByMACAddress, FindNodeBySysName
-   nxdbmgr option to migrate log tables in background
-   Windows event log synchronization, server side parsing and agent side filtering
-   Added option not to save to database Windows event log and syslog filtered by server parser
-   Maximum number of client sessions can be configured
-   Added support for SNMP data types `FLOAT`, `DOUBLE`, `INTEGER64`, `UINTEGER64`
-   Correct decoding of values inside OPAQUE SNMP varbinds
-   Added view for object tools with output executed on multiple nodes
-   Added synchronous methods and completion callbacks for object creation in Java API
-   Fixed nxdbmgr crash on import
-   New built-in agent action `Agent.RotateLog`
-   Server performance optimization for handling large number of agent connections
-   Performance optimization of SNMPv3 processing
-   NXSL performance optimization
-   Improved handling of external parameter providers in agent
-   Added background polling option for external tables in agent
-   Authentication method for LDAP users can be changed
-   Support for mobile devices with NTCB/FLEX protocol
-   Geolocation control for nodes, sensors, and mobile devices
-   Fixed screenshot issues on Windows 10 with DPI scaling
-   Fixed errors on graph properties modification
-   Fixed sorting in summary table when one column has different data types

## Fixed issues

-   NX-904 (Sensitive info should be hidden in Audit Log)
-   NX-1294 (Completed Scheduled Task Re-scheduling)
-   NX-1360 (Add ability to set custom icon for node)
-   NX-1416 (NetXMS Agents shutdown does not end ExternalParametersProviders)
-   NX-1823 (Using SSH login and password in object tools)
-   NX-1905 (Log Parser policy in Template Agent Policies does not automatically include Events in Export Configuration Tool)
-   NX-1907 (Add server configuration option to disable outdated SSL/TLS versions)
-   NX-1911 (Separate object name for use on maps)
-   NX-1931 ("Do not store" option for syslog)
-   NX-1933 (Update descriptions and units for server configuration variables)
-   NX-1951 (Moving a DCI to container deletes the DCI)
-   NX-1962 (Save time of last configuration poll across server restart)

# 3.5.152

-   Fixed agent crash on thread pool statistic access

# 3.5.133

-   Fixed server deadlock when unreachable node is deleted
-   Fixed SNMPv3 performance issue

## Fixed issues

-   NX-1966 (MySQL / MariaDB database access performance issues)

# 3.5.125

-   Fixed network map filter script read form database
-   Fixed server crash

## Fixed issues

-   NX-1928 (nxdbmgr export/import does not work properly with TimescaleDB)
-   NX-1930 (NodeJS POST requests to NetXMS WebAPI fail with http error 500 internal error / error 46)
-   NX-1953 (Migration from MySQL to TimescaleDB fails)
-   NX-1960 (Instance discovered tables not removed after template removed)

# 3.5.90

-   Added support for parallel event processing
-   Improved SNMP proxy performance
-   Support for SHA-2 based authentication in SNMP (SHA224, SHA256, SHA384, SHA512)
-   Roaming mode for server
-   Access to NXSL object's class metadata via `__class` attribute
-   Access to NXSL object's attributes via `__get` method
-   Invoke NXSL object's methods via `__invoke` method
-   Added `Hook::UnboundTunnelOpened` and `Hook::BoundTunnelOpened` NXSL hooks
-   Added per node trap flood detection
-   New event processing macros `%z` (zone UIN) and `%Z` (zone name)
-   Added `Topology.WirelessStations` and `Topology.SwitchForwardingDatabase` internal table metrics
-   Option to disable reading of Windows performance counters metadata on configuration poll
-   Alias (secondary name) for all network objects
-   Wildcards in nxdbmgr "get" command
-   Fixed modification flag for "Break" and "Action" fields in log parser policy
-   NXSL attribute `cipVendorCode` and methods `readInternalParameter`, `readInternalTable` are added to class `Node`
-   Added cluster object itself to event log filter opened on the cluster
-   Removed the limitation of one object for "Move to another container" action
-   Implemented `/alarms/{alarm-id}` path for REST API
-   Templates exported without GUID are assigned new GUID on import
-   Support for non-ASCII database and login names in PostgreSQL driver

## Fixed issues

-   NX-1594 (Alias (secondary name) for all network objects)
-   NX-1841 (Option to enumerate all attributes and methods of an object in NXSL)
-   NX-1879 (Unmanaged automatic network map is no more auto updated)
-   NX-1883 (Execute server script should allow to specify script parameters (those that are accessible via $ARGS))
-   NX-1884 (Do not show error while node is added to the cluster if the node is already there)
-   NX-1893 (Internal parameter to count total number of bound agent tunnels)
-   NX-1904 (REST API for specific node alarms returns Internal error 46)
-   NX-1908 (Expose FDB to NXSL)
-   NX-1914 (Removed deprecate `AllowDirectNotifications` server configuration setting)
-   NX-1919 (Internal parameters to count number of tunnels with agent, snmp, snmp trap, syslog proxies or with installed user agents)
-   NX-1924 (When importing event that has different GUID but matching name with already existing event, treat it as new event and give it a new name)
-   NX-1932 (DCI status in Template is not carried over in Export Configuration)
-   NX-1942 (Add property to actions in EPP "Do not run if timer is active")
-   NX-1945 (Memory leak in user support application when taking screenshots)

# 3.4.318

-   Fixed bug with interface tab display in UI

# 3.4.314

## Fixed issues

-   NX-1940 (AIX subagent may report incorrect file system size)

# 3.4.313

## Fixed issues

-   NX-1938 (Changes in user groups are not saved to database)

# 3.4.310

-   Added driver for SAF Tehnika Integra devices
-   Improved handling of UNICODE characters in external parameter output on Windows
-   Fixed UI crash when object query dashboard element is incorrectly configured

## Fixed issues

-   NX-1916 (Device could be marked as supporting ENTITY MIB when it is in fact not supported)
-   NX-1921 (SQL query failed into alarm\_events: 22001 ERROR: value too long for type character varying(2000))
-   NX-1922 (Spelling mistakes in Java API)
-   NX-1920 (Save deleted DCIs between restarts to delete it's data on housekeeper after restart)

# 3.4.284

-   PostgreSQL monitoring subagent
-   Improved driver for Cisco Nexus
-   Improved LLDP based network topology discovery
-   Correctly detect LLDP capability on MikroTik devices
-   New NXSL functions `GetServerNode` and `GetServerNodeId`
-   New NXSL function `SendMail`
-   Fixed UI bug with accessing collected performance data from data collection editor
-   Configurable size of SNMP proxy thread pool on agent
-   Housekeeper optimization
-   Added drivers for Cambium Networks devices (ePMP and cnPilot)

## Fixed issues

-   NX-498 (PostgreSQL monitoring sub-agent)
-   NX-1355 (Housekeeper process causing timeouts when creating new nodes)
-   NX-1863 (Logwatch fails on parsing large Windows Event Log events)
-   NX-1880 (Duplicate links on automatic maps with multiple seed nodes)
-   NX-1895 (After server restart GUI is not showing from where a custom attribute is inherited)
-   NX-1897 (ReadPersistentStorage returns incorrect value for non-existing key)
-   NX-1901 (Get node of active NetXMS server in NXSL)
-   NX-1910 (Spelling mistakes in Java API)

# 3.4.232

-   Improved logic for node capability expiration
-   "Reset identity" command line option in agent
-   EtherNet/IP has priority over SNMP when reading hardware information
-   Implemented Web API calls for DCI creation and modification
-   Implemented Web API calls for reading last value of specific DCI
-   NXSL function CreateDCI accepts numeric codes for data type and data origin
-   Improved node matching for agent tunnel automatic binding
-   Fixed bug that prevents PushDCIData NXSL function to work on chassis object
-   Fixed bug in template import

## Fixed issues

-   NX-1422 (SMTP HELO should be configurable)
-   NX-1886 (DCI Table using Script Origin ignores Column definition)
-   NX-1888 (Delete completed non-recurring scheduled tasks after configurable retention period)
-   NX-1890 (Object Name field in Create Node Object requires cleaning)
-   NX-1892 (Wrong format string on a map makes the map uneditable)

# 3.4.178

-   Improved topology based event correlation
-   New methods in NXSL class `Node`: `getInterfaceByIndex`, `getInterfaceByMACAddress`, `getInterfaceByName`
-   Method getInterface in NXSL class `Node` automatically detects if parameter is interface index, name, or MAC address
-   Added built-in NXSL constant `NXSL::SystemIsBigEndian`
-   Added NXSL hook for alarm state change (Hook::AlarmStateChange)
-   Can pass arguments to NXSL script executed as EPP action
-   Implemented agent metrics for available and cache memory on AIX
-   New agent parameter `WindowsFirewall.State` on Windows
-   Implemented disk latency parameters in Linux agent (`System.IO.WaitTime`, `System.IO.ReadWaitTime`, `System.IO.WriteWaitTime`)
-   User agent tooltip message can be set via policy

## Fixed issues

-   NX-470 (Hooks or events for alarm state change)
-   NX-763 (File Tail/Show should not access database directly)
-   NX-811 (`System.IO.WaitTime` unsupported on Linux)
-   NX-1043 (Windows installer cannot initialize Oracle database)
-   NX-1078 (Event correlation not working)
-   NX-1152 (Attempt to upload .npi pointing to non-existing installer lock up package manager on Windows)
-   NX-1176 (Handle routing loops during event correlation)
-   NX-1524 (Server configuration wizard is not visible on task bar)
-   NX-1556 (Add HMAC to every record in audit log table)
-   NX-1566 (NXSL Script Action to allow for parameters)
-   NX-1739 (When a node goes down and it's upstream port on a switch goes down, do not correlate those events)
-   NX-1753 (File downloads from agent and file upload to server should be logged to Audit Log)
-   NX-1801 (Strange if condition)
-   NX-1818 (Agent should remember servers for a specified time to send events when server reconnects)
-   NX-1832 (Export configuration does not detect referenced NXSL scripts within NXSL scripts)
-   NX-1837 (Store out of the box object tools as .xml files, not in database initialization script)
-   NX-1846 (Server crash when querying Audit Log)
-   NX-1848 (Add getGuid method to org.netxms.client.events.EventTemplate class in Java API)
-   NX-1853 (User Agent Notifications view in management console has no means to hide old notifications)
-   NX-1854 (When double-clicking a stacked graph in performance tab, it opens in a new view as non-stacked)
-   NX-1856 (Text in tooltip for user support application should be configurable)
-   NX-1860 (Parameters to get state of each Windows Firewall profile separately)
-   NX-1861 (Unable to add USM Credentials when zoning is ON)
-   NX-1862 (Lazy object synchronization breaks object-based link status display on maps)
-   NX-1865 (Remote Node using TLS Tunnel Added incorrectly if same name is resolvable on local NetXMS network)
-   NX-1866 (NXSL GetAvgDCIValue may not work with MySQL database)
-   NX-1867 (NXSL GetMaxDCIValue may return incorrect value)

# 3.3.350

-   Replace backslash and comma as part of host and DCI names normalizing in InfluxDB driver
-   Fixed bug in socket error reporting for agent tunnels
-   Fixed VMGR subagent crash
-   Fixed bug in agent policy deployment in 2.x compatibility mode
-   Fixed bug in database export

## Fixed issues

-   NX-1696 (Database export error)
-   NX-1868 (Zone SNMP Configuration SNMP v3 "Modify" button spelt incorrectly)
-   NX-1869 (Environment variables in file delivery policy expanded on save)

# 3.3.340

-   Fixed bugs in SIP registration testing in Asterisk subagent
-   Fixed memory leak in Asterisk subagent

# 3.3.330

-   Fixed issue NX-1855 (`NETXMS_FILE_STORE` environment variable not using FileStore agent setting)

# 3.3.323

-   Fixed bug in template import on server startup

# 3.3.315

-   Fixed server crash on agent certificate renewal

# 3.3.314

-   Fixed server crash when proxied SNMP device responds with "UDP port unreachable"

## Fixed issues

-   NX-1575 (Ability to duplicate event configuration)
-   NX-1780 (Unable to add file to file delivery policy in management console on MacOS)
-   NX-1839 (Show alarm key in Alarm Details)
-   NX-1844 ('Get list of agent sessions' error in nxmc and webui)
-   NX-1845 (Context menu for Service Root shows Create sensor twice)

# 3.3.305

-   Added driver for Moxa industrial routers
-   Fixed server crash when receiving ill-formed SNMP response
-   Fixed server crash when accessing zone object attributes from NXSL

## Fixed issues

-   NX-1849 (Agent policy schema sqlite error in 3.3.285)

# 3.3.285

-   Fixed server crash after scheduled task delete
-   Fixed web UI login screen issues

# 3.3.277

-   Option for blacklisting network device drivers
-   Option for switching SNMP probing during configuration poll into single OID per request mode
-   Automatic agent certificate renewal
-   Value ranges in NXSL switch/case statement
-   Explicit call of library functions in NXSL without "use" statement
-   New attributes `instanceColumns` and `instanceColumnIndexes` in NXSL class `Table`
-   New methods `readWebServiceList` and `readWebServiceParameter` in NXSL class `Node`
-   New methods `applyTemplate` and `removeTemplate` in NXSL class `DataCollectionTarget`
-   New NXSL functions: `GetThreadPoolNames`, `sqrt`
-   New NXSL class `Template` that represents template object
-   NXSL arrays can be implicitly converted to strings
-   Implemented instance discovery method "Agent Table"
-   Implemented instance discovery method "Windows Performance Counters"
-   Added option for discarding collected performance data when database writer queue grows beyond limit
-   Using `timestamptz` instead of integer for timestamp column in data collection tables on TimescaleDB

## Fixed issues

-   NX-392 (Use object names from Windows performance counters for instance discovery)
-   NX-713 (Scheduled DCI will not work with offline DCI functionality)
-   NX-806 (NXSL: add method to lookup table row by instance)
-   NX-807 (NXSL: add method to lookup instance column ID without iterating over Table::columns)
-   NX-814 (NXSL: add new node attribute – isRemotelyManaged)
-   NX-1362 (Pattern matching for command output in `SSH.Command` parameter)
-   NX-1511 (Save and display user ID of maintenance mode initiator)
-   NX-1699 (Allow user turn on "Prevent automatic SNMP configuration changes" when creating node)
-   NX-1729 (L2 maps get broken after server restart - all icons get coordinates (0, 0))
-   NX-1732 (Option for discarding collected performance data when database writer queue grows beyond limit)
-   NX-1765 (HTML codes visible in cell when viewing Table DCI last values in web management console)
-   NX-1771 (Add NXSL constants)
-   NX-1788 (NXSL: add support for ranges in switch/case)
-   NX-1793 (Out of range error)
-   NX-1806 (Change order in which ping3.ndd is used during discovery or allow unloading/blacklist)
-   NX-1807 (TimescaleDB continuous aggregates, retention policies, etc.)
-   NX-1671 (Title from Object Tool's properties is not used anywhere)
-   NX-1808 (Template may not appear in object tree on import)
-   NX-1820 (Object deletion and negative reference count)
-   NX-1824 (Physical links - access denied)
-   NX-1827 (Maintenance mode filter in dashboard element "Status Map")
-   NX-1828 (Windows agent returns error for parameters `System.FirewallProduct.*` if built-in Windows Firewall is used)
-   NX-1830 (Some events sent by agent may be lost if multiple events sent almost simultaneously)
-   NX-1831 (Template path in node data collection configuration is incorrect)
-   NX-1834 (Add NXSL function `sqrt`)
-   NX-1836 (Access attributes of template in auto-bind script)
-   NX-1840 (Ability to set communication option "this is address of remote management node" during node creation)
-   NX-1842 (Generate event when housekeeper process has started and finished)

# 3.2.472

-   Improved alarm browser performance when displaying big number of alarms
-   Fixed memory leak in server
-   Fixed issue NX-1821 (Scheduled Task script not accepting parameters)

# 3.2.462

-   Fixed bug in thread pool manager that can cause start of excessive number of threads
-   Additional SSL trace output in agent

# 3.2.451

-   Internal parameters for monitoring syncer performance (`Syncer.RunTime.*`)
-   Improved notification handling in user support application
-   Allow usage of chat ID as recipient address for Telegram
-   Support for standard SSH configuration file in SSH subagent
-   Environment variables from agent configuration file also set for user agent processes
-   Improved hypervisor type detection by agent
-   Tunnel option can be turned on in Windows agent installer
-   Fixed issues with hardened file system permissions in Windows installer
-   Added SMBIOS parameters support on FreeBSD

## Fixed issues

-   NX-1635 (Log parser can skip lines in a log file)
-   NX-1737 (User Agent Startup and Recurring Notifications not working)
-   NX-1810 (Server can cash if scheduled task deleted while running)
-   NX-1812 (In the WebUI Filter in Alarm browser hiding column headers and first row when resized)
-   NX-1814 (Values of internal parameters `Server.QueueSize.Average` and `Server.QueueSize.Current` are inconsistent)
-   NX-1815 (FDB cannot be read on certain Cisco switches)
-   NX-1816 (Removing node from cluster crashes server)
-   NX-1817 (Log file can be read twice after rotation by log parser on Windows)
-   NX-1819 (NXSL methods `NetObj::bindTo()` and `NetObj::unbindFrom()` crash server when given `null` as parameter)

# 3.2.400

-   Proxy nodes does not collect DCI data from SNMP nodes marked as down
-   Configurable address block size and inter-block delay for active network discovery
-   Fixed server memory leak in instance discovery code
-   Fixed broken `Net.ArpCache` and `Net.IP.RoutingTable` lists in Linux agent

## Fixed issues

-   NX-791 (CPU Count DCI not supported on HP-UX)
-   NX-1440 (After netxmsd restart custom schedule DCIs does not have value)
-   NX-1607 (Primary IP address should not be used for topology if it is not present on any interface)
-   NX-1768 (Server configuration variable `Objects.Interfaces.UseAliases` has no options to select)
-   NX-1773 ("Apply policy" in context menu of node is meaningless and does nothing)
-   NX-1803 (Configuration import with "Replace existing object tools" checkbox set does not replace them)

# 3.2.380

-   New attribute `primaryHostName` in NXSL class `Node`
-   Fixed memory leak in log parser subagent
-   Internal metric `Server.MemoryUsage.DataCollectionCache` fixed
-   Fixed broken Windows Event Log monitoring in logwatch subagent

## Fixed issues

-   NX-1794 (Problems with map decorations selection)
-   NX-1798 (Incorrect default EIP port number)
-   NX-1799 (Login name is limited to 13 characters if CAS is used)
-   NX-1800 (If CAS response contains proxy information ticket is always rejected)

# 3.2.350

-   Data collection from web services
-   Nodes within chassis and chassis view
-   EtherNet/IP device discovery
-   Image library management completely rewritten
-   Maximum password length supported by nxencpasswd increased to 64 characters
-   Removed support for ancient custom CheckPoint SNMP agent on port 260
-   Added option to control case sensitive matching in log parser rules
-   New internal parameters for server stats (object count, alarm count, etc.)
-   Method `setMapImage` of NXSL class `NetObj` now accepts `null` value as "reset to default" indicator

## Fixed issues

-   NX-50 (Allow per-DCI SNMP version settings)
-   NX-58 (Refactor Image Library)
-   NX-896 (Display blade chassis and servers in rack)
-   NX-1476 (NetXMS Server crashes when sending alarm summary email)
-   NX-1523 (Store object creation time)
-   NX-1525 (Use HTTP response data as DCI value)
-   NX-1720 (Merge Support App Agent Policy menu items)
-   NX-1724 (Implement agent parameters for inode usage)
-   NX-1741 (Node placement within chassis)
-   NX-1748 (User agent should check on startup if it is already running in same session)
-   NX-1750 (Configurable retention time for node hardware and software components)
-   NX-1754 (HTTPS and SOCKS proxy options in Telegram channel configuration)
-   NX-1767 (File manager may be unable to access file with percent sign in name)
-   NX-1781 (Process launched by ExternalParametersProvider inherits file handles of agent process)
-   NX-1782 (Windows installer offers generic.sms SMS driver, while the server is now reworked to have notification channels)
-   NX-1792 (Unable to use script with parameters for instance discovery)
-   NX-1796 (WebUI and REST API not connected securely to the NetXMS server)

# 3.1

-   Added physical links inventory for node interfaces and patch panels
-   Can enable usage of ICMP ping on primary IP address during status poll
-   Macro expansion in DCI polling interval and retention time values
-   New attribute `isInMaintenanceMode` in NXSL class `NetObj`
-   New attribute `downSince` in NXSL class `Node`
-   New attributes `dci` and `dciId` in NXSL class `Event`
-   New method `forcePoll` in NXSL class `DCI`
-   New NXSL functions `ExpandString` and `LoadEvent`
-   New methods `correlateTo` and `expandString` in NXSL class `Event`
-   New method `expandString` in NXSL class `NetObj`
-   New hook `Hook::EventProcessor` that is called for each event before passing it to EPP
-   New NXSL function `atan2`
-   Added global array `$ARGS` in NXSL scripts for simplified access to script arguments
-   Added NXSL constants `NXSL::VERSION` and `NXSL::BUILD_TAG`
-   Interface object names can be expanded from actual interface names using macros
-   Notification channel driver for Telegram
-   Notification channel driver for Microsoft Teams
-   File delivery policies for agents
-   Improved automatic IP topology maps
-   Added custom attributes inheritance
-   Web UI properties can be set via JNDI
-   Improved LLDP based network topology discovery

## Fixed issues

-   NX-366 (Generate event if duplicate IP address found)
-   NX-848 (API for modules to register new console commands)
-   NX-910 (`System.IO.DiskQueue(*)` doesn't support instances for Windows)
-   NX-1030 (Telegram bot integration)
-   NX-1462 (Add "File Policies" to push files/scripts out to agents)
-   NX-1550 (Not all internal queue sizes exposed as internal server parameters)
-   NX-1634 (Possible for `NDF_QUEUED_FOR_INSTANCE_POLL` flag to get stuck)
-   NX-1649 (NXSL functions or object methods for SSH interactions)
-   NX-1653 (Global user access rights are not updated in sessions)
-   NX-1668 ("Execute server script" appears in context menu in object tools configuration)
-   NX-1674 (Initiate DCI forced poll from NXSL)
-   NX-1675 (Context menu for containers and "Service Root" shows "Create sensor" twice)
-   NX-1681 (In NetXMS console refresh from view pull-down menu is not working on Data Collection Configuration)
-   NX-1686 (User Agent system tray menu covered by Windows system tray expanded hidden icon menu)
-   NX-1687 (User agent system tray menu closes when you click out of it)
-   NX-1691 (Network map link bend points seem a bit broken in 3.0)
-   NX-1694 (Russian language problem in Windows log)
-   NX-1706 (Compose interface name from the actual name and a suffix)
-   NX-1708 (Event tags in log file monitoring are not represented in UI)
-   NX-1710 (Add serialized to json event to event log)
-   NX-1712 (Add support for reading WMI query result as list or table)
-   NX-1713 (Object tool for container should be shown if it can be executed on at least one node)
-   NX-1717 (Alarm pop-ups appear only on console start, afterwards are not shown)
-   NX-1718 (Send user agent notification on container)
-   NX-1719 (File monitoring with rescan is not matching text past 4KB of the monitored file)
-   NX-1725 (LDAP attribute names should be case insensitive)
-   NX-1726 ("Tools" and "Graphs" menu items missing in object context menu on world map)
-   NX-1728 (No error description in poller output when configuration or status poll for a node cannot connect to NetXMS agent)
-   NX-1731 (NXSL method Node::readAgentList causes NetXMS server crash)
-   NX-1735 (`Agent.SessionAgentCount` returning incorrect value)
-   NX-1740 (When macro is used in threshold, it's value does not get expanded in event)
-   NX-1746 (Auto start user agent/support app process after agent install/upgrade)
-   NX-1749 (User Agent menu stay on top)
-   NX-1750 (Configurable retention time for node hardware and software components)
-   NX-1751 (DS18X20 on RPi erroneously writes to log "Unable to add sensor from configuration file...")
-   NX-1755 (In object tool `command` in file name truncates last char of command output)
-   NX-1758 (Typo in management console)
-   NX-1759 (Setting environment variable from `[ENV]` section in agent config does not work on Windows)
-   NX-1760 (Use folder specified by `--sysconfdir` instead of `--prefix` for configuration file search)
-   NX-1761 (Object script executor prints last output line after error message)
-   NX-1769 (Windows agent may crash if invalid strftime format character used in log parser file name specification)
-   NX-1784 (Software inventory - failed SQL queries)

# 3.0

-   SMS drivers replaced by notification channels
-   Agent policies were merged with templates
-   Event tags
-   ICMP polls for collecting ICMP response time statistic on server side
-   User agents (desktop support application)
-   Raw DCI values saved in history along with corresponding transformed values
-   New DCI data types - "32 bit counter" and "64 bit counter"
-   Collected DCI data recalculation based on stored raw values and current transformation settings
-   Agent always requires encryption unless RequireEncryption parameter explicitly set to off
-   Default values for missing custom attributes in macros (in form %{attr:default})
-   Support for macros in threshold values
-   Improved network discovery filter script capabilities
-   Internal server parameters for counting client sessions
-   New hook script UpdateInterface
-   Node creation option "create as zone proxy"
-   JSON support in NXSL
-   Improved NXSL performance
-   Null values interpreted as `false` in NXSL logical expressions
-   Added method `executeSSHCommand` in NXSL class `Node`
-   Cleanup of collected DCI data by housekeeper can be disabled
-   Service group support in Tuxedo subagent
-   Improved Enduro/X compatibility
-   Improved Cisco Aironet (former Airespace) driver
-   Added driver for Cisco Nexus switches
-   Duplicate IP address detection during network discovery
-   Improved I/O performance parameters in Windows agent
-   Optional JSON format for log files
-   Option to use stdout as log output device
-   Switched to pcre (from libtre) as regular expression matching engine
-   Event parameters exposed as writable `Event` class attributes in NXSL
-   New method `addParameter` in NXSL class `Event`
-   Some bit fields in NXSL classes (most notably flags in Node class) had changed their meaning
-   "Origin timestamp" for events
-   Object management functions in NXSL implemented as object methods
-   SNMP functions in NXSL implemented as transport methods
-   Range access for strings and arrays in NXSL via [:] operator
-   Access to VLAN information from NXSL
-   Object tool type "Agent Table" now used to read agent tables and "Agent List" to read agent lists
-   New agent parameter `Agent.SNMP.Traps`
-   Windows installer sets hardened file system permissions
-   Event `SYS_SCRIPT_ERROR` generated for instance discovery filter script compilation errors

## Fixed issues

-   NX-69 (Driver for Cisco Nexus)
-   NX-183 (Implemented responsible users for objects)
-   NX-415 (Oracle db driver drops connection on "password will expire" warning)
-   NX-725 (Add alarm comments from NXSL)
-   NX-782 (Better handling of counter resets and delta calc)
-   NX-900 (Server started during nxdbmgr check forced repair)
-   NX-1021 (Add event `SYS_SERVER_STARTED`)
-   NX-1102 (Implement event groups)
-   NX-1199 (SNMP credentials per-zone)
-   NX-1219 (Add "created" and "last login" columns to User Manager)
-   NX-1271 (Implement internal server topology map)
-   NX-1307 (After a node is deleted, its tunnel can't be unbound)
-   NX-1386 (Implement units for server variables)
-   NX-1426 (Transformation scripts for SNMP traps)
-   NX-1479 (DCI poll spread after NetXMS server/service restart)
-   NX-1562 (Add "tunnel only" option to node's agent communication configuration)
-   NX-1601 (Log Policy editor can't parse xml with unknown event code)
-   NX-1643 (Extra parameters for event generated by log parser)
-   NX-1679 (FreeBSD subagent fails to build on FreeBSD 12.0-RELEASE)
-   NX-1680 (In DCI Properties -> Instance Discovery when method=Script there is no label for script name field)
-   NX-1690 (UPS subagent parameter `UPS.OnlineStatus` is not working for devices with Megatec protocol)
-   NX-1702 (Windows installer install binaries with world-writable permissions and can be replaced by user)
-   NX-1703 (Agent policy list does not get updated when creating new policy)
-   NX-1704 (When removing node from template, log parsing agent policy stays on that node)

# 2.2.17

-   Fixed multiple MQTT broker connection support
-   Java 12 supported by reporting server
-   Fixed bug in agent file download to UI
-   Implemented per-device I/O counters on Windows
-   Fixed bugs in TCP proxy
-   Added object filtering by zone in REST API
-   Fixed server crash when using "SSH" or "device driver" DCI source

# 2.2.16

-   Improved systemd integration
-   Agent table `System.InstalledProducts` supported on AIX and FreeBSD

## Fixed issues

-   NX-857 (Server should send SNMP timeout to proxy agent)
-   NX-869 (nxevent sometimes hangs after sending event)
-   NX-1606 (DefaultInterfaceExpectedState - wrong values)
-   NX-1624 (Add "for the last minute" to description of `Icmp.*` per-minute agent parameters)
-   NX-1633 (Add option to "nxdbmgr export" which will skip selected tables)
-   NX-1646 (Agent can't start with invalid entry in the configuration file)
-   NX-1651 ("Thresholds" not updating live)
-   NX-1655 (Agent's parameters for network interfaces always return error on Solaris 11)

# 2.2.15

-   Improved driver for Cisco Small Business switches

## Fixed issues

-   NX-1609 (Duplicate server configuration parameters)
-   NX-1627 (Proxy node should not ping through itself)
-   NX-1637 (Unrecognized Cisco SG Switch)
-   NX-1639 (NXSL persistent storage entries not saved in database)
-   NX-1644 (DB gets corrupted when adding container/nodes)
-   NX-1645 (Broken UI element layout in table DCI "General" property page)

# 2.2.14

-   Local cache on agent side for data pushed with nxapush
-   Support for statsite sink format in nxapush
-   Updated default MIB collection
-   nxget command line option to print table as delimited text
-   Drill down dashboard or network map for "Gauge" dashboard element
-   Added trigonometric functions (`sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `sinh`, `cosh`, `tanh`) to NXSL
-   Improved configuration import
-   Implemented parameter `Process.WkSet` on AIX
-   Additional system information parameters on Windows
-   Added NXSL hook for subnet creation
-   Interface object properties can be changed inside interface creation hook
-   Improvements in web service API
-   Support for migration to and from TimescaleDB in nxdbmgr

## Fixed issues

-   NX-1537 ("Hidden" flag for DCI)
-   NX-1574 (Add `hasActiveThreshold` attribute/method to DCI object accessible in NXSL)
-   NX-1576 (Add `$2` to instance DCI script hint)
-   NX-1577 (Server configuration parameter `TopologyExpirationTime` renamed to `Topology.AdHocRequest.ExpirationTime`)
-   NX-1580 (Updated FOUNDRY MIB // Updated CPQHOST MIB)
-   NX-1586 (Comments field when putting node into maintenance mode)
-   NX-1588 (Object load error can cause server crash)
-   NX-1590 (SecondsToUptime function: Incorrect display in some cases)
-   NX-1593 (Create separate access right for configuration import)
-   NX-1603 (Windows Server 2019 is being detected as Windows Server 2016)
-   NX-1604 (ICMP sub-agent automatic targets may be deleted immediately after creation)
-   NX-1605 (MariaDB driver - TLS connections don't work)
-   NX-1608 (Support for PtP subnets /31 and /127)
-   NX-1614 (Improvements to DNS monitoring / resolving)

# 2.2.13

-   TimescaleDB supported as backend database
-   Added option to show SELECT output in nxdbmgr batch
-   New attribute `parameterNames` in NXSL class `Event`
-   New attribute `instanceData` in NXSL class `DCI`
-   Added option to play alarm notification sound only for active dashboard
-   Required object access is "read" for all forced polls except full configuration poll which requires "modify" access
-   Improved server startup and shutdown time
-   Added option to save network map as image file
-   New nxmc command line options `-take-map-snapshot` and `-exit-after-open`
-   Access to dependent nodes list from NXSL and Java API

## Fixed issues

-   NX-241 ("nxdbmgr batch" should support stdin)
-   NX-887 (Additional variables in threshold script)
-   NX-1388 (Event correlation route should start at proxy)
-   NX-1536 (No output from forced status poll without "modify" object access right)
-   NX-1552 (NXSL function to check for EPP timer existence)
-   NX-1558 (Add ability to change node's comment from script)
-   NX-1561 (Unexpected `SYS_SNMP_DOWN` events after SNMP proxy node restart)
-   NX-1567 (EPP selection gets stuck)
-   NX-1569 (Agent crash on 32 bit Windows 10)
-   NX-1571 (Option to automatically terminate resolved alarms after timeout)

# 2.2.12

-   Added support for active network discovery in remote zones
-   Database manager options to skip various logs during database export also works for database migration

## Fixed issues

-   NX-1206 (Full screen mode with only dashboard elements)
-   NX-1541 (Cannot open dashboard by name using command line option)
-   NX-1542 (Ampersand characters in template path not escaped in exported configuration XML file)

# 2.2.11

-   New parameter `Process.VMRegions` in Linux sub-agent
-   nxshell reads password from terminal if not given on command line
-   Housekeeper validates configuration for template DCIs

## Fixed issues

-   NX-1499 (Show last N values instead of line chart for string DCIs in alarm details view)
-   NX-1512 (File Manager: Unable to create new directory in root directory on Windows)
-   NX-1513 (Server installation fails with MySQL 8.0)
-   NX-1518 (Variable `$object` is not set for scheduled scripts associated with object other than node)
-   NX-1519 ("Import dashboard" action not available in dashboard group context menu)
-   NX-1520 (Object Details - Overview tab in desktop client is unusable when using dark gtk3 theme)
-   NX-1521 (Agent crash if file manager cannot resolve user or group name)
-   NX-1522 (Log parser can read file incorrectly during high write activity)
-   NX-1530 (Linux agent do not detect Hyper-V host)
-   NX-1531 (Scripts are not executed during macro expansion in "download file" type object tools)
-   NX-1532 (Agent external table does not handle UTF-8 text correctly)
-   NX-1535 (Auto bind to container is not working if node already is an indirect child of this container)

# 2.2.10

-   Improved server startup time
-   Added server startup event `SYS_SERVER_STARTED`
-   New method `readInternalParameter` in NXSL classes `Node`, `Cluster`, `MobileDevice`
-   Improved cached agent data reconciliation
-   Fixed DCI instance discovery issues
-   Fixed apkg installer script on AIX

## Fixed issues

-   NX-1477 (Offline data collection does not cleanup old data if there are no connection with the server)
-   NX-1514 (Predefined graph tree displayed incorrectly)

# 2.2.9

-   New NXSL functions: `Base64Decode`, `Base64Encode`, `EventCodeFromName`, `EventNameFromCode`
-   Original event name passed to alarm timeout event as 5th parameter
-   Added information tooltips in switch port view
-   Improved performance of active network discovery
-   Minimum, maximum, and moving average for ICMP response time in ping subagent

## Fixed issues

-   NX-1463 (Web UI does not work under Tomcat 9)
-   NX-1475 (Deselected "Create helpdesk ticket on alarm creation" is not being saved in EPP)
-   NX-1486 (NXSL function `CreateDCI` should allow creation with default retention and poll intervals)
-   NX-1489 (Unreliable MariaDB Connector/C version detection in workaround for MariaDB bug CONC-281)
-   NX-1494 (Release 2.2.8 failed to compile on macOS)
-   NX-1496 (Metrics `System.Memory.Physical.Available` and `System.Memory.Physical.AvailablePerc` are implemented inFreeBSD agent)
-   NX-1501 (In test mode `$dci` variable is not set)
-   NX-1502 (Configuration poll resets SNMP version on node)
-   NX-1503 (Access denied error on attempt to take screenshot even if user has take screenshot access right)
-   NX-1504 (Server crash after compiling library script with syntax error)
-   NX-1505 (Assignment in NXSL `global` statement ignored if variable already declared as global)
-   NX-1510 (Agent list `Net.InterfaceNames` not supported on FreeBSD)

# 2.2.8

-   Delayed actions in event processing policy
-   Raw event data stored in event log
-   New hook scripts: `PostObjectCreate` and `DiscoveryPoll`
-   Implemented watchdog functionality for external subagents
-   SNMP port and context can be specified in NXSL function CreateSNMPTransport
-   Fixed Summary DCI table fail when row limit set
-   Fixed menu path creation for Summary DCI Table and folder creation for graph view
-   New command line options for Windows agent installer: `/FORCECREATECONFIG`, `/LOGFILE=`, `/FILESTORE=`, `/CONFIGINCLUDEDIR=`
-   Server optimization for high load
-   Fixed SQL errors during database import or migration
-   New dashboard element "Port view"

## Fixed issues

-   NX-1186 (WebUI does not show objects on geo map)
-   NX-1377 (Can't upgrade sqlite database from version 21.4 to 21.5 with error "Unable to set not null constraint")
-   NX-1435 (AgentTunnelListenPort configuration parameter is missing from config table)
-   NX-1458 (DB upgrade from 0.454 to 0.455 failing for sqlite)
-   NX-1459 (Online upgrade for 22.21 failed on sqlite)
-   NX-1471 (Add option to create node in maintenance mode)
-   NX-1472 (Physical Hyper-V Hosts are reporting as Node Type "Virtual" in 2.2.7)
-   NX-1480 (Varbinds in SNMP Traps restricted to 255 characters)
-   NX-1481 (Configuration option to disable topology based event correlation)
-   NX-1482 (NetXMS server ignoring Syslog and Traps from devices in a Zone which are sending directly to NetXMS server)
-   NX-1484 (Corrupted event messages if MySQL is used as backend database)
-   NX-1488 ("Use active thresholds" checkbox gets checked after clicking on OK in map link properties)
-   NX-1492 (Changes in object status not reflected on geo map)

# 2.2.7

-   "Convert to hexadecimal string" option for SNMP table columns
-   Improved configuration wizard in Windows server installer
-   New command line option `/CONFIGENTRY` in Windows agent installer
-   New dashboard element "Object Details" (based on object queries)
-   TCP proxy functionality
-   Improved "Alarm Details" view in management console
-   Added support for agent actions defined in external subagents
-   TCP listener can be disabled in agent configuration file
-   Push connector can be disabled in agent configuration file
-   Virtual nodes detection via agent
-   Basic BIOS and hardware platform information provided by Windows agent

## Fixed issues

-   NX-993 (Windows installer should honor current state of services during upgrade)
-   NX-1438 (Increase debug level for thread pool messages)
-   NX-1453 (Windows installer option to disable database upgrade)
-   NX-1455 (Zone UIN in NXSL function CreateNode)
-   NX-1456 (DCI values aggregated on cluster may be incorrect on first few polls after server startup)
-   NX-1460 (Configure does not detect `pthread_setname_np` on macOS)
-   NX-1464 (Agent connection via proxy is not working for IPv6 destinations)
-   NX-1466 (Line length in agent's external table script limited to 255 characters)
-   NX-1467 (Agent cannot process requests for parameters longer than 255 characters)

# 2.2.6

-   NXSL based queries in object finder

## Fixed issues

-   NX-1395 (Change Object Filter to only search if at least 3 characters have been entered)
-   NX-1451 (Additional configs not loaded on agent startup)

# 2.2.5

-   Agent tunnel falls back to unbound mode in case of agent certificate validation failure
-   Zone information added to alarm log, event log, SNMP trap log, and syslog
-   Agent returns correct free memory value on Windows
-   Parameter `System.Memory.Physical.Cached` supported on Windows

## Fixed issues

-   NX-333 (Add windows service descriptions for both server and agent)
-   NX-622 (Alerts will not be generated in certain conditions: events, that persist after maintenance and node down after unreachable)
-   NX-640 (File manager should show file owner and permissions)
-   NX-716 (Server configurator on Windows should be marked as require-administrator)
-   NX-922 (Service check template objects disappears after server restart)
-   NX-1097 (Configuration option to ignore alarm's helpdesk state when doing resolve or terminate)
-   NX-1157 (configure `--with-dist` fails if OpenSSL is not installed)
-   NX-1397 (Implement Windows Update information parameters for Windows 10 and Windows Server 2016)
-   NX-1415 (Windows 10 upgrades break agent tunnels)
-   NX-1417 (`File.Size` parameter not working for Windows pagefile.sys)
-   NX-1418 (Sort scripts in Execute Server Script dropdown)
-   NX-1419 (`AgentTunnels.ProcessUnbound` scheduled task should be hidden)
-   NX-1420 (Do not use unmanaged devices with SNMP for MAC resolving)
-   NX-1421 (Configuration poll for node without SNMP and agent always read ARP cache from all SNMP devices in subnet)
-   NX-1427 (Max manual Y values for graphs limited to 2147483647)
-   NX-1431 ("Don't Fragment" option for ping sub-agent)
-   NX-1433 (LDAP timeout blocks internal user database)
-   NX-1434 (Return from function from within foreach loop in NXSL can cause unexpected runtime error)
-   NX-1436 (Write hostname to agent log on startup)
-   NX-1442 (Generic device driver cannot read interface list if device does not support ifNumber MIB object)
-   NX-1446 ( Only one agent policy editor can be opened, if another policy is opened for editing, previous is closed without saving)

# 2.2.4

-   Portech SMS gateway works correctly with newer gateway versions

## Fixed issues

-   NX-1208 (Added filter to alarm list)
-   NX-1295 (MIB Walk from DCI missing Column)
-   NX-1332 (Execution timeout for external parameter provider)
-   NX-1337 (Map link color based on object status)
-   NX-1346 (Unable to select template group on config export)
-   NX-1400 (NetworkMap link can be locked when using bendpoints)
-   NX-1403 (Setting floor plan view from right-click menu does not work)
-   NX-1404 (No source node in events generated by syslog parser)
-   NX-1405 (Agent may crash when parsing Windows event log message)
-   NX-1408 (Object filtering by zone in object browser and object search form)
-   NX-1411 (Server configuration option "UseInterfaceAliases" not working)
-   NX-1413 (Agent may crash when processing external parameters provider's output)

# 2.2.3

-   Additional information about captured Windows Event Log event passed to the server
-   Improved server startup time
-   Automatic termination of related alarms when DCI is deleted
-   Added attribute `isSTP` to NXSL class `Node`
-   File I/O functions in NXSL (disabled by default)
-   Sub-second interval between packets can be configured in PING subagent (down to 10 milliseconds)

## Fixed issues

-   NX-1149 (Pass EventRecordID with matched Windows event log record)
-   NX-1258 (Option to pass event data from Windows event log to NetXMS event)
-   NX-1259 (Added NXSL function - `FindAlarmByKeyRegex`)
-   NX-1363 (Automatic deployment of agent policies)
-   NX-1364 (Automatically create nodes for unbound agent tunnels)
-   NX-1367 (Fix HP aCC compiler warnings)
-   NX-1383 (Minimal interval before generating data collection script error events)
-   NX-1389 (If library script saved with compilation errors it disappears from script list)
-   NX-1392 (Reload log parser without agent restart)
-   NX-1393 (PostgreSQL deadlock on updating `raw_dci_data` table)
-   NX-1398 (Windows Server 2016 not detected correctly)
-   NX-1399 (Some SQL queries fail when using MariaDB driver because of MariaDB bug CONC-281)

# 2.2.2

-   Server command line tools working with agents (nxaction, nxap, nxget, nxupload) use encryption by default
-   "Floor plan" display mode for objects on network map
-   Access to zone data in network discovery filters
-   Automatic target configuration in PING subagent
-   Implemented option to display object status map in radial form

## Fixed issues

-   NX-513 (add `toString()` to all data objects in netxms-base)
-   NX-599 (Delete single collected value from a DCI)
-   NX-669 (DRBD monitoring is not working in some configurations)
-   NX-689 (Pass found SNMP configuration while discovery for new node creation)
-   NX-890 (Passive elements in rack)
-   NX-1169 (Encryption is not set by default between agent and server)
-   NX-1297 (Copying Files inside File Manager using CTRL and Drag&Drop is not working)
-   NX-1299 (Add username filter to `CountEx()` and `Process.XXX()` parameters in Linux subagent)
-   NX-1306 (Show system FQDN in tunnel manager)
-   NX-1350 (Invert Values option for performance tab DCIs; Performance tab graph configuration is maintained on double-click)
-   NX-1366 (Edit option for "group box" decorations on network maps)
-   NX-1369 (Title not displayed for dashboard element "Rack")
-   NX-1370 (Rack page not displayed correctly when switch between rack objects)
-   NX-1372 (PING subagent is not working)
-   NX-1374 (Element DashboardGroup not displayed in Dashboard perspective)
-   NX-1373 (Error message "Error loading RSA keys from ..." in all server-to-agent command line tools)
-   NX-1375 (Add functionality to switch off multipliers for graphs)
-   NX-1376 (Windows agent reports incorrect OS version on Windows 10)
-   NX-1379 (Rack width calculated incorrectly if only front/back selected)
-   NX-1380 (Database error when node has LLDP ID longer than 63 characters)
-   NX-1381 (Unjustified NXSL errors "cannot do automatic type cast")
-   NX-1384 (Automatic ping target configuration on first data request)
-   NX-1385 (Configurable status colors in UI)
-   NX-1387 (Performance tab graph sorting in not working with groups)

# 2.2.1

-   Implemented separate access rights for each DCI object
-   Option to read log files using VSS snapshots on Windows
-   Per stage confirmation in database manager during database check
-   Fixed file download cancellation
-   HTTPS support in SMSEagle driver
-   New network map element - text box
-   New debug log format with tags
-   Ability to set debug level per tag or tag mask
-   Improved audit logging on object creation
-   NXSL function `GeoLocation` replaced with `GeoLocation` class constructor
-   Optimized object updates in database (to reduce load on database in large installations)
-   Thread pool used for data collection instead of fixed number of poller threads
-   Optimized data collection from agents
-   Configurable number of records per transaction for writing DCI data

## Fixed issues

-   NX-662 (New network map element - text box)
-   NX-703 (Export/Import actions)
-   NX-757 (Instance discovery - grace period for removed instances before deleting DCIs)
-   NX-801 (Deleted nodes not removed from trusted nodes lists of other objects)
-   NX-1045 (Add rack/chassis diagram as dashboard element)
-   NX-1142 (Back view for racks)
-   NX-1201 (Discovered node links on map should automatically be set to color based on the status of the interfaces shown in connector names)
-   NX-1252 (Fix automatically generated transformation scripts for 64 bit interface counters)
-   NX-1268 (Do DNS resolve for node names via zone proxy)
-   NX-1289 (Override PollCountForStatusChange at Node level)
-   NX-1292 (Option for line charts to not always use 0 as base)
-   NX-1336 (Cluster DCI Max/Min aggregation returns value from last node instead of expected max/min)
-   NX-1339 (JIRA restricts subject field to 254 chars, helpdesk integration should trim alarm text or move reset of the message to issue description)
-   NX-1341 (Scheduled tasks enabled/disabled indicator)
-   NX-1342 (Increase text length limit in SMS sender)
-   NX-1343 (Server crash on re-enabling temporary disabled user)
-   NX-1344 (Search Bar for Agent Tunnel Manager)
-   NX-1345 (Add rule number to EPP export)
-   NX-1347 (New agent parameter `File.LineCount`)
-   NX-1348 (Continuous warnings in server log: seed object 0 cannot be found)
-   NX-1357 (Line chart is now opened on double clicking a Performance Chart)
-   NX-1359 (Last location in World Map is now saved)
-   NX-1361 (Data type of transformation script's input value can be incorrect)

# 2.1.2

-   Summary tables for table DCIs
-   Multi-valued columns in summary tables
-   Threshold violation events have current DCI value as parameter 8 (named as "dciValue")
-   New agent configuration parameter TunnelKeepaliveInterval
-   Optimizations in database access layer
-   Improved database check procedure
-   Management console:
    -   Option to set root object for "Geo Map" dashboard element
    -   Filter in geo map view
    -   "Duplicate" button in DCI threshold editor
    -   Option to show legend for performance tab graphs with single DCI
    -   Fixed file upload errors in web UI
    -   Option to show "Top N items" in dashboad summary table using given sorting columns

## Fixed issues

-   NX-1147 (Create separate access right for taking screenshots)
-   NX-1265 (Add option to apply template on Container(nodes that are under container))
-   NX-1270 (Ability to skip event log / audit log during "nxdbmgr export")
-   NX-1276 (Service components map as dashboard element)
-   NX-1282 (Non-English characters in agent policy can cause corrupted configuration)
-   NX-1290 (Add separate access rights for reading data directly from SNMP or agent)
-   NX-1296 (Audit Log: Parameters passed to actions are not being logged)
-   NX-1300 (Upgrading Agents via Packet Manager times out when using Agent Tunnels)
-   NX-1309 (Tunnel commands missing in console help)
-   NX-1313 (Node can get stuck in "Node down" when switching from direct connection to tunnel)
-   NX-1314 (Force DCI Poll displays "Clear collected data" progress)
-   NX-1315 (Only top level dashboards displayed in dashboard selection dialog (only in embedded dashboard element properties))
-   NX-1320 (Add button duplicate or copy for thresholds)
-   NX-1324 (World Map - Allow to use a zoom level greater than 18 (19 and 20, like on the openstreetmap.org website))
-   NX-1325 (World Map - Add filter for map nodes, like in the list widgets)
-   NX-1331 (Cluster IDATA tables are lost during export/import)
-   NX-1333 (nxdbmgr `-s`/`-S` export `raw_dci_values` table)
-   NX-1335 (nxdbmgr fail import if idata tables are missing)

# 2.1.1

-   XEN monitoring subagent
-   Fixed issues with agent tunnels
-   Fixed bug in STP-based topology discovery
-   Fixed unrestricted node poller queue growth when discovery from SNMP traps or syslog is on
-   Server's database password can be supplied by external tool
-   Fixed OpenBSD compatibility issues
-   Correct handling of "dormant" and "not present" interface operational states
-   Syslog messages received on loopback bound to receiving node (local management node or syslog proxy node)
-   Fixed mail sender address encoding
-   Fixed bug with lost agent connectivity after tunnel reconnect
-   Zone ID now referenced as Zone UIN (unique identification number) to avoid confusion with zone object ID
-   Fixed bug with not generated `*_UNREACHABLE` events after server restart
-   NXSL:
    -   New class `InetAddress`
    -   New attribute `ipAddressList` for class `Interface`
    -   New method `enableRoutingTablePolling` in class `Node`
-   Management console:
    -   Improved status map
    -   Fixed bug in sorting alarms by zone name
    -   Zone ID can be generated automatically on zone creation
    -   New node can be created directly from agent tunnel manager
    -   "Bar" mode for gauge dashboard elements working correctly

## Fixed issues

-   NX-930 (nxdbmgr export ignore `$NETXMS_HOME`)
-   NX-1143 ("Dormant" interface state is not supported correctly)
-   NX-1153 (SQL Injection in user profiles)
-   NX-1170 (Ask user confirmation before any action on FileManager UI)
-   NX-1263 ("Change zone" assigns node to zone's Object ID, not Zone ID)
-   NX-1272 (ExternalTable does not handle non-native live ending properly)
-   NX-1273 (Netxms 2.1 version. Copy Clipboard in Alarm Browser not work correctly)
-   NX-1278 (Unable to move dashboard to the first level)
-   NX-1281 (AdHocScheduler sleeping for 0 seconds)
-   NX-1284 (SQL errors when using mssql.ddr)
-   NX-1285 (SNMP trap varbind mapping by position broken)
-   NX-1286 (Internal parameter PingTime returns last known value if ICMP proxy for node is down)

# 2.1

-   Improved audit logging
-   Improved data reconciliation between agent and server
-   Improved Grafana integration
-   Server detects changes in installed packages during configuration poll
-   Added MariaDB database driver
-   Fixed excessive CPU usage by agent on AIX
-   nxshell can connect to server on non-standard port
-   Driver for Netonix switches
-   NXSL:
    -   New methods for arrays: `append`, `insert`, `pop`, `push`, `remove`
    -   Table methods `get` and `set` can accept column name instead of column index
    -   Table row method `get` can accept column name instead of column index
    -   Added table row method `set`
    -   Access to DCI owner object in data collection and instance discovery scripts via `$targetObject` variable
-   Management console:
    -   Improved layout of dashboard elements
    -   Added option to indicate alarm severity with background color in alarm list
    -   Fixed bug in folder download in file manager
    -   Proper support for ANSI colors in object tools output in web UI
    -   Object dragging on map disabled if user don't have write access to map object
    -   Option to hide sub-interfaces in UI (currently works only for Juniper switches)

## Fixed issues

-   NX-1039 (postgresql support problems)
-   NX-1041 (Encryption code incompatible with OpenSSL 1.1.0)
-   NX-1166 (Double click on a map link with attached DCIs should bring up a chart)
-   NX-1180 (Web localisation exceptions)
-   NX-1194 (Import ignoring " in Object Tool command)
-   NX-1195 (NetXMS Grafana Plugin)
-   NX-1212 (Threshold - disable fields depending on Function)
-   NX-1214 (Show only changed Server Configuration)
-   NX-1215 (EPP import fails)
-   NX-1234 (Provide access to DCI owner node in instance discovery filter when source node is set)
-   NX-1236 (Dashboard Groups)
-   NX-1243 (When dashboard is modified by admin, refresh request should be pushed to all connected clients)
-   NX-1244 (File manager -> Show file: "copy" in context menu not available after "Select all", only after manual selection with mouse or keyboard)
-   NX-1251 (Load object overview tab content only when tab is visible)
-   NX-1253 (NXSL: add new functions for arrays)
-   NX-1256 (Line chart improvements)
-   NX-1257 (Linux subagent segfault when core count > 64)
-   NX-1260 (Java subagent plugins can only be loaded with absolute path)
-   NX-1262 (Some parameters provided by JMX subagent are not working)
-   NX-1264 (Object tool output in web - not escaping JS control characters)

# 2.1-RC1

-   External tables in agent
-   Script source for table DCIs
-   Driver for IgniteNet devices
-   Network device database (allows some device specific information to be provided without drivers)
-   Server certificate's key can be stored in separate file
-   Multiple CA certificates can be specified in server configuration file
-   Number of samples can be configured for table thresholds
-   Null value can be used as "no change" option in auto bind scripts
-   Grafana integration
-   Management console:
    -   Node's zone name shown in alarm browser and object overview when zoning is enabled
    -   Sorting option in table based charts on dashboards (to implement "Top N" style charts)
    -   Full text object search
    -   Agent tunnel manager view

## Fixed issues

-   NX-386 (Access to components data from NXSL)
-   NX-1127 (Add support for .mib files instead of only .txt-files)
-   NX-1128 (Add functionality for recursively add MIBs from nested folder structure)
-   NX-1210 (New system right - "Access to external integration tools")
-   NX-1211 (REST-like API - user authentication)
-   NX-1222 (Show Zone in alarm browser)
-   NX-1231 (Create help desk ticket from alarm log viewer)
-   NX-1239 (IgniteNet driver)
-   NX-1240 (System-wide search)
-   NX-1242 (LLDP - wrong neighbor linked)

# 2.1-M3

-   Improved event correlation based on network topology
-   Improved the usability of the Server Configuration, by adding descriptions and recognition for data types and possible values
-   Alternative core configuration section can be set for nxagentd using `-G` command line option
-   Implicit external subagent registartion using `EXT:*` sections in agent configuration file
-   Unknown syslog sources can be automatically added as nodes
-   Server startup scripts
-   New method `setMapImage` in NXSL class `NetObj`
-   New attribute `mapImage` in NXSL class `NetObj`
-   New NXSL class `Container`
-   New NXSL function `AgentExecuteActionWithOutput`
-   Container autobind mode and script can be set from NXSL
-   Fixed bug in NXSL string concatenation
-   Events generated when interface expected state changed
-   Situations functionality is replaced with persistent storage that is included in each execution environment
-   Compression support in communication protocol
-   Switch forwarding database show correct interfaces for MikroTik devices
-   Driver for Juniper Networks switches
-   Driver for Extreme Networks switches
-   Experimental MQTT support
-   Experimental agent-to-server connections (agent tunnels)
-   Experimental Grafana integration
-   Management console:
    -   Mutiple files can be scheduled for upload to agent at once
    -   DCIs created from templates made visually distinguishable in data collection editor
    -   "Inverted" flag ignored in event processing policy if event or object list is empty
    -   Object tools can be filtered by custom attribute presence
    -   Configurable list of external URLs for each object
    -   Sound for outstanding alarm reminder can be configured

## Fixed issues

-   NX-60 (Implement object search by ID, IP address, primary host name)
-   NX-623 (Compression support on protocol level in file manager)
-   NX-630 (Descriptions and dropdowns with values in server configuration variables)
-   NX-743 (Finish script hints)
-   NX-916 (Stop command for server commands)
-   NX-1119 (Add Instance discovery for Table DCIs)
-   NX-1123 (Add filter for Table last values)
-   NX-1129 (nxmibc produces error compiling MIBs because of empty `OBJECTS` clause in `NOTIFICATION-TYPE` macro)
-   NX-1151 (`Process.CountEx` on Windows only checks first 255 characters of process command line)
-   NX-1161 (Android client crash)
-   NX-1165 (Notify user when edit DCI created from Templates(also from cluster))
-   NX-1171 (Add compression to usual netxms messages)
-   NX-1174 ("Copy name" additional option in context menu in the script library)
-   NX-1178 (Create helpdesk ticket on alarm creation)
-   NX-1187 (Additions to default EPPs)
-   NX-1188 (Zone proxy going down generates no alarms)
-   NX-1190 (Server configuration incorrectly detects type)
-   NX-1191 ("Display objects as" menu bug)
-   NX-1192 (Zone selection in node creation - show only zones)
-   NX-1193 (Drag-and-drop moving a larger ammount of EPPs can cause EPPs to disappear)
-   NX-1197 ('Download file' Object Tool - better handling when file not found)
-   NX-1198 (Container hierarchy deletion issue)
-   NX-1209 (Android client doesnt check server protocol version properly)
-   NX-1213 (Links to documentation for containers)
-   NX-1216 (After renaming user old login name still working until server restart)
-   NX-1217 (FreeBSD subagent `FileSystem.MountPoints` Parameter)
-   NX-1223 (Support multiple seed nodes per map)
-   NX-1224 (Show seed node for a map)
-   NX-1225 (Error on script delete from script librarry)
-   NX-1227 (Raspberry Pi SubAgent - CPU temperature)

# 2.1-M2

-   Added alarm category functionality to manage which alarms are seen by what users
-   EPP rules can be configured to generate categorised alarms
-   Alarm categories can be created and configured in Alarm Category Configurator
-   By default "View All Alarms" ACL added to Everyone group
-   Server can be configured to periodically send alarm summary emails
-   Added template graphs
-   New NXSL functions: `mktime`, `GetSyslogRuleCheckCount`, `GetSyslogRuleMatchCount`
-   New NXSL `Node` class attributes: `isInMaintenanceMode`, `lastAgentCommTime`
-   New NXSL `Table` class attribute `rows`
-   Access to object's alarms in NXSL via `alarms` attribute in `NetObj` class
-   Operator `new` in NXSL which can be used to instantiate objects if object class supports it
-   Template auto-apply and container auto-bind works for clusters
-   H3C driver correctly reads IPv6 addresses on interfaces
-   Improved HP ProCurve driver
-   SMS driver for Nexmo service
-   SMS driver for SMSEagle gateway
-   SMS driver for MyMobile service
-   Fixed FDB handling on Cisco switches
-   Added support for CHAP, MS-CHAPv1, and MS-CHAPv2 in RADIUS authentication
-   MySQL monitoring subagent
-   Fixed FreeBSD 11 compatibility issues
-   Implemented interrupt and context switch counters in platform subagents
-   Implemented CPU interrupt time parameters on Windows
-   JMX subagent
-   Event sending by agent do not restricted to master servers only anymore
-   Launcher for nxshell
-   Log monitoring subagent supports pre-allocated log files
-   Management console:
    -   File manager improvements
    -   Option to save graph as image
    -   Added multipliers support in data format string for gauges

## Fixed issues

-   NX-18 (Different layouts in port view based on driver information)
-   NX-79 (Command line tools should return proper error code)
-   NX-102 (Alarm categories)
-   NX-141 (Implement support for UNICODE logs in log monitoring subagent)
-   NX-146 (Find node by IP address)
-   NX-152 (Automatic database unlock in clustered environment)
-   NX-338 (Alarm summary e-mails)
-   NX-359 ("nxdbmgr migrate" should print out source and destination datasource before confirmation)
-   NX-394 (Performance tab should be available for cluster objects)
-   NX-442 (Importing Template that has a DCI that has a 'Performance Tab' graph attached to another DCI doesnt work properly)
-   NX-446 (Copying / moving a Template DCI with a 'Performance Tab' graph attached to another DCI doesnt work properly)
-   NX-576 ("Find IP address" should find node if node in NetXMS)
-   NX-664 (Template graphs)
-   NX-734 (Login messages (MOTD))
-   NX-736 (`System.Memory.*.*Perc` should return float)
-   NX-812 (View table DCI history for selected instance)
-   NX-824 (NXSL: foreach should be null-torelant)
-   NX-849 (File name during dashboard export should be set to dashboard name (now 'Untitled"))
-   NX-859 (Empty subnet deletion should happen at last node removal)
-   NX-867 (filemgr should support read only roots)
-   NX-870 (Agent - default MaxSessions if agent is a proxy)
-   NX-877 (Automatically refresh last values screen after forced DCI poll)
-   NX-901 (Add customizable color for status bar in the management console)
-   NX-931 (WriteAuditLog should use prepared statements)
-   NX-961 (Group can be added under group while LDAP sync.)
-   NX-970 (Save current graph to PNG)
-   NX-973 (Create file download progress bar (from agent to console))
-   NX-974 (Jira integration configuration is loaded on startup only (but marked as restart requied=no))
-   NX-976 ("diff" threshold value for unsigned data processed as unsigned)
-   NX-992 (context switches and Interrupts agent support)
-   NX-1013 (Object Tools - No longer in Alarm browser)
-   NX-1035 (Bulk alarm terminate)
-   NX-1042 (Resolve SNMP OIDs to textual representation in user interface)
-   NX-1049 (File manager path to file)
-   NX-1059 (Add default sorting in all log viewers)
-   NX-1060 (Average calculation for DCI summary table)
-   NX-1061 (New time option in condition filter (event log and others))
-   NX-1062 (Save button for agent editor broken)
-   NX-1065 (nxdbmgr export/import/migrate reference non existing tables `tdata_records`/`tdata_rows`)
-   NX-1067 (Unable to disable user "system" from user manager once it's enabled)
-   NX-1070 (Interface name sorting)
-   NX-1073 (Cannot set bind IP address for network service in GUI)
-   NX-1076 (Dashboard as Drilldown)
-   NX-1079 (ANSI color sequences not ignored in web console)
-   NX-1085 (Unicode handling errors)
-   NX-1088 ("Find MAC address" should find node if node in NetXMS)
-   NX-1095 (File manager fails with timeout on folders with large number of files)
-   NX-1096 (Watchdog with many nodes)
-   NX-1098 (icmp.cpp - Problems when there is many "ping poll" nodes)
-   NX-1099 (server crashes after a few seconds of running v2.0.6)
-   NX-1100 (Comments in scheduled tasks)
-   NX-1103 (High Load Average on update to 2.0.7 on FreeBSD 9.3)
-   NX-1106 (Separate access rights for entering/leaving maintenance mode)
-   NX-1107 (EnableReportingServer server config parameter not created by default)
-   NX-1108 (Threshold activation/deactivation events not considered as dependencies during export)
-   NX-1109 (nxdbmgr check can't create missing interface (Oracle))
-   NX-1112 (Force poll on push DCI changes it's state to "unsupported")
-   NX-1113 (Graphs tab does not automatically refresh when new predefined graph is added. Naming issues in template graph property pages.)
-   NX-1114 (Graph access rights do not save)
-   NX-1120 ("Invalid thread access" error on alarm state change to Acknowledge and Sticky Acknowledge)
-   NX-1122 (Not possible to save script from "Execute server script"(Web only))
-   NX-1125 (DCI's that are added from Teplates have problems with joint mapping on Performace tab of Object Details)
-   NX-1135 (Database 345 -> 346 upgrade failed on MSSQL)
-   NX-1138 (Dashboards Status Map Refresh)
-   NX-1139 (Remove unexpected up/down alarms when interface gets deleted)

# 2.1-M1

-   New policy type: Log Parser
-   New server configuration parameter "JobRetryCount"
-   Chassis objects
-   Hypervisor monitoring subagent
-   In case of Policy deploy, Policy uninstall or File upload jobs fail they are scheduled for reinstallation(scheduled tasks) "JobRetryCount" times. First time job is rescheduled in 10 minutes. Each next wait time is twice more than the previous time.
-   If policy is known as installed on the node by the server and agent reposts that it is not installed it is being reinstalled.
-   Added configuration option to log parser to generate event only if regular expression have been matched exact count of the times in a predefined time period
-   New internal parameters: `Server.ReceivedSNMPTraps`, `Server.ReceivedSyslogMessages`, `ReceivedSNMPTraps`, `ReceivedSyslogMessages`
-   Max size of agent data collectiors pool can be configured
-   Agent data reconciliation block size and timeout can be configured
-   New agent parameters `System.CPU.CurrentUsage` and `System.CPU.CurrentUsage(*)`
-   SSH subagent (for collecting data and executing actions via SSH)
-   Zone ID can be set for agent in SNMP proxy mode
-   Zones has common default proxy node for all protocols
-   Zone's proxy node can be placed inside that zone
-   Syslog proxy in agent
-   Built-in superuser account renamed to "system"
-   Default "admin" account now is ordinary member of "Admins" group without built-in privileges
-   New method `enableDiscoveryPolling` in NXSL class `Node`
-   New NXSL functions: `AgentExecuteAction`, `GetAllNodes`
-   NXSL functions `GetNodeInterfaces`, `GetNodeTemplates`, `GetNodeParents`, `GetObjectChildren` returns correct object classes
-   Agent effective user and group can be set in configuration file
-   Agent environment variables can be set in configuration file
-   Added method `getResourceOwner` and attribute `nodes` to NXSL `Cluster` class
-   New object tool type "server script"
-   Number of polls can be set for "diff" type thresholds
-   Instance discovery scripts can return instances as map instance/instance name
-   CPU usage parameters on Windows moved to winnt.nsm from winperf.nsm and no longer depends on PDH
-   New agent metrics for self-monitoring:
    -   `Agent.SyslogProxy.IsEnabled`
    -   `Agent.SyslogProxy.ReceivedMessages`
    -   `Agent.SyslogProxy.QueueSize`
-   Management console:
    -   New editors for Agent Config Policy and Log Parser Policy.
    -   DCI summary tables with empty menu path not shown in object context menu

## Fixed issues

-   NX-44 (Apply policy to node by clicking on node and selecting policies from list)
-   NX-53 (Monitors (event log, syslog, etc.) as dashboard elements)
-   NX-65 (Internal optimization for object references)
-   NX-272 (EPP Editor suggestion: change command names)
-   NX-355 (Apply policy automaticaly when node goes up)
-   NX-393 (NetXMS Agent Proxy SNMP Traps and Syslog)
-   NX-520 (Object tools - Columns tab present when it should not be)
-   NX-587 (Find switch port for a multi-selection in "Interfaces" tab)
-   NX-694 (Select source (agent / snmp) for new DCIs based node capabilities)
-   NX-697 (Reorder EPP rules using drag and drop)
-   NX-726 (Apply multiple templates at once)
-   NX-732 (Unify filter widgets in object selection dialogs)
-   NX-742 (Better accessability to "`>`" operator in Object browser filter)
-   NX-773 (Ability to nxget selected template DCI on any node)
-   NX-780 (Dashboard import should use name from xml file if not provided by user)
-   NX-787 (Search in results of a SNMP walk (MIB Explorer))
-   NX-796 (Additional information in management console title)
-   NX-825 (unable to export dashboard with invalid DCI IDs)
-   NX-832 (Object tree filter by Object ID)
-   NX-876 (Long running queries should be logged)
-   NX-880 (Use multipliers in agent tables DCIs)
-   NX-934 (Copy DCI name (not description) from last value view)
-   NX-956 (Scheduled file upload server-\>agent doesn't work with default file destination(empty destination file name))
-   NX-960 (DCI summary tables with no menu path should not show in right click menus)
-   NX-980 (execute script from object tool)
-   NX-989 (Create agent DCIs that will provide status fo agent log file, local database)
-   NX-996 (do not create DCI if windows cancel button)
-   NX-1000 (Type of search in class ColumnFilter should be change to Enum type.)
-   NX-1001 (DCI Summary Tables "Use multipliers" treat string objects as numbers)
-   NX-1004 (Object tools filer by client OS for local commands)
-   NX-1009 (Add button to clear filter)
-   NX-1012 (DCI description containing only {instance} macro is not substituted during instance discovery)
-   NX-1016 (Agentless UNIX monitoring over ssh)
-   NX-1018 (Java subagent fails if list size=0)
-   NX-1026 (Cannot set log size limit higher than 4GB)
-   NX-1033 (Add filter to FDB view)
-   NX-1034 (Refacrot Ping subagnet (Create `ICMP.Targets` table and `ICMP.Target` list with only IPs))
-   NX-1038 (Already created scheduled task cannot be modifyed from shcedule to one time execution)
-   NX-1051 (java api User object missing ldap\_dn + ldap\_unique\_id)

# 2.0.6

-   Fixed incorrect interface network mask reported by agent on Windows XP and Windows Server 2003
-   Added option to turn off quotes in `AT+CMGS` command in generic SMS driver
-   Improved compatibility with different GSM modem types in generic SMS driver
-   Fixed SQL errors when saving LDAP users to database
-   Fixed excessive temporary files creation by web UI
-   Fixed build errors on Solaris 11
-   Fixed memory leak in Oracle DB driver
-   Fixed bug in SNMP transport causing false timeout errors
-   New agent metrics for self-monitoring:
    -   `Agent.Proxy.ActiveSessions`
    -   `Agent.Proxy.ConnectionRequests`
    -   `Agent.Proxy.IsEnabled`
    -   `Agent.SNMP.IsProxyEnabled`
    -   `Agent.SNMP.IsTrapProxyEnabled`
    -   `Agent.SNMP.Requests`
    -   `Agent.SNMP.Responses`
    -   `Agent.SNMP.ServerRequests`
-   Management console:
    -   Fixed glitches in table value view

## Fixed issues

-   NX-545 ("Export to CSV" file save dialog use incorrect file mask (`*.*` instead of `*.csv`))
-   NX-614 (Agent parameter list not retrieved when using a proxy)
-   NX-639 (User management changes and upgrades)
-   NX-768 (Ctrl+a and Filter in node's Interfaces tab)
-   NX-1025 (Segfault)
-   NX-1028 (If mail encoding set to utf-8 mail body encoded incorrectly)
-   NX-1029 (`gps_history_%d` table not dropped when node is deleted)
-   NX-1031 (Bug with displaying cross(remove field) in edit table threshold)

# 2.0.5

-   Data collection script can return null to indicate data collection error
-   Added option to set type of each varbind in nxsnmpset
-   Fixed memory leak in PostgreSQL database driver
-   New attributes `source` and `sourceId` in NXSL class `Event`
-   New method `toJson()` in NXSL class `Event`
-   LVM monitoring parameters on AIX
-   Added option to get normalized server thread pool load average
-   Fixed bug in self-monitoring termplates
-   Management console
-   Fixed possible deadlock when executing server script
-   Fixed area charts on dashboards
-   "Interactive" option for line chart dashboard elements

## Fixed issues

-   NX-799 (Support 64bit interface counters on 64bit Linux)
-   NX-820 (Set `SYS_TABLE_THRESHOLD_ACTIVATED` and `SYS_TABLE_THRESHOLD_DEACTIVATED` as default in table threshold editor)
-   NX-997 (Force poll on DCI with custom schedule)
-   NX-1005 (Agent and server can write garbage instead of program name to syslog)
-   NX-1010 (NXSL function `FindObject` returns `NetObj` object for interfaces)

# 2.0.4

-   New parameters in Linux platform subagent to get additional CPU information (frequency, model, etc.)
-   Fixed bugs in LLDP based network topology discovery
-   Correct notifications on threshold script errors
-   Option to use last known value for cluster data aggregation in case of data collecion failure
-   Added server configuration parameter to ignore syslog message timestamps and always use server time
-   Added option to disconnect existing sessions of same user on login
-   NXSL: implemented compound assignment operators and prefix increment/decrement for array elements
-   NXSL: can access event parameters as event object attributes (like `$event->$1` or `$event->instance`)
-   Management console
-   Improved dashboard gauge widget
-   Added translucence option for dashboard line charts
-   Configurable display format for dashboard elements data sources
-   Improved inverted line chart support
-   DCI filter in DCI selection dialog
-   Configurable line width on ad-hoc line charts
-   Object tooltips in rack view
-   Line/area switch for all DCIs on chart level
-   Android console
-   Reorganized alarm notification section (issue NX-963)

## Fixed issues

-   NX-280 (NXSL, `++` and `+=` on array elements)
-   NX-567 (GetEventParameter issue)
-   NX-647 (Graph stacking only works on non inverted sources)
-   NX-765 (Agent Action - parameters not passed from object tool)
-   NX-866 (Linux NetXMS agent stops working.)
-   NX-892 (One check-box to "Area-chart" all DCIs on graph)
-   NX-955 (Remove deprecated table `policy_time_range_list`)
-   NX-963 (Refactoring of alarms notification)
-   NX-964 (DCI filter in DCI selection dialog)
-   NX-965 (Incorrect handling of VRRP MAC addresses)
-   NX-966 (Events got duplicated on template auto import)
-   NX-969 (Cannot select objects on map if zoom is not 100%)
-   NX-977 ((web) Exception in Server configuration -> new)
-   NX-978 (Suggested rack display improvements)
-   NX-981 (line width on graphs)
-   NX-986 (Add double click for schedule edit)
-   NX-990 (Agent cache not working if server is not configured as master server)
-   NX-1223 (Support multiple seed nodes per map)

# 2.0.3

-   Additional parameters in Oracle subagent for redo logs and ASM monitoring
-   NXSL: variable `$errormsg` holding error description set in catch block
-   New NXSL function `SplitString`
-   NXSL: new methods `setExpectedState` and `setExcludeFromTopology` in `Interface` class
-   Default interface expected state can be configured
-   GPS subagent (provides location data from NMEA compatible GPS receivers)
-   Server can update node location using GPS subagent
-   Fixed error while event alarm linking multiple times
-   Fixed server hang on shutdown
-   NetXMS processes uses `LC_CTYPE` from environment for terminal I/O
-   Fixed bug in saving service checks
-   Fixed server crash caused by heap corruption in MS SQL and DB/2 database drivers
-   Fixed server deadlock caused by simultaneous use of instance discovery and transformation scripts
-   Agent parameters for monitoring System V message queues
-   New action `User.ChangePassword` in WINNT subagent
-   Text2reach SMS driver improved
-   Port check subagent can be configured to return negative value as response time in case of error
-   Management console:
    -   Fixed grid issues in network maps
    -   Fixed object selection issues in network maps
    -   Added "hide links" option on network maps
    -   Added support for MAC addresses in format xxx.xxx.xxx.xxx

## Fixed issues

-   NX-733 ("Show object details" from DCI summary table)
-   NX-745 (Show Threshold value in DCI Configuration)
-   NX-769 (Default Expected State of Interface handling)
-   NX-829 (Change default legend position to "bottom")
-   NX-882 (Windows agent fails to parse/process some events.)
-   NX-902 (Object overview show expected state interface)
-   NX-909 (Setting for age of source data when alarm is created (for data reconciliation))
-   NX-913 (Maintenance mode from Summary Tables)
-   NX-923 (Agent can crash on Solaris when one of CPUs taken offline)
-   NX-924 (NXSL: DCI-related functions (`FindDCIByName`, etc.) fail on cluster nodes)
-   NX-929 (It should be possible to execute agent action on node behind proxy)
-   NX-938 (Add the option "fromPhone" for drivers websms)
-   NX-941 (Add option to enter and leave maintenance mode form nxsl script)
-   NX-944 (Java API `connect()` timeout)
-   NX-947 (No script error event when script uses "use" with non-existent library script)

# 2.0.2

-   Optimized LDAP synchronization for large directories
-   Added NXSL API for manipulating object geolocation
-   Fixed bug that allows to crash server remotely by sending garbage to client connector port
-   NXSL: new hash map attributes `keys` and `values`
-   Object custom attributes can be accessed as hash map in NXSL
-   New server debug console commands `log` and `logmark`
-   Management console:
    -   Improved file transfer error handling
    -   Double click on geo map zoom in and center map on point under cursor
-   Android Console:
    -   Updated ACRA library: now crash reports are sent via e-mail (will use the app installed on device to send mail)
    -   Fixed bug in action bar commands: disconnect and exit sometimes wasn't working
-   Android Agent:
    -   Updated ACRA library: now crash reports are sent via e-mail (will use the app installed on device to send mail)

## Fixed issues

-   NX-823 (F2 to rename objects in Object Tree)
-   NX-830 (Show template name with template groups as a path)
-   NX-873 (Improve `isPrinter` detection)
-   NX-891 (Maintenance mode doesn't work on subnet objects.)
-   NX-895 (Server may crash under heavy load if user logs in when objects being deleted from database)
-   NX-903 (NXSL functions to manipulate node location)
-   NX-906 (PollCountForStatusChange no longer has effect after upgrading to latest stable version)
-   NX-911 (ServiceResponseTime parameter can return 1 as error which can be interpreted as actual response time)
-   NX-912 (World map - zoom to cursor location, not to middle of map)
-   NX-915 (AIX(?) subagent should check if `FileSystem.Total` is -1)

# 2.0.1

-   Fixed random server crash if ODBC database driver is used
-   Fixed incorrect reading of long text fields by MS SQL database driver

## Fixed issues

-   NX-833 ("Thresholds" tab should be shown on clusters)
-   NX-844 (Android client graph problems)

# 2.0

-   Template import correctly handles updates for existing templates
-   Scripts can be used as instance source in instance discovery DCIs
-   NXSL node object attribute snmpSysDescription renamed back to sysDescription
-   Selectors in NXSL
-   Array attributes in NXSL: `size`, `minIndex`, `maxIndex`
-   Hash map attributes in NXSL: `size`
-   New NXSL function: `mapList`
-   Subnet mask for synthetic subnets can be set in server configuration
-   Added cumulative counters for server DB writer requests
-   Fixed data corruption issues in ODBC and Oracle DB drivers
-   Additional internal server metrics for monitoring DB activity and performance
-   Added interface creation hook
-   Improved `System.InstalledProducts` table handling on Windows
-   Fixed inefficient query in Oracle monitoring subagent
-   Server shutdown speed improved
-   Faster SNMP probing during configuration polls
-   Fixed false negative in node down detection if expected state of some interfaces set to IGNORE
-   Agent SNMP proxy improved
-   Improved agent data cache reconciliation
-   Fixed Oracle 12c compatibility issues
-   Automatic configuration import from templates directory on server startup
-   Fixed address list configuration bug
-   Management console:
    -   Object tool input fields can be rearranged
    -   Line width can be configured for line charts on dashboards
    -   Column sizes saved in table DCI last values view
    -   Rack height and numbering direction can be changed
-   Android Console:
    -   Refactoring of Alarms configuration section: alarm notification events fully customizable, added notify by vibration (SOS pattern) and by LED color (set to black to disable a specific category)
    -   Added action buttons in status bar for notification icon (reconect, disconnect and exit), only for Android version starting from v4.1
    -   Updated support library
-   Android Agent:
    -   Support for Marshmallow devices (v6.0)
    -   Updated support library

## Fixed issues

-   NX-171 (Add empty hook scripts to configuration library)
-   NX-635 (Add "last communication with agent" timestamp to Overview tab)
-   NX-637 (Disable a map object filtering script by checkbox deletes the script)
-   NX-731 (Ability to move Object Tool Input Fields)
-   NX-746 (Default EPP rules for SNMP and Agent un-responsiveness)
-   NX-747 (Agent List - Interface name list)
-   NX-749 (newly created DB is inconsistent (SQLite only?))
-   NX-750 (Server ignores agent cache mode settings for DCIs with source node set)
-   NX-754 (Client library compilation script package.cmd for Windows is broken)
-   NX-756 (Show interface operational status in UI)
-   NX-759 (Default EPPs for `SYS_THREAD_HANG` and `SYS_THREAD_RUNNING`)
-   NX-760 (`Hook::InterfaceAcceptFilter`)
-   NX-761 (Server config parameter for default subnet size)
-   NX-764 (Maintanance mode - default EPPs and visualization)
-   NX-772 (Tables (empty) on cluster shown even is aggregation is disabled for DCI)
-   NX-778 (Dashboard import do not match "Table Value" element)
-   NX-783 (Ability to skip collected data export during "nxdbmgr export")
-   NX-784 (Internal DCI "AgentStatus" is supported only if agent is present on the node)
-   NX-785 (Show maintenance mode status in object browser)
-   NX-794 (When table inside dashboard can't load data (invalid DCI, etc.) – console error message is displayed)
-   NX-800 (Can't create dashboard with more than 8 columns)
-   NX-805 (`Table::addRow()` in nxsl return null empty value instead of row id)
-   NX-810 (mysql query error)
-   NX-813 (`System.Memory.Physical.Available` reports wrong values)
-   NX-839 (Crash on server shutdown)
-   NX-851 (Slow server shutdown)
-   NX-852 (Template auto-apply script is lost if auto-apply is disabled)
-   NX-854 (SQL errors on Oracle 12c)
-   NX-861 (Housekeeper doesnt delete empty subnets in multi-zone deployment)
-   NX-862 (VPN connector is not saved if subnets are not specified)
-   NX-863 (EPP rules not saved to DB after import)
-   NX-864 (Empty DCIs return "" string instead of `null` to calling NXSL functions)
-   NX-865 (`FileSystem.Volumes` vs. `FileSystem.Type`() inconsistency)

# 2.0-RC2

-   Maintenance mode for nodes, clusters, and mobile devices (manual and scheduled)
-   Fixed broken instance discovery filters
-   Fixed agent crash when collecting SNMP data in cached mode
-   Agent returns correct OS version on Windows 10
-   New NXSL `Node` class attribute: `bridgeBaseAddress`
-   One LDAP attribute can be used in multiple mappings
-   Fied deadlock on LDAP user deletion while LDAP synchronization
-   Add option to use encrypted password in password fileds in configuration files and in the server configuration parameters.
-   Added SMS driver for web service text2reach.com
-   SNMP sysContact and sysLocation collected and stored
-   Server can accept traps and syslog messages from nodes in all zones (controlled by TrapSourcesInAllZones configuration option)
-   On instance discovery pool instance name is updated if it has changed
-   New SMS driver - slack.com
-   IPv6 support in built-in syslog server
-   Fixed event processing policy export/import issues
-   Global default retention time and polling interval for data collection
-   Initial support for scheduled tasks within system
-   Scheduled file upload
-   Management console:
    -   Object context menu available on geo map
    -   Filter in event template configurator
    -   Web console use client time zone to display time
    -   Added option to use server time zone to display time in console
    -   Access to event log, SNMP trap log, and syslog from object context menu
    -   Dashboards can be associated with other objects (nodes, containers, etc.) and opened from object's context menu
    -   Forced DCI polls from summary tables
    -   Script hints

## Fixed issues

-   NX-578 (Show DCI name under mouse on line charts)
-   NX-619 (Clone object tools)
-   NX-629 (Allow selection of SNMP port during network discovery)
-   NX-640 (File manager should show file owner and permissions)
-   NX-652 (Delete DCI from template causes SQL error)
-   NX-666 (Components data not collected from entity MIB on some devices)
-   NX-671 (Improve LLDP handling for devices that do not provide own LLDP ID)
-   NX-674 (scheduled maintenance/downtime)
-   NX-678 (LDAPConnection::getAllSyncParameters(): buffer overflow)
-   NX-679 (Disabled object tools shown in node commands)
-   NX-680 (Ability to bind node to container not from container's context menu, but from node's context menu as well)
-   NX-684 (ldapSync deadlock)
-   NX-685 (Object Tool - Server Command timeout)
-   NX-686 (Need function x2d - returns the decimal value of a hexidecimal.)
-   NX-688 (DATACOLL ThreadPool related parameters Unsupported on agent)
-   NX-690 (Show sysLocation and sysContact in object overview)
-   NX-691 (IPv6 support in syslog receiver)
-   NX-693 (Add option to use encrypted password in password fields in configuration files and in the server configuration parameters.)
-   NX-695 (Force Poll a DCI from a DCI Summary Table)
-   NX-698 (Show user source and auth method in User Manager)
-   NX-701 (Filter in Event Configuration window)
-   NX-705 (View Syslog/Events from node's right click menu)
-   NX-707 (Failure to read single value for bar chart prevents others from displaying)
-   NX-709 (Match syslog/snmp traps from all zones)
-   NX-715 ("`%*`" string cause crash in DCI container formatting string)
-   NX-717 (`try`/`catch` in NXSL can catch runtime errors after try block)
-   NX-721 (Change the behavior of DefaultDCIPollingInterval and DefaultDCIRetentionTime)
-   NX-727 (CreateSNMPTransport always creates a transport)
-   NX-729 (Threshold script for exported templates doesnt import)
-   NX-730 (Importing EPP rules fails when there already are EPP rules with same ID present)

# 2.0-RC1

-   Fixed LDAP authentication issues with Active Directory
-   Fixed character encoding issues in LDAP user data
-   Java subagent improved
-   Fixed multiple issues with agent side data caching
-   Hash maps implemented in NXSL
-   Improved array implementation in NXSL
-   New NXSL function `ArrayToString`
-   New OS parameters and tables: `System.HandleCount`, `System.OpenFiles`, `Process.Handles`
-   Unified macros in all types of object tools
-   Server can be switched to case-insensitive login names mode
-   Implemented support of "command generates output" option for server commands
-   Network device driver for TelcoBridges gateways
-   Fixed memory leak in Qtech OLT driver
-   Java subagent plugin for Ubiquity/LigoWave device monitoring
-   Management console:
    -   Default object display mode can be set in map properties
    -   Map drill-down can be enabled in dashboard map elements
    -   Input fields in object tools
    -   Improved script editor for script library
    -   Interface speed displayed in interface object details and in "Interfaces" tab
    -   Symbolic name of interface type diplayed when known

## Fixed issues

-   NX-14 (Script validation before save in script editor)
-   NX-31 (Object tools by template)
-   NX-533 ("Command generates output" not working for "Server Command")
-   NX-609 (netxms-server .deb package help info bug)
-   NX-617 (Logarithmic scale not working in certain conditions)
-   NX-618 (Maps should save "Display objects as" server-side)
-   NX-624 (Put in order default SNMP configuration)
-   NX-626 (Support for SNMP devices with multi-component interface indexes)
-   NX-628 (Macro Substitution unification in Object Tools)
-   NX-631 (Disable all authentication configuration except disable for LDAP users.)
-   NX-632 (Add `%userpassword%` variable in object tools)
-   NX-633 (Separate in file manager file tail and fils show)
-   NX-634 (Send file tail updates in separate connection.)
-   NX-636 (Adding warning that large file will not be shown fully.)
-   NX-638 (Make detach LDAP user as a separate command. Open change password dialog after detach.)
-   NX-641 (Agent should create FileStore directory if not exist)
-   NX-643 (SNMP non-UTF8 collected data breaks SQL operations)
-   NX-644 (Increase size limit for configuration parameters)
-   NX-645 (Case-insensitive user names)
-   NX-650 (Update list of internal parameters in selection dialog)
-   NX-654 (DCI container value not shown for network map on a dashboard if this network map is not opened)

# 2.0-M5

-   Agent-side caching of collected data
-   Fixed bug in handling floating point Windows performance counters
-   Added "comments" attribute to NXSL "DCI" class
-   New NXSL function sha256
-   Fixed broken nxagent.sms SMS driver
-   Added support for SNMP traps over IPv6
-   Switched to SHA-256 for password hashing
-   Timestamp can be provided in nxpush and nxapush
-   New methods in NXSL class "Event": setMessage, setSeverity, setUserTag
-   Command line options for nxagentd to change effective user and group after start
-   Fixed occasional NXSL compiler crash on scripts with syntax errors
-   Errors in auto bind/apply scripts interpreted as "ignore" instead of "false" result
-   New core agent parameter `File.FolderCount`
-   Fixed broken active discovery
-   Improved system behaviour on large installations
-   Management console:
    -   Fixed broken VPN connectors configuration
    -   "Inverted values" option on line charts
    -   Filter in predefined graphs tree
    -   Values of selected DCIs can be shown on object overview page
    -   "Stacked" option added to line charts on dashboards
    -   In-place file rename in file manager
    -   Option to export data from line charts on dashboard to CSV file
    -   "Select all objects" option in network maps
    -   "Proxy node" option in DCI properties renamed to "Source node" to avoid confusion
-   Android Console:
    -   Added "capabilities" in node overview (changed to expandable list view)

## Fixed issues

-   NX-26 (Show some last values in overview page)
-   NX-439 (Object selection highlight not showing in maps)
-   NX-572 (Multiple server file upload in one operation)
-   NX-573 (Script DCI Unsupported when parameters en-quoted)
-   NX-583 (`--disable-64bit` have no effect when building on CentOS 6.6 x64)
-   NX-586 ("Create another" checkbox when creating a new node)
-   NX-589 (Paswords in DB are hashed without salt)
-   NX-590 ("Select all" function on network maps)
-   NX-598 (XMPP message send delay)
-   NX-606 (File parameters for directories)
-   NX-607 (Negate values on graph)
-   NX-608 (BeaconHosts reversed format)
-   NX-612 (Dashboard Line Chars - missing "Stacked")
-   NX-620 (`Service.Check()` reply with "can't connect" for second request on the same connection (windows only))
-   NX-621 (netsvc should send user agent header for http(s) checks)
-   NX-625 (Rename proxy node to source node on DCI configuration page)

# 2.0-M4

-   Script export/import
-   Object tools export/import
-   DCI summary tables export/import
-   Template hierarchy preserved during export/import
-   NXSL functions and classes to work with alarms
-   MEGATEC protocol support in UPS subagent
-   Fixed broken WoL functionality
-   Fixed broken PING subagent
-   Fixed database upgrade issues on MS SQL
-   IPv6 support in PING subagent
-   Network device driver can be manually selected for node by setting snmp.driver custom attribute
-   Added default melodies for alarms
-   Added option to play sound on alarm sound preference page
-   Interface objects can be used on network maps
-   Android Agent:
    -   Added support for Lollipop MR1 (v5.1)
    -   Updated support library
-   Android Console:
    -   Changed order of overview items to match Java console (node browser)
    -   Added MTU field in interface details (node browser)
    -   Updated support library

## Fixed issues

-   NX-461 (Template groups not exported)
-   NX-463 (Export scripts)
-   NX-500 (Export Object Tools)
-   NX-505 (Export DCI Summary Tables)
-   NX-521 (No alarm when or any notification when all BeaconHosts down)
-   NX-591 (Map appearance page not shown for access point objects)
-   NX-592 (Allow interface objects on network maps)
-   NX-595 (Extend eventlog parser for Windows CRITICAL events)
-   NX-596 (Change error message that appears when try to add node with existing IP)
-   NX-597 (diff thresholds activated after server restart)
-   NX-602 (New NXSL function to find alarm by key)
-   NX-603 (New imported events are not usable)
-   NX-604 (EPP export can be wrong)

# 2.0-M3

-   IPv6 support: communications, address information, topology
-   New NXSL functions: gethostbyaddr, gethostbyname, md5, sha1, AgentReadList
-   Added posibility to wakeup unmanaged node
-   Instance discovery separated from configuration polls
-   Instance discovery type "SNMP Walk - OIDs" sets instance name to OID value by default
-   `GPIO.PinState` parameter in Raspberry Pi subagent
-   Server housekeeping process runs once per day at fixed configurable time
-   Server housekeeping process performance optimization
-   Added driver for Qtech OLT switches
-   New agent parameter `FileSystem.Type(*)`
-   New agent parameters `Net.Resolver.AddressByName(*)` and `Net.Resolver.NameByAddress(*)`
-   Fixed broken SNMP proxy functionality in agent
-   Management console:
    -   Fixed broken popup menu actions on "Interfaces" tab
    -   Macro `%USERNAME%` can be used in object tools
    -   VLAN highlight on port selection in VLAN view
    -   "Use multipliers" option in DCI summary tables
    -   "Zoom to fit" action in network maps
    -   "Always fit layout to screen" option in network maps
    -   Last selected zoom level preserved on network map close
    -   Invisible dashboards and charts do not refresh itself automatically
    -   "Current" column in extended line chart legend
    -   Option to clone network maps
-   Android console:
    -   Implemented feature NX-568 (WoL)

## Fixed issues

-   NX-494 (Instance Discovery - method - SNMP Walk - Varbinds)
-   NX-497 (Add "Use multipliers" in DCI summary tables)
-   NX-506 (Tools accessible from DCI Summary Table)
-   NX-519 (MTU not reported in "Interfaces" tab)
-   NX-522 (Add `%username%` variable in object tools)
-   NX-537 (Filter in "Server Configuration Variables")
-   NX-542 (Server crash on dashboard edit)
-   NX-544 (PostEvent() should log unknown events)
-   NX-547 (Allow non-English event names)
-   NX-548 (VPN-Connector object, wrong labeling on register 'Subnets')
-   NX-549 (Do not refresh graphs or dashboards on invisible UI parts)
-   NX-550 (Remember map zoom size)
-   NX-551 (Allow processing of static FDB entries)
-   NX-552 (Некорректное отображение)
-   NX-555 (Forced DCI poll)
-   NX-556 ("Enable session agent" option in agent installer)
-   NX-557 (Missing "show filter" icon in server file manager)
-   NX-558 (System description for Windows 8 and Windows Server 2012 is incorrect)
-   NX-559 (Failed configuration poll should not initiate instance discovery)
-   NX-560 (Deleted subnets appear on automatically built maps)
-   NX-561 (Subnets are being replicated when they contain only objects with unknown network masks)
-   NX-562 (Fit map to screen)
-   NX-563 (VLAN selection when you click on a port)
-   NX-568 (WoL in Android App)
-   NX-570 (Use proxy agent for DNS names resolution for nodes in remote zones)
-   NX-571 (QtechOLT)
-   NX-574 (Remove policy tab from policy object properties)
-   NX-577 ("Current" column in line chart extended legend)
-   NX-579 (Multi-select Event Processing Policy delete bug)
-   NX-580 (Copy to clipboard option in last values view)
-   NX-581 (Rename Action in object tools as Agent command)
-   NX-582 (rename SNMP Table to SNMP List)
-   NX-584 (Find switch port is broken)
-   NX-585 (Housekeeping consumes all CPU)

# 2.0-M2

-   Fixed server hang issue on some Windows versions
-   Fixed SNMPv3 communication issue with HP A series switches
-   Fixed LDAP sync problems on Windows
-   Russian translation improved
-   New MIB added: SYMBOL-CC-WS2000-MIB
-   Subagent for reading DS18T20 and DS18S20 temperature sensors on Linux
    -   NX-479 (Wake-on-LAN possibly not working)
    -   NX-503 (DCI Data source - Internal - PingTime - Stuck at 10k)
    -   NX-515 (Device drivers not loaded on Windows if NetXMS installed into non-default location)
    -   NX-518 (PingTime Unsupported)
    -   NX-527 (Remove `inet_pton` dependency on Solaris)
    -   NX-528 (LDAP sync problems on Windows)
    -   NX-529 (Object tool download file does not work on web)
    -   NX-534 (nxsnmpwalk: v3 AES encryption - Error parsing PDU)
    -   NX-536 (nxagent dep package missing libnxsnmp)

# 2.0-M1

-   New hook script `AcceptNewNode` (can be used as additional filter for network discovery to avoid unnecessary communications)
-   SMS driver for Kannel gateway
-   Oracle subagent: added parameter `Oracle.CriticalStats.Deadlocks`
-   Reporting server improved
-   Code page option added to all client command line tools (nxalarm, nxevent, nxpush, nxsms)
-   New NXSL functions: GetNodeTemplates
-   New parameters in Windows agent: `System.Update.LastDetectTime`, `System.Update.LastDownloadTime`, `System.Update.LastInstallTime`
-   Network service response time can be monitored
-   Added driver for HP A-series and V-series switches
-   MIB compiler correctly handles `REFERENCE` keyword in agent capabilities section
-   Oracle Tuxedo monitoring subagent
-   Improved server performance with PostgreSQL
-   Alias and MTU collected and stored for interfaces
-   Server uses ipAddressTable and ipAddressPrefixTable to collect configured IP addresses when supported by monitored nodes
-   Management console:
    -   New dashboard element "DCI summary table"
    -   Cluster objects shown on status maps
-   Android console:
    -   Added date in X axis (graphs) when the time frame is greather that one day
    -   Added 10 minutes, 12 hours, 5 days, 30 days, last year options in draw graph for last values tab (5, 7, and 30 days asks for confirmation of long task execution)
    -   Fixed graphical problem (checkbox) in last values tab
    -   Support for KitKat Wear and Lollipop, updated support library v4

## Fixed issues

-   NX-36 (SNMP trap forwarding by agent in SNMP proxy mode)
-   NX-223 (Platform specific Object tools)
-   NX-259 (Can't list parameters from external subagent, when there are too many of them)
-   NX-330 (`File.*` should expand ` `` ` only for MasterServer)
-   NX-390 (Monitor Network Service response time as DCI)
-   NX-437 (`REFERENCE` clause in MIB files not supported)
-   NX-443 (A function to return all "Template" type parents of a node)
-   NX-471 (FileManager should allow bulk and directory download)
-   NX-476 (NotificationProcessor not updating cachedListenerList after reconnect)
-   NX-477 ("nxagentd" init script doesnt support "status")
-   NX-478 ("netxmsd" debian init script runs with "-D 5")
-   NX-479 (Wake-on-LAN possibly not working)
-   NX-481 (NXSL function PushData)
-   NX-482 (Command line tools always use ASCII as code page)
-   NX-483 (Auto-discovery pre-filter)
-   NX-486 (Script DCI parameters should be en-quoted)
-   NX-488 (Template export bug)
-   NX-490 (Multiple "Predefined graph" issues)
-   NX-492 (Separate syslog access right from event log access right)
-   NX-493 (Fix access control for monitors)
-   NX-495 (/32s showing in "Entire Network")
-   NX-501 (Add "Use multipliers" in map link Data Sources)
-   NX-502 (DCI Data source - Internal - PingTime Unsupported)
-   NX-504 (Delete, Manage, Unmanage - not working from Status Map)
-   NX-508 (Infinite loop in NetworkMap::updateObjects)
-   NX-509 (Crash in node overview)
-   NX-511 (Interface alias on the "Interfaces" object tab)
-   NX-512 (SNMPv3 communication problems with ESXi and Ubuntu 14)
-   NX-514 (SNMP data collection not working on SNOM phones)

# 1.2.17

-   New DCI source: NXSL script executed on server
-   Configurable node matching policy for built-in syslog server (controlled by SyslogNodeMatchingPolicy configuration parameter)
-   Oracle monitoring subagent improved (bugs fixed, new metrics)
-   nxalarm tool supports commands add-comment and get-comments
-   Source port number added to events generated from SNMP trap (available via "sourcePort" named parameter)
-   Jira link: added possibility to set project's component for issues being created
-   ICMP proxy can be set for nodes
-   New methods in NXSL classes Node, Interface, and NetObj: setStatusCalculation and setStatusPropagation
-   New attributes "slot" and "port" in NXSL class Interface
-   Can execute arbitrary NXSL script in context of node, cluster, subnet, or container object from management console
-   Improved network topology changes detection
-   Added driver for H3C switches
-   Management console:
    -   Can show alarms for multiple selected objects
    -   Fixed non-working ordering in event list in alarm details view
    -   Fixed bug with LDAP user system rights
    -   Added default search string for LDAP to select all objects: `(objectClass=*)`
    -   Added device geolocation tracking and display on map
    -   Filter in event processing policy editor
    -   Fixed bug with deletion of subnet with corrected IP
    -   Added command line option to open specific dashboard after login
-   Android console:
    -   NX-467 (Predefined graphs with autocolor plotted with the same color)
    -   Added node boot time to overview tab
    -   Fix bug in notifying connection point not found
    -   Fix bug in computing interface expanded list size (removed hardcoded values)
    -   Added manage, unmanage, set expected state (up, down, ignore) and find switch port to interface list
    -   Fix aesthetic problems in expandable list (graphs and interfaces list)
    -   Integration of new support library
    -   Target to new API version (20)

## Fixed issues

-   NX-27 (Object Tools URL Caption)
-   NX-64 (Potential crash on business service deletion)
-   NX-228 (Ability to use DCI for node status calculation)
-   NX-243 (Investigate warning)
-   NX-283 (Copy chart to clipboard and/or file)
-   NX-365 (Remove manage/unmanage from Dashboard, Template and Policy object menu)
-   NX-373 (Allow use of environment variables in agent configuration files)
-   NX-396 (Option to show only status icon on network maps)
-   NX-388 (Allow delayed agent policy installation)
-   NX-404 (User defined list DCI)
-   NX-593 (Connection history for nodes, IP and MAC addresses)
-   NX-424 (Alarm filter for multiple objects)
-   NX-427 (Show icon next to object name in the alarm browser)
-   NX-433 (Agent on AIX occasionaly reports wrong CPU I/O wait value)
-   NX-435 (Show / hide link labels in L2 Maps)
-   NX-438 (/32s showing up in 'Entire Network')
-   NX-441 (Implement "Command generates output" option for agent action type object tools)
-   NX-444 (Add script function DeleteCustomAttribute())
-   NX-447 (Unable to use 'DCI summary tables' with multiple 'Dummy' type DCIs)
-   NX-448 ('network\_map\_links' DB table columns too small)
-   NX-449 (Process events in Windows event log created between system boot and agent start)
-   NX-450 (Threshold violations shown for disabled DCIs)
-   NX-456 (IP Mask is not shown in interface list)
-   NX-464 (Escape mode for commands executed on server)
-   NX-469 (Proxy ICMP requests without zoning enabled)

# 1.2.16

-   Fixed database upgrade issues
-   Fixed packaging issues
-   Fixed bug causing outdated peer information on interface objects
-   Fixed bug with upload to agent default path from server file store
-   Instance display name for DCIs created via instance discovery
-   DCIs created via instance discovery can be combined by instance into one chart on performance tab
-   Transformation script terminated by "abort" call will not generate `SYS_SCRIPT_ERROR` event
-   Database manager can detect and fix missing IData and TData tables
-   NXSL:
    -   String concatenation operation interprets NULL value as empty string instead of throwing runtime error
    -   Fixed incorrect processing of ilike, match, and imatch operators
    -   Added try / catch operator
-   New MIBs added: NETUP-MIB

## Fixed issues

-   NX-293 (Summary DCI tables: missing values for some hosts)
-   NX-312 (nxdbmgr should check existence and permissions on idata tables)
-   NX-374 (try / catch (or other runtime error handling) in NXSL)
-   NX-428 (Agent crashes if root folder set to / in file manager subagent)
-   NX-429 (Table DCI cannot be saved)
-   NX-430 (Disk space percentage always rounded on AIX)

# 1.2.15

-   LDAP support
-   Event names support in nxevent
-   Previous state parameter added to `SYS_NODE_UP` event
-   Added file management subagent (filemgr.nsm)
-   Removed agent configuration parameter EnableArbitraryFileUpload
-   New NXSL class "Zone"
-   New attributes "zone" and "zoneId" in NXSL classes "Node" and "Interface"
-   Syslog records from unmanaged nodes do not generate events
-   Syslog node matching improved
-   New access rights for nodes:
    -   Download File (download file from agent to local workstation)
    -   Upload File (upload file from local workstation to remote node)
    -   Manage Files (move, rename and delete files on remote node)
-   Management console:
    -   "Commands" box on node overview page made configurable
    -   Object tools can have icons
    -   "Last value" type gauge can show non-numeric values
    -   "Trusted Nodes" property page shown for condition objects
    -   Network map content can be copied to clipboard
    -   Perspectives export/import
    -   Topology related options in node's context menu grouped in "Topology" submenu
    -   Added specialized view for IP routing table
    -   Added specialized view for switch forwarding database
    -   Agent configurations manager implemented
-   Android Console:
    -   Added option in preference to show/hide legend in graphs
    -   Object comments displayed
    -   Added "Navigate to" option for objects with geolocation set

## Fixed issues

-   NX-105 (\\ in file name processed as formatting character by logger)
-   NX-125 (Cannot use SNMP OIDs longer then 255 characters)
-   NX-457 (Support for multiple tile providers)
-   NX-349 (Driver for MikroTik wireless devices)
-   NX-369 (Comments for DCIs)
-   NX-372 ("Unable to create raw socket for ICMP protocol" on Windows 2008)
-   NX-380 (NXSL: Deadlocks when CreateContainer called from Container's Auto-Bind Filtering script)
-   NX-389 (Allow agent deployment restart)
-   NX-391 (Resolve DNS hostname each time on Status Pool - option)
-   NX-401 (NXSL GetNodeParents result is empty)
-   NX-402 (NXSL Access to zone information)
-   NX-407 (Broken creation of double link and link with bend points on map)
-   NX-409 (Add actions to show switch FDB and routing tables)
-   NX-410 (Incorrect process command line handling on Linux)
-   NX-411 (Wrong integer DCI presentation in "Last Values")
-   NX-413 (Cannot replace existing image in image library)
-   NX-416 (Hide misleading error message (unknown symbol))
-   NX-417 (File Manager do not handle symlinks)
-   NX-418 (Oracle SQL query failed when saving line chart with lot of elements)
-   NX-419 (DCI proxy node ignored by instance discovery)
-   NX-421 (Link state based on two objects)
-   NX-423 (Limit amount of items displayed in Alarm browser)
-   NX-425 (Show object comments in Android Console)

# 1.2.14

-   STP (Spanning Tree Protocol) information used for topology discovery
-   Information source for interface peers (CDP, STP, etc.) shown in console
-   New NXSL function inList
-   New NXSL operator abort
-   New methods in NXSL class Node: enableAgent, enableConfigurationPoll, enableIcmp, enableSnmp, enableStatusPoll, enableTopologyPoll
-   Fixed server crash if SNMP proxy unavailable
-   New MIBs: AIRESPACE-REF-MIB, AIRESPACE-SWITCHING-MIB, AIRESPACE-WIRELESS-MIB, FROGFOOT-RESOURCES-MIB, MIKROTIK-MIB
-   SMS driver for websms.ru service
-   Macro expansion supported in pattern in agent parameters `File.Size` and `File.Count`
-   Attribute "instance" added to NXSL class "DCI"
-   Added "L" extension to DCI custom schedules
-   Traps from unmanaged nodes ignored
-   Fixed repeated threshold violation events after server restart
-   Added driver for MikroTik routers
-   Added driver for Ubiquity Networks wireless access points
-   Added driver for Cisco Wireless Controller 4400 (former Airespace)
-   Wireless controller and access point support improved
-   Log monitoring subagent sends Windows event source, severity, and code to the server as part of NetXMS event
-   DB/2 driver and monitoring subagent included into Windows installation package
-   Management console:
    -   DCI values can be shown on network map links
    -   DCI value can be shown on map as immage, that checnges depending on DCI value
    -   DCI value can be shown on map as a text
    -   Colored background for DCIs with active thresholds in DCI summary tables
    -   IP route visualisation improved
    -   On table DCI threshold property page columns can be chosen from dropdown
-   Reporting server rewritten from scratch

## Fixed issues

-   NX-46 (Use Spanning Tree data for network discovery)
-   NX-287 (Manually added elements on automatic maps)
-   NX-361 (Access to alarm log denied despite having "View alarms" Object Access Right)
-   NX-367 (VPN connectors not shown on topology map)
-   NX-368 (Deadlock in java web client - on disconnection)
-   NX-377 (Linux agent cuts decimal part off of `FileSystem.UsedPerc` and FreePerc DCIs)
-   NX-383 (Ability to return "DCI collection error" from transformation script)
-   NX-384 ("L" extension in the custom schedule)
-   NX-385 (Traps from unmanaged nodes sould be ignored)
-   NX-395 (First octet of cluster network address is replaced by 255)
-   NX-397 (Legend of combined graphs on perfomance tab doesn't have appropriate units)

# 1.2.13

-   Improved layer 2 topology discovery performance
-   Special handling of incorrect LLDP data provided by some D-Link switches
-   Optimizations in NXCP processing
-   Added driver for Cisco Small Business switches
-   Improved file retrieve from agent
-   Windows agent: added service list and service table (`System.Services`)
-   Fixed bug with SQL initialization script generation on HP-UX
-   Fixed Oracle DB initialization error
-   New macro %K (alarm key) in event actions
-   Management console:
    -   Implemented alarm sounds
    -   Fixed "broken pipe" errors
    -   Macros with alarm data in object tools
    -   Added option "Manage image library" in user access rights property page
    -   Fixed image upload in web console
-   Added support for sticky acknowledge in nxalarm tool
-   Fixed bug causing excessive memory usage by AIX agent
-   Fixed bug with interface status detection if agent runs in Solaris zone
-   Fixed agent crash if HTTPS service status requested
-   Android Console:
    -   Fix bug missing hide notification alarm in status bar
    -   Implemented "Font size in graph/dashboard sessions" (Feature NX-188)

## Fixed issues

-   NX-82 (Sound notifications for alarms (as in Legacy Console))
-   NX-188 (Customize font size in graph/dashboard sessions)
-   NX-294 (Graphs: add log. scale to Dashboard and Performance graphs)
-   NX-297 (Charts: make periods configurable for Performance tabs & Dashboards)
-   NX-300 (SnmpCheckCommSettings slows down server startup?)
-   NX-311 (Add every new discovered node to container)
-   NX-314 (Show unmanaged nodes without interfaces in Entire Network)
-   NX-318 (Windows DCI parameter "`System.Memory.Physical.Free`" reports available memory amount, not free memory amount)
-   NX-335 (File download with tail should detect that connection with agent is broken)
-   NX-346 (DCI selection dialog should save position)
-   NX-347 (Multiple selection in DCI selection dialog)
-   NX-360 (Show `Server.TotalEventsProcessed` in GUI, automatically collect Events per second DCI on management node)

# 1.2.12

-   Support for MetaSystem UPS in UPS subagent
-   Timed (temporary) alarm acknowledgement
-   New subagent DBQuery - replacement for ODBCQuery
-   DCI access functions in NXSL works correctly with table DCIs
-   Fixed bugs with instance discovery DCIs created from templates
-   New property "runtimeFlags" in NXSL class "Node"
-   New event `SYS_IF_PEER_CHANGED` (sent when peer change detected in interface)
-   New system permission: Manage Image Library
-   Object level access control can be enabled for logs
-   New NXSL function FindAllDCIs
-   Driver for Allied Telesis switches improved
-   Management console:
    -   Fixed bug with red zone display in "last value" dashboard element
    -   Edit and delete for alarm comments are working now
    -   Fixed Y axis range can be set for line and bar charts
    -   In alarm menue are not shown incompatible for selected alarm statuses.
    -   Alarm status flow can be changed to strict (terminate status can be set only after alarm is resolved). To change flow set "StrictAlarmStatusFlow" parameter to 1.
    -   SNMP MIB loaded into memory on first access
-   Android Agent:
    -   Implemented "Connection notification" in status bar (feature NX-323)
    -   Fix bug in resetting switch preference (settings)
-   Android Console:
    -   Fix bug in resetting switch preference (settings)
    -   Implemented "Entire network" root (feature NX-324)
    -   Manage last alarm from status bar: acknowledge, resolve, terminate (only for Android >= 4.1)

## Fixed issues

-   NX-52 (Timed alarm acknowledgement)
-   NX-61 (Add "disable" option to object tools)
-   NX-205 ("index" in NXSL can't find last char)
-   NX-208 (PVS-Studio)
-   NX-268 (Enable "Move to another group" for multiple selected items)
-   NX-271 (Filtering script is not propagated when Instance Discovery DCI applied from template)
-   NX-285 (Timeout is too short on log query)
-   NX-317 (configure PID file custom location does not work)
-   NX-321 (SMS Sending to Multiple Phone Number)
-   NX-323 (Report mobile agent connection problems in notification bar)
-   NX-324 (Entire Network browser)
-   NX-325 (Fixed upper limit for line charts)
-   NX-326 (Generate event on peer change)
-   NX-328 (`File.*` should resolve environment variables)
-   NX-329 (New DCI — zombies count)
-   NX-332 (Coredump after Ctrl+C)
-   NX-339 (Agent registration not working)
-   NX-342 (Load MIB file into memory only on first access)
-   NX-344 (User should not see log items from objects he has no access to)
-   NX-345 (ImageLibrary should have ACL option)

# 1.2.11

-   Thresholds can be defined as NXSL scripts
-   XMPP messaging support
-   "Do not save collected data to database" option for data collection items
-   Added "follow" option to "download file" object tools
-   New attribute "driver" for NXSL class "Node"
-   Management console:
    -   Stacked line charts implemented
    -   Authentication by certificates supported by Java console
    -   Russian translation improved

## Fixed issues

-   NX-2 (New threshold type: script)
-   NX-51 (Add certificate authentication to Java console)
-   NX-261 ("No storage" option for table DCIs)
-   NX-313 (Can't compile internal libexpat)
-   NX-316 (Linux subagent should ignore rootfs record in /etc/mtab)
-   NX-319 (Node removal from template process fails)

# 1.2.10

-   Event processing policy rules can be exported and imported
-   NXSL:
    -   Implemented post-increment and post-decrement for array elements
    -   New functions: GetDCIValues
-   Server's ICMP ping timeout can be configured
-   DB/2 monitoring subagent
-   DB/2 supported as backend database
-   Table DCIs can be used in condition objects
-   nxapush can push data on behalf of other nodes
-   Transformation script can be run on aggregated DCIs
-   Unknown SNMP trap sources can be automatically added as nodes
-   Syslog processing optimized for performance
-   Default shared secret for agents can be configured
-   Driver for Ping3 devices
-   Driver for Allied Telesis switches
-   Agent installer on Windows automatically adds firewall exception
-   Database migration tool
-   Additional parameters in Solaris platform sub-agent
-   Management console:
    -   New command line option -fullscreen
    -   Option to draw borders around each value in "gauge" dashboard elements
    -   Sorting by value in "Last Values" view takes data type into consideration
    -   "Nodes" tab in object details view for subnets and containers
    -   "Address Map" tab in object details view for subnets
    -   Czech and Russian localization

## Fixed issues

-   NX-68 (Add support for DB/2 as backend database)
-   NX-117 (SNMP Trap Monitor broken)
-   NX-177 (Export and import event processing policy)
-   NX-224 (Device discovery from SNMP traps)
-   NX-232 (Custom tooltip for alarm list with more details)
-   NX-246 (Legend not working correctly using Text Gauges)
-   NX-247 (shared lib suffix is always ".so", should ".dylib" on OS X)
-   NX-248 (Cannot Connect to Postgres running on alternative port (not 5432))
-   NX-249 (PDH error 800007D5 (No data to return) in agent's log)
-   NX-250 (Driver for Allied Telesis switches)
-   NX-254 (Oracle agent crashes after Oracle service restart)
-   NX-257 (Wrong configure.ac and no sql files as result)
-   NX-260 (Copy to clipboard and export to CSV for data collection configuration)
-   NX-263 (Delete installer files after agent upgrade)
-   NX-265 (Option to create interface DCIs in bits instead of bytes)
-   NX-401 (NXSL GetNodeParents result is empty)
-   NX-284 (NXSL function to get n last DCI values from database)
-   NX-414 (Oracle monitoring agent should print more diagnostics)
-   NX-286 (Status indicators with full color range)
-   NX-288 (Configurable ICMP ping timeout at status poll)
-   NX-301 (Remove server dependency for an existing log file)
-   NX-302 (NetXMS server accepts directories as configuration files)

# 1.2.9

-   Templates can be applied on clusters
-   Filters for automaticaly populated network maps
-   User-defined constants in NXSL
-   New methods deleteColumn and deleteRow in NXSL class Table
-   New NXSL functions: chr, ord
-   HTTPS support in port checker subagent
-   Added MIBs for Nortel/Trapeze Wireless security switches
-   New MIBs: BAY-STACK-NOTIFICATIONS-MIB, SUN-HW-CTRL-MIB, SUN-HW-TRAP-MIB, SUN-PLATFORM-MIB
-   Management console:
    -   New dashboard elements: status map and table value

## Fixed issues

-   NX-168 (User-defined constants in NXSL scripts)
-   NX-219 (Map object permanently selected when the grid is shown)
-   NX-221 (Add HTTPS support to portcheck subagent)
-   NX-222 (Templates with table DCIs not exported correctly)
-   NX-226 (Include nxpush into agent deb package)
-   NX-311 (Add every new discovered node to container)
-   NX-229 (UNICODE build fails on Solaris)
-   NX-230 (Status map as dashboard element)
-   NX-234 (EncryptionContext persists between connects)
-   NX-235 (Filtering script for automatic network maps)
-   NX-236 (Server crash on Solaris)
-   NX-237 (SNMP trap template for Nortel/Avaya switches)
-   NX-238 (Unable to move icon on map when grid is shown)
-   NX-239 ([Patch included] EncryptionContext is not thread safe)
-   NX-339 (Agent registration not working)
-   NX-240 (add "reset password" feature to nxdbmgr)
-   NX-242 (Wrong CPU utilization data on Ubuntu Server 12.04 LTS)

# 1.2.8

-   Support for data collection using SM-CLP protocol
-   Aggregated DCI values on cluster objects
-   Transformation scripts for table DCIs
-   Support for multi-column keys (instances) in table DCIs
-   Implemented SNMP table DCIs
-   Configurable DCI summary tables
-   Default background color for new network maps made configurable
-   Logged in users cannot be deleted
-   Empty containters have "Normal" status instead of "Unknown"
-   New NXSL functions: AgentReadTable, DeleteObject, GetDCIRawValue
-   Map objects can have status calculated from contained objects' status
-   SNMP trap listener port now configurable
-   HP-UX agent improved
-   Some D-Link MIBs added to distribution
-   Debian binaries built in UNICODE mode
-   Management console:
    -   Simplified table DCI configuration
    -   Charts can be created from table data
    -   Severity filter in dashboard element "Alarm Viewer"
    -   Zoom level can be configured for "Network Map" dashboard elements
    -   Values of custom attributes can be used in object tools
    -   Vertical orientation for dial chart elements
-   Web UI:
    -   Single sign-on support using CAS
    -   Configuration file nxmc.properties can be placed outside of war file
    -   Workbench layout and user preferences saved between sessions

## Fixed issues

-   NX-33 (Tables support in NXSL)
-   NX-34 ("Test" button on DCI transformation property page is not working)
-   NX-161 (Cluster DCIs in dashboards)
-   NX-164 (Support for SNMP tables)
-   NX-262 (GPS tracking)
-   NX-204 (Map object status based on objects on map)
-   NX-206 (NXSL function to retrieve last raw DCI value)
-   NX-207 (Add ability to use custom attribute values in object tools)
-   NX-209 (Situation attributes not shown in console)
-   NX-212 (Support for SNMP devices without standard MIBs)
-   NX-214 (UI option to configure interface "exclude from topology" flag)

# 1.2.7

-   Simplified configuration of DCIs based on Windows performance counters
-   Basic software inventory
-   Network discovery improved
-   Status of zone's proxy node now used in "node down" event correlation
-   Configurable default DCI retention time and polling interval
-   New NXSL functions: CreateNode, GetSumDCIValue
-   New NXSL operator @ - safe get object's attribute
-   New MIBs added: ASTARO-MIB, CPQHOST-MIB, CPQPOWER-MIB
-   Special support for wireless switches
-   Driver for Motorola/Symbol wireless switches
-   Fixed bugs in template export/import
-   Database manager: Fixed bugs in database export
-   New parameters for Windows Security Center provided by WMI subagent:
    -   `System.AntiSpywareProduct.Active`
    -   `System.AntiSpywareProduct.DisplayName`
    -   `System.AntiSpywareProduct.UpToDate`
    -   `System.AntiVirusProduct.Active`
    -   `System.AntiVirusProduct.DisplayName`
    -   `System.AntiVirusProduct.UpToDate`
    -   `System.FirewallProduct.Active`
    -   `System.FirewallProduct.DisplayName`
    -   `System.FirewallProduct.UpToDate`
-   Management console:
    -   "Export to CSV" option added to most tabular data views
    -   Auto login option for web console
    -   Last values of selected DCIs can be shown in object tooltips
        on network maps

## Fixed issues

-   NX-59 (Implement data export from log viewer)
-   NX-165 (Unable to unselect group box)
-   NX-190 (Add support for per-VLAN forwarding databases on Cisco Catalyst switches)
-   NX-193 (Implement MIB selection dialog similar to legacy console)
-   NX-194 (Configurable default value for data collection interval and retention time)
-   NX-195 (Incorrect selection in object tree after console start)
-   NX-196 (Implement uniform handling of Windows security log on all Windows versions)
-   NX-200 (Agent reply with uninitialized buffer when ExetnalParameter can't start)
-   NX-201 (Portcheck: Unicode build do not recode "MAIL FROM" into multibyte)
-   NX-268 (Enable "Move to another group" for multiple selected items)
-   NX-202 (FreeBSD subagent incorrectly not supporting swap/vm data collection (patch))

# 1.2.6

-   DCI instance discovery
-   nxshell: Python-based client-side scripting
-   Array initializers in NXSL
-   NXSL function PostEvent can use event names instead of event codes
-   New NXSL functions: AgentReadParameter, CreateDCI, ManageObject, SetInterfaceExpectedState, UnmanageObject
-   Management console:
    -   Network map functionality in web console now in sync with desktop version
    -   Alarm details view improved
    -   Configurable chart ordering on performance tab
    -   Syslog parser editor working correctly
-   Android Console:
    -   Force reconnection after changing settings (NX-189)
    -   Fixed bug in showing predefined graphs and dashboards (NX-187)
    -   Added support for mobile device objects
    -   Added geolocation info in overview tab
-   64bit interface counters in Windows agent
-   Improved LLDP support
-   Driver for D-Link switches
-   Event parameters passed as arguments to action scripts
-   PING subagent: targets can be specified using DNS names
-   Android Agent:
    -   Changed name of configuration parameters (NB needs reconfiguration of agent!!!)
    -   New location strategy: relay on updates from other apps or force update (frequency, duration and provider selectable).
    -   Show location strategy on home screen.
    -   Fixed bug in automatic connection on first start when agent was disabled
    -   Override for connection schedule on detecting change of connectivity (selectable)
-   New MIBs added: LLDP-EXT-DOT1-MIB, LLDP-EXT-DOT3-MIB

## Fixed issues

-   NX-163 (Extended alarm message)
-   NX-170 (Possibility to set default icon type for network map)
-   NX-172 (CreateDCI function in NXSL)
-   NX-174 (Custom Schedule not saved)
-   NX-176 (Adding image to map fails)
-   NX-178 (Could not create the view: Task already scheduled or cancelled)
-   NX-179 (Container source for alarm log)
-   NX-181 (Basic device info not resent)
-   NX-182 (UI hangs after password change on login)
-   NX-184 (Server complaint about too big packet when agent reply with huge list of supported DCIs)

# 1.2.5

-   Topology-based event correlation improved
-   Network discovery improved
-   Mapping tables
-   New NXSL functions: ceil, floor, round, format, map
-   Management console:
    -   "Alarm Details" view
    -   "Area" option implemented on line charts
    -   Multiple DCIs can be combined on one graph on "Performance" tab
    -   New dashboard element: separator
    -   DCIs can be created from MIB Explorer
    -   Textual conventions for selected MIB object displayed in MIB explorer
    -   Fixed bug with chart titles in dashboards
    -   "Snap to grid" and "Align to grid" options in network maps
    -   Improved Y-range adjustment in line charts
    -   Improved tooltips in line charts
    -   Custom logo can be set on login screen in web console
    -   Fixed performance and stability issues with image library
-   Android client:
    -   Select all/unselect all in alarms list
    -   Multipliers for graphs and last values: binary (power of two) and decimal (power of ten)
    -   Show number of pending alarms in home screen
-   API for creating embedded application agents
-   Initial (alpha) version of mobile agent for Android devices

## Fixed issues

-   NX-5 (MS SQL DB driver should find available native client)
-   NX-23 (Option to create DCI directly from MIB browser)
-   NX-25 (Show OID textual convention in MIB browser)
-   NX-103 (Alarm details view)
-   NX-121 ("Reload image library" is loaded over and over after changing something in the image library)
-   NX-129 (AIX: Unable to retrieve interface status via agent)
-   NX-130 (AIX agent does not return all IP addresses configured on interface)
-   NX-139 ("Snap to grid" feature for network maps)
-   NX-142 (Poll count for status change for network service objects)
-   NX-144 (Compilation warnings on Solaris 10)
-   NX-145 (Do not collect unnecessary information from nodes during network discovery)
-   NX-147 (Improve automatic event correlation based on network topology)
-   NX-153 (Map background set to geo map causes NPE in web UI)
-   NX-154 (Node remains unreachable after IP address change)
-   NX-155 (Accept traps from agents in different zones)
-   NX-156 (Bug in auto connection on connectivity change with scheduler disabled)
-   NX-159 (Option menu in Alarms activity doesn't work)
-   NX-160 (Implement basic style in UI)
-   NX-162 (Typing OID in MIB explorer not selecting elements in MIB tree)

# 1.2.4

-   New global variable $dci in transformation scripts
-   Management console:
    -   Command line options for automatic connect
    -   Container type objects can be expanded/collapsed by double click
        in the object tree
    -   Maps and dashboards can be opened by double click in the object tree
    -   Line charts can be opened by double click on DCI in last values view
    -   Implemented seed-based network maps
    -   Decoration elements on network maps can be moved and resized
    -   Object details view can be opened from alarm's context menu
    -   Custom time intervals can be set in line chart properties
-   NXSL: implemented short-circuit evaluation of logical expressions (&& and ||)
-   New attribute "isLocalMgmt" in NXSL "Node" class
-   New parameter `Icmp.PingStdDev` in PING subagent
-   Cisco Catalyst 3550 supported by CATALYST driver
-   Intervals of less than a minute can be defined with custom DCI schedules
-   Agent parameters `File.xxx` (`File.Size`, etc) now support strftime style macros for current date/time (similar to file name in log parser)
-   Android client:
    -   Restructured settings activity
    -   Alarm status icon notification configurable by settings (independent from playing the sound assigned to the category)
    -   Horizontal scrollable tabs for node info activity (tabs are no more compressed to show all together)
    -   Fixed bad format for DCI value in last values tab
    -   Scheduler for "passive" connection", parameters:
        -   Enable scheduler: enables the scheduler, if off program exposes the previous behaviour
        -   Interval: how many minutes have to elapse before trying to connect to server
        -   Duration: how many minutes connections has to be kept on
        -   Enable daily scheduler: if off, the above values are applied to the whole day. If on they will be applied only to the specified interval (for the whole week).
        -   Daily on: start daily time to apply scheduler values
        -   Daily off: stop daily time to apply scheduler values

## Fixed issues

-   NX-29 (Local commands with arguments works only with "Command generates output" option)
-   NX-93 (Truncated object tooltip texts in network maps)
-   NX-101 (Add support for Cisco Catalyst 3550)
-   NX-106 (Status indicator in dashboard causes web console to crash)
-   NX-111 (Local commands with arguments works only with "Command generates output" option)
-   NX-138 (netxmsd crash in script processing)

# 1.2.3

-   Improved LLDP support
-   New "Find IP address" function (find node's switch port by IP address)
-   Set MAC address for "unknown" interfaces from ARP cache
-   Detection of IP address change for nodes without agent and SNMP
-   Agent on Windows is in UNICODE
-   UNICODE build supported on Linux and FreeBSD
-   ifXTable used when possible for interface traffic DCIs creation
-   Server can be configured to use DNS host names instead of FQDN for newly discovered nodes
-   Script hooks for configuration poll
-   Management console:
    -   Configurable date and time format
    -   Background color can be set for network maps
    -   Different connection routing algorithms for network maps
    -   Fixed incorrect display of string data in DCI history
    -   Added "copy to clipboard" action in MAC address search reults
    -   Added "copy to clipboard" action in interface tab
    -   Double click in MIB explorer walk results selects OID in tree
    -   Fixed status indicator update problems in object browser
    -   Fixed dashboard navigator refresh issues
    -   Object tools execution on multiple objects
    -   Implemented "Clear collected data" action for DCIs
    -   Fixed missing scrollbar issue in VLAN view
-   Added commands "get" and "set" to nxdbmgr to manager server configuration variables
-   New NXSL function: RenameObject
-   Web interface look is more consistent with desktop client
-   Fixed critical bug in NXSL interpreter (incorrect execution of operation `--`)
-   Android client:
    -   Added: nodes and dashboards container status in home screen reflect children status
        (icon changes on WARNING, MINOR, MAJOR, and CRITICAL).
    -   Added: interfaces tab under node info activity
    -   Added: handle alarm sticky acnowledge action and state.
    -   Added: sort of alarm list in node info tab.
    -   Added: multiple selection for actions on alarms list.
    -   Added: sort by node name on alarm list.
    -   Fixed bug: added protection to null pointers
    -   Fixed bug: hidden wrong menu item in alarms tab

# 1.2.2

-   New alarm state - "Resolved"
-   Added drivers for Cisco ESW and Dell PowerConnect switches
-   Added MIBs for Dell PowerConnect switches
-   New event processing macros: %g and %I
-   Management console:
    -   In port view ports are colored according to physical port state
    -   Interface IP shown in connection point search results
    -   Interface IP and MAC shown in "Interfaces" tab
    -   Added "Status Map" view
    -   Added option to hide unsupported DCIs from "Last Values" view
    -   Added option to indicate data collection errors in "Last Values" view
    -   Added "copy to clipboard" function in log viewers and monitors
-   Android client:
    -   Dashboards implemented
    -   Node status/configuration/topology poll implemented
-   NXSL:
    -   Global variables can be declared in script code
    -   New functions: GetConfigurationVariable, GetObjectParents, GetObjectChildren, sleep
    -   New attribute "guid" in classes Interface, NetObj, and Node
-   AIX Subagent:
    -   New parameters available: `System.CPU.PhysicalAverage.*`
-   Fixed bugs:
    -   NX-? (Config file with CRLF loaded incorrectly on UNIX)
    -   NX-? (Unable to bind object in WebUI)
    -   NX-? (Graph colors can be ignored in dashboards)
    -   NX-? (Object deletion may not be immediately reflected in console)
    -   NX-? (Unable to upload file into image library from Web UI)

# 1.2.1

-   Implemented dashboard export/import
-   New NXSL functions for direct SNMP access
-   New NXSL functions for getting min, max, and average DCI value for period
-   Fixed memory leak in NXSL functions gmtime and localtime
-   Fixed memory leak in configuration poller
-   Added driver for HP E-series (ProCurve) switches
-   Implemented "sticky" alarm acknowledgements
-   Added option to disable automatic node unbinding from containers
-   Added option to disable automatic template removal
-   Added events for automatic container binding and unbinding
-   Added events for automatic template apply and remove
-   Java console:
    -   Configuration export implemented
    -   Added object status indication bar in object browser
    -   Added filtering by IP address and comments in object browser
-   Web UI:
    -   Windows installer improved
    -   Line charts improved
-   Agent now allows to define management server address as subnet
-   Additional I/O parameters in Solaris agent
-   Fixed bugs with static agent build

## Fixed issues

-   NX-333 (Add windows service descriptions for both server and agent)
-   NX-240 (add "reset password" feature to nxdbmgr)
-   NX-343 (Relative time filters in logs)
-   NX-353 (When disabling and enabling back dci in template it doesn't propogate)

# 1.2.0

-   Number of polls required for status change can be set individually for each interface
-   New NXSL functions and object properties for accessing topology information
-   New NXSL function FindObject
-   New NXSL functions for object creation and binding
-   Added option to set native agent port on node creation
-   Added support for INFORM messages in SNMP trap receiver
-   Implemented automatic creation of ChildStatus DCI when Network Service object created for Node
-   Implemented concept of "expected" interface state
-   Added option to use DNS names instead of IP addresses as primary host name for discovered nodes
-   Added possibility to add parameters and/or specify entry point in scripts called via %[] macro
-   Implemented alarm comments
-   Initial support for multi-valued (tabular) DCI
-   Java console:
    -   Added alarm history log viewer
    -   Time interval for line charts on dashboards made configurable
    -   Dashboard configuration improved; all dashboard elements now can be configured from GUI
    -   New tab for container objectss where threshold violations for underlying nodes are shown
    -   Multiple dashboards can be displayed in a loop (like slide show)
    -   Fixed problems with line chart configuration saving in perspective
    -   Resolved issue: Reports not working on Windows
    -   Resolved issue: Cannot delete non-existent object from event processing policy
    -   Resolved issue: No confirmation shown for object tools with "confirm before execution" flag
    -   Resolved issue: EPP editor do not support 'Negate cell'
-   Web UI:
    -   All functionality from Java console implemented
    -   Windows installer for web interface
    -   Resolved issue: NetXMS session not closed when web session is expired

## Fixed issues

-   NX-? (Internal libexpat failed to compile on debian5)
-   NX-? (Build failed on Solaris 11)
-   NX-? (Incorrect interface status reported by agent on FreeBSD)
-   NX-? (Database upgrade problems if SQLite used as backend database)

# 1.1.10

-   Completely new web interface
-   New action type: execute NXSL script
-   Changed default timeout for service checking subagent
-   Added Oracle monitoring subagent
-   Added option to force creation of character string instead of hex string in SNMP trap mapping
-   Java console:
    -   Log viewers greatly improved
    -   Added missing DCI option "process all thresholds"
    -   Added missing "interconnect networks" property for cluster objects
    -   Added possibility to add and edit names on map link
    -   SNMP trap monitor
    -   "Query" button implemented in agent parameter selection dialog
    -   Implemented syslog parser configuration
    -   Resolved issue: Cannot delete non-existing object from map
    -   Resolved issue: Template filtering script is lost when template is renamed
    -   Resolved issue: Tab character not stripped from DCI parameter configuration and server reports "unsupported"
    -   Resolved issue: Map background not drawn beyound viewport
    -   Resolved issue: Node under cluster not shown in object selection dialog
    -   Resolved issue: "Cluster resource" field unavailable for DCI on cluster node
    -   Resolved issue: Reports not working on Windows
    -   Resolved issue: extra new line characters in local command output
-   New format specifiers in nxalarm: `%x` and `%X`
-   New MIBs added: BAY-STACK-ADAC-MIB, BAY-STACK-ARP-INSPECTION-MIB, BAY-STACK-DHCP-SNOOPING-MIB, BAY-STACK-ECMP-MIB, BAY-STACK-ERROR-MESSAGE-MIB, BAY-STACK-LACP-EXT-MIB, BAY-STACK-MULTICAST-FLOODING-MIB, BAY-STACK-OSPF-EXT-MIB, BAY-STACK-PETH-EXT-MIB, BAY-STACK-RADIUS-MIB, BAY-STACK-SOURCE-GUARD-MIB, BAY-STACK-STATS-MIB, BAY-STACK-VRRP-EXT-MIB, FOUNDRY-CAR-MIB, FOUNDRY-SN-AGENT-MIB, FOUNDRY-SN-IP-MIB, FOUNDRY-SN-OSPF-GROUP-MIB, FOUNDRY-SN-ROOT-MIB, FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB, FOUNDRY-SN-SWITCH-GROUP-MIB, FOUNDRY-SN-TRAP-MIB, FOUNDRY-SN-VSRP-MIB

## Fixed issues

-   NX-? (Subnet objects not placed correctly under zones)
-   NX-? (No retention time for alarm history)

# 1.1.9

-   Fixed server crash during startup
-   Fixed failed SQL queries if MS SQL used as backend
-   FIxed "Resource not available" error when trying to view VLANs on a switch
-   Bugfix: data collection configuration not available for cluster objects
-   Bugfix: cannot remove package from list if file does not exist
-   Bugfix: temporary file not deleted after external parameter execution
-   Bugfix: cannot change node's "force encryption" flag from Java console
-   Bugfix: cannot execute local commands with spaces in path
-   Template can be moved between template groups
-   Added "refresh" function to alarm browser in Java console

# 1.1.8

-   New node properties: "disable topology polling" and "disable discovery polling"
-   Changes and improvements in Java console:
    -   Implemented embedded web page element type in dashboards
    -   Implemented alarm viewer element type in dashboards
    -   Dashboard cloning
    -   Syslog monitor
    -   Event monitor
    -   Implemented status calculation/propagation object property page
    -   Execution of "local command" type tools improved
    -   Dial charts improved
    -   Fixed object selection bug in network maps
    -   Implemented agent package management and deployment
-   Added common driver for Cisco Catalyst switches with CISCO-STACK-MIB support
-   Implemented event identification by name in sendEvent API
-   RADIUS authentication now supports passwords up to 128 characters long (was up to 16)
-   Fixed server crash on Windows 2008 R2
-   New MIBs added: CISCO-STACK-MIB, FDDI-SMT73-MIB

# 1.1.7

-   New internal parameter: `Net.IP.NextHop`
-   Implemented IP route visualization in management console
-   New MIBs added: JUNIPER-IVE-MIB
-   New NXSL functions: GetInterfaceObject
-   Many small improvements in management console

## Fixed issues

-   NX-236 (Server crash on Solaris)
-   NX-237 (SNMP trap template for Nortel/Avaya switches)
-   NX-238 (Unable to move icon on map when grid is shown)

# 1.1.6

-   Added possibility to run different subagents under different user accounts
-   Improved work with 802.1x capable switches
-   New MIBs added: EF-6000-MIB, ES-1000-MIB, IBM-6611-APPN-MIB, IBM-MIB, IBMCPU-MIB
-   Fixed interoperability problems with IBM AS/400 SNMP agent
-   AIX support improved
-   Fixed serious memory leaks in server
-   Many small improvements in management console

# 1.1.5

-   Added "foreach" operator in NXSL
-   New NXSL functions: GetDCIValueByName, GetDCIValueByDescription
-   New attribute "comments" in NXSL classes "Node" and "NetObj"
-   Dashboard configuration in console improved
-   Database upgrade bug fixed
-   Solaris support improved
-   Many small improvements in management console

# 1.1.4

-   Implemented named parameters for events
-   Added integration script for HP EVA disk arrays
-   Added driver for Netscreen firewalls
-   Usage of DNS names instead of IP address for defining primary communication address is now supported (for better support of nodes with dynamic IPs)
-   New MIBs added: ATM-TC-MIB, CISCO-BRIDGE-EXT-MIB, CISCO-IF-EXTENSION-MIB, CISCO-L2L3-INTERFACE-CONFIG-MIB, CISCO-PRIVATE-VLAN-MIB, CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB, DVMRP-MIB, IGMP-MIB, IPV6-TC, RAPID-CITY-BAY-STACK, RC-MLT-MIB
-   Mobile client for Android introduced
-   Many small improvements in management console
-   Fixed some problems with database export/import

## Fixed issues

-   NX-328 (`File.*` should resolve environment variables)
-   NX-231 (Deadlock during template import)
-   NX-232 (Custom tooltip for alarm list with more details)

# 1.1.3

-   Added SMS driver for Portech MV-37x VoIP GSM gateways
-   Fixed serious memory leaks in server
-   Fixed compilation problems on some Linux distributions
-   Multiple fixes and minor improvements in server and management console

# 1.1.2

-   Added VLAN view in management console
-   OpenStreetMap support improved; added local cache for map images
-   Added option to use alternative tile server for geographic maps
-   Geographic maps now can be used as background for network maps
-   Implemented hierarchical maps
-   New MIBs added: POLYCOM-RMX-MIB
-   Multiple fixes and minor improvements in management console

# 1.1.1

-   Network device drivers introduced
-   Added drivers for Avaya ERS switches
-   Added driver for Cisco Catalyst 2900XL, 2950, and 3500XL series switches
-   New threshold function: SUM
-   New NXSL functions: SetCustomAttribute
-   Added support for zoning (dividing network into independent parts with possibly overlapped address ranges)
-   OpenStreetMap integration for geolocation display
-   New MIBs added: CISCO-CLUSTER-MIB, CISCO-HSRP-EXT-MIB, CISCO-HSRP-MIB, CISCO-MAC-NOTIFICATION-MIB, CISCO-STACKMAKER-MIB, CISCO-STP-EXTENSIONS-MIB, CISCO-SWITCH-CGMP-MIB, CISCO-VLAN-MEMBERSHIP-MIB, EMBEDDED-NGX-MIB
-   nxpush now supports node identification by DNS name or IP address
-   Configurable dashboards introduced

# 1.1.0

-   Server jobs introduced
-   Java API added
-   Portable (Eclipse-based) management console introduced
-   Server switched to UNICODE on Windows platform
-   Windows x64 server version added
-   MIB compiler improved
-   Dropped agent support for Novell NetWare and Windows NT 4.0, 95, 98, Me

# 1.0.10

-   Network discovery improved
-   Added VRRP support
-   Added new object tools type: server command
-   New MIBs added: VRRP-MIB

## Fixed issues

-   NX-320 (Selected object information on "IP neighborhoods" view is not changed while object is not reselected)
-   NX-321 (SMS Sending to Multiple Phone Number)
-   NX-322 (Export all to CSV - get all data before export)

# 1.0.9

-   Added LLDP support
-   MIB compiler improved
-   SNMP tools improved
-   Added automatic conversion of non-printable strings in SNMP traps
-   New MIBs added: APPLICATION-MIB, JVM-MANAGEMENT-MIB, APACHE2-MIB, SYSAPPL-MIB, RADIUS-AUTH-CLIENT-MIB, RADIUS-DYNAUTH-CLIENT-MIB, RADIUS-AUTH-SERVER-MIB, RADIUS-DYNAUTH-SERVER-MIB, RDBMS-MIB, RADIUS-ACCT-CLIENT-MIB, MSSQLSERVER-MIB, RADIUS-ACCT-SERVER-MIB, BAY-STACK-MIB, S5-AGENT-MIB
-   Fixed broken static agent build

## Fixed issues

-   NX-313 (Can't compile internal libexpat)
-   NX-318 (Windows DCI parameter "`System.Memory.Physical.Free`" reports available memory amount, not free memory amount)

# 1.0.8

-   NXSL:
    -   now possible to create scripts without explicit main()
    -   named parameters added
    -   New functions: GetNodeParents, PostEvent

## Fixed issues

-   NX-311 (Add every new discovered node to container)
-   NX-312 (nxdbmgr should check existence and permissions on idata tables)
-   NX-316 (Linux subagent should ignore rootfs record in /etc/mtab)
-   NX-317 (configure PID file custom location does not work)

# 1.0.7

-   Implemented automatic alarm termination using regular expressions
-   Added support for ODBC connection strings in ODBCQUERY subagent and ODBC database driver
-   Added server configuration parameter ProcessAffinityMask

## Fixed issues

-   NX-226 (Include nxpush into agent deb package)
-   NX-227 (Create "nxdownload" utility)

# 1.0.6

-   Implemented adding existing nodes to cluster and removing nodes from cluster
-   LogWatch subagent improved

## Fixed issues

-   NX-223 (Platform specific Object tools)
-   NX-224 (Device discovery from SNMP traps)
-   NX-225 (Quidway switches support)

# 1.0.5

-   New NXSL operators: `+=` `-=` `*=` `/=` `.=` `%=` `&=` `|=` `^=`
-   New NXSL functions: index, rindex
-   MIB compiler improved
-   New MIBs added to default distribution: ASTERISK-MIB, DIGIUM-MIB, NetWare-Server-MIB, NETWORK-APPLIANCE-MIB
-   Windows console: fixed problem with saving Object Browser and maps in desktop layout

## Fixed issues

-   NX-279 (Editors in NXMC do not support Undo)
-   NX-220 (Increase event/alarm message limit)
-   NX-221 (Add HTTPS support to portcheck subagent)
-   NX-222 (Templates with table DCIs not exported correctly)

# 1.0.4

-   Built-in syslog server improved
-   Windows console improved
-   Created separate installation package for Windows console

## Fixed issues

-   NX-282 (command line option "-D" should override "DebugLevel" from config)
-   NX-288 (Configurable ICMP ping timeout at status poll)
-   NX-217 (netxms segfault)

# 1.0.3

-   Windows console:
    -   DCI thresholds, average, and trendlines can be shown on graphs
    -   Fixed history graph performance issue
    -   Fixed GDI resource leak
-   HP-UX platform subagent improved
-   New agent parameters for Linux: `System.Memory.Physical.Available` and `System.Memory.Physical.AvailablePerc`
-   Agent parameters `Disk.*` renamed to `FileSystem.*` (old names still recognized by agent for backward compatibility)
-   Fixed various inconsistencies in parameters between different systems

## Fixed issues

-   NX-219 (Map object permanently selected when the grid is shown)
-   NX-302 (NetXMS server accepts directories as configuration files)

# 1.0.2

-   Windows console: implemented custom graphs on Performance tab in Object Browser
-   Solaris platform subagent improved

## Fixed issues

-   NX-298 (Option to show 95% line on chart)

# 1.0.1

-   Added events for DCI state change
-   New NXSL functions: log, log10, and exp
-   Windows console: added logarithmic scale option on graphs
-   MIB compiler improved

## Fixed issues

-   NX-210 (Save network map as PDF)
-   NX-215 (Topology discovery not working on some Cisco devices)
-   NX-216 (Map decorations with color based on object status)

# 1.0.0

-   System configuration (events, SNMP traps, templates, event processing rules) can be exported and imported in XML format - this solves various problems with old NXMP files
-   NXSL improvements:
    -   New functions: GetDCIObject, GetInterfaceName, FindNodeObject, trace
    -   Added built-in constants TRUE and FALSE
-   Added support for encrypted DB passwords in netxmsd.conf
-   Improved SNMPv3 support
-   Windows management console: implemented object search by comments
-   Linux: DRBD monitoring rewritten

## Fixed issues

-   NX-37 (Implement "clear data" function for DCI)
-   NX-278 (EPP Editor – replace flat list with tree or groups)
-   NX-283 (Copy chart to clipboard and/or file)
-   NX-211 (Infrastructure tree synchronization with Active Directory structure)
-   NX-213 (DCI data aggregation)

# 0.2.31

-   Added external audit logging via syslog
-   Added support for secondary RADIUS server
-   Added size and age filters to agent parameters `File.Size` and `File.Count`
-   PortCheck subagent: connection timeout made configurable
-   NXSL: added functions trim(), ltrim(), and rtrim()
-   Expat XML parser bundled with NetXMS source package

## Fixed issues

-   NX-267 (Show server hostname in window title)
-   NX-268 (Enable "Move to another group" for multiple selected items)
-   NX-269 (Data Collection configuration - add toggle switch to hide items from template)
-   NX-270 (DCIs added by instance discovery should be deleted when "root" DCI is removed)
-   NX-272 (EPP Editor suggestion: change command names)
-   NX-273 (EPP Editor "wizard" - ability to create pair of matching create alarm/terminate alarm in one action)
-   NX-274 (EPP Editor - ability to collapse alarm/terminate pairs into single record)

# 0.2.30

-   Fixed various database upgrade issues in 0.2.29

## Fixed issues

-   NX-266 (New object tool filter - custom attribute)

# 0.2.29

-   Fixed database and agent upgrade issues in 0.2.28
-   NXSL: explicit type cast improved

# 0.2.28

-   Added encryption support for SNMP version 3
-   Fixed compatibility issues with NetXMS SNMP version 3 implementation and Cisco devices
-   Automatic network discovery improved
-   LOGSCAN subagent removed (superseded by LOGWATCH subagent)

## Fixed issues

-   NX-182 (UI hangs after password change on login)
-   NX-259 (Can't list parameters from external subagent, when there are too many of them)
-   NX-201 (Portcheck: Unicode build do not recode "MAIL FROM" into multibyte)
-   NX-261 ("No storage" option for table DCIs)
-   NX-262 (GPS tracking)
-   NX-263 (Delete installer files after agent upgrade)
-   NX-264 (System allows to save multiple graphs with same name)

# 0.2.27

-   Added support for SNMP version 3 (without encryption)
-   Log monitoring improved
-   Built-in scripting language (NXSL) improved

## Fixed issues

-   NX-223 (Platform specific Object tools)
-   NX-194 (Configurable default value for data collection interval and retention time)
-   NX-195 (Incorrect selection in object tree after console start)
-   NX-197 (Nevar izveidot NODE ar to pašu IP)
-   NX-198 (Nevar nomainīt IP adresi)
-   NX-199 (Primary IP address for node incorrectly changed)
-   NX-255 (Unable to edit newly created DCI)
-   NX-200 (Agent reply with uninitialized buffer when ExetnalParameter can't start)
-   NX-258 (DCI threshold deactivation event not generated)

# 0.2.26

-   Fixed compilation problems on some UNIX platforms
-   Fixed incorrect behaviour of `Disk.Free` parameter on some Windows systems
-   Fixed broken Windows 2000 support (issue #248)

# 0.2.25

-   Implemented automatic template application based on filters
-   Implemented automatic node binding to containers based on filters
-   Implemented database export and import
-   Database checking tool (nxdbmgr) improved
-   More standard parameters inplemented in Linux, FreeBSD, and Solaris subagents
-   Removed inconsistencies in some parameters' behavior on different platforms
-   DCI transformation scripts now can be tested from console
-   Network maps improved
-   Added support for matching Windows event log records by event source, severity, and event code

## Fixed issues

-   NX-163 (Extended alarm message)
-   NX-217 (netxms segfault)
-   NX-187 (Graphs with a lot of data are not rendered (black screen))
-   NX-188 (Customize font size in graph/dashboard sessions)
-   NX-189 (Force reconnection after changing configuration parameters)
-   NX-190 (Add support for per-VLAN forwarding databases on Cisco Catalyst switches)
-   NX-191 (Alarms activity crashes in presence of long list of alarms)
-   NX-244 (Support for discovery of non-responding (firewalled) hosts)
-   NX-192 (Overview tab scrolling)

# 0.2.24

-   Critical bugfixes:
    -   Compilation errors on FreeBSD
    -   Errors in database schema if doing fresh install

# 0.2.23

-   Implemented event forwarding between NetXMS servers
-   Added new subagent LOGWATCH for log monitoring
-   Implemented syslog message monitoring on built-in syslog server
-   New agent configuration parameter: WaitForProcess
-   Number of consecutive polls can be specified for "last value" threshold
-   Implemented "Clear DCI data" function
-   Management packs improved
-   Usage of ifXTable for interface naming made configurable
-   NXSL: added new attribute "status" for node objects
-   Implemented resending of failed e-mails
-   Database checking procedure improved
-   Windows console:
    -   Added support for negative values on graphs
    -   Implemented editing of predefned graphs
    -   Implemented cut/copy/paste in event policy editor
-   Java API introduced

## Fixed issues

-   NX-31 (Object tools by template)
-   NX-49 (Add option to create interfaces for discovered nodes in "unmanaged" state)
-   NX-113 (Object tools autodetection)
-   NX-218 (NXSL functions for managing status calculation/propagation)
-   NX-228 (Ability to use DCI for node status calculation)
-   NX-183 ("Responsible Persons" for node/container)
-   NX-184 (Server complaint about too big packet when agent reply with huge list of supported DCIs)
-   NX-185 (Implement "copy to clipboard" functionality in web UI)
-   NX-186 (SNMP agent unreachable)

# 0.2.22

-   Scripts now can be used to form event's message (via %[..] macro)
-   Scripts in event processing policy now has access to node properties via $node variable and to event properties via $event variable
-   Implemented XML encoding for NXCP messages
-   Added support of custom object attributes
-   Minor map improvements

## Fixed issues

-   NX-162 (Typing OID in MIB explorer not selecting elements in MIB tree)
-   NX-167 (Multiple parameters on one chart in performance tab cannot be set in template)
-   NX-216 (Map decorations with color based on object status)
-   NX-173 (Ability to run NXSL script from console for any node object)
-   NX-221 (Add HTTPS support to portcheck subagent)
-   NX-174 (Custom Schedule not saved)
-   NX-176 (Adding image to map fails)
-   NX-177 (Export and import event processing policy)
-   NX-180 (Configure should fail if iconv is not available)
-   NX-181 (Basic device info not resent)

# 0.2.21

-   Multiple network maps implemented
-   Added parameter ListenAddress to all services (server, web server, agent)
-   New possible value for UseInterfaceAliases - concatenate name with alias
-   Added possibility to create custom message in event matching script and use it in alarms and actions
-   WMI subagent added
-   SNMP sysDescr and agent's uname now polled and displayed
-   New features in Windows console:
    -   Possibility to use non-local timezone in Windows console
    -   Default graph settings can be changed
-   AIX subagent: implemented `System.CPU.LoadAvg*` and `System.Uptime` parameters

## Fixed issues

-   NX-193 (Implement MIB selection dialog similar to legacy console)
-   NX-160 (Implement basic style in UI)
-   NX-164 (Support for SNMP tables)
-   NX-170 (Possibility to set default icon type for network map)
-   NX-209 (Situation attributes not shown in console)
-   NX-211 (Infrastructure tree synchronization with Active Directory structure)
-   NX-212 (Support for SNMP devices without standard MIBs)
-   NX-213 (DCI data aggregation)
-   NX-214 (UI option to configure interface "exclude from topology" flag)
-   NX-215 (Topology discovery not working on some Cisco devices)

# 0.2.20

-   Implemented advanced event processing using situations
-   Added checking of NetXMS server own network connectivity via beacon hosts
-   Implemented "proxy node" functionality for DCIs
-   Added possibility to use values of other DCIs in transformation scripts
-   Added possibility to specify multiple recipients in e-mail or SMS action
-   Implemented `System.CPU.Usage` for individual processors on Linux
-   PING subagent: added parameter `ICMP.PacketLoss(*)`
-   Command line options for the server changed to use common style
-   Added UNICODE support in client part on Linux/UNIX
-   Implemented macros in template DCIs (expanded when template applies to node)
-   Added event storm detection
-   Added possibility to specify multiple SNMP community strings for discovery and configuration polls
-   NetXMS server now can understand interface aliases (description in Cisco terms)
-   Added optional synchronization of node names with DNS
-   New command line tool for managing alarms - nxalarm
-   Implemented "stop processing" option for event processing policy rule
-   Implemented "move" operation for templates (move between template groups)
-   New internal parameter: `ConditionStatus(*)`
-   NXSL:
    -   Implemented ternary operator (?:)
    -   New built-in functions: gmtime(), localtime(), left(), right()

## Fixed issues

-   NX-155 (Accept traps from agents in different zones)
-   NX-156 (Bug in auto connection on connectivity change with scheduler disabled)
-   NX-157 (Autoscale values in "last values" tab)
-   NX-158 (Add "Connectivity" tab to object details view)
-   NX-161 (Cluster DCIs in dashboards)
-   NX-164 (Support for SNMP tables)
-   NX-165 (Unable to unselect group box)
-   NX-169 (Use layer 2 topology information for event correlation)

# 0.2.19

-   Added SMS driver and subagent to send SMS via remote NetXMS agent
-   Added parameters `Net.RemoteShareStatus` and `Net.RemoteShareStatusText` to WINNT subagent
-   Added possibility to disable status, configuration, or routing table polls for specific host
-   Added possibility to define number of consecutive status polls with same result needed to change status of interface or network service object

## Fixed issues

-   NX-77 (Average DCI queue time is high after adding table DCI)
-   NX-134 (Test config and rollback to previous version is agent can't start)
-   NX-118 (FreeBSD agent crash on `Net.Interface.BytesIn`(1))
-   NX-146 (Find node by IP address)
-   NX-149 (Interfaces tab for subnets)
-   NX-150 (Setup first interface name and mac on node creation)
-   NX-151 (Action groups)
-   NX-152 (Automatic database unlock in clustered environment)
-   NX-153 (Map background set to geo map causes NPE in web UI)

# 0.2.18

-   Windows console: added "subordinates" view in object browser
-   WinPerf subagent:
    -   Improved non-English Windows support
    -   Added new parameter: `System.IO.DiskTime`
-   New MIB added: FIBRE-CHANNEL-FE-MIB

## Fixed issues

-   NX-5 (MS SQL DB driver should find available native client)
-   NX-129 (AIX: Unable to retrieve interface status via agent)
-   NX-130 (AIX agent does not return all IP addresses configured on interface)
-   NX-131 (Add DB optimization option to nxdbmgr)
-   NX-132 (not able to store history in version 1.2.2)
-   NX-134 (Test config and rollback to previous version is agent can't start)
-   NX-135 (Open node by name in Alarm Browser)
-   NX-137 (Агент перестал собирать ExternalParameter)
-   NX-139 ("Snap to grid" feature for network maps)
-   NX-140 (UDP ping)
-   NX-141 (Implement support for UNICODE logs in log monitoring subagent)
-   NX-142 (Poll count for status change for network service objects)
-   NX-143 (Large numbers shown on charts as -1)
-   NX-144 (Compilation warnings on Solaris 10)
-   NX-145 (Do not collect unnecessary information from nodes during network discovery)

# 0.2.17

-   Implemented alarm timeouts
-   ODBCQUERY subagent improved
-   Web interface improved
-   Object browser in Windows console improved

## Fixed issues

-   NX-95 (Templates for node attributes)
-   NX-101 (Add support for Cisco Catalyst 3550)
-   NX-102 (Alarm categories)
-   NX-105 (\ in file name processed as formatting character by logger)
-   NX-138 (netxmsd crash in script processing)
-   NX-108 (Support WinPerf on non-English Windows)
-   NX-123 (Implement "alarm tools" similar to object tools)
-   NX-124 (after Windows Firewall activated without exceptions NetXMS server crashes)
-   NX-125 (Cannot use SNMP OIDs longer then 255 characters)
-   NX-126 (Fails to retrieve interface list from node)
-   NX-128 (USB UPS monitoring support under Linux)
-   NX-129 (AIX: Unable to retrieve interface status via agent)

# 0.2.16

-   Implemented user authentification by certificates
-   Management packs fully functional - templates, events, and SNMP traps can be exported and imported
-   Cluster monitoring improved
-   Node names resolution working
-   Implemented OCI based driver for Oracle database
-   UPS subagent: added support for Microdowell devices
-   Windows console:
    -   Added layer 2 topology view for compatible switches
    -   Object search improved
    -   Graphs improved:
        -   Area graphs
        -   Predefined graphs
        -   Minor UI improvements
    -   Added possibility to manage/unmanage set of child objects
    -   Added possibility to hide unmanaged leaf objects
    -   Container objects can be placed above all others
    -   Other small UI improvements

## Fixed issues

-   NX-63 (Context menu in EPP editor shown only when clicking on rule number, not on the rule itself)
-   NX-79 (Command line tools should return proper error code)
-   NX-93 (Truncated object tooltip texts in network maps)
-   NX-110 (Disable account problems)
-   NX-114 (Custom Overview page)
-   NX-115 (Ability to change date formatting)
-   NX-116 (Sort network interfaces by number instead of name)
-   NX-117 (SNMP Trap Monitor broken)
-   NX-119 (Add support for number of drops on interface counters)
-   NX-120 (Tables support in NXSL)
-   NX-122 (Hub with over 150 interfaces)

# 0.2.15

-   Added initial support for cluster monitoring
-   Added preliminary support for management packs
-   Added SNMP proxy functionality to agent
-   IPSO agent improved
-   Added Extended Checksum subagent
-   Added ODBC Query subagent
-   New agent parameters: `Process.CountEx`(), `File.Time.Access`(), `File.Time.Change`(), and `File.Time.Modify`()
-   Parameters `File.Size`() and `File.Count`() improved
-   Parameters `Process.XXX` improved
-   NXSL improved: implemented switch ... case statement and break statement
-   Windows console:
    -   Now able to download and install update from web server pointed by NetXMS management server
    -   Object browser improved
    -   Graphs improved: implemented printing and "copy to clipboard" function
    -   Added server history in login dialog
    -   Added option "hide empty values" in last DCI values view

## Fixed issues

-   NX-78 (Cannot build static agent)
-   NX-96 ("Execute Script" option in popup-menu for node/container)
-   NX-103 (Alarm details view)
-   NX-104 (Object Tools URL Caption)
-   NX-107 (SMTP authentication support (for notifications))
-   NX-109 (LogWatch: ability to pass event source, facility, etc. with generated message)
-   NX-112 (Show thresholds on graph is broken)

# 0.2.14

-   Alarm system improved (three state alarms, helpdesk status, etc.)
-   Added new DCI data source: push agents
-   Threshold state now saved across NetXMS server restarts
-   Added possibility to specify custom threshold rearm event instead of `SYS_THRESHOLD_REARMED`
-   Added threshold processing option "Always process all thresholds"
-   Implemented "data collection error" threshold checking function
-   Implemented "mean absolute deviation" threshold checking function
-   Added possibility to set confirmation messages for object tools
-   Object tools "Shutdown system", "Restart system", "Restart agent" asks confirmation by default
-   Implemented agent traps and added trap sending API for subagents
-   Object comments added
-   Network discovery configuration simplified
-   Active network discovery implemented
-   Windows console:
    -   Console changed to use UNICODE internally
    -   Event processing policy editor improved
    -   Added confirmation for object deletion
    -   Implemented sorting in object tools tables
-   Server ported to AIX and HP-UX
-   Agent ported to HP-UX
-   Agent for AIX improved

## Fixed issues

-   NX-77 (Average DCI queue time is high after adding table DCI)
-   NX-82 (Sound notifications for alarms (as in Legacy Console))
-   NX-83 (NetXMS daemons not added to autostart after installation from deb package)
-   NX-84 (Use ifXTable when creating interface DCIs when possible)
-   NX-85 (Autostart demons NetXMS)
-   NX-86 (Implement custom time intervals for line charts)
-   NX-88 (Support for swipe in node info tabs)
-   NX-89 (Scheduler for passive mode)
-   NX-90 (Reorganize settings activity)
-   NX-92 (DCI value in last values tab not properly rendered with long description)
-   NX-94 (Request poll count for node before status change)
-   NX-97 (Instance name with number in the end processed incorrectly)
-   NX-98 (autoconf 2.69 complains abouti "INCLUDES")
-   NX-99 (Macros in file names in `File.xxx` parameters)
-   NX-100 (Define multiple files in log parser)
-   NX-133 (DCI not Polling Values for `System.CPU.Usage5`)
-   NX-106 (Status indicator in dashboard causes web console to crash)

# 0.2.13

-   Implemented central (stored on server) agent configs
-   Agent ported to IPSO
-   Added installer command line options for unattended installation of Windows agent
-   New MIBs added: S5-ETH-MULTISEG-TOPOLOGY-MIB, BN-IF-EXTENSIONS-MIB
-   Server startup and shutdown procedures improved
-   Added detection of lost database connections and automatic reconnect
-   Native operating system read/write locks used whenever possible
-   Added possibility to use alarm message text in actions (if action executed by the same event processing rule as alarm)
-   Better handling of interface names of Nortel ethernet switches
-   SNMP trap varbinds now can be mapped to event parameters not only by OID, but also by position in trap PDU
-   Windows binaries built against OpenSSL 0.9.8b
-   Windows console:
    -   DCI history data viewer improved
    -   Graphs improved
-   nxsnmpset utility improved
-   nxevent: added -e command line option to turn on session encryption
-   Implemented parameter `UPS.Load` for BCM/XCP compatible devices

## Fixed issues

-   NX-4 (Object deletion may not be immediately reflected in console)
-   NX-20 (nxdbmgr option for changing/resetting server configuration variables)
-   NX-23 (Option to create DCI directly from MIB browser)
-   NX-42 (Bulk change of flags for nodes (e.g. disable SNMP))
-   NX-52 (Timed alarm acknowledgement)
-   NX-53 (Monitors (event log, syslog, etc.) as dashboard elements)
-   NX-64 (Potential crash on business service deletion)
-   NX-65 (Internal optimization for object references)
-   NX-66 (Improve line charts in web UI)
-   NX-67 (Configurable management server address in nxmc servlet)
-   NX-68 (Add support for DB/2 as backend database)
-   NX-69 (Driver for Cisco Nexus)
-   NX-70 (Add ability to see current state of network discovery in console)
-   NX-71 (Show data source data in dashboard editor)
-   NX-72 (Debian package netxms-agent require librealine but do not list it as required package)
-   NX-73 (Node name in Object Browser shortened for no reason)
-   NX-74 (New node options - "expected capabilities")
-   NX-75 (Generate user manual PDF from Wiki)
-   NX-76 (MIB explorer - double click in walk results)

# 0.2.12

-   Added possibility to define complicated conditions using "condition" objects
-   Implemented RADIUS authentication for NetXMS users
-   Added support for compressed MIB files
-   New MIBs added: ENTITY-MIB
-   Added support for DRBD device monitoring
-   Windows console: Event editor improved
-   UPS subagent:
    -   Redesigned to improve stability and performance
    -   Added parameter `UPS.OnlineStatus`
    -   Fixed problem with occasional APC UPS disconnections

## Fixed issues

-   NX-62 (Errors when changing node's IP address)

# 0.2.11

-   Basic network maps implemented
-   Non-standart (other than 4701) ports now can be used for client-server communications
-   Copy/move/delete of saved desktop configurations implemented
-   SNMP walk function improved
-   Implemented "User must change password on next logon" function
-   UPS subagent: added support for BSMXCP protocol (used by Powerware, HP and Compaq UPSes)
-   Fixed Alarm Viewer crash

## Fixed issues

-   NX-28 (Disable account problems)
-   NX-11 (Scripts for automatic object icon selection)
-   NX-28 (Disable account problems)
-   NX-55 (Button "Test" is not working on DCI transformation property page)
-   NX-56 (Groups in event editor)
-   NX-57 (Proxy agent support in command line SNMP tools)
-   NX-58 (Refactor Image Library)
-   NX-59 (Implement data export from log viewer)
-   NX-60 (Implement object search by ID, IP address, primary host name)
-   NX-61 (Add "disable" option to object tools)

# 0.2.10

-   Web interface redesigned
-   Added OpenBSD platform subagent
-   Added UPS monitoring subagent
-   Netscreen (now Juniper) MIBs added
-   Windows console: graphs improved
-   Added possibility to log all incoming SNMP traps
-   Fixed problems with very long opening time of event log

## Fixed issues

-   NX-34 ("Test" button on DCI transformation property page is not working)
-   NX-47 (Check and update section 10.7 (agent parameters) in user manual)
-   NX-48 (Add second resolution to custom poll schedule)
-   NX-51 (Add certificate authentication to Java console)
-   NX-54 (Add new policy type for distributing log parsers)
-   NX-78 (Cannot build static agent)

# 0.2.9

-   Added built-in scripting language (NXSL - NetXMS Scripting Language)
-   Implemented DCI transformations (using NXSL)
-   Implemeted auto discovery filters (using NXSL)
-   Added startup scripts for Gentoo Linux
-   Windows console: agent configuration editor improved
-   Alarm Viewer: repeated alarm sounds added

## Fixed issues

-   NX-39 (NXSL script started from debug console via exec must redirect print output to console)
-   NX-43 (Autodiscovery: enable user to set default settings for discovered nodes)
-   NX-44 (Apply policy to node by clicking on node and selecting policies from list)
-   NX-45 (Policy templates for applying policy groups)
-   NX-46 (Use Spanning Tree data for network discovery)
-   NX-50 (Allow per-DCI SNMP version settings)

# 0.2.8

-   Implemented agent proxy
-   Object tools fully implemented (including configuration)
-   Added web session manager and very basic web interface
-   Added "node capability expiration" feature
-   Windows console:
    -   Fixed inconsistencies in object access control configuration
    -   Now can play sounds when new alarm arrives
    -   Added voice notifications for alarms (using SAPI)
-   Alarm viewer:
    -   The same audio notification options added
    -   Current time display added
-   Added support for Windows authentication in Microsoft SQL driver
-   Server configuration wizard: added possibility to configure service account
-   Added support for transactions in database manager
-   Fixed bugs in server's SMTP sender
-   Fixed bug in SMS driver

## Fixed issues

-   NX-33 (Tables support in NXSL)
-   NX-36 (SNMP trap forwarding by agent in SNMP proxy mode)
-   NX-38 (Predefined graphs cannot be deleted)
-   NX-40 (Add NXSL function RenameObject)
-   NX-41 (Tool execution on container or group of nodes)

# 0.2.7

-   Advanced status calculation mechanism implemented
-   Added support for SQLite embedded database engine
-   New MIBs added: IEEE 802.11
-   PING subagent: added "PacketRate" configuration parameter
-   Fixed some portability issues for 64bit platforms
-   Fixed build problems with version 0.2.6

## Fixed issues

-   NX-29 (Local commands with arguments works only with "Command generates output" option)
-   NX-31 (Object tools by template)
-   NX-35 (Intermittent SQL failures on SQLite)
-   NX-59 (Implement data export from log viewer)

# 0.2.6

-   Added possibility to change size of ICMP echo request packets sent by server
-   Added built-in syslog server
-   Implemented retrieving of only last N records from event log
-   Implemented "Select DCI" function for templates
-   Implemented own MIB compiler, removing last dependency from Net-SNMP library
-   MIBs now transferred to client in compiled form, reducing network traffic and making console startup faster
-   Implemented correct translation of SNMPv1 trap id to SNMPv2 trap id
-   Added advanced DCI collection scheduling
-   Core agent:
    -   Ported to AIX
    -   Fixed bug in signal handling causing agent to crash on shutdown
    -   Implemented autoloading of platform subagent on UNIX and NetWare
    -   Fixed broken under NT4 `Net.InterfaceList` enum
-   PING subagent:
    -   Ported to NetWare and AIX
    -   Added "packet size" argument to `Icmp.Ping(*)` parameter
    -   Added "packet size" option to target configuration
    -   Added DefaultPacketSize configuration parameter
-   Port checker subagent ported to AIX
-   Added possibility to build statically linked agents
-   Event configuration improved
-   New MIBs added: BGP4, PowerNet (APC), PRINTER, Synoptics (now part of Nortel Networks), UPS
-   Windows console:
    -   Improved handling of large number of objects
    -   Status and configuration poll windows improved
-   Database checker improved

## Fixed issues

-   NX-12 (Use dot1qTpFdbTable instead of dot1dTpFdbTable for FDB retrieval when possible)
-   NX-22 (Configurable date/time format in console)
-   NX-24 (Copy OID name to clipboard from MIB browser)
-   NX-25 (Show OID textual convention in MIB browser)
-   NX-26 (Show some last values in overview page)
-   NX-27 (Object Tools URL Caption)
-   NX-30 (Show thresholds on graph is broken)

# 0.2.5

-   Added support for CheckPoint SNMP agent running on port 260
-   Added SNMP MIBs for Nokia IPSO
-   Added new parameter `Agent.ActiveConnections` to core agent
-   Implemented object tools of type "Agent Table" and "SNMP Table"
-   Windows console:
    -   Sorting implemented in "Last DCI Values" view
    -   Added node tree in alarm browser
    -   Added possibility to copy DCIs to template
-   Fixed bug in core agent causing incorrect update of configuration file
-   Fixed incorrect interface aliases detection in Linux subagent

## Fixed issues

-   NX-15 (Peer information not cleared from interface)
-   NX-18 (Different layouts in port view based on driver information)
-   NX-21 (Nodes without IP address on interface added to the tree root)
-   NX-36 (SNMP trap forwarding by agent in SNMP proxy mode)

# 0.2.4

-   Implemented agent's configuration file editing from console
-   Implemented actions provided by subagents
-   Built-in action `Agent.Restart` added to core agent
-   Configurable object tools introduced (not fully implemented yet)
-   Fixed bug causing occasional server crash

## Fixed issues

-   NX-5 (MS SQL DB driver should find available native client)
-   NX-13 (Agentless WMI access)
-   NX-14 (Script validation before save in script editor)
-   NX-16 (Do not activate disabled DCIs after template change)
-   NX-17 (Web interface crashes in IE9)

# 0.2.3

-   Implemented basic event correlation
-   Added new object class: VPN connector
-   Active alarms now used in status calculation
-   Windows agent: implemented enum `Net.IP.RoutingTable`
-   Database Manager: implemented forced check/unlock flag
-   Maximum number of sessions in agent made configurable
-   Agent ported to Windows 95/98/Me
-   Windows console: added possibility to specify loopback address (127.0.0.1) as bind address for network service
-   Fixed bug causing random fails of connections from server to agent and from console to server

## Fixed issues

-   NX-9 (Unable to bind object in WebUI)
-   NX-10 (Implement copy to clipboard in all log viewers/monitors)
-   NX-29 (Local commands with arguments works only with "Command generates output" option)

# 0.2.2

-   Implemented communication session encryption
-   Added support for multiple database connections for better performance
-   Added generation of `SYS_NODE_DOWN` and `SYS_NODE_UP` events
-   Added possibility to edit server's configuration parameters from administrator's console
-   Object status calculation algorithm changed
-   Fixed incorrect 32 bit integer varbinds parsing in libnxsnmp
-   Fixed bug with new interface detection
-   Windows console: added simple export of collected DCI data
-   Core agent: added configuration option SessionIdleTimeout for automatic disconnect of idle or broken sessions

## Fixed issues

-   NX-8 (Config file with CRLF loaded incorrectly on UNIX (OS X only?))
-   NX-30 (Show thresholds on graph is broken)

# 0.2.1

-   Server startup procedure improved
-   Fixed bug in Windows service shutdown code
-   Added ICMP ping subagent
-   Server will not collect data from unmanaged nodes
-   Added PostgreSQL support under Windows
-   NetWare platform subagent improved
-   Linux subagent: Implemented all `Net.Interface.*` parameters except `Net.Interface.Speed`
-   Fixed crash in Microsoft SQL driver caused by unsuccessful connection
-   More SNMP MIBs added
-   Fixed issue #27 (poller threads deadlock)
-   Server's internal synchronization mechanisms improved
-   Added driver for generic GSM modems
-   SMS driver can be configured from server configuration wizard
-   Windows console:
    -   Action properties dialog improved
    -   Sorting implemented in data collection editor
    -   Object browser window can be saved in desktop configuration
-   Windows alarm viewer:
    -   Added autologin feature
    -   UI appearance improved

# 0.2.0

-   Windows installer improved
-   Fixed build issues on various platforms
-   Windows console:
    -   Items in Control Panel now sorted alphabetically
    -   Data collection editor now shows associated template for DCI
    -   Added automatic refresh to last values view
    -   Rule in policy editor can be enabled/disabled by double click
        on leftmost column (rule number)
-   Fixed incorrect interface detection on FreeBSD

# 0.1.20

-   Implemented object unbinding from administrator console
-   Implemented template removing
-   Added "Change IP address" function for node objects
-   Added Oracle support (via ODBC driver)
-   Added server installation program (Windows only)
-   Added server configuration wizard (Windows only)
-   SNMP agent connectivity check improved
-   Added special handling for CheckPoint SNMP agent
-   Added "Don't cache this session" option to Windows console login dialog
-   Added new console command "show stats"
-   Windows CE Console improved:
    -   Added "Last DCI Values" view
    -   Added graph view
    -   Added collected DCI data view
    -   Added full screen mode support
    -   Implemented sorting in alarm browser
    -   Implemented alarm browser autoupdate
    -   Implemented object managed/unmanaged state switching
    -   Implementen node wakeup
-   Network discovery polling mechanism redesigned
-   Fixed bug in "show pollers" console command handler
-   Fixed occasional appearance of invalid objects at the root of object tree

## Fixed issues

-   NX-14 (Error handling multiline SMTP responces)

# 0.1.19

-   Data collection templates fully functional
-   Added possibility to use server name instead of IP address in agent configuration
-   Added diff() method for DCI thresholds
-   Added possibility to set server config file via:
    -   environment variable `NETXMSD_CONFIG` on UNIX
    -   registry key `HKLM\Software\NetXMS\Server\ConfigFile` on Windows
-   Fixed deadlock in status poller
-   Fixed incorrect socket handling in AgentConnection class
-   Fixed sorting bug in Windows console alarm browser
-   Fixed GUI unresponsiveness when acknowledging large number of alarms

# 0.1.18

-   Added support for object database caching on client side
-   Polling performance increased
-   Fix: `SYS_SERVICE_DOWN` event was generated in place of `SYS_SERVICE_UNKNOWN`
-   nxadm completely rewritten, and now allows to execute any command available on server console in standalone mode
-   Windows console:
    -   Implemented desktop configuration save and restore
    -   Added possibility to change graph's time frame
    -   Added support for multiple DCIs on one graph
    -   Added graph presets
    -   Many small UI improvements

# 0.1.17

-   Templates can be manually applied
-   Fixed bug in filling DCI cache with values from database
-   Server now can save and restore last DCI poll time and raw value across restarts

## Fixed issues

-   NX-21 (agent crash on multiprocessor Solaris systems)
-   NX-22 (server can crash after unsuccessfull interface configuration poll)

# 0.1.16

-   Added `System.CPU.Usage(*)`, `System.CPU.Usage5(*)` and `System.CPU.Usage15(*)` parameters to WinPerf subagent
-   Fixed server crash sometimes caused by DCI deletion
-   Fixed memory leaks in DCI cache management
-   Added interface for processing SNMP traps by server modules
-   Added internal parameters AgentStatus and `ChildStatus(*)`
-   Some GUI improvements
-   Parameters `Net.Interface.AdminStatus(*)` and `Net.Interface.Link(*)` added to FreeBSD subagent

## Fixed issues

-   NX-1 (unable to modify network service port number)
-   NX-3 (server crash after DCI copy)
-   NX-4 (incorrect aliases handling by FreeBSD subagent)

# 0.1.15

-   DCI housekeeping implemented
-   Fixed server crash at forced poll time
-   Fixed critical bug in upgrade script starter under UNIX
-   Added support of HDD temperature monitoring under Windows and Linux
-   Added `PhysicalDisk.Model`, `PhysicalDisk.SerialNumber` and `PhysicalDisk.Firmware` parameters under Windows
-   Added parameters `System.CPU.Count`, `System.CPU.Usage`, `System.KStat(*)` and `System.Memory.Physical.*` to Solaris subagent
-   Parameters `System.Memory.Swap.*` removed from Windows agent because they are meaningless under Windows
-   Added parameter `Disk.Used(*)` to NetWare subagent

# 0.1.14

-   Parameters `System.Memory.*` behaves correctly under Windows
-   Fixed bug in loading of NetworkService objects from database
-   Fixed bug in interface status detection via NetXMS agent
-   Added support for NAT'ed nodes (correct interface polling, etc.)
-   Backslash (\) character is no longer works as escape character inside parameter arguments enclosed in quotes
-   Windows console: object tree works correctly for users without rights on root objects
-   Windows console: implemented user deletion from access lists
-   Implemented action delete
-   Windows agent deployment packages now built with InnoSetup
-   "Last Values" view added to Windows console
-   Added interface for SMS drivers
-   Optimized access to collected DCI data in database
-   Added support for `System.CPU.LoadAvg` to Solaris subagent
-   Added support for all `Net.Interface.*` parameters to Solaris subagent

## Fixed issues

-   NX-8 (Config file with CRLF loaded incorrectly on UNIX (OS X only?))

# 0.1.13

-   Fixed bug which cause server to hang when deleting unreacheable node
-   Added basic checking of node and interface objects to nxdbmgr

# 0.1.12

-   Added new object class - NetworkService, for simplified network service health checking
-   Server internal synchronization mechanisms improved to increase stability and performance
-   Fixed deadlock sometimes caused by retrieving DCI collected data
-   Added parameters `System.Hostname`, `System.Uname` and `System.Uptime` to Solaris subagent
-   Object status now recalculated after binding change
-   Implemented primary IP address selection for nodes
-   Added OSPF support detection
-   Fixed bug with StartupDelay parameter handling in core agent
-   Fixed communication problems on FreeBSD
-   Bug fixed: objects was not marked as modified when platform name or agent version changes
-   Windows console: implemented cell edit by double click in policy editor
-   Implemented external command execution under UNIX

## Fixed issues

-   NX-3 (Object status indicator in console not always updated correctly)

# 0.1.11

-   Fixed incorrect behavior of `Process.Count`() parameter under Linux and FreeBSD

# 0.1.10

-   Support for centralized upgrade added to agents
-   Implemented agent packages upload to server from console
-   New parameters added to Solaris subagent
-   Alarm deletion implemented
-   Implemented all delta calculation methods for DCI
-   Implemented thresholds for average values
-   Fixed bug with policy editor header drawing

# 0.1.9

-   Added support for server modules
-   Initial version of web interface created (for Microsoft IIS)
-   Microsoft SQL driver improved
-   Added file upload to agents (as preparation for centralized agent update)
-   Client library redesigned to support multiple connections within one process
-   Windows console: added automatic refresh in graphs
-   Very basic Solaris subagent added

# 0.1.8

-   Added support for `System.CPU.Count` and `System.ProcessList` parameters under Windows
-   Created our own SNMP library (currently SNMP versions 1 and 2c are supported). Server is no longer needs net-snmp library.
-   Component locks moved to RAM from SQL database
-   Added support for SNMP traps
-   Removed access right "View server configuration" as unneeded
-   Windows console: Added sorting to event selection dialog
-   Windows console: Objects in object browser are now sorted with respect to IP addresses when object name is an IP address
-   Windows console: Fixed bug with MDI window position restoration when window is maximized
-   Windows console: Fixed bug with duplication of child window title in parent's title when child is maximized
-   Windows console: Status icons now placed over object icons in object browser
-   Windows console: Policy editor drawing code improved
-   Added StartupDelay parameter to agent's configuration file
-   Windows console: Added "Save policy" function to policy editor
-   Fixed deadlock in Queue::GetOrBlock() which sometimes cause communication failures between client and server
-   Server now can detect that SNMP variable is not supported by agent and change DCI status to "Not supported" accordingly
-   Added interface status polling via SNMP
-   Agent: Fixed bug in interface operational status detection under Windows
-   Added server version checking in client connection procedure. If versions mismatch, client will not connect to server.
-   Windows console: when searching object in object browser, `*` characters assumed at the beginning and the end of search string
-   Added parameter `File.Count(*)` to core agent
-   Added possibility to change status of many DCIs status at once

# 0.1.7

-   Added more customized events for threshold violation
-   Added ability to send Wake-On-LAN packets to managed nodes
-   Fixed serious bug in DCI copy

# 0.1.6

-   Added parameter `System.ServiceState(*)` to core agent (Windows only)
-   Implemented user-defined counters in WinPerf subagent
-   Added support for macros in e-mail subject
-   Added support for data collection item duplication within same node
-   Now possible to copy DCIs to many nodes at once
-   Fixed memory management bugs in Windows console DCI editor
-   Added "instance" field to DCI which can be used as information text in user-defined data collection events and alarms
-   Client library do cleanup after NXCDisconnect()
-   User system rights now ORed with its group(s) system rights
-   Added database checking/upgrade utility (nxdbmgr)

# 0.1.5

-   Object access mutexes changed to read/write locks in server to improve performance
-   Algorithm of placing nodes into subnets improved
-   System no longer needs network mask when creating new node manually
-   Detection of incorrect network masks on interfaces added
-   Windows console: fixed bug in object browser which cause console to crash
-   Added internal statistics collection for average data collector queue length and average database writer queue length
-   All IP addresses now stored in database as text
-   Added external event sender (nxevent)
-   Fixed bug with user password change (new password was not saved to database)
-   Configuration script ("configure") improved

# 0.1.4

-   Created performance subagent for Windows (winperf.nsm)
-   Added SNMP OID to node type translation
-   Added support for Nortel Networks Passport routing switches
-   "configure" script improved

# 0.1.3

-   Added 64-bit string-to-binary conversion
-   Added MAC address property to interface objects
-   Added Template and TemplateGroup object classes
-   It's now possible to configure data collection items for templates

# 0.1.2

-   Added possibility for copying DCIs from one node to other(s)
-   Added server's startup script for RedHat Linux
-   Numerous bug fixes

# 0.1.1

-   First version number given to system: a lot of things works, and lot of things have to be done.
