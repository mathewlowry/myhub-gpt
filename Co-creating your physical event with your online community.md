
# Event co-creation on the Atmosphere

**Exploring what the ATmosphere offers event co-creation, focusing on what [standard.site](https://standard.site/) offers.**

*(Notes: This is version 3 of this post. As [explained here,](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e) I sometimes publish multiple, evolving versions of "experimental" posts in the hope that constructive comments will help me develop them further. More details and version control in the footer.)*

I built the very first online community of practice for the European Commission in 2002 (and [blogged about it in 2009](https://myhub.ai/items/building-communities-with-event-in-a-box)). I discovered, almost by accident, that **online event co-creation** helps you leverage your event to boost your online community, and use your online community to run a more successful event.

These and other online communities were to be my bread and butter for the following ~10 years, and then started dying off as the conversation moved to Twitter and Facebook. The problem was that Twitter and Facebook didn't share, and took the oxygen out of these web-based online communities.

> Twitter and Facebook didn't share... But the situation is now changing

But the situation is now changing, as I argued last November in Berlin: the ATProtocol means "[social media can support, not undermine, online communities](https://mathewlowry.medium.com/how-newsrooms-scientific-institutions-governments-can-best-use-bluesky-ee97d840a058)", because we can **integrate our website-based online communities with global social media networks.**

Where my Berlin presentation focused on magnifying online communities with custom feeds, however, I now want to explore what the ATmosphere can contribute to event co-creation. Specifically, I'm looking at [standard.site](https://standard.site/) - an emerging longform publishing ATProtocol lexicon - and (in this version) through the lens of [Leaflet](https://leaflet.pub/), one of the main implementations. Other standard.site implementations may be explored in future versions.

To ground this exploration, I'm running an experiment for [atproto.science 2026](https://atproto.science/events/atmosphere2026/) - a side event to AtmosphereConf2026 - at the end of March.

## What is Event Co-creation?

Event co-creation means involving your community in defining the event's content. There are many ways of doing this, but the classic method involves asking your community to submit proposals for "event items" (speeches, workshops, etc.), and then comment on "provisional" event items (published for community discussion, not yet in the final programme) and work with others' ideas to combine good ideas into better ones. 

The real magic is that by discussing content beforehand, attendees discover others with similar interests and network online *before* they meet face-to-face. Attendees arrive at the event knowing exactly *who* they want to meet and *what* they're going to talk about.

> Attendees know exactly *who* they want to meet and *what* they're going to talk about

A good process starts 6 months or more before the event, so the key is to start early. As set out in the following sub page, this approach can work extremely well - for one event, for example, we received over 8,000 comments in a single month to the networking programme, and that was August in Europe(!).

**→ Read more:** [[Event co-creation at a glance]] provides more detail on the basic idea.

## Key challenges

**How to simplify your CMS and amplify community engagement *and* content visibility in one step.** 

I've built websites with event co-creation several times since 2002. Each time, all of the interactivity was built into the website's content management system, which was as a result pretty complex.

Today I'm exploring if and how the website could integrate ATProto to both simplify the CMS and integrate event co-creation into the global social media conversation, amplifying engagement. An that means meeting two challenges.
### Identity Crisis?

**What about users who don't have a ATProto identity?**

After all, if the basic idea is to push as much of the site interactivity onto the Atmosphere as possible, would that not restrict the conversation to people with an ATProto Digital IDentity (DID; in most cases their Bluesky account)?

That *would* seem to be a problem... unless you simply **gave new users a DID and a Personal Data Server (PDS) - if they don't already have one - as part of their account creation process.** From their perspective, they're creating an account on your website so that they can get involved in your event. But you're actually giving them:

* a digital identity they can use on your website *and every other ATProto app on the Atmosphere*, from BlueSky through to Stream.Place
* and a PDS to store their content, which they can move elsewhere whenever they want (I [moved mine from Bluesky Social's to Eurosky's](https://bsky.app/profile/did:plc:2zxlmj2dvub7smpul2lvwqfk/post/3meok4klrgs22) earlier this year.

This is therefore best for organisations who have decided to integrate ATproto into both their website and social media presence. They should never have been separated. Pursuing this strategy brings two clear benefits:

* **personal sovereignty** - your users store their content on their PDS (either the one they already had, or the one you're providing them), which means they maintain ownership over it. Chances are more users will join your community if they know that as you can't own them, you have to treat them well. 
* **engagement reach**: your event content can become an integral part of the Atmosphere, a social network of over 40 million people with a quite incredibly active app development ecosystem (see [[There is no do everything app|Building energy in the Atmosphere]]). We'll explore how this looks below.
### Meet the Standard

**What does this mean for your CMS?**

You *won't* need to publish every single page of your website onto the Atmosphere - you simply decide which content types are stored on your users' PDSs and published onto your website with a little extra code, called a lexicon.

That sounds challenging, until you realise that the required lexicons already exists and are in use on multiple sites: **standard.site**. As a developer who discovered it less than 2 weeks before writing this put it:

> "Within a week, my site had actually turned ATProto into a CMS. I could make posts, update them, or delete them, and all the while these updates are broadcasted to a network that anyone could index" - [Standard.site: the Publishing Gateway](https://stevedylan.dev/posts/standard-site-the-publishing-gateway/) (Steve Dylan)

Steve shows how flexible and extensible the basic standard.site architecture is by adding a new lexicon for comments. Other developers have done something similar (eg [First thoughts on integrating with standard.site](https://isaaccorbrey.com/ramblings/first-thoughts-on-integrating-with-standard-site)).

### Handling Public Data

**Finally, we must tackle the fact that everything on the Atmosphere is public (for now).**

In Vancouver I look forward to hearing about the development of [permissioned data](https://myhub.ai/@mathewlowry/?tags=permissioned+data), but for this version of this post I'm operating on the assumption that *submitted* event items must be stored only in the website CMS. 

When they have been given provisional status by the Organisers, however:

* they are displayed to anonymous website users
* standard.site records are pushed to the users' PDS to ensure the event item is on the Atmosphere.

## Benefits: better reach with a simpler website 

**In this version of this post, I've only explored how this could look using the features offered by the [leaflet.pub ](http://leaflet.pub/)implementation of standard.site. They are considerable.** 

Sub-pages covering other implementations will follow if/when I find the time, but for now check out [[Event co-creation using Leaflet]] to better understand this image:

![[event-cocreation-leflet.png]]

Briefly, the above image shows how an event item in your website's provisional programme is created and published using standard.site, and connected to users across the Atmosphere via:

- multiple standard.site and Bluesky apps
- the social graph of the event items' original author 
- the social graph of anyone who comments on it on the website, or shares it to Bluesky
- the event's custom feed.

Moreover, your audience can easily subscribe to only those event items that interest them, following them via either Bluesky or any standard.site app.

So getting better reach for the conversations on your website becomes easier while your website itself becomes massively simpler. All because you're farming out most of the interactive features to the Atmosphere.

Read more in [[Event co-creation using Leaflet]].

## First tests

To ground this exploration, I'm running an experiment for [ATProto.science 2026](https://atproto2026.leaflet.pub/3mevfbw7r522w) (Vancouver, March 2026), testing whether Leaflet and Bluesky can support pre-event conversations about the programme. With help from [Ariel Lighty](https://www.linkedin.com/in/ariel-lighty/), we've published the successful proposals as Leaflet subpages, and will invite speakers to flesh out their ideas and provoke conversations.

Limitations are already clear - notably around notification routing and cross-platform mentions - but even minimal interaction will teach me how Leaflet and standard.site work in practice, directly relevant to my workshop: [Coopetition in the ATmosphere](https://leaflet.pub/7c7be6b7-1dbc-4aae-8f32-f5314aa99f90?page=019c60e7-6d9d-7773-a1b3-6521afff8f21).

**→ Read more:** [[Exploring event co-creation at atroto.science 2026]]


---

## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version: (2026-02-21)
	- Assisted by Claude Code (see [[v3 revision notes]]), I took the very long version 2 (below) and split it into four files
- version control
    - this is version: 3
    - this is the current version: [[Co-creating your physical event with your online community]]
    - here is the previous version: [[Co-creating your physical event with your online community 2]]