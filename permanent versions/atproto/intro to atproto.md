# Introduction to ATProto

**Interested in understanding how Bluesky and the ATProtocol works? This explainer starts with a very simple diagram, and then progressively adds detail.**

*(Sidenote Intro: This page explores an idea I had on how to explain Bluesky and ATProtocol to non-specialists. If this idea works, it will be republished and further developed into one of the [Explainers on the ATProtocol community wiki](https://atproto.wiki/en/wiki/explainers).* 

*Sidenotes like this will not appear, obviously.* 

*Unfortunately I am one of those non-specialists, so - as explained in [the #wiki-discussion on Discord](https://discord.gg/UF7AhwKR)  -  I will need help, and am sharing this proof-of-concept version here on my experimental wiki to see:*

* *if it will work*
* *and if anyone else would like to help me develop it further.* 

*This is version 2 (more version control info in the footer).* 

*If people think it has potential and want to help me get it right, I'll move it to the wiki for further development by a larger community. If you'd like to help me **before** then, ping me on Discord and I'll give you access via github to this file and [[atproto1.drawio]], from which all .pngs are currently derived (I'm currently exploring [tldraw](https://www.tldraw.com/)).*

*Final note: the final version will need a more attractive graphic, obviously. But let's get the content right first).*

---
## Geostationary Orbit view

**Looking at Bluesky from orbit, you can only distinguish three elements:**

![[atproto1.orbital-1.png]]

They are:

* **PDS**: Personal Data Servers - this is where your content lives. When you write something on Bluesky, or even Like someone else's post, that content goes on your PDS.
* **Relay**: this grabs content from the PDSs to create a "firehose" of all of the content in all of the PDSs they've looked at (or "crawled", like a search engine)
* **Appviews**: these are the *apps* with which you *view* the content of the Relay. Different apps therefore show different views of the same firehose. Bluesky is an appview. Others exist.

**2 More Things** about:

* **Your PDS** is essentially some storage space on a computer somewhere connected to the internet. The 2 things you need to know:
	* if you sign up for Bluesky using the Bluesky app, the Bluesky company gives you a PDS, but you can move it elsewhere and *you'll keep all your content*, and *all links to it will still work* 
	* *Everything on your PDS is public!* (Bluesky's DMs are not handled in the above way)
	* [learn more about PDSs.](https://atproto.wiki/en/wiki/reference/core-architecture/pds)
* **Relays**: in Bluesky's early days there was only one Relay, run by the Bluesky company, leading some people to believe that Bluesky "*wasn't really centralised*". The 2 things you need to know:
	* in 2025 other people started setting up Relays, because there's nothing stopping them and everything's open-source.
	* not all Relays are global - you can create a Relay just for you and your friends if you like - and any user can grab content from multiple Relays.
	* [learn more about Relays](https://atproto.wiki/en/wiki/reference/core-architecture/relay) and [firehoses](https://atproto.wiki/en/wiki/reference/networking/firehose)
* **Appviews**: 
	* The first two appviews launched were Bluesky and Whitewind, a blogging platform. 
	* Each appview uses a **Lexicon** to define what content it displays, and how it displays it. Bluesky therefore only looks for content structured using the Bluesky Lexicon, and so doesn't show its users Whitewind blog posts, and vice versa. 
	* learn more about [Appviews](https://atproto.wiki/en/wiki/reference/core-architecture/appview) and [Lexicons](https://atproto.wiki/en/wiki/reference/lexicons).

---

## Thermosphere view

**In the thermosphere you're still in orbit, but you're beginning to encounter some atmosphere. From this distance, a couple more details come into view:**

### 1) Users and their accounts

![[strato-did.drawio.png]]

* **A user** typing a post into an appview and hitting Publish. This stores the content in his/her PDS, from which it will be scooped up by the relay and shared with the world 
* **DID**: the user's account is a Decentralised Identifier (DID) - a file which *in this case* is stored on the user's PDS. Other options are possible.

**2 More Things** about:

* DIDs are central to keeping the user in control of their digital life in ATproto. You can use the same account in all appviews, move it wherever you want, and change your handle (your user-friendly name) - you won't lose your friends
* ATproto supports two methods for creating DIDs: "DID:PLC" (for Public Ledger of Credentials - see below) and "DID:web". Both are official standards, but the PLC method is more widely used 
* learn more about [DID](https://atproto.wiki/en/wiki/reference/identifiers/did)


### 2) PLC Directory

*(sidenote PLC Directory: I am now at the very edge of my understanding. Please be tolerant and correct my mistakes gently :) )*

The view from the stratosphere also shows us a new component, required for global search:

![[strato-did-all.drawio.png]]

* the **PLC Directory** (technically "DID:PLC Directory") allows appviews to find users and their content;
* In the image, someone using an Appview is searching for a user via "user search" - they'll find it thanks to the PLC Directory.

**2 More Things about PLC Directory**:

* The PLC Directory may be simple and low-cost tech, but it's absolutely *central* to allowing Bluesky and all other appviews to create a global conversation. 
* I use the word "central" deliberately - the PLC Directory is currently (May 2025) run by the Bluesky *company* (Bluesky Social PBC, which is frequently cited as evidence that Bluesky *the app* is not completely decentralised. Plans are afoot to spin it off as a separate entity, perhaps managed by multiple organisations as a public good. 
* learn more about [PLC Directory](https://web.plc.directory/)

---

## Mesosphere: Feed generators and labellers

**As you get deeper into the atmosphere, more details start appearing.**

![[meso.drawio.png]]

In the above diagram, two tools take content from the Relay and provide their outputs to appviews. Both are designed to put control of moderation in users' hands, and are independent of Bluesky:

* **feed generators**: as their name implies, these create **custom feeds**. Each is a subset of the Bluesky firehose, tuned to a particular community's interests and moderation preferences. They're infinite in number, as anyone can create one, and anyone can use any feed by simply “pinning” it.
* **labellers**: as the name implies, these apply labels to posts and/or accounts. Like custom feeds, anyone can create one, using a variety of tools, and anyone can subscribe to one if they want to see the label.

**2 More Things** about:

* **feed generators:** 
	* custom feeds are created using 3rd party tools (**custom feed builders**), and anyone can make one of _them_, too. Popular options so far include [Skyfeed](https://skyfeed.app/), [Bluesky Feed Creator](https://blueskyfeedcreator.com/) and [graze.social](http://graze.social/), which has a business model allowing feed editors to make money. The competition between builders means custom feeds themselves are only going to get more powerful.
	* custom feeds can also be bundled in Starter Packs, helping create a porous community within the global Bluesky conversation.
	* more about Feed Generators
* **labellers**: 
	* Like custom feeds, anyone can create a labeller, and anyone can subscribe to one if they want to see the label. ***And some custom feed generators then allow you to use labels to create a custom feed.***
		* [ ] to check!
	* **Block/mute lists** are a special type of labeller - subscribing to them means you trust the labeller's judgement that their list of people is composed of people you want to block or mute.
	* learn more about [labellers](https://atproto.wiki/en/wiki/reference/opinionated-services/labelers) and [labels](https://atproto.wiki/en/wiki/reference/opinionated-services/labels); for more on block/mute lists, start with MacKuba's [Safety & moderation](https://mackuba.eu/2024/02/21/bluesky-guide?utm_source=pocket_shared#safety) 

Principle source:  [Three things you probably didn't know about Bluesky](https://myhub.ai/items/three-things-you-probably-didnt-know-about-bluesky)"


---

## What should come next? (up to here)

*(sidenote Next: in this section I bullet-point the other concepts and terms which (I currently think) need to be introduced at higher and higher resolutions. I'm still reading the documentation - ie, I'm on a learning curve as I write - so currently I haven't proposed an order of treatment, or how they can be grouped. If you have any ideas, I'll see you on Discord.)*

* cryptographic signing of content, other cryptographic stuff
* CIDs
* AI URIs
* Blobs
* Records
* Record keys 
* Timestamp identifiers
* Namespaced identifiers
* opinionated services:
	* verifiers?
* Ozone
* from Bluesky to ATmosphere
* Oauth
* App passwords


---

## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version: 
	- rejigged the atmospheric layers, for the first time but surely not the last
	- added the mesopshere: feed generators and labellers, following some useful inputs from [Boris and Fry69 on Discord](https://discord.com/channels/1097580399187738645/1288609400432627816/1371870302719443035) 
- version control
    - this is version: 2
    - this is the current version: [[intro to atproto]]
    - here is the previous version: [[intro to atproto 1]]