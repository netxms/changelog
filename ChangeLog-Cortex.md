*
* 4.1
*

- Added DB driver options in subagent


*
* 4.0
*

- Max BIN length extended to 11 digits


*
* 3.9
*

- Check that term* table exist before reading from it


*
* 3.8
*

- Updated txnsend tool
- Added subagent configuration parameter TransactionGroupsAlwaysExist (when on unknown subagent will return value 0 for unknown BINs, terminals, and card acceptors)


*
* 3.4
*

- Cortex subagent performance optimization
- Removed unusable parameter Cortex.Version


*
* 3.0
*

- Cortex subagent can calculate statistic by card acceptor


*
* 2.2
*

- Implemented per acquirer/issuer pair transaction statistic
- Added handling of transactions with missing TLOGID
- Fixed memory leak in Cortex sub-agent


*
* 2.1.1-86
*

- Fixed performance issues on high load systems
- Added configuration option for interval between tunnel keepalive packets
- Fully qualified domain name sent as part of agent information during tunnel setup


*
* 2.1.1-5
*

- Additional debug information logged


*
* 2.1-89
*

- Transaction fields I_RSPSRC and I_CRDACPTID added to transaction serialization
- Transaction statistics collection by terminal and BIN can be switched off


*
* 2.1-RC1-103
*

- Fixed agent crash on startup


*
* 2.1-RC1-53
*

- Default session idle timeout increased to avoid issues with file tracking


*
* 2.1-RC1-47
*

- Fixed memory leak on AIX


*
* 2.1-RC1-39
*

- Terminal ID field extracted from transaction
- Transaction statistics per terminal
- Improved agent tunnel support
- Fixed log monitoring subagent crash
- Implemented external tables in agent
- Improved channel closure detection in agent tunnels
- Fixed agent restart issue
- Fixed agent crash after tunnel disconnect
- Fixed potential race condition during agent tunnel closure

