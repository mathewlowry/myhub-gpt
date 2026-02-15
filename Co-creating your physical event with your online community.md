**Revisiting some basic principles I've developed over the years in the light of the Atmosphere's potential.**

*(Notes: This is an early draft. As explained in [this newsletter edition](https://mathewlowry.medium.com/exploring-ai4communities-newsletter-6365b2716bb1), I am publishing these early versions as I develop my thoughts in the hope that constructive comments will help me finish the post. More version control in the footer.)*

I built the very first online community of practise for the European Commission in 2002 (and [blogged about it in 2009](https://myhub.ai/items/building-communities-with-event-in-a-box)). I discovered, almost by accident, that this technique helps you use your event to build your online community, and use your online community to build a better event.

These and other online communities were to be my bread and butter for the following ~10 years, and then started dying off as the conversation moved to Twitter and Facebook. The problem was that Twitter and Facebook didn't share, and took the oxygen out of these web-based online communities.

> Twitter and Facebook didn't share... But the situation is now changing

But the situation is now changing, as I argued last November in Berlin: the ATProtocol means "[social media can support, not undermine, online communities](https://mathewlowry.medium.com/how-newsrooms-scientific-institutions-governments-can-best-use-bluesky-ee97d840a058)), because we can integrate our website-based online communities with global social media networks.

Where my Berlin presentation focused on magnifying online communities with custom feeds, however, I want to start exploring how technologies like standard.site and Bluesky can help you **use event co-creation to build a community around your event, and build your event to serve your community**. 

I'm actually exploring this in practice in the run-up to the atproto.science event at the end of March. So if you're coming to the Atmosphere Conference in Vancouver, let me know and we'll compare notes.
## Event co-creation in brief

Event co-creation means involving your community in the definition of the event's content. Members' involvement can take several forms:

- submitting formal proposals for workshops, individual speeches, networking sessions, etc.
- commenting on “provisional” Sessions, Speeches and Exhibits to help the Organisers identify which have generated the most interest
- networking amongst proposers to combine ideas

### Key milestones

**The trick is to get started early.** A good process for an event held at T=0 looks something like this: 

* T-6 months: launch your event website with the simple "save the date," follow us on social, and subscribe to the newsletter messages, so that you can then follow up with your followers and subscribers for...
* T-5 months: launch your open call - in a traditional event co-creation process, users describe themselves as they join your community so that they can propose ideas for the event programme (workshops, speeches, papers, presentations, networking sessions, etc. - it's up to you)
	* If you already have a community then your existing members should be able to simply compose and submit the proposal.
	* while those who have not yet joined your community now have a very good reason to do so.
	* In both cases it helps enormously if your members are submitting ideas directly into your website content management system, not some separate system (online polling tools,  Google Sheets, etc.)
* T - 4 months. Close the call and read the proposals:
	* Mark the bad ones as rejected and inform their authors.
	* Mark the others as provisional. Importantly, there should be more provisional ideas than you actually have room and time for.
* T-minus 3.5 months: publish the Provisional Programme, thus opening the **event co-creation discussion phase**
	* invite your community members to comment and rate the ideas
	* Encourage people with similar ideas to combine forces.
* T-2 months: close the event co-creation discussion phase by publishing the final programme - basically this means 
	* Rejecting some more ideas, and informing the authors
	* Changing the status of the others from provisional to final.
* T-2 - event: continue to encourage the conversation around the final programme.

Of course you don't need to follow those dates exactly, but it is important that people know what the final programme is one or two months before the event so they can make the logistics arrangements. For the original events I helped organise 25 years ago, in fact, we launched the event website 8-9 months before the event because we had several phases of discussion:

* We first had a call for the conference programme where we asked people to submit ideas for workshops or individual presentations
* And when we finalised that programme we opened a second event co-creation phase: the networking session. The people who didn't "make the cut" for the conference programme were encouraged to present ideas for a programme of networking events, which took place in and around the exhibition. 

The last time I was involved we had over 8,000 comments on the provisional networking programme in the month of August, 2026.
### Co-creation benefits

This does much more than help you identify the most interesting Submissions - **it is where Members discover other Members with similar interests, and encourages them to network before they meet face to face**. 

This makes the event more valuable to each Member, and also turns each member into an ambassador. Being selected for the provisional programme, after all, is a very good reason to promote the event to all of your friends so they can upvote it.

In this way by the time people actually meet face-to-face, they will have been discussing the event content for the preceding months - **they will know exactly Who they want to meet, and What they're going to talk about** (as well as When and Where, thanks to the messaging system we also built into the site).
## Why look to the Atmosphere?

I've built websites with event co-creation built in several times since 2002, but in every case all of the interactivity was built into the website's content management system, which was as a result pretty complex.

Today I'm exploring if and how the website could integrate atproto to both simplify the CMS and integrate event co-creation into the global social media conversation, ensuring better engagement. 

But wouldn't this also restrict that conversation to people who have an **ATProto digital identity (DID**; in most cases a Bluesky account)? 
### Identity crisis?

**What if, when somebody joins your community and doesn't have a DID, you simply gave them one as part of their account creation process?** 

From their perspective, they're creating an account on your website so that they can get involved in your event. But you're actually giving them a digital identity they can use on your website *and every other ATProto app on the Atmosphere*, from BlueSky through to Stream.Place. 

Essentially this means that you provide a PDS for any members who don't already have a DID. This is therefore for organisations who have decided to integrate their online operations - both website and social media - with the Atmosphere.
### Benefits 

The first, obvious benefit is **personal sovereignty** - your users store their content on their Personal Data Server (PDS; either the one they already had, or the one you're providing them), which means they maintain ownership over it. You don't own them, so treat them well.

The other main benefit, of course, is **engagement reach**: your event content can become an integral part of the Atmosphere, a social network of over 40 million people. We'll explore this in a little more detail later, but essentially I'm hoping to find the following benefits:

* ?
## How?

### Meet the standard

Firstly, note that you probably won't need to publish every single page of your website onto the Atmosphere - you simply decide which content types are stored on your users' PDS and published onto your website with a little extra code, called a lexicon.

And that lexicon already exists: **standard.site**. As a developer who discovered it less than 2 weeks before writing this put it:

> "Within a week, my site had actually turned ATProto into a CMS. I could make posts, update them, or delete them, and all the while these updates are broadcasted to a network that anyone could index. It was like an RSS feed that because it met a standard could be aggregated with a single tool." - [Standard.site: the Publishing Gateway](https://stevedylan.dev/posts/standard-site-the-publishing-gateway/) (Steve Dylan)

Steve shows how flexible and extensible the basic standard.site architecture is by adding a new lexicon for comments, so standard.site already allows us to publish content onto the Atmosphere and allow users to comment on it.

So what? A first glimpse of the potential benefits can be seen on sites built using standard.site. One of the creators, for example, is leaflet.pub. It's evolving every day, but as I write this in February 2026:

*  ??*

---

As a result, this content can be both presented on your website and shared and interacted with by people across the Atmosphere. Every member of your site will therefore bring whatever content they contribute to your site to their audiences, so you're turning every member into an ambassador for your event, and by extension your organisation.


### Public data

But this is also where we have to tackle the fact that **everything on the ATmosphere is public**. 



---

## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version: 
	- none, as this is the first 
- version control
    - this is version: 1
    - this is the current version: [[Co-creating your physical event with your online community]]
    - here is the previous version: n/a