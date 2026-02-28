![[event-cocreation-leaflet-reach-v3.png]]
# Event co-creation on the Atmosphere

**Exploring what the ATmosphere offers event co-creation, focusing on what [standard.site](https://standard.site/) offers.**

*(Notes: This is version 4 of this post. As [explained here,](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e) I sometimes publish multiple, evolving versions of "experimental" posts in the hope that constructive comments will help me develop them further. More details and version control in the footer.)*

I built the very first online community of practice for the European Commission in 2002 (and [blogged about it in 2009](https://myhub.ai/items/building-communities-with-event-in-a-box)). I discovered, almost by accident, that **online event co-creation** helps you leverage your event to boost your online community, and use your online community to run a more successful event.

These and other online communities were to be my bread and butter for the following ~10 years. They then started dying off as the conversation moved to Twitter and Facebook, which didn't share, robbing oxygen from these web-based online communities.

> Twitter and Facebook didn't share... But the situation is now changing

But the situation is now changing, as I argued last November in Berlin: the ATProtocol means "[social media can support, not undermine, online communities](https://mathewlowry.medium.com/how-newsrooms-scientific-institutions-governments-can-best-use-bluesky-ee97d840a058)", because we can **integrate our website-based online communities with global social media networks.** This is important because web-based online communities can be designed by anyone for any purpose, whereas X  and Facebook impose the same features, content types, moderation regimes and algorithms on everyone. 

Where my Berlin presentation focused on magnifying online communities with custom feeds, however, I now want to explore what the ATmosphere can contribute to event co-creation. Specifically, I'm looking at [standard.site](https://standard.site/) - an emerging longform publishing ATProtocol lexicon - and (in this version) through the lens of [Leaflet](https://leaflet.pub/), one of the main implementations. Other standard.site implementations may be explored in future versions.

I'm also running a "light" event co-creation experiment for [atproto.science 2026](https://atproto.science/events/atmosphere2026/) - a side event to AtmosphereConf2026 - at the end of March, although mainly so I could get my head around Leaflet, and by extension standard.site.

## What is Event Co-creation?

**Involve your community in defining your event's content.** 

There are many ways of doing this, but the classic method involves 

* asking your community to submit proposals for "event items" (speeches, workshops, etc.),
* publishing some as "provisional" event items (OK'd by a Jury and published for community discussion, not yet in the final programme); 
* stimulating a community conversation on these provisional event items to develop and combine good ideas into better ones
* using these discussions to help select which events make it into the Final programme (ie,. get a room and a time).

At the very least, the event programme matches the needs and interests of the community. But the real magic is that by discussing the event programme beforehand, attendees discover others with similar interests and network online *before* they meet face-to-face. They then arrive at the event knowing exactly *who* they want to meet and *what* they're going to talk about.

> Attendees know exactly *who* they want to meet and *what* they're going to talk about

As set out in the following sub page, this approach can work extremely well - for one event, for example, we received over 8,000 comments in a single month to the networking programme, and that was August in Europe(!).

**→ Dig deeper:** [[Event co-creation at a glance]] provides more detail on the basic idea.

## Into the Atmosphere: key challenges

**Simplify your CMS *and* amplify community engagement *and* content visibility?** 

I've built websites with event co-creation several times since 2002. Each time, all of the interactivity was built into the website's content management system, which was as a result pretty complex.

Today I'm exploring if and how the website could integrate ATProto to both simplify the CMS and integrate event co-creation into the global social media conversation, amplifying engagement. And that means meeting two challenges.
### Identity Crisis?

**What about users who don't have a ATProto identity?**

After all, if the basic idea is to push as much of the site interactivity onto the Atmosphere as possible, would that not restrict the conversation to people with an ATProto Digital IDentity (DID; in most cases their Bluesky account)?

That *would* seem to be a problem... unless you simply **gave new users a DID and a Personal Data Server (PDS) - if they don't already have one - as part of their account creation process.** From their perspective, they're creating an account on your website so that they can get involved in your event. But you're actually giving them:

* a digital identity they can use on your website *and every other ATProto app on the Atmosphere*, from BlueSky through to Stream.Place
* and a PDS to store their content, which they can move elsewhere whenever they want (I [moved mine from Bluesky Social's to Eurosky's](https://bsky.app/profile/did:plc:2zxlmj2dvub7smpul2lvwqfk/post/3meok4klrgs22) earlier this year).

This is therefore best for organisations who have decided to integrate ATproto into both their website and social media presence. They should never have been separated. Pursuing this strategy brings two clear benefits:

* **personal sovereignty** - your users store their content on their PDS (either the one they already had, or the one you provide), which means they maintain ownership over it. As they know they can't suffer "social lockin" on your site, they know you'll have to treat them well, which should encourage them to join. 
* **engagement reach**: your event content can become an integral part of the Atmosphere, a social network of over 40 million people with an incredibly active app development ecosystem (see [[There is no do everything app|Building energy in the Atmosphere]]). We'll explore how this looks below.
### Meet the Standard

**What does this mean for your CMS?**

Moreover, you *won't* need to publish every single page of your website onto the Atmosphere - you simply decide which content is published using an ATproto lexicon.

That sounds challenging, until you realise that the technology already exists and is in use on multiple sites: **standard.site**. As a developer who discovered it less than 2 weeks before writing this put it:

> "Within a week, my site had actually turned ATProto into a CMS. I could make posts, update them, or delete them, and all the while these updates are broadcasted to a network that anyone could index" - [Standard.site: the Publishing Gateway](https://stevedylan.dev/posts/standard-site-the-publishing-gateway/) (Steve Dylan)

Steve shows how flexible and extensible the basic standard.site architecture is by adding a new lexicon for comments. Other developers have done something similar (eg [First thoughts on integrating with standard.site](https://isaaccorbrey.com/ramblings/first-thoughts-on-integrating-with-standard-site)).

### Handling Public Data

**But isn't everything on the Atmosphere public?**

Yes, although in Vancouver I look forward to hearing a lot more about [permissioned data](https://myhub.ai/@mathewlowry/?tags=permissioned+data), which should unlock massive new opportunities for communities within the Atmosphere.

In the previous version of this post, I assumed that *submitted* event items must be stored only in the website CMS, where the event jury can see them. When they give one provisional status, it would be pushed to the users' PDS and published from there onto the website for the community to discuss.

It was [Emelia](https://bsky.app/profile/thisismissem.social) who suggested a far cleaner approach: 

* the event website runs a **labeller** — a lightweight ATProto service — that publishes status changes as protocol-level labels attached to each event item. 
* the website displays only event items with provisional or approved labels.

In fact, according to Emelia, a CMS is really not needed at all: event co-creation could simply be supported purely by an Atmosphere app. But event co-creation is best embedded within a much larger community strategy, and besides I have to leave something for version 5 of this post ;)
## Benefits: better reach with a simpler website 

**In this version of this post, I've only explored how this could look using the features offered by the [leaflet.pub ](http://leaflet.pub/)implementation of standard.site. They are considerable.** 

Sub-pages covering other implementations will follow if/when I find the time, but for now check out [[Event co-creation using Leaflet]] to better understand this image:

![[event-cocreation-leaflet-reach-v4.png]]

Briefly, the above image shows how an event item in your website's provisional programme is created, labelled and published using standard.site, and connected to users across the Atmosphere via:

- multiple standard.site and Bluesky apps
- the social graph of the event items' original author 
- the social graph of anyone who comments on it on the website, or shares it to Bluesky
- the event's custom feed.

Moreover, your audience can easily subscribe to only those event items that interest them, following them via either Bluesky or any standard.site app.

So getting better reach for the conversations on your website becomes easier while your website itself becomes massively simpler. All because you're farming out most of the interactive features to the Atmosphere.

**→ Dig deeper:** [[Event co-creation using Leaflet]].

## First tests

To ground this exploration, I'm running an experiment for [ATProto.science 2026](https://atproto.science/events/atmosphere2026/) (Vancouver, March 2026), testing whether Leaflet and Bluesky can support pre-event conversations about the programme. [Ariel Lighty](https://www.linkedin.com/in/ariel-lighty/) and I have published the successful proposals as Leaflet subpages, and speakers are now invited to flesh out their ideas and provoke conversations using leaflet's features.

Limitations are already clear - notably around notification routing and cross-platform mentions - but even minimal interaction will teach me how Leaflet and standard.site work in practice, directly relevant to my workshop: **Your research institution in the Atmosphere**.

**→ Dig deeper:** [[Exploring event co-creation at atroto.science 2026]]


---

## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version: (2026-02-21)
	- introduction of labeller
- version control
    - this is version: 4
    - this is the current version: [[Co-creating your physical event with your online community]]
    - here is the previous version: [[Co-creating your physical event with your online community 3]]