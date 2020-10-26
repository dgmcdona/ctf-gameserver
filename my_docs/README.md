# Documentation for UNO CSCI Setup

## Platform
This fork will be documented for setup on the UNO computer science department's XCP-ng Cyber Range server pool, managed by Xen Orchestra. This will allow us to configure a private network on which the vulnboxes and gameserver will run.

## Base Debian 10 VM Configuration
The authors of FaustCTF designed this gameserver to run on a Debian 10 Buster operating system. Although the original repository lacks documentation, I believe that the `debian/install` file contains instructions for where to relocate certain files in this repository in order to properly configure nginx, django, etc. Best practice is to create a cloud-config file on the cyber range which will automate dependency installation AND to create a VM template that can simply be cloned and used right out of the box. The cloud-config should serve as redundancy in case something catastrophic happens to the template, or there are significant changes to the framework that necessitate starting from scratch.

### `apt` package dependencies
- git
- unzip
- python3
- make
- python3-pip
- postgresql
- postgresql-server-dev-all

See the included cloud-config for other apt packages that were installed by default on VM clone.
- TODO: create cloud-config for ctf-gameserver on cyber-range
### Python3 dependencies
- django
- Pillow
- markdown
- --upgrade setuptools
- psycopg2
- configargparse
- prometheus-client
## TODO's
- Consider setting up a pfsense router so that vulnboxes will have internet access for students to install tools. This is not strictly necessary, but is something that we have done in past CTF Attack-Defense competitions. I can't remember the details at the moment, but I think I remember iCTF using a NAT router to prevent players from distinguishing checker traffic from the traffic of their opponents.
- Configure a CTF Gameserver VM template, so that many of the steps documented here do not need to be repeated in future deployments.
- Vulnbox setup:
	- CHALLENGES!! Create services that run on the vulnboxes. These services must follow the rules for the 'checker', meaning that there must be a default way in which the checker can store and retrieve flags in order to score Service Level Agreement (SLA) points.
		- Consider dockerizing these services for easy restart in the event that a team's service becomes compromized by an opponent or the team itself. This follows the paradigm seen in prior attack-defense competitions, such as UCSB iCTF and FaustCTF.
	- Configure docker containers to start automatically upon boot. Players' vulnboxes should be delivered to them in a running state.
