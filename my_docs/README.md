# Documentation for UNO CSCI Setup

## Platform
This fork will be documented for setup on the UNO computer science department's XCP-ng Cyber Range server pool, managed by Xen Orchestra. This will allow us to configure a private network on which the vulnboxes and gameserver will run.

## TODO's
- Consider setting up a pfsense router so that vulnboxes will have internet access for students to install tools. This is not strictly necessary, but is something that we have done in past CTF Attack-Defense competitions. I can't remember the details at the moment, but I think I remember iCTF using a NAT router to prevent players from distinguishing checker traffic from the traffic of their opponents.
- Configure a CTF Gameserver VM template, so that many of the steps documented here do not need to be repeated in future deployments.
- Vulnbox setup:
	- CHALLENGES!! Create services that run on the vulnboxes. These services must follow the rules for the 'checker', meaning that there must be a default way in which the checker can store and retrieve flags in order to score Service Level Agreement (SLA) points.
		- Consider dockerizing these services for easy restart in the event that a team's service becomes compromized by an opponent or the team itself. This follows the paradigm seen in prior attack-defense competitions, such as UCSB iCTF and FaustCTF.
	- Configure docker containers to start automatically upon boot. Players' vulnboxes should be delivered to them in a running state.
