---
tags:
  - status/draft
  - type/blog
  - topic/adoption
  - topic/standard-site
  - audience/institutions
  - audience/general
---

# Powerful communities from simple ATmosphere sites

**Integrating ATProtocol with your website:
* **lets you build powerful, interactive online communities with very simple code** 
* **while giving you in-built reach to 40+m users across the Atmosphere** 
* **and allowing your members to own and manage their own data.** 

It's a triple-win, it sounds too good to be true, but it just might be the future.

*(Note: This is an early draft. As explained in [this newsletter edition](https://mathewlowry.medium.com/exploring-ai4communities-newsletter-6365b2716bb1), I publish versions of certain posts as I develop my thoughts. More version control in the footer.)*

## Problem statement

Building a successful community on your own website has always been worthwhile, but it's a challenge:

* you need rich interactivity — discussion threads, notifications, user profiles, status updates — so you need an expensive, complex content management system, 
* but you also have to figure out extremely good and credible reasons why your users should sign up and get involved - after all it's not as if there's nowhere else to spend their online time.

Squaring that circle was my stock in trade for the first 12 years of the century, but then almost everyone gave up and outsourced their community to Facebook or Twitter, as that's where their users - and their conversations - went. As I [pointed out in 2019](https://mathewlowry.medium.com/from-ep2009-to-ep2019-a-lost-decade-ccba4205ebbc), my employers "*could have chosen a different path, and not entirely subcontracted the conversation about Europe’s future to US-owned, Russian-manipulated, profit-driven social media platforms*", but in fairness [almost everyone else made the same mistake](https://www.techdirt.com/2026/02/03/whoops-websites-realize-that-killing-their-comment-sections-was-a-mistake/).

But it *was* a mistake - I don't think anyone I know still thinks it's a good idea to send European citizens to Facebook and X for a nuanced, useful conversation about European policies and programmes. Quite apart from the inbuilt toxicity of US big tech, you are completely dependent on platforms which can change their features and algorithms at any time.

The ATProtocol, originally developed by Bluesky but now used by dozens of new, inter-operable and user-first apps - offers a way out, **allowing you to build a powerful community with in-built reach while massively simplifying your website code.**

## Exploring alternatives

In 2002 I built the European Commission's very first online community using event co-creation, where we convened a community to help us define a three-day European research conference programme (I [blogged about it in 2009](https://myhub.ai/items/building-communities-with-event-in-a-box)). Over 20 years later, as I prepared a workshop for the ATScience.proto conference in Vancouver at the end of this month, I thought I'd revisit event co-creation using Atmosphere tools like Bluesky and Leaflet.

I wrote up what I found in a 4-part post here: [Event co-creation on the Atmosphere](https://experiments.myhub.ai/co-creating_your_physical_event_with_your_online_community). Check it out if you like detail, but the most important finding is simple: **integrating ATProtocol doesn't add complexity — it removes it,** as you shift interactivity onto Atmosphere apps and user management onto the users themselves. Your CMS is left doing what a CMS is actually for: managing your content. The Atmosphere handles the community.
## Benefits at a glance

This brings two principle simplification benefits 

* You don't need to design and build systems for commenting, messaging, curation, notification and subscription - the apps you integrate take care of that for you
* data privacy issues become extremely simple, as users manage their content on their Personal Data Server (PDS) at all times.

Moreover, you automatically tap your user's social graphs on the Atmosphere whenever they use any of the apps - every member of your community becomes an ambassador for it. 
## Innovations involved

There are some innovations required - you'll need to: 

* provide users with an ATproto identity and Personal Data Server (PDS), if they don't already have one (the good news is that they will be able to use that identity in every app on the Atmosphere, not just those you use for your online community)
* connect your website to a labeller to manage where the content stored on your users' PDSs is displayed on your website
* add your members' IDs to a List to drive the event's custom feed.

In the event co-creation use case I explored, for example:

* members submit "looseleaf Leaflets" (one of several Atmosphere publishing tools using the shared "standard.site" technology) to describe their workshop idea
* the conference selection jury uses the labeller to classify them as Submitted, Rejected, Provisional or Final 
* the website displays Submitted proposals to the selection jury only, and Provisional and Final proposals to all website visitors
* any Bluesky post from a Member with the event hashtag appears in the event's Custom Feed.

Because Leaflet is deeply integrated into Bluesky, the features and reach generated by this approach is impressive, particularly compared to the event website's simplicity: the following figure shows how a proposed workshop idea, provisionally accepted by the event Jury to allow the community to discuss it, is "*connected to users across the Atmosphere via:*

* *multiple standard.site and Bluesky apps,* 
* *the social graph of the original author,* 
* *the social graph of anyone who comments on it on the website, or shares it to Bluesky,* 
* *and the event's custom feed".*

![[https://experiments.myhub.ai/permanent_versions/focus-reach-v4.png]]

Not shown: members can 
* comment on the workshop idea without you building a commenting systems
* discover all Bluesky conversations without you needing a tracking system
- subscribe to only those event items and conversations that interest them without you buiding a notification system or enewsletter.

Event co-creation, of course, is just one example: there are many more use cases, and there are also many Atmosphere apps which I haven't investigated yet. In Vancouver I'm hoping to investigate how curation tools like Semble and sidewiki-style commenting systems like Margin could support different community use cases, as well as discover new apps currently being developed.

## Resilience

The result is a site that is not only simpler to build and richer to use, it is also resilient: while you are using other people's apps, these are not walled gardens, so if they drop a feature you're relying on, you can always rebuild it, and still access the underlying content, living on your members' PDSs.

The resilience extends beyond your website's interactive features. When you build community on Facebook or Twitter, you are building on someone else's land with someone else's rules. Your users' contributions, their networks, their content — all of it is effectively on loan to you, intermediated by a platform whose interests are not yours, or of your members.

ATProtocol reverses this. Users store their content on infrastructure they control. They can move PDS providers without losing their identity or their history. They cannot be socially locked in, which means they join your community on terms they understand and can trust. That trust is the foundation of any genuine community.

For European institutions, science organisations, and anyone else with good reasons to be wary of dependency on US platforms, this is not a marginal technical advantage. It is a credible alternative architecture for community-building — one that is becoming more capable and more practical every month.

The question is no longer whether you can build serious community infrastructure on the open protocol. The event co-creation example shows you can. The question is who starts building first.

---

## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version: (2026-03-04)
	- none, as this is the first 
- version control
    - this is version: 1
    - this is the current version: [[Simple sites powerful communities - the ATmosphere pattern]]
    - here is the previous version: n/a